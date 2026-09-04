#!/usr/bin/env python3
"""BORN Studio — the room engine.

Turns tools/room_data.py into one standalone page a client opens by link.

The whole system rests on two channels that are never mixed:

  REGISTER  which phase of the craft a piece of information belongs to.
            It sets the world — ground, texture, rule, type treatment.
            sketched (construction grid, dotted rule, graphite)
            stitched (diagonal hatch, stitch-dash rule, ink)
            born     (clean paper, solid rule, the red dot)

  STATE     whether the thing has happened. It sets the marker only.
            done · now · next

So the reader knows, at a glance and without a legend, both where in the craft
they are and what is settled. Scrolling the logbook is watching the garment go
from drawn, to sewn, to made.

Emits deliverables/index.html and tools/_work/room_artifact.html (body form).
"""
import base64, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from room_data import *          # noqa: F403 — the project content

S, W, O = "tools/src", "tools/_work", "deliverables"
os.makedirs(W, exist_ok=True)
rd = lambda p: open(p, encoding="utf-8").read()

def datauri(path, mime):
    return f"data:{mime};base64," + base64.b64encode(open(path, "rb").read()).decode("ascii")

FONTS = rd(f"{S}/fonts.css")
ROOT  = rd(f"{S}/root.css")
DEFS  = rd(f"{S}/defs.svg")
SVG   = {k: rd(f"{S}/{k}.svg") for k in
         ["wm_solo", "wm_solo_neg", "state_sketch", "state_stitch", "state_born"]}
IMG   = {f[:-4]: datauri(f"{O}/assets/{f}", "image/jpeg")
         for f in sorted(os.listdir(f"{O}/assets")) if f.endswith(".jpg")}

FAVICON = ("data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2064%2064'"
 "%3E%3Crect%20width='64'%20height='64'%20rx='13'%20fill='%231B1720'/%3E"
 "%3Ctext%20x='29'%20y='47'%20font-family='Georgia,Times,serif'%20font-size='46'%20font-weight='700'"
 "%20text-anchor='middle'%20fill='%23F2EEE6'%3EB%3C/text%3E%3Ccircle%20cx='47'%20cy='44'%20r='5'%20fill='%23C4122E'/%3E%3C/svg%3E")

SIZES = ["XS", "S", "M", "L", "XL"]
BY_NO = {s["no"]: s for s in STYLES}
MONTHS = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]

def money(v, cur="€"): return f"{cur}{v:,.2f}"

def cm(v):
    """Points of measure carry the decimals they were specified with — 9.0, not 9,
    and 0.72 when the tolerance is read to hundredths."""
    return f"{v:.2f}" if round(v * 100) % 10 else f"{v:.1f}"

def date(iso):
    if not iso or iso == "—": return iso
    y, m, d = iso.split("-")
    return f"{int(d)} {MONTHS[int(m)-1]} {y}"

def daymonth(iso):
    y, m, d = iso.split("-")
    return d, f"{MONTHS[int(m)-1]} {y}"

def mk(state, label=None):
    """The maturity marker. Outline · stitch · solid with the red dot."""
    if state in ("done", "born"):
        body = ('<rect x="1" y="1" width="9" height="9" fill="currentColor"/>'
                '<circle cx="11.5" cy="11.5" r="2.4" fill="#C4122E"/>')
    elif state in ("now", "stitched"):
        body = ('<rect x="1.6" y="1.6" width="9.8" height="9.8" fill="none" stroke="currentColor"'
                ' stroke-width="1.5" stroke-dasharray="2.6 2"/>')
    else:
        body = ('<rect x="1.6" y="1.6" width="9.8" height="9.8" fill="none" stroke="currentColor"'
                ' stroke-width="1.2" stroke-dasharray="1.5 2.2" opacity=".5"/>')
    return (f'<svg class="mk" viewBox="0 0 14 14" role="img" aria-label="{label or state}">'
            f'<title>{label or state.capitalize()}</title>{body}</svg>')

