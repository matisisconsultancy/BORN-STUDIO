#!/usr/bin/env python3
"""BORN Studio — sample-shipment kit (coordinated system).

Pure CSS/SVG styled scenes rendered by tools/_work/rcol.cjs (screenshots .frame):
  kit_1_unboxing  — open kraft box lined with patterned tissue, holding the
                    tape-card + sample bundle + studio props (the hero).
  kit_2_box       — closed shipping box (top-down) with branded gummed tape +
                    ship-to label.
  kit_3_tissue    — tissue-paper pattern sheet with the wax seal.
  kit_4_seals     — sticker / seal system: wax B, printed ring, negative, dot.
"""
import os
S="tools/src"; OUT="tools/_work/collateral"
os.makedirs(OUT, exist_ok=True)
rd=lambda p: open(p,encoding="utf-8").read()
FONTS=rd(f"{S}/fonts.css"); ROOT=rd(f"{S}/root.css")
LINEN="#F1ECDF"; INK="#1B1720"; RED="#C4122E"; G2="#4A454F"; G3="#8A8590"
KRAFT="#b9966a"; KRAFT2="#a9855a"; KRAFTD="#8f6c42"

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

def card_grain(op=.5,fq="0.6",seed=3,dark=".2"):
  return (f'<svg class="fab" style="opacity:{op};mix-blend-mode:multiply" width="100%" height="100%" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">'
   f'<filter id="gr{seed}"><feTurbulence type="fractalNoise" baseFrequency="{fq}" numOctaves="3" seed="{seed}" stitchTiles="stitch"/>'
   f'<feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 {dark} 0"/></filter>'
   f'<rect width="100%" height="100%" filter="url(#gr{seed})"/></svg>')

def cardboard(seed=11,op=.5):
  return (f'<svg class="fab" style="opacity:{op};mix-blend-mode:multiply" width="100%" height="100%" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">'
   f'<filter id="cb{seed}"><feTurbulence type="fractalNoise" baseFrequency="0.012 0.9" numOctaves="2" seed="{seed}"/>'
   '<feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 .5 0"/></filter>'
   f'<rect width="100%" height="100%" filter="url(#cb{seed})"/></svg>')

# ---- tape scale -----------------------------------------------------------
def hscale(w,h,edge="top",start=None,end=None,n=48,red_end=True,num=False):
  start=60 if start is None else start; end=(w-60) if end is None else end
  step=(end-start)/n; y=26 if edge=="top" else h-26; d=1 if edge=="top" else -1
  o=[f'<svg viewBox="0 0 {w} {h}" width="100%" height="{h}" preserveAspectRatio="none">']
  for i in range(n+1):
    x=start+step*i; big=(i%4==0); L=17 if big else 9
    col=RED if (red_end and i==n) else INK; sw=2 if big else 1.1
    o.append(f'<line x1="{x:.1f}" y1="{y}" x2="{x:.1f}" y2="{y+d*L}" stroke="{col}" stroke-width="{sw}"/>')
    if num and big and i%8==0:
      o.append(f'<text x="{x:.1f}" y="{y-d*12}" text-anchor="middle" font-family="Mono" font-size="15" fill="{G2}" dominant-baseline="{"auto" if edge=="top" else "hanging"}">{i}</text>')
  o.append('</svg>'); return "".join(o)

# ---- reusable belly band --------------------------------------------------
BAND_CSS=r"""
.band{position:relative;background:#F1ECDF;overflow:hidden}
.band .tt{position:absolute;left:0;right:0;top:0;height:70px}
.band .tb{position:absolute;left:0;right:0;bottom:0;height:70px}
.band .mid{position:absolute;left:0;right:0;top:0;bottom:0;display:flex;align-items:center;justify-content:center;gap:24px}
.band .mid .m{font-family:var(--word);font-size:46px;color:var(--ink);line-height:1}
.band .mid .m .d{color:var(--red)}
.band .mid .k{font-family:var(--mono);font-size:13px;letter-spacing:.3em;text-transform:uppercase;color:var(--g2)}
.band .mid .k b{color:var(--red);font-weight:400}
"""
def band(w,h=150):
  return ('<div class="band" style="width:%dpx;height:%dpx">'%(w,h)+weave(op=.35)
    +'<div class="tt">'+hscale(w,70,"top")+'</div><div class="tb">'+hscale(w,70,"bottom")+'</div>'
    +'<div class="mid"><span class="k">From idea<b>&nbsp;&middot;&nbsp;</b>to life</span>'
     '<span class="m">BORN<span class="d">.</span></span>'
     '<span class="k">Made<b>&nbsp;&middot;&nbsp;</b>measured</span></div></div>')

