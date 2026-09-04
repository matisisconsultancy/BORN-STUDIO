#!/usr/bin/env python3
"""Editorial preview of the redesigned BORN trackers (v2 — bigger, airier)."""
import os
OUT="tools/_work/collateral"; os.makedirs(OUT,exist_ok=True)
styles_s=["Shams Wide-Leg Leggings","Majara Regular Leggings","Qamar Long line top",
          "Suha Longline Integrated Tank-Bra","Zohra Heroine Jacket","Noor Dress"]
styles_d=["Mid range WOMEN","Mid Range MEN","Premium MEN","Premium silicone","Basic MEN",
          "Hoodie UNISEX","Zip pullover","Fitted Hat","6 panel Hat"]

CSS="""
*{margin:0;padding:0;box-sizing:border-box}
body{background:#8f8b93;font-family:Arial,'Helvetica Neue',sans-serif;padding:44px}
.wrap{display:inline-block;background:#6E6A73;padding:52px}
.sheet{background:#F4F1E9;box-shadow:0 36px 90px -24px rgba(0,0,0,.55);overflow:hidden;border-radius:2px}
/* banner */
.banner{background:#1B1720;display:flex;justify-content:space-between;align-items:center;padding:26px 40px}
.banner .wm{font-family:Georgia,'Times New Roman',serif;font-size:44px;font-weight:700;color:#fff;letter-spacing:.5px;line-height:1}
.banner .wm .d{color:#C4122E}
.banner .rt{text-align:right}
.banner .rt .t{font-family:'Courier New',monospace;color:#fff;font-size:19px;letter-spacing:6px}
.banner .rt .s{font-family:'Courier New',monospace;color:#B7B2BA;font-size:11px;letter-spacing:2px;margin-top:8px}
.rule{height:7px;background:#C4122E}
.tag{display:flex;justify-content:space-between;align-items:baseline;padding:16px 40px 6px}
.tag .l{font-family:Georgia,serif;font-style:italic;color:#4A454F;font-size:18px}
.tag .r{font-family:'Courier New',monospace;color:#8A8590;font-size:11px;letter-spacing:1.5px}
/* table */
table{border-collapse:collapse;width:100%;table-layout:fixed}
/* group headers */
.grp td{padding:20px 14px 12px;vertical-align:bottom;background:#F4F1E9}
.grp td span{font-family:Georgia,serif;font-weight:700;color:#1B1720;font-size:17px;letter-spacing:1.5px;
 text-transform:uppercase;border-bottom:3px solid #C4122E;padding-bottom:8px;display:inline-block}
.grp td.cost span{color:#1B1720}
.grp-line td{border-bottom:1.5px solid #1B1720;height:0;padding:0}
/* subheaders */
.sub td{font-family:'Courier New',monospace;font-size:10.5px;letter-spacing:1px;text-transform:uppercase;
 color:#8A8590;padding:12px 14px;vertical-align:bottom;border-bottom:1px solid #d8d2c6}
.sub td.c{text-align:center}
/* zones */
.z-sample{background:#FBF7EF}
.z-garment{background:#ECE7DC}
/* data */
tbody td{padding:16px 14px;border-bottom:1px solid #e2dccf;color:#1B1720;font-size:13px;vertical-align:middle;
 white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
td.idx{font-family:'Courier New',monospace;color:#C4122E;font-size:15px;font-weight:700;text-align:center}
td.fct{font-family:Georgia,serif;font-weight:700;font-size:18px;color:#1B1720}
td.meta{color:#4A454F;font-size:13px}
.chip{display:inline-block;border:1.4px solid #B7B2BA;border-radius:3px;padding:3px 11px;font-family:'Courier New',monospace;
 font-size:11px;letter-spacing:.5px;text-transform:uppercase;color:#4A454F}
td.cost{font-family:'Courier New',monospace;font-size:14px;text-align:center;color:#1B1720}
td.num{font-family:'Courier New',monospace;font-size:14px;text-align:center;color:#4A454F}
.status{display:inline-block;font-size:12px;font-weight:700;padding:7px 16px;border-radius:4px;letter-spacing:.5px}
.s-pref{background:#C4122E;color:#fff}
.s-short{background:transparent;color:#1B1720;border:1.6px solid #1B1720}
.s-hold{background:#F6E6C7;color:#6b5a2e}
.s-pass{background:transparent;color:#B7B2BA;font-style:italic;font-weight:400}
"""