# ═══════════════════════════════════════════════════════════════════════ CSS ═
CSS = ROOT + r"""
:root{
  --sheet:#FBF8F2; --sheet-2:#F4F0E7;
  --rule:rgba(27,23,32,.13); --rule-2:rgba(27,23,32,.28);
  --graphite:#5C5762;
  --topH:54px; --ribH:34px;
  --gut:clamp(3.2rem,7vw,5.4rem);        /* date gutter */
  --col:minmax(0,68ch);
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:calc(var(--topH) + var(--ribH) + 1rem)}
body{background:var(--paper);color:var(--ink);font-family:var(--sans);line-height:1.6;
  font-size:15.5px;-webkit-font-smoothing:antialiased}
img,svg{display:block;max-width:100%}
a{color:inherit}
::selection{background:var(--red);color:var(--paper)}
:focus-visible{outline:2px solid var(--red);outline-offset:3px;border-radius:2px}
.wrap{max-width:1120px;margin:0 auto;padding:0 clamp(1.1rem,4vw,3rem)}
.read{max-width:70ch}

/* ═══ chrome ══════════════════════════════════════════════════════════════ */
.top{position:sticky;top:0;z-index:60;background:rgba(242,238,230,.94);
  backdrop-filter:blur(14px);border-bottom:1px solid var(--rule)}
.top__in{display:flex;align-items:center;gap:1rem;max-width:1120px;margin:0 auto;
  padding:.42rem clamp(1.1rem,4vw,3rem);min-height:var(--topH);flex-wrap:wrap}
.top .mark{display:flex;align-items:center;gap:.6rem;text-decoration:none;flex:0 0 auto}
.top .mark svg{height:22px;width:auto;max-width:none}
.top .mark span{font-family:var(--mono);font-size:.53rem;letter-spacing:.18em;
  text-transform:uppercase;color:var(--g3);border-left:1px solid var(--rule);padding-left:.6rem}
.nav{display:flex;gap:.05rem;margin-left:auto;flex-wrap:wrap}
.nav button{font-family:var(--mono);font-size:.61rem;letter-spacing:.13em;text-transform:uppercase;
  color:var(--g2);background:none;border:0;cursor:pointer;padding:.46rem .62rem;border-radius:5px;
  white-space:nowrap;transition:color .18s,background .18s}
.nav button:hover{color:var(--ink);background:var(--paper-2)}
.nav button[aria-selected=true]{color:var(--paper);background:var(--ink)}
.nav .div{width:1px;background:var(--rule);margin:.4rem .45rem;align-self:stretch}

/* status ribbon — one line, always true, always visible */
.rib{position:sticky;top:var(--topH);z-index:55;background:var(--ink);color:var(--paper)}
.rib__in{max-width:1120px;margin:0 auto;padding:.5rem clamp(1.1rem,4vw,3rem);min-height:var(--ribH);
  display:flex;align-items:center;gap:.55rem 1.5rem;flex-wrap:wrap;
  font-family:var(--mono);font-size:.6rem;letter-spacing:.13em;text-transform:uppercase}
.rib b{font-weight:400;color:var(--paper)}
.rib .s{color:var(--g4)}
.rib .r{color:var(--red)}
.rib .dot{width:6px;height:6px;border-radius:50%;background:var(--red);display:inline-block;
  vertical-align:middle;margin-right:.4rem}
@media(prefers-reduced-motion:no-preference){
  .rib .dot{animation:pulse 3s var(--ease) 1s 3}
  @keyframes pulse{0%{box-shadow:0 0 0 0 rgba(196,18,46,.6)}
    70%{box-shadow:0 0 0 7px rgba(196,18,46,0)}100%{box-shadow:0 0 0 0 rgba(196,18,46,0)}}}

.panel{display:none}
.panel.active{display:block}

/* the maturity marker, and the path classes the stage wordmarks are drawn with */
.mk{width:13px;height:13px;flex:0 0 auto;display:block}
.p-sk{fill:none;stroke:var(--g2);stroke-linejoin:round}
.p-skc{fill:none;stroke:var(--g2);stroke-linecap:round}
.p-st{stroke:var(--ink);stroke-linejoin:round}
.p-ink{fill:var(--ink)}
.p-bo{fill:var(--red)}

/* ═══ standfirst — where we are, before the story starts ══════════════════ */
.stand{padding:clamp(2.4rem,6vw,4.6rem) 0 clamp(1.8rem,4vw,3rem)}
.stand .k{font-family:var(--mono);font-size:.6rem;letter-spacing:.24em;text-transform:uppercase;
  color:var(--red)}
.stand h1{font-family:var(--serif);font-weight:900;font-size:clamp(2.4rem,6.4vw,4.4rem);
  line-height:.98;letter-spacing:-.025em;margin:.7rem 0;max-width:16ch;text-wrap:balance}
.stand .lede{font-family:var(--serif6);font-weight:600;font-size:clamp(1.12rem,2vw,1.42rem);
  line-height:1.42;color:var(--g2);max-width:46ch}
.stand__grid{display:grid;grid-template-columns:1.35fr 1fr;gap:clamp(1.6rem,4vw,3.4rem);
  align-items:end}
@media(max-width:840px){.stand__grid{grid-template-columns:1fr}}
.facts{display:grid;grid-template-columns:repeat(2,1fr);gap:1.1rem 1.4rem}
.facts dt{font-family:var(--mono);font-size:.54rem;letter-spacing:.17em;text-transform:uppercase;
  color:var(--g3)}
.facts dd{font-family:var(--mono);font-size:.86rem;margin-top:.2rem;font-variant-numeric:tabular-nums}
.facts dd.big{font-family:var(--serif);font-weight:900;font-size:1.7rem;letter-spacing:-.01em}

/* the three-phase meter — solid where done, stitched where live, ghost ahead */
.meter{display:flex;align-items:center;gap:.5rem;margin:1.6rem 0 .5rem}
.meter i{height:2px;display:block;flex:1}
.meter i.done{background:var(--ink)}
.meter i.live{background:repeating-linear-gradient(90deg,var(--ink) 0 5px,transparent 5px 10px)}
.meter i.todo{background:var(--g4);opacity:.45}
.meter b{width:8px;height:8px;border-radius:50%;background:var(--red);flex:0 0 auto}
.meter__l{display:flex;justify-content:space-between;font-family:var(--mono);font-size:.55rem;
  letter-spacing:.15em;text-transform:uppercase;color:var(--g3)}

/* the one thing that needs the client */
.ask{border:1px solid var(--red);border-radius:2px;padding:1.05rem 1.25rem;
  margin:clamp(1.8rem,4vw,2.8rem) 0 0;display:flex;gap:1rem;align-items:flex-start;
  background:rgba(196,18,46,.035);max-width:none}
.ask .k{font-family:var(--mono);font-size:.55rem;letter-spacing:.18em;text-transform:uppercase;
  color:var(--red)}
.ask p{font-size:.92rem;margin-top:.25rem;color:var(--ink)}
.ask .mk{color:var(--red);margin-top:.28rem}

/* ═══ registers — the ambient world of each phase ═════════════════════════ */
.reg{position:relative}
.reg--sketched{
  --rule-style:dotted; --rule-col:var(--g4); --txt:var(--graphite);
  background-image:linear-gradient(rgba(74,69,79,.052) 1px,transparent 1px),
                   linear-gradient(90deg,rgba(74,69,79,.052) 1px,transparent 1px);
  background-size:27px 27px}
.reg--stitched{
  --rule-style:dashed; --rule-col:var(--rule-2); --txt:var(--ink);
  background-image:repeating-linear-gradient(45deg,rgba(27,23,32,.035) 0 1px,transparent 1px 10px)}
.reg--born{--rule-style:solid; --rule-col:var(--rule-2); --txt:var(--ink);
  background:var(--sheet)}

/* register band — the chapter break */
.band{border-top:1px solid var(--ink)}
.band__in{max-width:1120px;margin:0 auto;padding:clamp(1.6rem,3.4vw,2.6rem) clamp(1.1rem,4vw,3rem);
  display:grid;grid-template-columns:var(--gut) minmax(0,1fr) minmax(0,22ch);
  gap:1rem clamp(1rem,3vw,2.4rem);align-items:start}
@media(max-width:840px){.band__in{grid-template-columns:1fr;gap:.7rem}}
.band .n{padding-top:.5rem;font-family:var(--serif);font-weight:900;font-size:clamp(2.6rem,6vw,4rem);
  line-height:.8;letter-spacing:-.03em;color:var(--txt)}
.band h2{font-family:var(--serif);font-weight:900;font-size:clamp(1.5rem,3.2vw,2.2rem);
  line-height:1;letter-spacing:-.015em}
.band .lg{width:min(268px,100%);margin-top:.85rem}
.band .lg svg{width:100%;height:auto}
.band .ln{font-family:var(--serif6);font-weight:600;font-size:1rem;color:var(--g2);margin-top:.4rem}
.band .df{font-size:.84rem;color:var(--g2);line-height:1.55}
.band .win{font-family:var(--mono);font-size:.56rem;letter-spacing:.15em;text-transform:uppercase;
  color:var(--g3);margin-top:.6rem}
.band--born{background:var(--ink);color:var(--paper);border-top-color:var(--ink)}
.band--born .n,.band--born h2{color:var(--paper)}
.band--born .ln,.band--born .df{color:var(--g4)}
.band--born .win{color:var(--g3)}
.band--born .p-ink{fill:var(--paper)}
.band--born .p-st{stroke:var(--paper)}
.band--born .p-sk,.band--born .p-skc{stroke:var(--g4)}

/* ═══ the logbook spine ═══════════════════════════════════════════════════ */
.log{padding-bottom:clamp(2rem,5vw,3.6rem)}
.e{max-width:1120px;margin:0 auto;padding:0 clamp(1.1rem,4vw,3rem);
  display:grid;grid-template-columns:var(--gut) 26px minmax(0,1fr);align-items:stretch}
.e__d{padding:1.6rem .8rem 0 0;text-align:right}
.e__d .dd{font-family:var(--serif);font-weight:900;font-size:clamp(1.5rem,3vw,2rem);
  line-height:.9;display:block;letter-spacing:-.02em;color:var(--txt)}
.e__d .mm{font-family:var(--mono);font-size:.55rem;letter-spacing:.12em;text-transform:uppercase;
  color:var(--g3);display:block;margin-top:.3rem}
.e__s{position:relative}
.e__s::before{content:'';position:absolute;top:0;bottom:0;left:50%;
  border-left:1px var(--rule-style) var(--rule-col)}
.e:first-child .e__s::before{top:1.9rem}
.e:last-child .e__s::before{bottom:auto;height:1.9rem}
.e__s .mk{position:absolute;top:1.55rem;left:50%;transform:translateX(-50%);
  background:var(--paper);padding:3px 0;box-sizing:content-box;color:var(--txt)}
.reg--born .e__s .mk{background:var(--sheet)}
.e__b{padding:1.5rem 0 1.9rem 0;min-width:0}
.e__k{font-family:var(--mono);font-size:.56rem;letter-spacing:.19em;text-transform:uppercase;
  color:var(--g3)}
.e__h{font-family:var(--serif);font-weight:900;font-size:clamp(1.15rem,2.3vw,1.62rem);
  line-height:1.14;letter-spacing:-.012em;margin:.3rem 0 .5rem;max-width:26ch;text-wrap:balance}
.e__p{color:var(--g2);max-width:66ch;font-size:.95rem}
.reg--sketched .e__h{color:var(--graphite)}
.reg--sketched .e__p{font-family:var(--serif6);font-weight:600;font-size:1rem;color:var(--graphite)}

/* state: done · now · next — the marker, and nothing else */
.e.st-next .e__d .dd,.e.st-next .e__h{color:var(--g3)}
.e.st-next .e__p{color:var(--g3)}
.e.st-next .e__s::before{opacity:.42}
.e.st-now .e__k{color:var(--red)}
.e.st-now .e__s .mk{color:var(--red)}
.e.is-ask .e__h,.e.is-ask .e__d .dd{color:var(--ink)}
.e.is-ask .e__p{color:var(--g2)}
.e.is-ask .e__k{color:var(--red)}
.e.is-ask .e__s .mk{color:var(--red)}
.e.is-ask .e__s::before{opacity:1}
.e.st-now .e__h::after{content:'';display:inline-block;width:7px;height:7px;border-radius:50%;
  background:var(--red);margin-left:.5rem;vertical-align:.12em}

/* ═══ payloads ════════════════════════════════════════════════════════════ */
.pay{margin-top:1.15rem}
.pay--wide{max-width:none}

/* decision — chosen against considered, and the reason */
.dec{display:grid;grid-template-columns:1fr 1fr;gap:0;border:1px solid var(--rule-2);
  border-radius:2px;overflow:hidden;background:var(--sheet)}
@media(max-width:620px){.dec{grid-template-columns:1fr}}
.dec > div{padding:.95rem 1.1rem}
.dec .a{border-right:1px solid var(--rule)}
@media(max-width:620px){.dec .a{border-right:0;border-bottom:1px solid var(--rule)}}
.dec .b{background:repeating-linear-gradient(45deg,rgba(27,23,32,.03) 0 1px,transparent 1px 7px)}
.dec .lb{font-family:var(--mono);font-size:.54rem;letter-spacing:.18em;text-transform:uppercase;
  color:var(--g3);display:flex;align-items:center;gap:.45rem}
.dec .a .lb{color:var(--red)}
.dec .v{font-family:var(--serif6);font-weight:600;font-size:1.02rem;margin-top:.35rem;line-height:1.3}
.dec .b .v{color:var(--g3);text-decoration:line-through;text-decoration-color:var(--g4)}
.dec__why{grid-column:1/-1;border-top:1px solid var(--rule);font-size:.9rem;color:var(--g2)}
.dec__why b{color:var(--ink);font-weight:500}
.dec__cost{display:inline-block;margin-top:.7rem;font-family:var(--mono);font-size:.62rem;
  letter-spacing:.1em;color:var(--ink);border:1px solid var(--rule-2);border-radius:2px;
  padding:.18rem .5rem}

/* measure — only what moved, with the delta */
.meas{border:1px solid var(--rule-2);border-radius:2px;background:var(--sheet)}
.meas__h{display:flex;justify-content:space-between;gap:1rem;flex-wrap:wrap;
  padding:.75rem 1.05rem;border-bottom:1px solid var(--rule);
  font-family:var(--mono);font-size:.58rem;letter-spacing:.13em;text-transform:uppercase;
  color:var(--g3)}
.meas__h b{color:var(--ink);font-weight:400}
.meas__b{padding:.3rem 1.05rem .85rem}
.meas__f{padding:.7rem 1.05rem;border-top:1px solid var(--rule);display:flex;
  justify-content:space-between;gap:1rem;flex-wrap:wrap;align-items:center}
.clear{font-family:var(--mono);font-size:.62rem;letter-spacing:.1em;color:var(--g2)}
.clear b{color:var(--ink);font-weight:400}

/* materials — carried against dropped */
.mat tr.no td{color:var(--g3)}
.mat tr.no .em{text-decoration:line-through;text-decoration-color:var(--g4)}

/* sample + renders + flats */
.strip{display:grid;grid-template-columns:repeat(auto-fit,minmax(132px,1fr));gap:.6rem}
.strip figure{margin:0;border:1px solid var(--rule);background:#fff;overflow:hidden;border-radius:2px}
.strip img{width:100%;height:auto;aspect-ratio:3/4;object-fit:cover}
.strip figcaption{font-family:var(--mono);font-size:.53rem;letter-spacing:.11em;
  text-transform:uppercase;color:var(--g3);padding:.42rem .5rem;background:var(--sheet)}
.strip--flat img{aspect-ratio:16/10;object-fit:contain;background:#fff;padding:.5rem}
.strip--wide{grid-template-columns:repeat(auto-fit,minmax(190px,1fr))}
.vd{display:inline-flex;align-items:center;gap:.45rem;margin-top:.8rem;
  font-family:var(--mono);font-size:.6rem;letter-spacing:.13em;text-transform:uppercase;
  border:1px solid var(--rule-2);border-radius:2px;padding:.28rem .6rem;color:var(--g2)}
.vd.no{border-color:var(--red);color:var(--red)}

/* colour standards */
.cws{display:grid;grid-template-columns:repeat(auto-fit,minmax(112px,1fr));gap:.55rem}
.cw{border:1px solid var(--rule);border-radius:2px;overflow:hidden;background:var(--sheet)}
.cw i{display:block;height:62px}
.cw .b{padding:.48rem .58rem}
.cw .code{font-family:var(--mono);font-size:.55rem;letter-spacing:.05em;color:var(--g3)}
.cw .nm{font-family:var(--serif6);font-weight:600;font-size:.86rem;margin-top:.05rem}

/* release — the document this entry produced */
.rel{display:flex;align-items:center;gap:1rem;border:1px solid var(--ink);border-radius:2px;
  padding:.85rem 1.05rem;background:var(--sheet);flex-wrap:wrap}
.rel .ic{width:30px;flex:0 0 auto;color:var(--ink)}
.rel .t{flex:1 1 200px;min-width:0}
.rel .t .nm{font-family:var(--serif6);font-weight:600;font-size:1.05rem}
.rel .t .nt{font-family:var(--mono);font-size:.58rem;letter-spacing:.1em;text-transform:uppercase;
  color:var(--g3);margin-top:.12rem}
.rel .go{font-family:var(--mono);font-size:.6rem;letter-spacing:.13em;text-transform:uppercase;
  background:var(--ink);color:var(--paper);border:0;border-radius:2px;padding:.45rem .8rem;
  cursor:pointer;transition:background .18s}
.rel .go:hover{background:var(--red)}

/* approval — given, or waiting on the client */
.apr{border:1px solid var(--rule-2);border-radius:2px;padding:.9rem 1.1rem;background:var(--sheet);
  display:flex;gap:.9rem;align-items:flex-start;flex-wrap:wrap}
.apr .mk{margin-top:.25rem;color:var(--g2)}
.apr .lb{font-family:var(--mono);font-size:.55rem;letter-spacing:.17em;text-transform:uppercase;
  color:var(--g3)}
.apr .v{font-family:var(--serif6);font-weight:600;font-size:1rem;margin-top:.2rem}
.apr .w{font-family:var(--mono);font-size:.6rem;letter-spacing:.06em;color:var(--g2);margin-top:.3rem}
.apr--wait{border-color:var(--red);background:rgba(196,18,46,.035)}
.apr--wait .lb{color:var(--red)}
.apr--wait .mk{color:var(--red)}

/* watch — a risk, and what removes it */
.alr{border:1px solid var(--rule-2);border-radius:2px;background:var(--sheet);overflow:hidden}
.alr > div{padding:.85rem 1.05rem}
.alr .r{border-bottom:1px solid var(--rule);
  background:repeating-linear-gradient(45deg,rgba(196,18,46,.045) 0 1px,transparent 1px 8px)}
.alr .lb{font-family:var(--mono);font-size:.54rem;letter-spacing:.18em;text-transform:uppercase;
  color:var(--g3)}
.alr .r .lb{color:var(--red)}
.alr p{font-size:.9rem;color:var(--g2);margin-top:.3rem}
.alr .ow{font-family:var(--mono);font-size:.58rem;letter-spacing:.1em;text-transform:uppercase;
  color:var(--red);margin-top:.6rem}
"""

