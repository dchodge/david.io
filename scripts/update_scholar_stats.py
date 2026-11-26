"""Refresh citations and h-index in content/home/stats.md from your public Google Scholar profile.

  python3 scripts/update_scholar_stats.py            # dry run: show the new numbers
  python3 scripts/update_scholar_stats.py --apply    # write them to stats.md

Reads the profile URL from `scholar_url` in content/home/stats.md. Google Scholar has no API and
sometimes answers automated requests with a CAPTCHA; if that happens the script changes nothing and
you can retry later or update the numbers by hand. Run it occasionally (e.g. monthly), not on a loop.
"""
import datetime, os, re, ssl, sys, urllib.request

STATS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "content", "home", "stats.md")
APPLY = "--apply" in sys.argv

CTX = ssl.create_default_context()
if os.path.exists("/etc/ssl/cert.pem"):          # python.org builds on macOS lack root certs
    CTX.load_verify_locations("/etc/ssl/cert.pem")

text = open(STATS).read()
m = re.search(r'^scholar_url\s*=\s*"([^"]+)"', text, flags=re.M)
if not m:
    sys.exit("No scholar_url in stats.md")
url = m.group(1)

req = urllib.request.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
    "Accept-Language": "en",
})
try:
    page = urllib.request.urlopen(req, timeout=20, context=CTX).read().decode("utf-8", "replace")
except Exception as e:
    sys.exit(f"Could not fetch Scholar profile: {e}")

# The stats table: All / Since-year columns for Citations, h-index, i10-index
cells = re.findall(r'class="gsc_rsb_std">(\d+)<', page)
if len(cells) < 4:
    sys.exit("Scholar did not return the citation table (possibly a CAPTCHA). Nothing changed.")
citations, h_index = int(cells[0]), int(cells[2])
when = datetime.date.today().strftime("%B %Y")

old_c = re.search(r'^citations\s*=\s*(\d+)', text, flags=re.M)
old_h = re.search(r'^h_index\s*=\s*(\d+)', text, flags=re.M)
print(f"citations: {old_c.group(1) if old_c else '?'} -> {citations}")
print(f"h-index:   {old_h.group(1) if old_h else '?'} -> {h_index}")
print(f"as of:     {when}")

new = re.sub(r'^citations\s*=\s*\d+', f"citations = {citations}", text, count=1, flags=re.M)
new = re.sub(r'^h_index\s*=\s*\d+', f"h_index = {h_index}", new, count=1, flags=re.M)
new = re.sub(r'^stats_date\s*=\s*"[^"]*"', f'stats_date = "{when}"', new, count=1, flags=re.M)
# the "Citations / h-index" row in the stat sheet
new = re.sub(r'(label = "Citations / h-index"\n\s*value = ")[^"]*(")', rf"\g<1>{citations} / {h_index}\g<2>", new, count=1)

if APPLY:
    open(STATS, "w").write(new)
    print("stats.md updated")
else:
    print("dry run; use --apply to write")
