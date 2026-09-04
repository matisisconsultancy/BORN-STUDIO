#!/usr/bin/env python3
"""BORN Studio — the client Project Room.

One standalone page a client opens by link. It carries the live development
tracker plus five print-ready documents: quote, invoice, tech pack, fitting
report and handover. Same pipeline as build_book.py — fonts and marks embedded,
no build step, no network, nothing to install.

Everything renders from the PROJECT / STYLES / DOCS blocks below. Swap those and
the whole room re-renders: the tracker, every document header, every total.

Emits deliverables/index.html (standalone) and
tools/_work/deliverables_artifact.html (body form, for publishing).
"""
import base64, os

S, W, O = "tools/src", "tools/_work", "deliverables"
os.makedirs(W, exist_ok=True)
rd = lambda p: open(p, encoding="utf-8").read()

def datauri(path, mime):
    return f"data:{mime};base64," + base64.b64encode(open(path, "rb").read()).decode("ascii")

FONTS = rd(f"{S}/fonts.css")
ROOT  = rd(f"{S}/root.css")
DEFS  = rd(f"{S}/defs.svg")
SVG   = {k: rd(f"{S}/{k}.svg") for k in
         ["wm_solo", "wm_solo_neg", "ic_negativo", "ic_construccion"]}
IMG   = {f[:-4]: datauri(f"{O}/assets/{f}", "image/jpeg")
         for f in sorted(os.listdir(f"{O}/assets")) if f.endswith(".jpg")}

FAVICON = ("data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2064%2064'"
 "%3E%3Crect%20width='64'%20height='64'%20rx='13'%20fill='%231B1720'/%3E"
 "%3Ctext%20x='29'%20y='47'%20font-family='Georgia,Times,serif'%20font-size='46'%20font-weight='700'"
 "%20text-anchor='middle'%20fill='%23F2EEE6'%3EB%3C/text%3E%3Ccircle%20cx='47'%20cy='44'%20r='5'%20fill='%23C4122E'/%3E%3C/svg%3E")

# ═══════════════════════════════════════════════════════════ project state ═══
TODAY = "2026-09-04"

PROJECT = dict(
    client="LAYO", client_long="LAYO — Performance Luxury",
    contact="Layo Ade-Ojo", contact_role="Founder",
    capsule="Performance Luxury Capsule", drop="Drop 02",
    ref="BRN-LAYO-02", opened="2026-02-16", exfactory="2026-12-11",
    size_range="XS – XL", base_size="M", units=1800,
    studio="BORN Studio", studio_long="BORN Studio — Fashion Product Development",
    studio_person="María", studio_email="hello@bornstudio.co",
    vat="ESB-00000000", iban="ES00 0000 0000 0000 0000 0000",
    bic="XXXXESMMXXX", currency="EUR", terms="Net 15",
)

# The five colour standards approved for the capsule. Hex values are screen
# approximations of the TCX standards — dye to the physical Pantone chip.
COLORWAYS = [
    ("11-0701 TCX", "Whisper White",     "#EFEBE4", "light"),
    ("19-3911 TCX", "Black Beauty",      "#282A2D", "dark"),
    ("19-1862 TCX", "Jester Red",        "#9E1B32", "dark"),
    ("17-3919 TCX", "Purple Impression", "#7F84B7", "dark"),
    ("14-6312 TCX", "Cameo Green",       "#AFC0AC", "light"),
]

