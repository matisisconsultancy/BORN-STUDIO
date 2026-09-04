#!/usr/bin/env python3
"""BORN Studio — measuring-tape thank-you card: explorations + mockups."""
import os
S="tools/src"; OUT="tools/_work/collateral"
os.makedirs(OUT, exist_ok=True)
rd=lambda p: open(p,encoding="utf-8").read()
FONTS=rd(f"{S}/fonts.css"); ROOT=rd(f"{S}/root.css")
LINEN="#F1ECDF"; INK="#1B1720"; RED="#C4122E"; G2="#4A454F"; G3="#8A8590"

BASE = ROOT + FONTS + r"""
*{margin:0;padding:0;box-sizing:border-box}
body{background:#6E6A73}
.frame{display:inline-block;padding:70px;background:#6E6A73}
.card{position:relative;overflow:hidden}
.fab{position:absolute;inset:0;width:100%;height:100%;opacity:.4;mix-blend-mode:multiply;pointer-events:none}
"""
def weave(op=.4,fq="0.9 0.14"):
  return (f'<svg class="fab" style="opacity:{op}" width="100%" height="100%" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">'
   f'<filter id="wv"><feTurbulence type="turbulence" baseFrequency="{fq}" numOctaves="2" seed="7" stitchTiles="stitch"/>'
   '<feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 .38 0"/></filter>'
   '<rect width="100%" height="100%" filter="url(#wv)"/></svg>')

def page(title, css, inner):
  return ('<!doctype html><meta charset=utf-8><title>'+title+'</title><style>'+BASE+css+'</style>'
    '<div class="frame">'+inner+'</div>')

def scale(w, n=60, start=70, end=None, edge="top", h0=118, red_end=True):
  """ticks + upright mono numbers along one edge"""
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
    if i%10==0:
      ny = y - d*14
      out.append(f'<text x="{x:.1f}" y="{ny:.1f}" text-anchor="middle" dominant-baseline="{ "auto" if edge=="top" else "hanging"}" font-family="Mono" font-size="19" fill="{G2}">{i}</text>')
  out.append('</svg>'); return "".join(out)

# phase markers row (Sketched/Stitched/Inked/Born under the top scale)
def phases(w, start=70, end=None, n=60):
  end=w-70 if end is None else end; step=(end-start)/n
  labs=[(0,"Sketched",G3),(20,"Stitched",G3),(40,"Inked",G3),(60,"Born",RED)]
  out=[]
  for pos,lab,col in labs:
    x=start+step*pos
    out.append(f'<div style="position:absolute;left:{x:.0f}px;top:150px;transform:translateX(-50%);font-family:var(--mono);font-size:12.5px;letter-spacing:.18em;text-transform:uppercase;color:{col};text-align:center">{lab}</div>')
  return "".join(out)

# ============================================================ FRONT (refined)
frontCSS=r"""
.card{width:1680px;height:600px;background:#F1ECDF;box-shadow:0 40px 80px -30px rgba(0,0,0,.55);border-radius:3px}
.tt{position:absolute;left:0;right:0;top:0;height:118px}
.tb{position:absolute;left:0;right:0;bottom:0;height:118px}
.mid{position:absolute;left:0;right:0;top:0;bottom:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.mid .k{font-family:var(--mono);font-size:14px;letter-spacing:.36em;text-transform:uppercase;color:var(--red)}
.mid .m{font-family:var(--word);font-size:104px;line-height:.9;color:var(--ink);margin-top:6px}
.mid .m .d{color:var(--red)}
.mid .s{font-family:var(--serif6);font-weight:600;font-size:25px;color:var(--g2);margin-top:14px;line-height:1.35}
"""
front=('<div class="card">'+weave()
  +'<div class="tt">'+scale(1680,edge="top")+'</div>'
  +'<div class="tb">'+scale(1680,edge="bottom")+'</div>'
  +phases(1680)
  +'<div class="mid"><div class="k">From idea to life</div><div class="m">BORN<span class="d">.</span></div>'
   '<div class="s">Thank you for letting us measure<br>your idea, inch by inch.</div></div>'
  +'</div>')
open(f"{OUT}/tape_1_front.html","w").write(page("front",frontCSS,front))

# ============================================================ BACK (note)
backCSS=r"""
.card{width:1680px;height:600px;background:#F1ECDF;box-shadow:0 40px 80px -30px rgba(0,0,0,.55);border-radius:3px}
.te{position:absolute;left:0;right:0;top:0;height:118px}
.bk{position:absolute;left:120px;right:120px;top:150px;bottom:70px;display:flex;flex-direction:column}
.bk .hi{font-family:var(--serif6);font-weight:600;font-style:italic;font-size:30px;color:var(--ink)}
.bk .lines{margin-top:26px;flex:1}
.bk .lines div{border-bottom:1.4px solid rgba(27,23,32,.16);height:52px}
.bk .sign{display:flex;justify-content:space-between;align-items:flex-end;margin-top:14px}
.bk .sign .l{font-family:var(--mono);font-size:12.5px;letter-spacing:.2em;text-transform:uppercase;color:var(--g3)}
.bk .sign .r{font-family:var(--word);font-size:40px;color:var(--ink)}
.bk .sign .r .d{color:var(--red)}
"""
back=('<div class="card">'+weave()
  +'<div class="te">'+scale(1680,edge="top")+'</div>'
  +'<div class="bk"><div class="hi">Dear&nbsp;'+('&nbsp;'*14)+',</div>'
   '<div class="lines"><div></div><div></div><div></div></div>'
   '<div class="sign"><div class="l">Made &amp; measured with care<br>Born Studio &middot; @born.studio</div>'
   '<div class="r">BORN<span class="d">.</span></div></div></div>'
  +'</div>')