def sheet(title, sub, groups, subs, rows):
    ncol=len(subs)
    width=sum(w for _,_,w in subs)
    grp="".join(f'<td colspan="{c2-c1+1}" class="{cl}"><span>{lab}</span></td>' for c1,c2,lab,cl in groups)
    line="".join('<td></td>' for _ in range(ncol))
    subh="".join(f'<td class="{cl}">{s}</td>' for s,cl,_ in subs)
    cols="".join(f'<col style="width:{w}px">' for _,_,w in subs)
    body=""
    for cells in rows: body+="<tr>"+"".join(cells)+"</tr>"
    return f'''<div class="wrap"><div class="sheet" style="width:{width}px">
      <div class="banner"><div class="wm">BORN<span class="d">.</span></div>
        <div class="rt"><div class="t">{title}</div><div class="s">{sub}</div></div></div>
      <div class="rule"></div>
      <div class="tag"><div class="l">From idea to life</div><div class="r">FILTER · SORT · SHORTLIST</div></div>
      <table><colgroup>{cols}</colgroup>
      <thead><tr class="grp">{grp}</tr><tr class="grp-line">{line}</tr><tr class="sub">{subh}</tr></thead>
      <tbody>{body}</tbody></table></div></div>'''

def status(s):
    k={"Preferred":"s-pref","Shortlist":"s-short","Hold":"s-hold","Pass":"s-pass"}[s]
    return f'<td><span class="status {k}">{s}</span></td>'

# ---------------- SOURCING
groups_s=[(1,1,"",""),(2,4,"FACTORY",""),(5,7,"CONTACT",""),(8,10,"PRODUCTION",""),
          (11,16,"SAMPLE COST · USD","cost"),(17,22,"GARMENT COST · USD","cost"),(23,26,"STATUS","")]
subs_s=[("#","c",50),("Country","",96),("Category","",124),("Factory","",214)]\
      +[("Website","",140),("Email","",172),("POC","",118)]\
      +[("MOQ","c",76),("Sample","c",76),("Prod.","c",76)]\
      +[(s,"c z-sample",100) for s in styles_s]+[(s,"c z-garment",100) for s in styles_s]\
      +[("Certifications","",140),("Folder","",92),("Notes","",180),("Evaluation","c",128)]
def srow(i,country,cat,name,web,email,poc,moq,sl,pl,sc,gc,cert,folder,notes,ev):
    c=[f'<td class="idx">{i:02d}</td>',f'<td class="meta">{country}</td>',
       f'<td><span class="chip">{cat}</span></td>',f'<td class="fct">{name}</td>',
       f'<td class="meta">{web}</td>',f'<td class="meta">{email}</td>',f'<td class="meta">{poc}</td>',
       f'<td class="num">{moq:,}</td>',f'<td class="num">{sl} d</td>',f'<td class="num">{pl} d</td>']
    c+=[f'<td class="cost z-sample">${x:,}</td>' for x in sc]
    c+=[f'<td class="cost z-garment">${x:,}</td>' for x in gc]
    c+=[f'<td class="meta">{cert}</td>',f'<td class="meta">▸ {folder}</td>',f'<td class="meta">{notes}</td>',status(ev)]
    return c
