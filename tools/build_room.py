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
         ["wm_solo", "wm_solo_neg", "wm_solo_onred",
          "state_sketch", "state_stitch", "state_born"]}
import re as _re
from PIL import Image as _PIL
_ASSETS = [f for f in sorted(os.listdir(f"{O}/assets")) if f.endswith(".jpg")]
IMG   = {f[:-4]: datauri(f"{O}/assets/{f}", "image/jpeg") for f in _ASSETS}
RATIO = {f[:-4]: round(_PIL.open(f"{O}/assets/{f}").size[0] /
                       _PIL.open(f"{O}/assets/{f}").size[1], 4) for f in _ASSETS}
# Each picture is a single rule in the stylesheet and every use points at it,
# so an image that appears in six places is still downloaded once.
IMGCSS = "\n".join(f'.i-{k}{{background-image:url("{v}")}}' for k, v in IMG.items())

def im(key, alt, cls=""):
    """Place an image by reference. Ratio is baked in so nothing reflows."""
    c = f" {cls}" if cls else ""
    return (f'<span class="im i-{key}{c}" style="--r:{RATIO[key]}" '
            f'role="img" aria-label="{alt}"></span>')

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
    return d, f'{MONTHS[int(m)-1]} <span class="yr">{y}</span>' 

GRAIN = ('<svg class="grain" viewBox="0 0 74 9" aria-hidden="true">'
  '<path d="M1 1v7M73 1v7M1 4.5h72M6 1.5 1.5 4.5 6 7.5M68 1.5 72.5 4.5 68 7.5"/></svg>')

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
# Structure comes from space, alignment and scale. Rules are hairline and only
# appear where a division is real; borders are reserved for two things — the
# client's open action, and a sheet that will be printed. Drawings and renders
# sit on the paper with multiply blending, so they have no frame at all; only
# photographs are framed, because only they are of an object that exists.
CSS = ROOT + r"""
:root{
  --sheet:#FBF8F2; --hair:rgba(27,23,32,.15); --hair-2:rgba(27,23,32,.32);
  --graphite:#5C5762;
  --topH:52px;
  --gap:clamp(1.4rem,3.2vw,3rem);
  --pad:clamp(1.25rem,5vw,4.5rem);
  --max:1320px;
}
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth;scroll-padding-top:calc(var(--topH) + 1.5rem)}
body{background:var(--paper);color:var(--ink);font-family:var(--sans);
  font-size:16px;line-height:1.68;-webkit-font-smoothing:antialiased;overflow-x:clip}
img,svg{display:block;max-width:100%}
a{color:inherit;text-decoration:none}
::selection{background:var(--red);color:var(--paper)}
:focus-visible{outline:2px solid var(--red);outline-offset:4px}
.w{max-width:var(--max);margin:0 auto;padding:0 var(--pad)}

/* ── type scale ───────────────────────────────────────────────────────────── */
.d1{font-family:var(--serif);font-weight:900;letter-spacing:-.035em;line-height:.86;
  font-size:clamp(3.6rem,12vw,9.5rem)}
.d2{font-family:var(--serif);font-weight:900;letter-spacing:-.028em;line-height:.92;
  font-size:clamp(2.1rem,5.2vw,4rem)}
.d3{font-family:var(--serif);font-weight:900;letter-spacing:-.018em;line-height:1.02;
  font-size:clamp(1.5rem,3vw,2.3rem)}
.sub{font-family:var(--serif6);font-weight:600;line-height:1.34;
  font-size:clamp(1.1rem,1.85vw,1.42rem);color:var(--g2)}
.p{max-width:62ch;color:var(--g2)}
.p b,.p strong{color:var(--ink);font-weight:500}
.p + .p{margin-top:.85rem}
.m{font-family:var(--mono);font-size:.66rem;letter-spacing:.16em;text-transform:uppercase;
  color:var(--g3)}
.m--r{color:var(--red)}
.m--ink{color:var(--ink)}
.tnum{font-variant-numeric:tabular-nums}
.rule{border:0;border-top:1px solid var(--hair)}
.rule--ink{border-top:1px solid var(--ink)}

/* ── chrome ───────────────────────────────────────────────────────────────── */

.top{position:sticky;top:0;z-index:70;background:rgba(242,238,230,.93);
  backdrop-filter:blur(16px);border-bottom:1px solid var(--hair)}
.top__in{max-width:var(--max);margin:0 auto;padding:0 var(--pad);min-height:var(--topH);
  display:flex;align-items:center;gap:1.6rem;flex-wrap:wrap}
.top .mk-w{flex:0 0 auto;margin:.6rem 0}
.nav{display:flex;gap:1.15rem;margin-left:auto;flex-wrap:wrap;align-items:center}
.nav button{font-family:var(--mono);font-size:.63rem;letter-spacing:.15em;text-transform:uppercase;
  color:var(--g3);background:none;border:0;cursor:pointer;padding:.5rem 0;white-space:nowrap;
  border-bottom:2px solid transparent;transition:color .2s,border-color .2s}
.nav button:hover{color:var(--ink)}
.nav button[aria-selected=true]{color:var(--ink);border-bottom-color:var(--red)}
.nav .pr{color:var(--g3);border-bottom:0}
.nav .pr:hover{color:var(--red)}

.panel{display:none}
.panel.active{display:block}

/* ── images: drawings float on the paper, photographs are framed ─────────── */
/* the blending group is closed at <main>, so a multiplied drawing composites
   against the paper and never over the sticky header */
main{isolation:isolate;background:var(--paper);position:relative;z-index:1}
.im{display:block;width:100%;aspect-ratio:var(--r,1);background-repeat:no-repeat;
  background-position:center;background-size:contain;
  -webkit-print-color-adjust:exact;print-color-adjust:exact}
.float{mix-blend-mode:multiply}
.ph{background:#fff}
figure{margin:0}
figcaption{font-family:var(--mono);font-size:.6rem;letter-spacing:.13em;text-transform:uppercase;
  color:var(--g3);margin-top:.6rem}

/* ── cover ────────────────────────────────────────────────────────────────── */
.cover{overflow:hidden;isolation:isolate}
.cover__in{display:grid;grid-template-columns:minmax(0,1.05fr) minmax(0,1fr);
  align-items:stretch;min-height:min(92vh,820px)}
@media(max-width:900px){.cover__in{grid-template-columns:1fr;min-height:0}}
.cover__t{display:flex;flex-direction:column;justify-content:center;
  padding:clamp(2.6rem,6vw,5rem) clamp(1.25rem,5vw,4.5rem);
  max-width:calc(var(--max)/2 + 3rem);margin-left:auto;width:100%}
.cover__r{background:var(--paper);display:flex;align-items:center;justify-content:center;
  padding:clamp(1.4rem,3.5vw,3rem)}
.cover__r .im{mix-blend-mode:multiply}
.cover h1{margin:.6rem 0 0;font-size:clamp(4.2rem,11vw,10rem)}
.cover .cap{font-family:var(--serif6);font-weight:600;font-size:clamp(1.3rem,2.7vw,2.1rem);
  line-height:1.14;letter-spacing:-.01em;margin-top:.35rem;max-width:16ch}
.cover .lede{margin-top:1.5rem;max-width:44ch;font-size:1.06rem}
.cover__meta{display:grid;grid-template-columns:repeat(auto-fit,minmax(118px,1fr));
  gap:1rem 1.6rem;margin-top:clamp(1.8rem,4vw,2.8rem);padding-top:1.1rem;
  border-top:1px solid var(--ink)}
.cover__meta dt{font-family:var(--mono);font-size:.58rem;letter-spacing:.16em;
  text-transform:uppercase;color:var(--g3)}
.cover__meta dd{font-family:var(--mono);font-size:.82rem;margin-top:.2rem;
  font-variant-numeric:tabular-nums}
.cover__r .im{width:100%;max-height:74vh}
/* the mark matures once, on load — sketched, stitched, born */
.matur{position:relative;display:block;width:90px;height:19px}
.matur > span{position:absolute;inset:0;opacity:0}
.matur > span svg{width:100%;height:100%}
.matur > span.on{opacity:1}
@media(prefers-reduced-motion:no-preference){.matur > span{transition:opacity .45s var(--ease)}}
@media(prefers-reduced-motion:reduce){.matur > span:last-child{opacity:1}}

/* ── the three phases, each drawn in its own register ────────────────────── */
.proc{padding-block:clamp(2.4rem,6vw,4.6rem) clamp(1.6rem,3vw,2.4rem);border-top:1px solid var(--ink)}
.proc__h{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:var(--gap);
  align-items:end;padding-bottom:clamp(1.8rem,4vw,3rem)}
@media(max-width:860px){.proc__h{grid-template-columns:1fr;gap:1.4rem}}
.proc__g{display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(1.2rem,3vw,2.6rem)}
@media(max-width:860px){.proc__g{grid-template-columns:1fr;gap:2rem}}
.ph3{border-top:1px solid var(--ink);padding-top:1.1rem;display:flex;flex-direction:column}
.ph3__tex{padding:1.4rem 1.2rem;margin-bottom:1.2rem;display:flex;align-items:center;
  min-height:104px}
.ph3--sketched .ph3__tex{background-image:linear-gradient(rgba(74,69,79,.10) 1px,transparent 1px),
  linear-gradient(90deg,rgba(74,69,79,.10) 1px,transparent 1px);background-size:22px 22px}
.ph3--stitched .ph3__tex{background-image:repeating-linear-gradient(45deg,rgba(27,23,32,.075) 0 1px,transparent 1px 10px)}
.ph3--born .ph3__tex{background:var(--ink)}
.ph3__lg{width:100%;max-width:200px}
.ph3__lg svg{width:100%;height:auto}
.ph3--born .p-ink{fill:var(--paper)}
.ph3 .n{font-family:var(--mono);font-size:.6rem;letter-spacing:.17em;text-transform:uppercase;
  color:var(--g3)}
.ph3.is-now .n{color:var(--red)}
.ph3 .ln{font-family:var(--serif6);font-weight:600;font-size:1.02rem;color:var(--g2);
  margin:.25rem 0 .7rem}
.ph3 .p{font-size:.92rem}
.ph3__f{display:flex;align-items:center;gap:.6rem;margin-top:auto;padding-top:.9rem;
  border-top:1px solid var(--hair);font-family:var(--mono);font-size:.6rem;letter-spacing:.12em;
  text-transform:uppercase;color:var(--g3)}
.ph3.is-now .ph3__f{color:var(--red)}
.ph3__f .wk{margin-left:auto;color:var(--g3)}

/* ── the phase rail: where the view you are looking at came from ─────────── */
.rail{display:flex;align-items:center;gap:.6rem;margin-top:1.1rem;padding-top:.9rem;
  border-top:1px solid var(--hair)}
.rail__n{display:flex;align-items:center;gap:.45rem;flex:0 0 auto}
.rail__n .mk{color:var(--g4)}
.rail__l{font-family:var(--mono);font-size:.57rem;letter-spacing:.16em;text-transform:uppercase;
  color:var(--g4)}
.rail__r{flex:1 1 auto;height:1px;background:var(--g4);opacity:.5}
.rail__n.is-on .mk{color:var(--red)}
.rail__n.is-on .rail__l{color:var(--ink)}
.rail__n.is-past .mk{color:var(--ink)}
.rail__n.is-past .rail__l{color:var(--g2)}
.gal__hint{font-family:var(--mono);font-size:.57rem;letter-spacing:.14em;text-transform:uppercase;
  color:var(--g4);margin-top:.85rem;text-align:center;transition:color .2s}
.gal:hover .gal__hint{color:var(--g2)}

/* ── contents ─────────────────────────────────────────────────────────────── */
.toc{padding-block:clamp(2rem,5vw,3.4rem)}
.toc__h{display:flex;justify-content:space-between;align-items:baseline;gap:1rem;
  padding-bottom:.9rem;border-bottom:1px solid var(--ink);flex-wrap:wrap}
.toc a{display:grid;grid-template-columns:3.2rem minmax(0,1fr) minmax(0,13ch) 8rem;
  gap:1.4rem;align-items:center;padding:1.05rem 0;border-bottom:1px solid var(--hair);
  transition:background .2s}
@media(max-width:760px){.toc a{grid-template-columns:2.4rem minmax(0,1fr) 5rem;gap:.9rem}
  .toc a .cat{display:none}}
.toc a:hover{background:rgba(27,23,32,.028)}
.toc .ix{font-family:var(--serif);font-weight:900;font-size:1.6rem;line-height:1;color:var(--g4);
  transition:color .2s}
.toc a:hover .ix{color:var(--red)}
.toc .nm{font-family:var(--serif6);font-weight:600;font-size:clamp(1.05rem,1.9vw,1.32rem);
  line-height:1.2}
.toc .no{font-family:var(--mono);font-size:.7rem;letter-spacing:.1em;color:var(--g3);
  display:block;margin-top:.18rem}
.toc .cat{font-family:var(--mono);font-size:.63rem;letter-spacing:.13em;text-transform:uppercase;
  color:var(--g3)}
.toc .th{height:72px;display:flex;align-items:center;justify-content:flex-end}
.toc .th .im{height:72px;width:118px;aspect-ratio:auto;background-position:right center}

/* ── style spread ─────────────────────────────────────────────────────────── */
.sp{padding-block:0 clamp(2.4rem,6vw,4.5rem)}
.sp__h{display:grid;grid-template-columns:clamp(4.6rem,7.6vw,7.4rem) minmax(0,1fr) minmax(0,.56fr);
  gap:clamp(1rem,2.4vw,2.4rem) clamp(1.2rem,3vw,3rem);align-items:start;padding-top:1.6rem}
@media(max-width:900px){.sp__h{grid-template-columns:1fr;gap:.9rem}}
.sp__nm{min-width:0}
.sp__code{font-family:var(--mono);font-size:.86rem;letter-spacing:.06em;color:var(--g2);
  margin-top:.9rem;padding-top:.55rem;
  background:repeating-linear-gradient(90deg,rgba(27,23,32,.3) 0 1px,transparent 1px 11px)
    top left/100% 4px no-repeat}
.sp__ix{font-family:var(--serif);font-weight:900;line-height:.74;letter-spacing:-.055em;
  font-size:clamp(2.8rem,5vw,5.2rem);color:var(--ink);margin-left:-.05em}
.sp__ix em{font-style:normal;color:var(--red)}
.sp h2{margin-top:.1rem;max-width:17ch;letter-spacing:-.032em;line-height:.94}
.sp__meta{display:grid;gap:.75rem;padding-bottom:.4rem}
.sp__meta div{display:grid;grid-template-columns:8.5rem minmax(0,1fr);gap:.8rem;
  padding-bottom:.7rem;border-bottom:1px solid var(--hair)}
.sp__meta dt{font-family:var(--mono);font-size:.6rem;letter-spacing:.14em;text-transform:uppercase;
  color:var(--g3)}
.sp__meta dd{font-size:.93rem;color:var(--ink)}
.sp__body{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:var(--gap);
  padding-top:clamp(2rem,4.5vw,3.4rem);align-items:start}
.sp--flip .sp__body > div:first-child{order:2}
@media(max-width:900px){.sp--flip .sp__body > div:first-child{order:0}}
@media(max-width:900px){.sp__body{grid-template-columns:1fr}}
.calls{list-style:none;display:grid;gap:0;margin-top:1rem}
.calls li{padding:.62rem 0;border-bottom:1px solid var(--hair);display:flex;gap:.9rem;
  align-items:baseline;font-size:.94rem;color:var(--g2)}
.calls li span{font-family:var(--mono);font-size:.62rem;color:var(--g4);
  font-variant-numeric:tabular-nums;flex:0 0 1.6rem}
.sp__flat{max-width:min(100%,1040px);margin:clamp(2rem,4vw,3.2rem) auto 0}
.sp__flat .im{width:100%}
.sp__flat figcaption{text-align:center;margin-top:.9rem}
.cwl{list-style:none;display:grid;gap:0;margin-top:1rem}
.cwl li{display:flex;align-items:center;gap:.85rem;padding:.6rem 0;
  border-bottom:1px solid var(--hair)}
.cwl i{width:20px;height:20px;flex:0 0 auto;box-shadow:inset 0 0 0 1px rgba(27,23,32,.14)}
.cwl .nm{font-family:var(--serif6);font-weight:600;font-size:.96rem;flex:1 1 auto}
.cwl .cd{font-family:var(--mono);font-size:.62rem;letter-spacing:.06em;color:var(--g3)}

/* ── gallery: drawn · coloured · visualised · born ───────────────────────── */
/* the stage takes the shape of the view in it, so a wide technical flat and a
   tall legging are each shown whole, with no letterboxing either way */
.gal__stage{display:grid;aspect-ratio:var(--sr,.78);cursor:zoom-in;
  transition:aspect-ratio .42s var(--ease)}
@media(prefers-reduced-motion:reduce){.gal__stage{transition:none}}
.gal__stage > figure{grid-area:1/1;min-width:0;min-height:0;display:grid;
  grid-template-rows:minmax(0,1fr) auto;opacity:0;pointer-events:none;
  transition:opacity .42s var(--ease)}
.gal__stage > figure.on{opacity:1;pointer-events:auto}
@media(prefers-reduced-motion:reduce){.gal__stage > figure{transition:none}}
.gal__stage .im{width:100%;height:100%;aspect-ratio:auto}
.gal__stage figcaption{text-align:center;padding-top:.9rem;margin-top:.9rem;
  border-top:1px solid var(--hair)}
.gal__cap{display:flex;justify-content:space-between;gap:1rem;flex-wrap:wrap;
  padding-top:.85rem;margin-top:.9rem;border-top:1px solid var(--hair)}
.gal__cap .t{font-family:var(--serif6);font-weight:600;font-size:1rem}
.gal__cap .n{font-family:var(--mono);font-size:.63rem;letter-spacing:.12em;color:var(--g3);
  text-transform:uppercase}
.strip{display:flex;gap:1.4rem 1.8rem;margin-top:1.3rem;flex-wrap:wrap}
.strip__g{display:grid;gap:.5rem}
.strip__g > .m{font-size:.56rem;letter-spacing:.18em}
.strip__t{display:flex;gap:.4rem;flex-wrap:wrap}
.strip button{width:58px;height:70px;padding:0;background:none;border:0;cursor:pointer;
  border-bottom:2px solid transparent;display:flex;align-items:center;justify-content:center;
  transition:border-color .2s,opacity .2s;opacity:.55}
.strip button:hover{opacity:1}
.strip button[aria-pressed=true]{opacity:1;border-bottom-color:var(--red)}
.strip button .im{height:62px;width:52px;aspect-ratio:auto;background-size:contain}
.sw{display:inline-flex;align-items:center;gap:.5rem;font-family:var(--mono);font-size:.62rem;
  letter-spacing:.1em;text-transform:uppercase;color:var(--g3);background:none;border:0;
  cursor:pointer;padding:.35rem 0;border-bottom:2px solid transparent;transition:all .2s}
.sw i{width:15px;height:15px;flex:0 0 auto;box-shadow:inset 0 0 0 1px rgba(27,23,32,.14)}
.sw:hover{color:var(--ink)}
.sw[aria-pressed=true]{color:var(--ink);border-bottom-color:var(--red)}
.sws{display:flex;gap:1.1rem;flex-wrap:wrap;margin-top:1rem}

/* ── lightbox ─────────────────────────────────────────────────────────────── */
.lbx{position:fixed;inset:0;z-index:200;background:var(--paper);display:none;
  align-items:center;justify-content:center;padding:clamp(1rem,5vw,4rem);isolation:isolate}
.lbx.on{display:flex}
.lbx__box{position:relative;width:100%;max-width:1500px;height:78vh;overflow:hidden;
  touch-action:none;cursor:grab}
.lbx__box.zoomed{cursor:grab}
.lbx__box.dragging{cursor:grabbing}
.lbx .im{position:absolute;inset:0;width:100%;height:100%;aspect-ratio:auto;
  background-size:contain;transform-origin:50% 50%;
  transition:transform .28s var(--ease);will-change:transform}
.lbx__box.dragging .im{transition:none}
.lbx__bar{display:flex;align-items:center;gap:1.2rem;justify-content:center;margin-top:1.1rem;
  flex-wrap:wrap}
.lbx__z{display:flex;align-items:center;gap:.15rem;border:1px solid var(--hair-2)}
.lbx__z button{width:34px;height:30px;background:none;border:0;color:var(--ink);cursor:pointer;
  font-family:var(--mono);font-size:.9rem;line-height:1}
.lbx__z button:hover{background:var(--ink);color:var(--paper)}
.lbx__z span{font-family:var(--mono);font-size:.62rem;letter-spacing:.1em;color:var(--g2);
  min-width:4.2ch;text-align:center;font-variant-numeric:tabular-nums}
.lbx figcaption{color:var(--g2);text-align:center;margin-top:1.2rem}
.lbx__x{position:absolute;top:1.1rem;right:1.4rem;background:none;border:0;color:var(--ink);
  font-family:var(--mono);font-size:.66rem;letter-spacing:.16em;text-transform:uppercase;
  cursor:pointer;padding:.5rem;border-bottom:1px solid var(--ink)}
.lbx__a{position:absolute;top:50%;transform:translateY(-50%);background:none;border:0;
  color:var(--ink);font-size:2.2rem;line-height:1;cursor:pointer;padding:1rem;opacity:.45}
.lbx__a:hover{opacity:1}
.lbx__a.p{left:.5rem}.lbx__a.n{right:.5rem}

/* ── the ink counterpoint: colour standards, full bleed ──────────────────── */
.ink{background:var(--ink);color:var(--paper);padding-block:clamp(2.6rem,6vw,5rem)}
.ink .m{color:var(--g3)}
.ink .d2,.ink .d3{color:var(--paper)}
.ink .p{color:var(--g4)}
.chips{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:1px;
  margin-top:clamp(1.6rem,3.5vw,2.6rem);background:rgba(242,238,230,.14)}
.chip{background:var(--ink);padding-top:clamp(120px,17vw,190px);position:relative}
.chip i{position:absolute;top:0;left:0;right:0;height:clamp(120px,17vw,190px)}
.chip .b{padding:.9rem .1rem 0}
.chip .c{font-family:var(--mono);font-size:.62rem;letter-spacing:.08em;color:var(--g3)}
.chip .n{font-family:var(--serif6);font-weight:600;font-size:1.02rem;color:var(--paper);
  margin-top:.15rem}

/* ── registers: the texture belongs to the section opener, not every block ── */
.reg{position:relative}
.reg--sketched{--stroke:dotted;--strokec:var(--g4);--txt:var(--graphite)}
.reg--stitched{--stroke:dashed;--strokec:var(--hair-2);--txt:var(--ink)}
.reg--born{--stroke:solid;--strokec:var(--hair-2);--txt:var(--ink)}
.reg--born .band{padding-block:clamp(3rem,6.5vw,5.2rem) clamp(2.4rem,5vw,3.6rem)}
.reg--born .band::before,.reg--born .band::after{display:none}
.band{padding-block:clamp(2.4rem,5.5vw,4.4rem) clamp(1.6rem,3.5vw,2.6rem);
  border-top:1px solid var(--ink);position:relative;overflow:hidden}
.band::before{content:'';position:absolute;inset:0;pointer-events:none}
.reg--sketched .band::before{
  background-image:linear-gradient(rgba(74,69,79,.10) 1px,transparent 1px),
                   linear-gradient(90deg,rgba(74,69,79,.10) 1px,transparent 1px);
  background-size:30px 30px;
  -webkit-mask-image:linear-gradient(180deg,#000,transparent);
  mask-image:linear-gradient(180deg,#000,transparent)}
.reg--stitched .band::before{
  background-image:repeating-linear-gradient(45deg,rgba(27,23,32,.075) 0 1px,transparent 1px 11px);
  -webkit-mask-image:linear-gradient(180deg,#000,transparent);
  mask-image:linear-gradient(180deg,#000,transparent)}
.band__in{position:relative;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,.9fr);
  gap:var(--gap);align-items:end}
@media(max-width:820px){.band__in{grid-template-columns:1fr;gap:1.2rem}}
.band .n{font-family:var(--serif);font-weight:900;font-size:clamp(1rem,1.5vw,1.15rem);
  color:var(--red);letter-spacing:.02em}
.band h2{margin:.2rem 0 .1rem;color:var(--txt)}
.band .ln{font-family:var(--serif6);font-weight:600;font-size:clamp(1.05rem,1.9vw,1.35rem);
  color:var(--g2)}
.band .lg{width:min(260px,72%);margin-top:1.3rem}
.band .lg svg{width:100%;height:auto}
.band .df{color:var(--g2);font-size:.94rem;max-width:40ch}
.band .win{font-family:var(--mono);font-size:.6rem;letter-spacing:.15em;text-transform:uppercase;
  color:var(--g3);margin-top:1rem;padding-top:.7rem;border-top:1px solid var(--hair)}

/* ── logbook: a spine, hairlines, and nothing else ───────────────────────── */
.log{padding-bottom:clamp(1.5rem,4vw,3rem)}
.e{display:grid;grid-template-columns:clamp(3.4rem,6vw,5rem) 26px minmax(0,1fr);
  align-items:stretch}
.e__d{padding:1.9rem .9rem 0 0;text-align:right}
.e__d .dd{font-family:var(--serif);font-weight:900;font-size:clamp(1.4rem,2.6vw,1.85rem);
  line-height:.9;display:block;letter-spacing:-.02em;color:var(--txt)}
.e__d .mm{font-family:var(--mono);font-size:.56rem;letter-spacing:.13em;text-transform:uppercase;
  color:var(--g3);display:block;margin-top:.34rem}
.e__s{position:relative}
.e__s::before{content:'';position:absolute;top:0;bottom:0;left:50%;
  border-left:1px var(--stroke) var(--strokec)}
.e:first-child .e__s::before{top:2.2rem}
.e:last-child .e__s::before{bottom:auto;height:2.2rem}
.e__s .mk{position:absolute;top:1.85rem;left:50%;transform:translateX(-50%);
  background:var(--paper);padding:4px 0;box-sizing:content-box;color:var(--txt)}
.e__b{padding:1.75rem 0 2.2rem;min-width:0;border-bottom:1px solid var(--hair)}
.e:last-child .e__b{border-bottom:0}
.e__k{font-family:var(--mono);font-size:.58rem;letter-spacing:.19em;text-transform:uppercase;
  color:var(--g3)}
.e__h{font-family:var(--serif);font-weight:900;font-size:clamp(1.2rem,2.4vw,1.72rem);
  line-height:1.12;letter-spacing:-.015em;margin:.32rem 0 .55rem;max-width:26ch;text-wrap:balance}
.e__p{color:var(--g2);max-width:62ch;font-size:.97rem}
.reg--sketched .e__h{color:var(--graphite)}
.e.st-next .e__d .dd,.e.st-next .e__h,.e.st-next .e__p{color:var(--g3)}
.e.st-next .e__s::before{opacity:.45}
.e.st-now .e__k{color:var(--red)}
.e.st-now .e__s .mk{color:var(--red)}
.e.st-now .e__h::after{content:'';display:inline-block;width:7px;height:7px;border-radius:50%;
  background:var(--red);margin-left:.5rem;vertical-align:.14em}
.e.is-ask .e__h,.e.is-ask .e__d .dd{color:var(--ink)}
.e.is-ask .e__p{color:var(--g2)}
.e.is-ask .e__k{color:var(--red)}
.e.is-ask .e__s .mk{color:var(--red)}
.e.is-ask .e__s::before{opacity:1}
.mk{width:13px;height:13px;flex:0 0 auto;display:block}
.p-sk{fill:none;stroke:var(--g2);stroke-linejoin:round}
.p-skc{fill:none;stroke:var(--g2);stroke-linecap:round}
.p-st{stroke:var(--ink);stroke-linejoin:round}
.p-ink{fill:var(--ink)}
.p-bo{fill:var(--red)}

/* ── payloads: rules and space, no cards ─────────────────────────────────── */
.pay{margin-top:1.4rem}
.dec{display:grid;grid-template-columns:1fr 1fr;gap:0 clamp(1.4rem,3vw,2.6rem);
  border-top:1px solid var(--ink);padding-top:.85rem}
@media(max-width:620px){.dec{grid-template-columns:1fr;gap:1.1rem}}
.dec .lb{font-family:var(--mono);font-size:.56rem;letter-spacing:.18em;text-transform:uppercase;
  color:var(--g3);display:flex;align-items:center;gap:.45rem}
.dec .a .lb{color:var(--red)}
.dec .v{font-family:var(--serif6);font-weight:600;font-size:1.06rem;margin-top:.3rem;line-height:1.3}
.dec .b .v{color:var(--g4);text-decoration:line-through;text-decoration-color:var(--g4)}
.dec__why{grid-column:1/-1;margin-top:1.1rem;padding-top:.95rem;border-top:1px solid var(--hair);
  font-size:.95rem;color:var(--g2);max-width:66ch}
.dec__cost{display:block;margin-top:.9rem;font-family:var(--mono);font-size:.64rem;
  letter-spacing:.1em;color:var(--red)}
.meas__h{display:flex;justify-content:space-between;gap:1rem;flex-wrap:wrap;
  font-family:var(--mono);font-size:.6rem;letter-spacing:.14em;text-transform:uppercase;
  color:var(--g3);padding-bottom:.6rem}
.meas__h b{color:var(--ink);font-weight:400}
.meas__f{display:flex;justify-content:space-between;gap:1rem;flex-wrap:wrap;align-items:center;
  margin-top:.9rem}
.clear{display:flex;align-items:center;gap:.5rem;font-family:var(--mono);font-size:.64rem;
  letter-spacing:.08em;color:var(--g2)}
.clear b{color:var(--ink);font-weight:400}
.golink{font-family:var(--mono);font-size:.63rem;letter-spacing:.14em;text-transform:uppercase;
  background:none;border:0;border-bottom:1px solid var(--ink);color:var(--ink);cursor:pointer;
  padding:.2rem 0;transition:color .2s,border-color .2s}
.golink:hover{color:var(--red);border-color:var(--red)}
.mat tr.no td{color:var(--g4)}
.mat tr.no .em{text-decoration:line-through;text-decoration-color:var(--g4)}
.gridimgs{display:grid;grid-template-columns:repeat(auto-fit,minmax(148px,1fr));
  gap:clamp(.9rem,2vw,1.8rem);align-items:end}
.gridimgs figure .im{width:100%}
.vd{display:inline-flex;align-items:center;gap:.5rem;margin-top:1rem;font-family:var(--mono);
  font-size:.62rem;letter-spacing:.14em;text-transform:uppercase;color:var(--g2)}
.vd.no{color:var(--red)}
.rel{display:flex;align-items:baseline;gap:1rem;border-top:1px solid var(--ink);
  padding-top:.85rem;flex-wrap:wrap}
.rel .nm{font-family:var(--serif6);font-weight:600;font-size:1.1rem;flex:1 1 auto}
.rel .nt{font-family:var(--mono);font-size:.6rem;letter-spacing:.11em;text-transform:uppercase;
  color:var(--g3);display:block;margin-top:.18rem;font-weight:400}
.apr{display:flex;gap:.9rem;align-items:flex-start;border-top:1px solid var(--ink);
  padding-top:.85rem;flex-wrap:wrap}
.apr .mk{margin-top:.3rem;color:var(--g2)}
.apr .lb{font-family:var(--mono);font-size:.57rem;letter-spacing:.17em;text-transform:uppercase;
  color:var(--g3)}
.apr .v{font-family:var(--serif6);font-weight:600;font-size:1.05rem;margin-top:.2rem}
.apr .wq{font-family:var(--mono);font-size:.62rem;letter-spacing:.06em;color:var(--g2);
  margin-top:.35rem}
.apr--wait{border-color:var(--red);border-left:1px solid var(--red);border-bottom:1px solid var(--red);
  border-right:1px solid var(--red);padding:1rem 1.15rem;background:rgba(196,18,46,.03)}
.apr--wait .lb,.apr--wait .mk{color:var(--red)}
.alr{display:grid;grid-template-columns:1fr 1fr;gap:0 clamp(1.4rem,3vw,2.6rem);
  border-top:1px solid var(--red);padding-top:.85rem}
@media(max-width:620px){.alr{grid-template-columns:1fr;gap:1.1rem}}
.alr .lb{font-family:var(--mono);font-size:.56rem;letter-spacing:.18em;text-transform:uppercase;
  color:var(--g3)}
.alr .r .lb{color:var(--red)}
.alr p{font-size:.93rem;color:var(--g2);margin-top:.35rem}
.alr .ow{grid-column:1/-1;font-family:var(--mono);font-size:.6rem;letter-spacing:.11em;
  text-transform:uppercase;color:var(--red);margin-top:.9rem}

/* ── standfirst ───────────────────────────────────────────────────────────── */
.stand{padding-block:clamp(2.4rem,6vw,4.6rem) clamp(1.6rem,3.5vw,2.6rem)}
.stand__g{display:grid;grid-template-columns:minmax(0,1.4fr) minmax(0,1fr);gap:var(--gap);
  align-items:end}
@media(max-width:880px){.stand__g{grid-template-columns:1fr}}
.stand h1{margin:.6rem 0 .9rem;max-width:15ch}
.facts{display:grid;grid-template-columns:repeat(2,1fr);gap:1.1rem 1.6rem}
.facts dt{font-family:var(--mono);font-size:.57rem;letter-spacing:.16em;text-transform:uppercase;
  color:var(--g3)}
.facts dd{font-family:var(--mono);font-size:.85rem;margin-top:.2rem;font-variant-numeric:tabular-nums}
.facts dd.big{font-family:var(--serif);font-weight:900;font-size:1.85rem;letter-spacing:-.01em}
.meter{display:flex;align-items:center;gap:.5rem;margin:1.7rem 0 .55rem}
.meter i{height:2px;display:block;flex:1}
.meter i.done{background:var(--ink)}
.meter i.live{background:repeating-linear-gradient(90deg,var(--ink) 0 5px,transparent 5px 10px)}
.meter i.todo{background:var(--g4);opacity:.45}
.meter b{width:8px;height:8px;border-radius:50%;background:var(--red);flex:0 0 auto}
.meter__l{display:flex;justify-content:space-between;font-family:var(--mono);font-size:.56rem;
  letter-spacing:.16em;text-transform:uppercase;color:var(--g3)}
.ask{border:1px solid var(--red);padding:1.1rem 1.3rem;margin-top:clamp(1.8rem,4vw,2.8rem);
  display:flex;gap:1rem;align-items:flex-start;background:rgba(196,18,46,.03)}
.ask .k{font-family:var(--mono);font-size:.57rem;letter-spacing:.18em;text-transform:uppercase;
  color:var(--red)}
.ask p{font-size:.95rem;margin-top:.3rem}
.ask .mk{color:var(--red);margin-top:.3rem}

.cwrow{display:grid;grid-template-columns:repeat(auto-fit,minmax(104px,1fr));gap:1rem}
.cwrow i{display:block;height:78px;box-shadow:inset 0 0 0 1px rgba(27,23,32,.12)}
.cwrow .c{font-family:var(--mono);font-size:.58rem;letter-spacing:.06em;color:var(--g3);
  margin-top:.55rem}
.cwrow .n{font-family:var(--serif6);font-weight:600;font-size:.92rem;margin-top:.1rem}

/* ── documents ────────────────────────────────────────────────────────────── */
.doc{max-width:1080px;margin:0 auto;padding:clamp(1.6rem,4vw,3rem) var(--pad) 6rem}
.sheet{background:transparent}
.mast{display:flex;justify-content:space-between;align-items:flex-start;gap:1.6rem;
  padding-bottom:1.2rem;border-bottom:1px solid var(--ink);flex-wrap:wrap}
.mast__l{flex:1 1 340px;min-width:0}
.mast__l .type{font-family:var(--mono);font-size:.6rem;letter-spacing:.24em;text-transform:uppercase;
  color:var(--red)}
.mast__l h1{font-family:var(--serif);font-weight:900;font-size:clamp(1.9rem,4vw,3rem);
  line-height:1;letter-spacing:-.025em;margin:.35rem 0 .4rem;text-wrap:balance}
.mast__l .who{font-size:.93rem;color:var(--g2)}
.mast__r{text-align:right;flex:0 0 auto;padding-top:.3rem}
.mast__r svg{height:19px;width:auto;max-width:none;margin-left:auto}
.mast__r .meta{font-family:var(--mono);font-size:.58rem;letter-spacing:.1em;text-transform:uppercase;
  color:var(--g3);line-height:1.95;margin-top:.6rem}
.mast__r .meta b{color:var(--ink);font-weight:400}
.dl{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:1.1rem 1.8rem;
  margin-top:1.4rem}
.dl > div{min-width:0}
.dl dt{font-family:var(--mono);font-size:.56rem;letter-spacing:.16em;text-transform:uppercase;
  color:var(--g3)}
.dl dd{font-family:var(--mono);font-size:.84rem;margin-top:.18rem;font-variant-numeric:tabular-nums}
.sec{margin-top:clamp(2rem,4vw,3.2rem);position:relative}
.sec--rule{padding-top:clamp(1.5rem,3vw,2.2rem)}
.sec--rule::before{content:'';position:absolute;left:0;right:0;top:0;height:0;opacity:.5;
  border-top:var(--pw,1px) var(--pline,solid) var(--pcol,var(--hair));
  transform:scaleX(0);transform-origin:0 50%}
/* A section head is a head, not a caption: the document numbers its own
   sections down the left in the colour of the phase it is written in, the
   name is set in the display face, and whatever followed the middot stays
   beside it in small type — the qualifier a technical reader needs and the
   title a scanning reader needs, in one object. It draws itself in once, on
   the rule it sits on, and then it holds still to be read. */
.panel{counter-reset:sec}
.shd{display:flex;align-items:baseline;gap:clamp(.7rem,1.7vw,1.4rem);
  margin-bottom:clamp(1rem,2vw,1.4rem);counter-increment:sec}
.shd__n::before{content:counter(sec,decimal-leading-zero)}
.shd__n{flex:none;font-style:normal;font-family:var(--mono);font-size:.72rem;
  letter-spacing:.1em;color:var(--pink,var(--red));padding-top:.32em;
  font-variant-numeric:tabular-nums}
.shd__t{font-family:var(--serif);font-weight:900;color:var(--ink);text-wrap:balance;
  font-size:clamp(1.15rem,2.1vw,1.55rem);line-height:1.06;letter-spacing:-.015em;
  max-width:34ch}
.shd__q{display:block;font-family:var(--sans);font-weight:400;letter-spacing:0;
  font-size:.83rem;line-height:1.4;color:var(--graphite);margin-top:.4em;max-width:52ch}
.field--ink .shd__t,.field--red .shd__t{color:var(--paper)}
html.js .sec--rule::before{transition:transform 1s var(--ease)}
html.js .sec--rule.in::before{transform:scaleX(1)}
html.js .shd__n,html.js .shd__t{opacity:0;transform:translate3d(0,10px,0)}
html.js .sec.in .shd__n{opacity:1;transform:none;
  transition:opacity .6s var(--ease) .08s,transform .7s var(--ease) .08s}
html.js .sec.in .shd__t{opacity:1;transform:none;
  transition:opacity .65s var(--ease) .2s,transform .78s var(--ease) .2s}
html:not(.js) .sec--rule::before{transform:scaleX(1)}
@media(prefers-reduced-motion:reduce){
  html.js .sec--rule::before{transform:scaleX(1)}
  html.js .shd__n,html.js .shd__t{opacity:1;transform:none}}
.eyebrow{font-family:var(--mono);font-size:.58rem;letter-spacing:.2em;text-transform:uppercase;
  color:var(--g3);margin-bottom:1rem}
h2.h{font-family:var(--serif);font-weight:900;font-size:clamp(1.3rem,2.5vw,1.8rem);line-height:1.06;
  letter-spacing:-.012em;text-wrap:balance}
h3.sh{font-family:var(--serif6);font-weight:600;font-size:1.06rem;margin-bottom:.4rem}
p.body{color:var(--g2);max-width:64ch}
p.body + p.body{margin-top:.75rem}
p.body b{color:var(--ink);font-weight:500}
.note{font-family:var(--mono);font-size:.66rem;letter-spacing:.02em;color:var(--g3);line-height:1.8;
  max-width:78ch}
.two{display:grid;grid-template-columns:1.3fr 1fr;gap:var(--gap);align-items:start}
.two--even{grid-template-columns:1fr 1fr}
@media(max-width:820px){.two,.two--even{grid-template-columns:1fr}}
.plate{display:flex;align-items:center;justify-content:center}
.plate .im{width:100%}

.tw{overflow-x:auto;-webkit-overflow-scrolling:touch}
table.t{border-collapse:collapse;width:100%;min-width:520px;font-size:.82rem}
table.t th{font-family:var(--mono);font-size:.56rem;letter-spacing:.15em;text-transform:uppercase;
  color:var(--g3);text-align:left;padding:0 .8rem .55rem 0;border-bottom:1px solid var(--ink);
  white-space:nowrap;font-weight:400;vertical-align:bottom}
table.t td{padding:.55rem .8rem .55rem 0;border-bottom:1px solid var(--hair);vertical-align:top}
table.t tr:last-child td{border-bottom:0}
table.t .n{font-family:var(--mono);text-align:right;font-variant-numeric:tabular-nums;
  white-space:nowrap}
table.t th.n{text-align:right}
table.t td:last-child,table.t th:last-child{padding-right:0}
table.t .c{font-family:var(--mono);font-size:.74rem;letter-spacing:.04em;color:var(--g2);
  white-space:nowrap}
table.t .em{font-family:var(--serif6);font-weight:600;font-size:.95rem}
table.t tr.grp td{border-bottom:0;padding-top:1.3rem;padding-bottom:.25rem}
table.t tr.grp .gt{font-family:var(--mono);font-size:.58rem;letter-spacing:.16em;
  text-transform:uppercase;color:var(--red)}
table.t tr.sum td{border-top:1px solid var(--ink);border-bottom:0;padding-top:.75rem}
table.t tr.tot td{border-top:1px solid var(--ink);border-bottom:0;padding-top:.8rem;
  font-family:var(--serif6);font-weight:600;font-size:1.15rem}
table.t tr.tot .n{font-family:var(--mono);font-size:1.15rem;color:var(--red)}
.out{color:var(--red)}
.tag{font-family:var(--mono);font-size:.58rem;letter-spacing:.11em;text-transform:uppercase;
  color:var(--g3)}
.tag--r{color:var(--red)}

ul.li{list-style:none;display:grid;gap:0}
ul.li li{padding:.55rem 0;border-bottom:1px solid var(--hair);color:var(--g2);line-height:1.5;
  max-width:74ch}
ul.li li:last-child{border-bottom:0}
ol.num{list-style:none;counter-reset:c;display:grid;gap:0}
ol.num li{counter-increment:c;padding:.85rem 0 .85rem 2.4rem;position:relative;color:var(--g2);
  max-width:74ch;border-bottom:1px solid var(--hair)}
ol.num li:last-child{border-bottom:0}
ol.num li::before{content:counter(c,decimal-leading-zero);position:absolute;left:0;top:.95rem;
  font-family:var(--mono);font-size:.66rem;color:var(--red);letter-spacing:.04em}
ol.num li b{color:var(--ink);font-weight:500}

.pick{display:flex;gap:1.1rem;flex-wrap:wrap;margin-bottom:1.6rem;padding-bottom:.7rem;
  border-bottom:1px solid var(--hair)}
.pick button,.pick .pk{font-family:var(--mono);font-size:.63rem;letter-spacing:.12em;text-transform:uppercase;
  background:none;border:0;border-bottom:2px solid transparent;color:var(--g3);cursor:pointer;
  padding:.3rem 0;transition:all .2s}
.pick button:hover{color:var(--ink)}
.pick button[aria-pressed=true]{color:var(--ink);border-bottom-color:var(--red)}
.styl{display:none}.styl.on{display:block}

.pay-g{display:grid;grid-template-columns:repeat(auto-fit,minmax(178px,1fr));gap:0}
.pay-g > div{padding:1rem 1.2rem 1rem 0;border-top:1px solid var(--ink)}
.pay-g .pc{font-family:var(--serif);font-weight:900;font-size:2rem;line-height:1}
.pay-g .wh{font-family:var(--mono);font-size:.57rem;letter-spacing:.15em;text-transform:uppercase;
  color:var(--g3);margin:.4rem 0 .12rem}
.pay-g .am{font-family:var(--mono);font-size:.85rem;font-variant-numeric:tabular-nums}
.due{border-top:1px solid var(--red);border-bottom:1px solid var(--red);padding:1.4rem 0;
  display:flex;justify-content:space-between;align-items:center;gap:1.4rem 2rem;flex-wrap:wrap}
.due > div{flex:1 1 auto;min-width:0}
.due .l{font-family:var(--mono);font-size:.58rem;letter-spacing:.18em;text-transform:uppercase;
  color:var(--red)}
.due .v{font-family:var(--serif);font-weight:900;font-size:clamp(1.9rem,4.4vw,2.9rem);line-height:1;
  margin-top:.3rem}
.due .d{font-family:var(--mono);font-size:.66rem;line-height:1.85;color:var(--g2);text-align:right;
  flex:0 1 34ch}
.sign{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:2.2rem;
  margin-top:2.6rem}
.sign .nm{font-family:var(--serif6);font-weight:600;font-size:1.02rem}
.sign .rl{font-family:var(--mono);font-size:.57rem;letter-spacing:.14em;text-transform:uppercase;
  color:var(--g3);margin-top:.15rem}
.sign .ln{margin-top:1.7rem;border-bottom:1px solid var(--hair-2);height:1px}
.sign .lb{font-family:var(--mono);font-size:.54rem;letter-spacing:.14em;text-transform:uppercase;
  color:var(--g4);margin-top:.35rem}
.dfoot{margin-top:2.8rem;padding-top:1.1rem;border-top:1px solid var(--hair);display:flex;
  justify-content:space-between;gap:1rem;flex-wrap:wrap;font-family:var(--mono);font-size:.56rem;
  letter-spacing:.13em;text-transform:uppercase;color:var(--g3)}

/* ── system ───────────────────────────────────────────────────────────────── */
.spec{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));
  gap:clamp(1.2rem,3vw,2.4rem);margin-top:1.6rem}
.spec .sw-b{padding:1.4rem 1.4rem;min-height:120px;display:flex;align-items:center}
.spec .sw--sketched{background-image:linear-gradient(rgba(74,69,79,.09) 1px,transparent 1px),
  linear-gradient(90deg,rgba(74,69,79,.09) 1px,transparent 1px);background-size:24px 24px}
.spec .sw--stitched{background-image:repeating-linear-gradient(45deg,rgba(27,23,32,.07) 0 1px,transparent 1px 10px)}
.spec .sw--born{background:var(--ink)}
.spec .sw-b svg{width:100%;height:auto;max-width:190px}
.spec .sw--born .p-ink{fill:var(--paper)}
.spec h3{font-family:var(--serif);font-weight:900;font-size:1.35rem;line-height:1;margin-top:1rem}
.spec .ln{font-family:var(--serif6);font-weight:600;font-size:.94rem;color:var(--g2);margin:.3rem 0 .5rem}
.spec p{font-size:.88rem;color:var(--g2);line-height:1.55}
.kinds{display:grid;grid-template-columns:repeat(auto-fit,minmax(228px,1fr));
  gap:0 clamp(1.4rem,3vw,2.6rem);margin-top:1.4rem}
.kinds > div{padding:.95rem 0;border-top:1px solid var(--hair)}
.kinds .kn{font-family:var(--mono);font-size:.6rem;letter-spacing:.16em;text-transform:uppercase;
  color:var(--red);display:flex;align-items:center;gap:.5rem}
.kinds .kd{font-size:.88rem;color:var(--g2);margin-top:.35rem;line-height:1.55}
pre.code{background:var(--ink);color:var(--paper);padding:1.3rem 1.5rem;overflow-x:auto;
  font-family:var(--mono);font-size:.72rem;line-height:1.85;margin-top:1.2rem}
pre.code .cm{color:var(--g3)}
pre.code .st{color:#E8A0AE}
pre.code .ky{color:var(--g4)}

/* ═══════════════════════════════════════════════════════════════════════════
   THE PATTERN SHEET
   The vernacular here is not "editorial" in general — it is pattern making.
   A seam line carries its allowance five pixels below it. A grainline opens a
   section. A notch marks what is active. A graduated rule measures the read.
   Those are BORN's own materials, and they are what keep this from looking
   like every other document.
   ═══════════════════════════════════════════════════════════════════════════ */

/* ── voice ────────────────────────────────────────────────────────────────
   A label is something a person says, so it is set in the body face, in
   sentence case. The monospace is reserved for what a machine produced:
   codes, measurements, dates, money. Nothing else is ever set in it. */
.m,.eyebrow,.e__k,.gal__hint,.rail__l,.kinds .kn,.spec .ln,
.dl dt,.facts dt,.cover__meta dt,.sp__meta dt,table.t th,
.dec .lbl,.apr .lbl,.alr .lbl,.pay-g .wh,.due .l,.sign .rl,.sign .lb,
.toc .cat,.ph3 .n,.ph3__f,.meas__h,.clear,.rel .nt,.alr .ow,.vd,.tag,
.golink,.pick button,.nav button,.mast__l .type,.note,.apr .wq,
.lbx__x,.lbx__bar figcaption,.gal__stage figcaption,.strip figcaption{
  font-family:var(--sans);text-transform:none;letter-spacing:0;font-weight:400}
.m,.eyebrow{font-size:.83rem;color:var(--graphite);line-height:1.4}
.m--r{color:var(--red)}
.e__k,.toc .cat,.rel .nt,.apr .lbl,.dec .lbl,.alr .lbl,.ph3 .n,
.gal__hint,.rail__l,.sign .rl,.due .l,.pay-g .wh,.vd,.tag,.spec .ln{
  font-size:.8rem;color:var(--graphite)}
.dl dt,.facts dt,.cover__meta dt,.sp__meta dt,table.t th,.sign .lb{
  font-size:.76rem;color:var(--graphite)}
.note,.meas__h,.clear,.golink,.ph3__f,.kinds .kn{font-size:.8rem}
.eyebrow{margin-bottom:.8rem}
.meas__h b,.clear b{font-family:var(--mono);font-size:.76rem;color:var(--ink)}
.m--r,.dec .a .lbl,.apr--wait .lbl,.alr .r .lbl,.ph3.is-now .n,
.ph3.is-now .ph3__f,.alr .ow,.tag--r,.kinds .kn{color:var(--red)}
.mast__l .type{font-family:var(--serif6);font-weight:600;font-size:1rem;color:var(--red)}
.mast__r .meta,.dfoot{text-transform:none;letter-spacing:.02em}
.top .mark span{font-family:var(--sans);text-transform:none;letter-spacing:0;font-size:.78rem}

/* the payload labels, the captions and the remaining chrome speak too */
figcaption,.dec .lb,.apr .lb,.alr .lb,.band .win,.meter__l,.ask .k,
table.t tr.grp .gt,.pick .pk,.gal__cap .n,.sw{
  font-family:var(--sans);text-transform:none;letter-spacing:0;font-weight:400}
figcaption,.band .win,.meter__l,.ask .k,.pick .pk{font-size:.8rem;color:var(--graphite)}
.dec .lb,.apr .lb,.alr .lb{font-size:.8rem;color:var(--graphite)}
.dec .a .lb,.apr--wait .lb,.alr .r .lb,.ask .k{color:var(--red)}
table.t tr.grp .gt{font-size:.84rem;color:var(--red)}
/* dates, references and totals stay machined */
.e__d .mm,.mast__r .meta,.dfoot,.chip .c,.cwl .cd,.sp__code,.toc .no{
  font-family:var(--mono);text-transform:none}
.e__d .mm{letter-spacing:.04em}

/* ── the seam: a stitch line and the allowance that runs beside it ───────── */
.seam,.sp,.proc,.band,.toc__h,.mast,.sec--rule,.ph3,.dec,.alr,.rel,.apr,
.cover__meta,.gal__cap{position:relative}
.seam::before,.sp::before,.proc::before,.band::before,.ph3::before{
  content:'';position:absolute;left:0;right:0;top:0;border-top:1px solid var(--ink);
  pointer-events:none}
.seam::after,.sp::after,.proc::after,.band::after,.ph3::after{
  content:'';position:absolute;left:0;right:0;top:5px;
  border-top:1px dashed rgba(27,23,32,.34);pointer-events:none}
.sp,.proc,.ph3{border-top:0}
.band{border-top:0}
.reg--sketched .band::before,.reg--stitched .band::before{background:none}
.seam{height:6px;border:0;margin:0}

/* the register texture belongs to the band, not to its seam */
.band .tex{position:absolute;inset:6px 0 0;pointer-events:none;z-index:0}
.reg--sketched .band .tex{
  background-image:linear-gradient(rgba(74,69,79,.10) 1px,transparent 1px),
                   linear-gradient(90deg,rgba(74,69,79,.10) 1px,transparent 1px);
  background-size:30px 30px;
  -webkit-mask-image:linear-gradient(180deg,#000,transparent);
  mask-image:linear-gradient(180deg,#000,transparent)}
.reg--stitched .band .tex{
  background-image:repeating-linear-gradient(45deg,rgba(27,23,32,.075) 0 1px,transparent 1px 11px);
  -webkit-mask-image:linear-gradient(180deg,#000,transparent);
  mask-image:linear-gradient(180deg,#000,transparent)}

/* ── the grainline: the mark that opens a section ────────────────────────── */
.grain{width:74px;height:9px;color:var(--ink);opacity:.85;margin-bottom:.9rem}
.grain path{stroke:currentColor;stroke-width:1;fill:none}

/* ── the notch: what is active is cut, not underlined ────────────────────── */
.nav button{position:relative;border-bottom:0;padding:.62rem 0 .58rem;font-size:.83rem;
  color:var(--graphite)}
.nav button:hover{color:var(--ink)}
.nav button[aria-selected=true]{color:var(--ink);border-bottom:0}
.nav button[aria-selected=true]::after{content:'';position:absolute;left:50%;bottom:-1px;
  transform:translateX(-50%);width:0;height:0;
  border-left:6px solid transparent;border-right:6px solid transparent;
  border-bottom:7px solid var(--red)}
.pick button{border-bottom:0;position:relative;padding:.34rem 0 .5rem;font-size:.82rem}
.pick button[aria-selected=true],.pick button[aria-pressed=true]{border-bottom:0}
.pick button[aria-pressed=true]::after{content:'';position:absolute;left:50%;bottom:-1px;
  transform:translateX(-50%);width:0;height:0;
  border-left:5px solid transparent;border-right:5px solid transparent;
  border-bottom:6px solid var(--red)}
.strip button{border-bottom:0;position:relative}
.strip button[aria-pressed=true]::after{content:'';position:absolute;left:50%;bottom:-3px;
  transform:translateX(-50%);width:0;height:0;
  border-left:5px solid transparent;border-right:5px solid transparent;
  border-bottom:6px solid var(--red)}

/* ── the graduated rule: the header edge measures the read ───────────────── */
.top{border-bottom:0}
.top::after{content:'';position:absolute;left:0;right:0;bottom:0;height:7px;
  background:repeating-linear-gradient(90deg,rgba(27,23,32,.30) 0 1px,transparent 1px 12px)
             bottom left/100% 4px no-repeat,
             linear-gradient(var(--hair),var(--hair)) bottom left/100% 1px no-repeat;
  pointer-events:none}
.prog{position:absolute;left:0;bottom:0;height:4px;width:0;background:var(--red);z-index:1}

/* ═══════════════════════════════════════════════════════════════════════════
   CONTRASTO
   BORN's own identity work does colour takeovers — the page turns Rojo
   Valentino at the end of the brand book. So the document alternates ground
   instead of sitting on one: paper, ink, red. Each garment gets a poster that
   seduces and a sheet that specifies. Nothing on this page is timid, and
   nothing on it is imprecise.
   ═══════════════════════════════════════════════════════════════════════════ */
.bleed{width:100vw;margin-left:calc(50% - 50vw);position:relative}
.field--ink,.field--red{
  --hair:rgba(242,238,230,.22);--hair-2:rgba(242,238,230,.42);
  --graphite:rgba(242,238,230,.66);--g2:rgba(242,238,230,.80);
  --g3:rgba(242,238,230,.60);--g4:rgba(242,238,230,.42);
  color:var(--paper)}
.field--ink{background:var(--ink)}
.field--red{background:var(--red)}
.field--ink .d1,.field--ink .d2,.field--ink .d3,.field--ink h1,.field--ink h2,
.field--red .d1,.field--red .d2,.field--red .d3,.field--red h1,.field--red h2{color:var(--paper)}
.field--ink .p,.field--red .p{color:rgba(242,238,230,.82)}
.field--ink .sub,.field--red .sub{color:rgba(242,238,230,.74)}
.field--ink .m--r{color:var(--red)}
.field--red .m--r{color:var(--paper)}
.field--ink .p-ink,.field--red .p-ink{fill:var(--paper)}
.field--ink .p-sk,.field--ink .p-skc,.field--red .p-sk,.field--red .p-skc{stroke:rgba(242,238,230,.7)}
.field--ink .p-st,.field--red .p-st{stroke:var(--paper)}
.field--red .p-bo{fill:var(--paper)}
.field--ink .mk,.field--red .mk{color:var(--paper)}

/* type that is drawn rather than filled — the sketched state at poster scale */
.outline,.field--ink .outline,.field--red .outline{
  -webkit-text-stroke:1.6px var(--paper);color:transparent}
@media(max-width:760px){.outline{-webkit-text-stroke-width:1.1px}}
@media(max-width:760px){.outline{-webkit-text-stroke-width:1px}}

/* ── the poster: every garment opens with one ────────────────────────────── */
.hero{position:relative;overflow:hidden;isolation:isolate}
.hero__in{display:grid;grid-template-columns:minmax(0,1.04fr) minmax(0,1fr);
  align-items:stretch;min-height:min(88vh,760px)}
.hero__t{display:flex;flex-direction:column;justify-content:center;
  padding:clamp(2.4rem,6vw,5rem) clamp(1.25rem,5vw,4.5rem);
  max-width:calc(var(--max)/2 + 2rem);margin-left:auto;width:100%;position:relative;z-index:2}
.hero--flip .hero__t{order:2;margin-left:0;margin-right:auto}
.hero--flip .hero__img{order:1}
.hero__ix{font-family:var(--serif);font-weight:900;line-height:.68;letter-spacing:-.06em;
  font-size:clamp(5rem,15vw,13rem);color:var(--red);margin-left:-.055em;
  margin-bottom:-.10em;pointer-events:none}
.hero--flip .hero__ix{color:var(--paper)}
.hero__nm{font-family:var(--serif);font-weight:900;text-transform:uppercase;
  font-size:clamp(2.2rem,5.2vw,4.6rem);line-height:.88;letter-spacing:-.028em;
  margin:0;max-width:11ch;position:relative}
.hero__full{font-family:var(--mono);font-size:.72rem;letter-spacing:.04em;
  color:rgba(242,238,230,.66);margin-top:.9rem}
.hero__sub{font-family:var(--serif6);font-weight:600;font-size:clamp(1rem,1.7vw,1.28rem);
  line-height:1.3;max-width:30ch;margin-top:.9rem}
.hero__spec{font-family:var(--mono);font-size:.76rem;letter-spacing:.02em;line-height:2.1;
  margin-top:clamp(1.4rem,3vw,2.2rem);padding-top:.9rem;border-top:1px solid var(--hair-2);
  font-variant-numeric:tabular-nums}
.hero__spec b{font-weight:400;color:var(--paper)}

.hero__img{position:relative;background:var(--paper);display:flex;align-items:center;
  justify-content:center;padding:clamp(1.5rem,4vw,3.4rem)}
.hero__img .im{width:100%;max-height:74vh}
.hero__img .im{mix-blend-mode:multiply}

/* ── the three acts: paper, then ink, then Rojo Valentino ────────────────── */
.act{padding-block:clamp(3rem,8vw,6.5rem);position:relative;overflow:hidden}
.act__in{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);
  gap:clamp(1.6rem,4vw,4rem);align-items:end}
@media(max-width:880px){.act__in{grid-template-columns:1fr;gap:1.6rem}}
.act__n{font-family:var(--serif);font-weight:900;font-size:clamp(4rem,13vw,11rem);
  line-height:.7;letter-spacing:-.06em;margin-left:-.06em}
.act__nm{font-family:var(--serif);font-weight:900;font-size:clamp(2.4rem,6.5vw,5.4rem);
  line-height:.9;letter-spacing:-.03em;margin-top:.5rem}
.act__ln{font-family:var(--serif6);font-weight:600;font-size:clamp(1.1rem,2.1vw,1.6rem);
  margin-top:.6rem}
.act__lg{width:min(320px,80%);margin-top:clamp(1.4rem,3vw,2.2rem)}
.act__lg svg{width:100%;height:auto}
.act__f{display:flex;align-items:center;gap:.7rem;margin-top:clamp(1.4rem,3vw,2rem);
  padding-top:.9rem;border-top:1px solid var(--hair-2);font-size:.85rem}
.act__f .wk{margin-left:auto;font-family:var(--mono);font-size:.78rem}
.act--sketched{background:var(--paper)}
.act--sketched .act__tex{position:absolute;inset:0;pointer-events:none;
  background-image:linear-gradient(rgba(74,69,79,.11) 1px,transparent 1px),
                   linear-gradient(90deg,rgba(74,69,79,.11) 1px,transparent 1px);
  background-size:34px 34px;
  -webkit-mask-image:radial-gradient(120% 80% at 20% 40%,#000,transparent);
  mask-image:radial-gradient(120% 80% at 20% 40%,#000,transparent)}
.act--stitched .act__tex{position:absolute;inset:0;pointer-events:none;
  background-image:repeating-linear-gradient(45deg,rgba(242,238,230,.10) 0 1px,transparent 1px 13px)}
.act--born .act__tex{display:none}

/* ═══════════════════════════════════════════════════════════════════════════
   THE JOURNEY
   A phase is not a chapter you pass once — it is a set of graphic properties
   that every rule, tint and mark in the document inherits. Each phase owns a
   line (dotted, stitch-dashed, solid), a colour (graphite, ink, Rojo Valentino)
   and a texture (construction grid, diagonal hatch, clean paper). Scroll, or
   change what you are looking at, and the document crosses with you.
   ═══════════════════════════════════════════════════════════════════════════ */
.ph-sketched{--pline:dotted;--pcol:rgba(92,87,98,.85);--pink:var(--graphite);
  --ptint:rgba(74,69,79,.055);--pw:1px}
.ph-stitched{--pline:dashed;--pcol:rgba(27,23,32,.55);--pink:var(--ink);
  --ptint:rgba(27,23,32,.075);--pw:1.2px}
.ph-born{--pline:solid;--pcol:var(--red);--pink:var(--red);
  --ptint:rgba(196,18,46,.055);--pw:1.4px}

/* the sheet under a poster takes the phase of the view you are looking at */
.sp{--pline:dotted;--pcol:rgba(92,87,98,.85);--pink:var(--graphite);--ptint:transparent;--pw:1px}
.pband{display:flex;align-items:center;gap:.9rem;padding-top:clamp(1.4rem,3vw,2.2rem)}
.pband__ln{flex:1 1 auto;order:2;height:0;
  border-top:var(--pw) var(--pline) var(--pcol);transition:border-color .4s var(--ease)}
.pband__p{display:none;align-items:center;gap:.6rem;flex:0 0 auto;order:1}
.pband__p b{font-family:var(--serif6);font-weight:600;font-size:1.05rem;color:var(--pink);
  transition:color .4s var(--ease)}
.pband__p > span{font-size:.8rem;color:var(--graphite)}
.pband__p .mk{color:var(--pink)}
.sp.ph-sketched .pband__p[data-p=sketched],
.sp.ph-stitched .pband__p[data-p=stitched],
.sp.ph-born .pband__p[data-p=born]{display:flex}
@media(max-width:700px){.pband{flex-wrap:wrap}.pband__ln{flex-basis:100%;order:3}
  .pband__p > span{display:none}}
.sp__body{position:relative;transition:background-color .5s var(--ease)}
.sp__body::before{content:'';position:absolute;inset:0;pointer-events:none;
  background:var(--ptint);transition:background-color .5s var(--ease);z-index:-1}
.sp .calls li,.sp .cwl li{border-bottom:var(--pw) var(--pline) var(--pcol);
  transition:border-color .4s var(--ease)}
.sp .m{color:var(--pink);transition:color .4s var(--ease)}
.sp .gal__stage{position:relative}
.sp .gal__stage::after{content:'';position:absolute;left:0;right:0;bottom:-.55rem;
  border-bottom:var(--pw) var(--pline) var(--pcol);transition:border-color .4s var(--ease)}
.sp .strip button[aria-pressed=true]::after{border-bottom-color:var(--pink)}
.sp .rail__r{background:var(--pcol);opacity:.75}

/* the phase rail carries its own line, so the three states are told apart by
   stroke and not only by position */
.rail__r{height:0;border-top:1px dotted var(--g4);background:none!important}
.rail__n:nth-child(1) ~ .rail__r{border-top-style:dotted}
.rail{gap:.7rem}
.rail__n.is-on .rail__l{color:var(--pink)}

/* ── the header always says which phase you are in ───────────────────────── */
.pnow{display:flex;align-items:center;gap:.5rem;margin-left:1.4rem;flex:0 0 auto;
  font-size:.78rem;color:var(--graphite);white-space:nowrap;
  transition:color .4s var(--ease)}
.pnow .mk{color:var(--pink,var(--graphite))}
.pnow b{font-weight:400;color:var(--pink,var(--ink))}
.pnow__ln{width:26px;height:0;border-top:var(--pw,1px) var(--pline,dotted) var(--pcol,var(--g4));
  transition:border-color .4s var(--ease)}
@media(max-width:1000px){.pnow{margin-left:auto;order:0;font-size:.72rem}
  .pnow__ln{width:18px}.nav{width:100%;order:1}}
body{--pline:dotted;--pcol:rgba(92,87,98,.6);--pink:var(--graphite);--pw:1px}
.top{transition:none}
.prog{background:var(--pink,var(--red));transition:background-color .4s var(--ease)}

/* ── a document belongs to a phase, and says so ──────────────────────────── */
.pstrip{display:flex;align-items:center;gap:.7rem;margin-bottom:1.1rem;
  padding-bottom:.75rem;border-bottom:var(--pw) var(--pline) var(--pcol)}
.pstrip .mk{color:var(--pink)}
.pstrip b{font-family:var(--serif6);font-weight:600;font-size:1rem;color:var(--pink)}
.pstrip span{font-size:.8rem;color:var(--graphite)}
.pstrip .pstrip__t{margin-left:auto;font-family:var(--mono);font-size:.72rem;
  letter-spacing:.04em;color:var(--graphite)}
@media(max-width:620px){.pstrip{flex-wrap:wrap;gap:.45rem .7rem}
  .pstrip .pstrip__t{margin-left:0;width:100%}}

/* ── every document opens on ink and closes in Rojo Valentino ──────────────
   The opener behaves like the cover of the document it belongs to: the phase
   numeral stands at poster scale behind the title and drifts against the
   scroll, the title rises out of its own baseline a word at a time, and the
   reference matter is drawn in under a rule that opens from the left. Nothing
   moves once it has arrived — the page a client reads is a still page. */
.docopen{position:relative;overflow:hidden;
  padding-block:clamp(3rem,7vw,5.6rem) clamp(1.6rem,3.5vw,2.6rem)}
.docopen__in{position:relative;z-index:1;padding-left:var(--pad);padding-right:var(--pad)}
.docopen__gh{position:absolute;z-index:0;right:-.04em;top:clamp(1rem,7%,3.5rem);
  pointer-events:none;user-select:none;text-align:right;
  transform:translate3d(0,var(--gy,0px),0);
  opacity:0;transition:opacity 1.1s var(--ease) .15s}
.docopen__gh b{display:block;font-family:var(--serif);font-weight:900;line-height:.78;
  font-size:clamp(6.5rem,17vw,14rem);letter-spacing:-.05em;
  -webkit-text-stroke:2px var(--paper);color:transparent}
.docopen__gh span{display:block;font-family:var(--serif6);font-weight:600;
  font-size:clamp(.9rem,1.6vw,1.3rem);opacity:.9;margin-top:.3em;
  padding-right:clamp(1.2rem,4.5vw,4rem)}
.docopen.in .docopen__gh{opacity:.28}
.docopen .type{font-family:var(--serif6);font-weight:600;font-size:1.05rem;color:var(--red);
  display:flex;align-items:center;gap:.55rem}
.docopen__tk{display:block;width:8px;height:8px;border-radius:50%;flex:none;
  background:currentColor;transform:scale(0)}
.docopen--red .type{color:var(--paper);opacity:.75}
.docopen h1{font-family:var(--serif);font-weight:900;text-transform:uppercase;
  font-size:clamp(2.1rem,6vw,5rem);line-height:.88;letter-spacing:-.03em;
  margin:.55rem 0 .3rem;max-width:17ch}
.docopen h1 .wd{display:inline-block;overflow:hidden;vertical-align:bottom;
  padding-bottom:.1em;margin-bottom:-.1em}
.docopen h1 .wd i{display:block;font-style:normal}
.docopen .who{font-size:.95rem;color:rgba(242,238,230,.72)}
.docopen__rl{height:1px;background:currentColor;opacity:.3;margin-top:clamp(1.4rem,3vw,2.2rem);
  transform:scaleX(0);transform-origin:0 50%}
.docopen__b{display:flex;justify-content:space-between;align-items:flex-end;gap:1.4rem;
  flex-wrap:wrap;margin-top:1rem;padding-top:0}

/* the arrival, once and only once */
html.js .docopen h1 .wd i{transform:translate3d(0,105%,0)}
html.js .docopen.in h1 .wd i{transform:none;transition:transform .9s var(--ease)}
html.js .docopen.in h1 .wd:nth-child(2) i{transition-delay:.06s}
html.js .docopen.in h1 .wd:nth-child(3) i{transition-delay:.12s}
html.js .docopen.in h1 .wd:nth-child(4) i{transition-delay:.18s}
html.js .docopen.in h1 .wd:nth-child(5) i{transition-delay:.24s}
html.js .docopen.in h1 .wd:nth-child(n+6) i{transition-delay:.30s}
html.js .docopen .type,html.js .docopen .who,html.js .docopen__b{
  opacity:0;transform:translate3d(0,12px,0)}
html.js .docopen.in .type{opacity:1;transform:none;
  transition:opacity .7s var(--ease),transform .8s var(--ease)}
html.js .docopen.in .who{opacity:1;transform:none;
  transition:opacity .7s var(--ease) .34s,transform .8s var(--ease) .34s}
html.js .docopen.in .docopen__b{opacity:1;transform:none;
  transition:opacity .7s var(--ease) .5s,transform .8s var(--ease) .5s}
html.js .docopen.in .docopen__tk{transform:scale(1);
  transition:transform .55s cubic-bezier(.2,1.5,.4,1) .1s}
html.js .docopen.in .docopen__rl{transform:scaleX(1);
  transition:transform 1.05s var(--ease) .42s}
html:not(.js) .docopen__tk,html:not(.js) .docopen__rl{transform:none}
html:not(.js) .docopen__gh{opacity:.28}
@media(prefers-reduced-motion:reduce){
  html.js .docopen h1 .wd i,html.js .docopen .type,html.js .docopen .who,
  html.js .docopen__b{transform:none;opacity:1;transition:none}
  html.js .docopen__tk{transform:scale(1)}
  html.js .docopen__rl{transform:scaleX(1)}}
@media(max-width:760px){
  .docopen__gh b{-webkit-text-stroke-width:1.4px;font-size:clamp(4.6rem,22vw,8rem)}
  .docopen__gh span{font-size:.95rem}
  .docopen.in .docopen__gh{opacity:.22}}
.docopen__m{font-family:var(--mono);font-size:.78rem;letter-spacing:.02em;line-height:2;
  font-variant-numeric:tabular-nums;text-align:right}
.docopen__m b{font-weight:400;color:var(--paper)}
.docopen .pstrip{border-bottom:0;margin:0;padding:0;gap:.65rem}
.docopen .pstrip b,.docopen .pstrip .mk{color:var(--paper)}
.docopen .pstrip span{color:rgba(242,238,230,.66)}
.docopen .pstrip__t{display:none}

/* the amount due is the loudest number in the document */
.duefield{padding-block:clamp(2.6rem,6vw,4.4rem)}
.duefield__in{padding-left:var(--pad);padding-right:var(--pad);display:flex;
  justify-content:space-between;align-items:flex-end;gap:1.6rem 2.4rem;flex-wrap:wrap}
.duefield .l{font-family:var(--serif6);font-weight:600;font-size:1.05rem;
  color:rgba(242,238,230,.8)}
.duefield .v{font-family:var(--serif);font-weight:900;font-size:clamp(3rem,10vw,8rem);
  line-height:.82;letter-spacing:-.045em;color:var(--paper);margin-top:.3rem}
.duefield .d{font-family:var(--mono);font-size:.8rem;line-height:2.1;
  color:rgba(242,238,230,.82);text-align:right}
@media(max-width:700px){.duefield .d{text-align:left}}

/* a verdict is a field, not a box */
.vfield{padding-block:clamp(2.2rem,5vw,3.6rem)}
.vfield__in{padding-left:var(--pad);padding-right:var(--pad);display:grid;
  grid-template-columns:minmax(0,1.1fr) minmax(0,1fr);gap:1.4rem 2.6rem;align-items:end}
@media(max-width:820px){.vfield__in{grid-template-columns:1fr}}
.vfield .l{font-family:var(--serif6);font-weight:600;font-size:1rem;color:rgba(242,238,230,.75)}
.vfield h2{font-family:var(--serif);font-weight:900;font-size:clamp(1.7rem,4.4vw,3.2rem);
  line-height:.96;letter-spacing:-.025em;color:var(--paper);margin-top:.4rem}
.vfield p{font-size:.92rem;color:rgba(242,238,230,.8)}


/* ═══════════════════════════════════════════════════════════════════════════
   THE ROOM OPENS
   A front door that states what this is, three phases you scroll *through*
   rather than past, a marker you can drag along the rule, and a page that
   turns Rojo Valentino as you reach the end of it.
   ═══════════════════════════════════════════════════════════════════════════ */

/* ── the front door ──────────────────────────────────────────────────────── */
.door{min-height:calc(100vh - var(--topH));display:grid;align-content:center;
  justify-items:center;text-align:center;gap:clamp(1rem,2.4vw,1.8rem);
  padding-block:clamp(3rem,10vh,7rem);position:relative;overflow:hidden}
.door__grid{position:absolute;inset:0;pointer-events:none;
  background-image:linear-gradient(rgba(74,69,79,.09) 1px,transparent 1px),
                   linear-gradient(90deg,rgba(74,69,79,.09) 1px,transparent 1px);
  background-size:38px 38px;
  -webkit-mask-image:radial-gradient(58% 46% at 50% 46%,#000,transparent);
  mask-image:radial-gradient(58% 46% at 50% 46%,#000,transparent)}
.door > *{position:relative}
.door__wm{width:min(340px,62vw);height:auto;position:relative}
.door__wm > span{display:block}
.door__wm > span:not(:first-child){position:absolute;inset:0}
.door__wm svg{width:100%;height:auto}
.door__wm > span{opacity:0;transition:opacity .5s var(--ease)}
.door__wm > span.on{opacity:1}
.door h1{font-family:var(--serif);font-weight:900;text-transform:uppercase;
  font-size:clamp(2.3rem,8.4vw,7rem);line-height:.86;letter-spacing:-.04em;
  max-width:12ch}
.door .lede{font-family:var(--serif6);font-weight:600;
  font-size:clamp(1.05rem,2.1vw,1.5rem);line-height:1.34;color:var(--g2);max-width:34ch}
.door__ph{display:flex;align-items:center;gap:clamp(.6rem,2vw,1.4rem);flex-wrap:wrap;
  justify-content:center;margin-top:clamp(.6rem,2vw,1.2rem)}
.door__ph span{display:flex;align-items:center;gap:.45rem;font-size:.85rem;color:var(--graphite)}
.door__ph i{width:clamp(18px,4vw,44px);height:0;display:block}
.door__ph i:nth-of-type(1){border-top:1px dotted var(--g4)}
.door__ph i:nth-of-type(2){border-top:1.2px dashed var(--hair-2)}
.door__cue{font-size:.8rem;color:var(--graphite);display:flex;align-items:center;gap:.5rem;
  margin-top:clamp(1rem,3vh,2.4rem)}
.door__cue b{font-weight:400;display:block;width:1px;height:34px;background:var(--hair-2);
  position:relative;overflow:hidden}
.door__cue b::after{content:'';position:absolute;inset:0;background:var(--red);
  transform:translateY(-100%)}
@media(prefers-reduced-motion:no-preference){
  .door__cue b::after{animation:drop 2.4s var(--ease) infinite}
  @keyframes drop{0%{transform:translateY(-100%)}55%{transform:translateY(0)}
    100%{transform:translateY(100%)}}}

/* ── three states you scroll through ─────────────────────────────────────── */
.acts{position:relative}
html.js .acts{height:330vh}
.acts__stage{display:grid;grid-template-rows:1fr auto;gap:1.5rem;
  padding-block:clamp(2rem,5vh,3.4rem);background:var(--paper);
  transition:background-color .18s linear,color .3s linear}
html.js .acts__stage{position:sticky;top:var(--topH);height:calc(100vh - var(--topH));
  overflow:hidden}
.acts__tex{position:absolute;inset:0;pointer-events:none;opacity:0;
  transition:opacity .5s var(--ease)}
.acts__tex--grid{background-image:linear-gradient(rgba(74,69,79,.13) 1px,transparent 1px),
  linear-gradient(90deg,rgba(74,69,79,.13) 1px,transparent 1px);background-size:34px 34px}
.acts__tex--hatch{background-image:repeating-linear-gradient(45deg,rgba(242,238,230,.11) 0 1px,transparent 1px 13px)}
.acts__in{display:grid;align-content:center;position:relative}
.acts__s{grid-area:1/1;display:grid;grid-template-columns:minmax(0,.92fr) minmax(0,1.08fr);
  gap:clamp(1.4rem,4vw,4rem);align-items:center}
@media(max-width:880px){.acts__s{grid-template-columns:1fr;gap:1.2rem;align-content:center}}
html.js .acts__s{opacity:0;transition:opacity .32s var(--ease),transform .5s var(--ease);
  transform:translateY(14px);pointer-events:none}
html.js .acts__s.on{opacity:1;transform:none;pointer-events:auto}
.acts__n{font-family:var(--serif);font-weight:900;font-size:clamp(3.4rem,11vw,9rem);
  line-height:.7;letter-spacing:-.06em;margin-left:-.06em}
.acts__nm{font-family:var(--serif);font-weight:900;font-size:clamp(2.2rem,6vw,5rem);
  line-height:.9;letter-spacing:-.03em;margin-top:.4rem}
.acts__ln{font-family:var(--serif6);font-weight:600;font-size:clamp(1.05rem,2vw,1.5rem);
  margin-top:.5rem;opacity:.85}
.acts__lg{width:min(300px,74%);margin-top:clamp(1rem,2.5vw,1.8rem)}
.acts__lg svg{width:100%;height:auto}
.acts__s[data-phase=stitched] .p-st{stroke:rgba(242,238,230,.88)}
.acts__s[data-phase=stitched] .p-sk,.acts__s[data-phase=stitched] .p-skc{stroke:rgba(242,238,230,.6)}
.acts__s[data-phase=born] .p-bo,.acts__s[data-phase=born] .p-ink{fill:var(--paper)}
.acts__body{font-size:clamp(.98rem,1.4vw,1.1rem);line-height:1.6;max-width:44ch}
.acts__f{display:flex;align-items:center;gap:.7rem;margin-top:1.4rem;padding-top:.9rem;
  border-top:1px solid currentColor;font-size:.85rem;opacity:.78}
.acts__f .wk{margin-left:auto;font-family:var(--mono);font-size:.78rem}
.acts__rail{display:flex;align-items:center;gap:.7rem;flex-wrap:wrap}
.acts__rail span{display:flex;align-items:center;gap:.45rem;font-size:.8rem;opacity:.45;
  transition:opacity .4s var(--ease)}
.acts__rail span.on{opacity:1}
.acts__rail i{flex:1 1 auto;height:0;border-top:1px solid currentColor;opacity:.32}
@media(prefers-reduced-motion:reduce){
  html.js .acts{height:auto}
  html.js .acts__stage{position:static;height:auto}
  html.js .acts__s{opacity:1;transform:none;position:relative;grid-area:auto;
    margin-bottom:3rem;pointer-events:auto}}

/* ── the marker you can drag along the rule ──────────────────────────────── */
.nav{position:relative}
.notch{position:absolute;bottom:-1px;left:0;width:0;height:0;
  border-left:7px solid transparent;border-right:7px solid transparent;
  border-bottom:8px solid var(--red);cursor:grab;touch-action:none;
  transform:translateX(-7px);transition:transform .42s var(--ease);z-index:2}
.notch::before{content:'';position:absolute;left:-13px;right:-13px;top:-14px;bottom:-8px}
.notch.dragging{cursor:grabbing;transition:none}
.notch.dragging::after{content:'';position:absolute;left:50%;bottom:9px;width:1px;height:13px;
  background:var(--red);transform:translateX(-50%)}
.nav button[aria-selected=true]::after{display:none}
.nav.armed button{color:var(--graphite)}
.nav.armed button.near{color:var(--ink)}

/* ── the page turns red at the end ───────────────────────────────────────── */
.top{background:var(--top-bg,rgba(242,238,230,.93))}
.top.turned .nav button,.top.turned .pnow,.top.turned .pr,.top.turned .pnow b{color:var(--paper)}
.top.turned .nav button[aria-selected=true]{color:var(--paper)}
.top.turned .p-ink{fill:var(--paper)}
.top.turned .p-bo{fill:var(--paper)}
.top.turned .notch{border-bottom-color:var(--paper)}
.top.turned .prog{background:var(--paper)}
.top.turned::after{opacity:.5}
.top,.top .nav button,.top .pnow{transition:background-color .35s linear,color .35s linear}


/* ── a title wears its own state ─────────────────────────────────────────
   Sketched is drawn and not filled. Stitched is filled with thread. BORN is
   solid and in colour. The same three states the mark lives, in the type.
   The ink these are drawn in is --ts, named on whatever ground they sit on:
   a stroke or a thread cannot be currentColor, because on these titles the
   colour itself is what has been taken away. */
/* the doubled class is deliberate: these have to outrank whatever colours a
   heading on the ground it happens to be sitting on */
.t-sketch.t-sketch{-webkit-text-stroke:1.8px var(--ts,var(--ink));color:transparent}
.t-stitch.t-stitch{background-image:repeating-linear-gradient(45deg,
    var(--ts,var(--ink)) 0 2.2px,transparent 2.2px 6.4px);
  -webkit-background-clip:text;background-clip:text;color:transparent;
  -webkit-text-stroke:.9px var(--ts,var(--ink))}
/* BORN is solid in whatever colour the ground calls for, so it is left alone */
.field--ink,.field--red,.acts__s[data-i="1"],.acts__s[data-i="2"]{--ts:var(--paper)}
.acts__s[data-i="0"],.band{--ts:var(--ink)}
@media(max-width:760px){.t-sketch.t-sketch{-webkit-text-stroke-width:1.2px}
  .t-stitch.t-stitch{-webkit-text-stroke-width:.6px;
    background-image:repeating-linear-gradient(45deg,
      var(--ts,var(--ink)) 0 1.5px,transparent 1.5px 4.4px)}}

/* the fill sweeps in when its state arrives */
html.js .acts__s .acts__nm{clip-path:inset(0 102% 0 0)}
html.js .acts__s.on .acts__nm{clip-path:inset(0 -2% 0 0);
  transition:clip-path .85s var(--ease) .12s}
@media(prefers-reduced-motion:reduce){
  html.js .acts__s .acts__nm,html.js .acts__s.on .acts__nm{clip-path:none;transition:none}}

/* ── the last section: the sentence finishes ──────────────────────────────
   The closer is not a footer, it is the end of the studio's own sentence, and
   the scrollbar plays it. Rojo Valentino floods up from the foot of the page
   and swallows the graph paper; the mark is then drawn, stitched and set
   solid; and the last thing left standing is the finished logotype with its
   dot. Hold the scroll anywhere and the sequence holds with you; scroll back
   up and it runs backwards. Without JavaScript, and in print, the whole thing
   collapses to the finished mark on red — the still frame the sequence ends on. */
.closer{position:relative;background:var(--from,var(--paper));color:var(--paper)}
.closer__track{position:relative}
html.js .closer__track{height:250vh}
.closer__stage{position:relative;overflow:hidden;background:var(--from,var(--paper));
  display:grid;place-items:center;align-content:center;
  min-height:min(94vh,780px);padding-block:clamp(3rem,9vh,6rem)}
html.js .closer__stage{position:sticky;top:0;height:100vh;min-height:540px;padding-block:0}
.closer__flood{position:absolute;inset:0;background:var(--red);
  transform:translate3d(0,calc((1 - var(--fl,1)) * 101%),0);will-change:transform}
.closer__grid{position:absolute;inset:0;opacity:calc(1 - var(--fl,1));
  background-image:linear-gradient(var(--rule) 1px,transparent 1px),
   linear-gradient(90deg,var(--rule) 1px,transparent 1px);
  background-size:34px 34px}

/* the three states, and then the mark itself */
.closer__in{position:relative;z-index:1;display:flex;flex-direction:column;
  align-items:center;text-align:center;width:100%}
.closer__wm{position:relative;width:min(430px,74vw)}
.closer__wm > span{display:block;opacity:0;transform:scale(.98);
  transition:opacity .5s var(--ease),transform .8s var(--ease)}
.closer__wm > span:not(:first-child){position:absolute;inset:0}
.closer__wm > span.on{opacity:1;transform:none}
.closer__wm svg{width:100%;height:auto;display:block}
.closer .p-sk,.closer .p-skc{stroke:rgba(242,238,230,.9)}
.closer .p-st{stroke:var(--paper)}
.closer .p-bo{fill:var(--paper)}
.closer .wmdot{transform-box:fill-box;transform-origin:50% 50%;transform:scale(0)}
.closer__wm > span.on .wmdot{transform:none;
  transition:transform .62s cubic-bezier(.18,1.55,.35,1) .28s}
.closer__stg{position:relative;height:2em;width:100%;margin-top:clamp(1rem,2.6vh,1.7rem)}
.closer__stg span{position:absolute;left:0;right:0;opacity:0;transform:translate3d(0,9px,0);
  transition:opacity .42s var(--ease),transform .55s var(--ease);
  font-family:var(--serif6);font-weight:600;font-size:clamp(1rem,2.3vw,1.45rem)}
.closer__stg span.on{opacity:1;transform:none}
.closer__stg i{font-style:normal;font-family:var(--mono);font-size:.6rem;letter-spacing:.18em;
  opacity:.62;margin-right:.7rem;vertical-align:.3em}

/* the rail keeps count of where the sequence is */
.closer__rail{position:absolute;z-index:2;left:clamp(1rem,4vw,3.2rem);top:50%;
  transform:translateY(-50%);display:flex;flex-direction:column;gap:.95rem;
  opacity:0;transition:opacity .5s var(--ease)}
.closer.lit .closer__rail{opacity:1}
.closer__rail b{display:flex;align-items:center;gap:.55rem;font-weight:400;
  font-family:var(--mono);font-size:.6rem;letter-spacing:.16em;
  color:rgba(242,238,230,.4);transition:color .45s var(--ease)}
.closer__rail b::before{content:'';width:24px;height:1px;background:currentColor;flex:none;
  transform:scaleX(.34);transform-origin:0 50%;transition:transform .55s var(--ease)}
.closer__rail b.on{color:var(--paper)}
.closer__rail b.on::before{transform:scaleX(1)}

/* and the words the document signs off with */
.closer__end{position:absolute;left:0;right:0;bottom:clamp(1.6rem,6vh,4rem);z-index:1;
  padding-left:var(--pad);padding-right:var(--pad);
  display:flex;flex-direction:column;align-items:center;text-align:center;gap:.85rem;
  opacity:0;transform:translate3d(0,20px,0);
  transition:opacity .7s var(--ease),transform .8s var(--ease)}
.closer.ended .closer__end{opacity:1;transform:none}
.closer h2{font-family:var(--serif);font-weight:900;font-size:clamp(1.4rem,3.4vw,2.5rem);
  line-height:1.02;letter-spacing:-.025em;max-width:22ch;text-wrap:balance;color:inherit}
.closer p{font-size:.95rem;max-width:52ch;opacity:.84;color:inherit}
.closer .sig{font-family:var(--mono);font-size:.7rem;letter-spacing:.06em;opacity:.7;
  padding-top:.8rem;border-top:1px solid currentColor}
@media(max-height:760px){
  .closer__wm{width:min(340px,58vw)}
  .closer h2{font-size:clamp(1.2rem,2.6vw,1.7rem)}
  .closer p:not(.sig){display:none}}
@media(max-width:760px){
  .closer__rail{display:none}
  .closer__end{gap:.6rem}
  html.js .closer__track{height:230vh}}
/* still frames: no script, reduced motion, print */
html:not(.js) .closer__flood,html:not(.js) .closer__grid{transform:none}
html:not(.js) .closer__grid{display:none}
html:not(.js) .closer__end{opacity:1;transform:none}
html:not(.js) .closer__rail{display:none}
@media(prefers-reduced-motion:reduce){
  html.js .closer__track{height:auto}
  html.js .closer__stage{position:static;height:auto;min-height:min(94vh,780px);
    padding-block:clamp(3rem,9vh,6rem);background:var(--red)}
  html.js .closer__flood,html.js .closer__grid{display:none}
  html.js .closer__end{position:relative;bottom:auto;opacity:1;transform:none;
    margin-top:clamp(1.6rem,5vh,3rem)}
  html.js .closer__rail{display:none}
  html.js .closer__wm > span{transition:none}
  html.js .closer .wmdot{transform:none}}


/* ── smaller screens ──────────────────────────────────────────────────────
   The document keeps every word; what changes is how much room each part is
   given and how wide type is set. Nothing is hidden that carries meaning. */
@media(max-width:1000px){
  .top__in{gap:.4rem 1rem;padding-block:.35rem}
  .nav{width:100%;margin-left:0;flex-wrap:nowrap;overflow-x:auto;gap:1.15rem;
    scrollbar-width:none;-ms-overflow-style:none;
    padding-bottom:.15rem;scroll-snap-type:x proximity}
  .nav::-webkit-scrollbar{display:none}
  .nav button{scroll-snap-align:start}
  .top .matur{width:78px;height:17px}
}
@media(max-width:900px){
  .hero__in,.cover__in{grid-template-columns:1fr}
  .hero__t,.hero--flip .hero__t{order:2;margin:0;max-width:none;
    padding:clamp(1.8rem,6vw,2.6rem) var(--pad) clamp(2.2rem,7vw,3rem)}
  .hero__img,.hero--flip .hero__img{order:1;padding:1.4rem var(--pad)}
  .hero__img .im{max-height:52vh}
  .hero__ix{font-size:clamp(4.4rem,26vw,8rem)}
  .hero__nm{font-size:clamp(1.9rem,9vw,3rem);max-width:none}
  .act__in{align-items:start}
}
@media(max-width:760px){
  body{font-size:15px;line-height:1.62}
  .p{max-width:none}
  .cover .lede{font-size:1rem}
  .cover__in{gap:1.6rem}
  .cover__r{order:-1;padding:1.6rem var(--pad)}
  .cover__t{padding:2rem var(--pad) 2.6rem}
  .cover__r .im{max-height:46vh;background-position:center}
  .cover h1{font-size:clamp(3.6rem,20vw,6rem)}
  .cover .cap{font-size:clamp(1.15rem,5.6vw,1.6rem);max-width:none}
  .cover__meta{gap:.9rem 1.2rem}
  .sp__ix{font-size:clamp(4.2rem,22vw,7rem)}
  .sp__meta div{grid-template-columns:6.4rem minmax(0,1fr);gap:.7rem}
  .sp__meta dd{font-size:.9rem}
  .toc .th{height:58px}.toc .th .im{height:58px;width:82px}
  .toc a{padding:.85rem 0}
  .cwl .nm{font-size:.9rem;min-width:0}
  .cwl .cd{flex:0 0 auto;font-size:.58rem}
  .gal__stage{aspect-ratio:var(--sr,.78)}
  .strip{gap:1.1rem 1.4rem}
  .strip button{width:50px;height:60px}
  .strip button .im{height:54px;width:44px}
  .rail__l{font-size:.53rem;letter-spacing:.1em}
  .rail{gap:.4rem}
  .due .d{text-align:left;flex:1 1 100%}
  .dfoot{gap:.4rem;flex-direction:column}
  .mast__r{text-align:left;padding-top:.8rem}
  .mast__r svg{margin-left:0}
  .ph3__tex{min-height:84px;padding:1.1rem}
  pre.code{font-size:.66rem;padding:1rem}
}
@media(max-width:620px){
  .e{grid-template-columns:3.1rem 20px minmax(0,1fr)}
  .e__d{padding:1.6rem .55rem 0 0}
  .e__d .dd{font-size:1.3rem}
  .e__d .mm{font-size:.5rem;letter-spacing:.08em}
  .e__d .yr{display:none}
  .e__s .mk{top:1.6rem}
  .e__b{padding:1.45rem 0 1.9rem}
  .e__h{font-size:1.15rem;max-width:none}
  .lbx{padding:.75rem}
  .lbx__box{height:66vh}
  .lbx__a{font-size:1.6rem;padding:.5rem}
  .lbx__x{top:.5rem;right:.7rem;font-size:.6rem}
  .lbx__bar{gap:.7rem;margin-top:.8rem}
  .gal__hint{color:var(--g2);font-size:.55rem}
  .sign{gap:1.6rem}
}
/* wide tables scroll; the fading edge says so without adding a label */
@media(max-width:820px){
  .tw{-webkit-mask-image:linear-gradient(90deg,#000 calc(100% - 26px),transparent);
      mask-image:linear-gradient(90deg,#000 calc(100% - 26px),transparent)}
}

/* ── print ────────────────────────────────────────────────────────────────── */
@page{size:A4;margin:13mm}
@media print{
  .top,.prog,.pick,.strip,.sws,.golink,.lbx,.nav{display:none!important}
  body{background:#fff;font-size:10.4pt}
  .panel:not(.active){display:none}
  .doc{padding:0;max-width:none}
  .styl{display:block!important}
  .styl + .styl{page-break-before:always}
  .sec--rule,.tw,table.t tr,.e,.dec,.alr,.sp,figure{page-break-inside:avoid}
  .band,.sp{page-break-before:always}
  .band::before,.reg--sketched .band::before{display:none}
  .ink,.field--ink,.field--red,.hero,.act,.hero__img{background:#fff!important;color:#000!important}
  .field--ink *,.field--red *,.hero *,.act *{color:#000!important}
  .outline,.field--ink .outline{-webkit-text-stroke:0;color:#000!important}
  .act__tex,.bleed{width:auto;margin-left:0}
  .acts,html.js .acts{height:auto!important}
  .acts__stage,html.js .acts__stage{position:static!important;height:auto!important;
    background:#fff!important;color:#000!important;overflow:visible}
  .acts__s,html.js .acts__s{opacity:1!important;transform:none!important;
    position:relative;grid-area:auto;margin-bottom:2rem}
  .acts__tex,.acts__rail,.door__cue,.door__grid,.notch{display:none!important}
  .sec--rule::before,.docopen__rl,.docopen__tk{transform:none!important}
  .shd__n,.shd__t{opacity:1!important;transform:none!important}
  .shd{page-break-after:avoid}
  .docopen h1 .wd i,.docopen .type,.docopen .who,.docopen__b,.closer__end{
    opacity:1!important;transform:none!important}
  .docopen__gh,.closer__rail,.closer__grid,.closer__flood{display:none!important}
  .closer__track,html.js .closer__track{height:auto!important}
  .closer__stage,html.js .closer__stage{position:static!important;height:auto!important;
    min-height:0!important;background:#fff!important;color:#000!important;overflow:visible}
  .closer__end{position:static!important;margin-top:1.4rem}
  .closer__wm > span:not(:last-child){display:none}
  .closer__wm > span:last-child{position:static;opacity:1!important}
  .closer__wm{width:210px}
  .closer .p-bo,.closer__wm svg path{fill:#000!important}
  .closer__stg span:not(.on){display:none}
  .door{min-height:0;page-break-after:always}
  .hero__in{min-height:0}
  .ink{background:#fff;color:#000}
  .ink .d2,.ink .d3,.chip .n{color:#000}
  .chip{background:#fff}
  .float{mix-blend-mode:normal}
  .im{-webkit-print-color-adjust:exact;print-color-adjust:exact}
  .gal__stage > figure{opacity:1!important;position:static;grid-area:auto}
  .gal__stage{display:grid;grid-template-columns:repeat(3,1fr);gap:.6rem;min-height:0;
    aspect-ratio:auto;transition:none}
  .gal__hint,.rail{display:none}
  .ph3__tex{background:none!important;border:1px solid #ccc}
  .ph3--born .p-ink{fill:#000}
  .gal__stage .im{height:auto;width:100%}
  .due,.ask,.apr--wait{border:1px solid #000}
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
    cws = "".join(f'<div><i style="background:{h}"></i><p class="c">{c}</p><p class="n">{n}</p></div>'
                  for c, n, h, _ in COLORWAYS)
    return f'<div class="cwrow">{cws}</div>'

def pay_flats(p):
    figs = "".join(
        f'<figure>{im(BY_NO[no]["img"], BY_NO[no]["name"] + " technical flat", "float")}'
        f'<figcaption>{no} &middot; {BY_NO[no]["short"]}</figcaption></figure>' for no in p["styles"])
    return f'<div class="gridimgs">{figs}</div>'

def pay_renders(p):
    figs = "".join(f'<figure>{im(k, cap, "float")}'
                   f'<figcaption>{cap}</figcaption></figure>' for k, cap in p["keys"])
    return f'<div class="gridimgs">{figs}</div>'

def pay_sample(p):
    figs = "".join(f'<figure class="ph">{im(k, cap)}'
                   f'<figcaption>{cap}</figcaption></figure>' for k, cap in p["keys"])
    cls = "vd" if p["ok"] else "vd no"
    return (f'<div class="gridimgs">{figs}</div>'
            f'<span class="{cls}">{mk("done" if p["ok"] else "now")} {p["round"]} &middot; {p["verdict"]}</span>')

def pay_measure(p):
    rows = "".join(
        f'<tr><td class="c">{sn}</td><td class="c">{code}</td><td>{name}</td>'
        f'<td class="n">{cm(spec)}</td><td class="n">{cm(got)}</td>'
        f'<td class="n out">{got - spec:+.2f}</td><td class="n">&plusmn;{cm(tol)}</td>'
        f'<td><span class="tag{" tag--r" if owner == "Pattern" or owner == "Block" else ""}">{owner}</span></td></tr>'
        for sn, code, name, spec, got, tol, owner in p["rows"])
    more = (f' &middot; {p["more"]} further points listed in the report' if p.get("more") else "")
    go = (f'<button class="golink" data-go="{p["go"]}">Full points of measure &rarr;</button>'
          if p.get("go") else "")
    return f"""<div>
 <div class="meas__h"><span>Out of tolerance &middot; <b>{p['session']}</b></span>
   <span>Measured against <b>{p['spec']}</b></span></div>
 <div class="tw"><table class="t" style="min-width:600px"><thead><tr>
   <th>Style</th><th>Code</th><th>Point of measure</th><th class="n">Spec</th>
   <th class="n">Got</th><th class="n">Dev.</th><th class="n">Tol.</th><th>Cause</th>
  </tr></thead><tbody>{rows}</tbody></table></div>
 <div class="meas__f"><span class="clear">{mk('done')} <b>{p['clear']} of {p['total']}</b>
   points measured clean{more}</span>{go}</div>
