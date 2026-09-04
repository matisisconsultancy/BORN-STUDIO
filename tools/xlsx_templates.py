#!/usr/bin/env python3
"""BORN Studio — redesigned Sourcing & Development trackers (v2, editorial).

Big type, index numbers, editorial group headers with a Rojo rule, tinted
cost zones, bold status chips, generous rows, frozen panes, filters,
dropdowns, conditional status colour, currency formats, an example row and a
'Start here' guide sheet.
"""
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter as L
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule
from openpyxl.comments import Comment
import openpyxl.worksheet.properties as wsprops
try:
    from openpyxl.cell.rich_text import CellRichText, TextBlock
    from openpyxl.cell.text import InlineFont
    RICH=True
except Exception:
    RICH=False
import os
OUTDIR="assets/templates"; os.makedirs(OUTDIR, exist_ok=True)

INK="FF1B1720"; INKD="FF14111A"; PAPER="FFF4F1E9"; PAPER2="FFECE7DC"
G2="FF4A454F"; G3="FF8A8590"; G4="FFB7B2BA"; RED="FFC4122E"; WHITE="FFFFFFFF"
WARM="FFFBF7EF"; COOL="FFEDE8DE"; HAIR="FFE2DCCF"; INKHAIR="FFCFC9BE"
SERIF="Georgia"; SANS="Arial"; MONO="Courier New"

def fillc(c): return PatternFill("solid", fgColor=c)
def S(c, style="thin"): return Side(style=style, color=c)
def box(l=None,r=None,t=None,b=None): return Border(left=l,right=r,top=t,bottom=b)

def merge(ws,r1,c1,r2,c2): ws.merge_cells(start_row=r1,start_column=c1,end_row=r2,end_column=c2)
def paint(ws,r1,c1,r2,c2,color):
    for r in range(r1,r2+1):
        for c in range(c1,c2+1): ws.cell(r,c).fill=fillc(color)

def banner(ws, ncols, title, subtitle):
    ws.sheet_view.showGridLines=False
    wend=min(ncols,6)
    ws.row_dimensions[1].height=42
    merge(ws,1,1,1,wend); paint(ws,1,1,1,ncols,INK)
    a=ws.cell(1,1)
    if RICH:
        a.value=CellRichText(TextBlock(InlineFont(rFont=SERIF,sz=26,b=True,color="FFFFFF"),"BORN"),
                             TextBlock(InlineFont(rFont=SERIF,sz=26,b=True,color="C4122E"),"."))
    else:
        a.value="BORN."; a.font=Font(name=SERIF,size=26,bold=True,color=WHITE)
    a.alignment=Alignment(horizontal="left",vertical="center",indent=1)
    merge(ws,1,wend+1,1,ncols)
    t=ws.cell(1,wend+1); t.value=title
    t.font=Font(name=MONO,size=15,bold=True,color=WHITE)
    t.alignment=Alignment(horizontal="right",vertical="center",indent=2)
    ws.row_dimensions[2].height=5; paint(ws,2,1,2,ncols,RED)
    ws.row_dimensions[3].height=22
    merge(ws,3,1,3,wend); paint(ws,3,1,3,ncols,PAPER)
    tg=ws.cell(3,1); tg.value="From idea to life"
    tg.font=Font(name=SERIF,size=11,italic=True,color=G2)
    tg.alignment=Alignment(horizontal="left",vertical="center",indent=1)
    merge(ws,3,wend+1,3,ncols)
    st=ws.cell(3,wend+1); st.value=subtitle
    st.font=Font(name=MONO,size=9,color=G3)
    st.alignment=Alignment(horizontal="right",vertical="center",indent=2)
    ws.row_dimensions[4].height=8; paint(ws,4,1,4,ncols,PAPER)

def group_header(ws,row,groups):
    ws.row_dimensions[row].height=28
    for c1,c2,label in groups:
        merge(ws,row,c1,row,c2)
        cell=ws.cell(row,c1); cell.value=label
        cell.font=Font(name=SERIF,size=13,bold=True,color=INK)
        cell.alignment=Alignment(horizontal="left",vertical="center",indent=1)
        for c in range(c1,c2+1):
            ws.cell(row,c).fill=fillc(PAPER)
            ws.cell(row,c).border=box(b=S(RED,"medium"))