CSS += r"""
/* ═══ documents ═══════════════════════════════════════════════════════════ */
.docwrap{padding:clamp(1.2rem,3vw,2.4rem) clamp(1.1rem,4vw,3rem) 5rem;max-width:1080px;margin:0 auto}
.sheet{background:var(--sheet);border:1px solid var(--rule);border-radius:2px;
  box-shadow:0 24px 54px -38px rgba(27,23,32,.45);padding:clamp(1.6rem,3.6vw,3.2rem)}
.mast{display:flex;justify-content:space-between;align-items:flex-start;gap:1.5rem;
  padding-bottom:1.1rem;border-bottom:2px solid var(--ink);flex-wrap:wrap}
.mast__l{flex:1 1 340px;min-width:0}
.mast__l .type{font-family:var(--mono);font-size:.58rem;letter-spacing:.24em;
  text-transform:uppercase;color:var(--red)}
.mast__l h1{font-family:var(--serif);font-weight:900;font-size:clamp(1.7rem,3.6vw,2.6rem);
  line-height:1.02;letter-spacing:-.018em;margin:.25rem 0 .3rem;text-wrap:balance}
.mast__l .who{font-size:.9rem;color:var(--g2)}
.mast__r{text-align:right;flex:0 0 auto;padding-top:.2rem}
.mast__r svg{height:21px;width:auto;max-width:none;margin-left:auto}
.mast__r .meta{font-family:var(--mono);font-size:.57rem;letter-spacing:.1em;text-transform:uppercase;
  color:var(--g3);line-height:1.9;margin-top:.5rem}
.mast__r .meta b{color:var(--ink);font-weight:400}
.dl{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:1rem 1.6rem;
  margin-top:1.2rem}
.dl > div{min-width:0}
.dl dt{font-family:var(--mono);font-size:.54rem;letter-spacing:.16em;text-transform:uppercase;
  color:var(--g3)}
.dl dd{font-family:var(--mono);font-size:.83rem;margin-top:.15rem;font-variant-numeric:tabular-nums}
.sec{margin-top:clamp(1.8rem,3.4vw,2.6rem)}
.sec--rule{border-top:1px solid var(--rule);padding-top:clamp(1.4rem,2.6vw,2rem)}
.eyebrow{font-family:var(--mono);font-size:.57rem;letter-spacing:.2em;text-transform:uppercase;
  color:var(--g3);margin-bottom:.9rem}
h2.h{font-family:var(--serif);font-weight:900;font-size:clamp(1.25rem,2.4vw,1.7rem);
  line-height:1.08;letter-spacing:-.01em;text-wrap:balance}
h3.sh{font-family:var(--serif6);font-weight:600;font-size:1.05rem;margin-bottom:.35rem}
p.body{color:var(--g2);max-width:68ch}
p.body + p.body{margin-top:.7rem}
p.body b{color:var(--ink);font-weight:500}
.note{font-family:var(--mono);font-size:.65rem;letter-spacing:.03em;color:var(--g3);
  line-height:1.75;max-width:78ch}
.two{display:grid;grid-template-columns:1.35fr 1fr;gap:1.5rem;align-items:start}
.two--even{grid-template-columns:1fr 1fr}
@media(max-width:820px){.two,.two--even{grid-template-columns:1fr}}
.plate{background:#fff;border:1px solid var(--rule);border-radius:2px;padding:1rem;
  display:flex;align-items:center;justify-content:center}

/* tables */
.tw{overflow-x:auto;-webkit-overflow-scrolling:touch}
table.t{border-collapse:collapse;width:100%;min-width:520px;font-size:.81rem}
table.t th{font-family:var(--mono);font-size:.55rem;letter-spacing:.15em;text-transform:uppercase;
  color:var(--g3);text-align:left;padding:0 .7rem .5rem 0;border-bottom:1px solid var(--ink);
  white-space:nowrap;font-weight:400;vertical-align:bottom}
table.t td{padding:.5rem .7rem;padding-left:0;border-bottom:1px solid var(--rule);vertical-align:top}
table.t tr:last-child td{border-bottom:0}
table.t .n{font-family:var(--mono);text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
table.t th.n{text-align:right}
table.t td:last-child,table.t th:last-child{padding-right:0}
table.t .c{font-family:var(--mono);font-size:.73rem;letter-spacing:.04em;color:var(--g2);white-space:nowrap}
table.t .em{font-family:var(--serif6);font-weight:600;font-size:.94rem}
table.t tr.grp td{border-bottom:0;padding-top:1.1rem;padding-bottom:.2rem}
table.t tr.grp .gt{font-family:var(--mono);font-size:.57rem;letter-spacing:.16em;
  text-transform:uppercase;color:var(--red)}
table.t tr.sum td{border-top:1px solid var(--ink);border-bottom:0;padding-top:.7rem}
table.t tr.tot td{border-top:2px solid var(--ink);border-bottom:0;padding-top:.75rem;
  font-family:var(--serif6);font-weight:600;font-size:1.14rem}
table.t tr.tot .n{font-family:var(--mono);font-size:1.14rem;color:var(--red)}
.out{color:var(--red)}
.tag{display:inline-block;padding:.05rem .38rem;border:1px solid var(--rule-2);border-radius:2px;
  font-family:var(--mono);font-size:.58rem;letter-spacing:.1em;text-transform:uppercase;color:var(--g2)}
.tag--r{border-color:var(--red);color:var(--red)}

/* lists */
ul.li{list-style:none;display:grid;gap:.52rem}
ul.li li{padding-left:1.3rem;position:relative;color:var(--g2);line-height:1.5;max-width:74ch}
ul.li li::before{content:'';position:absolute;left:0;top:.62em;width:8px;height:2px;background:var(--red)}
ul.li--q li::before{background:var(--g4)}
ol.num{list-style:none;counter-reset:c;display:grid;gap:.95rem}
ol.num li{counter-increment:c;padding-left:2rem;position:relative;color:var(--g2);max-width:74ch}
ol.num li::before{content:counter(c,decimal-leading-zero);position:absolute;left:0;top:.05em;
  font-family:var(--mono);font-size:.66rem;color:var(--red);letter-spacing:.04em}
ol.num li b{color:var(--ink);font-weight:500}

.chips{display:flex;gap:.32rem;flex-wrap:wrap;margin-bottom:1.3rem}
.chip{font-family:var(--mono);font-size:.61rem;letter-spacing:.1em;text-transform:uppercase;
  background:none;border:1px solid var(--rule-2);color:var(--g2);border-radius:18px;
  padding:.32rem .74rem;cursor:pointer;transition:all .18s}
.chip:hover{border-color:var(--ink);color:var(--ink)}
.chip[aria-pressed=true]{background:var(--ink);border-color:var(--ink);color:var(--paper)}
.styl{display:none}.styl.on{display:block}

.pay-g{display:grid;grid-template-columns:repeat(auto-fit,minmax(178px,1fr));gap:.75rem}
.pay-g > div{border:1px solid var(--rule);border-radius:2px;padding:.85rem 1rem;background:var(--sheet-2)}
.pay-g .pc{font-family:var(--serif);font-weight:900;font-size:1.85rem;line-height:1}
.pay-g .wh{font-family:var(--mono);font-size:.56rem;letter-spacing:.14em;text-transform:uppercase;
  color:var(--g3);margin:.32rem 0 .1rem}
.pay-g .am{font-family:var(--mono);font-size:.84rem;font-variant-numeric:tabular-nums}
.due{border:1px solid var(--red);border-radius:2px;padding:1.2rem 1.4rem;display:flex;
  justify-content:space-between;align-items:center;gap:1.3rem 2rem;flex-wrap:wrap}
.due > div{flex:1 1 auto;min-width:0}
.due .l{font-family:var(--mono);font-size:.58rem;letter-spacing:.18em;text-transform:uppercase;color:var(--red)}
.due .v{font-family:var(--serif);font-weight:900;font-size:clamp(1.7rem,4vw,2.5rem);line-height:1}
.due .d{font-family:var(--mono);font-size:.66rem;line-height:1.8;color:var(--g2);text-align:right;flex:0 1 34ch}
.sign{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:2rem;margin-top:2.4rem}
.sign .nm{font-family:var(--serif6);font-weight:600;font-size:1rem}
.sign .rl{font-family:var(--mono);font-size:.56rem;letter-spacing:.14em;text-transform:uppercase;
  color:var(--g3);margin-top:.15rem}
.sign .ln{margin-top:1.5rem;border-bottom:1px solid var(--rule-2);height:1px}
.sign .lb{font-family:var(--mono);font-size:.53rem;letter-spacing:.14em;text-transform:uppercase;
  color:var(--g4);margin-top:.32rem}
.dfoot{margin-top:2.4rem;padding-top:1rem;border-top:1px solid var(--rule);display:flex;
  justify-content:space-between;gap:1rem;flex-wrap:wrap;font-family:var(--mono);font-size:.55rem;
  letter-spacing:.12em;text-transform:uppercase;color:var(--g3)}
.printbtn{font-family:var(--mono);font-size:.6rem;letter-spacing:.13em;text-transform:uppercase;
  background:none;border:1px solid var(--rule-2);color:var(--ink);border-radius:5px;
  padding:.42rem .76rem;cursor:pointer;transition:all .18s}
.printbtn:hover{background:var(--ink);color:var(--paper);border-color:var(--ink)}

/* ═══ the system view ═════════════════════════════════════════════════════ */
.sys{padding:clamp(2rem,5vw,3.6rem) 0 5rem}
.spec{display:grid;grid-template-columns:repeat(auto-fit,minmax(258px,1fr));gap:1.1rem;margin-top:1.3rem}
.spec > article{border:1px solid var(--rule);border-radius:2px;overflow:hidden;background:var(--sheet)}
.spec .sw{padding:1.15rem 1.2rem;border-bottom:1px solid var(--rule);min-height:112px}
.spec .sw--sketched{background-image:linear-gradient(rgba(74,69,79,.075) 1px,transparent 1px),
  linear-gradient(90deg,rgba(74,69,79,.075) 1px,transparent 1px);background-size:22px 22px}
.spec .sw--stitched{background-image:repeating-linear-gradient(45deg,rgba(27,23,32,.06) 0 1px,transparent 1px 9px)}
.spec .sw--born{background:var(--ink)}
.spec .sw svg{width:100%;height:auto;max-width:180px}
.spec .sb{padding:.95rem 1.2rem}
.spec .sb h3{font-family:var(--serif);font-weight:900;font-size:1.3rem;line-height:1}
.spec .sb .ln{font-family:var(--serif6);font-weight:600;font-size:.92rem;color:var(--g2);margin:.25rem 0 .5rem}
.spec .sb p{font-size:.86rem;color:var(--g2);line-height:1.5}
.kinds{display:grid;grid-template-columns:repeat(auto-fit,minmax(232px,1fr));gap:.8rem;margin-top:1.2rem}
.kinds > div{border:1px solid var(--rule);border-radius:2px;padding:.9rem 1rem;background:var(--sheet)}
.kinds .kn{font-family:var(--mono);font-size:.58rem;letter-spacing:.16em;text-transform:uppercase;
  color:var(--red)}
.kinds .kd{font-size:.86rem;color:var(--g2);margin-top:.3rem;line-height:1.5}
pre.code{background:var(--ink);color:var(--paper);border-radius:2px;padding:1.1rem 1.25rem;
  overflow-x:auto;font-family:var(--mono);font-size:.72rem;line-height:1.75;margin-top:1rem}
pre.code .cm{color:var(--g3)}
pre.code .st{color:#E8A0AE}
pre.code .ky{color:var(--g4)}

/* ═══ print ═══════════════════════════════════════════════════════════════ */
@page{size:A4;margin:13mm}
@media print{
  .top,.rib,.printbtn,.chips,.rel .go{display:none!important}
  body{background:#fff;font-size:10.4pt}
  .panel:not(.active){display:none}
  .docwrap{padding:0;max-width:none}
  .sheet{border:0;box-shadow:none;padding:0;background:#fff}
  .styl{display:block!important}
  .styl + .styl{page-break-before:always}
  .sec--rule,.tw,table.t tr,.strip figure,.e,.dec,.meas,.alr{page-break-inside:avoid}
  .band{page-break-before:always;background:#fff!important;color:#000!important}
  .band--born *{color:#000!important}
  .reg{background-image:none!important}
  .due,.ask,.apr--wait{border:1px solid #000;background:#fff}
  .stand{padding-top:0}
}
"""