</div>"""

def pay_release(p):
    go = (f'<button class="golink" data-go="{p["go"]}">Open &rarr;</button>' if p.get("go") else "")
    rev = f' &middot; {p["rev"]}' if p.get("rev") and p["rev"] != "—" else ""
    return f"""<div class="rel"><span class="nm">{p['name']}{rev}
  <span class="nt">{p.get('note','')}</span></span>{go}</div>"""

def pay_approval(p):
    wait = p["status"] == "waiting"
    return f"""<div class="apr{' apr--wait' if wait else ''}">{mk('next' if wait else 'done')}
 <div><p class="lb">{'Waiting on you' if wait else 'Approved'}</p>
  <p class="v">{p['what']}</p>
  <p class="wq">{p['who']} &middot; {'by ' if wait else ''}{date(p['when'])}</p></div></div>"""

def pay_alert(p):
    return f"""<div class="alr">
 <div class="r"><p class="lb">The risk</p><p>{p['risk']}</p></div>
 <div><p class="lb">What removes it</p><p>{p['fix']}</p></div>
 <p class="ow">{p['owner']}</p></div>"""

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

TSTATE = {"sketched": "t-sketch", "stitched": "t-stitch", "born": "t-born"}

def band(key):
    r = REGISTERS[key]
    ph = next(p for p in PHASES if p["key"] == key)
    logo = {"sketched": SVG["state_sketch"], "stitched": SVG["state_stitch"],
            "born": SVG["state_born"]}[key]
    red = ' field--red' if key == 'born' else ''
    return f"""<div class="band{red}"><div class="tex" aria-hidden="true"></div><div class="w band__in">
 <div><p class="n">Phase {r['n']}</p><h2 class="d2 {TSTATE[key]}">{r['name']}</h2>
   <p class="ln">{r['line']}</p><div class="lg">{logo}</div></div>
 <div><p class="df">{r['defn']}</p>
   <p class="win">{ph['title']} &middot; {ph['window']}</p></div>