# ═════════════════════════════════════════════════════════════ the six styles ═
# fabric / trims / pom rows come straight off the approved design-stage deck.
# pom row = (code, point of measure, XS, S, M, L, XL, tolerance)
STYLES = [
 dict(no="ALO006", name="Dual-Layer Cold Shoulder Long Sleeve Bra Top",
   short="Cold Shoulder Bra Top", cat="Top", img="flat_alo006", photo=["photo_bra_f", "photo_bra_b"],
   fabric="Performance rib knit · 78% nylon / 22% elastane · 280 g/m² · 4-way stretch",
   hand="Moisture-wicking, breathable, soft hand feel, lightweight support",
   details=["Long sleeve bra top with cold shoulder construction", "Dual-layer body construction",
            "Fixed shoulder straps", "Cross-back straps", "Raglan sleeves",
            "Elastic binding band", "Thumb holes"],
   bom=[("Shell", "Performance rib knit 280 g/m², 78% NY / 22% EL", "Fujian Kingtex", "KT-RIB280", "19-3911 TCX", "1.15 m"),
        ("Binding", "Self rib, 40 mm cut, folded to 20 mm", "Fujian Kingtex", "KT-RIB280", "Self", "0.35 m"),
        ("Underband", "Knitted elastic 25 mm, soft edge", "Kufner", "KE-25S", "Black", "0.85 m"),
        ("Logo", "Silicone heat transfer 32 × 9 mm", "Sinotech", "ST-SIL-32", "Tonal", "1 pc"),
        ("Main label", "Woven damask 40 × 20 mm, centre-fold", "Etiquetas Vigo", "LB-LAYO-01", "Ink / Ivory", "1 pc"),
        ("Care label", "Satin 30 × 55 mm, 4-fold, EU 1007/2011", "Etiquetas Vigo", "LB-CARE-EU", "Ivory", "1 pc"),
        ("Thread", "Textured nylon 150D", "A&E", "PERMA-150", "TTM", "—")],
   pom=[("A01", "Bust ½, relaxed", 30.0, 32.0, 34.0, 36.5, 39.0, 0.8),
        ("A02", "Underband ½, relaxed", 27.0, 29.0, 31.0, 33.5, 36.0, 0.8),
        ("A03", "Binding band height", 4.0, 4.0, 4.0, 4.0, 4.0, 0.2),
        ("B01", "CF length from HPS", 30.0, 31.0, 32.0, 33.0, 34.0, 0.5),
        ("B02", "Strap width", 1.6, 1.6, 1.6, 1.6, 1.6, 0.1),
        ("B03", "Cross-back strap drop", 11.0, 11.5, 12.0, 12.5, 13.0, 0.3),
        ("C01", "Sleeve length, CB to cuff", 76.0, 77.5, 79.0, 80.5, 82.0, 0.5),
        ("C02", "Bicep ½, relaxed", 12.0, 12.6, 13.2, 13.8, 14.4, 0.4),
        ("C03", "Cuff ½ at thumb hole", 7.0, 7.3, 7.6, 7.9, 8.2, 0.2),
        ("C04", "Thumb hole length", 3.2, 3.2, 3.2, 3.2, 3.2, 0.2),
        ("C05", "Thumb hole position from cuff edge", 6.0, 6.0, 6.0, 6.0, 6.0, 0.3)],
   build=["Body and sleeve joined raglan, 4-thread overlock, 6 mm seam allowance.",
          "Dual-layer body: shell and inner cut as one, quilted at the binding only — no free-floating liner.",
          "Binding band applied with 3-thread coverstitch, 6 mm topstitch, no visible needle chew on the rib.",
          "Thumb holes bound in self, 3 mm binding, bartacked at both ends.",
          "Straps cut on the wale, elastic-inserted; strap tension checked on a live fit, not the form."]),

 dict(no="LY-JK-149", name="Full-Zip Performance Training Jacket",
   short="Training Jacket", cat="Outerwear", img="flat_jk149", photo=["photo_jacket_f", "photo_jacket_b"],
   fabric="Interlock performance knit · 76% nylon / 24% elastane · 240 g/m² · 4-way stretch",
   hand="Flexibility, durability and shape retention across repeated wear",
   details=["High stand collar", "Full front zipper with chin guard", "Raglan sleeve",
            "Princess seam shaping", "Ergonomic contour paneling", "Invisible zipper pockets",
            "Silicone zipper pull", "Tone-on-tone stitching", "Clean bonded hem", "Clean bonded cuffs",
            "Silicone logo"],
   bom=[("Shell", "Interlock performance knit 240 g/m², 76% NY / 24% EL", "Fujian Kingtex", "KT-INT240", "19-3911 TCX", "1.65 m"),
        ("Front zip", "Reverse coil #3, 59 cm, tonal tape", "YKK", "CFC-3-59", "Tonal", "1 pc"),
        ("Pocket zips", "Invisible #3, 16 cm", "YKK", "CFI-3-16", "Tonal", "2 pcs"),
        ("Zipper pull", "Silicone moulded, 28 mm, debossed", "Sinotech", "ST-PULL-28", "Tonal", "3 pcs"),
        ("Chin guard", "Self, fused KF-40W", "Fujian Kingtex", "KT-INT240", "Self", "0.05 m"),
        ("Bonding tape", "PU hot-melt 15 mm, hem and cuffs", "Bemis", "3218-15", "Clear", "1.40 m"),
        ("Logo", "Silicone heat transfer 32 × 9 mm, CB neck", "Sinotech", "ST-SIL-32", "Tonal", "1 pc"),
        ("Main label", "Woven damask 40 × 20 mm, centre-fold", "Etiquetas Vigo", "LB-LAYO-01", "Ink / Ivory", "1 pc"),
        ("Thread", "Textured nylon 150D, tone-on-tone", "A&E", "PERMA-150", "TTM", "—")],
   pom=[("A01", "Chest ½, 2.5 cm below armhole", 41.0, 43.0, 45.0, 47.5, 50.0, 1.0),
        ("A02", "Waist ½, 38 cm from HPS", 37.0, 39.0, 41.0, 43.5, 46.0, 1.0),
        ("A03", "Sweep ½ at bonded hem", 39.0, 41.0, 43.0, 45.5, 48.0, 1.0),
        ("B01", "CB length from HPS", 57.0, 58.5, 60.0, 61.5, 63.0, 0.5),
        ("B02", "Raglan, neck point to sleeve seam", 12.5, 13.0, 13.5, 14.0, 14.5, 0.3),
        ("B03", "Across back, 15 cm from HPS", 34.0, 35.5, 37.0, 38.5, 40.0, 0.5),
        ("C01", "Sleeve length, CB to cuff", 78.0, 79.5, 81.0, 82.5, 84.0, 0.5),
        ("C02", "Bicep ½, 2.5 cm below armhole", 15.0, 15.8, 16.6, 17.4, 18.2, 0.4),
        ("C03", "Cuff opening ½, bonded", 8.4, 8.7, 9.0, 9.3, 9.6, 0.3),
        ("D01", "Stand collar height, CB", 7.5, 7.5, 7.5, 7.5, 7.5, 0.2),
        ("D02", "Front zip length", 56.0, 57.5, 59.0, 60.5, 62.0, 0.5)],
   build=["Princess seams and contour panels joined 4-thread overlock, then 6 mm coverstitch flat to the body.",
          "Hem and cuffs bonded with Bemis 3218 — no stitch line on the face. Press at 140 °C / 3 bar / 15 s.",
          "Chin guard fused and caught in the collar seam; the zip top stop sits 4 mm below the collar fold.",
          "Invisible pocket zips set into the princess seam, not a slash — the seam carries the load.",
          "All topstitching tone-on-tone, 150D textured nylon; no contrast thread anywhere on the shell."]),

 dict(no="LY-6012156", name="Oasis PureLuxe High-Waisted 6\" Shorts",
   short="PureLuxe 6\" Shorts", cat="Bottom", img="flat_6012156", photo=[],
   fabric="PureLuxe interlock · 72% recycled nylon / 28% elastane · 210 g/m² · 4-way stretch",
   hand="Lightweight stretch engineered for mobility and structural stability",
   details=["High-rise waistband with twin-needle stitching", "Heart-shape yoke",
            "Integrated pocket design", "Crotch with twin-needle stitching",
            "Back rise with twin-needle stitching", "Hem with twin-needle stitching", "Silicone logo"],
   bom=[("Shell", "PureLuxe interlock 210 g/m², 72% rNY / 28% EL", "Fujian Kingtex", "KT-PLX210", "19-3911 TCX", "0.85 m"),
        ("Waistband", "Self, 12 cm double layer", "Fujian Kingtex", "KT-PLX210", "Self", "0.30 m"),
        ("Pocket mesh", "Power mesh 120 g/m²", "Fujian Kingtex", "KT-PM120", "Tonal", "0.15 m"),
        ("Gusset", "Self, single layer", "Fujian Kingtex", "KT-PLX210", "Self", "incl."),
        ("Logo", "Silicone heat transfer 24 × 7 mm", "Sinotech", "ST-SIL-24", "Tonal", "1 pc"),
        ("Care label", "Satin 30 × 55 mm, 4-fold, EU 1007/2011", "Etiquetas Vigo", "LB-CARE-EU", "Ivory", "1 pc"),
        ("Thread", "Textured nylon 150D, twin-needle coverstitch", "A&E", "PERMA-150", "TTM", "—")],
   pom=[("A01", "Waistband height, finished", 12.0, 12.0, 12.0, 12.0, 12.0, 0.3),
        ("A02", "Waist ½, relaxed", 28.0, 30.0, 32.0, 34.5, 37.0, 0.8),
        ("A03", "Hip ½, 20 cm below waist", 40.0, 42.0, 44.0, 46.5, 49.0, 1.0),
        ("B01", "Front rise incl. waistband", 28.0, 29.0, 30.0, 31.0, 32.0, 0.5),
        ("B02", "Back rise incl. waistband", 35.0, 36.0, 37.0, 38.0, 39.0, 0.5),
        ("B03", "Inseam", 15.2, 15.2, 15.2, 15.2, 15.2, 0.3),
        ("C01", "Thigh ½, 2.5 cm below crotch", 25.0, 26.2, 27.4, 28.6, 29.8, 0.5),
        ("C02", "Leg opening ½", 26.0, 27.2, 28.4, 29.6, 30.8, 0.5)],
   build=["Waistband, rises and hem all twin-needle coverstitch, 6 mm gauge — one gauge across the whole style.",
          "Heart-shape yoke seam runs into the back rise; match the notch or the yoke reads crooked at 3 m.",
          "Pocket bag in power mesh, caught in the waistband seam and bartacked at the opening corners.",
          "Gusset set flat, single layer, no seam crossing at the crotch point.",
          "Silicone logo applied after the waistband is closed, 4 cm from the CF, on the band face."]),

 dict(no="LY-HD-025", name="UrbanEase Cropped Zip Hoodie",
   short="Cropped Zip Hoodie", cat="Top", img="flat_hd025", photo=["photo_hoodie_f", "photo_hoodie_b"],
   fabric="Brushed-back French terry · 68% cotton / 27% polyester / 5% elastane · 320 g/m²",
   hand="Smooth exterior, brushed interior — warmth without bulk",
   details=["Oversized fit, relaxed body shape", "Cropped silhouette", "Dropped shoulders",
            "Double-layer hood", "Full front zipper", "Front kangaroo pocket",
            "Rib cuffs and rib hem", "Silicone logo"],
   bom=[("Shell", "Brushed-back French terry 320 g/m², 68% CO / 27% PES / 5% EL", "Ningbo Weiye", "NW-FT320", "17-3919 TCX", "2.10 m"),
        ("Rib", "2 × 1 rib 340 g/m², cuffs and hem", "Ningbo Weiye", "NW-RIB340", "Self", "0.45 m"),
        ("Front zip", "Reverse coil #5, 46 cm, tonal tape", "YKK", "CFC-5-46", "Tonal", "1 pc"),
        ("Zipper pull", "Silicone moulded, 28 mm, debossed", "Sinotech", "ST-PULL-28", "Tonal", "1 pc"),
        ("Hood lining", "Self — hood cut double layer", "Ningbo Weiye", "NW-FT320", "Self", "incl."),
        ("Logo", "Silicone heat transfer 32 × 9 mm, LH chest", "Sinotech", "ST-SIL-32", "19-1862 TCX", "1 pc"),
        ("Main label", "Woven damask 40 × 20 mm, centre-fold", "Etiquetas Vigo", "LB-LAYO-01", "Ink / Ivory", "1 pc"),
        ("Thread", "Core-spun poly 75/2", "Coats", "EPIC-75", "TTM", "—")],
   pom=[("A01", "Chest ½, 2.5 cm below armhole", 54.0, 56.0, 58.0, 60.5, 63.0, 1.0),
        ("A02", "Sweep ½ at rib hem, relaxed", 46.0, 48.0, 50.0, 52.5, 55.0, 1.0),
        ("B01", "CB length from HPS", 47.0, 48.5, 50.0, 51.5, 53.0, 0.5),
        ("B02", "Across shoulder, dropped", 50.0, 52.0, 54.0, 56.0, 58.0, 0.8),
        ("B03", "Armhole depth from HPS", 28.0, 29.0, 30.0, 31.0, 32.0, 0.5),
        ("C01", "Sleeve length from shoulder seam", 52.0, 53.0, 54.0, 55.0, 56.0, 0.5),
        ("C02", "Cuff rib height", 6.0, 6.0, 6.0, 6.0, 6.0, 0.2),
        ("C03", "Hem rib height", 5.0, 5.0, 5.0, 5.0, 5.0, 0.2),
        ("D01", "Hood height, CF neck to top", 34.0, 35.0, 36.0, 37.0, 38.0, 0.5),
        ("D02", "Hood width at widest", 26.0, 26.5, 27.0, 27.5, 28.0, 0.5)],
   build=["Body seams 4-thread overlock, shoulder seams taped — the dropped shoulder carries the hood's weight.",
          "Hood cut double layer in self, no separate lining; CB seam of the outer and inner offset 5 mm so they do not stack.",
          "Rib cuffs and hem attached with a 1 : 1.15 stretch ratio. Over-stretching here is what makes a hoodie hang open.",
          "Kangaroo pocket bartacked at all four opening corners, 8 mm bartack.",
          "Zip set with the terry relaxed, not tensioned — a tensioned zip tape ripples after the first wash."]),

 dict(no="WB082601", name="Ultra-High Waist Core Support Leggings",
   short="Core Support Leggings", cat="Bottom", img="flat_wb082601", photo=[],
   fabric="Second-skin interlock · 75% recycled nylon / 25% elastane · 260 g/m² · high recovery",
   hand="Smooth, second-skin feel with durability and recovery after repeated wear",
   details=["Ultra high-rise seamless extended waistband", "Minimal seam construction",
            "Front rise with 4-needle 6-thread flatlock", "Back rise with 4-needle 6-thread flatlock",
            "Crotch with 4-needle 6-thread flatlock", "Flatlock hem finish", "Silicone logo"],
   bom=[("Shell", "Second-skin interlock 260 g/m², 75% rNY / 25% EL", "Fujian Kingtex", "KT-SSK260", "11-0701 TCX", "1.05 m"),
        ("Waistband", "Self, extended seamless, 15 cm", "Fujian Kingtex", "KT-SSK260", "Self", "0.35 m"),
        ("Gusset", "Self, flatlock set", "Fujian Kingtex", "KT-SSK260", "Self", "incl."),
        ("Logo", "Silicone heat transfer 24 × 7 mm", "Sinotech", "ST-SIL-24", "19-1862 TCX", "1 pc"),
        ("Care label", "Satin 30 × 55 mm, 4-fold, EU 1007/2011", "Etiquetas Vigo", "LB-CARE-EU", "Ivory", "1 pc"),
        ("Thread", "Textured nylon 150D, 4-needle 6-thread flatlock", "A&E", "PERMA-150", "TTM", "—")],
   pom=[("A01", "Waistband height, finished", 15.0, 15.0, 15.0, 15.0, 15.0, 0.3),
        ("A02", "Waist ½, relaxed", 28.0, 30.0, 32.0, 34.5, 37.0, 0.8),
        ("A03", "Hip ½, 20 cm below waist", 40.0, 42.0, 44.0, 46.5, 49.0, 1.0),
        ("B01", "Front rise incl. waistband", 32.0, 33.0, 34.0, 35.0, 36.0, 0.5),
        ("B02", "Back rise incl. waistband", 40.0, 41.0, 42.0, 43.0, 44.0, 0.5),
        ("B03", "Inseam", 66.0, 67.0, 68.0, 69.0, 70.0, 0.5),
        ("C01", "Thigh ½, 2.5 cm below crotch", 25.0, 26.2, 27.4, 28.6, 29.8, 0.5),
        ("C02", "Knee ½, 33 cm below crotch", 17.0, 17.8, 18.6, 19.4, 20.2, 0.4),
        ("C03", "Leg opening ½", 10.4, 10.8, 11.2, 11.6, 12.0, 0.3)],
   build=["Every structural seam 4-needle 6-thread flatlock — no overlock anywhere the skin touches.",
          "Waistband cut as an extension of the front and back, not a separate band. There is no waist seam to roll.",
          "Squat test on the size set before approval: the shell must not go translucent at 260 g/m² under stretch.",
          "Recovery check — 30 min wear, then measure A02 again. More than 2 cm of growth fails the quality.",
          "Gusset flatlocked in, seams crossing at no more than two layers."]),

 dict(no="WB082608", name="Noir White-Trim High-Rise Compression Leggings",
   short="White-Trim Compression Leggings", cat="Bottom", img="flat_wb082608", photo=[],
   fabric="Matte compression knit · 79% nylon / 21% elastane · 290 g/m² · high compression",
   hand="Deep matte black with an unbroken, elongating line from hip to ankle",
   details=["High-rise waistband with contrast trim at its edge", "Front rise with flatseamer",
            "Flat-seam crotch", "Flat-seam side", "Flatlock hem finish", "Silicone logo"],
   bom=[("Shell", "Matte compression knit 290 g/m², 79% NY / 21% EL", "Fujian Kingtex", "KT-CMP290", "19-3911 TCX", "1.05 m"),
        ("Contrast trim", "Self-fabric binding 6 mm finished, waistband edge", "Fujian Kingtex", "KT-CMP290", "11-0701 TCX", "1.10 m"),
        ("Waistband", "Self, 13 cm double layer", "Fujian Kingtex", "KT-CMP290", "Self", "0.30 m"),
        ("Gusset", "Self, flat-seam set", "Fujian Kingtex", "KT-CMP290", "Self", "incl."),
        ("Logo", "Silicone heat transfer 24 × 7 mm", "Sinotech", "ST-SIL-24", "11-0701 TCX", "1 pc"),
        ("Care label", "Satin 30 × 55 mm, 4-fold, EU 1007/2011", "Etiquetas Vigo", "LB-CARE-EU", "Ivory", "1 pc"),
        ("Thread", "Textured nylon 150D, flatseam", "A&E", "PERMA-150", "TTM / white at trim", "—")],
   pom=[("A01", "Waistband height, finished", 13.0, 13.0, 13.0, 13.0, 13.0, 0.3),
        ("A02", "Contrast trim width, finished", 0.6, 0.6, 0.6, 0.6, 0.6, 0.1),
        ("A03", "Waist ½, relaxed", 27.0, 29.0, 31.0, 33.5, 36.0, 0.8),
        ("A04", "Hip ½, 20 cm below waist", 39.0, 41.0, 43.0, 45.5, 48.0, 1.0),
        ("B01", "Front rise incl. waistband", 30.0, 31.0, 32.0, 33.0, 34.0, 0.5),
        ("B02", "Back rise incl. waistband", 38.0, 39.0, 40.0, 41.0, 42.0, 0.5),
        ("B03", "Inseam", 66.0, 67.0, 68.0, 69.0, 70.0, 0.5),
        ("C01", "Thigh ½, 2.5 cm below crotch", 24.0, 25.2, 26.4, 27.6, 28.8, 0.5),
        ("C02", "Leg opening ½", 10.2, 10.6, 11.0, 11.4, 11.8, 0.3)],
   build=["Contrast trim is the whole style — 0.6 cm finished, dead even, or the piece fails. Cut on the wale, never crossgrain.",
          "Side seams flatseamed; the leg reads as one unbroken line, which is the point of the silhouette.",
          "Matte hand must survive finishing: no calendering, no optical brightener migration onto the white trim.",
          "Crock test the black against the white trim before bulk — dry and wet, grade 4 minimum.",
          "Front rise flatseamed, back rise and crotch flat-seam set; no seam stack at the crotch point."]),
]