# ═══════════════════════════════════════════════════════════════ payloads ════
# Each returns the block that belongs to one kind of information. Anatomy above
# them is identical; only this changes, so density follows the content.

def pay_decision(p):
    return f"""<div class="dec">
 <div class="a"><p class="lb">{mk('done')} Chosen</p><p class="v">{p['chosen']}</p></div>
 <div class="b"><p class="lb">Considered</p><p class="v">{p['considered']}</p></div>
 <div class="dec__why"><p>{p['why']}</p><span class="dec__cost">{p['cost']}</span></div>
</div>"""

def pay_materials(p):
    rows = "".join(
        f'<tr class="{"" if keep else "no"}"><td class="c">{ref}</td><td class="em">{desc}</td>'
        f'<td class="n">{gsm}</td><td class="c">{stretch}</td><td class="c">{rec}</td>'
        f'<td>{"" if keep else ""}{verdict}</td></tr>'
        for ref, desc, gsm, stretch, rec, verdict, keep in p["rows"])
    return (f'<div class="tw"><table class="t mat" style="min-width:600px"><thead><tr>'
            f'<th>Ref</th><th>Quality</th><th class="n">Weight</th><th>Stretch</th>'
            f'<th>Recovery</th><th>Verdict</th></tr></thead><tbody>{rows}</tbody></table></div>')

def pay_colour(p):
    cws = "".join(f'<div class="cw"><i style="background:{h}"></i><div class="b">'
                  f'<div class="code">{c}</div><div class="nm">{n}</div></div></div>'
                  for c, n, h, _ in COLORWAYS)
    return f'<div class="cws">{cws}</div>'

def pay_flats(p):
    figs = "".join(
        f'<figure><img src="{IMG[BY_NO[no]["img"]]}" alt="{BY_NO[no]["name"]} technical flat">'
        f'<figcaption>{no} &middot; {BY_NO[no]["short"]}</figcaption></figure>' for no in p["styles"])
    return f'<div class="strip strip--flat strip--wide">{figs}</div>'

def pay_renders(p):
    figs = "".join(f'<figure><img src="{IMG[k]}" alt="{cap}"><figcaption>{cap}</figcaption></figure>'
                   for k, cap in p["keys"])
    return f'<div class="strip">{figs}</div>'

def pay_sample(p):
    figs = "".join(f'<figure><img src="{IMG[k]}" alt="{cap}"><figcaption>{cap}</figcaption></figure>'
                   for k, cap in p["keys"])
    cls = "vd" if p["ok"] else "vd no"
    return (f'<div class="strip">{figs}</div>'
            f'<span class="{cls}">{mk("done" if p["ok"] else "now")} {p["round"]} &middot; {p["verdict"]}</span>')

def pay_measure(p):
    rows = "".join(
        f'<tr><td class="c">{sn}</td><td class="c">{code}</td><td>{name}</td>'
        f'<td class="n">{cm(spec)}</td><td class="n">{cm(got)}</td>'
        f'<td class="n out">{got - spec:+.2f}</td><td class="n">&plusmn;{cm(tol)}</td>'
        f'<td><span class="tag{" tag--r" if owner == "Pattern" or owner == "Block" else ""}">{owner}</span></td></tr>'
        for sn, code, name, spec, got, tol, owner in p["rows"])
    more = (f' &middot; {p["more"]} further points listed in the report' if p.get("more") else "")
    go = (f'<button class="rel go" data-go="{p["go"]}">Full points of measure &rarr;</button>'
          if p.get("go") else "")
    return f"""<div class="meas">
 <div class="meas__h"><span>Out of tolerance &middot; <b>{p['session']}</b></span>
   <span>Measured against <b>{p['spec']}</b></span></div>
 <div class="meas__b"><div class="tw"><table class="t" style="min-width:600px"><thead><tr>
   <th>Style</th><th>Code</th><th>Point of measure</th><th class="n">Spec</th>
   <th class="n">Got</th><th class="n">Dev.</th><th class="n">Tol.</th><th>Cause</th>
  </tr></thead><tbody>{rows}</tbody></table></div></div>
 <div class="meas__f"><span class="clear">{mk('done')} <b>{p['clear']} of {p['total']}</b>
   points measured clean{more}</span>{go}</div>
</div>"""

DOC_ICON = ('<svg viewBox="0 0 30 34" fill="none" stroke="currentColor" stroke-width="1.4">'
  '<path d="M4 1h14l8 8v24H4z"/><path d="M18 1v8h8" stroke-dasharray="2.4 2"/>'
  '<path d="M9 17h12M9 22h12M9 27h7"/><circle cx="24" cy="27" r="2.6" fill="#C4122E" stroke="none"/></svg>')

def pay_release(p):
    go = (f'<button class="go" data-go="{p["go"]}">Open &rarr;</button>' if p.get("go") else "")
    rev = f' &middot; {p["rev"]}' if p.get("rev") and p["rev"] != "—" else ""
    return f"""<div class="rel"><span class="ic">{DOC_ICON}</span>
 <span class="t"><span class="nm">{p['name']}{rev}</span>
  <span class="nt">{p.get('note','')}</span></span>{go}</div>"""

def pay_approval(p):
    wait = p["status"] == "waiting"
    return f"""<div class="apr{' apr--wait' if wait else ''}">{mk('next' if wait else 'done')}
 <div><p class="lb">{'Waiting on you' if wait else 'Approved'}</p>
  <p class="v">{p['what']}</p>
  <p class="w">{p['who']} &middot; {'by ' if wait else ''}{date(p['when'])}</p></div></div>"""

def pay_alert(p):
    return f"""<div class="alr">
 <div class="r"><p class="lb">The risk</p><p>{p['risk']}</p></div>
 <div><p class="lb">What removes it</p><p>{p['fix']}</p><p class="ow">{p['owner']}</p></div></div>"""

