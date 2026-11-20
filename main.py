#!/usr/bin/env python3
"""
THE WORLD TODAY — Friday, 20 November 2026 in one image.

Entry program for the make.fun bounty "Sum up 20 November's world news
in one image" (news-image-20261120).

The program is fully self-contained: the day's news (gathered from the
day's reporting on 20 November 2026) is embedded below as data, and the
poster is drawn with Pillow only. No network, no randomness, no clock:
every run writes byte-identical output to /output/entry.png
(or to $OUTPUT_PATH when set).
"""

import os

from PIL import Image, ImageDraw, ImageFont

# ---------------------------------------------------------------- fonts

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


# ---------------------------------------------------------------- palette

PAPER = (247, 243, 233)
INK = (18, 18, 20)
MUTE = (92, 88, 80)
RED = (178, 34, 40)
NAVY = (16, 42, 74)
RULE = (30, 30, 30)
LIGHT = (206, 198, 180)

W = H = 1024

# ---------------------------------------------------------------- the news
# Friday, 20 November 2026, as reported that day (Open Chronicle global
# brief, One Turn world front page, BBC/Euronews headlines of the day).

HERO_KICKER = "SHENZHEN  •  DIPLOMACY"
HERO_HEAD = "Trump, Xi and Putin\nHold First Three-Way Summit"
HERO_SUB = "The US, Chinese and Russian presidents met in Shenzhen and signed a four-point joint peace declaration — a first-of-its-kind summit."

LEAD2_KICKER = "THE HAGUE  •  INTERNATIONAL JUSTICE"
LEAD2_HEAD = "ICJ Rules Myanmar Committed Genocide Against the Rohingya"
LEAD2_SUB = "The World Court's landmark judgment is the first genocide finding against a state in its history."

BRIEFS = [
    ("WAR IN UKRAINE",
     "Russia's Massive Strike on Kyiv",
     "Overnight missile and drone barrage hit the capital: three bridges struck, embassies damaged, residents in metro shelters."),
    ("MIDDLE EAST",
     "Houthi Missile Damages Riyadh Tower",
     "Strike on the financial district damaged the Public Investment Fund tower as Hormuz tanker attacks intensified."),
    ("MARKETS",
     "AI Sell-Off Deepens Worldwide",
     "AI valuation doubts after Anthropic's record Nasdaq debut dragged stocks lower for a fifth straight day."),
    ("CLIMATE",
     "COP31 Draft Drops Fossil-Fuel Exit",
     "Negotiators in Antalya cut any phase-out call from the slimmed-down draft deal."),
    ("EUROPE",
     "EU and UK Seal Brexit 'Reset'",
     "Brussels summit sealed the reset deal of the renewed partnership; talks continue in some areas."),
    ("HEALTH",
     "Kenya's Last Ebola Patient Goes Home",
     "Final patient discharged; the 42-day countdown to an Ebola-free declaration begins."),
    ("ASIA",
     "Cyclone Akvan Hits Odisha",
     "The cyclone made landfall on India's Odisha coast amid a week of regional floods and fires."),
    ("GAZA",
     "First Incursion Since the Truce",
     "Israeli forces crossed the Yellow Line in central Gaza, first such move since the ceasefire."),
]

TICKER = "NIKKEI −4.8%  •  S&P 500 FALLS AGAIN  •  ANTHROPIC SLIDES AFTER IPO  •  TANKER ABLAZE IN HORMUZ"
OBIT = "FIONA THE HIPPO  2017–2026 — Cincinnati Zoo's beloved hippo, a global star since her premature birth, has died aged nine."
FOOTER = "Summarised from the day's reporting — Shenzhen, The Hague, Kyiv, Riyadh, Antalya, Brussels, Nairobi, Odisha, Gaza."

# ---------------------------------------------------------------- drawing


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w_
    if cur:
        lines.append(cur)
    return lines


def block_h(draw, text, fnt, max_w, leading):
    return int(len(wrap(draw, text, fnt, max_w)) * fnt.size * leading)


def text_block(draw, x, y, text, fnt, fill, max_w, leading=1.22):
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=fill)
        y += int(fnt.size * leading)
    return y