# ══════════════════════════════════════════════════════════ the three phases ═
# state: "born" done · "stitched" in progress · "sketched" not started yet
PHASES = [
 dict(key="sketched", n="Phase 01", title="The Briefing", state="born",
   window="16 Feb — 22 Apr 2026", note="Sketched — the idea on paper",
   items=[("2026-02-20", "Discovery session and the three filters", "born"),
          ("2026-02-27", "Material selection — 3 mills shortlisted, 9 qualities handled", "born"),
          ("2026-03-13", "Technical sketches — 6 styles, front / back / side with callouts", "born"),
          ("2026-03-27", "Colour development — 5 TCX standards approved", "born"),
          ("2026-04-03", "3D visualization — 4 colourway sets", "born"),
          ("2026-04-08", "Design stage delivered", "born"),
          ("2026-04-22", "Tech pack v1.0 released — 6 styles, factory-ready", "born")]),
 dict(key="stitched", n="Phase 02", title="The Development", state="stitched",
   window="6 May — 2 Oct 2026", note="Stitched — tested with thread and needle",
   items=[("2026-05-06", "Factory pairing confirmed and contracted", "born"),
          ("2026-05-29", "Lab dips submitted — 5 standards, 3 qualities", "born"),
          ("2026-06-19", "Lab dip approval — all 5 standards to chip", "born"),
          ("2026-07-10", "SMS 1 received — 6 styles, size M", "born"),
          ("2026-07-17", "Fit session 01 — 11 corrections raised", "born"),
          ("2026-08-14", "Tech pack v2.0 — post-fit corrections", "born"),
          ("2026-08-28", "SMS 2 received — 6 styles, size M", "born"),
          ("2026-09-04", "Fit session 02 — measured against v2.0 spec", "stitched"),
          ("2026-09-18", "Size set XS – XL, all styles", "sketched"),
          ("2026-10-02", "Final approved sample", "sketched")]),
 dict(key="born", n="Phase 03", title="Production Oversight", state="sketched",
   window="16 Oct — 11 Dec 2026", note="BORN — it goes out into the world",
   items=[("2026-10-16", "PPS sign-off", "sketched"),
          ("2026-10-30", "Bulk fabric in-house at the factory", "sketched"),
          ("2026-11-20", "Inline QC visit", "sketched"),
          ("2026-12-04", "Final inspection — AQL 2.5 major / 4.0 minor", "sketched"),
          ("2026-12-11", "Ex-factory and documented handover", "sketched")]),
]

UPDATE = dict(date="2026-09-04", by="María",
  title="SMS 2 fitted. Two styles clear, four carry a correction.",
  body="Fit session 02 ran this morning against the v2.0 spec. <b>WB082601</b> and "
       "<b>LY-6012156</b> measured clean across every point — both go straight to size set. "
       "<b>LY-JK-149</b> came back 0.7 cm tall at the stand collar and the bonded cuff reads "
       "0.4 cm wide; the collar is a pattern correction, the cuff is a bonding-jig setting at "
       "the factory. <b>ALO006</b> has the thumb hole sitting 1.1 cm too low, which is why the "
       "cuff drags on the hand. <b>LY-HD-025</b> is over on hood height — 1.2 cm — and I would "
       "rather take it out of the hood than the neckline. <b>WB082608</b> is only out on the "
       "white trim width, 1.2 mm over, and that is a binder-foot change, not a pattern one."
       "<br><br>Corrections go into <b>tech pack v2.1</b> by Monday. The factory has confirmed "
       "the size set for 18 September, which holds the 11 December ex-factory date. "
       "No third full sample round is needed — that keeps €3,120 out of the budget.")

SAMPLES = [
 ("SMS 1", "2026-07-08", "2026-07-17", "Corrected — re-sample", "born"),
 ("SMS 2", "2026-08-28", "2026-09-04", "Corrected — approve to size set", "born"),
 ("Size set XS – XL", "2026-09-18", "—", "Scheduled", "sketched"),
 ("PPS", "2026-10-16", "—", "Scheduled", "sketched"),
]

# ═════════════════════════════════════════════════════════════════ documents ═
QUOTE = dict(no="Q-2026-031", issued="2026-02-09", valid="2026-03-11",
  groups=[
   ("Phase 01 · The Briefing", "Design and technical development, per style", [
     ("Discovery, the three filters, and a scoped development plan", "", ""),
     ("Material selection — mill shortlist, handles, weight and stretch qualification", "", ""),
     ("Technical sketches — front, back and side with construction callouts", "", ""),
     ("Colour development — up to 5 TCX standards, applied across the range", "", ""),
     ("3D visualization for review before a single metre is cut", "", ""),
     ("Factory-ready tech pack v1.0 — BOM, graded POM, construction, grading intent", "6 styles × €680", 4080.00)]),
   ("Phase 02 · The Development", "Sampling, fitting and revision", [
     ("Factory shortlist, pairing and contract review", "", ""),
     ("Fabric and trim sourcing, lab dip management to chip", "", ""),
     ("Two sample rounds — SMS 1 and SMS 2 — with documented fit sessions", "", ""),
     ("Tech pack revisions through to the approved sample", "6 styles × €990", 5940.00)]),
   ("Phase 03 · Production Oversight", "From size set to the client's hands", [
     ("Size set review and PPS sign-off", "", ""),
     ("Order placement support and bulk timeline management", "", ""),
     ("Inline QC visit and final AQL 2.5 inspection report", "", ""),
     ("Documented handover and full production archive", "6 styles × €580", 3480.00)])],
  passthrough=[("Lab dips — 5 standards across 3 qualities", 450.00),
               ("Sampling yardage — 26.4 m across 3 qualities", 1188.00),
               ("Trim samples — zips, pulls, labels, 6 style sets", 264.00),
               ("Courier — mill, factory and studio, est. 3 shipments", 318.00)],
  schedule=[("On signature", "40%", 5400.00), ("On SMS 2 delivered", "40%", 5400.00),
            ("On ex-factory", "20%", 2700.00)],
  assumptions=["6 styles, up to 5 colour standards, size range XS – XL, base size M.",
   "Two sample rounds are included. A third round, if the client changes the design after "
   "tech pack release, is billed at €520 per style.",
   "Timeline assumes approvals are returned within 5 working days. Every day beyond that "
   "moves the ex-factory date one day.",
   "Quoted in EUR, excluding VAT. Pass-through costs are billed at cost, on receipt, with "
   "the supplier invoice attached."],
  exclusions=["Bulk fabric and trim purchase — invoiced by the mill and factory directly.",
   "Production cost, freight, duties and customs clearance.",
   "Campaign and e-commerce photography.",
   "Packaging, hangtag and label print runs.",
   "Retail, wholesale or marketing strategy."])

INVOICE = dict(no="INV-2026-078", issued="2026-09-04", due="2026-09-19",
  ref="Q-2026-031", milestone="Milestone 2 of 3 — SMS 2 delivered",
  lines=[("Phase 02 · The Development", "Milestone 2 of 3 — 40% of the agreed fee", 1, 5400.00),
         ("Lab dips", "15 submissions — 5 standards × 3 qualities", 15, 30.00),
         ("Sampling yardage", "Performance knit, 3 qualities, 26.4 m", 26.4, 45.00),
         ("Trim samples", "Zips, silicone pulls, woven and care labels — 6 style sets", 6, 44.00),
         ("Courier", "Mill → factory → studio, 3 shipments", 3, 106.00)],
  vat_rate=0.21,
  paid=[("2026-02-20", "INV-2026-012 · Milestone 1 of 3", 6534.00)])

FITTING = dict(no="FIT-02", session="2026-09-04", sample="SMS 2", size="M",
  received="2026-08-28", form="Alvanon EU 38 · live fit 176 cm / 86-70-94",
  present="María (BORN Studio) · Layo Ade-Ojo (LAYO)", spec="Tech pack v2.0",
  # style no -> [(code, spec, measured)]
  measured={
   "LY-JK-149": [("A01", 45.0, 45.3), ("A02", 41.0, 41.2), ("A03", 43.0, 43.4),
                 ("B01", 60.0, 60.2), ("B02", 13.5, 13.6), ("B03", 37.0, 37.3),
                 ("C01", 81.0, 81.4), ("C02", 16.6, 16.8), ("C03", 9.0, 9.4),
                 ("D01", 7.5, 8.2), ("D02", 59.0, 59.0)],
   "ALO006":    [("A01", 34.0, 34.4), ("A02", 31.0, 31.3), ("A03", 4.0, 4.1),
                 ("B01", 32.0, 32.3), ("B02", 1.6, 1.6), ("B03", 12.0, 12.2),
                 ("C01", 79.0, 79.3), ("C02", 13.2, 13.4), ("C03", 7.6, 7.7),
                 ("C04", 3.2, 3.3), ("C05", 6.0, 7.1)],
   "LY-HD-025": [("A01", 58.0, 58.6), ("A02", 50.0, 50.4), ("B01", 50.0, 50.3),
                 ("B02", 54.0, 54.5), ("B03", 30.0, 30.3), ("C01", 54.0, 54.2),
                 ("C02", 6.0, 6.1), ("C03", 5.0, 5.1), ("D01", 36.0, 37.2), ("D02", 27.0, 27.4)],
   "LY-6012156":[("A01", 12.0, 12.1), ("A02", 32.0, 32.3), ("A03", 44.0, 44.5),
                 ("B01", 30.0, 30.2), ("B02", 37.0, 37.3), ("B03", 15.2, 15.3),
                 ("C01", 27.4, 27.6), ("C02", 28.4, 28.7)],
   "WB082601":  [("A01", 15.0, 15.1), ("A02", 32.0, 32.4), ("A03", 44.0, 44.6),
                 ("B01", 34.0, 34.2), ("B02", 42.0, 42.3), ("B03", 68.0, 68.3),
                 ("C01", 27.4, 27.6), ("C02", 18.6, 18.8), ("C03", 11.2, 11.3)],
   "WB082608":  [("A01", 13.0, 13.1), ("A02", 0.6, 0.72), ("A03", 31.0, 31.4),
                 ("A04", 43.0, 43.5), ("B01", 32.0, 32.2), ("B02", 40.0, 40.3),
                 ("B03", 68.0, 68.2), ("C01", 26.4, 26.7), ("C02", 11.0, 11.2)]},
  corrections=[
   ("LY-JK-149", "D01", "Stand collar reads 8.2 cm against a 7.5 cm spec. It stands away from the "
    "neck and breaks at the CB. Take 0.7 cm off the stand height and re-cut the under-collar on "
    "the bias in self, not the fused piece currently used.", "Pattern — v2.1"),
   ("LY-JK-149", "C03", "Bonded cuff opening 9.4 cm against 9.0 cm. The pattern is right; the "
    "bonding jig is set 0.4 cm wide. Reset the jig and re-press two cuffs for approval before "
    "the size set is cut.", "Factory — jig setting"),
   ("ALO006", "C05", "The thumb hole sits 1.1 cm below its marked position, so the cuff drags across "
    "the base of the thumb. Raise the opening 1.1 cm and hold the 3.2 cm length.", "Pattern — v2.1"),
   ("LY-HD-025", "D01", "Hood height 37.2 cm against 36.0 cm. Take the 1.2 cm out of the hood "
    "crown, not the neckline — the neckline is sitting correctly and the crop length depends on it.",
    "Pattern — v2.1"),
   ("WB082608", "A02", "Contrast trim finished at 0.69 cm against a 0.6 cm spec, and it reads "
    "uneven along the CB. Change the binder foot to a 6 mm and re-run. This trim is the style.",
    "Factory — binder foot")],
  holds=["LY-JK-149 — princess seams and contour panels sit square on the form and on the body. "
         "Sleeve pitch reads correct from the side. Do not touch the panel geometry.",
         "WB082601 — passed the squat test at 260 g/m² with no translucency, and recovered to "
         "within 0.6 cm after 30 minutes of wear. This is the quality; hold the mill and the weight.",
         "LY-6012156 — clean on every point. The heart-shape yoke matched the notch on both legs.",
         "All styles — tone-on-tone stitching reads as specified. No contrast thread crept in."],
  verdict="Correct and approve to size set.",
  verdict_note="No third full sample round. Corrections go into tech pack v2.1; the size set is "
               "cut to v2.1 and delivered by 18 September. Two of the five corrections are factory "
               "settings, not pattern changes, so they cost nothing but a re-press.")