open(f"{OUT}/tape_2_back.html","w").write(page("back",backCSS,back))

# ============================================================ DIE-CUT (metal end)
diecutCSS=r"""
.wrap{position:relative;width:1720px;height:520px}
.tab{position:absolute;left:0;top:120px;width:150px;height:280px;background:linear-gradient(90deg,#C9C4C0,#E7E3DE);border-radius:14px 6px 6px 14px;box-shadow:0 30px 60px -28px rgba(0,0,0,.55)}
.tab .hole{position:absolute;left:44px;top:50%;width:34px;height:34px;border-radius:50%;background:#6E6A73;transform:translateY(-50%);box-shadow:inset 0 2px 4px rgba(0,0,0,.5)}
.tab .rivet{position:absolute;right:26px;top:26px;width:12px;height:12px;border-radius:50%;background:#9a9490}
.tab .rivet2{position:absolute;right:26px;bottom:26px;width:12px;height:12px;border-radius:50%;background:#9a9490}
.card{position:absolute;left:120px;top:0;width:1600px;height:520px;background:#F1ECDF;border-radius:0 60px 60px 0;box-shadow:0 40px 80px -30px rgba(0,0,0,.5);overflow:hidden}
.tt{position:absolute;left:0;right:0;top:0;height:118px}
.tb{position:absolute;left:0;right:0;bottom:0;height:118px}
.mid{position:absolute;left:120px;right:60px;top:0;bottom:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center}
.mid .k{font-family:var(--mono);font-size:13px;letter-spacing:.34em;text-transform:uppercase;color:var(--red)}
.mid .m{font-family:var(--word);font-size:92px;line-height:.9;color:var(--ink);margin-top:4px}
.mid .m .d{color:var(--red)}
.mid .s{font-family:var(--serif6);font-weight:600;font-size:22px;color:var(--g2);margin-top:12px;line-height:1.35}
"""
diecut=('<div class="wrap"><div class="tab"><div class="hole"></div><div class="rivet"></div><div class="rivet2"></div></div>'
  '<div class="card">'+weave()
  +'<div class="tt">'+scale(1600,start=110,edge="top")+'</div>'
  +'<div class="tb">'+scale(1600,start=110,edge="bottom")+'</div>'
  +'<div class="mid"><div class="k">From idea to life</div><div class="m">BORN<span class="d">.</span></div>'
   '<div class="s">Measured every inch<br>of the way. Thank you.</div></div>'
  '</div></div>')
open(f"{OUT}/tape_3_diecut.html","w").write(page("diecut",diecutCSS,diecut))

# ============================================================ VERTICAL (hangtag)
vertCSS=r"""
.card{width:420px;height:1200px;background:#F1ECDF;box-shadow:0 40px 80px -30px rgba(0,0,0,.55);border-radius:8px}
.hole{position:absolute;left:50%;top:40px;width:34px;height:34px;border-radius:50%;border:3px solid var(--ink);transform:translateX(-50%)}
.tl{position:absolute;left:0;top:0;bottom:0;width:118px}
.mid{position:absolute;left:118px;right:0;top:0;bottom:0;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:0 24px}
.mid .k{font-family:var(--mono);font-size:12px;letter-spacing:.3em;text-transform:uppercase;color:var(--red);writing-mode:vertical-rl;position:absolute;left:8px;top:50%;transform:translateY(-50%)}
.mid .m{font-family:var(--word);font-size:60px;line-height:.9;color:var(--ink);writing-mode:vertical-rl;text-orientation:mixed;letter-spacing:.04em}
.mid .m .d{color:var(--red)}
.mid .s{font-family:var(--serif6);font-weight:600;font-size:19px;color:var(--g2);margin-top:20px;writing-mode:vertical-rl}
.ph{position:absolute;right:16px;font-family:var(--mono);font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--g3);writing-mode:vertical-rl}
"""
def vphases():
  labs=[(150,"Sketched",G3),(430,"Stitched",G3),(710,"Inked",G3),(1010,"Born",RED)]
  return "".join(f'<div class="ph" style="top:{y}px;color:{c}">{t}</div>' for y,t,c in labs)
vert=('<div class="card">'+weave()
  +'<div class="hole"></div>'
  +'<div class="tl">'+scale(1200,start=90,edge="top",h0=118)+'</div>'  # placeholder; vertical scale below
  +vphases()
  +'<div class="mid"><div class="m">BORN<span class="d">.</span></div>'
   '<div class="s">From idea to life</div></div>'
  +'</div>')
# vertical scale: rotate a horizontal scale
vert=vert.replace('<div class="tl">'+scale(1200,start=90,edge="top",h0=118)+'</div>',
  '<div class="tl" style="left:0;top:0;bottom:0;width:118px"><div style="position:absolute;top:0;left:0;width:1200px;height:118px;transform-origin:0 0;transform:rotate(90deg) translateY(-118px)">'+scale(1200,start=70,end=1130,edge="top")+'</div></div>')
open(f"{OUT}/tape_4_vertical.html","w").write(page("vertical",vertCSS,vert))
print("explorations written")