rows_s=[
 srow(1,"Portugal","Activewear","Atelier Norte","ateliernorte.pt","hello@ateliernorte.pt","Marta Sousa",300,15,45,
      [65,55,45,60,120,85],[18,15,12,16,34,24],"GOTS · OEKO-TEX","Drive","Strong on technical knits.","Preferred"),
 srow(2,"Türkiye","Knit","Bosphorus Knitworks","bosphorusknit.com","sales@bosphorusknit.com","Emre K.",500,20,55,
      [58,50,42,54,110,78],[16,13,11,14,30,21],"BSCI","Drive","Great price, longer lead.","Shortlist"),
 srow(3,"India","Woven","Surat Textile Co.","surattextile.in","info@surattextile.in","Priya N.",800,25,60,
      [40,36,30,38,84,60],[11,10,8,10,22,16],"SEDEX","Drive","High MOQ; verify quality.","Hold"),
 srow(4,"Mexico","Activewear","Taller Monterrey","tallermty.mx","hola@tallermty.mx","Luis R.",250,18,40,
      [72,62,52,66,128,92],[20,17,14,18,36,26],"—","Drive","Nearshore; small runs.","Pass"),
]

# ---------------- DEVELOPMENT
groups_d=[(1,1,"",""),(2,4,"SUPPLIER",""),(5,7,"PRODUCTION",""),
          (8,16,"SAMPLE COST · USD","cost"),(17,25,"PRODUCTION COST · USD","cost"),(26,30,"TERMS & STATUS","")]
subs_d=[("#","c",50),("Factory","",214),("Email","",172),("POC","",118)]\
      +[("MOQ","c",76),("Sample","c",76),("Prod.","c",76)]\
      +[(s,"c z-sample",98) for s in styles_d]+[(s,"c z-garment",98) for s in styles_d]\
      +[("Payment","",150),("Certs","",112),("Invoice","",92),("Samples $","c",104),("Next Step","",172)]
def drow(i,name,email,poc,moq,sl,pl,sc,pc,pay,cert,inv,scost,nxt):
    c=[f'<td class="idx">{i:02d}</td>',f'<td class="fct">{name}</td>',
       f'<td class="meta">{email}</td>',f'<td class="meta">{poc}</td>',
       f'<td class="num">{moq:,}</td>',f'<td class="num">{sl} d</td>',f'<td class="num">{pl} d</td>']
    c+=[f'<td class="cost z-sample">${x:,}</td>' for x in sc]
    c+=[f'<td class="cost z-garment">${x:,}</td>' for x in pc]
    c+=[f'<td class="meta">{pay}</td>',f'<td class="meta">{cert}</td>',f'<td class="meta">▸ {inv}</td>',
        f'<td class="cost">${scost:,}</td>',f'<td class="meta">{nxt}</td>']
    return c
rows_d=[
 drow(1,"Atelier Norte","hello@ateliernorte.pt","Marta Sousa",300,15,45,
      [45,40,70,95,32,38,42,18,22],[14,12,22,30,9,12,13,6,7],"30% dep · Net 30","OEKO-TEX","link",240,"Send tech packs"),
 drow(2,"Bosphorus Knitworks","sales@bosphorusknit.com","Emre K.",500,20,55,
      [42,38,66,90,30,35,40,17,20],[13,11,21,28,8,11,12,6,7],"50% deposit","BSCI","link",190,"Approve sample 2"),
 drow(3,"Taller Monterrey","hola@tallermty.mx","Luis R.",250,18,40,
      [48,43,74,98,34,40,44,19,24],[15,13,23,31,10,13,14,7,8],"Net 15","—","link",300,"Cost negotiation"),
]

html_s=sheet("SOURCING","Supplier sourcing · 2026",groups_s,subs_s,rows_s)
html_d=sheet("DEVELOPMENT","Product development · 2026",groups_d,subs_d,rows_d)
open(f"{OUT}/xlsx_sourcing.html","w").write(f"<!doctype html><meta charset=utf-8><style>{CSS}</style>{html_s}")
open(f"{OUT}/xlsx_development.html","w").write(f"<!doctype html><meta charset=utf-8><style>{CSS}</style>{html_d}")
print("previews v2 written")
