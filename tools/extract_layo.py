#!/usr/bin/env python3
"""Derive the LAYO capsule imagery from the approved design-stage deck.

Renders each deck page at print density, crops the regions the deliverables
use (technical flats, colorway board, 3D renders, final garment photography)
and writes trimmed, web-weight JPEGs to deliverables/assets/.
"""
import os, pymupdf
from PIL import Image, ImageChops

SRC = "source/BORN_LayoCapsule_DesignStage.pdf"
OUT = "deliverables/assets"
DPI = 190
os.makedirs(OUT, exist_ok=True)

# name -> (page, left, top, right, bottom) as fractions of the page box
CROPS = {
    # ── technical flats: the line drawings with construction callouts ────────
    "flat_alo006":  (2, .100, .340, .478, .740),
    "flat_jk149":   (2, .515, .335, .975, .745),
    "flat_hd025":   (3, .030, .255, .490, .765),
    "flat_6012156": (3, .515, .255, .985, .765),
    "flat_wb082608":(4, .030, .255, .490, .765),
    "flat_wb082601":(4, .515, .255, .985, .765),

    # ── colourway flats: every style in every standard it was drawn in ──────
    "cw_jacket_black":   (5, .015, .115, .295, .515),
    "cw_jacket_peri":    (5, .015, .515, .295, .930),
    "cw_hoodie_peri":    (5, .315, .120, .600, .760),
    "cw_hoodie_whisper": (5, .675, .120, .998, .760),
    "cw_bra_red":        (6, .080, .295, .345, .915),
    "cw_bra_black":      (6, .365, .295, .630, .915),
    "cw_bra_green":      (6, .645, .295, .910, .915),

    # ── 3D visualisation ────────────────────────────────────────────────────
    "render_periwinkle": (7, .045, .185, .258, .610),
    "render_whisper":    (7, .235, .415, .482, .862),
    "render_black":      (7, .546, .308, .732, .610),
    "render_blue":       (7, .742, .218, .972, .472),
    "render_bra_red":    (8, .038, .095, .255, .580),
    "render_bra_green":  (8, .660, .115, .998, .500),
    "render_bra_black":  (8, .640, .515, .998, .905),
    "render_motion":     (8, .298, .205, .605, .868),

    # ── sample photography: the garments as they came off the line ──────────
    "photo_hoodie_f":  (9, .222, .075, .525, .512),
    "photo_jacket_f":  (9, .530, .075, .758, .512),
    "photo_jacket_b":  (9, .762, .075, .990, .512),
    "photo_hoodie_b":  (9, .222, .520, .525, .972),
    "photo_bra_f":     (9, .530, .520, .758, .972),
    "photo_bra_b":     (9, .762, .520, .990, .972),
    "photo_bra_red_f": (10, .046, .183, .267, .634),
    "photo_bra_red_b": (10, .272, .183, .491, .634),
    "photo_bra_blk_f": (10, .497, .183, .716, .634),
    "photo_bra_blk_b": (10, .728, .183, .948, .634),
    "photo_leg_white_f":(11, .074, .084, .293, .534),
    "photo_leg_white_b":(11, .299, .084, .518, .534),
    "photo_leg_trim_f": (11, .531, .084, .751, .534),
    "photo_leg_trim_b": (11, .758, .084, .978, .534),
    "photo_short_f":    (11, .524, .551, .751, .972),
    "photo_short_b":    (11, .742, .551, .968, .972),
}

def drop_dark_header(im, thresh=110, look=.60):
    """The source deck stamps a dark title bar over each style panel; the new
    documents carry their own headers, so cut everything above the bar away."""
    g = im.convert("L")
    w, h = g.size
    win = int(h * look)
    dark = [y for y in range(win)
            if sum(g.crop((0, y, w, y + 1)).getdata()) / w <= thresh]
    return im.crop((0, dark[-1] + 1, w, h)) if dark else im

def trim(im, bg=(255, 255, 255), tol=8):
    """Drop uniform margins so each asset sits tight in its own box."""
    ref = Image.new("RGB", im.size, bg)
    diff = ImageChops.difference(im.convert("RGB"), ref).convert("L").point(lambda v: 255 if v > tol else 0)
    box = diff.getbbox()
    return im.crop(box) if box else im

def main():
    doc = pymupdf.open(SRC)
    pages = {}
    for n in sorted({c[0] for c in CROPS.values()}):
        pages[n] = doc[n - 1].get_pixmap(dpi=DPI)

    for name, (n, l, t, r, b) in CROPS.items():
        px = pages[n]
        im = Image.frombytes("RGB", (px.width, px.height), px.samples)
        im = im.crop((int(l * px.width), int(t * px.height),
                      int(r * px.width), int(b * px.height)))
        if name.startswith("flat_"): im = drop_dark_header(im)
        im = trim(im)
        im.thumbnail((1600, 1600) if name == "render_motion" else (1150, 1150), Image.LANCZOS)
        path = f"{OUT}/{name}.jpg"
        im.save(path, "JPEG", quality=80, optimize=True, progressive=True)
        print(f"{name:16s} {im.size[0]:4d}x{im.size[1]:4d}  {os.path.getsize(path)//1024:4d} KB")

if __name__ == "__main__":
    main()