def sub_header(ws,row,cols):
    ws.row_dimensions[row].height=40
    for i,(name,_w,_f,kind) in enumerate(cols,start=1):
        c=ws.cell(row,i); c.value=name; c.fill=fillc(PAPER)
        c.font=Font(name=MONO,size=8.5,color=G3)
        al="center" if kind in ("idx","num","cost_s","cost_g","cat","eval","samples") else "left"
        c.alignment=Alignment(horizontal=al,vertical="center",wrap_text=True,indent=0 if al=="center" else 1)
        c.border=box(b=S(INKHAIR))

def style_cell(c, kind, band):
    fill=band
    font=Font(name=SANS,size=11,color=INK); al=Alignment(horizontal="left",vertical="center",indent=1); nf=None
    bd=box(b=S(HAIR))
    if kind=="idx":
        font=Font(name=MONO,size=12,bold=True,color=RED); al=Alignment(horizontal="center",vertical="center")
    elif kind=="fct":
        font=Font(name=SERIF,size=13,bold=True,color=INK)
    elif kind in ("num","samples"):
        font=Font(name=MONO,size=11,color=INK); al=Alignment(horizontal="center",vertical="center")
    elif kind=="cost_s":
        font=Font(name=MONO,size=11,color=INK); al=Alignment(horizontal="center",vertical="center"); fill=WARM
    elif kind=="cost_g":
        font=Font(name=MONO,size=11,color=INK); al=Alignment(horizontal="center",vertical="center"); fill=COOL
    elif kind=="cat":
        font=Font(name=MONO,size=8.5,color=G2); al=Alignment(horizontal="center",vertical="center")
        bd=box(b=S(HAIR),l=S(G4),r=S(G4),t=S(G4))  # chip-like box (approx)
    elif kind=="eval":
        font=Font(name=SANS,size=11,bold=True,color=INK); al=Alignment(horizontal="center",vertical="center")
    c.fill=fillc(fill); c.font=font; c.alignment=al; c.border=bd
    return c

def data_body(ws,first,nrows,cols,example,fct_col_letter):
    for ridx in range(nrows):
        row=first+ridx
        ws.row_dimensions[row].height=26
        for i,(name,_w,numfmt,kind) in enumerate(cols,start=1):
            c=ws.cell(row,i)
            style_cell(c,kind,PAPER)
            if numfmt and kind!="idx": c.number_format=numfmt
            if kind=="idx":
                c.value=f'=IF(${fct_col_letter}{row}<>"",TEXT(ROW()-{first-1},"00"),"")'
            elif ridx==0 and name in example:
                c.value=example[name]
        if ridx==0:  # example row: subtle top rule + note
            for i in range(1,len(cols)+1):
                cur=ws.cell(row,i).border
                ws.cell(row,i).border=box(b=cur.bottom,l=cur.left,r=cur.right,t=S(G3))
            ws.cell(row,1).comment=Comment("Example row — overwrite or delete.\nEvery row below is yours to fill.","BORN Studio")

def clet(cols,name):
    for i,(n,*_ ) in enumerate(cols,start=1):
        if n==name: return L(i)