PAYLOADS = {"decision": pay_decision, "materials": pay_materials, "colour": pay_colour,
            "flats": pay_flats, "renders": pay_renders, "sample": pay_sample,
            "measure": pay_measure, "release": pay_release, "approval": pay_approval,
            "alert": pay_alert}

# ═════════════════════════════════════════════════════════ the logbook ═══════
def entry(e):
    dd, mm = daymonth(e["date"])
    ask = e.get("pay", {}).get("type") == "approval" and e["pay"]["status"] == "waiting"
    pay = ""
    if e.get("pay"):
        pay = f'<div class="pay">{PAYLOADS[e["pay"]["type"]](e["pay"])}</div>'
    body = f'<p class="e__p">{e["body"]}</p>' if e.get("body") else ""
    return f"""<article class="e st-{e['state']}{' is-ask' if ask else ''}" id="e-{e['date']}">
 <div class="e__d"><span class="dd">{dd}</span><span class="mm">{mm}</span></div>
 <div class="e__s">{mk(e['state'], e['state'])}</div>
 <div class="e__b"><p class="e__k">{e['kind']}</p><h3 class="e__h">{e['title']}</h3>
  {body}{pay}</div>
</article>"""

def band(key):
    r = REGISTERS[key]
    ph = next(p for p in PHASES if p["key"] == key)
    logo = {"sketched": SVG["state_sketch"], "stitched": SVG["state_stitch"],
            "born": SVG["state_born"]}[key]
    return f"""<div class="band{' band--born' if key == 'born' else ''}"><div class="band__in">
 <div class="n">{r['n']}</div>
 <div><h2>{r['name']}</h2><p class="ln">{r['line']}</p>
   <div class="lg">{logo}</div>
   <p class="win">{ph['title']} &middot; {ph['window']}</p></div>
 <div><p class="df">{r['defn']}</p></div>
</div></div>"""

def logbook():
    out = []
    for key in ["sketched", "stitched", "born"]:
        rows = "".join(entry(e) for e in ENTRIES if e["phase"] == key)
        out.append(f'<section class="reg reg--{key}">{band(key)}<div class="log">{rows}</div></section>')
    return "".join(out)

# ═══════════════════════════════════════════════════════ standfirst + chrome ═
def counts():
    done = sum(1 for e in ENTRIES if e["state"] == "done")
    return done, len(ENTRIES)

def waiting():
    """The one thing the client has to do. Everything else is BORN's problem."""
    return next((e for e in ENTRIES
                 if e.get("pay", {}).get("type") == "approval"
                 and e["pay"]["status"] == "waiting"), None)

def standfirst():
    done, total = counts()
    live = next(p for p in PHASES if p["state"] == "stitched")
    now = next(e for e in ENTRIES if e["state"] == "now")
    ask = waiting()
    askblock = ""
    if ask:
        askblock = f"""<div class="ask">{mk('next')}
 <div><p class="k">Waiting on you &middot; by {date(ask['pay']['when'])}</p>
  <p>{ask['title']} {ask['body'].split('.')[0]}.</p></div></div>"""
    bars = ""
    for p in PHASES:
        cls = {"born": "done", "stitched": "live", "sketched": "todo"}[p["state"]]
        bars += f'<i class="{cls}"></i>' + ("<b></b>" if p["state"] == "stitched" else "")
    return f"""<div class="wrap stand"><div class="stand__grid">
 <div>
  <p class="k">Logbook &middot; {PROJECT['client_long']}</p>
  <h1>{now['title'].rstrip('.')}</h1>
  <p class="lede">{PROJECT['capsule']} &middot; {PROJECT['drop']}. Six styles, five colour
   standards, {PROJECT['units']:,} units. Every decision, sample and measurement below,
   with the date it happened and the reason behind it.</p>
 </div>
 <div>
  <dl class="facts">
   <div><dt>Phase</dt><dd class="big">{live['n'].replace('Phase ','')}</dd></div>
   <div><dt>Signed off</dt><dd class="big">{done}/{total}</dd></div>
   <div><dt>Reference</dt><dd>{PROJECT['ref']}</dd></div>
   <div><dt>Ex-factory</dt><dd>{date(PROJECT['exfactory'])}</dd></div>
   <div><dt>Size range</dt><dd>{PROJECT['size_range']} &middot; base {PROJECT['base_size']}</dd></div>
   <div><dt>Your contact</dt><dd>{PROJECT['studio_person']}, {PROJECT['studio']}</dd></div>
  </dl>
  <div class="meter" aria-label="Progress across the three phases">{bars}</div>
  <div class="meter__l"><span>Sketched</span><span>Stitched</span><span>BORN</span></div>
 </div>
</div>{askblock}</div>"""

DOCS = [("logbook", "Logbook"), ("techpack", "Tech pack"), ("fitting", "Fitting"),
        ("quote", "Quote"), ("invoice", "Invoice"), ("handover", "Handover"),
        ("system", "System")]

def top():
    tabs = ""
    for i, (k, lbl) in enumerate(DOCS):
        if k in ("techpack", "system"): tabs += '<span class="div"></span>'
        tabs += (f'<button role="tab" id="t-{k}" aria-controls="p-{k}" data-doc="{k}" '
                 f'aria-selected="{"true" if i == 0 else "false"}">{lbl}</button>')
    return f"""<header class="top"><div class="top__in">
 <a class="mark" href="#p-logbook" aria-label="BORN Studio">{SVG['wm_solo']}
  <span>Project room</span></a>
 <div class="nav" role="tablist" aria-label="Sections">{tabs}</div>
 <button class="printbtn" id="printBtn" type="button">&#8595;&nbsp; Print</button>
</div></header>"""

def ribbon():
    done, total = counts()
    live = next(p for p in PHASES if p["state"] == "stitched")
    nxt = next(e for e in ENTRIES if e["state"] == "next")
    ask = waiting()
    tail = (f'<span class="r"><span class="dot"></span>Sign-off due {date(ask["pay"]["when"])}</span>'
            if ask else
            f'<span class="s">Next &middot; {nxt["title"].rstrip(".")}, {date(nxt["date"])}</span>')
    return f"""<div class="rib"><div class="rib__in">
 <span><b>{PROJECT['client']}</b> <span class="s">&middot; {PROJECT['drop']}</span></span>
 <span class="s">{live['n']} &middot; {live['title']}</span>
 <span class="s">{done}/{total} signed off</span>
 {tail}
</div></div>"""

# ══════════════════════════════════════════════════════ the four documents ═
# Compiled views onto the same project. The logbook tells the story; these
# hold the detail, and each prints to A4 on its own.
def masthead(doctype, title, meta):
    rows = "".join(f"<div>{k} <b>{v}</b></div>" for k, v in meta)
    return f"""<div class="mast">
 <div class="mast__l"><p class="type">{doctype}</p><h1>{title}</h1>
  <p class="who">{PROJECT['client_long']} &middot; {PROJECT['capsule']} &middot; {PROJECT['drop']}</p></div>
 <div class="mast__r">{SVG['wm_solo']}<div class="meta">{rows}</div></div>
</div>"""

def sheetfoot(extra=""):
    return (f'<div class="dfoot"><span>{PROJECT["studio_long"]}</span>'
            f'<span>{extra or "Sketched. Stitched. BORN."}</span>'
            f'<span>{PROJECT["ref"]}</span></div>')

def dl(pairs):
    cells = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in pairs)
    return f'<dl class="dl">{cells}</dl>'

# ════════════════════════════════════════════════════════════════════ quote ═══
def quote():
    rows, fees = [], 0.0
    for gt, gs, items in QUOTE["groups"]:
        rows.append(f'<tr class="grp"><td colspan="2"><span class="gt">{gt}</span><br>'
                    f'<span class="c">{gs}</span></td></tr>')
        for text, qty, amt in items:
            a = f'{money(amt)}' if amt != "" else ""
            q = f'<br><span class="c">{qty}</span>' if qty else ""
            rows.append(f'<tr><td>{text}{q}</td><td class="n">{a}</td></tr>')
            if amt != "": fees += amt
    pt = sum(v for _, v in QUOTE["passthrough"])
    ptrows = "".join(f'<tr><td>{t}</td><td class="n">{money(v)}</td></tr>'
                     for t, v in QUOTE["passthrough"])
    pay = "".join(
        f'<div><div class="pc">{pc}</div><div class="wh">{wh}</div>'
        f'<div class="am">{money(a)}</div></div>' for wh, pc, a in QUOTE["schedule"])
    return f"""<section class="panel" id="p-quote" role="tabpanel" aria-labelledby="t-quote">
 <div class="docwrap"><div class="sheet">
  {masthead("Quote", "Development of a six-style capsule",
            [("No.", QUOTE["no"]), ("Issued", date(QUOTE["issued"])), ("Valid to", date(QUOTE["valid"]))])}
  {dl([("Client", PROJECT["client_long"]), ("Attention", f"{PROJECT['contact']}, {PROJECT['contact_role']}"),
       ("Scope", "6 styles &middot; 5 colour standards"), ("Size range", PROJECT["size_range"]),
       ("Currency", f"{PROJECT['currency']}, excl. VAT"), ("Terms", PROJECT["terms"])])}

  <div class="sec"><p class="eyebrow">Scope and fees</p>
   <div class="tw"><table class="t"><thead><tr><th>Deliverable</th><th class="n">Fee</th></tr></thead>
    <tbody>{''.join(rows)}
     <tr class="sum"><td class="em">Studio fees</td><td class="n em">{money(fees)}</td></tr>
    </tbody></table></div>
  </div>

  <div class="sec sec--rule"><p class="eyebrow">Pass-through, at cost &middot; estimate</p>
   <div class="tw"><table class="t"><tbody>{ptrows}
     <tr class="sum"><td class="em">Estimated pass-through</td><td class="n em">{money(pt)}</td></tr>
    </tbody></table></div>
   <p class="note" style="margin-top:.8rem">Billed at cost as it is incurred, with the supplier
    invoice attached. Nothing here carries a studio margin.</p>
  </div>

  <div class="sec sec--rule"><p class="eyebrow">Payment schedule</p>
   <div class="pay-g">{pay}</div>
  </div>

  <div class="sec sec--rule"><div class="two">
   <div><h2 class="h">What this assumes</h2>
    <ul class="li" style="margin-top:.9rem">{''.join(f'<li>{a}</li>' for a in QUOTE['assumptions'])}</ul></div>
   <div><h2 class="h">What it does not cover</h2>
    <ul class="li li--q" style="margin-top:.9rem">{''.join(f'<li>{e}</li>' for e in QUOTE['exclusions'])}</ul></div>
  </div></div>

  <div class="sec sec--rule"><p class="eyebrow">How this works</p>
   <p class="body">BORN takes an idea to a manufacturable product. It does not cut or sew, it does
    not buy your materials, and it does not take equity. What it sells is the judgment that sits
    between a drawing and a factory floor &mdash; and three filters every style has to pass before
    it goes anywhere near bulk: <b>can it be made</b>, <b>does it leave margin</b>, and
    <b>does it work on a body</b>.</p>
   <p class="body">Accept by returning a signed copy of this quote. The first invoice issues on
    signature and the briefing starts the same week.</p>
  </div>

  <div class="sign">
   <div><div class="ln"></div><div class="lb">Signed for {PROJECT['client']}</div></div>
   <div><div class="ln"></div><div class="lb">Date</div></div>
  </div>
  {sheetfoot(f"Quote {QUOTE['no']} &middot; valid to {date(QUOTE['valid'])}")}
 </div></div>
</section>"""