HANDOVER = dict(no="HO-2026-031", due="2026-12-11", status="Issues at ex-factory",
  plan=[("Styles", "6"), ("Colour standards", "5 TCX"), ("Size range", "XS – XL"),
        ("Contracted units", "1,800"), ("Incoterms", "FCA Porto"),
        ("Final inspection", "AQL 2.5 major / 4.0 minor"), ("Ex-factory", "11 Dec 2026"),
        ("Programme", "43 weeks from kickoff")],
  archive=[
   ("Technical", ["Tech pack final revision — PDF and editable source, all 6 styles",
                  "Graded patterns, DXF, XS – XL",
                  "Graded POM sheets with achieved measurements",
                  "Construction and stitch specifications"]),
   ("Colour and materials", ["Approved lab dips, 5 TCX standards, with mill references",
                             "BOM with supplier contacts, references, MOQs and lead times",
                             "Care and composition labelling artwork, EU 1007/2011"]),
   ("Development record", ["Fit reports FIT-01 through FIT-04",
                           "Size set and PPS records with sign-off",
                           "Sample photography — flat and on form"]),
   ("Production", ["Final inspection report with AQL result",
                   "Packing list, carton dimensions and weights",
                   "Commercial invoice and shipping documents"])],
  signoff=[("BORN Studio", "María", "Founder"), ("LAYO", "Layo Ade-Ojo", "Founder")],
  next=["Silicone trims ran a 3-week lead this round. Order at kickoff next season and that "
        "comes off the critical path entirely.",
        "Kingtex holds KT-SSK260 on a stock service from January. Booking it early removes "
        "two weeks from the sampling window.",
        "Two of the five SMS 2 corrections were factory settings, not pattern. Ask for a "
        "jig and binder-foot check on the first PPS next season."])