</div></div>"""

def logbook():
    out = []
    for key in ["sketched", "stitched", "born"]:
        rows = "".join(entry(e) for e in ENTRIES if e["phase"] == key)
        out.append(f'<section class="reg reg--{key} ph-{key}" data-phase-region="{key}">'
                   f'{band(key)}<div class="log w">{rows}</div></section>')
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
    return f"""<div class="w stand"><div class="stand__g">
 <div>
  <p class="m m--r">Logbook &middot; {PROJECT['client_long']}</p>
  <h1 class="d2">{now['title'].rstrip('.')}</h1>
  <p class="sub">{PROJECT['capsule']} &middot; {PROJECT['drop']}. Six styles, five colour
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

DOCS = [("range", "The range"), ("logbook", "Logbook"), ("techpack", "Tech pack"),
        ("fitting", "Fitting"), ("handover", "Handover"), ("system", "System")]

def top():
    tabs = "".join(
        f'<button role="tab" id="t-{k}" aria-controls="p-{k}" data-doc="{k}" '
        f'aria-selected="{"true" if i == 0 else "false"}">{lbl}</button>'
        for i, (k, lbl) in enumerate(DOCS))
    return f"""<header class="top"><div class="prog" id="prog" aria-hidden="true"></div>
<div class="top__in">
 <span class="mk-w matur" id="matur" aria-label="BORN Studio">
  <span data-i="0">{SVG['state_sketch']}</span>
  <span data-i="1">{SVG['state_stitch']}</span>
  <span data-i="2" class="on">{SVG['wm_solo']}</span>
 </span>
 <p class="pnow" id="pnow" aria-live="polite"><span class="pnow__ln"></span>
  {mk('next')}<b>Sketched</b></p>
 <nav class="nav" role="tablist" aria-label="Sections">{tabs}
  <button class="pr" id="printBtn" type="button">Print</button>
  <span class="notch" id="notch" role="slider" tabindex="0" aria-label="Section marker"
   aria-valuemin="1" aria-valuemax="{len(DOCS)}" aria-valuenow="1"></span></nav>
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
DOC_PHASE = {"techpack": ("sketched", "The specification the factory builds from"),
             "fitting": ("stitched", "Measured against thread and needle"),
             "billing": ("stitched", "Billed as the work is made"),
             "handover": ("born", "Everything transfers, and the project closes")}

def pstrip(doc):
    """A document belongs to a phase. It says so, in the phase's own line."""
    key, note = DOC_PHASE[doc]
    r = REGISTERS[key]
    st = {"sketched": "next", "stitched": "now", "born": "done"}[key]
    return (f'<div class="pstrip">{mk(st)}<b>{r["name"]}</b>'
            f'<span>Phase {r["n"]} &middot; {r["line"]}</span>'
            f'<span class="pstrip__t">{note}</span></div>')