# ══════════════════════════════════════════════════════════════════ invoice ═══
def invoice():
    rows, sub = [], 0.0
    for t, d, q, unit in INVOICE["lines"]:
        amt = q * unit
        sub += amt
        qty = f"{q:,.1f}".rstrip("0").rstrip(".")
        rows.append(f'<tr><td class="em">{t}</td><td>{d}</td><td class="n">{qty}</td>'
                    f'<td class="n">{money(unit)}</td><td class="n">{money(amt)}</td></tr>')
    vat = round(sub * INVOICE["vat_rate"], 2)
    tot = sub + vat
    paid = "".join(f'<tr><td class="c">{date(d)}</td><td>{t}</td><td class="n">{money(v)}</td></tr>'
                   for d, t, v in INVOICE["paid"])
    return f"""<section class="panel" id="p-invoice" role="tabpanel" aria-labelledby="t-invoice">
 <div class="docwrap"><div class="sheet">
  {masthead("Invoice", INVOICE["milestone"],
            [("No.", INVOICE["no"]), ("Issued", date(INVOICE["issued"])), ("Due", date(INVOICE["due"]))])}
  {dl([("Bill to", PROJECT["client_long"]), ("Attention", PROJECT["contact"]),
       ("Against", f"Quote {INVOICE['ref']}"), ("Project", PROJECT["ref"]),
       ("Terms", PROJECT["terms"]), ("Currency", PROJECT["currency"])])}

  <div class="sec">
   <div class="tw"><table class="t"><thead><tr><th>Item</th><th>Detail</th><th class="n">Qty</th>
    <th class="n">Unit</th><th class="n">Amount</th></tr></thead><tbody>{''.join(rows)}
    <tr class="sum"><td colspan="4">Subtotal, excl. VAT</td><td class="n">{money(sub)}</td></tr>
    <tr><td colspan="4">VAT {int(INVOICE['vat_rate']*100)}%</td><td class="n">{money(vat)}</td></tr>
    <tr class="tot"><td colspan="4">Total</td><td class="n">{money(tot)}</td></tr>
   </tbody></table></div>
  </div>

  <div class="sec sec--rule"><div class="due">
    <div><p class="l">Amount due</p><p class="v">{money(tot)}</p></div>
    <p class="d">Payable by {date(INVOICE['due'])}<br>{PROJECT['terms']} from the issue date<br>
     Overdue balances accrue 1.5% per month</p>
  </div></div>

  <div class="sec sec--rule"><div class="two">
   <div><p class="eyebrow">Payment details</p>
    {dl([("Account name", PROJECT["studio"]), ("IBAN", PROJECT["iban"]),
         ("BIC / SWIFT", PROJECT["bic"]), ("VAT no.", PROJECT["vat"]),
         ("Reference", INVOICE["no"])])}</div>
   <div><p class="eyebrow">Already settled on this project</p>
    <div class="tw"><table class="t" style="min-width:0"><tbody>{paid}</tbody></table></div>
    <p class="note" style="margin-top:.8rem">Milestone 3 &mdash; 20% &mdash; issues at ex-factory,
     scheduled {date(PROJECT['exfactory'])}.</p></div>
  </div></div>

  <div class="sec sec--rule"><p class="eyebrow">What milestone 2 covered</p>
   <p class="body">Factory pairing and contract, lab dip management to chip across five standards
    and three qualities, two full sample rounds with documented fit sessions, and the tech pack
    revision that carried SMS 1's eleven corrections into v2.0. SMS 2 was delivered on
    {date('2026-08-28')} and fitted on {date('2026-09-04')}.</p>
   <p class="body">Quote your reference <b>{INVOICE['no']}</b> on the transfer so it reconciles
    against the right milestone.</p>
  </div>
  {sheetfoot(f"Invoice {INVOICE['no']} &middot; due {date(INVOICE['due'])}")}
 </div></div>
</section>"""

# ═══════════════════════════════════════════════════════════════ tech pack ═══
def techpack():
    chips = "".join(f'<button class="chip" data-s="{s["no"]}" aria-pressed="false">{s["no"]}</button>'
                    for s in STYLES)
    plates = []
    for s in STYLES:
        pom = "".join(
            f'<tr><td class="c">{c}</td><td>{p}</td>'
            + "".join(f'<td class="n">{v:.1f}</td>' for v in (xs, sm, md, lg, xl))
            + f'<td class="n">&plusmn;{tol:.1f}</td></tr>'
            for c, p, xs, sm, md, lg, xl, tol in s["pom"])
        bom = "".join(
            f'<tr><td class="em">{c}</td><td>{d}</td><td>{sup}</td><td class="c">{ref}</td>'
            f'<td class="c">{col}</td><td class="n">{cons}</td></tr>'
            for c, d, sup, ref, col, cons in s["bom"])
        det = "".join(f'<li>{d}</li>' for d in s["details"])
        build = "".join(f'<li>{b}</li>' for b in s["build"])
        plates.append(f"""<div class="styl" data-s="{s['no']}">
 <div class="two">
  <div class="plate"><img src="{IMG[s['img']]}" alt="{s['name']} — technical flat with callouts"></div>
  <div>
   <p class="eyebrow">{s['cat']} &middot; {s['no']}</p>
   <h2 class="h">{s['name']}</h2>
   <p class="body" style="margin-top:.7rem">{s['hand']}.</p>
   {dl([("Base quality", s["fabric"].split(" · ")[0]),
        ("Composition", s["fabric"].split(" · ")[1]),
        ("Weight", s["fabric"].split(" · ")[2]),
        ("Base size", PROJECT["base_size"]), ("Grading", PROJECT["size_range"])])}
   <p class="eyebrow" style="margin-top:1.4rem">Construction callouts</p>
   <ul class="li">{det}</ul>
  </div>
 </div>

 <div class="sec sec--rule"><p class="eyebrow">Bill of materials</p>
  <div class="tw"><table class="t"><thead><tr><th>Component</th><th>Description</th><th>Supplier</th>
   <th>Ref</th><th>Colour</th><th class="n">Cons.</th></tr></thead><tbody>{bom}</tbody></table></div>
 </div>

 <div class="sec sec--rule"><p class="eyebrow">Points of measure &middot; centimetres, base size {PROJECT['base_size']}</p>
  <div class="tw"><table class="t"><thead><tr><th>Code</th><th>Point of measure</th>
   {''.join(f'<th class="n">{z}</th>' for z in SIZES)}<th class="n">Tol.</th></tr></thead>
   <tbody>{pom}</tbody></table></div>
  <p class="note" style="margin-top:.8rem">Half measurements are marked &frac12; and taken flat,
   relaxed, on a conditioned sample. Measure after 24 hours of rest &mdash; a knit read straight
   off the press will lie to you.</p>
 </div>

 <div class="sec sec--rule"><p class="eyebrow">Construction and finishing</p>
  <ol class="num">{build}</ol>
 </div>
</div>""")
    return f"""<section class="panel" id="p-techpack" role="tabpanel" aria-labelledby="t-techpack">
 <div class="docwrap"><div class="sheet">
  {masthead("Tech pack", "Factory-ready specification",
            [("Revision", "v2.0"), ("Released", date("2026-08-14")), ("Styles", "6")])}
  {dl([("Client", PROJECT["client_long"]), ("Capsule", f"{PROJECT['capsule']} &middot; {PROJECT['drop']}"),
       ("Size range", PROJECT["size_range"]), ("Base size", PROJECT["base_size"]),
       ("Colour standards", "5 TCX"), ("Units", f"{PROJECT['units']:,}")])}

  <div class="sec"><p class="eyebrow">Revision history</p>
   <div class="tw"><table class="t"><thead><tr><th>Rev</th><th>Date</th><th>Change</th></tr></thead><tbody>
    <tr><td class="c">v1.0</td><td class="c">{date('2026-04-22')}</td><td>Initial release &mdash; 6 styles, factory-ready</td></tr>
    <tr><td class="c">v1.1</td><td class="c">{date('2026-05-22')}</td><td>Qualities confirmed against approved lab dips; KT-PLX210 replaced the 190 g/m² for the shorts</td></tr>
    <tr><td class="c">v2.0</td><td class="c">{date('2026-08-14')}</td><td>Post SMS 1 &mdash; 11 corrections across 6 styles</td></tr>
    <tr><td class="c">v2.1</td><td class="c">{date('2026-09-08')}</td><td>Post SMS 2 &mdash; 3 pattern corrections, 2 factory settings <span class="tag tag--r">in progress</span></td></tr>
   </tbody></table></div>
  </div>

  <div class="sec sec--rule"><p class="eyebrow">Select a style</p>
   <div class="chips" role="group" aria-label="Style">{chips}</div>
   {''.join(plates)}
  </div>

  <div class="sec sec--rule"><p class="eyebrow">Applies to every style</p>
   <ul class="li">
    <li>Sew to the graded POM, not to the flat sketch. Where the two disagree, the POM wins and BORN gets a call.</li>
    <li>All measurements in centimetres. Any measurement outside its tolerance on the size set stops the style until it is signed off in writing.</li>
    <li>Fabric relaxed 24 hours before cutting. Shrinkage tested at 3 washes &mdash; more than 3% and the quality is rejected.</li>
    <li>Colour approved against the physical TCX chip under D65. Screen values on any document are a reference, never an approval.</li>
    <li>Care and composition labelling to EU 1007/2011, in the languages listed on the artwork sheet.</li>
    <li>No substitution of any component in this BOM without written approval from BORN Studio.</li>
   </ul>
  </div>
  {sheetfoot("Tech pack v2.0 &middot; 6 styles")}
 </div></div>
</section>"""

