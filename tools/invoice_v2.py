#!/usr/bin/env python3
"""BORN Studio — invoice system, three professional directions.

  invoice_2_spec       "The Spec"      — tech-pack title-block / measurement sheet
  invoice_3_editorial  "Editorial"     — Didone masthead, the total as the hero
  invoice_4_tape       "The Tape"      — the bill measured out along a tailor's tape

Each is a distinct point of view on the same identity, not a recolor.
A4 portrait (1240x1754). USD, commercial (no tax).
"""
import os
S="tools/src"; OUT="tools/_work/collateral"
os.makedirs(OUT, exist_ok=True)
rd=lambda p: open(p,encoding="utf-8").read()
FONTS=rd(f"{S}/fonts.css"); ROOT=rd(f"{S}/root.css")
INK="#1B1720"; RED="#C4122E"; G2="#4A454F"; G3="#8A8590"; G4="#B7B2BA"; LINEN="#EFEADD"

# shared line items (desc, sub, phase, phasecolor, qty, rate, amount, cum-unit-on-a-60-scale)
ITEMS=[
 ("Discovery &amp; tech pack","Capsule SS26 &middot; 24 styles","Sketched",G3,"1","2,400","2,400",8),
 ("Factory sourcing &amp; pairing","Shortlist, MOQ &amp; costing","Sketched",G3,"1","600","600",15),
 ("Sample development","Proto &rarr; SMS &middot; 3 fitting rounds","Stitched",G2,"3","850","2,550",25),
 ("Size set &amp; signed PPS","Pre-production approval","Born",RED,"1","1,000","1,000",35),
 ("Production oversight","Bulk &middot; inline &amp; final QC","Born",RED,"1","1,800","1,800",45),
]
SUBTOTAL="8,350"; DEPOSIT="4,175"; BALANCE="4,175"
NUM="BORN&ndash;0042"

def hticks(w,h=30,n=48,red_end=True,col=INK):
  step=w/n; o=[f'<svg viewBox="0 0 {w} {h}" width="100%" height="{h}" preserveAspectRatio="none">']
  for i in range(n+1):
    x=step*i; big=(i%4==0); L=h*0.6 if big else h*0.32
    c=RED if (red_end and i==n) else col; sw=1.8 if big else 1
    o.append(f'<line x1="{x:.1f}" y1="0" x2="{x:.1f}" y2="{L:.1f}" stroke="{c}" stroke-width="{sw}"/>')
  o.append('</svg>'); return "".join(o)

def vscale(H, W=120, n=60, top=60, bot=60, num=True, weave_bg=False, mark_unit=None):
  """vertical gauge: ticks on the right edge pointing left, numbers upright."""
  span=H-top-bot; step=span/n
  o=[f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}">']
  if weave_bg:
    o.append(f'<defs><filter id="lw"><feTurbulence type="turbulence" baseFrequency="0.12 0.9" numOctaves="2" seed="7" stitchTiles="stitch"/>'
      '<feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 .28 0"/></filter></defs>'
      f'<rect width="{W}" height="{H}" fill="{LINEN}"/><rect width="{W}" height="{H}" filter="url(#lw)" opacity=".5"/>')
  edge=W-2
  for i in range(n+1):
    y=top+step*i; big=(i%5==0); L=26 if big else 13
    c=RED if i==n else INK; sw=2 if big else 1.1
    o.append(f'<line x1="{edge}" y1="{y:.1f}" x2="{edge-L}" y2="{y:.1f}" stroke="{c}" stroke-width="{sw}"/>')
    if num and i%10==0:
      o.append(f'<text x="{edge-L-9}" y="{y+5:.1f}" text-anchor="end" font-family="Mono,monospace" font-size="15" fill="{G2}">{i}</text>')
  o.append('</svg>'); return "".join(o), (lambda u: top+step*u)