# ════════════════════════════════════════════════════════ section heads ═══
_EYE = _re.compile(r'<div class="(sec(?: sec--rule)?)">\s*<p class="eyebrow">(.*?)</p>',
                   _re.S)

def heads(html, key):
    """Promote a document's own section labels to section heads. The label is
    written once, in one place, as plain text; the count, the phase colour and
    the split between name and qualifier are the system's business, not the
    content's. The count is a CSS counter rather than a number written into
    the markup, because a tech pack shows one style at a time: a section that
    is not on screen must not take a number, or the reader watches the count
    jump when they change style. The section also takes the phase the document
    is written in, so
    the rule it opens on is drawn in that phase's own line — dotted while the
    work is being sketched, stitch-dashed while it is being fitted, solid once
    it is BORN. Only a label that opens a section is touched; the ones that
    caption a garment or a spread are left as they are."""
    def one(m):
        bits = m.group(2).split("&middot;", 1)
        q = f'<span class="shd__q">{bits[1].strip()}</span>' if len(bits) > 1 else ""
        return (f'<div class="{m.group(1)} ph-{key}">'
                f'<div class="shd"><i class="shd__n" aria-hidden="true"></i>'
                f'<p class="shd__t">{bits[0].strip()}{q}</p></div>')
    return _EYE.sub(one, html)

