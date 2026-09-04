#!/usr/bin/env python3
"""BORN Studio — measuring-tape thank-you card: contextual mockups.

Pure CSS/SVG styled scenes (no photography): a flat-lay with studio props,
the tape as a belly-band around a wrapped sample bundle, and the vertical
hangtag hung by a red cord against draped fabric.
Rendered by tools/_work/rcol.cjs (screenshots .frame).
"""
import os
S="tools/src"; OUT="tools/_work/collateral"
os.makedirs(OUT, exist_ok=True)
rd=lambda p: open(p,encoding="utf-8").read()
FONTS=rd(f"{S}/fonts.css"); ROOT=rd(f"{S}/root.css")
LINEN="#F1ECDF"; INK="#1B1720"; RED="#C4122E"; G2="#4A454F"; G3="#8A8590"

BASE = ROOT + FONTS + r"""
*{margin:0;padding:0;box-sizing:border-box}
body{background:#6E6A73}
.frame{position:relative;display:inline-block;overflow:hidden}
.fab{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}
"""
def page(title, css, inner):
  return ('<!doctype html><meta charset=utf-8><title>'+title+'</title><style>'+BASE+css+'</style>'
    '<div class="frame">'+inner+'</div>')

# ---- textures -------------------------------------------------------------
def weave(op=.4,fq="0.9 0.14",seed=7):
  return (f'<svg class="fab" style="opacity:{op};mix-blend-mode:multiply" width="100%" height="100%" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">'
   f'<filter id="wv{seed}"><feTurbulence type="turbulence" baseFrequency="{fq}" numOctaves="2" seed="{seed}" stitchTiles="stitch"/>'
   '<feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 .38 0"/></filter>'
   f'<rect width="100%" height="100%" filter="url(#wv{seed})"/></svg>')

def grain(op=.5,fq="0.65",seed=3,dark=".22"):
  return (f'<svg class="fab" style="opacity:{op};mix-blend-mode:multiply" width="100%" height="100%" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">'
   f'<filter id="gr{seed}"><feTurbulence type="fractalNoise" baseFrequency="{fq}" numOctaves="3" seed="{seed}" stitchTiles="stitch"/>'
   f'<feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 {dark} 0"/></filter>'
   f'<rect width="100%" height="100%" filter="url(#gr{seed})"/></svg>')