# ═══════════════════════════════════════════════════════════════════════ CSS ═
CSS = ROOT + r"""
:root{
  --sheet:#FBF8F2;            /* document paper, a shade above the app ground */
  --sheet-2:#F4F0E7;          /* nested blocks inside a sheet */
  --rule:rgba(27,23,32,.14);
  --rule-2:rgba(27,23,32,.30);
  --topH:58px;
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{background:var(--paper);color:var(--ink);font-family:var(--sans);line-height:1.55;
  -webkit-font-smoothing:antialiased;font-size:15px}
img,svg{display:block;max-width:100%}
a{color:inherit}
::selection{background:var(--red);color:var(--paper)}
:focus-visible{outline:2px solid var(--red);outline-offset:2px;border-radius:3px}

/* ── top bar ─────────────────────────────────────────────────────────────── */
.top{position:sticky;top:0;z-index:60;background:rgba(242,238,230,.93);
  backdrop-filter:blur(12px);border-bottom:1px solid var(--rule)}
.top__in{display:flex;align-items:center;gap:1rem;padding:.5rem clamp(.9rem,2.5vw,1.6rem);
  min-height:var(--topH);flex-wrap:wrap}
.top .mark{flex:0 0 auto;display:flex;align-items:center;gap:.55rem;text-decoration:none}
.top .mark svg{height:24px;width:auto;max-width:none}
.top .mark .sub{font-family:var(--mono);font-size:.55rem;letter-spacing:.16em;
  text-transform:uppercase;color:var(--g3);border-left:1px solid var(--rule);padding-left:.55rem}
.docnav{display:flex;gap:.1rem;margin-left:auto;flex-wrap:wrap}
.docnav button{font-family:var(--mono);font-size:.63rem;letter-spacing:.12em;text-transform:uppercase;
  color:var(--g2);background:none;border:0;cursor:pointer;padding:.5rem .7rem;border-radius:6px;
  white-space:nowrap;transition:color .18s,background .18s}
.docnav button:hover{color:var(--ink);background:var(--paper-2)}
.docnav button[aria-selected=true]{color:var(--paper);background:var(--ink)}
.printbtn{font-family:var(--mono);font-size:.63rem;letter-spacing:.12em;text-transform:uppercase;
  background:none;border:1px solid var(--rule-2);color:var(--ink);border-radius:6px;
  padding:.45rem .8rem;cursor:pointer;transition:background .18s,color .18s}
.printbtn:hover{background:var(--ink);color:var(--paper);border-color:var(--ink)}

/* ── the room: docket rail + document stage ──────────────────────────────── */
.app{display:grid;grid-template-columns:272px minmax(0,1fr);align-items:stretch}
@media(max-width:1000px){.app{grid-template-columns:1fr}}
.rail{background:var(--ink);color:var(--paper)}
.rail__in{position:sticky;top:var(--topH);padding:1.5rem 1.35rem 2rem;
  min-height:calc(100vh - var(--topH));display:flex;flex-direction:column;gap:1.5rem}
@media(max-width:1000px){.rail__in{position:static;min-height:0}}
.rail h2{font-family:var(--serif);font-weight:900;font-size:1.5rem;line-height:1.05;
  letter-spacing:-.01em;margin-top:.2rem}
.rail .k{font-family:var(--mono);font-size:.56rem;letter-spacing:.2em;text-transform:uppercase;
  color:var(--g4)}
.rail dl{display:grid;grid-template-columns:1fr;gap:.7rem}
.rail dt{font-family:var(--mono);font-size:.55rem;letter-spacing:.16em;text-transform:uppercase;
  color:var(--g4)}
.rail dd{font-size:.88rem;color:var(--paper);margin-top:.1rem}
.rail dd.mono{font-family:var(--mono);font-size:.78rem;letter-spacing:.02em}
.rail .sep{height:1px;background:var(--line-d)}
.rail .now{border:1px solid var(--line-d);border-radius:10px;padding:.85rem .9rem;
  background:rgba(242,238,230,.05)}
.rail .now .ph{display:flex;align-items:center;gap:.5rem;font-family:var(--serif6);
  font-weight:600;font-size:1.05rem}
.rail .now p{font-size:.82rem;color:var(--g4);margin-top:.35rem;line-height:1.45}
.rail .foot{margin-top:auto;font-family:var(--mono);font-size:.55rem;letter-spacing:.12em;
  text-transform:uppercase;color:var(--g3);line-height:1.8}
.rail .foot a{color:var(--g4);text-decoration:none;border-bottom:1px solid rgba(242,238,230,.2)}
.rail .foot a:hover{color:var(--paper)}

/* progress rule: solid where the work is done, stitched where it is live */
.prog{display:flex;align-items:center;gap:0}
.prog i{height:3px;flex:1;display:block}
.prog i.done{background:var(--paper)}
.prog i.live{background:repeating-linear-gradient(90deg,var(--paper) 0 5px,transparent 5px 10px)}
.prog i.todo{background:rgba(242,238,230,.20)}
.prog b{width:9px;height:9px;border-radius:50%;background:var(--red);flex:0 0 auto;
  margin:0 3px;box-shadow:0 0 0 0 rgba(196,18,46,.55)}
@media(prefers-reduced-motion:no-preference){
  .prog b{animation:pulse 2.6s var(--ease) 1.2s 3}
  @keyframes pulse{0%{box-shadow:0 0 0 0 rgba(196,18,46,.55)}
                   70%{box-shadow:0 0 0 9px rgba(196,18,46,0)}
                   100%{box-shadow:0 0 0 0 rgba(196,18,46,0)}}}

/* ── stage and sheets ────────────────────────────────────────────────────── */
.stage{padding:clamp(1.1rem,2.6vw,2.2rem) clamp(.9rem,2.6vw,2.2rem) 5rem;min-width:0}
.panel{display:none}
.panel.active{display:block}
.sheet{background:var(--sheet);border:1px solid var(--rule);border-radius:3px;
  box-shadow:0 22px 50px -34px rgba(27,23,32,.5);max-width:940px;margin:0 auto;
  padding:clamp(1.6rem,3.4vw,3rem)}
.sheet + .sheet{margin-top:1.6rem}

/* document masthead — the same object on every sheet */
.mast{display:flex;justify-content:space-between;align-items:flex-start;gap:1.5rem;
  padding-bottom:1.1rem;border-bottom:2px solid var(--ink);flex-wrap:wrap}
.mast__l{flex:1 1 340px;min-width:0}
.mast__l .type{font-family:var(--mono);font-size:.6rem;letter-spacing:.24em;
  text-transform:uppercase;color:var(--red)}
.mast__l h1{font-family:var(--serif);font-weight:900;font-size:clamp(1.7rem,3.6vw,2.6rem);
  line-height:1.02;letter-spacing:-.015em;margin:.25rem 0 .3rem;text-wrap:balance}
.mast__l .who{font-size:.92rem;color:var(--g2)}
.mast__r{text-align:right;flex:0 0 auto;padding-top:.2rem}
.mast__r svg{height:22px;width:auto;max-width:none;margin-left:auto}
.mast__r .meta{font-family:var(--mono);font-size:.58rem;letter-spacing:.1em;
  text-transform:uppercase;color:var(--g3);line-height:1.85;margin-top:.5rem}
.mast__r .meta b{color:var(--ink);font-weight:400}

.dl{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:1rem 1.6rem;
  margin-top:1.2rem}
.dl > div{min-width:0}
.dl dt{font-family:var(--mono);font-size:.55rem;letter-spacing:.16em;text-transform:uppercase;
  color:var(--g3)}
.dl dd{font-family:var(--mono);font-size:.84rem;margin-top:.15rem;font-variant-numeric:tabular-nums}

.sec{margin-top:clamp(1.8rem,3.4vw,2.6rem)}
.sec--rule{border-top:1px solid var(--rule);padding-top:clamp(1.4rem,2.6vw,2rem)}
.eyebrow{font-family:var(--mono);font-size:.58rem;letter-spacing:.2em;text-transform:uppercase;
  color:var(--g3);margin-bottom:.9rem}
h2.h{font-family:var(--serif);font-weight:900;font-size:clamp(1.25rem,2.4vw,1.7rem);
  line-height:1.08;letter-spacing:-.01em;text-wrap:balance}
h3.sh{font-family:var(--serif6);font-weight:600;font-size:1.06rem;margin-bottom:.35rem}
p.body{color:var(--g2);max-width:68ch}
p.body + p.body{margin-top:.7rem}
p.body b{color:var(--ink);font-weight:500}
.note{font-family:var(--mono);font-size:.66rem;letter-spacing:.04em;color:var(--g3);
  line-height:1.7;max-width:78ch}

/* ── the maturity marker: outline / stitch / solid + red dot ─────────────── */
.mk{width:13px;height:13px;flex:0 0 auto;display:block}
.st-row{display:flex;gap:.7rem;align-items:flex-start}
.st-row .mk{margin-top:.3em}

/* ── tables ──────────────────────────────────────────────────────────────── */
.tw{overflow-x:auto;-webkit-overflow-scrolling:touch}
table.t{border-collapse:collapse;width:100%;min-width:520px;font-size:.82rem}
table.t th{font-family:var(--mono);font-size:.56rem;letter-spacing:.15em;text-transform:uppercase;
  color:var(--g3);text-align:left;padding:0 .7rem .5rem 0;border-bottom:1px solid var(--ink);
  white-space:nowrap;font-weight:400;vertical-align:bottom}
table.t td{padding:.52rem .7rem .52rem 0;border-bottom:1px solid var(--rule);vertical-align:top}
table.t tr:last-child td{border-bottom:0}
table.t .n{font-family:var(--mono);text-align:right;font-variant-numeric:tabular-nums;
  white-space:nowrap}
table.t th.n{text-align:right}
table.t td:last-child,table.t th:last-child{padding-right:0}
table.t .c{font-family:var(--mono);font-size:.74rem;letter-spacing:.05em;color:var(--g2);
  white-space:nowrap}
table.t .em{font-family:var(--serif6);font-weight:600;font-size:.95rem}
table.t tr.grp td{border-bottom:0;padding-top:1.1rem;padding-bottom:.2rem}
table.t tr.grp .gt{font-family:var(--mono);font-size:.58rem;letter-spacing:.16em;
  text-transform:uppercase;color:var(--red)}
table.t tr.sum td{border-top:1px solid var(--ink);border-bottom:0;padding-top:.7rem}
table.t tr.tot td{border-top:2px solid var(--ink);border-bottom:0;padding-top:.75rem;
  font-family:var(--serif6);font-weight:600;font-size:1.15rem}
table.t tr.tot .n{font-family:var(--mono);font-size:1.15rem;color:var(--red)}
.out{color:var(--red)}
.out-mk{display:inline-block;padding:.05rem .38rem;border:1px solid var(--red);border-radius:3px;
  font-family:var(--mono);font-size:.6rem;letter-spacing:.1em;text-transform:uppercase;color:var(--red)}
.ok-mk{display:inline-block;padding:.05rem .38rem;border:1px solid var(--rule-2);border-radius:3px;
  font-family:var(--mono);font-size:.6rem;letter-spacing:.1em;text-transform:uppercase;color:var(--g2)}

/* ── tracker ─────────────────────────────────────────────────────────────── */
.upd{background:var(--ink);color:var(--paper);border-radius:3px;padding:clamp(1.3rem,2.6vw,2rem)}
.upd .k{font-family:var(--mono);font-size:.58rem;letter-spacing:.2em;text-transform:uppercase;
  color:var(--red)}
.upd h2{font-family:var(--serif);font-weight:900;font-size:clamp(1.35rem,2.7vw,1.95rem);
  line-height:1.1;margin:.4rem 0 .7rem;text-wrap:balance}
.upd p{color:var(--g4);max-width:70ch;font-size:.95rem}
.upd p b{color:var(--paper);font-weight:400}
.upd .by{font-family:var(--mono);font-size:.58rem;letter-spacing:.14em;text-transform:uppercase;
  color:var(--g3);margin-top:1.1rem}

.phases{display:grid;gap:1.1rem;grid-template-columns:repeat(auto-fit,minmax(238px,1fr));
  margin-top:1.2rem}
.ph{border:1px solid var(--rule);border-radius:3px;padding:1.2rem 1.25rem;background:var(--sheet)}
.ph--live{border-color:var(--ink);box-shadow:inset 3px 0 0 var(--red)}
.ph__h{display:flex;justify-content:space-between;align-items:baseline;gap:.6rem}
.ph__h .n{font-family:var(--mono);font-size:.58rem;letter-spacing:.16em;text-transform:uppercase;
  color:var(--g3)}
.ph--live .ph__h .n{color:var(--red)}
.ph h3{font-family:var(--serif);font-weight:900;font-size:1.45rem;line-height:1.05;margin:.15rem 0}
.ph .win{font-family:var(--mono);font-size:.62rem;letter-spacing:.06em;color:var(--g3)}
.ph .nt{font-family:var(--serif6);font-weight:600;font-size:.9rem;color:var(--g2);
  margin:.5rem 0 .9rem;padding-bottom:.9rem;border-bottom:1px solid var(--rule)}
.ph ul{list-style:none;display:grid;gap:.62rem}
.ph li{display:flex;gap:.65rem;align-items:flex-start;font-size:.86rem;line-height:1.4}
.ph li .mk{margin-top:.28em}
.ph li .d{font-family:var(--mono);font-size:.62rem;color:var(--g3);display:block;
  letter-spacing:.04em;margin-top:.1rem}
.ph li.done{color:var(--g2)}
.ph li.live{color:var(--ink);font-weight:500}
.ph li.live .d{color:var(--red)}
.ph li.todo{color:var(--g3)}

/* ── style picker + plates ───────────────────────────────────────────────── */
.chips{display:flex;gap:.35rem;flex-wrap:wrap;margin-bottom:1.3rem}
.chip{font-family:var(--mono);font-size:.62rem;letter-spacing:.1em;text-transform:uppercase;
  background:none;border:1px solid var(--rule-2);color:var(--g2);border-radius:20px;
  padding:.34rem .78rem;cursor:pointer;transition:all .18s}
.chip:hover{border-color:var(--ink);color:var(--ink)}
.chip[aria-pressed=true]{background:var(--ink);border-color:var(--ink);color:var(--paper)}
.styl{display:none}
.styl.on{display:block}
.plate{background:#fff;border:1px solid var(--rule);border-radius:3px;padding:1rem;
  display:flex;align-items:center;justify-content:center}
.plate img{width:100%;height:auto}
.two{display:grid;grid-template-columns:1.35fr 1fr;gap:1.4rem;align-items:start}
@media(max-width:820px){.two{grid-template-columns:1fr}}

/* ── colour standards ────────────────────────────────────────────────────── */
.cws{display:grid;grid-template-columns:repeat(auto-fit,minmax(128px,1fr));gap:.7rem}
.cw{border:1px solid var(--rule);border-radius:3px;overflow:hidden;background:var(--sheet)}
.cw i{display:block;height:72px}
.cw .b{padding:.55rem .65rem}
.cw .b .code{font-family:var(--mono);font-size:.6rem;letter-spacing:.06em;color:var(--g3)}
.cw .b .nm{font-family:var(--serif6);font-weight:600;font-size:.92rem;margin-top:.05rem}

/* ── photo strip ─────────────────────────────────────────────────────────── */
.strip{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:.7rem}
.strip figure{margin:0;border:1px solid var(--rule);border-radius:3px;overflow:hidden;background:#fff}
.strip img{width:100%;height:auto;aspect-ratio:3/4;object-fit:cover}
.strip figcaption{font-family:var(--mono);font-size:.56rem;letter-spacing:.12em;
  text-transform:uppercase;color:var(--g3);padding:.5rem .6rem;background:var(--sheet)}

/* ── lists ───────────────────────────────────────────────────────────────── */
ul.li{list-style:none;display:grid;gap:.55rem}
ul.li li{padding-left:1.35rem;position:relative;color:var(--g2);line-height:1.5;max-width:74ch}
ul.li li::before{content:'';position:absolute;left:0;top:.62em;width:8px;height:2px;
  background:var(--red)}
ul.li--q li::before{background:var(--g4)}
ol.num{list-style:none;counter-reset:c;display:grid;gap:1rem}
ol.num li{counter-increment:c;padding-left:2.1rem;position:relative;color:var(--g2);max-width:74ch}
ol.num li::before{content:counter(c,decimal-leading-zero);position:absolute;left:0;top:.05em;
  font-family:var(--mono);font-size:.68rem;color:var(--red);letter-spacing:.05em}
ol.num li b{color:var(--ink);font-weight:500}

.pay{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:.8rem}
.pay > div{border:1px solid var(--rule);border-radius:3px;padding:.9rem 1rem;background:var(--sheet-2)}
.pay .pc{font-family:var(--serif);font-weight:900;font-size:1.9rem;line-height:1}
.pay .wh{font-family:var(--mono);font-size:.58rem;letter-spacing:.14em;text-transform:uppercase;
  color:var(--g3);margin:.35rem 0 .1rem}
.pay .am{font-family:var(--mono);font-size:.86rem;font-variant-numeric:tabular-nums}

.due{border:1px solid var(--red);border-radius:3px;padding:1.2rem 1.4rem;
  display:flex;justify-content:space-between;align-items:center;gap:1.4rem 2rem;flex-wrap:wrap}
.due > div{flex:1 1 auto;min-width:0}
.due .l{font-family:var(--mono);font-size:.6rem;letter-spacing:.18em;text-transform:uppercase;
  color:var(--red)}
.due .v{font-family:var(--serif);font-weight:900;font-size:clamp(1.8rem,4vw,2.6rem);line-height:1}
.due .d{font-family:var(--mono);font-size:.68rem;line-height:1.75;color:var(--g2);
  text-align:right;flex:0 1 34ch}

.sign{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:2rem;
  margin-top:2.5rem}
.sign > div{padding-top:.2rem}
.sign .nm{font-family:var(--serif6);font-weight:600;font-size:1rem}
.sign .rl{font-family:var(--mono);font-size:.58rem;letter-spacing:.14em;text-transform:uppercase;
  color:var(--g3);margin-top:.15rem}
.sign .ln{margin-top:1.6rem;border-bottom:1px solid var(--rule-2);height:1px}
.sign .lb{font-family:var(--mono);font-size:.54rem;letter-spacing:.14em;text-transform:uppercase;
  color:var(--g4);margin-top:.35rem}

.foot{margin-top:2.6rem;padding-top:1rem;border-top:1px solid var(--rule);
  display:flex;justify-content:space-between;gap:1rem;flex-wrap:wrap;
  font-family:var(--mono);font-size:.56rem;letter-spacing:.12em;text-transform:uppercase;
  color:var(--g3)}

.demo{background:var(--paper-3);border-bottom:1px solid var(--rule);
  font-family:var(--mono);font-size:.6rem;letter-spacing:.1em;color:var(--g2);
  padding:.5rem clamp(.9rem,2.5vw,1.6rem);display:flex;gap:.6rem;align-items:center}
.demo b{color:var(--red);letter-spacing:.16em;text-transform:uppercase;font-weight:400}

/* ── print: one document, A4, no chrome ──────────────────────────────────── */
@page{size:A4;margin:13mm}
@media print{
  .top,.rail,.demo,.printbtn,.chips{display:none!important}
  body{background:#fff;font-size:10.5pt}
  .app{display:block}
  .stage{padding:0}
  .panel:not(.active){display:none}
  .sheet{max-width:none;border:0;box-shadow:none;padding:0;background:#fff;border-radius:0}
  .sheet + .sheet{margin-top:0;page-break-before:always}
  .styl{display:block!important}         /* print every style, not just the open one */
  .styl + .styl{page-break-before:always}
  .sec--rule,.tw,table.t tr,.ph,.cw,.strip figure{page-break-inside:avoid}
  .upd,.due{border:1px solid #000;background:#fff;color:#000}
  .upd h2,.upd p b{color:#000}.upd p{color:#333}.upd .k{color:#000}
  .rail{display:none}
}
"""

# ═════════════════════════════════════════════════════════════════ helpers ═══
SIZES = ["XS", "S", "M", "L", "XL"]
BY_NO = {s["no"]: s for s in STYLES}

def money(v, cur="€"):
    return f"{cur}{v:,.2f}"

def date(iso):
    """2026-09-04 -> 4 Sep 2026 — the form the documents read in."""
    if not iso or iso == "—": return iso
    m = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    y, mo, d = iso.split("-")
    return f"{int(d)} {m[int(mo)-1]} {y}"

def mk(state, title=None):
    """The maturity marker — the logo's own language used as a status glyph.
    sketched = pencil outline · stitched = stitch dashes · born = solid + red dot"""
    t = f'<title>{title or state.capitalize()}</title>'
    if state == "born":
        body = ('<rect x="1" y="1" width="9" height="9" fill="#1B1720"/>'
                '<circle cx="11.5" cy="11.5" r="2.4" fill="#C4122E"/>')
    elif state == "stitched":
        body = ('<rect x="1.6" y="1.6" width="9.8" height="9.8" fill="none" stroke="#1B1720"'
                ' stroke-width="1.5" stroke-dasharray="2.6 2"/>')
    else:
        body = ('<rect x="1.6" y="1.6" width="9.8" height="9.8" fill="none" stroke="#B7B2BA"'
                ' stroke-width="1.2" stroke-dasharray="1.5 2.2"/>')
    return f'<svg class="mk" viewBox="0 0 14 14" role="img" aria-label="{title or state}">{t}{body}</svg>'