# ═════════════════════════════════════════════════════════════════ fitting ═══
BADGE_OUT = '<span class="tag tag--r">Correct</span>'
BADGE_OK  = '<span class="tag">Pass</span>'

def fitting():
    # summary across the range, computed from the measured values against spec tolerance
    summary, detail = [], []
    for s in STYLES:
        tol = {c: t for c, _, _, _, _, _, _, t in s["pom"]}
        pomname = {c: p for c, p, *_ in s["pom"]}
        rows = FITTING["measured"][s["no"]]
        outs = [(c, sp, ms) for c, sp, ms in rows if abs(ms - sp) > tol[c] + 1e-9]
        plural = "s" if len(outs) > 1 else ""
        verdict = "Approve to size set" if not outs else f"Correct &mdash; {len(outs)} point{plural}"
        n_out = f'<span class="out">{len(outs)}</span>' if outs else "0"
        badge = BADGE_OUT if outs else BADGE_OK
        summary.append(
            f'<tr><td class="c">{s["no"]}</td><td class="em">{s["short"]}</td>'
            f'<td class="n">{len(rows)}</td><td class="n">{n_out}</td>'
            f'<td>{badge} <span class="c">{verdict}</span></td></tr>')
        def pom_row(c, sp, ms):
            over = abs(ms - sp) > tol[c] + 1e-9
            return (f'<tr><td class="c">{c}</td><td>{pomname[c]}</td><td class="n">{sp:.1f}</td>'
                    f'<td class="n">{ms:.2f}</td>'
                    f'<td class="n{" out" if over else ""}">{ms - sp:+.2f}</td>'
                    f'<td class="n">&plusmn;{tol[c]:.1f}</td>'
                    f'<td>{BADGE_OUT if over else BADGE_OK}</td></tr>')
        body = "".join(pom_row(c, sp, ms) for c, sp, ms in rows)
        photos = ""
        if s["photo"]:
            cards = "".join(
                f'<figure><img src="{IMG[k]}" alt="{s["no"]} sample">'
                f'<figcaption>{"front" if k.endswith("_f") else "back"}</figcaption></figure>'
                for k in s["photo"])
            photos = f'<div class="strip" style="margin-top:1rem;max-width:340px">{cards}</div>' 
        detail.append(f"""<div class="styl" data-s="{s['no']}">
 <p class="eyebrow">{s['no']} &middot; {s['cat']}</p><h2 class="h">{s['short']}</h2>
 {photos}
 <div class="tw" style="margin-top:1.1rem"><table class="t"><thead><tr><th>Code</th>
  <th>Point of measure</th><th class="n">Spec</th><th class="n">Measured</th>
  <th class="n">Dev.</th><th class="n">Tol.</th><th>Verdict</th></tr></thead>
  <tbody>{body}</tbody></table></div>
</div>""")
    chips = "".join(f'<button class="chip" data-s="{s["no"]}" aria-pressed="false">{s["no"]}</button>'
                    for s in STYLES)
    corr = "".join(
        f'<li><b>{BY_NO[sn]["short"]} &middot; {sn}{"" if pt == "—" else " &middot; " + pt}</b><br>{txt}'
        f'<br><span class="c" style="color:var(--red)">{owner}</span></li>'
        for sn, pt, txt, owner in FITTING["corrections"])
    holds = "".join(f'<li>{h}</li>' for h in FITTING["holds"])
    return f"""<section class="panel" id="p-fitting" role="tabpanel" aria-labelledby="t-fitting">
 <div class="docwrap"><div class="sheet">
  {masthead("Fitting report", f"{FITTING['sample']} &middot; fit session 02",
            [("No.", FITTING["no"]), ("Session", date(FITTING["session"])), ("Size", FITTING["size"])])}
  {dl([("Sample round", FITTING["sample"]), ("Received", date(FITTING["received"])),
       ("Measured against", FITTING["spec"]), ("Form", FITTING["form"]),
       ("Present", FITTING["present"]), ("Styles fitted", "6")])}

  <div class="sec"><p class="eyebrow">Verdict</p>
   <div class="due"><div><p class="l">Outcome</p><p class="v" style="font-size:clamp(1.4rem,3vw,2rem)">{FITTING['verdict']}</p></div>
    <p class="d" style="max-width:34ch;text-align:left">{FITTING['verdict_note']}</p></div>
  </div>

  <div class="sec sec--rule"><p class="eyebrow">Across the range</p>
   <div class="tw"><table class="t"><thead><tr><th>Style no.</th><th>Style</th>
    <th class="n">Points</th><th class="n">Out of tol.</th><th>Verdict</th></tr></thead>
    <tbody>{''.join(summary)}</tbody></table></div>
  </div>

  <div class="sec sec--rule"><p class="eyebrow">Measured &middot; select a style</p>
   <div class="chips" role="group" aria-label="Style">{chips}</div>
   {''.join(detail)}
  </div>

  <div class="sec sec--rule"><p class="eyebrow">Corrections into v2.1</p>
   <ol class="num">{corr}</ol>
   <p class="note" style="margin-top:1rem">Three of these are pattern changes and go into the tech
    pack. Two are factory settings &mdash; a bonding jig and a binder foot &mdash; and cost a
    re-press, not a re-cut.</p>
  </div>

  <div class="sec sec--rule"><p class="eyebrow">Holds &mdash; do not change these</p>
   <ul class="li li--q">{holds}</ul>
  </div>

  <div class="sign">
   <div><div class="nm">{PROJECT['studio_person']}</div><div class="rl">{PROJECT['studio']}</div>
    <div class="ln"></div><div class="lb">Signature and date</div></div>
   <div><div class="nm">{PROJECT['contact']}</div><div class="rl">{PROJECT['client']}</div>
    <div class="ln"></div><div class="lb">Signature and date</div></div>
  </div>
  {sheetfoot(f"Fitting report {FITTING['no']} &middot; {date(FITTING['session'])}")}
 </div></div>
</section>"""

# ════════════════════════════════════════════════════════════════ handover ═══
def handover():
    plan = "".join(f"<dt>{k}</dt><dd>{v}</dd>" for k, v in HANDOVER["plan"])
    arch = "".join(
        f'<div><h3 class="sh">{g}</h3><ul class="li">{"".join(f"<li>{i}</li>" for i in items)}</ul></div>'
        for g, items in HANDOVER["archive"])
    nxt = "".join(f"<li>{n}</li>" for n in HANDOVER["next"])
    sign = "".join(
        f'<div><div class="nm">{who}</div><div class="rl">{org} &middot; {role}</div>'
        f'<div class="ln"></div><div class="lb">Signature and date</div></div>'
        for org, who, role in HANDOVER["signoff"])
    renders = "".join(
        f'<figure><img src="{IMG[k]}" alt="{cap}"><figcaption>{cap}</figcaption></figure>'
        for k, cap in [("render_periwinkle", "17-3919 Purple Impression"),
                       ("render_whisper", "11-0701 Whisper White"),
                       ("render_black", "19-3911 Black Beauty"),
                       ("render_blue", "17-3919 · jacket and short")])
    return f"""<section class="panel" id="p-handover" role="tabpanel" aria-labelledby="t-handover">
 <div class="docwrap"><div class="sheet">
  {masthead("Handover", "What LAYO owns at the end",
            [("No.", HANDOVER["no"]), ("Issues", date(HANDOVER["due"])), ("Status", HANDOVER["status"])])}

  <div class="sec"><p class="body">This is the document that closes the project. It issues at
   ex-factory with the production figures filled in, and it lists everything that transfers to
   LAYO &mdash; patterns, specifications, supplier references, colour approvals and the full
   development record. <b>Nothing is held back.</b> If LAYO takes the next drop elsewhere, it
   leaves with a complete, executable file.</p>
   <p class="note" style="margin-top:1rem">Figures below are the contracted plan. Achieved units,
    the AQL result, landed cost and the shipping record are entered at ex-factory, scheduled
    {date(HANDOVER['due'])}.</p>
  </div>

  <div class="sec sec--rule"><p class="eyebrow">The programme</p>
   <dl class="dl">{plan}</dl>
  </div>

  <div class="sec sec--rule"><p class="eyebrow">Production record &middot; completed at ex-factory</p>
   <div class="tw"><table class="t"><thead><tr><th>Line</th><th>Planned</th><th>Achieved</th></tr></thead><tbody>
    <tr><td class="em">Units shipped</td><td class="c">1,800</td><td class="c">&mdash;</td></tr>
    <tr><td class="em">Final inspection</td><td class="c">AQL 2.5 / 4.0</td><td class="c">&mdash;</td></tr>
    <tr><td class="em">Ex-factory date</td><td class="c">{date(HANDOVER['due'])}</td><td class="c">&mdash;</td></tr>
    <tr><td class="em">Programme length</td><td class="c">43 weeks</td><td class="c">&mdash;</td></tr>
    <tr><td class="em">Cartons / gross weight</td><td class="c">&mdash;</td><td class="c">&mdash;</td></tr>
   </tbody></table></div>
  </div>

  <div class="sec sec--rule"><p class="eyebrow">The archive &middot; delivered on handover</p>
   <div class="two--even" style="display:grid;gap:1.6rem 2.4rem">{arch}</div>
  </div>

  <div class="sec sec--rule"><p class="eyebrow">Approved colourway sets</p>
   <div class="strip">{renders}</div>
   <p class="note" style="margin-top:.9rem">Visualised at the design stage, 3 Apr 2026, and carried
    through to the approved lab dips.</p>
  </div>

  <div class="sec sec--rule"><p class="eyebrow">For the next drop</p>
   <ul class="li">{nxt}</ul>
  </div>

  <div class="sec sec--rule"><p class="eyebrow">Sign-off</p>
   <p class="body">Signing below confirms the archive above was received in full and the programme
    is closed. It does not waive any latent defect claim against the factory.</p>
   <div class="sign">{sign}</div>
  </div>
  {sheetfoot(f"Handover {HANDOVER['no']}")}
 </div></div>
</section>"""