# ---- tape scale -----------------------------------------------------------
def scale(w, n=60, start=70, end=None, edge="top", h0=118, red_end=True, num=True):
  end = w-70 if end is None else end
  step=(end-start)/n
  y = 46 if edge=="top" else h0-46
  d = 1 if edge=="top" else -1
  out=[f'<svg viewBox="0 0 {w} {h0}" width="100%" height="{h0}" preserveAspectRatio="none">']
  for i in range(n+1):
    x=start+step*i; big=(i%5==0); L=32 if big else 16
    col=RED if (red_end and i==n) else INK; sw=2.4 if big else 1.3
    y2=y+d*L
    out.append(f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{x:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="{sw}"/>')
    if num and i%10==0:
      ny = y - d*14
      out.append(f'<text x="{x:.1f}" y="{ny:.1f}" text-anchor="middle" dominant-baseline="{ "auto" if edge=="top" else "hanging"}" font-family="Mono" font-size="19" fill="{G2}">{i}</text>')
  out.append('</svg>'); return "".join(out)

def phases(w, start=70, end=None, n=60, top=150):
  end=w-70 if end is None else end; step=(end-start)/n
  labs=[(0,"Sketched",G3),(20,"Stitched",G3),(40,"Inked",G3),(60,"Born",RED)]
  out=[]
  for pos,lab,col in labs:
    x=start+step*pos
    out.append(f'<div style="position:absolute;left:{x:.0f}px;top:{top}px;transform:translateX(-50%);font-family:var(--mono);font-size:12.5px;letter-spacing:.18em;text-transform:uppercase;color:{col};text-align:center">{lab}</div>')
  return "".join(out)

# ---- reusable card faces --------------------------------------------------
CARD_CSS=r"""
.tapecard{position:relative;background:#F1ECDF;overflow:hidden}
.tapecard .tt{position:absolute;left:0;right:0;top:0;height:118px}
.tapecard .tb{position:absolute;left:0;right:0;bottom:0;height:118px}
.tapecard .mid{position:absolute;left:0;right:0;top:0;bottom:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.tapecard .mid .k{font-family:var(--mono);font-size:14px;letter-spacing:.36em;text-transform:uppercase;color:var(--red)}
.tapecard .mid .m{font-family:var(--word);font-size:104px;line-height:.9;color:var(--ink);margin-top:6px}
.tapecard .mid .m .d{color:var(--red)}
.tapecard .mid .s{font-family:var(--serif6);font-weight:600;font-size:25px;color:var(--g2);margin-top:14px;line-height:1.35}
"""
def front_card(w=1680,h=600):
  return ('<div class="tapecard" style="width:%dpx;height:%dpx">'%(w,h)+weave()
    +'<div class="tt">'+scale(w,edge="top")+'</div>'
    +'<div class="tb">'+scale(w,edge="bottom")+'</div>'
    +phases(w)
    +'<div class="mid"><div class="k">From idea to life</div><div class="m">BORN<span class="d">.</span></div>'
     '<div class="s">Thank you for letting us measure<br>your idea, inch by inch.</div></div>'
    +'</div>')

# slim belly band
BAND_CSS=r"""
.band{position:relative;background:#F1ECDF;overflow:hidden}
.band .tt{position:absolute;left:0;right:0;top:0;height:70px}
.band .tb{position:absolute;left:0;right:0;bottom:0;height:70px}
.band .mid{position:absolute;left:0;right:0;top:0;bottom:0;display:flex;align-items:center;justify-content:center;gap:26px}
.band .mid .m{font-family:var(--word);font-size:52px;color:var(--ink);line-height:1}
.band .mid .m .d{color:var(--red)}
.band .mid .k{font-family:var(--mono);font-size:15px;letter-spacing:.32em;text-transform:uppercase;color:var(--g2)}
.band .mid .k b{color:var(--red);font-weight:400}
"""
def band(w,h=170):
  def sscale(edge):
    y=26 if edge=="top" else h-26; d=1 if edge=="top" else -1
    start=60; end=w-60; n=48; step=(end-start)/n
    o=[f'<svg viewBox="0 0 {w} {h}" width="100%" height="{h}" preserveAspectRatio="none">']
    for i in range(n+1):
      x=start+step*i; big=(i%4==0); L=16 if big else 9
      col=RED if i==n else INK; sw=2 if big else 1.1
      o.append(f'<line x1="{x:.1f}" y1="{y}" x2="{x:.1f}" y2="{y+d*L}" stroke="{col}" stroke-width="{sw}"/>')
    o.append('</svg>'); return "".join(o)
  return ('<div class="band" style="width:%dpx;height:%dpx">'%(w,h)+weave(op=.35)
    +'<div class="tt">'+sscale("top")+'</div><div class="tb">'+sscale("bottom")+'</div>'
    +'<div class="mid"><span class="k">From idea<b>&nbsp;&middot;&nbsp;</b>to life</span>'
     '<span class="m">BORN<span class="d">.</span></span>'
     '<span class="k">Made<b>&nbsp;&middot;&nbsp;</b>measured</span></div>'
    +'</div>')

# vertical hangtag (reused from explorations)
VERT_CSS=r"""
.vtag{position:relative;background:#F1ECDF;overflow:hidden;border-radius:10px}
.vtag .hole{position:absolute;left:50%;top:40px;width:34px;height:34px;border-radius:50%;border:3px solid var(--ink);transform:translateX(-50%)}
.vtag .tl{position:absolute;left:0;top:0;bottom:0;width:118px}
.vtag .mid{position:absolute;left:118px;right:0;top:0;bottom:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 24px}
.vtag .mid .m{font-family:var(--word);font-size:60px;line-height:.9;color:var(--ink);writing-mode:vertical-rl;text-orientation:mixed;letter-spacing:.04em}
.vtag .mid .m .d{color:var(--red)}
.vtag .mid .s{font-family:var(--serif6);font-weight:600;font-size:19px;color:var(--g2);margin-top:20px;writing-mode:vertical-rl}
.vtag .ph{position:absolute;right:16px;font-family:var(--mono);font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--g3);writing-mode:vertical-rl}
"""
def vtag(w=420,h=1200):
  labs=[(150,"Sketched",G3),(430,"Stitched",G3),(710,"Inked",G3),(1010,"Born",RED)]
  ph="".join(f'<div class="ph" style="top:{y}px;color:{c}">{t}</div>' for y,t,c in labs)
  vs=('<div class="tl"><div style="position:absolute;top:0;left:0;width:%dpx;height:118px;transform-origin:0 0;transform:rotate(90deg) translateY(-118px)">'%h
      +scale(h,start=70,end=h-70,edge="top")+'</div></div>')
  return ('<div class="vtag" style="width:%dpx;height:%dpx">'%(w,h)+weave()
    +'<div class="hole"></div>'+vs+ph
    +'<div class="mid"><div class="m">BORN<span class="d">.</span></div>'
     '<div class="s">From idea to life</div></div></div>')

# ---- studio props (inline SVG) --------------------------------------------
def spool(w=430):
  """side-view wooden spool wound with red thread, loose strand trailing."""
  h=int(w*0.62)
  return f'''<svg width="{w}" height="{h}" viewBox="0 0 430 266" xmlns="http://www.w3.org/2000/svg">
  <defs>
   <linearGradient id="wood" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#c9a877"/><stop offset=".5" stop-color="#b08a55"/><stop offset="1" stop-color="#8f6c3d"/></linearGradient>
   <linearGradient id="thr" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0" stop-color="#e0324a"/><stop offset=".5" stop-color="#C4122E"/><stop offset="1" stop-color="#8f0c22"/></linearGradient>
  </defs>
  <path d="M40 60 Q120 30 210 120 T400 210" fill="none" stroke="#C4122E" stroke-width="4" opacity=".85"/>
  <ellipse cx="70" cy="133" rx="30" ry="103" fill="url(#wood)"/>
  <ellipse cx="360" cy="133" rx="30" ry="103" fill="url(#wood)"/>
  <rect x="70" y="44" width="290" height="178" rx="10" fill="url(#thr)"/>
  {"".join(f'<line x1="{72+i*7}" y1="46" x2="{72+i*7}" y2="220" stroke="#a50f26" stroke-width="1" opacity=".45"/>' for i in range(41))}
  <ellipse cx="70" cy="133" rx="30" ry="103" fill="url(#wood)"/>
  <ellipse cx="70" cy="133" rx="13" ry="46" fill="#6f5231"/>
  <ellipse cx="360" cy="133" rx="30" ry="103" fill="url(#wood)" opacity=".5"/>
  </svg>'''

def swatch(w=360,col="#3C3C40"):
  """folded fabric swatch with turned corner + weave."""
  return f'''<svg width="{w}" height="{w}" viewBox="0 0 360 360" xmlns="http://www.w3.org/2000/svg">
  <defs><filter id="sw"><feTurbulence type="turbulence" baseFrequency="0.9 0.14" numOctaves="2" seed="4" stitchTiles="stitch"/>
   <feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 .5 0"/></filter></defs>
  <rect x="20" y="20" width="320" height="320" rx="6" fill="{col}"/>
  <rect x="20" y="20" width="320" height="320" rx="6" fill="{col}" filter="url(#sw)" opacity=".5" style="mix-blend-mode:screen"/>
  <path d="M240 340 L340 340 L340 240 Z" fill="#000" opacity=".22"/>
  <path d="M252 340 L340 340 L340 252 Z" fill="{col}"/>
  <path d="M252 340 L340 252" stroke="#000" stroke-width="1.5" opacity=".3"/>
  </svg>'''

def pin(angle=0,head=RED):
  return f'''<svg width="220" height="60" viewBox="0 0 220 60" style="transform:rotate({angle}deg)" xmlns="http://www.w3.org/2000/svg">
  <line x1="30" y1="30" x2="205" y2="30" stroke="#b9b6bd" stroke-width="3"/>
  <line x1="30" y1="30" x2="205" y2="30" stroke="#fff" stroke-width="1" opacity=".7"/>
  <circle cx="205" cy="30" r="6" fill="#8a8790"/>
  <circle cx="22" cy="30" r="16" fill="{head}"/>
  <circle cx="17" cy="25" r="5" fill="#fff" opacity=".5"/>
  </svg>'''

def wax():
  return '''<svg width="200" height="200" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <defs><radialGradient id="wx" cx=".4" cy=".35" r=".8">
   <stop offset="0" stop-color="#d8324a"/><stop offset=".6" stop-color="#C4122E"/><stop offset="1" stop-color="#8f0c22"/></radialGradient></defs>
  <path d="M100 14 C140 10 160 40 176 70 C192 100 190 140 160 168 C132 194 90 194 58 174 C24 152 8 116 18 78 C28 42 60 18 100 14 Z" fill="url(#wx)"/>
  <path d="M100 30 C132 28 150 50 162 74 C176 100 172 132 148 154 C124 176 90 176 64 160 C36 142 26 112 34 82 C42 52 68 32 100 30 Z" fill="none" stroke="#8f0c22" stroke-width="2" opacity=".5"/>
  <text x="100" y="132" text-anchor="middle" font-family="Didot,serif" font-size="118" fill="#8f0c22" opacity=".55">B</text>
  <text x="98" y="129" text-anchor="middle" font-family="Didot,serif" font-size="118" fill="#e6516a" opacity=".4">B</text>
  </svg>'''

def wax_sm(d=88):
  return f'''<svg width="{d}" height="{d}" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <defs><radialGradient id="wxs" cx=".4" cy=".35" r=".8">
   <stop offset="0" stop-color="#d8324a"/><stop offset=".6" stop-color="#C4122E"/><stop offset="1" stop-color="#8f0c22"/></radialGradient></defs>
  <path d="M100 14 C140 10 160 40 176 70 C192 100 190 140 160 168 C132 194 90 194 58 174 C24 152 8 116 18 78 C28 42 60 18 100 14 Z" fill="url(#wxs)"/>
  <text x="100" y="134" text-anchor="middle" font-family="Didot,serif" font-size="120" fill="#8f0c22" opacity=".55">B</text>
  <text x="98" y="131" text-anchor="middle" font-family="Didot,serif" font-size="120" fill="#e6516a" opacity=".38">B</text>
  </svg>'''

# ============================================================ 1. FLAT-LAY
flatCSS=CARD_CSS+r"""
.frame{width:2200px;height:1520px;background:radial-gradient(120% 120% at 50% 22%,#ded6c8 0%,#d2c9ba 46%,#c3b9a8 100%)}
.vig{position:absolute;inset:0;box-shadow:inset 0 0 340px 60px rgba(70,60,45,.32);pointer-events:none}
.el{position:absolute}
.dropbig{filter:drop-shadow(0 46px 44px rgba(50,40,25,.42))}
.drop{filter:drop-shadow(0 22px 22px rgba(50,40,25,.4))}
.tapecard{border-radius:4px;box-shadow:0 54px 90px -34px rgba(40,30,15,.55),0 8px 20px rgba(40,30,15,.18)}
"""
flat=('<div class="vig"></div>'+grain(op=.4,fq="0.5",dark=".16")
  +'<div class="el" style="left:340px;top:470px;transform:rotate(-3.2deg)">'+front_card()+'</div>'
  +'<div class="el dropbig" style="left:150px;top:120px;transform:rotate(-16deg)">'+spool()+'</div>'
  +'<div class="el drop" style="right:130px;top:150px;transform:rotate(9deg)">'+swatch()+'</div>'
  +'<div class="el drop" style="left:250px;top:1230px;transform:rotate(-4deg)">'+wax()+'</div>'
  +'<div class="el drop" style="right:360px;top:1210px">'+pin(-18)+'</div>'
  +'<div class="el drop" style="right:300px;top:1250px">'+pin(12,INK)+'</div>'
  +'<div class="el drop" style="right:190px;bottom:150px;transform:rotate(4deg)">'+swatch(190,"#F1ECDF")+'</div>')
open(f"{OUT}/mock_1_flatlay.html","w").write(page("flatlay",flatCSS,flat))

# ============================================================ 2. BUNDLE + BAND
bundleCSS=BAND_CSS+r"""
.frame{width:2000px;height:1500px;background:radial-gradient(130% 120% at 50% 20%,#e7e1d5 0%,#d9d2c4 50%,#cabfac 100%)}
.vig{position:absolute;inset:0;box-shadow:inset 0 0 320px 50px rgba(70,60,45,.3);pointer-events:none}
.contact{position:absolute;left:50%;top:1120px;width:1180px;height:120px;transform:translateX(-50%);
 background:radial-gradient(60% 60% at 50% 40%,rgba(40,30,15,.42),rgba(40,30,15,0) 70%);filter:blur(8px)}
.bundle{position:absolute;left:50%;top:360px;width:1120px;height:760px;transform:translateX(-50%);
 border-radius:60px/90px;background:linear-gradient(160deg,#fbf8f1 0%,#f0ebe0 46%,#e2daca 100%);
 box-shadow:inset 0 40px 70px rgba(255,255,255,.55),inset 0 -50px 80px rgba(120,105,80,.28),0 30px 60px -20px rgba(60,50,30,.4)}
.crease{position:absolute;inset:0;pointer-events:none;opacity:.5}
.band{position:absolute;left:50%;top:640px;transform:translateX(-50%);border-radius:2px;
 box-shadow:0 20px 34px -12px rgba(40,30,15,.5),0 3px 8px rgba(40,30,15,.25)}
.band::before,.band::after{content:"";position:absolute;top:0;bottom:0;width:70px;pointer-events:none}
.band::before{left:0;background:linear-gradient(90deg,rgba(90,75,50,.34),rgba(90,75,50,0))}
.band::after{right:0;background:linear-gradient(270deg,rgba(90,75,50,.34),rgba(90,75,50,0))}
.twine{position:absolute;left:520px;top:360px;width:11px;height:760px;
 background:linear-gradient(90deg,#7d0a1e,#e0324a 45%,#C4122E 55%,#7d0a1e);border-radius:6px;
 box-shadow:0 4px 9px rgba(40,30,15,.3)}
.tail{position:absolute;top:724px;width:8px;height:150px;border-radius:5px;
 background:linear-gradient(90deg,#7d0a1e,#C4122E 55%,#7d0a1e);box-shadow:0 4px 8px rgba(40,30,15,.28)}
.tailL{left:504px;transform:rotate(9deg);transform-origin:top}
.tailR{left:540px;transform:rotate(-9deg);transform-origin:top}
.seal{position:absolute;left:525px;top:724px;transform:translate(-50%,-50%);
 filter:drop-shadow(0 8px 14px rgba(40,30,15,.4))}
"""
crease=('<svg class="crease" viewBox="0 0 1120 760" preserveAspectRatio="none">'
  '<path d="M120 90 Q400 40 700 120 T1000 110" fill="none" stroke="#b7a888" stroke-width="2" opacity=".5"/>'
  '<path d="M90 300 Q380 260 720 340" fill="none" stroke="#b7a888" stroke-width="2" opacity=".4"/>'
  '<path d="M140 600 Q460 660 940 590" fill="none" stroke="#b7a888" stroke-width="2" opacity=".4"/>'
  '<path d="M300 120 Q340 400 260 640" fill="none" stroke="#c8b89a" stroke-width="1.6" opacity=".45"/>'
  '<path d="M840 120 Q890 380 820 650" fill="none" stroke="#c8b89a" stroke-width="1.6" opacity=".45"/>'
  '</svg>')
bundle=('<div class="vig"></div>'+grain(op=.34,fq="0.5",dark=".14")
  +'<div class="contact"></div>'
  +'<div class="bundle">'+weave(op=.16,seed=9)+crease+'</div>'
  +'<div class="tail tailL"></div><div class="tail tailR"></div>'
  +'<div class="twine"></div>'
  +band(1240,168)
  +'<div class="seal">'+wax_sm()+'</div>')
open(f"{OUT}/mock_2_bundle.html","w").write(page("bundle",bundleCSS,bundle))

# ============================================================ 3. HANGTAG
hangCSS=VERT_CSS+r"""
.frame{width:1600px;height:1640px;background:linear-gradient(135deg,#4a444d 0%,#3c3740 50%,#2c2830 100%)}
.drape{position:absolute;inset:0;opacity:.5;pointer-events:none}
.vig{position:absolute;inset:0;box-shadow:inset 0 0 360px 70px rgba(0,0,0,.5);pointer-events:none}
.cord{position:absolute;left:50%;top:-40px;width:11px;height:430px;transform-origin:top center;
 background:linear-gradient(90deg,#8f0c22,#e0324a 45%,#C4122E 55%,#8f0c22);border-radius:6px}
.cordL{transform:translateX(-50%) rotate(6deg)}
.cordR{transform:translateX(-50%) rotate(-6deg)}
.vtag{position:absolute;left:50%;top:360px;transform:translateX(-50%) rotate(2.4deg);
 box-shadow:0 60px 90px -30px rgba(0,0,0,.7),0 12px 30px rgba(0,0,0,.4)}
.pinch{position:absolute;left:50%;top:344px;width:64px;height:40px;transform:translateX(-50%) rotate(2.4deg);
 background:radial-gradient(circle at 50% 30%,#e0324a,#C4122E 60%,#8f0c22);border-radius:0 0 30px 30px;z-index:3}
"""
# a soft drape of vertical folds
drape=('<svg class="drape" viewBox="0 0 1600 1640" preserveAspectRatio="none">'
  + "".join(f'<rect x="{i*90}" y="0" width="46" height="1640" fill="#000" opacity="{0.05+0.05*(i%3)}"/>' for i in range(18))
  + "".join(f'<rect x="{i*90+46}" y="0" width="44" height="1640" fill="#fff" opacity="0.03"/>' for i in range(18))
  +'</svg>')
hang=('<div class="drape">'+drape+'</div>'+weave(op=.2,fq="0.7 0.12",seed=5)+'<div class="vig"></div>'
  +'<div class="cord cordL"></div><div class="cord cordR"></div>'
  +'<div class="pinch"></div>'
  +vtag()
  +'</div>')
open(f"{OUT}/mock_3_hangtag.html","w").write(page("hangtag",hangCSS,hang))

print("mockups written")