BASE = ROOT + FONTS + "*{margin:0;padding:0;box-sizing:border-box}"
def page(css, inner, bodybg="#cfc7b8"):
  return (f'<!doctype html><meta charset=utf-8><style>{BASE} body{{background:{bodybg}}}{css}</style>'
    f'<div class="frame">{inner}</div>')

# ============================================================ A · THE SPEC
def build_spec():
  gauge,_=vscale(1754, W=118, n=60, top=70, bot=70, weave_bg=False)
  cells=[("Invoice №",NUM),("Issued","04 Sep 2026"),("Due","04 Oct 2026"),
         ("Terms","Net 30"),("Currency","USD"),("Sheet","1 / 1")]
  metacells="".join(f'<div class="mc"><span class="mk">{k}</span><span class="mv">{v}</span></div>' for k,v in cells)
  rows=[]
  for i,(d,sub,ph,pc,qty,rate,amt,_u) in enumerate(ITEMS,1):
    rows.append(f'''<tr>
      <td class="n">{i:02d}</td>
      <td class="d"><b>{d}</b><span>{sub}</span></td>
      <td class="ph"><i style="background:{pc}"></i>{ph}</td>
      <td class="q">{qty}</td><td class="r">${rate}</td><td class="a">${amt}</td></tr>''')
  css=r"""
.frame{position:relative;width:1240px;height:1754px;background:#F1EFE8;overflow:hidden;font-family:var(--sans);color:var(--ink)}
.rail{position:absolute;left:0;top:0;bottom:0;width:118px;border-right:1.4px solid var(--ink)}
.rail .lbl{position:absolute;left:20px;top:50%;writing-mode:vertical-rl;transform:translateY(-50%) rotate(180deg);
 font-family:var(--mono);font-size:11px;letter-spacing:.4em;text-transform:uppercase;color:var(--g3)}
.body{position:absolute;left:118px;right:0;top:0;bottom:0;padding:60px 80px 56px 60px;display:flex;flex-direction:column}
.sys{display:flex;justify-content:space-between;font-family:var(--mono);font-size:11px;letter-spacing:.18em;
 text-transform:uppercase;color:var(--g3);padding-bottom:14px;border-bottom:1.4px solid var(--ink)}
.sys b{color:var(--ink);font-weight:400}
.tb{display:flex;justify-content:space-between;align-items:flex-start;margin-top:34px}
.tb .wm{font-family:var(--word);font-size:58px;line-height:.85;color:var(--ink)}
.tb .wm .d{color:var(--red)}
.tb .wm .tag{display:block;font-family:var(--mono);font-size:10px;letter-spacing:.26em;text-transform:uppercase;color:var(--g3);margin-top:12px}
.meta{display:grid;grid-template-columns:repeat(3,1fr);border:1.4px solid var(--ink);border-bottom:0;border-right:0;width:430px}
.mc{border-right:1.4px solid var(--ink);border-bottom:1.4px solid var(--ink);padding:10px 12px 12px}
.mk{display:block;font-family:var(--mono);font-size:8.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--g3)}
.mv{display:block;font-family:var(--mono);font-size:14px;color:var(--ink);margin-top:5px}
.parties{display:flex;margin-top:26px;border:1.4px solid var(--ink)}
.pcell{flex:1;padding:14px 16px 16px}
.pcell+.pcell{border-left:1.4px solid var(--ink)}
.pk{font-family:var(--mono);font-size:9px;letter-spacing:.2em;text-transform:uppercase;color:var(--red)}
.pn{font-family:var(--serif6);font-weight:600;font-size:18px;margin-top:8px}
.pl{font-size:13px;color:var(--g2);line-height:1.65;margin-top:4px}
table{width:100%;border-collapse:collapse;margin-top:30px}
thead th{font-family:var(--mono);font-size:9.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--g3);
 text-align:left;padding:0 8px 10px;border-bottom:1.4px solid var(--ink)}
thead th.q,thead th.r,thead th.a{text-align:right}
tbody td{padding:15px 8px;border-bottom:1px solid var(--line);vertical-align:top}
td.n{font-family:var(--mono);font-size:12px;color:var(--g4);width:44px}
td.d b{font-family:var(--serif6);font-weight:600;font-size:16px;display:block}
td.d span{font-size:12px;color:var(--g3);display:block;margin-top:3px}
td.ph{font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--g2);width:130px;white-space:nowrap}
td.ph i{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:8px;vertical-align:middle}
td.q,td.r,td.a{text-align:right;font-family:var(--mono);font-size:13.5px}
td.q{width:60px;color:var(--g2)}td.r{width:110px;color:var(--g2)}td.a{width:120px;color:var(--ink)}
.foot-row{display:flex;justify-content:space-between;gap:40px;margin-top:34px;align-items:flex-start}
.pay .pk{margin-bottom:10px}
.pay .pl{font-family:var(--mono);font-size:12px;color:var(--g2);line-height:1.9}
.pay .pl b{color:var(--ink);font-weight:400}
.tot{width:400px;border:1.4px solid var(--ink)}
.tot .tr{display:flex;justify-content:space-between;padding:11px 16px;font-family:var(--mono);font-size:13px;color:var(--g2);border-bottom:1px solid var(--line)}
.tot .tr .v{color:var(--ink)}
.tot .due{display:flex;justify-content:space-between;align-items:center;padding:14px 16px;background:var(--red)}
.tot .due .l{font-family:var(--mono);font-size:10.5px;letter-spacing:.16em;text-transform:uppercase;color:rgba(255,255,255,.85)}
.tot .due .v{font-family:var(--word);font-size:40px;color:#fff;line-height:.9}
.callout{margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end;padding-top:22px;border-top:1.4px solid var(--ink)}
.callout .ty{font-family:var(--serif6);font-weight:600;font-style:italic;font-size:16px;color:var(--ink)}
.callout .sig{font-family:var(--mono);font-size:10px;letter-spacing:.16em;text-transform:uppercase;color:var(--g3);text-align:right;line-height:1.8}
"""
  inner=(f'<div class="rail">{gauge}<div class="lbl">Measured &middot; from idea to life</div></div>'
    '<div class="body">'
    f'<div class="sys"><span>Born Studio &mdash; <b>Apparel Development</b></span><span>Invoice &middot; <b>{NUM}</b></span></div>'
    '<div class="tb"><div class="wm">BORN<span class="d">.</span><span class="tag">Billing sheet</span></div>'
    f'<div class="meta">{metacells}</div></div>'
    '<div class="parties">'
    '<div class="pcell"><div class="pk">From</div><div class="pn">Born Studio</div>'
    '<div class="pl">hello@born.studio<br>Ciudad de México, MX</div></div>'
    '<div class="pcell"><div class="pk">Billed to</div><div class="pn">Atelier Marisol</div>'
    '<div class="pl">Marisol Rivera &middot; accounts@ateliermarisol.com<br>Av. Reforma 210, CDMX</div></div></div>'
    '<table><thead><tr><th class="n">#</th><th class="d">Description</th><th class="ph">Phase</th>'
    '<th class="q">Qty</th><th class="r">Rate</th><th class="a">Amount</th></tr></thead>'
    f'<tbody>{"".join(rows)}</tbody></table>'
    '<div class="foot-row"><div class="pay"><div class="pk">Payment</div>'
    '<div class="pl"><b>Net 30</b> &middot; wire / ACH<br>BBVA &middot; Born Studio S.A.<br>CLABE 012 180 0000 0000 0000<br>Ref. invoice № on transfer</div></div>'
    '<div class="tot">'
    f'<div class="tr"><span>Subtotal</span><span class="v">${SUBTOTAL}</span></div>'
    f'<div class="tr"><span>Deposit received &middot; 50%</span><span class="v">&minus;${DEPOSIT}</span></div>'
    f'<div class="due"><span class="l">Balance due &middot; USD</span><span class="v">${BALANCE}</span></div></div></div>'
    '<div class="callout"><div class="ty">Measured every inch of the way. Thank you.</div>'
    '<div class="sig">Sketched &middot; Stitched &middot; Born<br>Sheet 1 / 1</div></div>'
    '</div>')
  open(f"{OUT}/invoice_2_spec.html","w").write(page(css,inner))

