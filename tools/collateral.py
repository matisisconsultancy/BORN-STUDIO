#!/usr/bin/env python3
"""BORN Studio physical collateral — thank-you card concepts (round 1)."""
import os
S="tools/src"; OUT="tools/_work/collateral"
os.makedirs(OUT, exist_ok=True)
rd=lambda p: open(p,encoding="utf-8").read()
FONTS=rd(f"{S}/fonts.css"); ROOT=rd(f"{S}/root.css")

BASE = ROOT + FONTS + r"""
*{margin:0;padding:0;box-sizing:border-box}
body{background:#6E6A73}
.frame{display:inline-block;padding:70px;background:#6E6A73}
.card{position:relative;overflow:hidden}
.fabric{position:absolute;inset:0;width:100%;height:100%;opacity:.42;mix-blend-mode:multiply;pointer-events:none}
"""
WEAVE = ('<svg class="fabric" width="100%" height="100%" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">'
 '<filter id="w"><feTurbulence type="turbulence" baseFrequency="0.9 0.14" numOctaves="2" seed="7" stitchTiles="stitch"/>'
 '<feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 .38 0"/></filter>'
 '<rect width="100%" height="100%" filter="url(#w)"/></svg>')

def page(title, css, inner, w, h):
    return ('<!doctype html><meta charset=utf-8><title>'+title+'</title><style>'+BASE+css+
      f'\n.card{{width:{w}px;height:{h}px}}</style><div class="frame"><div class="card">'+WEAVE+inner+'</div></div>')

def care_symbols(sz=40):
    ink="#1B1720"; red="#C4122E"; g="#8A8590"
    s=lambda inner:f'<svg viewBox="0 0 40 40" fill="none" stroke="{ink}" stroke-width="2" width="{sz}" height="{sz}">{inner}</svg>'
    return (s(f'<rect x="6" y="6" width="28" height="28" stroke="{g}" stroke-dasharray="3 3"/>')
      + s(f'<rect x="6" y="6" width="28" height="28"/><line x1="6" y1="6" x2="34" y2="34" stroke="{g}"/><line x1="34" y1="6" x2="6" y2="34" stroke="{g}"/>')
      + s('<rect x="6" y="6" width="28" height="28" fill="#1B1720"/>')
      + s(f'<circle cx="20" cy="20" r="8" fill="{red}" stroke="none"/>'))

# merrow (serged) zigzag red border
def merrow(w,h,inset=16,step=26,amp=11):
    import math
    pts=[]
    def edge(x0,y0,x1,y1,nx,ny):
        dx,dy=x1-x0,y1-y0; L=math.hypot(dx,dy); n=max(2,int(L/step))
        for i in range(n+1):
            t=i/n; o=amp if i%2 else 0
            pts.append((x0+dx*t+nx*o, y0+dy*t+ny*o))
    x=inset;y=inset;W=w-inset;H=h-inset
    edge(x,y,W,y,0,-1);edge(W,y,W,H,1,0);edge(W,H,x,H,0,1);edge(x,H,x,y,-1,0)
    d="M"+" L".join(f"{a:.1f} {b:.1f}" for a,b in pts)+" Z"
    return f'<svg viewBox="0 0 {w} {h}" width="{w}" height="{h}" style="position:absolute;inset:0"><path d="{d}" fill="none" stroke="#C4122E" stroke-width="3" stroke-linejoin="round"/></svg>'

# ------------------------------------------------------------- A) WOVEN LABEL
labelCSS = r"""
.card{background:var(--paper);box-shadow:0 40px 80px -30px rgba(0,0,0,.55);border-radius:3px}
.li{position:absolute;inset:60px 56px;display:flex;flex-direction:column;align-items:center;text-align:center}
.li .top{font-family:var(--mono);font-size:14px;letter-spacing:.3em;text-transform:uppercase;color:var(--g3)}
.li .mark{font-family:var(--word);font-size:120px;line-height:.9;color:var(--ink);margin-top:auto}
.li .mark .d{color:var(--red)}
.li .th{font-family:var(--serif6);font-weight:600;font-size:33px;color:var(--ink);margin-top:26px;line-height:1.22}
.li .care{font-family:var(--mono);font-size:14px;letter-spacing:.16em;text-transform:uppercase;color:var(--g2);line-height:2.5;margin-top:26px}
.li .syms{display:flex;gap:26px;margin-top:28px;margin-bottom:auto}
.li .note{font-family:var(--serif6);font-style:italic;font-weight:600;font-size:20px;color:var(--g2)}
.rthread{position:absolute;left:50%;top:16px;width:2.5px;height:44px;background:var(--red);transform:translateX(-50%)}
"""
labelHTML=(merrow(760,1040)+'<div class="rthread"></div><div class="li">'
  '<div class="top">Born Studio &middot; Made to be Born</div>'
  '<div class="mark">BORN<span class="d">.</span></div>'
  '<div class="th">Thank you for trusting us<br>with your idea.</div>'
  '<div class="care">Do not rush the process<br>Handle the idea with care<br>100% intention</div>'
  '<div class="syms">'+care_symbols()+'</div>'
  '<div class="note">&mdash; from the studio, with care</div></div>')