def masthead(doctype, title, meta):
    rows = "".join(f"<div>{k} <b>{v}</b></div>" for k, v in meta)
    return f"""<div class="mast">
 <div class="mast__l"><p class="type">{doctype}</p><h1>{title}</h1>
  <p class="who">{PROJECT['client_long']} &middot; {PROJECT['capsule']} &middot; {PROJECT['drop']}</p></div>
 <div class="mast__r">{SVG['wm_solo']}<div class="meta">{rows}</div></div>
</div>"""

def sheetfoot(extra=""):
    return (f'<div class="foot"><span>{PROJECT["studio_long"]}</span>'
            f'<span>{extra or "Sketched. Stitched. BORN."}</span>'
            f'<span>{PROJECT["ref"]}</span></div>')

def dl(pairs):
    cells = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in pairs)
    return f'<dl class="dl">{cells}</dl>'

# ══════════════════════════════════════════════════════════════════ tracker ═══
def phase_card(p):
    live = p["state"] == "stitched"
    items = "".join(
        f'<li class="{ {"born":"done","stitched":"live","sketched":"todo"}[st] }">{mk(st)}'
        f'<span>{txt}<span class="d">{date(d)}</span></span></li>'
        for d, txt, st in p["items"])
    done = sum(1 for _, _, st in p["items"] if st == "born")
    return f"""<div class="ph{' ph--live' if live else ''}">
 <div class="ph__h"><span class="n">{p['n']}</span>
   <span class="win">{done}/{len(p['items'])}</span></div>
 <h3>{p['title']}</h3><p class="win">{p['window']}</p>
 <p class="nt">{p['note']}</p><ul>{items}</ul></div>"""

def tracker():
    photos = "".join(
        f'<figure><img src="{IMG[k]}" alt="{cap}">'
        f'<figcaption>{cap}</figcaption></figure>'
        for k, cap in [("photo_jacket_f", "LY-JK-149 · front"), ("photo_jacket_b", "LY-JK-149 · back"),
                       ("photo_hoodie_f", "LY-HD-025 · front"), ("photo_hoodie_b", "LY-HD-025 · back"),
                       ("photo_bra_f", "ALO006 · front"), ("photo_bra_b", "ALO006 · back")])
    samples = "".join(
        f'<tr><td class="em">{n}</td><td class="c">{date(rec)}</td><td class="c">{date(fit)}</td>'
        f'<td><span class="st-row">{mk(st)}<span>{v}</span></span></td></tr>'
        for n, rec, fit, v, st in SAMPLES)
    styles = "".join(
        f'<tr><td class="c">{s["no"]}</td><td class="em">{s["short"]}</td>'
        f'<td>{s["cat"]}</td><td class="c">{s["fabric"].split(" · ")[0]}</td></tr>'
        for s in STYLES)
    cws = "".join(
        f'<div class="cw"><i style="background:{hexv}"></i><div class="b">'
        f'<div class="code">{code}</div><div class="nm">{nm}</div></div></div>'
        for code, nm, hexv, _ in COLORWAYS)
    return f"""<section class="panel active" id="p-tracker" role="tabpanel" aria-labelledby="t-tracker">
 <div class="sheet">
  {masthead("Development tracker", "Where the capsule stands",
            [("Updated", date(TODAY)), ("Ref", PROJECT["ref"]), ("Ex-factory", date(PROJECT["exfactory"]))])}

  <div class="sec"><div class="upd">
    <p class="k">Latest update &middot; {date(UPDATE['date'])}</p>
    <h2>{UPDATE['title']}</h2><p>{UPDATE['body']}</p>
    <p class="by">{UPDATE['by']} &middot; {PROJECT['studio']}</p>
  </div></div>

  <div class="sec sec--rule"><p class="eyebrow">The journey &middot; three phases</p>
   <div class="phases">{''.join(phase_card(p) for p in PHASES)}</div>
   <p class="note" style="margin-top:1.2rem">Each item carries its own state: a pencil outline is
    still to come, a stitched square is live this week, a solid square with the red dot is done and
    signed off. The same three states run through every document in this room.</p>
  </div>

  <div class="sec sec--rule"><p class="eyebrow">Sample log</p>
   <div class="tw"><table class="t"><thead><tr><th>Round</th><th>Received</th><th>Fitted</th>
    <th>Verdict</th></tr></thead><tbody>{samples}</tbody></table></div>
  </div>

  <div class="sec sec--rule"><p class="eyebrow">SMS 2 &middot; photographed on form, 28 Aug 2026</p>
   <div class="strip">{photos}</div>
   <p class="note" style="margin-top:.9rem">Sample photography, not renders. These are the second
    samples as they arrived from the factory, before the v2.1 corrections.</p>
  </div>

  <div class="sec sec--rule"><p class="eyebrow">The range &middot; 6 styles</p>
   <div class="tw"><table class="t"><thead><tr><th>Style no.</th><th>Style</th><th>Category</th>
    <th>Base quality</th></tr></thead><tbody>{styles}</tbody></table></div>
  </div>

  <div class="sec sec--rule"><p class="eyebrow">Colour standards &middot; approved 27 Mar 2026</p>
   <div class="cws">{cws}</div>
   <p class="note" style="margin-top:.9rem">Screen values approximate the TCX standards. Dye and
    approve against the physical Pantone chip, never against this page.</p>
  </div>

  {sheetfoot("Development tracker &middot; live")}
 </div>
</section>"""

# ════════════════════════════════════════════════════════════════════ quote ═══
def quote():
    rows, fees = [], 0.0
    for gt, gs, items in QUOTE["groups"]:
        rows.append(f'<tr class="grp"><td colspan="2"><span class="gt">{gt}</span><br>'
                    f'<span class="c">{gs}</span></td></tr>')
        for text, qty, amt in items:
            a = f'{money(amt)}' if amt != "" else ""
            q = f'<br><span class="c">{qty}</span>' if qty else ""
            rows.append(f'<tr><td>{text}{q}</td><td class="n">{a}</td></tr>')
            if amt != "": fees += amt
    pt = sum(v for _, v in QUOTE["passthrough"])
    ptrows = "".join(f'<tr><td>{t}</td><td class="n">{money(v)}</td></tr>'
                     for t, v in QUOTE["passthrough"])
    pay = "".join(
        f'<div><div class="pc">{pc}</div><div class="wh">{wh}</div>'
        f'<div class="am">{money(a)}</div></div>' for wh, pc, a in QUOTE["schedule"])
    return f"""<section class="panel" id="p-quote" role="tabpanel" aria-labelledby="t-quote">
 <div class="sheet">
  {masthead("Quote", "Development of a six-style capsule",
            [("No.", QUOTE["no"]), ("Issued", date(QUOTE["issued"])), ("Valid to", date(QUOTE["valid"]))])}
  {dl([("Client", PROJECT["client_long"]), ("Attention", f"{PROJECT['contact']}, {PROJECT['contact_role']}"),
       ("Scope", "6 styles &middot; 5 colour standards"), ("Size range", PROJECT["size_range"]),
       ("Currency", f"{PROJECT['currency']}, excl. VAT"), ("Terms", PROJECT["terms"])])}

  <div class="sec"><p class="eyebrow">Scope and fees</p>
   <div class="tw"><table class="t"><thead><tr><th>Deliverable</th><th class="n">Fee</th></tr></thead>
    <tbody>{''.join(rows)}
     <tr class="sum"><td class="em">Studio fees</td><td class="n em">{money(fees)}</td></tr>
    </tbody></table></div>
  </div>

  <div class="sec sec--rule"><p class="eyebrow">Pass-through, at cost &middot; estimate</p>
   <div class="tw"><table class="t"><tbody>{ptrows}
     <tr class="sum"><td class="em">Estimated pass-through</td><td class="n em">{money(pt)}</td></tr>
    </tbody></table></div>
   <p class="note" style="margin-top:.8rem">Billed at cost as it is incurred, with the supplier
    invoice attached. Nothing here carries a studio margin.</p>
  </div>

  <div class="sec sec--rule"><p class="eyebrow">Payment schedule</p>
   <div class="pay">{pay}</div>
  </div>

  <div class="sec sec--rule"><div class="two">
   <div><h2 class="h">What this assumes</h2>
    <ul class="li" style="margin-top:.9rem">{''.join(f'<li>{a}</li>' for a in QUOTE['assumptions'])}</ul></div>
   <div><h2 class="h">What it does not cover</h2>
    <ul class="li li--q" style="margin-top:.9rem">{''.join(f'<li>{e}</li>' for e in QUOTE['exclusions'])}</ul></div>
  </div></div>

  <div class="sec sec--rule"><p class="eyebrow">How this works</p>
   <p class="body">BORN takes an idea to a manufacturable product. It does not cut or sew, it does
    not buy your materials, and it does not take equity. What it sells is the judgment that sits
    between a drawing and a factory floor &mdash; and three filters every style has to pass before
    it goes anywhere near bulk: <b>can it be made</b>, <b>does it leave margin</b>, and
    <b>does it work on a body</b>.</p>
   <p class="body">Accept by returning a signed copy of this quote. The first invoice issues on
    signature and the briefing starts the same week.</p>
  </div>

  <div class="sign">
   <div><div class="ln"></div><div class="lb">Signed for {PROJECT['client']}</div></div>
   <div><div class="ln"></div><div class="lb">Date</div></div>
  </div>
  {sheetfoot(f"Quote {QUOTE['no']} &middot; valid to {date(QUOTE['valid'])}")}
 </div>
</section>"""

# ══════════════════════════════════════════════════════════════════ invoice ═══
def invoice():
    rows, sub = [], 0.0
    for t, d, q, unit in INVOICE["lines"]:
        amt = q * unit
        sub += amt
        qty = f"{q:,.1f}".rstrip("0").rstrip(".")
        rows.append(f'<tr><td class="em">{t}</td><td>{d}</td><td class="n">{qty}</td>'
                    f'<td class="n">{money(unit)}</td><td class="n">{money(amt)}</td></tr>')
    vat = round(sub * INVOICE["vat_rate"], 2)
    tot = sub + vat
    paid = "".join(f'<tr><td class="c">{date(d)}</td><td>{t}</td><td class="n">{money(v)}</td></tr>'
                   for d, t, v in INVOICE["paid"])
    return f"""<section class="panel" id="p-invoice" role="tabpanel" aria-labelledby="t-invoice">
 <div class="sheet">
  {masthead("Invoice", INVOICE["milestone"],
            [("No.", INVOICE["no"]), ("Issued", date(INVOICE["issued"])), ("Due", date(INVOICE["due"]))])}
  {dl([("Bill to", PROJECT["client_long"]), ("Attention", PROJECT["contact"]),
       ("Against", f"Quote {INVOICE['ref']}"), ("Project", PROJECT["ref"]),
       ("Terms", PROJECT["terms"]), ("Currency", PROJECT["currency"])])}

  <div class="sec">
   <div class="tw"><table class="t"><thead><tr><th>Item</th><th>Detail</th><th class="n">Qty</th>
    <th class="n">Unit</th><th class="n">Amount</th></tr></thead><tbody>{''.join(rows)}
    <tr class="sum"><td colspan="4">Subtotal, excl. VAT</td><td class="n">{money(sub)}</td></tr>
    <tr><td colspan="4">VAT {int(INVOICE['vat_rate']*100)}%</td><td class="n">{money(vat)}</td></tr>
    <tr class="tot"><td colspan="4">Total</td><td class="n">{money(tot)}</td></tr>
   </tbody></table></div>
  </div>

  <div class="sec sec--rule"><div class="due">
    <div><p class="l">Amount due</p><p class="v">{money(tot)}</p></div>
    <p class="d">Payable by {date(INVOICE['due'])}<br>{PROJECT['terms']} from the issue date<br>
     Overdue balances accrue 1.5% per month</p>
  </div></div>

  <div class="sec sec--rule"><div class="two">
   <div><p class="eyebrow">Payment details</p>
    {dl([("Account name", PROJECT["studio"]), ("IBAN", PROJECT["iban"]),
         ("BIC / SWIFT", PROJECT["bic"]), ("VAT no.", PROJECT["vat"]),
         ("Reference", INVOICE["no"])])}</div>
   <div><p class="eyebrow">Already settled on this project</p>
    <div class="tw"><table class="t" style="min-width:0"><tbody>{paid}</tbody></table></div>
    <p class="note" style="margin-top:.8rem">Milestone 3 &mdash; 20% &mdash; issues at ex-factory,
     scheduled {date(PROJECT['exfactory'])}.</p></div>
  </div></div>

  <div class="sec sec--rule"><p class="eyebrow">What milestone 2 covered</p>
   <p class="body">Factory pairing and contract, lab dip management to chip across five standards
    and three qualities, two full sample rounds with documented fit sessions, and the tech pack
    revision that carried SMS 1's eleven corrections into v2.0. SMS 2 was delivered on
    {date('2026-08-28')} and fitted on {date('2026-09-04')}.</p>
   <p class="body">Quote your reference <b>{INVOICE['no']}</b> on the transfer so it reconciles
    against the right milestone.</p>
  </div>
  {sheetfoot(f"Invoice {INVOICE['no']} &middot; due {date(INVOICE['due'])}")}
 </div>
</section>"""