# ============================================================ B · EDITORIAL
def build_editorial():
  rows=[]
  for d,sub,ph,pc,qty,rate,amt,_u in ITEMS:
    rows.append(f'''<div class="li">
      <div class="li-d"><span class="dd">{d}</span><span class="ds">{sub}</span></div>
      <div class="li-p"><i style="background:{pc}"></i>{ph}</div>
      <div class="li-a">${amt}</div></div>''')
  css=r"""
.frame{position:relative;width:1240px;height:1754px;background:#F4F1E9;overflow:hidden;font-family:var(--sans);color:var(--ink);
 padding:120px 130px 96px}
.mast{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:1.4px solid var(--ink);padding-bottom:26px}
.mast .wm{font-family:var(--word);font-size:104px;line-height:.8;color:var(--ink)}
.mast .wm .d{color:var(--red)}
.mast .rt{text-align:right;font-family:var(--mono);font-size:12px;letter-spacing:.24em;text-transform:uppercase;color:var(--g3);line-height:2}
.mast .rt b{color:var(--ink);font-weight:400;font-size:15px;letter-spacing:.12em}
.kick{margin-top:22px;font-family:var(--mono);font-size:11.5px;letter-spacing:.26em;text-transform:uppercase;color:var(--g2)}
.kick b{color:var(--red);font-weight:400}
.parties{display:flex;gap:80px;margin-top:70px}
.party{flex:1}
.party .k{font-family:var(--mono);font-size:10px;letter-spacing:.24em;text-transform:uppercase;color:var(--g3)}
.party .n{font-family:var(--serif);font-size:23px;margin-top:10px}
.party .l{font-size:14px;color:var(--g2);line-height:1.7;margin-top:8px}
.items{margin-top:74px}
.ihd{display:flex;justify-content:space-between;font-family:var(--mono);font-size:10px;letter-spacing:.2em;
 text-transform:uppercase;color:var(--g4);padding-bottom:12px}
.li{display:flex;align-items:baseline;gap:24px;padding:22px 0;border-top:1px solid var(--line)}
.li-d{flex:1}
.li-d .dd{font-family:var(--serif);font-size:22px;color:var(--ink);display:block}
.li-d .ds{font-size:13px;color:var(--g3);margin-top:4px;display:block}
.li-p{width:150px;font-family:var(--mono);font-size:10.5px;letter-spacing:.12em;text-transform:uppercase;color:var(--g2)}
.li-p i{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:8px;vertical-align:middle}
.li-a{width:150px;text-align:right;font-family:var(--serif);font-size:22px;color:var(--ink)}
.hero{display:flex;justify-content:space-between;align-items:flex-end;margin-top:84px}
.hero .meta{font-family:var(--mono);font-size:12px;color:var(--g2);line-height:2.1}
.hero .meta .row{display:flex;gap:16px}.hero .meta .row span:first-child{color:var(--g3);min-width:180px;text-transform:uppercase;letter-spacing:.14em;font-size:10.5px}
.hero .meta .row span:last-child{color:var(--ink)}
.hero .big{text-align:right}
.hero .big .l{font-family:var(--mono);font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--g3)}
.hero .big .n{font-family:var(--word);font-size:112px;line-height:.82;color:var(--red);margin-top:8px}
.sign{position:absolute;left:130px;right:130px;bottom:70px;display:flex;justify-content:space-between;align-items:baseline;
 border-top:1.4px solid var(--ink);padding-top:22px}
.sign .ty{font-family:var(--serif);font-style:italic;font-size:19px;color:var(--ink)}
.sign .st{font-family:var(--mono);font-size:10px;letter-spacing:.2em;text-transform:uppercase;color:var(--g3)}
.sign .st .d{color:var(--red)}
"""
  inner=('<div class="mast"><div class="wm">BORN<span class="d">.</span></div>'
    '<div class="rt"><b>Invoice</b><br>Full-Service Apparel Development</div></div>'
    f'<div class="kick">{NUM}<b> / </b>Issued 04.09.26<b> / </b>Due 04.10.26<b> / </b>USD</div>'
    '<div class="parties"><div class="party"><div class="k">From</div><div class="n">Born Studio</div>'
    '<div class="l">hello@born.studio &middot; @born.studio<br>Ciudad de México, MX</div></div>'
    '<div class="party"><div class="k">Billed to</div><div class="n">Atelier Marisol</div>'
    '<div class="l">Marisol Rivera, Founder<br>accounts@ateliermarisol.com &middot; CDMX</div></div></div>'
    '<div class="items"><div class="ihd"><span>Service</span><span>Phase / Amount</span></div>'
    f'{"".join(rows)}</div>'
    '<div class="hero"><div class="meta">'
    f'<div class="row"><span>Subtotal</span><span>${SUBTOTAL}</span></div>'
    f'<div class="row"><span>Deposit received 50%</span><span>&minus;${DEPOSIT}</span></div>'
    '<div class="row"><span>Payment</span><span>Net 30 &middot; wire / ACH</span></div>'
    '</div><div class="big"><div class="l">Balance due, USD</div>'
    f'<div class="n">${BALANCE}</div></div></div>'
    '<div class="sign"><div class="ty">Thank you for letting us measure your idea, inch by inch.</div>'
    '<div class="st">From idea to life<span class="d">.</span></div></div>')
  open(f"{OUT}/invoice_3_editorial.html","w").write(page(css,inner))

