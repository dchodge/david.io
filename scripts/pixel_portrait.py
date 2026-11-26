"""Hand-placed pixel sprite, 3/4 view facing down-left, painterly shading -> SVG.

Usage: python3 scripts/pixel_portrait.py static/img/pixel-me.svg

Each letter in the grid is one pixel; '.' is transparent. Edit PAL to recolour.
Materials use 3 tones + a darker same-hue outline (no pure black), lit from top-left.
"""
import sys

W = 36
PAL = {
    # skin
    "A": "#f3cfa8", "S": "#dca47e", "s": "#b4775a", "O": "#6e4334",
    # blonde hair
    "Y": "#fbe7a2", "H": "#e3bf62", "h": "#b88f3e", "D": "#6f5226",
    # eyes / face details
    "k": "#2c1f24", "i": "#f6efe6", "M": "#a8783a", "m": "#6a2c2c", "T": "#f8f1e4",
    # linen shirt
    "W": "#f2efe8", "w": "#d4cfcb", "v": "#a9a2a6", "V": "#625c66",
    # gold chain
    "C": "#d6b45e",
    # belt + buckle
    "B": "#4a3329", "G": "#d9b85c",
    # black trousers
    "P": "#4d4d5c", "p": "#363641", "q": "#25252d", "Q": "#121216",
    # shoes
    "N": "#8a5a3e", "n": "#5f3b2a", "Z": "#33201a",
}

def row(left, body):
    r = "." * left + body
    assert len(r) <= W, (len(r), r)
    return r.ljust(W, ".")

R = [
    # --- windswept blonde hair, sweeping up and back ---
    row(17, "DD"),
    row(14, "DDYYD.DD"),
    row(12, "DDYYHHDDHHD.D"),
    row(11, "DYYYHHHHHHHHDHD"),
    row(10, "DYYHHHHHHHHHHHhD"),
    row(10, "DYHHHYHHHHHHHhhD"),
    row(10, "DHHYHHHHHHHHhhhD"),
    row(10, "DHHHHHHHHHHHhhhD"),
    row(10, "DHhHAHhHHHHhhhhD"),
    # --- face: nose points left, ear and back of head to the right ---
    row(10, "O" + "AAAAAAAASS" + "hH" + "hh" + "D"),
    row(10, "O" + "AhhAAhhhSS" + "Ss" + "hh" + "D"),
    row(10, "O" + "AkkASkkkSs" + "sS" + "hh" + "D"),
    row(10, "O" + "AkiASkikSs" + "sS" + "hh" + "D"),
    row(9,  "OA" + "SsSASSSSss" + "sO" + "hh" + "D"),
    row(10, "O" + "MMMMMMSSss" + "O" + "h" + "D"),
    row(10, "O" + "MmTTTTmMSs" + "sO"),
    row(10, "O" + "SSmmmmSSss" + "O"),
    row(11, "OSSSSSSssO"),
    row(12, "OOSSssOO"),
    row(14, "OSssO"),
    # --- linen shirt, open collar with a chain, sloped shoulders ---
    row(10, "VVWWWASSswwvvV"),
    row(8,  "VVWWWWWACsSwwwvvVV"),
    row(7,  "VWWWWWWWWCCwwwwvvvvV"),
    row(7,  "VWWV" + "WWWWWWwwwwvv" + "VvvV"),
    row(7,  "VWwV" + "WWWWWWWwwwvv" + "VvvV"),
    row(7,  "VWwV" + "WWWWWwwwwvvv" + "VvvV"),
    row(7,  "VwwV" + "WWWWWWwwwwvv" + "VvvV"),
    row(7,  "VvvV" + "WWWWWwwwwvvv" + "VVVV"),
    # --- rolled sleeves, forearms ---
    row(7,  "OAsO" + "WWWWWWwwwwvv" + "OSsO"),
    row(7,  "OASO" + "WWWWWwwwwvvv" + "OSsO"),
    row(7,  "OASO" + "WWWWWWwwwwvv" + "OssO"),
    row(7,  "OASO" + "wWWWWwwwwvvv" + "OssO"),
    row(7,  "OASO" + "BBBBBBGBBBBB" + "OsSO"),
    row(7,  "OAsO" + "PPPPPppppqqq" + "OssO"),
    row(7,  "OAAO" + "PPPPPppppqqq" + "OSsO"),
    row(7,  "OSsO" + "PPPPppppqqqq" + "OssO"),
    row(7,  ".OO." + "PPPPPpppqqqq" + ".OO."),
    # --- wide stance: baggy trousers flare at the hip, split into two legs ---
    row(10, "QPPPPPPppppqqQ"),
    row(9,  "QPPPPPPPppppqqqQ"),
    row(9,  "QPPPPPPpppppqqqQ"),
    row(8,  "QPPPPPPPQpppqqqqQ"),
]