def build(path, sheet_title, banner_title, subtitle, groups, cols, example,
          fct_name, freeze_col, category_at=None, eval_at=None, glossary=None, nrows=40):
    wb=openpyxl.Workbook(); guide=wb.active; guide.title="Start here"
    ws=wb.create_sheet(sheet_title); ncols=len(cols)
    GH,SH,D0=5,6,7
    paint(ws,1,1,D0+nrows,ncols,PAPER)
    banner(ws,ncols,banner_title,subtitle)
    group_header(ws,GH,groups)
    sub_header(ws,SH,cols)
    data_body(ws,D0,nrows,cols,example,clet(cols,fct_name))
    for i,(_,w,_,_) in enumerate(cols,start=1): ws.column_dimensions[L(i)].width=w
    ws.freeze_panes=f"{freeze_col}{D0}"
    last=D0+nrows-1
    ws.auto_filter.ref=f"A{SH}:{L(ncols)}{last}"
    tips={"MOQ":"Minimum Order Quantity — smallest run the factory will make.",
          "Sample":"Sample lead time in working days.","Prod.":"Production lead time in working days.",
          "Evaluation":"Supplier status — pick from the dropdown.","Next Step":"The one action to move this supplier forward."}
    for name,tip in tips.items():
        cl=clet(cols,name)
        if cl: ws[f"{cl}{SH}"].comment=Comment(tip,"BORN Studio")
    if category_at:
        dv=DataValidation(type="list",formula1='"Knit,Woven,Activewear,Denim,Outerwear,Accessories,Trims & Notions"',
                          allow_blank=True,showErrorMessage=True)
        dv.promptTitle="Category"; dv.prompt="Pick a category"
        ws.add_data_validation(dv); dv.add(f"{category_at}{D0}:{category_at}{last}")
    if eval_at:
        dv=DataValidation(type="list",formula1='"Preferred,Shortlist,Hold,Pass"',allow_blank=True,showErrorMessage=True)
        dv.promptTitle="Evaluation"; dv.prompt="Set the supplier status"
        ws.add_data_validation(dv); dv.add(f"{eval_at}{D0}:{eval_at}{last}")
        rng=f"{eval_at}{D0}:{eval_at}{last}"
        for status,fg,fnt in [("Preferred",RED,Font(name=SANS,size=11,bold=True,color=WHITE)),
                              ("Shortlist","FFDED8CC",Font(name=SANS,size=11,bold=True,color=INK)),
                              ("Hold","FFF6E6C7",Font(name=SANS,size=11,color=G2)),
                              ("Pass",PAPER2,Font(name=SANS,size=11,italic=True,color=G4))]:
            ws.conditional_formatting.add(rng,CellIsRule(operator="equal",formula=[f'"{status}"'],fill=fillc(fg),font=fnt))
    build_guide(guide,banner_title,subtitle,glossary or [],bool(eval_at))
    ws.page_setup.orientation="landscape"; ws.page_setup.fitToWidth=1; ws.page_setup.fitToHeight=0
    ws.sheet_properties.pageSetUpPr=wsprops.PageSetupProperties(fitToPage=True)
    ws.page_margins.left=ws.page_margins.right=ws.page_margins.top=ws.page_margins.bottom=0.3
    wb.save(path); return path