# ═══════════════════════════════════════════════════════════ the system view ═
KINDS = [
 ("Note", "Something happened that the client should know about. No payload — just the "
          "sentence and the date. Use it when there is nothing to show."),
 ("Decision", "A fork with a reason. Shows what was chosen against what was considered, "
              "why, and what the choice cost or saved. Never a decision without its price."),
 ("Materials", "A shortlist with verdicts. Carried qualities read in ink, dropped ones "
               "struck through, so the reasoning survives after the choice is made."),
 ("Colour", "The approved standards as chips, with their TCX codes. Always says that "
            "screen values are a reference and the physical chip is the approval."),
 ("Release", "A document left the studio. Carries its name, revision and a way straight "
             "into it. If a release has no document behind it, it is a note, not a release."),
 ("Sample", "A physical thing arrived. Photographed on the form before anything is "
            "touched, with the round and the verdict."),
 ("Measure", "A fit session. Shows only the points that fell outside tolerance, with the "
             "deviation and whether the cause is the pattern or the factory. The full "
             "graded POM stays in the tech pack, one click away."),
 ("Approval", "A gate. Either given, with who and when, or waiting — in which case it is "
              "red, says what it needs and by when, and is repeated at the top of the page."),
 ("Watch", "A risk that is not a problem yet. Always paired with the action that removes "
           "it and who holds it. A risk written without its fix is just worry."),
]

SNIPPET = """<span class="cm"># tools/room_data.py — add an entry and rebuild. That is the whole workflow.</span>

dict(date=<span class="st">"2026-09-18"</span>, phase=<span class="st">"stitched"</span>, state=<span class="st">"next"</span>, kind=<span class="st">"Sample"</span>,
  title=<span class="st">"Size set, XS to XL, all six styles."</span>,
  body=<span class="st">"The first time the grade is tested rather than calculated."</span>,
  pay=dict(type=<span class="st">"sample"</span>, round=<span class="st">"Size set"</span>, ok=<span class="ky">True</span>,
           keys=[(<span class="st">"photo_jacket_f"</span>, <span class="st">"LY-JK-149 · front"</span>)],
           verdict=<span class="st">"Approved"</span>)),

<span class="cm"># phase  sets the register — the world it is drawn in</span>
<span class="cm"># state  sets the marker  — done · now · next</span>
<span class="cm"># kind   is the label the client reads</span>
<span class="cm"># pay    is optional. No payload is a perfectly good entry.</span>

$ python3 tools/build_room.py"""

def system():
    regs = ""
    for k in ["sketched", "stitched", "born"]:
        r = REGISTERS[k]
        logo = {"sketched": SVG["state_sketch"], "stitched": SVG["state_stitch"],
                "born": SVG["state_born"]}[k]
        regs += f"""<article><div class="sw sw--{k}">{logo}</div>
 <div class="sb"><h3>{r['name']}</h3><p class="ln">{r['line']}</p><p>{r['defn']}</p></div></article>"""
    kinds = "".join(f'<div><p class="kn">{n}</p><p class="kd">{d}</p></div>' for n, d in KINDS)
    states = "".join(
        f'<div><p class="kn">{mk(s)} &nbsp;{lbl}</p><p class="kd">{d}</p></div>'
        for s, lbl, d in [
          ("next", "Not yet", "Pencil outline. It is scheduled, nothing has happened."),
          ("now", "Live", "Stitch dashes. It is happening this week and may still move."),
          ("done", "Signed off", "Solid, with the red dot. It happened and it is recorded.")])
    return f"""<section class="panel" id="p-system" role="tabpanel" aria-labelledby="t-system">
 <div class="docwrap"><div class="sheet">
  {masthead("The system", "How a room is built",
            [("For", "BORN Studio"), ("Version", "1.0"), ("Applies to", "Every project")])}

  <div class="sec"><p class="body">A room is not designed per client. It is assembled from
   the pieces below, so two projects delivered a year apart read as the same studio and a
   client who has seen one can read the next without being taught it again.</p>
  </div>

  <div class="sec sec--rule"><p class="eyebrow">The rule everything rests on</p>
   <h2 class="h">Two channels. Never mixed.</h2>
   <div class="two--even" style="display:grid;gap:1.4rem 2.4rem;margin-top:1.2rem">
    <div><h3 class="sh">Register &mdash; where in the craft</h3>
     <p class="body">The ground, the texture and the rule say which phase a piece of
      information belongs to. Sketched has a construction grid behind it and dotted
      hairlines. Stitched has a diagonal hatch and dashes cut like a topstitch. BORN is
      clean paper, a solid rule and the red dot. <b>The register never says whether
      something is finished.</b></p></div>
    <div><h3 class="sh">State &mdash; whether it happened</h3>
     <p class="body">One small marker, and nothing else. Outline for what has not started,
      stitch for what is live, solid with the red dot for what is signed off. <b>The marker
      never says which phase you are in.</b> Keeping these apart is what lets a reader
      answer both questions in one glance without a legend.</p></div>
   </div>
  </div>

  <div class="sec sec--rule"><p class="eyebrow">The three registers</p>
   <div class="spec">{regs}</div>
  </div>

  <div class="sec sec--rule"><p class="eyebrow">The three states</p>
   <div class="kinds">{states}</div>
  </div>

  <div class="sec sec--rule"><p class="eyebrow">The nine entry kinds</p>
   <p class="body">Anatomy is identical on every entry &mdash; date, kind, headline, body
    &mdash; so the page stays scannable. Only the payload changes, so density follows the
    content instead of the template.</p>
   <div class="kinds">{kinds}</div>
  </div>

  <div class="sec sec--rule"><p class="eyebrow">Rules that keep it honest</p>
   <ol class="num">
    <li><b>Red is scarce.</b> It marks three things only: what is live, what is waiting on
     the client, and what is out of tolerance. If red appears anywhere else it stops working.</li>
    <li><b>Never a decision without its price.</b> Every decision entry carries what the
     choice cost or saved, in money or in weeks. That is the studio's judgment made visible.</li>
    <li><b>Never a risk without its fix.</b> A watch entry that only names a problem is
     worry. Name the action that removes it and who holds it.</li>
    <li><b>Show what moved, not everything.</b> A fit session lists the points outside
     tolerance and links to the full graded POM. Precision lives in the tech pack; the
     logbook carries the judgment.</li>
    <li><b>One ask at a time.</b> At most one approval is waiting. It sits at the top of
     the page, in the ribbon and in the logbook, with a date. Two open asks means neither
     gets answered.</li>
    <li><b>Screens never approve colour.</b> Any colour on any screen is labelled a
     reference. The physical TCX chip under D65 is the approval.</li>
   </ol>
  </div>

  <div class="sec sec--rule"><p class="eyebrow">Adding to a room</p>
   <p class="body">All project content lives in one file. Nothing in it knows how anything
    looks, so writing an entry is writing a sentence and a date &mdash; the register, the
    marker, the spine and the print layout resolve themselves.</p>
   <pre class="code">{SNIPPET}</pre>
   <p class="note" style="margin-top:1rem">Opening a room for a new client: copy
    <code>tools/room_data.py</code>, replace PROJECT, STYLES and ENTRIES, run the build.
    Fonts and images are embedded, so the result is one file that works offline, over
    email, or on any static host.</p>
  </div>
  {sheetfoot("The system &middot; v1.0")}
 </div></div>
</section>"""

# ══════════════════════════════════════════════════════════════════════ JS ═══
JS = r"""<script>
(function(){
  var tabs=[].slice.call(document.querySelectorAll('.nav [data-doc]'));
  function show(key,keepScroll){
    var found=false;
    tabs.forEach(function(t){
      var on=t.dataset.doc===key; if(on)found=true;
      t.setAttribute('aria-selected',on?'true':'false');
      var p=document.getElementById('p-'+t.dataset.doc);
      if(p)p.classList.toggle('active',on);
    });
    if(!found)return;
    history.replaceState(null,'','#'+key);
    if(!keepScroll)window.scrollTo(0,0);
  }
  tabs.forEach(function(t){t.addEventListener('click',function(){show(t.dataset.doc);});});
  tabs.forEach(function(t,i){t.addEventListener('keydown',function(e){
    var d=e.key==='ArrowRight'?1:e.key==='ArrowLeft'?-1:0;
    if(!d)return;e.preventDefault();
    var n=tabs[(i+d+tabs.length)%tabs.length];n.focus();show(n.dataset.doc);
  });});
  if(location.hash)show(location.hash.slice(1),true);

  // logbook entries link into the document they produced
  document.querySelectorAll('[data-go]').forEach(function(b){
    b.addEventListener('click',function(){show(b.dataset.go);});
  });

  // per-panel style pickers
  document.querySelectorAll('.panel').forEach(function(panel){
    var chips=[].slice.call(panel.querySelectorAll('.chip[data-s]')),
        plates=[].slice.call(panel.querySelectorAll('.styl[data-s]'));
    if(!chips.length)return;
    function pick(no){
      chips.forEach(function(c){c.setAttribute('aria-pressed',c.dataset.s===no?'true':'false');});
      plates.forEach(function(p){p.classList.toggle('on',p.dataset.s===no);});
    }
    chips.forEach(function(c){c.addEventListener('click',function(){pick(c.dataset.s);});});
    pick(chips[0].dataset.s);
  });

  document.getElementById('printBtn').addEventListener('click',function(){window.print();});
})();
</script>"""

# ══════════════════════════════════════════════════════════════════ output ═══
LOGBOOK = ('<section class="panel active" id="p-logbook" role="tabpanel" '
           'aria-labelledby="t-logbook">' + standfirst() + logbook() + '</section>')

BODY = (DEFS + top() + ribbon() + '<main>' + LOGBOOK + techpack() + fitting()
        + quote() + invoice() + handover() + system() + '</main>' + JS)
HEAD = "<style>\n" + FONTS + "\n" + CSS + "\n</style>"

artifact = "<title>BORN Project Room</title>\n" + HEAD + "\n" + BODY
open(f"{W}/room_artifact.html", "w", encoding="utf-8").write(artifact)

page = ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
  '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
  f'<title>BORN Project Room &mdash; {PROJECT["client"]}</title>\n'
  '<meta name="description" content="BORN Studio project room — the development logbook, '
  'tech pack, fitting report, quote, invoice and handover.">\n'
  '<meta name="theme-color" content="#F2EEE6">\n'
  f'<link rel="icon" href="{FAVICON}">\n' + HEAD + "\n</head>\n<body>\n" + BODY + "\n</body>\n</html>\n")
open(f"{O}/index.html", "w", encoding="utf-8").write(page)
print(f"deliverables/index.html: {len(page)//1024} KB   artifact: {len(artifact)//1024} KB")