def build():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 46                      # page margin
    CW = W - 2 * M              # content width

    # ---- masthead ------------------------------------------------------
    d.text((M, 22), "THE WORLD TODAY", font=font(SERIF_B, 74), fill=INK)
    d.line([(M, 118), (W - M, 118)], fill=RULE, width=5)
    d.line([(M, 126), (W - M, 126)], fill=RULE, width=2)
    d.text((M, 134), "FRIDAY, 20 NOVEMBER 2026", font=font(SANS_B, 20), fill=NAVY)
    right = "THE DAY'S WORLD NEWS, ON ONE PAGE"
    d.text((W - M - d.textlength(right, font=font(SANS, 17)), 136),
           right, font=font(SANS, 17), fill=MUTE)
    d.line([(M, 164), (W - M, 164)], fill=RULE, width=2)

    # ---- hero ----------------------------------------------------------
    # a pale panel with a red spine sets the lead story apart from the page
    d.rectangle([(M - 12, 166), (W - M + 12, 363)], fill=(239, 233, 215))
    d.rectangle([(M - 12, 166), (M - 6, 363)], fill=RED)
    y = 176
    d.text((M, y), HERO_KICKER, font=font(SANS_B, 18), fill=RED)
    y += 25
    for line in HERO_HEAD.split("\n"):
        d.text((M, y), line, font=font(SERIF_B, 44), fill=INK)
        y += 52
    y += 1
    y = text_block(d, M, y, HERO_SUB, font(SERIF, 21), (40, 40, 44), CW, 1.24)
    y += 9
    d.line([(M, y), (W - M, y)], fill=RULE, width=2)
    y += 11

    # ---- second lead ---------------------------------------------------
    d.text((M, y), LEAD2_KICKER, font=font(SANS_B, 17), fill=NAVY)
    y += 23
    y = text_block(d, M, y, LEAD2_HEAD, font(SERIF_B, 30), INK, CW, 1.14)
    y += 1
    y = text_block(d, M, y, LEAD2_SUB, font(SANS, 18), (40, 40, 44), CW, 1.22)
    y += 9
    d.line([(M, y), (W - M, y)], fill=RULE, width=2)
    y += 12

    # ---- briefs grid: 2 columns, rows sized to content -----------------
    col_w = (CW - 28) // 2
    kf, hf, bf = font(SANS_B, 14), font(SERIF_B, 20), font(SANS, 14)
    for r in range(4):
        pair = BRIEFS[2 * r:2 * r + 2]
        heights = []
        for kick, head, body in pair:
            hh = 19 + block_h(d, head, hf, col_w, 1.1) + 2 + block_h(d, body, bf, col_w, 1.15)
            heights.append(hh)
        row_h = max(heights)
        for c, (kick, head, body) in enumerate(pair):
            cx = M + c * (col_w + 28)
            if c == 1:
                d.line([(cx - 14, y), (cx - 14, y + row_h - 6)], fill=LIGHT, width=2)
            d.text((cx, y), kick, font=kf, fill=RED)
            yy = text_block(d, cx, y + 19, head, hf, INK, col_w, 1.1)
            text_block(d, cx, yy + 2, body, bf, (52, 50, 46), col_w, 1.15)
        y += row_h + 8
    y -= 2
    d.line([(M, y), (W - M, y)], fill=RULE, width=2)
    y += 10

    # ---- obit ------------------------------------------------------------
    y = text_block(d, M, y, OBIT, font(SERIF, 16), MUTE, CW, 1.22)
    y += 8

    # ---- markets ticker (auto-fit) ---------------------------------------
    d.rectangle([(M, y), (W - M, y + 36)], fill=NAVY)
    tsize = 16
    tf = font(SANS_B, tsize)
    while d.textlength(TICKER, font=tf) > CW - 20 and tsize > 10:
        tsize -= 1
        tf = font(SANS_B, tsize)
    tw = d.textlength(TICKER, font=tf)
    d.text((M + (CW - tw) / 2, y + 9), TICKER, font=tf, fill=(240, 236, 224))
    y += 46

    # ---- footer ------------------------------------------------------------
    d.line([(M, H - 40), (W - M, H - 40)], fill=RULE, width=2)
    d.text((M, H - 32), FOOTER, font=font(SANS, 13), fill=MUTE)
    return img


def main():
    img = build()
    out = os.environ.get("OUTPUT_PATH", "/output/entry.png")
    folder = os.path.dirname(out)
    if folder:
        os.makedirs(folder, exist_ok=True)
    img.save(out, format="PNG", optimize=True)


if __name__ == "__main__":
    main()