open(f"{OUT}/A_woven_label.html","w").write(page("Woven label",labelCSS,labelHTML,760,1040))

# ------------------------------------------------------------- B) MEASURING TAPE
def ticks(w,start=70,end=1610,y=46):
    out=[f'<svg viewBox="0 0 {w} 118" width="100%" height="100%" preserveAspectRatio="none">']
    step=(end-start)/60.0
    for i in range(61):
        x=start+step*i; big=(i%5==0); h=32 if big else 16
        col="#C4122E" if i==60 else "#1B1720"; sw=2.4 if big else 1.3
        out.append(f'<line x1="{x:.1f}" y1="{y}" x2="{x:.1f}" y2="{y+h}" stroke="{col}" stroke-width="{sw}"/>')
        if i%10==0:
            out.append(f'<text x="{x:.1f}" y="{y-14}" text-anchor="middle" font-family="Mono" font-size="19" fill="#4A454F">{i}</text>')
    out.append('</svg>'); return "".join(out)
tapeCSS = r"""
.card{background:#F1ECDF;box-shadow:0 40px 80px -30px rgba(0,0,0,.55);border-radius:2px}
.tt{position:absolute;left:0;right:0;top:0;height:118px}
.tb{position:absolute;left:0;right:0;bottom:0;height:118px;transform:scaleY(-1)}
.tbody{position:absolute;left:0;right:0;top:118px;bottom:118px;display:flex;align-items:center;justify-content:space-between;padding:0 84px}
.tside{font-family:var(--mono);font-size:15px;letter-spacing:.26em;text-transform:uppercase;color:var(--g2);line-height:2.1;text-align:center}
.tmid{text-align:center}
.tmid .k{font-family:var(--mono);font-size:14px;letter-spacing:.34em;text-transform:uppercase;color:var(--red)}
.tmid .m{font-family:var(--word);font-size:100px;line-height:.9;color:var(--ink);margin-top:4px}
.tmid .m .d{color:var(--red)}
.tmid .s{font-family:var(--serif6);font-weight:600;font-size:24px;color:var(--g2);margin-top:12px;line-height:1.35}
"""
tapeHTML=('<div class="tt">'+ticks(1680)+'</div><div class="tb">'+ticks(1680)+'</div>'
  '<div class="tbody"><div class="tside">Sketched<br><span style="color:#8A8590">the idea</span></div>'
  '<div class="tmid"><div class="k">From idea to life</div><div class="m">BORN<span class="d">.</span></div>'
  '<div class="s">Thank you for letting us measure<br>your idea, inch by inch.</div></div>'
  '<div class="tside">Born<br><span style="color:#C4122E">the product</span></div></div>')
open(f"{OUT}/B_measuring_tape.html","w").write(page("Measuring tape",tapeCSS,tapeHTML,1680,560))

# ------------------------------------------------------------- C) RUNNING-STITCH CARD
stitchCSS = r"""
.card{background:var(--paper);box-shadow:0 40px 80px -30px rgba(0,0,0,.55);border-radius:4px}
.rs{position:absolute;inset:34px;border:2px dashed var(--red);border-radius:2px}
.ri{position:absolute;inset:34px;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:50px}
.ri .k{font-family:var(--mono);font-size:15px;letter-spacing:.34em;text-transform:uppercase;color:var(--red)}
.ri .h{font-family:var(--serif);font-weight:900;font-size:64px;line-height:1.02;color:var(--ink);margin-top:20px;letter-spacing:-.01em}
.ri .p{font-family:var(--sans);font-size:22px;line-height:1.6;color:var(--g2);margin-top:22px;max-width:30ch}
.ri .m{font-family:var(--word);font-size:54px;color:var(--ink);margin-top:28px}
.ri .m .d{color:var(--red)}
.rfoot{position:absolute;left:0;right:0;bottom:58px;text-align:center;font-family:var(--mono);font-size:14px;letter-spacing:.24em;text-transform:uppercase;color:var(--g3)}
"""
stitchHTML=('<div class="rs"></div><div class="ri"><div class="k">Sketched &middot; Stitched &middot; Born</div>'
  '<div class="h">Thank you for making<br>it with us.</div>'
  '<div class="p">Every BORN begins as a sketch. Thank you for trusting the studio to bring yours to life.</div>'
  '<div class="m">BORN<span class="d">.</span></div></div><div class="rfoot">From idea to life</div>')
open(f"{OUT}/C_stitched_card.html","w").write(page("Stitched card",stitchCSS,stitchHTML,1400,980))
print("ok")