# ---- front tape card (for insert / hero) ----------------------------------
CARD_CSS=r"""
.tapecard{position:relative;background:#F1ECDF;overflow:hidden}
.tapecard .tt,.tapecard .tb{position:absolute;left:0;right:0;height:100px}
.tapecard .tt{top:0}.tapecard .tb{bottom:0}
.tapecard .mid{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.tapecard .mid .k{font-family:var(--mono);font-size:12px;letter-spacing:.34em;text-transform:uppercase;color:var(--red)}
.tapecard .mid .m{font-family:var(--word);font-size:88px;line-height:.9;color:var(--ink);margin-top:5px}
.tapecard .mid .m .d{color:var(--red)}
.tapecard .mid .s{font-family:var(--serif6);font-weight:600;font-size:21px;color:var(--g2);margin-top:12px;line-height:1.35}
"""
def front_card(w=1420,h=500):
  return ('<div class="tapecard" style="width:%dpx;height:%dpx">'%(w,h)+weave()
    +'<div class="tt">'+hscale(w,100,"top",n=52)+'</div><div class="tb">'+hscale(w,100,"bottom",n=52)+'</div>'
    +'<div class="mid"><div class="k">From idea to life</div><div class="m">BORN<span class="d">.</span></div>'
     '<div class="s">Thank you for letting us measure<br>your idea, inch by inch.</div></div></div>')

# ---- seals ----------------------------------------------------------------
def wax(d=120,letter=True):
  return f'''<svg width="{d}" height="{d}" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <defs><radialGradient id="wx{d}" cx=".4" cy=".35" r=".85">
   <stop offset="0" stop-color="#d8324a"/><stop offset=".6" stop-color="#C4122E"/><stop offset="1" stop-color="#8f0c22"/></radialGradient></defs>
  <path d="M100 12 C142 8 162 40 178 70 C194 100 192 142 160 170 C132 196 88 196 56 176 C22 154 6 116 16 76 C26 40 58 16 100 12 Z" fill="url(#wx{d})"/>
  {'<text x="100" y="134" text-anchor="middle" font-family="Didot,serif" font-size="120" fill="#8f0c22" opacity=".5">B</text><text x="98" y="131" text-anchor="middle" font-family="Didot,serif" font-size="120" fill="#e6516a" opacity=".38">B</text>' if letter else ''}
  </svg>'''

def sticker(kind="ink", d=300):
  """circular printed sticker: BORN. inside a ruler ring + slogan arc."""
  bg = {"ink":"#F1ECDF","red":RED,"neg":INK}[kind]
  fg = {"ink":INK,"red":"#F1ECDF","neg":"#F1ECDF"}[kind]
  ac = {"ink":RED,"red":"#F1ECDF","neg":RED}[kind]
  R=150; ticks=[]
  import math
  for i in range(60):
    a=math.radians(i*6-90); big=(i%5==0); r1=R-6; r2=R-(20 if big else 12)
    x1=100+r1*math.cos(a); y1=100+r1*math.sin(a); x2=100+r2*math.cos(a); y2=100+r2*math.sin(a)
    col=ac if i==0 else fg
    ticks.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{col}" stroke-width="{2 if big else 1}" opacity=".8"/>')
  return f'''<svg width="{d}" height="{d}" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg">
  <circle cx="100" cy="100" r="98" fill="{bg}"/>
  <circle cx="100" cy="100" r="150" fill="none"/>
  <g transform="scale(0.5) translate(100 100)">{''.join(ticks)}</g>
  <circle cx="100" cy="100" r="70" fill="none" stroke="{fg}" stroke-width="1" opacity=".35"/>
  <text x="100" y="96" text-anchor="middle" font-family="Didot,serif" font-size="46" fill="{fg}">BORN<tspan fill="{ac}">.</tspan></text>
  <text x="100" y="120" text-anchor="middle" font-family="Mono,monospace" font-size="9.5" letter-spacing="2.4" fill="{fg}" opacity=".8">EST · STUDIO</text>
  </svg>'''

