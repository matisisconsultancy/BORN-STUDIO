#!/usr/bin/env python3
"""Faithful HTML preview of the redesigned BORN trackers (for a PNG mock).
Mirrors the .xlsx design with the Office-safe font stack it actually uses."""
import os
OUT="tools/_work/collateral"; os.makedirs(OUT,exist_ok=True)
styles_s=["Shams Wide-Leg Leggings","Majara Regular Leggings","Qamar Long line top",
          "Suha Longline Integrated Tank-Bra","Zohra Heroine Jacket","Noor Dress"]
styles_d=["Mid range WOMEN","Mid Range MEN","Premium MEN","Premium silicone","Basic MEN",
          "Hoodie UNISEX","Zip pullover","Fitted Hat","6 panel Hat"]

CSS="""
*{margin:0;padding:0;box-sizing:border-box}
body{background:#8f8b93;font-family:Arial,'Helvetica Neue',sans-serif;padding:40px}
.wrap{display:inline-block;background:#6E6A73;padding:46px}
.sheet{background:#F2EEE6;box-shadow:0 30px 70px -20px rgba(0,0,0,.5);overflow:hidden}
.banner{background:#1B1720;display:flex;justify-content:space-between;align-items:center;padding:16px 22px}
.banner .wm{font-family:Georgia,'Times New Roman',serif;font-size:27px;font-weight:700;color:#fff;letter-spacing:.5px}
.banner .wm .d{color:#C4122E}
.banner .title{font-family:'Courier New',monospace;color:#fff;font-size:13px;letter-spacing:3px}
.rule{height:5px;background:#C4122E}
.tag{display:flex;justify-content:space-between;padding:5px 22px 7px}
.tag .l{font-family:Georgia,serif;font-style:italic;color:#4A454F;font-size:12px}
.tag .r{font-family:'Courier New',monospace;color:#8A8590;font-size:10px;letter-spacing:1px}
table{border-collapse:collapse;width:100%;table-layout:fixed}
.grp td{background:#1B1720;color:#fff;font-family:Georgia,serif;font-weight:700;text-align:center;
 border-bottom:3px solid #C4122E;border-left:1px solid #14111A;border-right:1px solid #14111A;font-size:12.5px;padding:7px 4px;letter-spacing:.5px}
.sub td{background:#DED8CC;color:#1B1720;font-weight:700;font-size:10px;text-align:center;padding:7px 4px;
 border:1px solid #cfc9be;vertical-align:middle;line-height:1.2}
tbody td{font-size:11px;padding:7px 7px;border:1px solid #E4DFD4;color:#1B1720;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
tbody tr:nth-child(odd) td{background:#F2EEE6}
tbody tr:nth-child(even) td{background:#EAE5DA}
tbody tr.ex td{border-top:2px solid #8A8590}
.cost{font-family:'Courier New',monospace;text-align:center;color:#1B1720}
.num{font-family:'Courier New',monospace;text-align:center}
.pill{display:inline-block;font-weight:700;font-size:10px;padding:3px 0;border-radius:2px;width:100%;text-align:center}
.p-pref{background:#C4122E;color:#fff}
.p-short{background:#DED8CC;color:#1B1720}
.p-hold{background:#F6E6C7;color:#4A454F}
.p-pass{background:#EAE5DA;color:#B7B2BA;font-style:italic}
"""

def sheet(title, kicker, groups, subs, rows, width):
    ncol=len(subs)
    grp="".join(f'<td colspan="{c2-c1+1}">{lab}</td>' for c1,c2,lab in groups)
    sub="".join(f'<td>{s}</td>' for s in subs)
    body=""
    for cls,cells in rows:
        tds="".join(cells)
        body+=f'<tr class="{cls}">{tds}</tr>'
    return f'''<div class="wrap"><div class="sheet" style="width:{width}px">
      <div class="banner"><div class="wm">BORN<span class="d">.</span></div><div class="title">{title}</div></div>
      <div class="rule"></div>
      <div class="tag"><div class="l">From idea to life</div><div class="r">{kicker}</div></div>
      <table><colgroup>{''.join('<col>' for _ in range(ncol))}</colgroup>
      <thead><tr class="grp">{grp}</tr><tr class="sub">{sub}</tr></thead>
      <tbody>{body}</tbody></table></div></div>'''

def td(v="",cls=""): return f'<td class="{cls}">{v}</td>'
def cost(v): return td(f"${v:,}","cost")
def pill(status):
    k={"Preferred":"p-pref","Shortlist":"p-short","Hold":"p-hold","Pass":"p-pass"}[status]
    return f'<td><span class="pill {k}">{status}</span></td>'