def build_guide(ws,title,subtitle,glossary,has_eval):
    ws.sheet_view.showGridLines=False; W=8
    for i,w in {1:3,2:22,3:30,4:22,5:22,6:20,7:20,8:6}.items(): ws.column_dimensions[L(i)].width=w
    paint(ws,1,1,60,W,PAPER)
    banner(ws,W,title,subtitle)
    def heading(row,text):
        merge(ws,row,2,row,7); c=ws.cell(row,2); c.value=text
        c.font=Font(name=SERIF,size=16,bold=True,color=INK); c.alignment=Alignment(vertical="center")
        ws.row_dimensions[row].height=30
        for cc in range(2,8): ws.cell(row,cc).border=box(b=S(RED,"medium"))
    def body(row,text,font=None):
        merge(ws,row,2,row,7); c=ws.cell(row,2); c.value=text
        c.font=font or Font(name=SANS,size=11,color=G2)
        c.alignment=Alignment(horizontal="left",vertical="center",wrap_text=True)
        ws.row_dimensions[row].height=24
    r=7; heading(r,"How to use this tracker"); r+=1
    for s in ["Each row is one factory. Start on the first data row — the example shows the format.",
              "Fill left to right: who they are, how they produce, then their cost per style (USD).",
              "Sample cost = one prototype. Garment / production cost = per unit at MOQ.",
              "Use the ▾ filters on the header row to compare, sort and shortlist.",
              ("Set each supplier's status in Evaluation — Preferred lights up in Rojo." if has_eval
               else "Keep one clear Next Step per supplier so nothing stalls.")]:
        body(r,"—  "+s); r+=1
    r+=1; heading(r,"The key"); r+=1
    for kc,label,desc in [(INK,"Section header","Editorial groups: who / production / cost / status."),
                          (WARM,"Sample cost zone","Warm-tinted columns — prototype prices."),
                          (COOL,"Production cost zone","Cool-tinted columns — per-unit prices at MOQ."),
                          (RED,"Preferred","Your chosen factories light up in Rojo Valentino.")]:
        ws.row_dimensions[r].height=24
        ws.cell(r,2).fill=fillc(kc); ws.cell(r,2).border=box(l=S(INKHAIR),r=S(INKHAIR),t=S(INKHAIR),b=S(INKHAIR))
        c=ws.cell(r,3); c.value=label; c.font=Font(name=SANS,size=11,bold=True,color=INK)
        c.alignment=Alignment(horizontal="left",vertical="center",indent=1)
        merge(ws,r,4,r,7); d=ws.cell(r,4); d.value=desc; d.font=Font(name=SANS,size=11,color=G2)
        d.alignment=Alignment(horizontal="left",vertical="center"); r+=1
    r+=1
    if glossary:
        heading(r,"Field glossary"); r+=1
        for field,desc in glossary:
            ws.row_dimensions[r].height=22
            c=ws.cell(r,2); c.value=field; c.font=Font(name=SANS,size=11,bold=True,color=INK)
            c.alignment=Alignment(horizontal="left",vertical="center");
            for cc in range(2,8): ws.cell(r,cc).border=box(b=S(HAIR))
            merge(ws,r,4,r,7); d=ws.cell(r,4); d.value=desc; d.font=Font(name=SANS,size=11,color=G2)
            d.alignment=Alignment(horizontal="left",vertical="center"); r+=1
    r+=2
    merge(ws,r,2,r,7); f=ws.cell(r,2)
    f.value="Born Studio · Full-Service Apparel Development · v1.0"
    f.font=Font(name=MONO,size=9,color=G4)

# ============================================================ SOURCING
styles_s=["Shams Wide-Leg Leggings","Majara Regular Leggings","Qamar Long line top",
          "Suha Longline Integrated Tank-Bra","Zohra Heroine Jacket","Noor Dress"]
cols_s=[("#",5,None,"idx"),("Country",13,None,"meta"),("Category",15,None,"cat"),("Factory",27,None,"fct"),
        ("Website",20,None,"link"),("Email",24,None,"link"),("POC",15,None,"meta"),
        ("MOQ",8,'#,##0',"num"),("Sample",9,'0" d"',"num"),("Prod.",9,'0" d"',"num")]
cols_s+=[(s,13,'$#,##0',"cost_s") for s in styles_s]
cols_s+=[(s,13,'$#,##0',"cost_g") for s in styles_s]
cols_s+=[("Certifications",18,None,"meta"),("Vendors Folder",13,None,"link"),
         ("Notes",28,None,"meta"),("Evaluation",15,None,"eval")]
groups_s=[(2,4,"FACTORY"),(5,7,"CONTACT"),(8,10,"PRODUCTION"),
          (11,16,"SAMPLE COST · USD"),(17,22,"GARMENT COST · USD"),(23,26,"STATUS")]
ex_s={"Country":"Portugal","Category":"Activewear","Factory":"Atelier Norte",
      "Website":"ateliernorte.pt","Email":"hello@ateliernorte.pt","POC":"Marta Sousa",
      "MOQ":300,"Sample":15,"Prod.":45,
      "Shams Wide-Leg Leggings":65,"Majara Regular Leggings":55,"Qamar Long line top":45,
      "Suha Longline Integrated Tank-Bra":60,"Zohra Heroine Jacket":120,"Noor Dress":85,
      "Certifications":"GOTS · OEKO-TEX","Vendors Folder":"▸ Drive",
      "Notes":"Strong on technical knits; English-speaking POC.","Evaluation":"Preferred"}
