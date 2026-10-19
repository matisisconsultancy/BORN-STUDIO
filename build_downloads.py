#!/usr/bin/env python3
"""Public brand downloads for the brand book (served as real files by GitHub Pages).
Source: the curated 01_Marca folder of the stage-1 delivery.
Only public brand material goes here: logos, animations, fonts.
Templates, manuals and deliverables stay in the studio's Drive."""
import os, sys, zipfile
SRC = sys.argv[1]                               # .../01_Marca
OUT = "downloads"; os.makedirs(OUT, exist_ok=True)
README = ("Born Apparel Studio - Brand kit\nBrand book: https://matisisconsultancy.github.io/BORN-STUDIO/\n\n"
 "logos-png/   High-resolution PNG, transparent background. For screens, documents, social.\n"
 "logos-svg/   Vector. For print, embroidery, signage and any size.\n"
 "animations/  The two animated signatures: MP4 (universal) and WebM.\n"
 "fonts/       Bodoni Moda (voice), Jost (reading), Space Mono (technical data). SIL Open Font License.\n"
 "\n"
 "Red is earned: #C4122E, only where BORN is born.\nSketched. Stitched. BORN.\n")
def add_dir(z, d, arc):
    for f in sorted(os.listdir(os.path.join(SRC, d))):
        if not f.startswith("."): z.write(os.path.join(SRC, d, f), f"{arc}/{f}")
def mk(name, parts, extra=True):
    with zipfile.ZipFile(f"{OUT}/{name}", "w", zipfile.ZIP_DEFLATED) as z:
        for d, arc in parts: add_dir(z, d, arc)
        if extra:
            z.writestr("README.txt", README)
mk("BORN-Brand-Kit.zip", [("Logos_PNG","logos-png"),("Logos_SVG","logos-svg"),("Animaciones","animations"),("Tipografias","fonts")])
mk("BORN-Logos-SVG.zip", [("Logos_SVG","logos-svg")], extra=False)
mk("BORN-Fonts.zip", [("Tipografias","fonts")], extra=False)
for f in sorted(os.listdir(OUT)): print(f, round(os.path.getsize(f"{OUT}/{f}")/1024), "KB")
