#!/usr/bin/env python3
"""BORN Studio — commercial invoice (branded, A4, USD, no tax)."""
import os
S="tools/src"; OUT="tools/_work/collateral"
os.makedirs(OUT, exist_ok=True)
rd=lambda p: open(p,encoding="utf-8").read()
FONTS=rd(f"{S}/fonts.css"); ROOT=rd(f"{S}/root.css")
INK="#1B1720"; RED="#C4122E"; G2="#4A454F"; G3="#8A8590"; G4="#B7B2BA"

def ticks(w,h=34,n=48,red_end=True):
  start=0; end=w; step=(end-start)/n; y=0
  o=[f'<svg viewBox="0 0 {w} {h}" width="100%" height="{h}" preserveAspectRatio="none">']
  for i in range(n+1):
    x=start+step*i; big=(i%4==0); L=h*0.62 if big else h*0.34
    col=RED if (red_end and i==n) else INK; sw=2 if big else 1.1
    o.append(f'<line x1="{x:.1f}" y1="0" x2="{x:.1f}" y2="{L:.1f}" stroke="{col}" stroke-width="{sw}"/>')
  o.append('</svg>'); return "".join(o)

# line items --------------------------------------------------------------
# (description, subline, phase, phasecolor, qty, rate, amount)
ITEMS=[
 ("Discovery &amp; production-ready tech pack","Capsule SS26 &middot; 24 styles","Sketched",G3,"1","2,400","2,400"),
 ("Factory sourcing &amp; pairing","Shortlist, MOQ &amp; costing","Sketched",G3,"1","600","600"),
 ("Sample development &amp; documented fitting","Proto &rarr; SMS, 3 rounds","Stitched",G2,"3","850","2,550"),
 ("Size set &amp; signed PPS","Pre-production approval","Born",RED,"1","1,000","1,000"),
 ("Production oversight","Bulk, inline &amp; final QC","Born",RED,"1","1,800","1,800"),
]
SUBTOTAL="8,350"; DEPOSIT="4,175"; BALANCE="4,175"

def rows():
  out=[]
  for desc,sub,ph,pc,qty,rate,amt in ITEMS:
    out.append(f'''<tr>
      <td class="c-desc"><div class="d">{desc}</div><div class="sub">{sub}</div></td>
      <td class="c-ph"><span class="phase"><i style="background:{pc}"></i>{ph}</span></td>
      <td class="c-qty">{qty}</td>
      <td class="c-rate">${rate}</td>
      <td class="c-amt">${amt}</td></tr>''')
  return "".join(out)

CSS = ROOT + FONTS + r"""
*{margin:0;padding:0;box-sizing:border-box}
body{background:#cfc7b8}
.frame{position:relative;width:1240px;height:1754px;background:#F4F1E9;overflow:hidden;
 font-family:var(--sans);color:var(--ink)}
.pad{position:absolute;left:96px;right:96px;top:64px;bottom:70px;display:flex;flex-direction:column}
.topticks{position:absolute;left:0;right:0;top:0;height:34px;opacity:.9}
/* header */
.hd{display:flex;justify-content:space-between;align-items:flex-start;margin-top:26px}
.hd .wm{font-family:var(--word);font-size:70px;line-height:.86;color:var(--ink)}
.hd .wm .d{color:var(--red)}
.hd .tag{font-family:var(--mono);font-size:11px;letter-spacing:.28em;text-transform:uppercase;color:var(--g3);margin-top:12px}
.hd .rt{text-align:right}
.hd .rt .lab{font-family:var(--word);font-size:40px;letter-spacing:.02em;color:var(--ink)}
.hd .rt .meta{margin-top:16px;font-family:var(--mono);font-size:12.5px;color:var(--g2);line-height:1.9}
.hd .rt .meta b{color:var(--ink);font-weight:400}
.hd .rt .meta .k{color:var(--g3);display:inline-block;min-width:96px;text-align:left;text-transform:uppercase;letter-spacing:.14em;font-size:10.5px}
/* parties */
.parties{display:flex;gap:60px;margin-top:52px}
.party{flex:1}
.party .k{font-family:var(--mono);font-size:10.5px;letter-spacing:.22em;text-transform:uppercase;color:var(--red)}
.party .nm{font-family:var(--serif6);font-weight:600;font-size:20px;margin-top:12px;color:var(--ink)}
.party .ln{font-size:14.5px;color:var(--g2);line-height:1.7;margin-top:6px}
.party .ln a,.party .ln span{color:var(--g2)}
/* table */
table{width:100%;border-collapse:collapse;margin-top:56px}
thead th{font-family:var(--mono);font-size:10.5px;letter-spacing:.18em;text-transform:uppercase;color:var(--g3);
 text-align:left;padding:0 0 12px;border-bottom:1.6px solid var(--ink)}
thead th.c-qty,thead th.c-rate,thead th.c-amt{text-align:right}
tbody td{padding:20px 0;border-bottom:1px solid rgba(27,23,32,.12);vertical-align:top}
.c-desc .d{font-family:var(--serif6);font-weight:600;font-size:17px;color:var(--ink)}
.c-desc .sub{font-size:13px;color:var(--g3);margin-top:4px;font-family:var(--sans)}
.c-ph{width:150px}
.phase{display:inline-flex;align-items:center;gap:9px;font-family:var(--mono);font-size:11px;letter-spacing:.12em;
 text-transform:uppercase;color:var(--g2);white-space:nowrap}
.phase i{width:9px;height:9px;border-radius:50%;display:inline-block}
.c-qty,.c-rate,.c-amt{text-align:right;font-family:var(--mono);font-size:14px;color:var(--ink);white-space:nowrap}
.c-qty{width:80px;color:var(--g2)}.c-rate{width:130px;color:var(--g2)}.c-amt{width:140px}
/* totals */
.totwrap{display:flex;justify-content:space-between;gap:60px;margin-top:40px}
.pay{flex:1;max-width:520px}
.pay .k{font-family:var(--mono);font-size:10.5px;letter-spacing:.22em;text-transform:uppercase;color:var(--red)}
.pay .ln{font-family:var(--mono);font-size:12.5px;color:var(--g2);line-height:1.95;margin-top:12px}
.pay .ln b{color:var(--ink);font-weight:400}
.totals{width:420px}
.totals .row{display:flex;justify-content:space-between;align-items:baseline;padding:11px 0;font-family:var(--mono);
 font-size:14px;color:var(--g2)}
.totals .row .v{color:var(--ink)}
.totals .row.sub{border-bottom:1px solid rgba(27,23,32,.12)}
.totals .due{display:flex;justify-content:space-between;align-items:baseline;margin-top:16px;padding-top:18px;border-top:1.6px solid var(--ink)}
.totals .due .lbl{font-family:var(--mono);font-size:11px;letter-spacing:.2em;text-transform:uppercase;color:var(--ink);align-self:center}
.totals .due .amt{font-family:var(--word);font-size:52px;line-height:.9;color:var(--red)}
/* note */
.note{margin-top:auto;padding-top:30px;border-top:1px solid rgba(27,23,32,.12);display:flex;justify-content:space-between;align-items:flex-end;gap:40px}
.note .ty{font-family:var(--serif6);font-weight:600;font-style:italic;font-size:19px;color:var(--ink);max-width:560px;line-height:1.4}
.note .sig{text-align:right;font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--g3);line-height:1.8}
/* footer */
.foot{position:absolute;left:96px;right:96px;bottom:34px;display:flex;justify-content:space-between;align-items:center;
 font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--g3)}
.foot .d{color:var(--red)}
.botticks{position:absolute;left:0;right:0;bottom:0;height:22px;opacity:.5}
"""