def masthead(doctype, title, meta, doc=None, red=False):
    """Documents open the way the garments do — a full-bleed field, the title at
    poster scale, and the phase the document belongs to stated in its own line.
    The phase numeral stands behind the title at cover scale and drifts against
    the scroll; the title arrives a word at a time and then stops. Everything a
    reader has to read is still by the time they are reading it."""
    rows = "".join(f"<div>{k} <b>{v}</b></div>" for k, v in meta)
    field = "field--red docopen--red" if red else "field--ink"
    ghost = ""
    if doc:
        r = REGISTERS[DOC_PHASE[doc][0]]
        ghost = (f'<div class="docopen__gh" aria-hidden="true">'
                 f'<b>{r["n"]}</b><span>{r["name"]}</span></div>')
    words = " ".join(f'<span class="wd"><i>{w}</i></span>' for w in title.split(" "))
    return f"""<div class="docopen bleed {field}" data-open>{ghost}<div class="doc docopen__in">
 <p class="type"><i class="docopen__tk"></i>{doctype}</p>
 <h1>{words}</h1>
 <p class="who">{PROJECT['client_long']} &middot; {PROJECT['capsule']} &middot; {PROJECT['drop']}</p>
 <div class="docopen__rl"></div>
 <div class="docopen__b">{pstrip(doc) if doc else '<span></span>'}
  <div class="docopen__m">{rows}</div></div>
</div></div>"""