# ---------- SOURCING preview
subs_s=["Country","Category","Factory Name","Website","Email","POC","MOQ","Sample Lead","Prod. Lead"]+styles_s+styles_s+["Certifications","Vendors Folder","Notes","Evaluation"]
groups_s=[(1,3,"FACTORY"),(4,6,"CONTACT"),(7,9,"PRODUCTION"),(10,15,"SAMPLE COST · USD"),(16,21,"GARMENT COST · USD"),(22,25,"REFERENCE & STATUS")]
def srow(country,cat,name,web,email,poc,moq,sl,pl,scost,gcost,cert,folder,notes,ev,ex=False):
    cells=[td(country),td(cat),td(f"<b>{name}</b>"),td(web),td(email),td(poc),
           td(f"{moq:,}","num"),td(f"{sl} d","num"),td(f"{pl} d","num")]
    cells+=[cost(x) for x in scost]+[cost(x) for x in gcost]
    cells+=[td(cert),td(folder),td(notes)]+[pill(ev)]
    return ("ex" if ex else "", cells)
rows_s=[
 srow("Portugal","Activewear","Atelier Norte","ateliernorte.pt","hello@ateliernorte.pt","Marta Sousa",300,15,45,
      [65,55,45,60,120,85],[18,15,12,16,34,24],"GOTS · OEKO-TEX","▸ Drive","Strong on technical knits.","Preferred",ex=True),
 srow("Türkiye","Knit","Bosphorus Knitworks","bosphorusknit.com","sales@bosphorusknit.com","Emre K.",500,20,55,
      [58,50,42,54,110,78],[16,13,11,14,30,21],"BSCI","▸ Drive","Great price, longer lead.","Shortlist"),
 srow("India","Woven","Surat Textile Co.","surattextile.in","info@surattextile.in","Priya N.",800,25,60,
      [40,36,30,38,84,60],[11,10,8,10,22,16],"SEDEX","▸ Drive","High MOQ; verify quality.","Hold"),
 srow("Mexico","Activewear","Taller Monterrey","tallermty.mx","hola@tallermty.mx","Luis R.",250,18,40,
      [72,62,52,66,128,92],[20,17,14,18,36,26],"—","▸ Drive","Nearshore; small runs.","Pass"),
]

# ---------- DEVELOPMENT preview
subs_d=["Factory Name","Email","POC","MOQ","Sample Lead","Prod. Lead"]+styles_d+styles_d+["Payment Terms","Certifications","Invoice","Samples Cost","Next Step"]
groups_d=[(1,3,"SUPPLIER"),(4,6,"PRODUCTION"),(7,15,"SAMPLE COST · USD"),(16,24,"PRODUCTION COST · USD"),(25,29,"TERMS & STATUS")]
def drow(name,email,poc,moq,sl,pl,scost,pcost,pay,cert,inv,sc,nxt,ex=False):
    cells=[td(f"<b>{name}</b>"),td(email),td(poc),td(f"{moq:,}","num"),td(f"{sl} d","num"),td(f"{pl} d","num")]
    cells+=[cost(x) for x in scost]+[cost(x) for x in pcost]
    cells+=[td(pay),td(cert),td(inv),cost(sc),td(nxt)]
    return ("ex" if ex else "", cells)
rows_d=[
 drow("Atelier Norte","hello@ateliernorte.pt","Marta Sousa",300,15,45,
      [45,40,70,95,32,38,42,18,22],[14,12,22,30,9,12,13,6,7],"30% deposit · Net 30","OEKO-TEX","▸ link",240,"Send tech packs",ex=True),
 drow("Bosphorus Knitworks","sales@bosphorusknit.com","Emre K.",500,20,55,
      [42,38,66,90,30,35,40,17,20],[13,11,21,28,8,11,12,6,7],"50% deposit","BSCI","▸ link",190,"Approve sample 2"),
 drow("Taller Monterrey","hola@tallermty.mx","Luis R.",250,18,40,
      [48,43,74,98,34,40,44,19,24],[15,13,23,31,10,13,14,7,8],"Net 15","—","▸ link",300,"Cost negotiation"),
]

html_s=sheet("SOURCING TRACKER","Supplier sourcing · v1.0",groups_s,subs_s,rows_s,2560)
html_d=sheet("DEVELOPMENT TRACKER","Product development · v1.0",groups_d,subs_d,rows_d,2760)
open(f"{OUT}/xlsx_sourcing.html","w").write(f"<!doctype html><meta charset=utf-8><style>{CSS}</style>{html_s}")
open(f"{OUT}/xlsx_development.html","w").write(f"<!doctype html><meta charset=utf-8><style>{CSS}</style>{html_d}")
print("previews written")