# ============================================================ C · THE TAPE
def build_tape():
  gauge,ypos=vscale(1754, W=300, n=60, top=250, bot=150, weave_bg=True)
  # place each item next to its cumulative tape mark
  leaders=[]; rowsHTML=[]
  for d,sub,ph,pc,qty,rate,amt,u in ITEMS:
    y=ypos(u)
    leaders.append(f'<div class="leader" style="top:{y:.0f}px"></div>')
    rowsHTML.append(f'''<div class="li" style="top:{y-28:.0f}px">
      <div class="li-d"><b>{d}</b><span>{sub} &middot; <i style="color:{pc}">{ph}</i></span></div>
      <div class="li-a">${amt}</div></div>''')
  yBal=ypos(60); ySub=yBal-118
  css=r"""
.frame{position:relative;width:1240px;height:1754px;background:#F4F1E9;overflow:hidden;font-family:var(--sans);color:var(--ink)}
.tape{position:absolute;left:0;top:0;bottom:0;width:300px;box-shadow:8px 0 40px -20px rgba(40,30,15,.4)}
.tapelbl{position:absolute;left:56px;top:250px;writing-mode:vertical-rl;transform:rotate(180deg);
 font-family:var(--mono);font-size:11px;letter-spacing:.34em;text-transform:uppercase;color:var(--g3)}
.hd{position:absolute;left:360px;right:90px;top:120px;display:flex;justify-content:space-between;align-items:flex-start}
.hd .wm{font-family:var(--word);font-size:66px;line-height:.85;color:var(--ink)}
.hd .wm .d{color:var(--red)}
.hd .wm .tag{display:block;font-family:var(--mono);font-size:10px;letter-spacing:.24em;text-transform:uppercase;color:var(--g3);margin-top:12px}
.hd .rt{text-align:right;font-family:var(--mono);font-size:12px;color:var(--g2);line-height:1.95}
.hd .rt .k{color:var(--g3);text-transform:uppercase;letter-spacing:.14em;font-size:10px;margin-right:10px}
.hd .rt b{color:var(--ink);font-weight:400}
.stage{position:absolute;left:360px;right:90px;top:0;bottom:0}
.leader{position:absolute;left:-60px;width:44px;height:0;border-top:1.4px dotted var(--g4)}
.leader::before{content:"";position:absolute;left:-6px;top:-4px;width:8px;height:8px;border-radius:50%;background:var(--red)}
.li{position:absolute;left:0;right:0;display:flex;justify-content:space-between;align-items:baseline;gap:24px}
.li-d b{font-family:var(--serif6);font-weight:600;font-size:19px;color:var(--ink)}
.li-d span{display:block;font-family:var(--mono);font-size:11px;letter-spacing:.04em;color:var(--g3);margin-top:5px;text-transform:uppercase}
.li-d span i{font-style:normal}
.li-a{font-family:var(--mono);font-size:17px;color:var(--ink);white-space:nowrap}
.sums{position:absolute;left:360px;right:90px}
.subrow{display:flex;justify-content:flex-end;gap:40px;font-family:var(--mono);font-size:13px;color:var(--g2)}
.subrow+.subrow{margin-top:8px}.subrow .v{color:var(--ink);min-width:110px;text-align:right}
.balrow{position:absolute;left:360px;right:90px;display:flex;justify-content:space-between;align-items:center}
.balrow .l{font-family:var(--mono);font-size:11px;letter-spacing:.18em;text-transform:uppercase;color:var(--ink)}
.balrow .amt{font-family:var(--word);font-size:64px;line-height:.85;color:var(--red)}
.balrow .connect{position:absolute;left:-60px;width:44px;top:50%;border-top:2px solid var(--red)}
.balrow .connect::before{content:"";position:absolute;left:-7px;top:-5px;width:10px;height:10px;border-radius:50%;background:var(--red)}
.foot{position:absolute;left:360px;right:90px;bottom:70px;border-top:1px solid var(--line);padding-top:20px;
 display:flex;justify-content:space-between;align-items:baseline}
.foot .ty{font-family:var(--serif6);font-weight:600;font-style:italic;font-size:16px;color:var(--ink);max-width:440px}
.foot .st{font-family:var(--mono);font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:var(--g3);text-align:right;line-height:1.8}
"""
  inner=(f'<div class="tape">{gauge}</div><div class="tapelbl">Measured, inch by inch</div>'
    '<div class="hd"><div class="wm">BORN<span class="d">.</span><span class="tag">Invoice</span></div>'
    f'<div class="rt"><div><span class="k">Invoice №</span><b>{NUM}</b></div>'
    '<div><span class="k">Issued</span>04 Sep 2026</div>'
    '<div><span class="k">Due</span>04 Oct 2026</div>'
    '<div><span class="k">Billed to</span><b>Atelier Marisol</b></div></div></div>'
    f'<div class="stage">{"".join(leaders)}{"".join(rowsHTML)}</div>'
    f'<div class="sums" style="top:{ySub:.0f}px">'
    f'<div class="subrow"><span>Subtotal</span><span class="v">${SUBTOTAL}</span></div>'
    f'<div class="subrow"><span>Deposit received &middot; 50%</span><span class="v">&minus;${DEPOSIT}</span></div></div>'
    f'<div class="balrow" style="top:{yBal-32:.0f}px"><div class="connect"></div>'
    f'<div class="l">Balance<br>due &middot; USD</div><div class="amt">${BALANCE}</div></div>'
    '<div class="foot"><div class="ty">Thank you for letting us measure your idea, inch by inch.</div>'
    '<div class="st">Born Studio<br>From idea to life</div></div>')
  open(f"{OUT}/invoice_4_tape.html","w").write(page(css,inner))

build_spec(); build_editorial(); build_tape()
print("invoice v2 written")