ON = ' class="on"'   # f-strings cannot hold a backslash, so the quotes live here

# The finished logotype, set for a red ground, with the dot on a handle of its
# own so it can be made to land at the end of the sequence.
FINAL_WM = SVG["wm_solo_onred"].replace(
    '<path fill="#1B1720"', '<g class="wmdot"><path fill="#1B1720"', 1)
assert FINAL_WM.count('<g class="wmdot">') == 1
FINAL_WM = FINAL_WM.replace("/></svg>", "/></g></svg>", 1)
# on red the hatch has to be cut in paper, not in ink
STITCH_WM = SVG["state_stitch"].replace("url(#hatch)", "url(#hatch-d)")

def closer(line, note, frm="var(--paper)"):
    """The end of a document is the end of the studio's sentence, and the
    scrollbar reads it out: Rojo Valentino floods up over the graph paper, the
    mark is drawn, then stitched, then set solid, and the last thing standing is
    the finished logotype — BORN, with its dot landing on the end of it. Hold
    the scroll and the sequence holds; scroll back and it runs backwards."""
    stages = [("01", "Sketched"), ("02", "Stitched"), ("03", "BORN"),
              ("", "From idea to life")]
    rail = "".join(f"<b data-r=\"{i}\">{n or '&mdash;'}</b>"
                   for i, (n, _) in enumerate(stages))
    names = "".join(
        f'<span data-s="{i}"{ON if i == 3 else ""}>'
        f'{f"<i>{n}</i>" if n else ""}{t}</span>'
        for i, (n, t) in enumerate(stages))
    return f"""<div class="closer bleed" data-closer style="--from:{frm}">
 <div class="closer__track"><div class="closer__stage">
  <div class="closer__flood" aria-hidden="true"></div>
  <div class="closer__grid" aria-hidden="true"></div>
  <div class="closer__rail" aria-hidden="true">{rail}</div>
  <div class="closer__in">
   <div class="closer__wm" aria-label="Sketched, stitched, BORN.">
    <span data-i="0">{SVG['state_sketch']}</span>
    <span data-i="1">{STITCH_WM}</span>
    <span data-i="2">{SVG['state_born']}</span>
    <span data-i="3" class="on">{FINAL_WM}</span>
   </div>
   <p class="closer__stg">{names}</p>
  </div>
  <div class="closer__end">
   <h2>{line}</h2>
   <p>{note}</p>
   <p class="sig">{PROJECT['studio_long']} &middot; {PROJECT['ref']}</p>
  </div>
 </div></div>
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
    return f"""<section class="panel ph-stitched" data-phase-region="stitched" id="p-billing" role="tabpanel" aria-labelledby="t-billing">
 {masthead("Quote", "Development of a six-style capsule",
            [("No.", QUOTE["no"]), ("Issued", date(QUOTE["issued"])), ("Valid to", date(QUOTE["valid"]))], "billing")}
 <div class="doc"><div class="sheet">
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
 </div></div>"""

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
    return f"""{masthead("Invoice", INVOICE["milestone"],
            [("No.", INVOICE["no"]), ("Issued", date(INVOICE["issued"])), ("Due", date(INVOICE["due"]))],
            "billing", red=True)}
 <div class="doc"><div class="sheet">
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

  </div></div>
 <div class="duefield bleed field--red"><div class="doc duefield__in">
   <div><p class="l">Amount due</p><p class="v">{money(tot)}</p></div>
   <p class="d">Payable by {date(INVOICE['due'])}<br>{PROJECT['terms']} from the issue date<br>
    Overdue balances accrue 1.5% per month</p>
 </div></div>
 <div class="doc"><div class="sheet">

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
 {closer("Made to be BORN.", "Milestone three issues at ex-factory. Quote the invoice reference on the transfer so it reconciles against the right milestone.")}"""

# ═══════════════════════════════════════════════════════════════ tech pack ═══
def techpack():
    chips = "".join(f'<button class="pk" data-s="{s["no"]}" aria-pressed="false">{s["no"]}</button>'
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
  <div class="plate">{im(s['img'], s['name'] + " — technical flat with callouts", "float")}</div>
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
    return f"""<section class="panel ph-sketched" data-phase-region="sketched" id="p-techpack" role="tabpanel" aria-labelledby="t-techpack">
 {masthead("Tech pack", "Factory-ready specification",
            [("Revision", "v2.0"), ("Released", date("2026-08-14")), ("Styles", "6")], "techpack")}
 <div class="doc"><div class="sheet">
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
   <div class="pick" role="group" aria-label="Style">{chips}</div>
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
 {closer("Sew to the spec,<br>not to the sketch.", "Where the two disagree the points of measure win, and BORN gets a call before anything is cut.")}
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
        cards = "".join(
            f'<figure class="ph">{im(k, s["no"] + " sample")}'
            f'<figcaption>{cap}</figcaption></figure>' for k, cap in s["photos"][:2])
        photos = f'<div class="gridimgs" style="margin-top:1.1rem;max-width:360px">{cards}</div>' 
        detail.append(f"""<div class="styl" data-s="{s['no']}">
 <p class="eyebrow">{s['no']} &middot; {s['cat']}</p><h2 class="h">{s['short']}</h2>
 {photos}
 <div class="tw" style="margin-top:1.1rem"><table class="t"><thead><tr><th>Code</th>
  <th>Point of measure</th><th class="n">Spec</th><th class="n">Measured</th>
  <th class="n">Dev.</th><th class="n">Tol.</th><th>Verdict</th></tr></thead>
  <tbody>{body}</tbody></table></div>
</div>""")
    chips = "".join(f'<button class="pk" data-s="{s["no"]}" aria-pressed="false">{s["no"]}</button>'
                    for s in STYLES)
    corr = "".join(
        f'<li><b>{BY_NO[sn]["short"]} &middot; {sn}{"" if pt == "—" else " &middot; " + pt}</b><br>{txt}'
        f'<br><span class="c" style="color:var(--red)">{owner}</span></li>'
        for sn, pt, txt, owner in FITTING["corrections"])
    holds = "".join(f'<li>{h}</li>' for h in FITTING["holds"])
    return f"""<section class="panel ph-stitched" data-phase-region="stitched" id="p-fitting" role="tabpanel" aria-labelledby="t-fitting">
 {masthead("Fitting report", f"{FITTING['sample']} &middot; fit session 02",
            [("No.", FITTING["no"]), ("Session", date(FITTING["session"])), ("Size", FITTING["size"])], "fitting")}
 <div class="doc"><div class="sheet">
  {dl([("Sample round", FITTING["sample"]), ("Received", date(FITTING["received"])),
       ("Measured against", FITTING["spec"]), ("Form", FITTING["form"]),
       ("Present", FITTING["present"]), ("Styles fitted", "6")])}

  </div></div>
 <div class="vfield bleed field--ink"><div class="doc vfield__in">
   <div><p class="l">Verdict</p><h2>{FITTING['verdict']}</h2></div>
   <p>{FITTING['verdict_note']}</p>
 </div></div>
 <div class="doc"><div class="sheet">

  <div class="sec sec--rule"><p class="eyebrow">Across the range</p>
   <div class="tw"><table class="t"><thead><tr><th>Style no.</th><th>Style</th>
    <th class="n">Points</th><th class="n">Out of tol.</th><th>Verdict</th></tr></thead>
    <tbody>{''.join(summary)}</tbody></table></div>
  </div>

  <div class="sec sec--rule"><p class="eyebrow">Measured &middot; select a style</p>
   <div class="pick" role="group" aria-label="Style">{chips}</div>
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
 {closer("Corrected,<br>and approved to size set.", "Three pattern corrections and two factory settings. No third sample round, and the ex-factory date holds.")}
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
        f'<figure>{im(k, cap, "float")}'
        f'<figcaption>{cap}</figcaption></figure>'
        for k, cap in [("render_periwinkle", "17-3919 Purple Impression"),
                       ("render_whisper", "11-0701 Whisper White"),
                       ("render_black", "19-3911 Black Beauty"),
                       ("render_blue", "17-3919 · jacket and short")])
    return f"""<section class="panel ph-born" data-phase-region="born" id="p-handover" role="tabpanel" aria-labelledby="t-handover">
 {masthead("Handover", "What LAYO owns at the end",
            [("No.", HANDOVER["no"]), ("Issues", date(HANDOVER["due"])), ("Status", HANDOVER["status"])], "handover", red=True)}
 <div class="doc"><div class="sheet">
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
   <div class="gridimgs">{renders}</div>
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
 {closer("Everything is made<br>to be BORN.", "Patterns, specifications, supplier references, colour approvals and the full development record. Nothing is held back.")}
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
 {masthead("The system", "How a room is built",
            [("For", "BORN Studio"), ("Version", "1.0"), ("Applies to", "Every project")])}
 <div class="doc"><div class="sheet">
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
 {closer("One studio,<br>every project.", "Copy the content file, replace the project, and the room opens for the next client in the same language.")}