def spool(w=380):
  h=int(w*0.62)
  return f'''<svg width="{w}" height="{h}" viewBox="0 0 430 266" xmlns="http://www.w3.org/2000/svg">
  <defs><linearGradient id="wood2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#c9a877"/><stop offset=".5" stop-color="#b08a55"/><stop offset="1" stop-color="#8f6c3d"/></linearGradient>
  <linearGradient id="thr2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e0324a"/><stop offset=".5" stop-color="#C4122E"/><stop offset="1" stop-color="#8f0c22"/></linearGradient></defs>
  <path d="M40 60 Q120 30 210 120 T400 210" fill="none" stroke="#C4122E" stroke-width="4" opacity=".85"/>
  <ellipse cx="70" cy="133" rx="30" ry="103" fill="url(#wood2)"/><ellipse cx="360" cy="133" rx="30" ry="103" fill="url(#wood2)"/>
  <rect x="70" y="44" width="290" height="178" rx="10" fill="url(#thr2)"/>
  {"".join(f'<line x1="{72+i*7}" y1="46" x2="{72+i*7}" y2="220" stroke="#a50f26" stroke-width="1" opacity=".45"/>' for i in range(41))}
  <ellipse cx="70" cy="133" rx="30" ry="103" fill="url(#wood2)"/><ellipse cx="70" cy="133" rx="13" ry="46" fill="#6f5231"/>
  <ellipse cx="360" cy="133" rx="30" ry="103" fill="url(#wood2)" opacity=".5"/></svg>'''

# ---- tissue pattern -------------------------------------------------------
def tissue_pattern(op_ink=".10", op_red=".24", angle=-18, id="tp"):
  """tileable BORN + ruler + slogan pattern, faint, for tissue / box lining."""
  ticks="".join(f'<line x1="{20+i*22}" y1="250" x2="{20+i*22}" y2="{250-(15 if i%4==0 else 8)}" stroke="{INK}" stroke-width="1" opacity="{op_ink}"/>' for i in range(24))
  tile=(f'<pattern id="{id}" width="560" height="300" patternUnits="userSpaceOnUse" patternTransform="rotate({angle})">'
    f'<text x="30" y="150" font-family="Didot,serif" font-size="76" fill="{INK}" opacity="{op_ink}">BORN<tspan fill="{RED}" opacity="{op_red}">.</tspan></text>'
    f'<text x="320" y="150" font-family="Didot,serif" font-size="76" fill="{INK}" opacity="{op_ink}">BORN<tspan fill="{RED}" opacity="{op_red}">.</tspan></text>'
    f'<text x="30" y="60" font-family="Mono,monospace" font-size="15" letter-spacing="4" fill="{INK}" opacity="{op_ink}">FROM IDEA TO LIFE</text>'
    f'<text x="330" y="290" font-family="Mono,monospace" font-size="15" letter-spacing="4" fill="{INK}" opacity="{op_ink}">SKETCHED · STITCHED</text>'
    f'{ticks}</pattern>')
  return tile

def tissue_layer(op_ink=".10",op_red=".24",angle=-18,seed=None):
  seed = angle
  return (f'<svg class="fab" width="100%" height="100%" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">'
    f'<defs>{tissue_pattern(op_ink,op_red,angle,id="tp"+str(abs(seed)))}</defs>'
    f'<rect width="100%" height="100%" fill="url(#tp{abs(seed)})"/></svg>')