def leg_row(segs):
    """segs: list of (x0, width, side, band) -> one 36-wide row of trouser legs."""
    r = ["."] * W
    for x0, w, side, band in segs:
        n = w - 2
        if band:                        # wrapped ankle band
            body = "n" * n
            edge = "Z"
        elif side == "near":            # lit from the left: light, mid, one dark
            lit = max(1, round(n * 0.5))
            body = "P" * lit + "p" * (n - lit - 1) + "q"
            edge = "Q"
        else:                           # far leg sits in shadow
            body = "p" + "q" * (n - 1)
            edge = "Q"
        for i, c in enumerate(edge + body + edge):
            r[x0 + i] = c
    return "".join(r)

# (near x0, near width, far x0, far width): near leg angles down-left, far leg planted down-right
LEGS = [
    (8, 8, 17, 8),
    (7, 8, 18, 8),
    (7, 8, 18, 8),
    (6, 8, 19, 7),
    (6, 8, 19, 7),
    (5, 8, 19, 7),   # knees
    (5, 7, 20, 6),
    (4, 7, 20, 6),
    (4, 7, 20, 6),
    (4, 6, 20, 6),
    (3, 6, 21, 5),
]
for nx, nw, fx, fw in LEGS:
    R.append(leg_row([(nx, nw, "near", False), (fx, fw, "far", False)]))
# wrapped ankles
R.append(leg_row([(3, 6, "near", True), (21, 5, "far", True)]))
R.append(leg_row([(3, 6, "near", True), (21, 6, "far", True)]))
# boots: near foot points down-left, far foot down-right and set a touch higher
R += [
    row(1, "ZZnNNnZ" + "." * 13 + "ZnNNNnZ"),
    row(1, "ZnNNNNNnZ" + "." * 11 + "ZnNNNNnZ"),
    row(1, "ZnNNNNnnZ" + "." * 11 + "ZZZZZZZZ"),
    row(1, "ZZZZZZZZZ"),
]

H = len(R)
PAD_X, PAD_TOP, PAD_BOT = 6, 3, 4
CW, CH = W + 2 * PAD_X, H + PAD_TOP + PAD_BOT

rects = []
# soft isometric ground shadow
gy = PAD_TOP + H - 2
for dy, (x0, x1, op) in enumerate([(4, 30, 0.08), (0, 32, 0.12), (2, 30, 0.08), (7, 25, 0.05)]):
    rects.append(f'<rect x="{x0 + PAD_X}" y="{gy + dy}" width="{x1 - x0}" height="1" fill="#000" opacity="{op}"/>')
for y, r in enumerate(R):
    x = 0
    while x < W:
        c = r[x]
        if c == ".":
            x += 1
            continue
        run = 1
        while x + run < W and r[x + run] == c:
            run += 1
        rects.append(f'<rect x="{x + PAD_X}" y="{y + PAD_TOP}" width="{run}" height="1" fill="{PAL[c]}"/>')
        x += run

svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {CW} {CH}" width="{CW * 10}" height="{CH * 10}" '
       f'shape-rendering="crispEdges" role="img" aria-label="Pixel art portrait of David Hodgson">'
       f'<rect width="{CW}" height="{CH}" fill="#f7f6f3"/>' + "".join(rects) + "</svg>\n")
open(sys.argv[1], "w").write(svg)
print(f"sprite {W}x{H}, canvas {CW}x{CH}")