</section>"""


# ═════════════════════════════════════════════════════════════════ the range ═
# Every image the studio produced for this capsule, arranged the way the work
# was actually done: the drawing, the colourways it was drawn in, the
# visualisation, and finally the garment as it came off the line. The gallery
# navigation is the process — Drawn, Coloured, Visualised, Born.

def views(st):
    """(group label, [(image key, caption, is_photograph)])"""
    return [
     ("Drawn",      "sketched", [(st["img"], "Technical flat &middot; front, back and side", False)]),
     ("Coloured",   "sketched", [(k, f"{nm} &middot; {code}", False) for k, code, nm, _ in st["colourways"]]),
     ("Visualised", "sketched", [(k, f"{nm} &middot; 3D visualisation", False) for k, nm in st["renders"]]),
     ("Sampled",    "stitched", [(k, f"SMS 2 &middot; {cap}", True) for k, cap in st["photos"]]),
    ]

def phase_rail():
    """Three nodes on a rule. The view you are looking at lights its own phase, so
    every image says which state of the craft it came out of."""
    n = ""
    for i, key in enumerate(("sketched", "stitched", "born")):
        r = REGISTERS[key]
        n += (f'<span class="rail__n" data-p="{key}">{mk("next", r["name"])}'
              f'<span class="rail__l">{r["name"]}</span></span>')
        if i < 2: n += '<span class="rail__r"></span>'
    return f'<div class="rail" aria-hidden="true">{n}</div>'

def gallery(st, gid):
    figs, thumbs, i = [], [], 0
    for label, phase, items in views(st):
        if not items: continue
        buttons = ""
        for key, cap, photo in items:
            alt = f'{st["short"]} — {cap}'
            figs.append(
                f'<figure class="{"on" if i == 0 else ""}{" ph" if photo else ""}" '
                f'data-i="{i}" data-phase="{phase}">'
                f'{im(key, alt, "" if photo else "float")}'
                f'<figcaption>{cap}</figcaption></figure>')
            buttons += (f'<button data-g="{gid}" data-i="{i}" '
                        f'aria-pressed="{"true" if i == 0 else "false"}" title="{cap}">'
                        f'{im(key, "", "th")}</button>')
            i += 1
        thumbs.append(f'<div class="strip__g"><p class="m">{label}</p>'
                      f'<div class="strip__t">{buttons}</div></div>')
    return (f'<div class="gal" data-gal="{gid}">'
            f'<div class="gal__stage" data-stage="{gid}" role="button" tabindex="0" '
            f'aria-label="Open this view full size">{"".join(figs)}</div>'
            f'<p class="gal__hint">Open full size to zoom in on the construction</p>'
            f'{phase_rail()}'
            f'<div class="strip">{"".join(thumbs)}</div></div>')

def hero(st, n):
    """A poster that seduces, sitting on a sheet that specifies. The side the
    garment takes alternates down the document, so the rhythm never settles."""
    flip = n % 2 == 0
    q = st["fabric"].split(" · ")
    nm = st["short"].upper()
    spec = " &nbsp;·&nbsp; ".join([f"<b>{st['no']}</b>", st["cat"], q[1], q[2],
                                   f"{PROJECT['size_range']}"])
    return f"""<div class="hero bleed field--ink{' hero--flip' if flip else ''}">
 <div class="hero__in">
  <div class="hero__t">
   <p class="hero__ix">{n:02d}<span style="color:var(--red)">.</span></p>
   <h2 class="hero__nm outline">{nm}</h2>
   <p class="hero__full">{st['name']}</p>
   <p class="hero__sub">{st['hand']}.</p>
   <p class="hero__spec">{spec}<br>{q[0]}</p>
  </div>
  <div class="hero__img">{im(st['renders'][0][0], st['name'], 'float')}</div>
 </div>
</div>"""

def spread(st, n):
    calls = "".join(f'<li><span>{j+1:02d}</span>{d}</li>' for j, d in enumerate(st["details"]))
    cwl = "".join(
        f'<li><i style="background:{hx}"></i><span class="nm">{nm}</span>'
        f'<span class="cd">{code}</span></li>' for _, code, nm, hx in st["colourways"])
    return f"""<section class="sp{' sp--flip' if n % 2 == 0 else ''} ph-sketched"
 data-phase-region="sketched" id="s-{st['no']}">
 {hero(st, n)}
 <div class="w pband">
  <span class="pband__ln"></span>
  <span class="pband__p" data-p="sketched">{mk('next')}<b>Sketched</b>
   <span>Drawn, coloured, visualised &mdash; nothing cut yet</span></span>
  <span class="pband__p" data-p="stitched">{mk('now')}<b>Stitched</b>
   <span>The garment exists and is being measured</span></span>
  <span class="pband__p" data-p="born">{mk('done')}<b>BORN</b>
   <span>It goes out into the world</span></span>
 </div>
 <div class="w sp__body">
  <div><p class="p">{st['hand']}.</p>
   <p class="m" style="margin-top:1.7rem">Construction</p>
   <ul class="calls">{calls}</ul>
   <p class="m" style="margin-top:1.7rem">Colourways</p>
   <ul class="cwl">{cwl}</ul></div>
  <div>{gallery(st, st['no'])}</div>
 </div>
</section>"""

PHASE_WORK = {
 "sketched": ("Material selection, technical sketches with construction callouts, colour "
              "development against physical chips, 3D visualisation, and a factory-ready "
              "tech pack.", "1–3 weeks"),
 "stitched": ("Factory pairing, lab dip management, sample rounds with documented fit "
              "sessions, and tech pack revisions carried through to the approved sample.",
              "2–6 months"),
 "born":     ("Size set and PPS sign-off, bulk oversight, inline QC, final AQL inspection "
              "and a documented handover with the full production archive.", "4–8 weeks"),
}

def door():
    """What this is, before whose it is. The mark matures on arrival — sketched,
    stitched, born — which is the studio's whole argument in three seconds."""
    ph = "".join(
        f'<span>{mk(st)}{REGISTERS[k]["name"]}</span>' + ('<i></i>' if k != "born" else "")
        for k, st in (("sketched", "next"), ("stitched", "now"), ("born", "done")))
    return f"""<div class="w door">
 <div class="door__grid" aria-hidden="true"></div>
 <div class="door__wm" id="doorwm" aria-label="BORN Studio">
  <span data-i="0">{SVG['state_sketch']}</span>
  <span data-i="1">{SVG['state_stitch']}</span>
  <span data-i="2" class="on">{SVG['wm_solo']}</span>
 </div>
 <p class="m m--r">{PROJECT['studio_long']}</p>
 <h1>The Project Room</h1>
 <p class="lede">One link that holds the whole development. Every decision, every sample and
  every measurement, with the date it happened and the reason behind it.</p>
 <p class="door__ph">{ph}</p>
 <p class="door__cue"><b></b>Scroll to open {PROJECT['client']}</p>
</div>"""

def process():
    """Paper, then ink, then Rojo Valentino. The colour of the ground is the
    argument: an idea on paper, tested in the dark, born in colour."""
    slides, rail = "", ""
    for i, key in enumerate(("sketched", "stitched", "born")):
        r = REGISTERS[key]
        ph = next(p for p in PHASES if p["key"] == key)
        work, span = PHASE_WORK[key]
        live, done = ph["state"] == "stitched", ph["state"] == "born"
        state = "done" if done else ("now" if live else "next")
        where = "Complete" if done else "Where the capsule is now" if live else "Ahead"
        logo = {"sketched": SVG["state_sketch"], "stitched": SVG["state_stitch"],
                "born": SVG["state_born"]}[key]
        slides += f"""<div class="acts__s{' on' if i == 0 else ''}" data-i="{i}" data-phase="{key}">
 <div><p class="acts__n">{r['n']}</p><h3 class="acts__nm {TSTATE[key]}">{r['name']}</h3>
  <p class="acts__ln">{r['line']}</p><div class="acts__lg">{logo}</div></div>
 <div><p class="acts__body">{work}</p>
  <p class="acts__f">{mk(state)}<span>{where}</span><span class="wk">{span}</span></p></div>
</div>"""
        on = ' class="on"' if i == 0 else ''
        rail += (f'<span data-i="{i}"{on}>{mk(state)}{r["name"]}</span>'
                 + ("<i></i>" if i < 2 else ""))
    acts = f"""<section class="acts bleed" id="acts">
 <div class="acts__stage" id="actstage">
  <div class="acts__tex acts__tex--grid" data-tex="0" aria-hidden="true"></div>
  <div class="acts__tex acts__tex--hatch" data-tex="1" aria-hidden="true"></div>
  <div class="w acts__in">{slides}</div>
  <div class="w acts__rail" id="actrail">{rail}</div>
 </div>
</section>"""
    return f"""<div class="w proc">
 <div class="proc__h">
  <div>{GRAIN}<p class="m m--r">The process</p>
   <h2 class="d2">Every garment<br>lives three states.</h2></div>
  <p class="p">The mark changes with the phase &mdash; outline while it is being drawn,
   topstitch while it is being tested, solid and in colour once it goes out into the
   world. So does the ground you are reading it on. <b>Keep scrolling and you will watch
   it happen.</b></p>
 </div>
</div>{acts}"""

def range_panel():
    toc = "".join(
        f'<a href="#s-{st["no"]}"><span class="ix">{n:02d}</span>'
        f'<span><span class="nm">{st["short"]}</span><span class="no">{st["no"]}</span></span>'
        f'<span class="cat">{st["cat"]}</span>'
        f'<span class="th">{im(st["renders"][0][0], "", "th float")}</span></a>'
        for n, st in enumerate(STYLES, 1))
    chips = "".join(
        f'<div class="chip"><i style="background:{h}"></i><div class="b">'
        f'<p class="c">{c}</p><p class="n">{nm}</p></div></div>'
        for c, nm, h, _ in COLORWAYS)
    spreads = "".join(spread(st, n) for n, st in enumerate(STYLES, 1))
    return f"""<section class="panel active" id="p-range" role="tabpanel" aria-labelledby="t-range">
{door()}{process()}
 <div class="cover bleed field--ink"><div class="cover__in">
  <div class="cover__t">
   <p class="m m--r">{PROJECT['studio_long']}</p>
   <h1 class="d1">{PROJECT['client']}</h1>
   <p class="cap">{PROJECT['capsule']}</p>
   <p class="p lede">Six styles, five colour standards, {PROJECT['units']:,} units.
    Drawn, coloured, visualised and made &mdash; every drawing, every colourway and every
    sample photograph the studio produced for this capsule is in this document.</p>
   <dl class="cover__meta">
    <div><dt>Drop</dt><dd>{PROJECT['drop']}</dd></div>
    <div><dt>Reference</dt><dd>{PROJECT['ref']}</dd></div>
    <div><dt>Opened</dt><dd>{date(PROJECT['opened'])}</dd></div>
    <div><dt>Ex-factory</dt><dd>{date(PROJECT['exfactory'])}</dd></div>
    <div><dt>Size range</dt><dd>{PROJECT['size_range']}</dd></div>
   </dl>
  </div>
  <div class="cover__r">{im('render_motion',
    'Jester Red bra top and leggings, 3D visualisation in motion', 'float')}</div>
 </div></div>

 <div class="w toc">
  <div class="toc__h"><div>{GRAIN}<h2 class="d3">The range</h2></div><p class="m">Six styles &middot; {PROJECT['drop']}</p></div>
  {toc}
 </div>
{spreads}

 <div class="ink"><div class="w">
  <p class="m m--r">Colour</p>
  <h2 class="d2">Five standards,<br>approved to chip.</h2>
  <p class="p" style="margin-top:1.1rem">Chosen against physical Pantone chips under D65 and
   carried through every lab dip. The values printed here are a screen reference and never an
   approval &mdash; the chip is.</p>
  <div class="chips">{chips}</div>
 </div></div>
 {closer('Sketched. Stitched. <span style="opacity:.72">BORN.</span>',
   'Six styles drawn, coloured, visualised and made. Every image the studio produced for this capsule is in this document.',
   'var(--ink)')}
</section>"""