# ============================================================ 1. UNBOXING
Wi,Hi=1200,900; fd=230
FX,FY=1100,820   # interior center
unboxCSS=CARD_CSS+r"""
.frame{width:2200px;height:1640px;background:radial-gradient(120% 120% at 50% 20%,#ded6c8 0%,#d2c9ba 48%,#c1b7a6 100%)}
.vig{position:absolute;inset:0;box-shadow:inset 0 0 340px 70px rgba(70,60,45,.34);pointer-events:none}
.flap{position:absolute;overflow:hidden}
.flap .cut{position:absolute;background:linear-gradient(#e8dcc4,#cdbb98);opacity:.9}
.interior{position:absolute;left:INTLpx;top:INTTpx;width:INTWpx;height:INTHpx;transform:translate(-50%,-50%);
 background:linear-gradient(150deg,#9c7c4e,#8a6a3e);border-radius:10px;overflow:hidden;
 box-shadow:inset 0 0 90px 30px rgba(60,42,20,.6),0 40px 70px -20px rgba(40,28,10,.5)}
.tissue{position:absolute;inset:14px;border-radius:6px;background:linear-gradient(150deg,#fbf8f1,#efe9dd);overflow:hidden;
 box-shadow:inset 0 30px 60px rgba(255,255,255,.5),inset 0 -40px 70px rgba(150,130,95,.3)}
.crease{position:absolute;inset:0;pointer-events:none;opacity:.5}
.el{position:absolute}
.drop{filter:drop-shadow(0 20px 22px rgba(50,38,20,.4))}
.tapecard{border-radius:4px;box-shadow:0 40px 70px -26px rgba(40,30,15,.55),0 6px 16px rgba(40,30,15,.2)}
.bundle{position:absolute;border-radius:44px/64px;background:linear-gradient(160deg,#fbf8f1,#e7dfcf);
 box-shadow:inset 0 30px 50px rgba(255,255,255,.5),inset 0 -36px 60px rgba(140,120,88,.3),0 26px 46px -16px rgba(40,30,15,.45)}
.bband{position:absolute;background:#F1ECDF;overflow:hidden;box-shadow:0 12px 22px -8px rgba(40,30,15,.4)}
.bthr{position:absolute;background:linear-gradient(90deg,#7d0a1e,#C4122E 55%,#7d0a1e);border-radius:5px}
""".replace("INTL",str(FX)).replace("INTT",str(FY)).replace("INTW",str(Wi)).replace("INTH",str(Hi))
def flap(x,y,w,h,fold):
  """kraft flap; fold = which inner edge has the fold shadow: t/b/l/r"""
  sh={'t':'inset 0 34px 40px -18px rgba(50,34,14,.55)','b':'inset 0 -34px 40px -18px rgba(50,34,14,.55)',
      'l':'inset 34px 0 40px -18px rgba(50,34,14,.55)','r':'inset -34px 0 40px -18px rgba(50,34,14,.55)'}[fold]
  cut={'t':'left:0;right:0;bottom:0;height:8px','b':'left:0;right:0;top:0;height:8px',
       'l':'top:0;bottom:0;right:0;width:8px','r':'top:0;bottom:0;left:0;width:8px'}[fold]
  return (f'<div class="flap" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;'
    f'background:linear-gradient(135deg,#c39a68,#b0885a);box-shadow:{sh},0 20px 40px -20px rgba(40,28,10,.4)">'
    +cardboard(op=.35)+f'<div class="cut" style="{cut}"></div></div>')

iL=FX-Wi//2; iT=FY-Hi//2; iR=FX+Wi//2; iB=FY+Hi//2
crease=('<svg class="crease" viewBox="0 0 1200 900" preserveAspectRatio="none">'
  '<path d="M120 120 Q400 80 760 150 T1080 130" fill="none" stroke="#c7b790" stroke-width="2" opacity=".5"/>'
  '<path d="M100 420 Q420 380 800 460" fill="none" stroke="#c7b790" stroke-width="2" opacity=".4"/>'
  '<path d="M160 760 Q520 820 1040 720" fill="none" stroke="#c7b790" stroke-width="2" opacity=".4"/>'
  '<path d="M320 120 Q360 460 300 780" fill="none" stroke="#d3c4a0" stroke-width="1.6" opacity=".45"/>'
  '<path d="M900 120 Q950 470 880 770" fill="none" stroke="#d3c4a0" stroke-width="1.6" opacity=".45"/></svg>')
