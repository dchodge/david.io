"""Fill in missing abstracts and exact publication dates for content/publication/* from their DOIs.

Sources: Europe PMC (abstracts) and Crossref (dates, fallback abstracts). Both are free, keyless APIs.

  python3 scripts/update_publications.py            # dry run: show what would change
  python3 scripts/update_publications.py --apply    # write changes

Rules:
  * abstract is only written when the entry's abstract is empty ("" or missing)
  * date/publishDate are only replaced when the current date is a 1 January placeholder
"""
import html, json, os, re, ssl, sys, time, urllib.parse, urllib.request

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "publication")
UA = {"User-Agent": "hugo-site-publication-updater/1.0 (personal academic website)"}
APPLY = "--apply" in sys.argv


# python.org builds on macOS ship without root certificates; also trust the system bundle.
CTX = ssl.create_default_context()
if os.path.exists("/etc/ssl/cert.pem"):
    CTX.load_verify_locations("/etc/ssl/cert.pem")


def get_json(url):
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=20, context=CTX) as r:
            return json.load(r)
    except Exception as e:  # network errors, 404s for unregistered DOIs, etc.
        return {"_error": str(e)}


def clean(text):
    text = re.sub(r"<jats:title>.*?</jats:title>", " ", text or "", flags=re.S)
    # structured-abstract headings -> bold labels, e.g. "**Methods.**"
    text = re.sub(r"<h\d[^>]*>\s*(.*?)\s*</h\d>", r" **\1.** ", text, flags=re.S)
    # strip only real tags (a letter right after "<"), so "aged <5 years" survives;
    # inline formatting tags vanish without leaving a space
    text = re.sub(r"</?(?:jats:)?(?:i|b|em|strong|sup|sub|italic|bold|span)\b[^<>]*>", "", text)
    text = re.sub(r"</?(?:jats:)?[A-Za-z][^<>]*>", " ", text)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    return re.sub(r"^\**Abstract\.?\**\s*", "", text)


def norm_doi(doi):
    return re.sub(r"^https?://(dx\.)?doi\.org/", "", doi.strip().strip('"')).strip()


def crossref(doi):
    d = get_json("https://api.crossref.org/works/" + urllib.parse.quote(doi))
    m = d.get("message") or {}
    date = None
    for key in ("published", "published-online", "posted", "issued", "published-print"):
        parts = (m.get(key) or {}).get("date-parts") or [[]]
        if parts and len(parts[0]) == 3:
            date = "%04d-%02d-%02d" % tuple(parts[0])
            break
    return date, clean(m.get("abstract", ""))


def europepmc(doi):
    q = urllib.parse.quote(f'DOI:"{doi}"')
    d = get_json(f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={q}&resultType=core&format=json")
    res = ((d.get("resultList") or {}).get("result") or [])
    return clean(res[0].get("abstractText", "")) if res else ""


def front_matter(text):
    m = re.match(r"---\n(.*?)\n---\n?", text, flags=re.S)
    return m.group(1) if m else ""


def abstract_is_empty(fm):
    m = re.search(r'^abstract:(.*)$', fm, flags=re.M)
    if not m:
        return True
    rest = m.group(1).strip()
    return rest in ('""', "''", "")  and not re.search(r'^abstract:\s*[|>]', fm, flags=re.M)


def yaml_block(text):
    words, lines, line = text.split(), [], ""
    for w in words:
        if len(line) + len(w) + 1 > 100:
            lines.append(line)
            line = w
        else:
            line = (line + " " + w).strip()
    if line:
        lines.append(line)
    return "abstract: |\n" + "".join(f"  {l}\n" for l in lines)


changes = 0
for key in sorted(os.listdir(ROOT)):
    path = os.path.join(ROOT, key, "index.md")
    if not os.path.isfile(path):
        continue
    text = open(path).read()
    fm = front_matter(text)
    m = re.search(r'^doi:\s*"?([^"\n]+)"?', fm, flags=re.M)
    if not m:
        print(f"{key:26} no DOI, skipped")
        continue
    doi = norm_doi(m.group(1))
    date, cr_abs = crossref(doi)
    time.sleep(0.3)
    abstract = europepmc(doi) or cr_abs
    time.sleep(0.3)

    notes, new = [], text
    cur = re.search(r'^date:\s*"(\d{4}-\d{2}-\d{2})', fm, flags=re.M)
    if date and cur and cur.group(1).endswith("-01-01") and cur.group(1) != date:
        notes.append(f"date {cur.group(1)} -> {date}")
        new = re.sub(r'^date:\s*".*?"', f'date: "{date}T00:00:00Z"', new, count=1, flags=re.M)
        new = re.sub(r'^publishDate:\s*".*?"', f'publishDate: "{date}T00:00:00Z"', new, count=1, flags=re.M)
    if abstract and abstract_is_empty(fm):
        notes.append(f"abstract added ({len(abstract.split())} words)")
        if re.search(r'^abstract:.*$', new, flags=re.M):
            new = re.sub(r'^abstract:.*\n', lambda _: yaml_block(abstract), new, count=1, flags=re.M)
        else:
            new = new.replace("\n---", "\n" + yaml_block(abstract).rstrip("\n") + "\n---", 1)
    if not notes:
        notes.append("no change" + ("" if (date or abstract) else " (DOI not found)"))
    else:
        changes += 1
        if APPLY:
            open(path, "w").write(new)
    print(f"{key:26} {'; '.join(notes)}")

print(f"\n{changes} entries {'updated' if APPLY else 'would change (dry run; use --apply)'}")
