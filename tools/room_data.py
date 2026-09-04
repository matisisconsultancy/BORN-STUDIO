#!/usr/bin/env python3
"""BORN Studio — project content.

This is the file María's team edits. It holds one project: who it is for, the
three phases, the styles with their technical specification, the logbook
entries, and the four compiled documents. Nothing here knows how anything looks
— tools/build_room.py turns it into the room.

To open a room for a new client: copy this file, replace PROJECT, STYLES and
ENTRIES, and run `python3 tools/build_room.py`.
"""

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


# ═════════════════════════════════════════════════════════════════ the logbook ═
# The client reads this top to bottom and watches the garment come to life.
#
#   phase  — which register the entry is drawn in: sketched · stitched · born
#   state  — whether it has happened: done · now · next
#   kind   — the label the reader sees
#   pay    — the payload, which changes with the kind of information:
#            decision · materials · colour · flats · renders · sample
#            measure · release · approval · alert   (or None for a plain note)
#
# Anatomy stays the same on every entry — date, kind, headline, body — so the
# page is scannable. Only the payload changes, so density follows the content.

ENTRIES = [
 dict(date="2026-02-16", phase="sketched", state="done", kind="Opening note",
   title="The room is open.",
   body="Everything about this capsule lives here — every decision, every sample, "
        "every measurement, with the date it happened and the reason behind it. "
        "You will not have to ask where we are. Scroll down and you will see the "
        "styles go from drawn, to sewn, to made. Anything that needs you is marked "
        "in red and says what it needs and by when."),

 dict(date="2026-02-20", phase="sketched", state="done", kind="Decision",
   title="Six styles, not nine.",
   body="LAYO came in with nine. Three did not survive the filters, and cutting them "
        "early is what keeps the other six affordable.",
   pay=dict(type="decision",
     chosen="6 styles, one mill, one maker",
     considered="9 styles, two mills, split MOQ",
     why="Two of the nine were legging bodies that duplicated WB082601 at a different "
         "rise — the same pattern work, twice the sampling. The third needed a cotton "
         "jersey no performance mill carries, which meant a second supplier and a "
         "second minimum. Holding the range at six keeps every style inside one mill's "
         "MOQ and takes roughly €8,000 out of the sampling budget before a single metre "
         "is cut.",
     cost="−€8,000 sampling · −4 weeks")),

 dict(date="2026-02-27", phase="sketched", state="done", kind="Materials",
   title="Nine qualities handled. Three carried forward.",
   body="Weight, stretch, recovery and hand, tested against what each style has to do "
        "on a body. Recovery is what separates activewear that lasts from activewear "
        "that bags at the knee after three wears.",
   pay=dict(type="materials", rows=[
     ("KT-INT240", "Interlock, 76% NY / 24% EL", "240 g/m²", "4-way", "Excellent",
      "Carried — jacket", True),
     ("KT-SSK260", "Second-skin interlock, 75% rNY / 25% EL", "260 g/m²", "4-way", "Excellent",
      "Carried — leggings", True),
     ("KT-RIB280", "Performance rib, 78% NY / 22% EL", "280 g/m²", "4-way", "Very good",
      "Carried — bra top", True),
     ("KT-PLX190", "PureLuxe interlock", "190 g/m²", "4-way", "Fair",
      "Dropped — translucent under stretch", False),
     ("NW-FT280", "French terry, 100% CO", "280 g/m²", "None", "n/a",
      "Dropped — no elastane, hem will not hold", False),
     ("KT-CMP310", "Compression knit", "310 g/m²", "2-way", "Good",
      "Dropped — too heavy for the silhouette", False)])),

 dict(date="2026-03-13", phase="sketched", state="done", kind="Release",
   title="Technical sketches — six styles, front, back and side.",
   body="Every seam, every closure, every stitch type called out where the factory "
        "will look for it. This is the drawing a maker can quote from without a phone call.",
   pay=dict(type="flats", styles=["LY-JK-149", "ALO006", "LY-HD-025"])),

 dict(date="2026-03-27", phase="sketched", state="done", kind="Colour",
   title="Five standards, approved to chip.",
   body="Screens lie about colour. These were chosen against physical Pantone chips "
        "under D65 and every lab dip from here is judged against the chip, never "
        "against a file.",
   pay=dict(type="colour")),

 dict(date="2026-04-03", phase="sketched", state="done", kind="Release",
   title="3D visualisation — four colourway sets.",
   body="Rendered before a metre was cut, so the range could be judged as a range: "
        "how the jacket sits over the short, whether the periwinkle carries a full "
        "look or only a piece of one.",
   pay=dict(type="renders",
     keys=[("render_periwinkle", "17-3919 Purple Impression"),
           ("render_whisper", "11-0701 Whisper White"),
           ("render_black", "19-3911 Black Beauty"),
           ("render_blue", "17-3919 · jacket and short")])),

 dict(date="2026-04-08", phase="sketched", state="done", kind="Release",
   title="Design stage delivered.",
   body="Sketches, colourways and renders in one document. The last point at which a "
        "design change is free — after this, every change costs a sample.",
   pay=dict(type="release", name="Design stage", rev="—", note="6 styles · 5 standards")),

 dict(date="2026-04-22", phase="sketched", state="done", kind="Release",
   title="Tech pack v1.0 — factory-ready.",
   body="Bill of materials, graded points of measure with tolerances, construction "
        "and grading intent. Six styles. This is the file a factory builds from.",
   pay=dict(type="release", name="Tech pack", rev="v1.0", go="techpack",
            note="BOM · graded POM · construction")),

 # ── phase 02 ───────────────────────────────────────────────────────────────
 dict(date="2026-05-06", phase="stitched", state="done", kind="Decision",
   title="Paired with the maker who was not the cheapest.",
   body="Two factories quoted. The gap was 11% on unit cost, and we went the other way.",
   pay=dict(type="decision",
     chosen="Vilar — 4-needle 6-thread flatlock in-house",
     considered="The quote 11% under, coverstitch only",
     why="Three of the six styles are specified flatlock because a coverstitched crotch "
         "seam is what a customer feels when she squats. The cheaper maker would have "
         "subcontracted that operation, which means a second factory, a second quality "
         "standard and nobody to hold responsible when a seam fails. Eleven percent on "
         "unit cost is cheaper than a returns rate.",
     cost="+11% unit cost · −1 supplier · one line responsible")),

 dict(date="2026-05-29", phase="stitched", state="done", kind="Note",
   title="Lab dips submitted — fifteen submissions.",
   body="Five standards across three qualities. Each quality takes dye differently, so "
        "Black Beauty on the rib and Black Beauty on the compression knit are two "
        "separate approvals, not one."),

 dict(date="2026-06-19", phase="stitched", state="done", kind="Approval",
   title="Lab dips approved. All five to chip, first round.",
   body="Unusual — a first-round pass on five standards across three qualities normally "
        "takes two. Credit the mill.",
   pay=dict(type="approval", status="given", what="Colour approval, 5 TCX standards",
            who="Layo Ade-Ojo", when="2026-06-19")),

 dict(date="2026-07-10", phase="stitched", state="done", kind="Sample",
   title="SMS 1 arrived — six styles, size M.",
   body="First time the drawing exists as an object. Photographed on the form before "
        "anything was touched.",
   pay=dict(type="sample", round="SMS 1",
            keys=[("photo_jacket_f", "LY-JK-149 · front"), ("photo_jacket_b", "LY-JK-149 · back"),
                  ("photo_hoodie_f", "LY-HD-025 · front"), ("photo_bra_f", "ALO006 · front")],
            verdict="Corrected — re-sample", ok=False)),

 dict(date="2026-07-17", phase="stitched", state="done", kind="Measure",
   title="Fit session 01 — eleven points off, across five styles.",
   body="Expected on a first sample. The pattern is what matters: the jacket came back "
        "small through the chest and bicep, which is a block problem, not a cutting one.",
   pay=dict(type="measure", session="FIT-01", spec="Tech pack v1.0", clear=11, total=22,
     rows=[("ALO006", "C01", "Sleeve length, CB to cuff", 79.0, 81.4, 0.5, "Pattern"),
           ("LY-JK-149", "A01", "Chest ½", 45.0, 43.2, 1.0, "Block"),
           ("LY-JK-149", "C02", "Bicep ½", 16.6, 15.6, 0.4, "Block"),
           ("LY-HD-025", "B02", "Across shoulder, dropped", 54.0, 51.8, 0.8, "Pattern"),
           ("WB082601", "B02", "Back rise incl. waistband", 42.0, 40.6, 0.5, "Pattern"),
           ("LY-6012156", "B03", "Inseam", 15.2, 16.4, 0.3, "Cutting")],
     more=5, go="fitting")),

 dict(date="2026-08-14", phase="stitched", state="done", kind="Release",
   title="Tech pack v2.0 — eleven corrections carried in.",
   body="Every correction from fit session 01, written into the spec the factory cuts "
        "from. Nothing was left in an email.",
   pay=dict(type="release", name="Tech pack", rev="v2.0", go="techpack",
            note="11 corrections · 6 styles")),

 dict(date="2026-08-28", phase="stitched", state="done", kind="Sample",
   title="SMS 2 arrived.",
   body="Cut to v2.0. The jacket now reads square through the chest and the panel "
        "geometry sits correctly on the body — which is the hard part done.",
   pay=dict(type="sample", round="SMS 2",
            keys=[("photo_jacket_f", "LY-JK-149 · front"), ("photo_jacket_b", "LY-JK-149 · back"),
                  ("photo_hoodie_b", "LY-HD-025 · back"), ("photo_bra_b", "ALO006 · back")],
            verdict="Approve to size set", ok=True)),

 dict(date="2026-09-04", phase="stitched", state="now", kind="Measure",
   title="Fit session 02 — two styles clear, four carry a correction.",
   body="Seventeen of twenty-two points measured clean. The five that did not are small, "
        "and two of them are factory settings rather than pattern changes — a bonding jig "
        "and a binder foot — which cost a re-press, not a re-cut. No third full sample "
        "round is needed, which keeps €3,120 out of the budget and holds the ex-factory date.",
   pay=dict(type="measure", session="FIT-02", spec="Tech pack v2.0", clear=17, total=22,
     rows=[("LY-JK-149", "D01", "Stand collar height, CB", 7.5, 8.2, 0.2, "Pattern"),
           ("LY-JK-149", "C03", "Cuff opening ½, bonded", 9.0, 9.4, 0.3, "Factory"),
           ("ALO006", "C05", "Thumb hole position", 6.0, 7.1, 0.3, "Pattern"),
           ("LY-HD-025", "D01", "Hood height, CF to top", 36.0, 37.2, 0.5, "Pattern"),
           ("WB082608", "A02", "Contrast trim width", 0.6, 0.72, 0.1, "Factory")],
     more=0, go="fitting")),

 dict(date="2026-09-05", phase="stitched", state="now", kind="Watch",
   title="Silicone trims are running a three-week lead.",
   body="Not a problem yet, and it becomes one if it waits.",
   pay=dict(type="alert",
     risk="Logos and zipper pulls quoted at three weeks against the two we planned. "
          "Ordered at PPS sign-off, they land after the bulk line is booked and push "
          "ex-factory into the week of 18 December.",
     fix="Order the trims now, against v2.1. None of the five corrections touch a trim, "
         "so there is nothing left to decide. This removes the dependency entirely and "
         "costs nothing but committing €1,240 three weeks earlier than planned.",
     owner="BORN · awaiting your yes")),

 dict(date="2026-09-08", phase="stitched", state="next", kind="Approval",
   title="Tech pack v2.1 needs your sign-off.",
   body="Three pattern corrections and two factory settings. Once you sign, the size "
        "set is cut to v2.1 and the 11 December ex-factory date holds. Every working "
        "day past the 8th moves that date by one.",
   pay=dict(type="approval", status="waiting", what="Tech pack v2.1 — 5 corrections",
            who="Layo Ade-Ojo", when="2026-09-08")),

 dict(date="2026-09-18", phase="stitched", state="next", kind="Sample",
   title="Size set, XS to XL, all six styles.",
   body="The first time the grade is tested rather than calculated. Every style measured "
        "at every size against the graded POM."),

 dict(date="2026-10-02", phase="stitched", state="next", kind="Approval",
   title="Final approved sample.",
   body="The sample the whole bulk run is judged against. Sealed, signed and held by both sides."),

 # ── phase 03 ───────────────────────────────────────────────────────────────
 dict(date="2026-10-16", phase="born", state="next", kind="Approval",
   title="Pre-production sample signed off.",
   body="Cut from bulk fabric, on the bulk line, by the operators who will make the order. "
        "The last gate before 1,800 units."),

 dict(date="2026-10-30", phase="born", state="next", kind="Note",
   title="Bulk fabric in-house at the factory.",
   body="Shade-banded and relaxed 24 hours before cutting."),

 dict(date="2026-11-20", phase="born", state="next", kind="Note",
   title="Inline QC visit.",
   body="Caught on the line, while it can still be fixed. Finding a problem at final "
        "inspection means reworking a container."),

 dict(date="2026-12-04", phase="born", state="next", kind="Measure",
   title="Final inspection — AQL 2.5 major, 4.0 minor.",
   body="Sampled to the standard, measured against the sealed sample, with a written report."),

 dict(date="2026-12-11", phase="born", state="next", kind="Release",
   title="Ex-factory, and everything transfers to LAYO.",
   body="Patterns, specifications, supplier references, colour approvals and the full "
        "development record. Nothing held back.",
   pay=dict(type="release", name="Handover", rev="HO-2026-031", go="handover",
            note="Patterns · specs · suppliers · record")),
]

# ═══════════════════════════════════════════════ how the room reads its states ═
# Register = which phase of the craft the entry belongs to. It sets the world:
# the ground, the rule, the texture. State = whether it has happened yet. It
# sets the marker. Two channels, never mixed.
REGISTERS = {
 "sketched": dict(n="01", name="Sketched", line="The idea on paper",
   defn="Outline, graphite, a construction grid behind everything. Nothing here is "
        "settled — it is being drawn, and drawing is where changes are free."),
 "stitched": dict(n="02", name="Stitched", line="Tested with thread and needle",
   defn="Topstitch and tension. The idea now exists as an object and every claim about "
        "it is measured against a tolerance rather than argued."),
 "born":     dict(n="03", name="BORN", line="It goes out into the world",
   defn="Solid, in colour, signed. Clean paper and nothing provisional left on the page."),
}