# nested bundle inside the box (upper area), tape card resting lower, props
bundleW,bundleH=760,470; bx=FX-150; by=FY-150
bundle=(f'<div class="bundle" style="left:{bx-bundleW//2}px;top:{by-bundleH//2}px;width:{bundleW}px;height:{bundleH}px">'
  +weave(op=.14,seed=9)+'</div>'
  +f'<div class="bband" style="left:{bx-bundleW//2}px;top:{by-40}px;width:{bundleW}px;height:150px">'
   +weave(op=.3)+'<div style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;gap:18px">'
   '<span style="font-family:var(--mono);font-size:11px;letter-spacing:.28em;text-transform:uppercase;color:'+G2+'">From idea</span>'
   '<span style="font-family:var(--word);font-size:40px;color:'+INK+'">BORN<span style="color:'+RED+'">.</span></span>'
   '<span style="font-family:var(--mono);font-size:11px;letter-spacing:.28em;text-transform:uppercase;color:'+G2+'">to life</span></div>'
   +hscale(bundleW,150//2,"top",n=30)+'</div>'
  +f'<div class="bthr" style="left:{bx-256}px;top:{by-150//2-40}px;width:9px;height:230px"></div>'
  +f'<div class="el drop" style="left:{bx-291}px;top:{by-6}px">'+wax(78)+'</div>')

unbox=('<div class="vig"></div>'+card_grain(op=.4,fq="0.5",dark=".14")
  # flaps (behind interior visually but drawn first)
  +flap(iL, iT-fd, Wi, fd, 'b')      # top flap (above)
  +flap(iL, iB, Wi, fd, 't')          # bottom flap (below)
  +flap(iL-fd, iT, fd, Hi, 'r')       # left flap
  +flap(iR, iT, fd, Hi, 'l')          # right flap
  +'<div class="interior"><div class="tissue">'+tissue_layer(op_ink=".11",op_red=".26",angle=-16)+weave(op=.12,seed=4)+crease+'</div></div>'
  +bundle
  # tape card resting across the lower third, angled, half on tissue half on flap
  +'<div class="el" style="left:%dpx;top:%dpx;transform:rotate(-4deg)">'%(FX-710, FY+250)+front_card()+'</div>'
  # props on the surface
  +'<div class="el drop" style="left:120px;top:150px;transform:rotate(-14deg)">'+spool()+'</div>'
  +'<div class="el drop" style="right:150px;bottom:170px;transform:rotate(6deg)">'+wax(150)+'</div>')
open(f"{OUT}/kit_1_unboxing.html","w").write(page("unboxing",unboxCSS,unbox))

# ============================================================ 2. SHIPPING BOX
boxCSS=r"""
.frame{width:2000px;height:1500px;background:radial-gradient(130% 120% at 50% 22%,#e0d8ca 0%,#d2c9ba 52%,#c0b6a4 100%)}
.vig{position:absolute;inset:0;box-shadow:inset 0 0 320px 60px rgba(70,60,45,.32);pointer-events:none}
.box{position:absolute;left:50%;top:50%;width:1240px;height:940px;transform:translate(-50%,-50%);
 background:linear-gradient(150deg,#c49a67,#b0885a 55%,#9d7748);border-radius:12px;overflow:hidden;
 box-shadow:0 60px 100px -34px rgba(40,28,10,.55),inset 0 2px 0 rgba(255,240,215,.4)}
.seam{position:absolute;left:50%;top:0;bottom:0;width:2px;transform:translateX(-50%);background:rgba(60,42,20,.35)}
.gtape{position:absolute;left:50%;top:-20px;width:270px;height:980px;transform:translateX(-50%) rotate(0deg);
 background:linear-gradient(90deg,#efe7d6,#f6f1e6 50%,#e9e1cf);overflow:hidden;
 box-shadow:0 14px 26px -10px rgba(40,28,10,.45);opacity:.97}
.gtape .rep{position:absolute;inset:0;display:flex;align-items:center;justify-content:center}
.gtape .rep .v{writing-mode:vertical-rl;text-orientation:mixed;font-family:var(--mono);font-size:15px;
 letter-spacing:.36em;text-transform:uppercase;color:#8a8590;white-space:nowrap;line-height:1}
.gtape .rep .v b{color:var(--red);font-weight:400}
.gtape .tedge{position:absolute;top:0;bottom:0;width:2px;background:repeating-linear-gradient(#1B1720 0 12px,transparent 12px 26px);opacity:.5}
.gtape .tl{left:20px}.gtape .tr{right:20px}
.label{position:absolute;left:135px;top:250px;width:560px;height:440px;background:#F2EEE6;transform:rotate(-1.4deg);
 box-shadow:0 24px 44px -16px rgba(40,28,10,.5);overflow:hidden;padding:34px 40px}
.label .hd{display:flex;justify-content:space-between;align-items:flex-start}
.label .hd .m{font-family:var(--word);font-size:44px;color:var(--ink);line-height:1}
.label .hd .m .d{color:var(--red)}
.label .hd .k{font-family:var(--mono);font-size:11px;letter-spacing:.24em;text-transform:uppercase;color:var(--g3);text-align:right;margin-top:6px}
.label .ru{height:1.4px;background:rgba(27,23,32,.18);margin:8px 0}
.label .sec{font-family:var(--mono);font-size:12px;letter-spacing:.24em;text-transform:uppercase;color:var(--red);margin-top:22px}
.label .ln{border-bottom:1.4px solid rgba(27,23,32,.16);height:34px;margin-top:14px}
.label .ft{position:absolute;left:40px;right:40px;bottom:26px;display:flex;justify-content:space-between;align-items:flex-end;
 font-family:var(--mono);font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--g3)}
.stamp{position:absolute;right:150px;bottom:230px}
.embw{position:absolute;right:150px;top:250px;font-family:var(--word);font-size:70px;color:rgba(60,42,20,.55);
 text-shadow:0 1px 0 rgba(255,240,215,.4)}
.embw .d{color:rgba(150,20,44,.6)}
"""
def gtape_reps(n=3):
  phrase='Born<b>&nbsp;·&nbsp;</b>from idea to life<b>&nbsp;·&nbsp;</b>made<b>&nbsp;·&nbsp;</b>measured<b>&nbsp;·&nbsp;</b>'
  return '<div class="rep"><div class="v">'+ (phrase*n) +'</div></div>'
box=('<div class="vig"></div>'+card_grain(op=.36,fq="0.5",dark=".13")
  +'<div class="box">'+cardboard(op=.4)+'<div class="seam"></div>'
   +'<div class="embw">BORN<span class="d">.</span></div>'
   +'<div class="label">'
     '<div class="hd"><div class="m">BORN<span class="d">.</span></div>'
     '<div class="k">Sample<br>enclosed</div></div>'
     '<div class="ru"></div>'
     '<div class="sec">Ship to</div><div class="ln"></div><div class="ln"></div><div class="ln"></div>'
     '<div class="ft"><div>From · Born Studio<br>@born.studio</div><div>Handle<br>with care</div></div>'
   '</div>'
   +'<div class="gtape">'+weave(op=.28)
     +'<div class="tedge tl"></div><div class="tedge tr"></div>'
     +gtape_reps()
   +'</div>'
   +'<div class="stamp">'+wax(150)+'</div>'
  +'</div>')
open(f"{OUT}/kit_2_box.html","w").write(page("box",boxCSS,box))

# ============================================================ 3. TISSUE SHEET
tisCSS=r"""
.frame{width:2000px;height:1400px;background:radial-gradient(130% 120% at 50% 20%,#d9d1c3 0%,#cbc2b3 55%,#b9af9d 100%)}
.vig{position:absolute;inset:0;box-shadow:inset 0 0 300px 60px rgba(70,60,45,.34);pointer-events:none}
.sheet{position:absolute;left:50%;top:50%;width:1560px;height:1060px;transform:translate(-50%,-50%) rotate(-1deg);
 background:linear-gradient(150deg,#fdfaf3,#f1ebdf 60%,#e6dfcf);border-radius:4px;overflow:hidden;
 box-shadow:0 50px 90px -34px rgba(40,30,15,.5)}
.folds{position:absolute;inset:0;pointer-events:none}
.seal{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%) rotate(-6deg);filter:drop-shadow(0 20px 26px rgba(40,30,15,.4))}
.corner{position:absolute;width:180px;height:180px;background:linear-gradient(135deg,rgba(0,0,0,.12),rgba(0,0,0,0));pointer-events:none}
.cap{position:absolute;left:60px;top:54px;font-family:var(--mono);font-size:13px;letter-spacing:.3em;text-transform:uppercase;color:var(--g3)}
"""
folds=('<svg class="folds" viewBox="0 0 1560 1060" preserveAspectRatio="none">'
  +''.join(f'<line x1="{i*195}" y1="0" x2="{i*195}" y2="1060" stroke="#000" stroke-width="1" opacity="0.05"/>' for i in range(1,8))
  +''.join(f'<line x1="0" y1="{i*212}" x2="1560" y2="{i*212}" stroke="#000" stroke-width="1" opacity="0.05"/>' for i in range(1,5))
  +'</svg>')
tis=('<div class="vig"></div>'
  +'<div class="sheet">'+tissue_layer(op_ink=".13",op_red=".3",angle=-16)+weave(op=.14,seed=6)+folds
   +'<div class="corner" style="left:0;top:0"></div><div class="corner" style="right:0;bottom:0;transform:rotate(180deg)"></div>'
   +'<div class="seal">'+wax(210)+'</div>'
  +'</div>')
open(f"{OUT}/kit_3_tissue.html","w").write(page("tissue",tisCSS,tis))

# ============================================================ 4. SEAL SYSTEM
sealCSS=r"""
.frame{width:2000px;height:1000px;background:linear-gradient(160deg,#efe9dd,#e2dbcd 60%,#d3cabb)}
.vig{position:absolute;inset:0;box-shadow:inset 0 0 240px 50px rgba(70,60,45,.24);pointer-events:none}
.hd{position:absolute;left:120px;top:90px}
.hd .t{font-family:var(--word);font-size:56px;color:var(--ink)}.hd .t .d{color:var(--red)}
.hd .k{font-family:var(--mono);font-size:14px;letter-spacing:.3em;text-transform:uppercase;color:var(--g3);margin-top:8px}
.row{position:absolute;left:0;right:0;top:440px;display:flex;justify-content:center;gap:120px}
.cell{text-align:center}
.disc{filter:drop-shadow(0 22px 28px rgba(40,30,15,.32));border-radius:50%}
.cap{margin-top:34px;font-family:var(--mono);font-size:14px;letter-spacing:.24em;text-transform:uppercase;color:var(--g2)}
.dotcard{width:300px;height:300px;border-radius:50%;background:#F1ECDF;position:relative;overflow:hidden;
 filter:drop-shadow(0 22px 28px rgba(40,30,15,.32))}
.dotcard .dd{position:absolute;left:50%;top:50%;width:70px;height:70px;border-radius:50%;background:var(--red);transform:translate(-50%,-50%)}
.dotcard .rr{position:absolute;left:50%;top:50%;width:210px;height:210px;border:1px solid rgba(27,23,32,.3);border-radius:50%;transform:translate(-50%,-50%)}
"""
seal=('<div class="vig"></div>'
  +'<div class="hd"><div class="t">The seal<span class="d">.</span></div>'
   '<div class="k">One mark · four ways to close a story</div></div>'
  +'<div class="row">'
   +'<div class="cell"><div class="disc">'+sticker("ink",300)+'</div><div class="cap">Printed · ivory</div></div>'
   +'<div class="cell"><div class="disc">'+sticker("red",300)+'</div><div class="cap">Printed · red</div></div>'
   +'<div class="cell"><div class="disc">'+sticker("neg",300)+'</div><div class="cap">Negative</div></div>'
   +'<div class="cell"><div>'+wax(300)+'</div><div class="cap">Wax · B</div></div>'
  +'</div>')
open(f"{OUT}/kit_4_seals.html","w").write(page("seals",sealCSS,seal))

print("kit written")