HTML=('<!doctype html><meta charset=utf-8><title>invoice</title><style>'+CSS+'</style>'
 '<div class="frame">'
 '<div class="topticks">'+ticks(1240,34)+'</div>'
 '<div class="pad">'
   '<div class="hd">'
     '<div><div class="wm">BORN<span class="d">.</span></div>'
       '<div class="tag">Full-Service Apparel Development Studio</div></div>'
     '<div class="rt"><div class="lab">Invoice</div>'
       '<div class="meta">'
       '<div><span class="k">Invoice №</span> <b>BORN&ndash;0042</b></div>'
       '<div><span class="k">Issued</span> 04 Sep 2026</div>'
       '<div><span class="k">Due</span> 04 Oct 2026</div>'
       '</div></div>'
   '</div>'
   '<div class="parties">'
     '<div class="party"><div class="k">From</div>'
       '<div class="nm">Born Studio</div>'
       '<div class="ln">Full-service apparel development<br>hello@born.studio &middot; @born.studio<br>Ciudad de México, MX</div></div>'
     '<div class="party"><div class="k">Billed to</div>'
       '<div class="nm">Atelier Marisol</div>'
       '<div class="ln">Marisol Rivera, Founder<br>accounts@ateliermarisol.com<br>Av. Reforma 210, CDMX</div></div>'
   '</div>'
   '<table>'
     '<thead><tr><th class="c-desc">Description</th><th class="c-ph">Phase</th>'
       '<th class="c-qty">Qty</th><th class="c-rate">Rate</th><th class="c-amt">Amount</th></tr></thead>'
     '<tbody>'+rows()+'</tbody>'
   '</table>'
   '<div class="totwrap">'
     '<div class="pay"><div class="k">Payment</div>'
       '<div class="ln">Net 30 &middot; wire / ACH<br><b>Bank</b> BBVA &middot; <b>Acct</b> Born Studio S.A.<br>'
       'CLABE 012 180 00000000000 0<br>Ref. invoice number on transfer</div></div>'
     '<div class="totals">'
       '<div class="row sub"><span>Subtotal</span><span class="v">$'+SUBTOTAL+'</span></div>'
       '<div class="row"><span>Deposit received (50%)</span><span class="v">&minus;$'+DEPOSIT+'</span></div>'
       '<div class="due"><span class="lbl">Balance due (USD)</span><span class="amt">$'+BALANCE+'</span></div>'
     '</div>'
   '</div>'
   '<div class="note">'
     '<div class="ty">Thank you for letting us measure your idea, inch by inch.</div>'
     '<div class="sig">Sketched &middot; Stitched &middot; Born<br>From idea to life</div>'
   '</div>'
 '</div>'
 '<div class="foot"><span>born.studio</span><span>From idea to life<span class="d">.</span></span><span>Invoice BORN&ndash;0042</span></div>'
 '<div class="botticks">'+ticks(1240,22)+'</div>'
 '</div>')
open(f"{OUT}/invoice_1.html","w").write(HTML)
print("invoice written")
