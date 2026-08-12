#!/usr/bin/env python3
"""Extract the approved logo/icon/animation SVGs (plus <style> and hatch defs)
from the committed logos.html into tools/_work/. Source of truth = logos.html."""
import re, os, json
SRC="logos.html"; WORK="tools/_work"
os.makedirs(WORK, exist_ok=True)
txt=open(SRC, encoding="utf-8").read()
lines=txt.split("\n")

# 1) style block (fonts + all CSS incl. animation keyframes & :root vars)
style=re.search(r"<style>(.*?)</style>", txt, re.S).group(1)
open(f"{WORK}/style.css","w",encoding="utf-8").write(style)

# 2) hatch/filter defs (the hidden <svg class="hatch-defs">...)
defs=re.search(r'(<svg[^>]*class="hatch-defs".*?</svg>)', txt, re.S).group(1)
open(f"{WORK}/defs.svg","w",encoding="utf-8").write(defs)

def svg_before(line, endpos):
    """last <svg ...>...</svg> whose </svg> ends at/just before endpos"""
    e=line.rfind("</svg>", 0, endpos)
    assert e!=-1, "no </svg>"
    e+=6
    s=line.rfind("<svg", 0, e)
    return line[s:e]

def cards_on_line(idx):
    l=lines[idx-1]
    out={}
    for m in re.finditer(r'<h3 class="opt__name">(.*?)</h3>', l):
        name=m.group(1)
        out[name]=svg_before(l, m.start())
    return out

# map: friendly key -> (line, name-substring-in-file)
TARGETS={
  # wordmark lockups (line 175)
  "wm_principal"      : (175, "negro + slogan"),
  "wm_sin_slogan"     : (175, "negro + punto"),
  "wm_ecorojo_slogan" : (175, "eco rojo + slogan"),
  "wm_ecorojo"        : (175, "&middot; eco rojo</h3"),   # plain eco rojo (no slogan)
  # base clean doble (line 181) - compact/emblem
  "wm_base"           : (181, "Doble exposici&oacute;n</h3"),
  # icons (line 163)
  "ic_negativo"       : (163, "Icono &middot; negativo"),
  "ic_construccion"   : (163, "construcci&oacute;n"),
  "ic_doble"          : (163, "Icono &middot; doble exposici"),
  # animations (line 169)
  "an_ensamblaje"     : (169, "Ensamblaje"),
  "an_barrida"        : (169, "Barrida"),
}

# build per-line name->svg once
linecache={}
manifest={}
for key,(ln,needle) in TARGETS.items():
    if ln not in linecache: linecache[ln]=cards_on_line(ln)
    cards=linecache[ln]
    # find the card whose full name (with entities) contains needle (entity-aware)
    match=None
    for name,svg in cards.items():
        hay=(name+"</h3")
        if needle in name or needle in hay:
            match=(name,svg); break
    if not match:
        # try raw-line fallback: locate needle directly then svg_before
        l=lines[ln-1]; p=l.find(needle.replace("</h3",""))
        assert p!=-1, f"NOT FOUND: {key} needle={needle!r}"
        match=(needle, svg_before(l, p))
    name,svg=match
    open(f"{WORK}/{key}.svg","w",encoding="utf-8").write(svg)
    manifest[key]={"name":name,"line":ln,"len":len(svg)}

json.dump(manifest, open(f"{WORK}/manifest.json","w"), indent=1, ensure_ascii=False)
print("style:",len(style),"defs:",len(defs))
for k,v in manifest.items():
    print(f"  {k:20s} <- {v['name'][:42]:42s} ({v['len']} chars)")