# ═══════════════════════════════════════════════════════════════ tech pack ═══
def techpack():
    chips = "".join(f'<button class="chip" data-s="{s["no"]}" aria-pressed="false">{s["no"]}</button>'
                    for s in STYLES)
    plates = []
    for s in STYLES:
        pom = "".join(
            f'<tr><td class="c">{c}</td><td>{p}</td>'
            + "".join(f'<td class="n">{v:.1f}</td>' for v in (xs, sm, md, lg, xl))
            + f'<td class="n">&plusmn;{tol:.1f}</td></tr>'
            for c, p, xs, sm, md, lg, xl, tol in s["pom"])
        bom = "".join(
            f'<tr><td class="em">{c}</td><td>{d}</td><td>{sup}</td><td class="c">{ref}</td>'
            f'<td class="c">{col}</td><td class="n">{cons}</td></tr>'
            for c, d, sup, ref, col, cons in s["bom"])
        det = "".join(f'<li>{d}</li>' for d in s["details"])
        build = "".join(f'<li>{b}</li>' for b in s["build"])
        plates.append(f"""<div class="styl" data-s="{s['no']}">
 <div class="two">
  <div class="plate"><img src="{IMG[s['img']]}" alt="{s['name']} — technical flat with callouts"></div>
  <div>
   <p class="eyebrow">{s['cat']} &middot; {s['no']}</p>
   <h2 class="h">{s['name']}</h2>
   <p class="body" style="margin-top:.7rem">{s['hand']}.</p>
   {dl([("Base quality", s["fabric"].split(" · ")[0]),
        ("Composition", s["fabric"].split(" · ")[1]),
        ("Weight", s["fabric"].split(" · ")[2]),
        ("Base size", PROJECT["base_size"]), ("Grading", PROJECT["size_range"])])}
   <p class="eyebrow" style="margin-top:1.4rem">Construction callouts</p>
   <ul class="li">{det}</ul>
  </div>
 </div>

 <div class="sec sec--rule"><p class="eyebrow">Bill of materials</p>
  <div class="tw"><table class="t"><thead><tr><th>Component</th><th>Description</th><th>Supplier</th>
   <th>Ref</th><th>Colour</th><th class="n">Cons.</th></tr></thead><tbody>{bom}</tbody></table></div>
 </div>

 <div class="sec sec--rule"><p class="eyebrow">Points of measure &middot; centimetres, base size {PROJECT['base_size']}</p>
  <div class="tw"><table class="t"><thead><tr><th>Code</th><th>Point of measure</th>
   {''.join(f'<th class="n">{z}</th>' for z in SIZES)}<th class="n">Tol.</th></tr></thead>
   <tbody>{pom}</tbody></table></div>
  <p class="note" style="margin-top:.8rem">Half measurements are marked &frac12; and taken flat,
   relaxed, on a conditioned sample. Measure after 24 hours of rest &mdash; a knit read straight
   off the press will lie to you.</p>
 </div>

 <div class="sec sec--rule"><p class="eyebrow">Construction and finishing</p>
  <ol class="num">{build}</ol>
 </div>
</div>""")
    return f"""<section class="panel" id="p-techpack" role="tabpanel" aria-labelledby="t-techpack">
 <div class="sheet">
  {masthead("Tech pack", "Factory-ready specification",
            [("Revision", "v2.0"), ("Released", date("2026-08-14")), ("Styles", "6")])}
  {dl([("Client", PROJECT["client_long"]), ("Capsule", f"{PROJECT['capsule']} &middot; {PROJECT['drop']}"),
       ("Size range", PROJECT["size_range"]), ("Base size", PROJECT["base_size"]),
       ("Colour standards", "5 TCX"), ("Units", f"{PROJECT['units']:,}")])}

  <div class="sec"><p class="eyebrow">Revision history</p>
   <div class="tw"><table class="t"><thead><tr><th>Rev</th><th>Date</th><th>Change</th></tr></thead><tbody>
    <tr><td class="c">v1.0</td><td class="c">{date('2026-04-22')}</td><td>Initial release &mdash; 6 styles, factory-ready</td></tr>
    <tr><td class="c">v1.1</td><td class="c">{date('2026-05-22')}</td><td>Qualities confirmed against approved lab dips; KT-PLX210 replaced the 190 g/m² for the shorts</td></tr>
    <tr><td class="c">v2.0</td><td class="c">{date('2026-08-14')}</td><td>Post SMS 1 &mdash; 11 corrections across 6 styles</td></tr>
    <tr><td class="c">v2.1</td><td class="c">{date('2026-09-08')}</td><td>Post SMS 2 &mdash; 3 pattern corrections, 2 factory settings <span class="out-mk">in progress</span></td></tr>
   </tbody></table></div>
  </div>

  <div class="sec sec--rule"><p class="eyebrow">Select a style</p>
   <div class="chips" role="group" aria-label="Style">{chips}</div>
   {''.join(plates)}
  </div>

  <div class="sec sec--rule"><p class="eyebrow">Applies to every style</p>
   <ul class="li">
    <li>Sew to the graded POM, not to the flat sketch. Where the two disagree, the POM wins and BORN gets a call.</li>
    <li>All measurements in centimetres. Any measurement outside its tolerance on the size set stops the style until it is signed off in writing.</li>
    <li>Fabric relaxed 24 hours before cutting. Shrinkage tested at 3 washes &mdash; more than 3% and the quality is rejected.</li>
    <li>Colour approved against the physical TCX chip under D65. Screen values on any document are a reference, never an approval.</li>
    <li>Care and composition labelling to EU 1007/2011, in the languages listed on the artwork sheet.</li>
    <li>No substitution of any component in this BOM without written approval from BORN Studio.</li>
   </ul>
  </div>
  {sheetfoot("Tech pack v2.0 &middot; 6 styles")}
 </div>
</section>"""

# ═════════════════════════════════════════════════════════════════ fitting ═══
BADGE_OUT = '<span class="out-mk">Correct</span>'
BADGE_OK  = '<span class="ok-mk">Pass</span>'

def fitting():
    # summary across the range, computed from the measured values against spec tolerance
    summary, detail = [], []
    for s in STYLES:
        tol = {c: t for c, _, _, _, _, _, _, t in s["pom"]}
        pomname = {c: p for c, p, *_ in s["pom"]}
        rows = FITTING["measured"][s["no"]]
        outs = [(c, sp, ms) for c, sp, ms in rows if abs(ms - sp) > tol[c] + 1e-9]
        plural = "s" if len(outs) > 1 else ""
        verdict = "Approve to size set" if not outs else f"Correct &mdash; {len(outs)} point{plural}"
        n_out = f'<span class="out">{len(outs)}</span>' if outs else "0"
        badge = BADGE_OUT if outs else BADGE_OK
        summary.append(
            f'<tr><td class="c">{s["no"]}</td><td class="em">{s["short"]}</td>'
            f'<td class="n">{len(rows)}</td><td class="n">{n_out}</td>'
            f'<td>{badge} <span class="c">{verdict}</span></td></tr>')
        def pom_row(c, sp, ms):
            over = abs(ms - sp) > tol[c] + 1e-9
            return (f'<tr><td class="c">{c}</td><td>{pomname[c]}</td><td class="n">{sp:.1f}</td>'
                    f'<td class="n">{ms:.2f}</td>'
                    f'<td class="n{" out" if over else ""}">{ms - sp:+.2f}</td>'
                    f'<td class="n">&plusmn;{tol[c]:.1f}</td>'
                    f'<td>{BADGE_OUT if over else BADGE_OK}</td></tr>')
        body = "".join(pom_row(c, sp, ms) for c, sp, ms in rows)
        photos = ""
        if s["photo"]:
            cards = "".join(
                f'<figure><img src="{IMG[k]}" alt="{s["no"]} sample">'
                f'<figcaption>{"front" if k.endswith("_f") else "back"}</figcaption></figure>'
                for k in s["photo"])
            photos = f'<div class="strip" style="margin-top:1rem;max-width:340px">{cards}</div>' 
        detail.append(f"""<div class="styl" data-s="{s['no']}">
 <p class="eyebrow">{s['no']} &middot; {s['cat']}</p><h2 class="h">{s['short']}</h2>
 {photos}
 <div class="tw" style="margin-top:1.1rem"><table class="t"><thead><tr><th>Code</th>
  <th>Point of measure</th><th class="n">Spec</th><th class="n">Measured</th>
  <th class="n">Dev.</th><th class="n">Tol.</th><th>Verdict</th></tr></thead>
  <tbody>{body}</tbody></table></div>
</div>""")
    chips = "".join(f'<button class="chip" data-s="{s["no"]}" aria-pressed="false">{s["no"]}</button>'
                    for s in STYLES)
    corr = "".join(
        f'<li><b>{BY_NO[sn]["short"]} &middot; {sn}{"" if pt == "—" else " &middot; " + pt}</b><br>{txt}'
        f'<br><span class="c" style="color:var(--red)">{owner}</span></li>'
        for sn, pt, txt, owner in FITTING["corrections"])
    holds = "".join(f'<li>{h}</li>' for h in FITTING["holds"])
    return f"""<section class="panel" id="p-fitting" role="tabpanel" aria-labelledby="t-fitting">
 <div class="sheet">
  {masthead("Fitting report", f"{FITTING['sample']} &middot; fit session 02",
            [("No.", FITTING["no"]), ("Session", date(FITTING["session"])), ("Size", FITTING["size"])])}
  {dl([("Sample round", FITTING["sample"]), ("Received", date(FITTING["received"])),
       ("Measured against", FITTING["spec"]), ("Form", FITTING["form"]),
       ("Present", FITTING["present"]), ("Styles fitted", "6")])}

  <div class="sec"><p class="eyebrow">Verdict</p>
   <div class="due"><div><p class="l">Outcome</p><p class="v" style="font-size:clamp(1.4rem,3vw,2rem)">{FITTING['verdict']}</p></div>
    <p class="d" style="max-width:34ch;text-align:left">{FITTING['verdict_note']}</p></div>
  </div>

  <div class="sec sec--rule"><p class="eyebrow">Across the range</p>
   <div class="tw"><table class="t"><thead><tr><th>Style no.</th><th>Style</th>
    <th class="n">Points</th><th class="n">Out of tol.</th><th>Verdict</th></tr></thead>
    <tbody>{''.join(summary)}</tbody></table></div>
  </div>

  <div class="sec sec--rule"><p class="eyebrow">Measured &middot; select a style</p>
   <div class="chips" role="group" aria-label="Style">{chips}</div>
   {''.join(detail)}
  </div>

  <div class="sec sec--rule"><p class="eyebrow">Corrections into v2.1</p>
   <ol class="num">{corr}</ol>
   <p class="note" style="margin-top:1rem">Three of these are pattern changes and go into the tech
    pack. Two are factory settings &mdash; a bonding jig and a binder foot &mdash; and cost a
    re-press, not a re-cut.</p>
  </div>

  <div class="sec sec--rule"><p class="eyebrow">Holds &mdash; do not change these</p>
   <ul class="li li--q">{holds}</ul>
  </div>

  <div class="sign">
   <div><div class="nm">{PROJECT['studio_person']}</div><div class="rl">{PROJECT['studio']}</div>
    <div class="ln"></div><div class="lb">Signature and date</div></div>
   <div><div class="nm">{PROJECT['contact']}</div><div class="rl">{PROJECT['client']}</div>
    <div class="ln"></div><div class="lb">Signature and date</div></div>
  </div>
  {sheetfoot(f"Fitting report {FITTING['no']} &middot; {date(FITTING['session'])}")}
 </div>
</section>"""

