#!/usr/bin/env python3
"""Draw the front page for Thursday 26 November 2026 (1024x1024 PNG).

Six stories, all first reported on 26 November 2026:
  1. Houthis say they struck the Ras Tanura refinery, Saudi Arabia.
  2. Tankers burn after hitting mines in the Strait of Hormuz.
  3. North Korea expels Switzerland's envoy from Pyongyang.
  4. Thanksgiving travel gridlock across the United States.
  5. A record day of migrant arrivals in Spain's Canary Islands.
  6. Bangladesh lifts the garment minimum wage by 36%.

Pillow only. Flat vector scenes plus real text, so nothing is garbled.
The output is deterministic: run it twice and the bytes match.
"""
import math
import random

from PIL import Image, ImageDraw, ImageFont

PAGE_W, PAGE_H = 1024, 1024
PAPER = (250, 246, 234)
INK = (20, 32, 60)
NAVY = (15, 30, 62)
CRIMSON = (176, 26, 26)
AMBER = (182, 84, 8)
TEAL = (13, 72, 90)
MUTED = (88, 94, 108)
BODY = (46, 54, 76)
CREAM = (234, 229, 215)

SERIF_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
SANS_REG = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_ITALIC = "/usr/share/fonts/truetype/liberation/LiberationSans-Italic.ttf"


def load(path, size):
    return ImageFont.truetype(path, size)


def shade(top, bottom, box, canvas):
    """Vertical gradient inside box, top colour to bottom colour."""
    x0, y0, x1, y1 = box
    span = max(1, y1 - y0 - 1)
    for yy in range(y0, y1):
        k = (yy - y0) / span
        col = tuple(int(top[i] + (bottom[i] - top[i]) * k) for i in range(3))
        canvas.line([(x0, yy), (x1, yy)], fill=col)