# ══════════════════════════════════════════════════════════════════════ JS ═══
JS = r"""<script>
(function(){
  document.documentElement.classList.add('js');
  var $=function(q,c){return (c||document).querySelector(q);},
      $$=function(q,c){return [].slice.call((c||document).querySelectorAll(q));};

  // ── sections ───────────────────────────────────────────────────────────────
  var tabs=$$('.nav [data-doc]');
  function show(key,keep){
    var found=false;
    tabs.forEach(function(t){
      var on=t.dataset.doc===key; if(on)found=true;
      t.setAttribute('aria-selected',on?'true':'false');
      var p=document.getElementById('p-'+t.dataset.doc);
      if(p)p.classList.toggle('active',on);
    });
    if(!found)return;
    history.replaceState(null,'','#'+key);
    setTimeout(function(){readPhase();settle();paintReveal();paintFlood();},40);
    if(!keep)window.scrollTo(0,0);
  }
  tabs.forEach(function(t){t.addEventListener('click',function(){show(t.dataset.doc);});});
  tabs.forEach(function(t,i){t.addEventListener('keydown',function(e){
    var d=e.key==='ArrowRight'?1:e.key==='ArrowLeft'?-1:0;
    if(!d)return;e.preventDefault();
    var n=tabs[(i+d+tabs.length)%tabs.length];n.focus();show(n.dataset.doc);
  });});
  if(location.hash)show(location.hash.slice(1),true);
  setTimeout(readPhase,60);
  $$('[data-go]').forEach(function(b){
    b.addEventListener('click',function(){show(b.dataset.go);});
  });

  // ── scroll hairline, and the phase the reader is standing in ─────────────
  var prog=$('#prog'),pnow=$('#pnow'),PH=['sketched','stitched','born'],
      NAMES={sketched:'Sketched',stitched:'Stitched',born:'BORN'},
      MARKS={sketched:'next',stitched:'now',born:'done'},cur_ph='';
  function setPhase(k){
    if(k===cur_ph)return; cur_ph=k;
    PH.forEach(function(x){document.body.classList.toggle('ph-'+x,x===k);});
    if(!pnow)return;
    var b=$('b',pnow); if(b)b.textContent=NAMES[k]||'';
    pnow.style.visibility=k?'visible':'hidden';
    var m=$('.mk',pnow);
    if(m){var t=$('title',m); if(t)t.textContent=NAMES[k]||'';}
  }
  function readPhase(){
    var d=document.documentElement,h=d.scrollHeight-d.clientHeight;
    prog.style.width=(h>0?(d.scrollTop/h*100):0)+'%';
    // a whole document can belong to a phase, so the panel itself counts too
    var mark=innerHeight*0.34,best=null,
        act=$('.panel.active'),
        list=act?[].concat(act.matches('[data-phase-region]')?[act]:[],
                           $$('[data-phase-region]',act)):[];
    var last=null;
    list.forEach(function(e){
      var r=e.getBoundingClientRect();
      if(r.top<=mark&&r.bottom>mark)best=e;
      if(r.top<=mark)last=e;
    });
    best=best||last;
    setPhase(best?best.dataset.phaseRegion:'');
  }
  var tick=false;
  addEventListener('scroll',function(){
    if(tick)return; tick=true;
    requestAnimationFrame(function(){readPhase();tick=false;});
  },{passive:true});
  addEventListener('resize',readPhase,{passive:true});

  // ── the mark matures once, on load ────────────────────────────────────────
  var mat=$('#matur');
  if(mat&&!matchMedia('(prefers-reduced-motion: reduce)').matches){
    var st=$$('span',mat);
    st.forEach(function(d){d.classList.remove('on');});
    st[0].classList.add('on');
    [1,2].forEach(function(i){
      setTimeout(function(){st[i-1].classList.remove('on');st[i].classList.add('on');},620+i*560);
    });
  }

  // ── galleries: drawn · coloured · visualised · born ───────────────────────
  var GAL={};
  $$('.gal').forEach(function(g){
    var id=g.dataset.gal,
        figs=$$('.gal__stage > figure',g),
        btns=$$('.strip button',g);
    GAL[id]={figs:figs,i:0};
    var stage=$('.gal__stage',g),rail=$$('.rail__n',g),ORDER=['sketched','stitched','born'];
    function pick(n){
      n=(n+figs.length)%figs.length;
      GAL[id].i=n;
      figs.forEach(function(f,j){f.classList.toggle('on',j===n);});
      btns.forEach(function(b){b.setAttribute('aria-pressed',+b.dataset.i===n?'true':'false');});
      var f=figs[n],
          r=parseFloat(getComputedStyle($('.im',f)).getPropertyValue('--r'))||1;
      stage.style.setProperty('--sr',Math.min(1.75,Math.max(.66,r)));
      var at=ORDER.indexOf(f.dataset.phase),sec=g.closest('.sp');
      rail.forEach(function(nd,k){
        nd.classList.toggle('is-on',k===at);
        nd.classList.toggle('is-past',k<at);
      });
      if(sec){
        ORDER.forEach(function(k){sec.classList.remove('ph-'+k);});
        sec.classList.add('ph-'+f.dataset.phase);
        sec.dataset.phaseRegion=f.dataset.phase;
      }
    }
    btns.forEach(function(b){b.addEventListener('click',function(){pick(+b.dataset.i);});});
    GAL[id].pick=pick;
    pick(0);   // set the stage shape and the phase rail before the first click
  });

  // ── lightbox ──────────────────────────────────────────────────────────────
  var lb=$('#lb'),lbI=$('#lbI'),lbC=$('#lbC'),cur=null;
  var box=$('#lbBox'),zEl=$('#lbZ'),z=1,ox=0,oy=0,drag=null;
  function apply(){
    lbI.style.transform='translate('+ox+'px,'+oy+'px) scale('+z+')';
    zEl.textContent=Math.round(z*100)+'%';
    box.classList.toggle('zoomed',z>1);
  }
  function zoom(nz,cx,cy){
    nz=Math.min(6,Math.max(1,nz));
    var r=box.getBoundingClientRect();
    cx=(cx==null?r.width/2:cx-r.left)-r.width/2;
    cy=(cy==null?r.height/2:cy-r.top)-r.height/2;
    var k=nz/z;
    ox=cx-(cx-ox)*k; oy=cy-(cy-oy)*k;
    z=nz;
    if(z===1){ox=0;oy=0;}
    apply();
  }
  function openZoom(ir){
    // `contain` fits the whole image in; on a narrow screen a wide technical
    // flat then lands as a thin strip, so it opens filled to the height instead
    var r=box.getBoundingClientRect(),br=r.width/r.height;
    return ir/br > 1.5 ? Math.min(2.8,ir/br) : 1;
  }
  function paint(){
    var g=GAL[cur],f=g.figs[g.i],src=$('.im',f),
        ir=parseFloat(getComputedStyle(src).getPropertyValue('--r'))||1;
    lbI.className=src.className;
    lbI.setAttribute('aria-label',src.getAttribute('aria-label')||'');
    lbC.innerHTML=$('figcaption',f).innerHTML;
    ox=0;oy=0;z=openZoom(ir);apply();
  }
  $('#lbIn').addEventListener('click',function(e){e.stopPropagation();zoom(z*1.5);});
  $('#lbOut').addEventListener('click',function(e){e.stopPropagation();zoom(z/1.5);});
  box.addEventListener('wheel',function(e){
    e.preventDefault();zoom(z*(e.deltaY<0?1.18:1/1.18),e.clientX,e.clientY);
  },{passive:false});
  box.addEventListener('dblclick',function(e){zoom(z>1?1:2.6,e.clientX,e.clientY);});
  var pts={},pinch=null;
  function two(){var k=Object.keys(pts);return k.length===2?[pts[k[0]],pts[k[1]]]:null;}
  box.addEventListener('pointerdown',function(e){
    pts[e.pointerId]={x:e.clientX,y:e.clientY};
    box.setPointerCapture(e.pointerId);
    var t=two();
    if(t){
      drag=null;
      pinch={d:Math.hypot(t[0].x-t[1].x,t[0].y-t[1].y),z:z,
             cx:(t[0].x+t[1].x)/2,cy:(t[0].y+t[1].y)/2};
      return;
    }
    if(z>1){drag={x:e.clientX-ox,y:e.clientY-oy};box.classList.add('dragging');}
  });
  box.addEventListener('pointermove',function(e){
    if(pts[e.pointerId]){pts[e.pointerId].x=e.clientX;pts[e.pointerId].y=e.clientY;}
    var t=two();
    if(pinch&&t){
      var d=Math.hypot(t[0].x-t[1].x,t[0].y-t[1].y);
      if(pinch.d>0)zoom(pinch.z*(d/pinch.d),pinch.cx,pinch.cy);
      return;
    }
    if(!drag)return;ox=e.clientX-drag.x;oy=e.clientY-drag.y;apply();
  });
  ['pointerup','pointercancel','pointerleave'].forEach(function(t){
    box.addEventListener(t,function(e){
      delete pts[e.pointerId];
      if(Object.keys(pts).length<2)pinch=null;
      drag=null;box.classList.remove('dragging');
    });
  });
  function open(id){cur=id;lb.classList.add('on');document.body.style.overflow='hidden';
    paint();$('#lbX').focus();}
  function close(){lb.classList.remove('on');document.body.style.overflow='';cur=null;}
  function step(d){if(!cur)return;GAL[cur].pick(GAL[cur].i+d);paint();}
  $$('.gal__stage').forEach(function(st){
    st.addEventListener('click',function(e){
      if(e.target.closest('button'))return;
      open(st.dataset.stage);});
    st.addEventListener('keydown',function(e){
      if(e.key==='Enter'||e.key===' '){e.preventDefault();open(st.dataset.stage);}
    });
  });
  $('#lbX').addEventListener('click',close);
  $('#lbP').addEventListener('click',function(e){e.stopPropagation();step(-1);});
  $('#lbN').addEventListener('click',function(e){e.stopPropagation();step(1);});
  lb.addEventListener('click',function(e){if(e.target===lb)close();});
  addEventListener('keydown',function(e){
    if(!cur)return;
    if(e.key==='Escape')close();
    if(e.key==='ArrowLeft')step(-1);
    if(e.key==='ArrowRight')step(1);
    if(e.key==='+'||e.key==='=')zoom(z*1.5);
    if(e.key==='-')zoom(z/1.5);
    if(e.key==='0')zoom(1);
  });

  // ── contents links jump inside the panel ─────────────────────────────────
  $$('.toc a').forEach(function(a){
    a.addEventListener('click',function(e){
      var t=document.querySelector(a.getAttribute('href'));
      if(!t)return; e.preventDefault();
      t.scrollIntoView({behavior:'smooth',block:'start'});
    });
  });

  // ── per-document style pickers ───────────────────────────────────────────
  $$('.panel').forEach(function(panel){
    var pk=$$('.pk[data-s]',panel),pl=$$('.styl[data-s]',panel);
    if(!pk.length)return;
    function set(no){
      pk.forEach(function(c){c.setAttribute('aria-pressed',c.dataset.s===no?'true':'false');});
      pl.forEach(function(p){p.classList.toggle('on',p.dataset.s===no);});
    }
    pk.forEach(function(c){c.addEventListener('click',function(){set(c.dataset.s);});});
    set(pk[0].dataset.s);
  });

  // ── the mark matures when the room opens ─────────────────────────────────
  var dwm=$('#doorwm');
  if(dwm&&!matchMedia('(prefers-reduced-motion: reduce)').matches){
    var ds=$$('span',dwm); ds.forEach(function(d){d.classList.remove('on');});
    ds[0].classList.add('on');
    [1,2].forEach(function(i){setTimeout(function(){
      ds[i-1].classList.remove('on');ds[i].classList.add('on');},520+i*620);});
  }

  // ── three states you scroll through ──────────────────────────────────────
  var PAPER=[242,238,230],INK=[27,23,32],RED=[196,18,46];
  function lerp(a,b,t){return [0,1,2].map(function(i){
    return Math.round(a[i]+(b[i]-a[i])*t);});}
  function rgb(c){return 'rgb('+c[0]+','+c[1]+','+c[2]+')';}
  var acts=$('#acts'),stage=$('#actstage'),
      slides=acts?$$('.acts__s',acts):[],rails=$$('#actrail span'),
      texA=acts?$('[data-tex="0"]',acts):null,texB=acts?$('[data-tex="1"]',acts):null,
      reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  function paintActs(){
    if(!acts||!stage||reduce)return;
    var r=acts.getBoundingClientRect(),span=r.height-innerHeight;
    if(span<=0)return;
    var p=Math.min(1,Math.max(0,-r.top/span));
    // each ground holds while its state is on screen and crosses quickly between,
    // so nothing is ever read against a half-mixed colour
    var bg;
    if(p<.20)bg=PAPER;
    else if(p<.30)bg=lerp(PAPER,INK,(p-.20)/.10);
    else if(p<.62)bg=INK;
    else if(p<.72)bg=lerp(INK,RED,(p-.62)/.10);
    else bg=RED;
    stage.style.backgroundColor=rgb(bg);
    stage.style.color=p>.25?'rgb(242,238,230)':'rgb(27,23,32)';
    if(texA)texA.style.opacity=String(Math.max(0,1-p/.18));
    if(texB)texB.style.opacity=String(p>.32&&p<.62?1:0);
    var idx=p<.26?0:(p<.66?1:2);
    slides.forEach(function(sl,i){sl.classList.toggle('on',i===idx);});
    rails.forEach(function(sp,i){sp.classList.toggle('on',i===idx);});
  }

  // ── the last section floods, and the mark finishes the sentence ──────────
  // The scrollbar is the transport. Progress through the closer's track drives
  // the flood first, then the three states in order, and the finished logotype
  // last, with the dot landing on it. Nothing here runs on a timer, so it can
  // be held, reversed, or read at whatever pace the client scrolls at.
  var closers=$$('[data-closer]'),REDUCED=matchMedia('(prefers-reduced-motion:reduce)').matches;
  function paintFlood(){
    closers.forEach(function(c){
      var tr=c.firstElementChild;if(!tr)return;
      var r=tr.getBoundingClientRect();
      if(r.bottom<-300||r.top>innerHeight+300)return;
      var run=tr.offsetHeight-innerHeight,f;
      if(REDUCED||run<80){f=Math.min(1,Math.max(0,(innerHeight-r.top)/(innerHeight*.72)));}
      else{f=Math.min(1,Math.max(0,-r.top/run));}
      c.style.setProperty('--f',f.toFixed(3));
      c.style.setProperty('--fl',Math.min(1,f/.16).toFixed(3));
      c.classList.toggle('flooded',f>.12);
      c.classList.toggle('seen',f>.02);
      c.classList.toggle('lit',f>.20&&f<.90);
      c.classList.toggle('ended',f>.80);
      var k=f<.18?-1:(f<.37?0:(f<.55?1:(f<.70?2:3)));
      $$('.closer__wm > span',c).forEach(function(sp,i){sp.classList.toggle('on',i===k);});
      $$('.closer__stg span',c).forEach(function(sp,i){sp.classList.toggle('on',i===k);});
      $$('.closer__rail b',c).forEach(function(b,i){b.classList.toggle('on',i<=k);});
    });
  }

  // ── openers and section heads arrive as you reach them ───────────────────
  // Once each, and only in the panel on screen: a head that has arrived stays
  // arrived, so nothing re-animates under a reader who scrolls back up.
  function paintReveal(){
    var host=$('.panel.active');if(!host)return;
    var els=host.querySelectorAll('.docopen:not(.in),.sec:not(.in)');
    for(var i=0;i<els.length;i++){
      var r=els[i].getBoundingClientRect();
      if(r.top<innerHeight*.92&&r.bottom>-40)els[i].classList.add('in');
    }
    var op=host.querySelector('.docopen');
    if(op){
      var g=op.querySelector('.docopen__gh');
      if(g)g.style.setProperty('--gy',
        Math.round(Math.max(-90,Math.min(90,-op.getBoundingClientRect().top*.13)))+'px');
    }
  }

  // ── the header turns with it ─────────────────────────────────────────────
  var topbar=$('.top');
  function paintTurn(){
    var cl=$('.panel.active .closer'),t=0;
    if(cl){
      var r=cl.getBoundingClientRect();
      t=Math.min(1,Math.max(0,(innerHeight*.78-r.top)/(innerHeight*.46)));
    }
    topbar.style.setProperty('--top-bg',t>0?rgb(lerp([247,244,238],RED,t)):'');
    topbar.classList.toggle('turned',t>.55);
  }

  // ── the marker slides, and you can drag it ───────────────────────────────
  var nav=$('.nav'),notch=$('#notch'),ndrag=false;
  function centreOf(btn){
    var nr=nav.getBoundingClientRect(),br=btn.getBoundingClientRect();
    return br.left-nr.left+br.width/2;
  }
  function place(x){notch.style.transform='translateX('+(x-7)+'px)';}
  function settle(){
    if(!notch||!nav)return;
    var a=tabs.filter(function(t){return t.getAttribute('aria-selected')==='true';})[0];
    if(a){place(centreOf(a));notch.setAttribute('aria-valuenow',String(tabs.indexOf(a)+1));}
  }
  function nearest(x){
    var best=tabs[0],bd=1e9;
    tabs.forEach(function(t){var d=Math.abs(centreOf(t)-x);if(d<bd){bd=d;best=t;}});
    return best;
  }
  if(notch&&nav){
    notch.addEventListener('pointerdown',function(e){
      e.preventDefault();ndrag=true;notch.classList.add('dragging');
      nav.classList.add('armed');notch.setPointerCapture(e.pointerId);
    });
    notch.addEventListener('pointermove',function(e){
      if(!ndrag)return;
      var nr=nav.getBoundingClientRect(),
          x=Math.min(nr.width,Math.max(0,e.clientX-nr.left));
      place(x);
      var n=nearest(x);
      tabs.forEach(function(t){t.classList.toggle('near',t===n);});
    });
    ['pointerup','pointercancel'].forEach(function(ev){
      notch.addEventListener(ev,function(e){
        if(!ndrag)return;ndrag=false;
        notch.classList.remove('dragging');nav.classList.remove('armed');
        var nr=nav.getBoundingClientRect(),
            x=Math.min(nr.width,Math.max(0,e.clientX-nr.left));
        tabs.forEach(function(t){t.classList.remove('near');});
        show(nearest(x).dataset.doc);settle();
      });
    });
    notch.addEventListener('keydown',function(e){
      var d=e.key==='ArrowRight'?1:e.key==='ArrowLeft'?-1:0;
      if(!d)return;e.preventDefault();
      var a=tabs.filter(function(t){return t.getAttribute('aria-selected')==='true';})[0],
          i=(tabs.indexOf(a)+d+tabs.length)%tabs.length;
      show(tabs[i].dataset.doc);settle();
    });
    addEventListener('resize',settle);
    setTimeout(settle,90);
  }

  var raf=false;
  function frame(){paintActs();paintFlood();paintTurn();paintReveal();raf=false;}
  addEventListener('scroll',function(){
    if(raf)return;raf=true;requestAnimationFrame(frame);
  },{passive:true});
  addEventListener('resize',function(){requestAnimationFrame(frame);},{passive:true});
  setTimeout(frame,120);

  $('#printBtn').addEventListener('click',function(){window.print();});
})();
</script>"""

# ══════════════════════════════════════════════════════════════════ output ═══
LOGBOOK = ('<section class="panel" id="p-logbook" role="tabpanel" '
           'aria-labelledby="t-logbook">' + standfirst() + logbook()
           + closer("From idea to life.",
                    "Every decision, every sample and every measurement, with the date it "
                    "happened and the reason behind it.", "var(--red)") + '</section>')
# The quote and the invoice are still built; drop ("billing", "Billing") back into
# DOCS and BILLING back into BODY to put the tab back in the room.
BILLING = quote() + invoice() + "</section>"
LIGHTBOX = ('<div class="lbx" id="lb" role="dialog" aria-modal="true" aria-label="Full size">'
            '<button class="lbx__x" id="lbX" type="button">Close &times;</button>'
            '<button class="lbx__a p" id="lbP" type="button" aria-label="Previous">&#8249;</button>'
            '<figure style="width:100%;max-width:1500px">'
            '<div class="lbx__box" id="lbBox"><span class="im" id="lbI" role="img"></span></div>'
            '<div class="lbx__bar"><span class="lbx__z">'
            '<button type="button" id="lbOut" aria-label="Zoom out">&minus;</button>'
            '<span id="lbZ">100%</span>'
            '<button type="button" id="lbIn" aria-label="Zoom in">+</button></span>'
            '<figcaption id="lbC"></figcaption></div></figure>'
            '<button class="lbx__a n" id="lbN" type="button" aria-label="Next">&#8250;</button></div>')

BODY = (DEFS + top() + '<main>' + range_panel() + LOGBOOK
        + heads(techpack(), "sketched") + heads(fitting(), "stitched")
        + heads(handover(), "born") + heads(system(), "born")
        + '</main>' + LIGHTBOX + JS)
HEAD = "<style>\n" + FONTS + "\n" + CSS + "\n" + IMGCSS + "\n</style>"

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