# ════════════════════════════════════════════════════════════════ handover ═══
def handover():
    plan = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in HANDOVER["plan"])
    arch = "".join(
        f'<div><h3 class="sh">{g}</h3><ul class="li">{"".join(f"<li>{i}</li>" for i in items)}</ul></div>'
        for g, items in HANDOVER["archive"])
    nxt = "".join(f"<li>{n}</li>" for n in HANDOVER["next"])
    sign = "".join(
        f'<div><div class="nm">{who}</div><div class="rl">{org} &middot; {role}</div>'
        f'<div class="ln"></div><div class="lb">Signature and date</div></div>'
        for org, who, role in HANDOVER["signoff"])
    renders = "".join(
        f'<figure><img src="{IMG[k]}" alt="{cap}"><figcaption>{cap}</figcaption></figure>'
        for k, cap in [("render_periwinkle", "17-3919 Purple Impression"),
                       ("render_whisper", "11-0701 Whisper White"),
                       ("render_black", "19-3911 Black Beauty"),
                       ("render_blue", "17-3919 · jacket and short")])
    return f"""<section class="panel" id="p-handover" role="tabpanel" aria-labelledby="t-handover">
 <div class="sheet">
  {masthead("Handover", "What LAYO owns at the end",
            [("No.", HANDOVER["no"]), ("Issues", date(HANDOVER["due"])), ("Status", HANDOVER["status"])])}

  <div class="sec"><p class="body">This is the document that closes the project. It issues at
   ex-factory with the production figures filled in, and it lists everything that transfers to
   LAYO &mdash; patterns, specifications, supplier references, colour approvals and the full
   development record. <b>Nothing is held back.</b> If LAYO takes the next drop elsewhere, it
   leaves with a complete, executable file.</p>
   <p class="note" style="margin-top:1rem">Figures below are the contracted plan. Achieved units,
    the AQL result, landed cost and the shipping record are entered at ex-factory, scheduled
    {date(HANDOVER['due'])}.</p>
  </div>

  <div class="sec sec--rule"><p class="eyebrow">The programme</p>
   <dl class="dl">{plan}</dl>
  </div>

  <div class="sec sec--rule"><p class="eyebrow">Production record &middot; completed at ex-factory</p>
   <div class="tw"><table class="t"><thead><tr><th>Line</th><th>Planned</th><th>Achieved</th></tr></thead><tbody>
    <tr><td class="em">Units shipped</td><td class="c">1,800</td><td class="c">&mdash;</td></tr>
    <tr><td class="em">Final inspection</td><td class="c">AQL 2.5 / 4.0</td><td class="c">&mdash;</td></tr>
    <tr><td class="em">Ex-factory date</td><td class="c">{date(HANDOVER['due'])}</td><td class="c">&mdash;</td></tr>
    <tr><td class="em">Programme length</td><td class="c">43 weeks</td><td class="c">&mdash;</td></tr>
    <tr><td class="em">Cartons / gross weight</td><td class="c">&mdash;</td><td class="c">&mdash;</td></tr>
   </tbody></table></div>
  </div>

  <div class="sec sec--rule"><p class="eyebrow">The archive &middot; delivered on handover</p>
   <div class="two" style="grid-template-columns:1fr 1fr;gap:1.6rem 2.4rem">{arch}</div>
  </div>

  <div class="sec sec--rule"><p class="eyebrow">Approved colourway sets</p>
   <div class="strip">{renders}</div>
   <p class="note" style="margin-top:.9rem">Visualised at the design stage, 3 Apr 2026, and carried
    through to the approved lab dips.</p>
  </div>

  <div class="sec sec--rule"><p class="eyebrow">For the next drop</p>
   <ul class="li">{nxt}</ul>
  </div>

  <div class="sec sec--rule"><p class="eyebrow">Sign-off</p>
   <p class="body">Signing below confirms the archive above was received in full and the programme
    is closed. It does not waive any latent defect claim against the factory.</p>
   <div class="sign">{sign}</div>
  </div>
  {sheetfoot(f"Handover {HANDOVER['no']}")}
 </div>
</section>"""

# ══════════════════════════════════════════════════════════════════ chrome ═══
DOCS = [("tracker", "Tracker"), ("quote", "Quote"), ("invoice", "Invoice"),
        ("techpack", "Tech pack"), ("fitting", "Fitting"), ("handover", "Handover")]

def top():
    tabs = "".join(
        f'<button role="tab" id="t-{k}" aria-controls="p-{k}" data-doc="{k}" '
        f'aria-selected="{"true" if i == 0 else "false"}">{lbl}</button>'
        for i, (k, lbl) in enumerate(DOCS))
    return f"""<div class="demo"><b>Demo</b><span>Sample project room built on the approved LAYO
 design-stage deck. Swap the PROJECT block in <code>tools/build_deliverables.py</code> to point it
 at any client.</span></div>
<header class="top"><div class="top__in">
 <a class="mark" href="#p-tracker" aria-label="BORN Studio">{SVG['wm_solo']}
  <span class="sub">Project room</span></a>
 <div class="docnav" role="tablist" aria-label="Documents">{tabs}</div>
 <button class="printbtn" id="printBtn" type="button">&#8595;&nbsp; Print / PDF</button>
</div></header>"""

def rail():
    done = sum(1 for p in PHASES for _, _, st in p["items"] if st == "born")
    total = sum(len(p["items"]) for p in PHASES)
    live = next(p for p in PHASES if p["state"] == "stitched")
    nxt = next(((d, t) for p in PHASES for d, t, st in p["items"] if st == "sketched"), None)
    bars = ""
    for p in PHASES:
        cls = {"born": "done", "stitched": "live", "sketched": "todo"}[p["state"]]
        bars += f'<i class="{cls}"></i>' + ('<b></b>' if p["state"] == "stitched" else "")
    return f"""<aside class="rail"><div class="rail__in">
 <div><p class="k">Project room</p><h2>{PROJECT['client']}</h2>
  <p class="k" style="color:var(--g3);margin-top:.35rem">Performance Luxury</p></div>
 <div class="prog" aria-label="Progress across the three phases">{bars}</div>
 <div class="now">
  <p class="ph">{mk('stitched')} {live['n']} &middot; {live['title']}</p>
  <p>{done} of {total} milestones signed off. Next up &mdash;
   {nxt[1].split(' — ')[0].split(',')[0]}, {date(nxt[0])}.</p>
 </div>
 <div class="sep"></div>
 <dl>
  <div><dt>Capsule</dt><dd>{PROJECT['capsule']}</dd></div>
  <div><dt>Drop</dt><dd>{PROJECT['drop']} &middot; 6 styles</dd></div>
  <div><dt>Reference</dt><dd class="mono">{PROJECT['ref']}</dd></div>
  <div><dt>Size range</dt><dd class="mono">{PROJECT['size_range']} &middot; base {PROJECT['base_size']}</dd></div>
  <div><dt>Opened</dt><dd class="mono">{date(PROJECT['opened'])}</dd></div>
  <div><dt>Ex-factory</dt><dd class="mono">{date(PROJECT['exfactory'])}</dd></div>
  <div><dt>Your contact</dt><dd>{PROJECT['studio_person']}, {PROJECT['studio']}</dd></div>
 </dl>
 <div class="foot">
  <div>{PROJECT['studio_long']}</div>
  <div><a href="mailto:{PROJECT['studio_email']}">{PROJECT['studio_email']}</a></div>
  <div style="color:var(--red);margin-top:.5rem">From idea to life</div>
 </div>
</div></aside>"""

JS = r"""<script>
(function(){
  document.documentElement.classList.add('js');
  // ── document tabs ─────────────────────────────────────────────────────────
  var tabs=[].slice.call(document.querySelectorAll('.docnav [data-doc]'));
  function show(key){
    tabs.forEach(function(t){
      var on=t.dataset.doc===key;
      t.setAttribute('aria-selected',on?'true':'false');
      var p=document.getElementById('p-'+t.dataset.doc);
      if(p)p.classList.toggle('active',on);
    });
    if(location.hash.slice(1)!==key)history.replaceState(null,'','#'+key);
    window.scrollTo({top:0,behavior:'instant' in document.body.style?'instant':'auto'});
  }
  tabs.forEach(function(t){t.addEventListener('click',function(){show(t.dataset.doc);});});
  tabs.forEach(function(t,i){t.addEventListener('keydown',function(e){
    var d=e.key==='ArrowRight'?1:e.key==='ArrowLeft'?-1:0;
    if(!d)return;e.preventDefault();
    var n=tabs[(i+d+tabs.length)%tabs.length];n.focus();show(n.dataset.doc);
  });});
  if(location.hash){var k=location.hash.slice(1);
    if(document.getElementById('p-'+k))show(k);}

  // ── per-panel style pickers (tech pack, fitting) ─────────────────────────
  document.querySelectorAll('.panel').forEach(function(panel){
    var chips=[].slice.call(panel.querySelectorAll('.chip[data-s]')),
        plates=[].slice.call(panel.querySelectorAll('.styl[data-s]'));
    if(!chips.length)return;
    function pick(no){
      chips.forEach(function(c){c.setAttribute('aria-pressed',c.dataset.s===no?'true':'false');});
      plates.forEach(function(p){p.classList.toggle('on',p.dataset.s===no);});
    }
    chips.forEach(function(c){c.addEventListener('click',function(){pick(c.dataset.s);});});
    pick(chips[0].dataset.s);
  });

  // ── print the document that is open ──────────────────────────────────────
  document.getElementById('printBtn').addEventListener('click',function(){window.print();});
})();
</script>"""

# ══════════════════════════════════════════════════════════════════ output ═══
BODY = (DEFS + top() + '<div class="app">' + rail() + '<main class="stage">'
        + tracker() + quote() + invoice() + techpack() + fitting() + handover()
        + '</main></div>' + JS)
HEAD = "<style>\n" + FONTS + "\n" + CSS + "\n</style>"

artifact = "<title>BORN Project Room</title>\n" + HEAD + "\n" + BODY
open(f"{W}/deliverables_artifact.html", "w", encoding="utf-8").write(artifact)

page = ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
  '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
  '<title>BORN Project Room &mdash; LAYO</title>\n'
  '<meta name="description" content="BORN Studio client project room — development tracker, '
  'quote, invoice, tech pack, fitting report and handover.">\n'
  '<meta name="theme-color" content="#F2EEE6">\n'
  f'<link rel="icon" href="{FAVICON}">\n' + HEAD + "\n</head>\n<body>\n" + BODY + "\n</body>\n</html>\n")
open(f"{O}/index.html", "w", encoding="utf-8").write(page)
print(f"deliverables/index.html: {len(page)//1024} KB   artifact: {len(artifact)//1024} KB")