def split_lines(canvas, text, face, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    words = text.split()
    lines, current = [], ""
    for word in words:
        trial = (current + " " + word).strip()
        if canvas.textlength(trial, font=face) <= max_w:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def paragraph(canvas, pos, text, face, colour, max_w, gap=None):
    """Draw wrapped text; return the y just below the last line."""
    x, y = pos
    step = gap or int(face.size * 1.18)
    for line in split_lines(canvas, text, face, max_w):
        canvas.text((x, y), line, font=face, fill=colour)
        y += step
    return y


def starburst(canvas, cx, cy, radius, colour):
    points = []
    for n in range(16):
        ang = math.pi * n / 8
        r = radius if n % 2 == 0 else radius * 0.45
        points.append((cx + math.cos(ang) * r, cy + math.sin(ang) * r))
    canvas.polygon(points, fill=colour)


def disc(canvas, cx, cy, radius, colour):
    canvas.ellipse([cx - radius, cy - radius, cx + radius, cy + radius],
                   fill=colour)


def rooftops(canvas, x0, base, x1, colour, seed):
    rng = random.Random(seed)
    x = x0
    while x < x1:
        w = rng.randint(22, 46)
        h = rng.randint(18, 46)
        canvas.rectangle([x, base - h, x + w, base], fill=colour)
        x += w + rng.randint(4, 10)


# ------------------------------------------------------------------ scenes
def refinery(canvas, x0, y0, x1, y1):
    """Ras Tanura at dusk: distillation towers, storage tanks, smoke."""
    shade((58, 44, 62), (150, 74, 60), (x0, y0, x1, y1), canvas)
    disc(canvas, x1 - 60, y0 + 30, 18, (248, 214, 130))
    # storage tanks
    for tx in (x0 + 20, x0 + 110, x0 + 200):
        canvas.rectangle([tx, y1 - 62, tx + 74, y1 - 6], fill=(38, 34, 40))
        canvas.ellipse([tx, y1 - 74, tx + 74, y1 - 50], fill=(52, 48, 54))
    # distillation columns
    for cx, hgt in ((x0 + 320, 150), (x0 + 372, 120), (x0 + 420, 96)):
        canvas.rectangle([cx - 12, y1 - 6 - hgt, cx + 12, y1 - 6],
                         fill=(24, 22, 28))
        canvas.rectangle([cx - 18, y1 - 6 - hgt, cx + 18, y1 - 2 - hgt],
                         fill=(24, 22, 28))
    # flame on the tallest column
    starburst(canvas, x0 + 320, y1 - 6 - 150 - 14, 18, (232, 118, 38))
    starburst(canvas, x0 + 320, y1 - 6 - 150 - 12, 9, (248, 200, 90))
    # thick black smoke drifting right
    for ox, oy, r in [(x0 + 320, y0 + 26, 13), (x0 + 356, y0 + 14, 16),
                      (x0 + 390, y0 + 28, 12), (x0 + 420, y0 + 16, 14)]:
        disc(canvas, ox, oy, r, (30, 28, 30))
    canvas.rectangle([x0, y1 - 6, x1, y1], fill=(20, 18, 24))


def strait(canvas, x0, y0, x1, y1):
    """A tanker burning in the Strait of Hormuz, mines in the water."""
    shade((10, 26, 52), (6, 14, 32), (x0, y0, x1, y1), canvas)
    for sx, sy in [(30, 14), (120, 24), (210, 12), (268, 28)]:
        disc(canvas, x0 + sx, y0 + sy, 2, (240, 240, 220))
    # tanker hull
    canvas.polygon([(x0 + 40, y1 - 30), (x0 + 280, y1 - 30),
                    (x0 + 258, y1 - 10), (x0 + 62, y1 - 10)],
                   fill=(14, 16, 26))
    canvas.rectangle([x0 + 90, y1 - 52, x0 + 118, y1 - 30], fill=(14, 16, 26))
    # fire mid-ship
    starburst(canvas, x0 + 170, y1 - 48, 16, (232, 118, 38))
    starburst(canvas, x0 + 170, y1 - 46, 8, (248, 200, 90))
    # smoke
    for ox, oy, r in [(x0 + 150, y0 + 12, 9), (x0 + 178, y0 + 6, 11),
                      (x0 + 202, y0 + 16, 8)]:
        disc(canvas, ox, oy, r, (60, 60, 64))
    # spiked mines bobbing on the waves
    for mx in (x0 + 24, x0 + 300):
        disc(canvas, mx, y1 - 16, 7, (200, 205, 220))
        for a in range(8):
            ang = math.pi * a / 4
            canvas.line([(mx, y1 - 16),
                         (mx + math.cos(ang) * 11, y1 - 16 + math.sin(ang) * 11)],
                        fill=(200, 205, 220), width=2)
    for yy in (y1 - 8,):
        for xx in range(x0 + 6, x1 - 6, 38):
            canvas.arc([xx, yy, xx + 28, yy + 10], 0, 180,
                       fill=(150, 195, 215), width=2)


def pyongyang(canvas, x0, y0, x1, y1):
    """A government office in Pyongyang; the Swiss flag comes down."""
    shade((148, 92, 96), (60, 44, 66), (x0, y0, x1, y1), canvas)
    disc(canvas, x0 + 44, y0 + 24, 14, (248, 200, 120))
    rooftops(canvas, x0 + 8, y1 - 6, x1 - 8, (28, 24, 34), seed=3)
    # the office block, centre
    bx0, bx1 = x0 + 92, x1 - 92
    canvas.rectangle([bx0, y0 + 30, bx1, y1 - 6], fill=(216, 210, 192))
    canvas.polygon([(bx0 - 8, y0 + 32), ((bx0 + bx1) // 2, y0 + 12),
                    (bx1 + 8, y0 + 32)], fill=(233, 228, 214))
    for i in range(3):
        wx = bx0 + 16 + i * 34
        canvas.rectangle([wx, y0 + 40, wx + 18, y0 + 52], fill=(24, 96, 122))
    canvas.rectangle([((bx0 + bx1) // 2) - 10, y1 - 18,
                      ((bx0 + bx1) // 2) + 10, y1 - 6], fill=(24, 32, 54))
    # flagpole with the Swiss flag, half lowered
    fx = x1 - 44
    canvas.line([(fx, y0 + 10), (fx, y1 - 6)], fill=(233, 228, 214), width=3)
    canvas.rectangle([fx, y0 + 30, fx + 42, y0 + 52], fill=(176, 26, 26))
    canvas.rectangle([fx + 18, y0 + 36, fx + 24, y0 + 46], fill=(248, 244, 232))
    canvas.rectangle([fx + 14, y0 + 40, fx + 28, y0 + 42], fill=(248, 244, 232))


def airport(canvas, x0, y0, x1, y1):
    """Thanksgiving queues: terminal, control tower, a plane in the sky."""
    shade((196, 122, 64), (96, 52, 66), (x0, y0, x1, y1), canvas)
    disc(canvas, x1 - 44, y0 + 22, 16, (248, 236, 200))
    # control tower
    canvas.rectangle([x0 + 30, y0 + 20, x0 + 42, y1 - 6], fill=(40, 34, 44))
    canvas.ellipse([x0 + 20, y0 + 8, x0 + 52, y0 + 28], fill=(40, 34, 44))
    canvas.ellipse([x0 + 26, y0 + 12, x0 + 46, y0 + 24], fill=(150, 195, 215))
    # terminal block with lit windows
    canvas.rectangle([x0 + 60, y0 + 44, x1 - 8, y1 - 6], fill=(30, 26, 34))
    for i in range(6):
        wx = x0 + 74 + i * 34
        canvas.rectangle([wx, y0 + 56, wx + 20, y0 + 74], fill=(248, 200, 90))
    # plane silhouette overhead
    px, py = x0 + 200, y0 + 16
    canvas.polygon([(px, py + 3), (px + 10, py), (px + 44, py), (px + 50, py + 3),
                    (px + 44, py + 6), (px + 10, py + 6)], fill=(20, 18, 26))
    canvas.polygon([(px + 18, py + 3), (px + 26, py - 6), (px + 30, py + 3)],
                   fill=(20, 18, 26))
    canvas.polygon([(px + 4, py + 3), (px + 8, py - 5), (px + 12, py + 3)],
                   fill=(20, 18, 26))
    # queue of travellers
    for i in range(5):
        qx = x0 + 84 + i * 44
        disc(canvas, qx, y1 - 26, 5, (248, 244, 232))
        canvas.rectangle([qx - 4, y1 - 22, qx + 4, y1 - 6], fill=(248, 244, 232))


def canaries(canvas, x0, y0, x1, y1):
    """Small boats reaching the Canary Islands at sunrise."""
    shade((24, 66, 96), (196, 120, 66), (x0, y0, x1, y1), canvas)
    disc(canvas, x1 - 52, y0 + 26, 18, (248, 214, 130))
    # island silhouette
    canvas.polygon([(x0 + 8, y1 - 6), (x0 + 120, y1 - 54), (x0 + 210, y1 - 6)],
                   fill=(28, 24, 34))
    # two crowded boats
    for bx, bw in ((x0 + 240, 90), (x0 + 350, 70)):
        canvas.polygon([(bx, y1 - 22), (bx + bw, y1 - 22), (bx + bw - 10, y1 - 8),
                        (bx + 10, y1 - 8)], fill=(200, 205, 220))
        for i in range(4):
            disc(canvas, bx + 14 + i * 18, y1 - 28, 4, (248, 244, 232))
    for yy in (y1 - 8,):
        for xx in range(x0 + 6, x1 - 6, 38):
            canvas.arc([xx, yy, xx + 28, yy + 10], 0, 180,
                       fill=(220, 225, 235), width=2)


def dhaka(canvas, x0, y0, x1, y1):
    """A garment factory in Dhaka; a wage banner goes up."""
    shade((150, 84, 96), (52, 38, 62), (x0, y0, x1, y1), canvas)
    disc(canvas, x0 + 46, y0 + 24, 15, (248, 200, 120))
    # factory with sawtooth roof
    canvas.rectangle([x0 + 20, y0 + 28, x1 - 20, y1 - 6], fill=(216, 210, 192))
    for i in range(4):
        sx = x0 + 30 + i * 108
        canvas.polygon([(sx, y0 + 28), (sx + 54, y0 + 14), (sx + 108, y0 + 28)],
                       fill=(176, 26, 26))
    for i in range(5):
        wx = x0 + 44 + i * 84
        canvas.rectangle([wx, y0 + 34, wx + 52, y0 + 44], fill=(24, 96, 122))
    # wage banner along the base
    canvas.rectangle([x0 + 60, y1 - 18, x1 - 60, y1 - 6], fill=(176, 26, 26))
    canvas.text((x0 + 72, y1 - 17), "17,000 TAKA  ·  +36%",
                font=load(SANS_BOLD, 12), fill=(248, 244, 232))


# ------------------------------------------------------------------ page
page = Image.new("RGB", (PAGE_W, PAGE_H), PAPER)
d = ImageDraw.Draw(page)

# masthead
d.rectangle([0, 0, PAGE_W, 128], fill=NAVY)
d.text((28, 18), "THE WORLD", font=load(SERIF_BOLD, 92), fill=(248, 244, 232))
d.text((612, 30), "THURSDAY 26 NOVEMBER 2026", font=load(SANS_BOLD, 24),
       fill=(248, 244, 232))
d.rectangle([612, 72, 996, 76], fill=(182, 84, 8))
d.text((612, 86), "ONE DAY  ·  SIX STORIES", font=load(SANS_REG, 20),
       fill=(200, 205, 220))
d.rectangle([0, 128, PAGE_W, 134], fill=CRIMSON)

# ------------------------------------------------------------- lead story
lx0, ly0, lx1, ly1 = 28, 152, 560, 470
refinery(d, lx0, ly0, lx1, ly1)
d.rectangle([lx0, ly1 - 4, lx1, ly1], fill=INK)

tx = 584
d.text((tx, 158), "RAS TANURA, SAUDI ARABIA", font=load(SANS_BOLD, 25),
       fill=CRIMSON)
end = paragraph(d, (tx, 192), "HOUTHIS HIT SAUDI REFINERY",
                load(SANS_BOLD, 46), INK, 412, gap=52)
end += 10
paragraph(d, (tx, end),
          "Yemen's Houthis say they struck Ras Tanura, the kingdom's "
          "largest refinery, processing 550,000 barrels a day. The "
          "Saudi-led coalition says it shot down four drones and has not "
          "confirmed a hit. Brent crude jumped 2.4% to about $93.60.",
          load(SANS_REG, 21), BODY, 412, gap=28)

d.rectangle([28, 486, PAGE_W - 28, 490], fill=INK)

# ------------------------------------------------------------- three across
ART = {"strait": strait, "envoy": pyongyang, "airport": airport}
TRIO = [
    ("STRAIT OF HORMUZ", "MINES IN THE STRAIT",
     "Oil tankers catch fire after hitting naval mines in the Strait of "
     "Hormuz. Iran claims five more hit in 24 hours and says the strait "
     "will stay shut until its demands are met.",
     "strait"),
    ("PYONGYANG", "NORTH KOREA EXPELS SWISS ENVOY",
     "Pyongyang orders Switzerland to shut its office and its envoy to "
     "leave in 48 hours, after Kim Yo Jong condemned Swiss sanctions.",
     "envoy"),
    ("UNITED STATES", "THANKSGIVING GRIDLOCK",
     "Travellers face long airport lines and bad weather in the run-up "
     "to Thanksgiving Day, as the year's busiest travel weekend begins.",
     "airport"),
]

for i, (place, head, body, kind) in enumerate(TRIO):
    cx = 28 + i * (312 + 16)
    cy = 504
    ART[kind](d, cx, cy, cx + 312, cy + 64)
    d.rectangle([cx, cy + 61, cx + 312, cy + 64], fill=CRIMSON)
    d.text((cx, cy + 70), place, font=load(SANS_BOLD, 16), fill=CRIMSON)
    y = paragraph(d, (cx, cy + 92), head, load(SANS_BOLD, 22), INK, 312,
                  gap=24)
    paragraph(d, (cx, y + 3), body, load(SANS_REG, 16), BODY, 312, gap=19)

# ------------------------------------------------------------- two across
DUO = [
    ("CANARY ISLANDS", "RECORD DAY IN THE CANARIES",
     "Nearly 2,000 migrants reach Spain's Canary Islands in a record "
     "single-day arrival, the largest one-day total yet recorded.",
     "canaries"),
    ("DHAKA", "DHAKA RAISES THE FLOOR",
     "Bangladesh raises garment workers' minimum wage by 36% to 17,000 "
     "taka a month, after weeks of protests by factory workers.",
     "dhaka"),
]
ART2 = {"canaries": canaries, "dhaka": dhaka}

for i, (place, head, body, kind) in enumerate(DUO):
    cx = 28 + i * (476 + 16)
    cy = 730
    ART2[kind](d, cx, cy, cx + 476, cy + 64)
    d.rectangle([cx, cy + 61, cx + 476, cy + 64], fill=CRIMSON)
    d.text((cx, cy + 70), place, font=load(SANS_BOLD, 16), fill=CRIMSON)
    y = paragraph(d, (cx, cy + 92), head, load(SANS_BOLD, 22), INK, 476,
                  gap=24)
    paragraph(d, (cx, y + 3), body, load(SANS_REG, 16), BODY, 476, gap=19)

# footer
d.rectangle([0, 924, PAGE_W, 928], fill=INK)
d.rectangle([0, 928, PAGE_W, PAGE_H], fill=NAVY)
d.text((28, 942),
       "MARKETS:  Brent crude $93.60, up 2.4% after the Ras Tanura strike  ·  "
       "Oil flows through Hormuz under threat",
       font=load(SANS_REG, 16), fill=(220, 224, 232))
d.text((28, 972), "THURSDAY 26 NOVEMBER 2026  ·  SIX STORIES, ONE DAY",
       font=load(SANS_BOLD, 16), fill=(180, 190, 205))

page.save("entry.png", optimize=True)
print("saved entry.png")