gloss_s=[("Country / Category","Where they are and what they specialise in."),
         ("Factory","Legal or trade name you'll reference everywhere."),
         ("MOQ","Minimum Order Quantity per style / colour."),
         ("Sample / Prod.","Turnaround in working days."),
         ("Sample cost","Price of one prototype per style."),
         ("Garment cost","Per-unit production price at MOQ per style."),
         ("Certifications","GOTS, OEKO-TEX, BSCI…"),
         ("Vendors Folder","Link to their profile, quotes and docs."),
         ("Evaluation","Preferred · Shortlist · Hold · Pass.")]
def build_sourcing():
    p=f"{OUTDIR}/BORN_Sourcing_Tracker.xlsx"
    build(p,"Suppliers","SOURCING","Supplier sourcing · 2026",groups_s,cols_s,ex_s,
          fct_name="Factory",freeze_col="E",category_at="C",eval_at="Z",glossary=gloss_s)
    wb=openpyxl.load_workbook(p); ws=wb["Suppliers"]
    for i,v in enumerate([18,15,12,16,34,24]): ws.cell(7,17+i).value=v
    wb.save(p); return p

# ============================================================ DEVELOPMENT
styles_d=["Mid range WOMEN","Mid Range MEN","Premium MEN","Premium silicone","Basic MEN",
          "Hoodie UNISEX","Zip pullover","Fitted Hat","6 panel Hat"]
cols_d=[("#",5,None,"idx"),("Factory",27,None,"fct"),("Email",24,None,"link"),("POC",15,None,"meta"),
        ("MOQ",8,'#,##0',"num"),("Sample",9,'0" d"',"num"),("Prod.",9,'0" d"',"num")]
cols_d+=[(s,12,'$#,##0',"cost_s") for s in styles_d]
cols_d+=[(s,12,'$#,##0',"cost_g") for s in styles_d]
cols_d+=[("Payment Terms",18,None,"meta"),("Certifications",15,None,"meta"),
         ("Invoice",12,None,"link"),("Samples Cost",12,'$#,##0',"samples"),("Next Step",22,None,"meta")]
groups_d=[(2,4,"SUPPLIER"),(5,7,"PRODUCTION"),(8,16,"SAMPLE COST · USD"),
          (17,25,"PRODUCTION COST · USD"),(26,30,"TERMS & STATUS")]
ex_d={"Factory":"Atelier Norte","Email":"hello@ateliernorte.pt","POC":"Marta Sousa",
      "MOQ":300,"Sample":15,"Prod.":45,"Payment Terms":"30% deposit · Net 30",
      "Certifications":"OEKO-TEX","Invoice":"▸ link","Samples Cost":240,"Next Step":"Send tech packs"}
gloss_d=[("Factory","Legal or trade name."),("Email / POC","Contact and your point of contact."),
         ("MOQ","Minimum Order Quantity per style."),("Sample / Prod.","Turnaround in working days."),
         ("Sample cost","Prototype price per style."),("Production cost","Per-unit price at MOQ per style."),
         ("Payment Terms","Deposit % and net terms."),("Certifications","OEKO-TEX, GRS…"),
         ("Invoice","Link to the latest invoice."),("Samples Cost","Total spent on samples so far."),
         ("Next Step","The one action to move this factory forward.")]
def build_development():
    p=f"{OUTDIR}/BORN_Development_Tracker.xlsx"
    build(p,"Development","DEVELOPMENT","Product development · 2026",groups_d,cols_d,ex_d,
          fct_name="Factory",freeze_col="C",category_at=None,eval_at=None,glossary=gloss_d)
    wb=openpyxl.load_workbook(p); ws=wb["Development"]
    for i,v in enumerate([45,40,70,95,32,38,42,18,22]): ws.cell(7,8+i).value=v
    for i,v in enumerate([14,12,22,30,9,12,13,6,7]): ws.cell(7,17+i).value=v
    wb.save(p); return p

print(build_sourcing()); print(build_development())
