#!/usr/bin/env python3
"""BORN Studio brand book — tabbed, English, visual.
Tabs: Brand / Logo / Color / Typography / Applications / Downloads / Exploration.
Final double-exposure logo only. Stage logos (sketched/stitched/inked/BORN) and
icons applied visually. Animations render as inline SVG+CSS (reliable in-page).
Downloads use Blob object URLs + an "Open" fallback + a client-side ZIP.
Emits index.html (standalone) and tools/_work/artifact.html (body form)."""
import base64, os, json

S="tools/src"; W="tools/_work"; A="assets/logos"   # S = tracked sources, W = temp output
os.makedirs(W, exist_ok=True)
rd=lambda p: open(p, encoding="utf-8").read()
def datauri(path, mime): return f"data:{mime};base64,"+base64.b64encode(open(path,"rb").read()).decode("ascii")

FONTS = rd(f"{S}/fonts.css")
ROOT  = rd(f"{S}/root.css")
DEFS  = rd(f"{S}/defs.svg")                     # hatch patterns for the stitched state
SVGKEYS=["wm_principal","wm_sin_slogan","wm_solo","wm_ecorojo_slogan","wm_ecorojo",
  "ic_negativo","ic_construccion","ic_doble","ic_doble_red",
  "wm_principal_neg","wm_principal_onred","wm_solo_neg","wm_solo_onred",
  "state_sketch","state_stitch","state_ink","state_born"]
SVG = {k: rd(f"{S}/{k}.svg") for k in SVGKEYS}
ANI = {"ens": rd(f"{S}/an_ensamblaje.svg"), "bar": rd(f"{S}/an_barrida.svg")}
PNG = {k: datauri(f"{A}/{k}.png","image/png") for k in SVGKEYS}
VID = {"ens_mp4":datauri(f"{A}/an_ensamblaje.mp4","video/mp4"),"ens_webm":datauri(f"{A}/an_ensamblaje.webm","video/webm"),
       "bar_mp4":datauri(f"{A}/an_barrida.mp4","video/mp4"),"bar_webm":datauri(f"{A}/an_barrida.webm","video/webm")}
EXPL_ESC = rd("logos.html").replace("&","&amp;").replace('"',"&quot;")

# ---- pre-build the whole-kit ZIP and embed it as a data URI, so the "Download
#      everything" button is a NATIVE <a download> (most compatible; works where
#      JS-synthesised downloads are blocked by the artifact sandbox) -----------
import io, zipfile
def _build_zip():
    groups={
     "01-logos":[("wm_principal","BORN-logo-primary"),("wm_sin_slogan","BORN-logo-no-tagline"),
       ("wm_solo","BORN-wordmark"),("wm_ecorojo_slogan","BORN-logo-red-echo-tagline"),("wm_ecorojo","BORN-logo-red-echo")],
     "02-negatives":[("wm_principal_neg","BORN-logo-primary-negative"),("wm_solo_neg","BORN-wordmark-negative"),
       ("wm_principal_onred","BORN-logo-primary-on-red"),("wm_solo_onred","BORN-wordmark-on-red")],
     "03-stages":[("state_sketch","BORN-stage-sketched"),("state_stitch","BORN-stage-stitched"),
       ("state_ink","BORN-stage-inked"),("state_born","BORN-stage-born")],
     "04-icons":[("ic_negativo","BORN-icon-negative"),("ic_construccion","BORN-icon-construction"),
       ("ic_doble","BORN-icon-double-exposure"),("ic_doble_red","BORN-icon-red")],
    }
    buf=io.BytesIO()
    with zipfile.ZipFile(buf,"w",zipfile.ZIP_DEFLATED) as z:
        for folder,items in groups.items():
            for src,dst in items:
                if os.path.exists(f"{A}/{src}.png"): z.write(f"{A}/{src}.png", f"{folder}/{dst}.png")
                if os.path.exists(f"{S}/{src}.svg"): z.writestr(f"06-vector-svg/{dst}.svg", rd(f"{S}/{src}.svg"))
        for src,dst in [("an_ensamblaje","BORN-assembly"),("an_barrida","BORN-sweep")]:
            for ext in ["mp4","webm"]: z.write(f"{A}/{src}.{ext}", f"05-animations/{dst}.{ext}")
        z.writestr("README.txt","BORN Studio - Brand Kit. Every stage logo carries the red dot.\nFrom idea to life.\n")
    return "data:application/zip;base64,"+base64.b64encode(buf.getvalue()).decode("ascii")
ZIP_URI=_build_zip()

# download registry: key -> (nice filename, human title)
KIT=[
 ("wm_principal","BORN-logo-primary.png","Primary logo"),
 ("wm_principal_neg","BORN-logo-primary-negative.png","Primary — negative"),
 ("wm_principal_onred","BORN-logo-primary-on-red.png","Primary — on red"),
 ("wm_sin_slogan","BORN-logo-no-tagline.png","No tagline"),
 ("wm_solo","BORN-wordmark.png","Wordmark only"),
 ("wm_solo_neg","BORN-wordmark-negative.png","Wordmark — negative"),
 ("wm_ecorojo_slogan","BORN-logo-red-echo-tagline.png","Red echo + tagline"),
 ("wm_ecorojo","BORN-logo-red-echo.png","Red echo"),
 ("state_sketch","BORN-stage-sketched.png","Sketched stage"),
 ("state_stitch","BORN-stage-stitched.png","Stitched stage"),
 ("state_ink","BORN-stage-inked.png","Inked stage"),
 ("state_born","BORN-stage-born.png","BORN stage"),
 ("ic_negativo","BORN-icon-negative.png","Icon — negative"),
 ("ic_construccion","BORN-icon-construction.png","Icon — construction"),
 ("ic_doble","BORN-icon-double-exposure.png","Icon — double exposure"),
 ("ic_doble_red","BORN-icon-red.png","Icon — red"),
]
DL={k:f for k,f,t in KIT}; TITLE={k:t for k,f,t in KIT}

FAVICON=("data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2064%2064'"
 "%3E%3Crect%20width='64'%20height='64'%20rx='13'%20fill='%231B1720'/%3E"
 "%3Ctext%20x='29'%20y='47'%20font-family='Georgia,Times,serif'%20font-size='46'%20font-weight='700'"
 "%20text-anchor='middle'%20fill='%23F2EEE6'%3EB%3C/text%3E%3Ccircle%20cx='47'%20cy='44'%20r='5'%20fill='%23C4122E'/%3E%3C/svg%3E")

# ------------------------------------------------------------------ CSS ------
CSS = ROOT + r"""
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{background:var(--paper);color:var(--ink);font-family:var(--sans);-webkit-font-smoothing:antialiased;line-height:1.6}
img,svg,video{display:block;max-width:100%}
a{color:inherit}
.wrap{max-width:1140px;margin:0 auto;padding:0 clamp(1.25rem,5vw,3rem)}
::selection{background:var(--red);color:var(--paper)}
/* top bar */
.top{position:sticky;top:0;z-index:50;background:rgba(242,238,230,.88);backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}
.top__in{display:flex;align-items:center;gap:1.2rem;max-width:1140px;margin:0 auto;padding:.65rem clamp(1.25rem,5vw,3rem);flex-wrap:wrap}
.brand{display:flex;align-items:center;text-decoration:none;flex:0 0 auto}
.brand svg{height:30px;width:auto;max-width:none;display:block}
.brand:hover{opacity:.75;transition:opacity .2s}
.tabs{display:flex;gap:.15rem;margin-left:auto;flex-wrap:wrap}
.tab{font-family:var(--mono);font-size:.67rem;letter-spacing:.13em;text-transform:uppercase;color:var(--g2);background:none;border:0;cursor:pointer;padding:.55rem .8rem;border-radius:7px;white-space:nowrap;transition:color .2s,background .2s}
.tab:hover{color:var(--ink);background:var(--paper-2)}
.tab[aria-selected=true],.tab[aria-selected=true]:hover{color:var(--paper);background:var(--ink)}
.bar{height:2px;background:var(--red);width:0;transition:width .12s linear}
/* panels */
.panel{display:none;padding:clamp(2.2rem,5vw,4rem) 0 clamp(3rem,8vw,6rem)}
.panel.active{display:block;animation:pfade .45s ease}
@keyframes pfade{from{opacity:0}to{opacity:1}}
/* staggered scroll-reveal (progressive enhancement: only hides when JS is on) */
html.js:not(.reduce) .rv{transition:opacity .7s var(--ease),transform .7s var(--ease)}
html.js:not(.reduce) .rv:not(.in){opacity:0;transform:translateY(24px)}
@media(prefers-reduced-motion:reduce){.panel{animation:none}}
.kicker{font-family:var(--mono);font-size:.66rem;letter-spacing:.24em;text-transform:uppercase;color:var(--red);margin-bottom:.7rem}
.h1{font-family:var(--serif);font-weight:900;font-size:clamp(2.3rem,6.5vw,4.6rem);line-height:.96;letter-spacing:-.02em;text-wrap:balance}
.h2{font-family:var(--serif);font-weight:900;font-size:clamp(1.6rem,3.6vw,2.5rem);line-height:1.03;letter-spacing:-.01em}
.lede{font-family:var(--serif6);font-weight:600;font-size:clamp(1.2rem,2.1vw,1.6rem);line-height:1.38;color:var(--g2);max-width:36ch}
.prose{font-size:clamp(1rem,1.3vw,1.14rem);line-height:1.65;color:var(--g2);max-width:64ch}
.prose b,.prose strong{color:var(--ink)}
.sec{margin-top:clamp(2.6rem,6vw,4.6rem)}
.sec--line{border-top:1px solid var(--line);padding-top:clamp(2.2rem,5vw,3.4rem)}
.eyebrow{font-family:var(--mono);font-size:.64rem;letter-spacing:.2em;text-transform:uppercase;color:var(--g3);margin-bottom:1.1rem}
.grid{display:grid;gap:1.2rem}
.g2{grid-template-columns:repeat(auto-fit,minmax(270px,1fr))}
.g3{grid-template-columns:repeat(auto-fit,minmax(215px,1fr))}
.g4{grid-template-columns:repeat(auto-fit,minmax(165px,1fr))}
.card{background:var(--paper-2);border:1px solid var(--line);border-radius:14px;padding:1.5rem 1.6rem;transition:transform .25s var(--ease),box-shadow .25s var(--ease)}
.card:hover{transform:translateY(-3px);box-shadow:0 18px 40px -24px rgba(27,23,32,.4)}
.card h3{font-family:var(--serif6);font-weight:600;font-size:1.1rem;margin-bottom:.4rem}
.card p{font-size:.93rem;color:var(--g2);line-height:1.55}
.muted{font-family:var(--mono);font-size:.62rem;letter-spacing:.1em;text-transform:uppercase;color:var(--g3)}
.dl-grid{display:grid;grid-template-columns:max-content 1fr;gap:.6rem 1.6rem}
.dl-grid dt{font-family:var(--mono);font-size:.64rem;letter-spacing:.12em;text-transform:uppercase;color:var(--g3);align-self:center}
.dl-grid dd{color:var(--ink);font-family:var(--serif6);font-weight:600;font-size:1.06rem}
.list{list-style:none;display:grid;gap:.55rem}
.list li{padding-left:1.4rem;position:relative;color:var(--g2);line-height:1.5}
.list li::before{content:'';position:absolute;left:0;top:.62em;width:8px;height:2px;background:var(--red)}
.list--no li::before{background:var(--g4);width:8px;height:8px;border-radius:50%;top:.5em}
/* hero */
.hero{text-align:center;padding:clamp(.5rem,3vw,2rem) 0 0}
.hero .lock{width:min(720px,94%);margin:1.4rem auto 1rem}
.hero .lock svg{width:100%;height:auto}
.hero .claim{font-family:var(--serif);font-weight:900;font-size:clamp(1.4rem,3.4vw,2.3rem);letter-spacing:-.01em}
.hero .claim .r{color:var(--red)}
.hero .tag{font-family:var(--mono);font-size:.72rem;letter-spacing:.3em;text-transform:uppercase;color:var(--g3);margin-top:.75rem}
.hint{font-family:var(--mono);font-size:.58rem;letter-spacing:.18em;text-transform:uppercase;color:var(--g4);margin-top:1.4rem}
/* stages */
.stage{background:var(--paper-2);border:1px solid var(--line);border-radius:14px;display:flex;align-items:center;justify-content:center;padding:clamp(1.6rem,4.5vw,3rem);transition:transform .25s var(--ease)}
.stage:hover{transform:translateY(-3px)}
.stage svg{width:100%;height:auto}
.stage--sq{aspect-ratio:1/1}.stage--sq svg{width:70%}
.stage--dark{background:var(--ink);border-color:transparent}
.stage--red{background:var(--red);border-color:transparent}
.capt{margin-top:.7rem}
.capt b{font-family:var(--serif6);font-weight:600;font-size:1.02rem;display:block}
.capt span{font-family:var(--mono);font-size:.6rem;letter-spacing:.1em;text-transform:uppercase;color:var(--g3)}
.capt p{font-size:.88rem;color:var(--g2);line-height:1.5;margin-top:.35rem}
.bgnote{font-family:var(--mono);font-size:.6rem;letter-spacing:.1em;text-transform:uppercase;color:var(--g3);margin-top:.5rem}
/* animation display */
.motion{display:grid;gap:1.4rem;grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}
.animbox{background:var(--paper-2);border:1px solid var(--line);border-radius:14px;padding:clamp(1.8rem,5vw,3rem);display:flex;align-items:center;justify-content:center}
.animbox svg{width:100%;height:auto}
/* phase (applications) */
.phase{border:1px solid var(--line);border-radius:14px;overflow:hidden;background:var(--paper-2);display:flex;flex-direction:column}
.phase__logo{padding:clamp(1.6rem,4vw,2.4rem) 1.4rem;background:var(--paper);border-bottom:1px solid var(--line);display:flex;align-items:center;justify-content:center;min-height:118px}
.phase__logo svg{width:82%;height:auto}
.phase__b{padding:1.3rem 1.5rem}
.phase__b .n{font-family:var(--mono);font-size:.62rem;letter-spacing:.14em;text-transform:uppercase;color:var(--red)}
.phase__b h3{font-family:var(--serif);font-weight:900;font-size:1.55rem;margin:.2rem 0 .5rem}
/* color swatches */
.sw{border:1px solid var(--line);border-radius:14px;overflow:hidden;cursor:pointer;background:var(--paper-2);transition:transform .2s}
.sw:hover{transform:translateY(-3px)}
.sw__c{height:110px}.sw__m{padding:.7rem .9rem}
.sw__m b{font-family:var(--serif6);font-weight:600;font-size:.96rem;display:block}
.sw__m span{font-family:var(--mono);font-size:.66rem;color:var(--g3);letter-spacing:.05em}
/* type specimens */
.spec{border-top:1px solid var(--line);padding:1.35rem 0;display:grid;gap:.5rem}
.spec-head{display:flex;align-items:center;justify-content:space-between;gap:1rem;flex-wrap:wrap}
.spec .meta{font-family:var(--mono);font-size:.62rem;letter-spacing:.12em;text-transform:uppercase;color:var(--g3)}
.spec .samp{color:var(--ink);line-height:1.1}
.fontdl{font-family:var(--mono);font-size:.6rem;letter-spacing:.08em;text-transform:uppercase;color:var(--paper);background:var(--ink);border-radius:6px;padding:.45rem .8rem;text-decoration:none;white-space:nowrap;transition:background .2s}
.fontdl:hover{background:var(--red)}
/* downloads */
.kit{display:grid;gap:1.2rem;grid-template-columns:repeat(auto-fill,minmax(232px,1fr));margin-top:1.6rem}
.ki{display:flex;flex-direction:column;background:var(--paper-2);border:1px solid var(--line);border-radius:14px;overflow:hidden;transition:transform .2s}
.ki:hover{transform:translateY(-3px)}
.ki__p{background:var(--paper);display:flex;align-items:center;justify-content:center;padding:1.1rem;min-height:130px}
.ki__p img,.ki__p svg{max-width:100%;max-height:150px;width:auto;height:auto}
.ki__m{padding:.85rem 1.05rem;border-top:1px solid var(--line);display:flex;flex-direction:column;gap:.55rem;flex:1}
.ki__m b{font-family:var(--sans7);font-size:.93rem}
.ki__f{font-family:var(--mono);font-size:.6rem;letter-spacing:.1em;text-transform:uppercase;color:var(--g3)}
.dls{display:flex;gap:.5rem;flex-wrap:wrap;margin-top:auto}
.dl{font-family:var(--mono);font-size:.62rem;letter-spacing:.08em;text-transform:uppercase;color:var(--paper);background:var(--ink);border:0;border-radius:6px;padding:.55rem .85rem;text-decoration:none;cursor:pointer;transition:background .2s}
.dl:hover{background:var(--red)}
.dl--ghost{background:transparent;color:var(--g2);border:1px solid var(--line)}
.dl--ghost:hover{background:var(--paper-3);color:var(--ink)}
.dl--big{font-size:.72rem;padding:.85rem 1.4rem}
.note{font-family:var(--mono);font-size:.7rem;letter-spacing:.04em;color:var(--g3);line-height:1.6;margin-top:1.5rem}
/* exploration frame */
.expl-bar{display:flex;align-items:center;justify-content:space-between;gap:1rem;flex-wrap:wrap;background:var(--ink);color:var(--paper);border-radius:14px 14px 0 0;padding:.75rem 1.1rem;margin-top:1.4rem}
.expl-bar b{font-family:var(--mono);font-size:.66rem;letter-spacing:.14em;text-transform:uppercase;font-weight:400}
.expl-bar a{font-family:var(--mono);font-size:.62rem;letter-spacing:.1em;color:var(--paper);text-decoration:none;border:1px solid rgba(242,238,230,.4);padding:.35rem .75rem;border-radius:6px}
.expl-bar a:hover{background:var(--paper);color:var(--ink)}
.expl-frame{width:100%;height:80vh;min-height:540px;border:1px solid var(--line);border-top:0;border-radius:0 0 14px 14px;background:#fff;display:block}
/* red seal strip */
.seal{background:var(--red);color:var(--paper);border-radius:16px;padding:clamp(2rem,6vw,3.6rem);text-align:center;margin-top:clamp(2.6rem,6vw,4rem)}
.seal h2{font-family:var(--serif);font-weight:900;font-size:clamp(1.6rem,4vw,2.6rem);line-height:1.05}
.seal p{font-family:var(--mono);font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;margin-top:.9rem;opacity:.85}
/* footer */
.foot{border-top:1px solid var(--line);padding:clamp(2.4rem,6vw,4rem) 0;text-align:center}
.foot .fm{width:min(320px,64%);margin:0 auto 1.2rem}
.foot p{font-family:var(--mono);font-size:.66rem;letter-spacing:.1em;color:var(--g3);line-height:1.9}
.toast{position:fixed;left:50%;bottom:24px;transform:translateX(-50%) translateY(20px);opacity:0;background:var(--ink);color:var(--paper);font-family:var(--mono);font-size:.7rem;letter-spacing:.1em;padding:.6rem 1rem;border-radius:8px;pointer-events:none;transition:.3s;z-index:60}
.toast.on{opacity:1;transform:translateX(-50%) translateY(0)}
/* mobile hamburger menu */
.menu-btn{display:none;margin-left:auto;background:none;border:0;cursor:pointer;width:42px;height:34px;position:relative;padding:0}
.menu-btn span{position:absolute;left:9px;right:9px;height:2px;background:var(--ink);border-radius:2px;transition:transform .3s var(--ease),opacity .2s}
.menu-btn span:nth-child(1){top:11px}.menu-btn span:nth-child(2){top:16px}.menu-btn span:nth-child(3){top:21px}
.top.open .menu-btn span:nth-child(1){transform:translateY(5px) rotate(45deg)}
.top.open .menu-btn span:nth-child(2){opacity:0}
.top.open .menu-btn span:nth-child(3){transform:translateY(-5px) rotate(-45deg)}
@media(max-width:760px){
  .menu-btn{display:block}
  .tabs{position:absolute;top:100%;left:0;right:0;flex-direction:column;gap:.15rem;background:rgba(242,238,230,.97);backdrop-filter:blur(12px);border-bottom:1px solid var(--line);padding:.6rem clamp(1.25rem,5vw,3rem) 1.1rem;transform:translateY(-10px);opacity:0;pointer-events:none;transition:transform .3s var(--ease),opacity .3s var(--ease);box-shadow:0 26px 44px -28px rgba(27,23,32,.4)}
  .top.open .tabs{transform:none;opacity:1;pointer-events:auto}
  .tab{width:100%;text-align:left;font-size:.82rem;letter-spacing:.16em;padding:.9rem .7rem;border-radius:9px}
  .tab:hover{background:var(--paper-2)}
  .expl-frame{height:72vh;min-height:440px}.expl-bar a{display:none}
}
""" + r"""
/* ---- inline animation engine (ensamblaje ax1 / barrida ax7) ---- */
.axwrap{overflow:visible}
.axwrap .ax-g1{opacity:.30;transform:translate(-12px,-9px)}
.axwrap .ax-g2{opacity:.42;transform:translate(-7px,-6px)}
.axwrap .ax-front{opacity:1}
.axwrap .ax-dot{opacity:1;transform-box:fill-box;transform-origin:center}
.ax1 .ax-g1{animation:x1a 6s var(--ease) infinite}
.ax1 .ax-g1 path{stroke-dasharray:3600;stroke-dashoffset:3600;animation:x1d 6s var(--ease) infinite}
.ax1 .ax-g2{animation:x1b 6s var(--ease) infinite}
.ax1 .ax-front{animation:x1f 6s var(--ease) infinite}
.ax1 .ax-dot{animation:x1o 6s var(--ease) infinite}
@keyframes x1d{0%{stroke-dashoffset:3600}22%{stroke-dashoffset:0}100%{stroke-dashoffset:0}}
@keyframes x1a{0%{opacity:0}8%{opacity:.30}90%{opacity:.30}97%{opacity:0}100%{opacity:0}}
@keyframes x1b{0%,24%{opacity:0}36%{opacity:.42}90%{opacity:.42}97%{opacity:0}100%{opacity:0}}
@keyframes x1f{0%,42%{opacity:0}60%,100%{opacity:1}}
@keyframes x1o{0%,60%{opacity:0;transform:scale(.3)}72%{opacity:1;transform:scale(1)}100%{opacity:1;transform:scale(1)}}
.ax7 .ax-front{clip-path:inset(0 100% 0 0);animation:x7 5s var(--ease) infinite}
.ax7 .ax-dot{animation:x7o 5s var(--ease) infinite}
@keyframes x7{0%,10%{clip-path:inset(0 100% 0 0)}55%,92%{clip-path:inset(0 0 0 0)}100%{clip-path:inset(0 100% 0 0)}}
@keyframes x7o{0%,52%{opacity:0}64%,92%{opacity:1}100%{opacity:0}}
@media(prefers-reduced-motion:reduce){.axwrap *{animation:none!important}.ax7 .ax-front{clip-path:none!important}.ax1 .ax-g1 path{stroke-dashoffset:0!important}.axwrap .ax-front,.axwrap .ax-dot{opacity:1!important}}
/* ---- stage-path colors for the inline stage wordmarks ---- */
.p-sk{fill:none;stroke:var(--g2);stroke-linejoin:round}
.p-skc{fill:none;stroke:var(--g2);stroke-linecap:round}
.p-st{stroke:var(--ink);stroke-linejoin:round}
.p-ink{fill:var(--ink)}
.p-bo{fill:var(--red)}
/* ================= impact & interaction — Rojo Valentino ================= */
html{overflow-x:hidden}
/* active tab + hover go red */
.tab:hover{color:var(--red)}
.tab[aria-selected=true],.tab[aria-selected=true]:hover{background:var(--red);color:var(--paper)}
/* red cursor companion (desktop pointers only) */
.rdot{position:fixed;top:0;left:0;width:11px;height:11px;border-radius:50%;background:var(--red);
  pointer-events:none;z-index:95;opacity:0;transition:opacity .3s,width .25s var(--ease),height .25s var(--ease),background .25s}
.rdot.big{width:44px;height:44px;background:rgba(196,18,46,.16);border:1.5px solid var(--red)}
@media (hover:none),(pointer:coarse){.rdot{display:none}}
/* elegant transition: a fine Rojo Valentino hairline sweeps across the top */
.sweepline{position:fixed;top:0;left:0;height:2px;width:100%;background:var(--red);transform:scaleX(0);
  transform-origin:left;z-index:121;pointer-events:none;opacity:0}
.sweepline.run{animation:sweep .74s cubic-bezier(.76,0,.24,1)}
@keyframes sweep{0%{opacity:1;transform:scaleX(0);transform-origin:left}
  48%{opacity:1;transform:scaleX(1);transform-origin:left}
  52%{opacity:1;transform:scaleX(1);transform-origin:right}
  100%{opacity:1;transform:scaleX(0);transform-origin:right}}
@media(prefers-reduced-motion:reduce){.sweepline{display:none}}
/* tactile feedback for touch + click */
.tab,.chip,.dl,.fontdl,.sw{transition:color .2s,background .2s,border-color .2s,transform .12s var(--ease)}
.tab:active,.chip:active,.dl:active,.fontdl:active,.sw:active,.brand:active{transform:scale(.96)}
/* hero red glow + replay affordance */
.hero{position:relative;cursor:default}
.hero::before{content:"";position:absolute;left:50%;top:52%;width:min(720px,92%);height:clamp(220px,40vw,420px);
  transform:translate(-50%,-50%);background:radial-gradient(ellipse at center,rgba(196,18,46,.16),transparent 68%);
  pointer-events:none;z-index:-1;animation:glow 6s ease-in-out infinite}
@keyframes glow{0%,100%{opacity:.6}50%{opacity:1}}
@media(prefers-reduced-motion:reduce){.hero::before{animation:none}}
/* full-bleed red manifesto band */
.fullred{position:relative;background:var(--red);color:var(--paper);text-align:center;overflow:hidden;
  margin-left:calc(50% - 50vw);margin-right:calc(50% - 50vw);width:100vw;
  padding:clamp(3.4rem,10vw,7rem) clamp(1.25rem,6vw,3rem);margin-top:clamp(2.8rem,7vw,4.5rem)}
.fullred .fr-k{font-family:var(--mono);font-size:.66rem;letter-spacing:.24em;text-transform:uppercase;opacity:.8;margin-bottom:1rem}
.fullred h2{font-family:var(--serif);font-weight:900;font-size:clamp(2.4rem,9vw,6rem);line-height:.94;letter-spacing:-.02em;text-wrap:balance}
.fullred h2 .op{color:rgba(242,238,230,.42)}
.fullred .bigdot{width:clamp(38px,7vw,74px);height:clamp(38px,7vw,74px);border-radius:50%;background:var(--paper);margin:1.6rem auto 0;animation:beat 2.4s var(--ease) infinite}
@keyframes beat{0%,100%{transform:scale(1)}50%{transform:scale(1.16)}}
.fullred p.fr-s{font-family:var(--mono);font-size:clamp(.68rem,1.6vw,.86rem);letter-spacing:.18em;text-transform:uppercase;margin-top:1.4rem;opacity:.85}
@media(prefers-reduced-motion:reduce){.fullred .bigdot{animation:none}}
/* interactive stage explorer */
.stagex{border:1px solid var(--line);border-radius:16px;overflow:hidden;background:var(--paper-2);margin-top:1.4rem}
.stagex__disp{display:grid;place-items:center;padding:clamp(2rem,7vw,4.6rem);min-height:clamp(150px,28vw,300px);background:var(--paper);position:relative}
.stagex__disp .sx{grid-area:1/1;width:min(640px,88%);opacity:0;transform:scale(.98);transition:opacity .5s var(--ease),transform .5s var(--ease)}
.stagex__disp .sx.on{opacity:1;transform:none}
.stagex__disp .sx svg{width:100%;height:auto}
.stagex__chips{display:flex;flex-wrap:wrap;gap:.55rem;padding:1rem clamp(1rem,3vw,1.6rem);border-top:1px solid var(--line);align-items:center}
.chip{font-family:var(--mono);font-size:.64rem;letter-spacing:.12em;text-transform:uppercase;color:var(--g2);background:var(--paper);border:1px solid var(--line);border-radius:22px;padding:.55rem 1.05rem;cursor:pointer;transition:.2s}
.chip:hover{border-color:var(--red);color:var(--red)}
.chip[aria-pressed=true]{background:var(--ink);color:var(--paper);border-color:var(--ink)}
.chip__auto{margin-left:auto;font-family:var(--mono);font-size:.58rem;letter-spacing:.14em;text-transform:uppercase;color:var(--g3)}
/* red accents on cards / specs */
.card:hover{border-color:rgba(196,18,46,.45)}
.spec:hover .meta{color:var(--red)}
.lede .r,.hero .claim .r{color:var(--red)}
/* ===== preloader: the process becomes a finished product (idea -> life) ===== */
#preload{position:fixed;inset:0;z-index:200;background:var(--paper);display:flex;flex-direction:column;
  align-items:center;justify-content:center;gap:1.5rem;overflow:hidden;
  transition:transform .85s cubic-bezier(.76,0,.24,1)}
#preload.hide{display:none}
#preload.done{transform:translateY(-102%)}
.pl-mark{position:relative;width:min(560px,82vw);display:grid;place-items:center;z-index:1}
.pl-s{grid-area:1/1;width:100%;opacity:0;transform:scale(.985);transition:opacity .45s var(--ease),transform .45s var(--ease)}
.pl-s.on{opacity:1;transform:none}
.pl-s svg{width:100%;height:auto}
.pl-cap{font-family:var(--mono);font-size:clamp(.62rem,1.5vw,.76rem);letter-spacing:.34em;text-transform:uppercase;color:var(--g3);z-index:1;transition:color .45s}
.pl-flood{position:absolute;top:50%;left:54%;width:24px;height:24px;border-radius:50%;background:var(--red);
  transform:translate(-50%,-50%) scale(0);z-index:0}
#preload.flood .pl-flood{transform:translate(-50%,-50%) scale(170);transition:transform .9s cubic-bezier(.65,0,.35,1)}
#preload.flood .pl-cap{color:var(--paper)}
@media(prefers-reduced-motion:reduce){#preload{display:none}}
/* hero replay control */
.replaybtn{margin-top:1.7rem;font-family:var(--mono);font-size:.63rem;letter-spacing:.18em;text-transform:uppercase;
  color:var(--ink);background:none;border:1px solid var(--line);border-radius:24px;padding:.62rem 1.25rem;cursor:pointer;
  transition:background .25s,color .25s,border-color .25s,transform .12s var(--ease)}
.replaybtn:hover{background:var(--red);color:var(--paper);border-color:var(--red)}
.replaybtn:active{transform:scale(.96)}
"""

# ------------------------------------------------------------------ helpers --
def stage(svg,cls=""): return f'<div class="stage {cls}">{svg}</div>'
def capt(b,s,p=""):
    p=f'<p>{p}</p>' if p else ''
    return f'<div class="capt"><b>{b}</b><span>{s}</span>{p}</div>'

# ------------------------------------------------------------------ BRAND -----
brand = f"""
<section class="panel active" id="p-brand" role="tabpanel" aria-labelledby="t-brand">
 <div class="hero">
   <p class="kicker">Brand Book &middot; v1.0</p>
   <h1 class="h1">The brand is the process</h1>
   <div class="lock">{ANI['ens']}</div>
   <p class="claim">Sketched. Stitched. <span class="r">BORN.</span></p>
   <p class="tag">From idea to life</p>
   <p class="hint">The mark builds itself &mdash; sketch, then ink, then the red dot is born</p>
   <button class="replaybtn" id="replayBtn" type="button">&#9654;&nbsp;&nbsp;Watch it come to life</button>
 </div>

 <div class="sec sec--line">
   <p class="eyebrow">01 &middot; The brand at a glance</p>
   <dl class="dl-grid">
     <dt>Name</dt><dd>BORN Studio</dd>
     <dt>Category</dt><dd>Full Service Apparel Development Studio</dd>
     <dt>Master claim</dt><dd>Sketched. Stitched. BORN.</dd>
     <dt>Tagline</dt><dd>From idea to life</dd>
     <dt>Essence</dt><dd>Maturing an idea into a manufacturable product</dd>
     <dt>Archetype</dt><dd>Creator + Caregiver</dd>
     <dt>Ideal client</dt><dd>Emerging founder with vision and capital, no factory network</dd>
     <dt>Three filters</dt><dd>Viability &middot; Cost &middot; Usability</dd>
   </dl>
 </div>

 <div class="sec sec--line">
   <p class="eyebrow">02 &middot; Origin</p>
   <h2 class="h2">A factory studio that does strategic design</h2>
   <p class="prose" style="margin-top:1rem">Mar&iacute;a learned the craft on the production floors of Portugal, Spain, Los Angeles and Austria &mdash; not at a desk, but at the machine. She knows how things are cut and sewn, where they break, and what makes a tech pack executable. The typical designer draws something pretty and throws the problem over the wall to the factory; <b>Mar&iacute;a knows what that problem costs before she draws</b>, and how to prevent it. That is the whole difference.</p>
 </div>

 <div class="sec sec--line">
   <p class="eyebrow">03 &middot; Positioning</p>
   <div class="grid g2" style="margin-top:.6rem">
     <div class="card"><h3>BORN is&hellip;</h3>
       <ul class="list"><li>A studio that takes an idea to a manufacturable product</li>
       <li>Discovery, tech pack, factory match, samples, fitting, bulk oversight</li>
       <li>Factory-floor technical judgment</li>
       <li>A product brand: consistent aesthetic, voice and touchpoints</li></ul></div>
     <div class="card"><h3>BORN is not&hellip;</h3>
       <ul class="list list--no"><li>A factory &mdash; it does not cut or sew</li>
       <li>A sourcing agency &mdash; it does not buy materials for the client</li>
       <li>An incubator &mdash; it does not invest capital or take equity</li>
       <li>A creative design studio &mdash; it does not lead the conceptual aesthetic</li></ul></div>
   </div>
 </div>

 <div class="sec sec--line">
   <p class="eyebrow">04 &middot; Essence &amp; promise</p>
   <h2 class="h2">Three filters against three fears</h2>
   <div class="grid g3" style="margin-top:1.2rem">
     <div class="card"><h3>01 &middot; Viability</h3><p>Can it exist in the physical world?</p></div>
     <div class="card"><h3>02 &middot; Cost</h3><p>Does it leave margin without sacrificing quality?</p></div>
     <div class="card"><h3>03 &middot; Usability</h3><p>Does it work on the body, not just on the sample?</p></div>
   </div>
   <p class="prose" style="margin-top:1.3rem">What BORN really sells is <b>confidence</b>. The tech pack, the sample and the oversight are its tangible forms. The promise &mdash; <b>From idea to life</b> &mdash; the client hands over an idea; BORN hands back life.</p>
 </div>

 <div class="sec sec--line">
   <p class="eyebrow">05 &middot; Verbal architecture</p>
   <h2 class="h2">The claim is the process</h2>
   <p class="prose" style="margin-top:1rem"><b>Sketched</b> is outline &mdash; the idea on paper. <b>Stitched</b> is topstitch &mdash; tested with thread and needle. <b>BORN</b> is solid and alive &mdash; it goes out into the world with the studio's signature. The tagline <em>From idea to life</em> turns the craft into an emotional promise.</p>
 </div>

 <div class="sec sec--line">
   <p class="eyebrow">06 &middot; Voice &amp; tone</p>
   <div class="grid g2" style="margin-top:.6rem">
     <div class="card"><h3>Creator</h3><p>Pushes the idea toward its best version. Never just executes the brief &mdash; it questions it, improves it, takes it one step further.</p></div>
     <div class="card"><h3>Caregiver</h3><p>Protects the founder from costly mistakes. Says &ldquo;don't do this&rdquo; when it sees it, even if it costs the sale.</p></div>
   </div>
   <p class="muted" style="margin-top:1.1rem">Tone &middot; Direct &middot; Warm &middot; Editorial &middot; Bilingual &middot; Precise &middot; With judgment</p>
 </div>

 <div class="fullred">
   <p class="fr-k">The promise</p>
   <h2>From idea<br>to <span class="op">life</span><span style="color:var(--paper)">.</span></h2>
   <div class="bigdot"></div>
   <p class="fr-s">The client hands over an idea &middot; BORN hands back life</p>
 </div>
</section>"""

# ------------------------------------------------------------------ LOGO ------
logo = f"""
<section class="panel" id="p-logo" role="tabpanel" aria-labelledby="t-logo">
 <p class="kicker">The logotype</p>
 <h1 class="h1">Double exposure</h1>
 <p class="lede" style="margin-top:1rem">The word <b>BORN</b> resolved in black with its process-ghost behind it, closed by the red dot. The only thing born in color is the dot.</p>

 <div class="sec">{stage(SVG['wm_principal'])}
   {capt('Primary lockup','BORN + dot + tagline','The construction sketch ghosts behind the word. Every application derives from here.')}</div>

 <div class="sec sec--line">
   <p class="eyebrow">Motion signatures</p>
   <p class="prose" style="margin-bottom:1.3rem">Two live signatures, drawn in real time &mdash; not video, pure vector, so they always render crisp.</p>
   <div class="motion">
     <div><div class="animbox">{ANI['ens']}</div>{capt('Assembly','6s loop','The sketch draws in and assembles into the final word, then the red dot is born.')}</div>
     <div><div class="animbox">{ANI['bar']}</div>{capt('Sweep','5s loop','First the sketch; a sweep prints the letters over the process and the red dot lands last.')}</div>
   </div>
 </div>

 <div class="sec sec--line">
   <p class="eyebrow">The mark by stage &mdash; tap to explore</p>
   <p class="prose" style="margin-bottom:1.4rem">The wordmark lives each phase of the craft. Tap a state and watch it transform &mdash; sketched for the brief, stitched for development, inked and BORN for production.</p>
   <div class="stagex">
     <div class="stagex__disp">
       <div class="sx" data-s="sketch">{SVG['state_sketch']}</div>
       <div class="sx" data-s="stitch">{SVG['state_stitch']}</div>
       <div class="sx" data-s="ink">{SVG['state_ink']}</div>
       <div class="sx" data-s="born">{SVG['state_born']}</div>
     </div>
     <div class="stagex__chips">
       <button class="chip" data-s="sketch">Sketched</button>
       <button class="chip" data-s="stitch">Stitched</button>
       <button class="chip" data-s="ink">Inked</button>
       <button class="chip" data-s="born">BORN</button>
       <span class="chip__auto" data-auto>Auto &#9654;</span>
     </div>
   </div>
 </div>

 <div class="sec sec--line">
   <p class="eyebrow">The icon &mdash; the B</p>
   <div class="grid g4">
     <div><div class="stage stage--sq">{SVG['ic_negativo']}</div>{capt('Negative','Primary','Favicon, avatar, app, seal.')}</div>
     <div><div class="stage stage--sq">{SVG['ic_construccion']}</div>{capt('Construction','Development','Tech packs, work in progress.')}</div>
     <div><div class="stage stage--sq">{SVG['ic_doble']}</div>{capt('Double exposure','Alternate','Solid B with its process-ghost.')}</div>
     <div><div class="stage stage--sq" style="background:var(--paper-3)">{SVG['ic_doble_red']}</div>{capt('Red','Accent','For the BORN stage &amp; highlights.')}</div>
   </div>
 </div>

 <div class="sec sec--line">
   <p class="eyebrow">Negatives &amp; color backgrounds</p>
   <p class="prose" style="margin-bottom:1.4rem">The logo works on paper, on ink and on the red. In negative the word turns ivory; the dot stays red on dark and becomes ink on red to keep contrast.</p>
   <div class="grid g3">
     <div>{stage(SVG['wm_principal'])}<p class="bgnote">Positive &middot; on paper</p></div>
     <div><div class="stage stage--dark">{SVG['wm_principal_neg']}</div><p class="bgnote">Negative &middot; on ink</p></div>
     <div><div class="stage stage--red">{SVG['wm_principal_onred']}</div><p class="bgnote">On Rojo Valentino</p></div>
   </div>
   <div class="grid g3" style="margin-top:1.2rem">
     <div><div class="stage stage--sq">{SVG['ic_negativo']}</div><p class="bgnote">Icon &middot; negative</p></div>
     <div><div class="stage stage--dark">{SVG['wm_solo_neg']}</div><p class="bgnote">Wordmark &middot; negative</p></div>
     <div><div class="stage stage--red">{SVG['wm_solo_onred']}</div><p class="bgnote">Wordmark &middot; on red</p></div>
   </div>
 </div>

 <div class="sec sec--line">
   <p class="eyebrow">Variants</p>
   <div class="grid g2">
     <div>{stage(SVG['wm_sin_slogan'])}{capt('No tagline','Black + dot','The primary without the tagline.')}</div>
     <div>{stage(SVG['wm_solo'])}{capt('Wordmark only','Reduced','Most discreet: word and dot only.')}</div>
     <div>{stage(SVG['wm_ecorojo_slogan'])}{capt('Red echo + tagline','Red lines','Process-ghost in red, with tagline.')}</div>
     <div>{stage(SVG['wm_ecorojo'])}{capt('Red echo','Red lines','Process in red, no tagline.')}</div>
   </div>
 </div>

 <div class="sec sec--line">
   <p class="eyebrow">Incorrect uses</p>
   <ul class="list list--no" style="max-width:60ch">
     <li>Do not distort or change the proportions</li>
     <li>Do not rotate the lockup</li>
     <li>Do not recolor the word &mdash; only the dot is red</li>
     <li>Do not crowd the logo &mdash; keep clear space around it</li>
   </ul>
 </div>
</section>"""

# ------------------------------------------------------------------ COLOR -----
SW=[("Paper","#F1F1EC","Background &middot; the paper"),("Graphite 40","#ABABB0","Development"),
 ("Graphite 60","#78787E","Development"),("Graphite 80","#3C3C40","Development"),
 ("Ink","#151517","Text &middot; ink"),("Rojo Valentino","#C4122E","Pantone 3546 C &middot; life")]
sw_html="".join(f'<div class="sw" data-hex="{h}"><div class="sw__c" style="background:{h}"></div><div class="sw__m"><b>{n}</b><span>{h}</span></div></div>' for n,h,_ in SW)
color = f"""
<section class="panel" id="p-color" role="tabpanel" aria-labelledby="t-color">
 <p class="kicker">Color</p>
 <h1 class="h1">From black &amp; white to life</h1>
 <p class="lede" style="margin-top:1rem">A sketch begins in pencil. Color arrives when the idea comes to life: monochrome graphite as the world of development, and a single red earned on reaching BORN.</p>
 <div class="sec"><div class="grid g3">{sw_html}</div>
 <p class="note">Tap a swatch to copy the hex. For print, use Pantone 3546 C directly.</p></div>
</section>"""

# ------------------------------------------------------------------ TYPE ------
typo = f"""
<section class="panel" id="p-type" role="tabpanel" aria-labelledby="t-type">
 <p class="kicker">Typography</p>
 <h1 class="h1">One Didot, three companions</h1>
 <p class="lede" style="margin-top:1rem">The wordmark is set in <b>Didot</b> &mdash; the typeface of Vogue. The system rests on three families. All four are free, open-source (SIL Open Font License) &mdash; download each family below.</p>
 <div class="sec">
   <div class="spec"><div class="spec-head"><span class="meta">Wordmark &middot; GFS Didot</span><a class="fontdl" href="https://fonts.google.com/download?family=GFS%20Didot" target="_blank" rel="noopener">&#8595; Download family</a></div><div class="samp" style="font-family:var(--word);font-size:clamp(2.4rem,7vw,4.5rem)">BORN.</div></div>
   <div class="spec"><div class="spec-head"><span class="meta">Display &amp; Subhead &middot; Bodoni Moda</span><a class="fontdl" href="https://fonts.google.com/download?family=Bodoni%20Moda" target="_blank" rel="noopener">&#8595; Download family</a></div><div class="samp" style="font-family:var(--serif);font-weight:900;font-size:clamp(1.8rem,5vw,3rem)">Sketched. Stitched. BORN.</div><div class="samp" style="font-family:var(--serif6);font-weight:600;font-size:clamp(1.2rem,2.6vw,1.7rem);margin-top:.3rem">Full Service Apparel Development</div></div>
   <div class="spec"><div class="spec-head"><span class="meta">Body &middot; Jost</span><a class="fontdl" href="https://fonts.google.com/download?family=Jost" target="_blank" rel="noopener">&#8595; Download family</a></div><div class="samp" style="font-family:var(--sans);font-size:clamp(1.05rem,2vw,1.35rem);line-height:1.5">The studio where a fashion idea matures until it becomes a manufacturable product.</div></div>
   <div class="spec"><div class="spec-head"><span class="meta">Technical &middot; Space Mono</span><a class="fontdl" href="https://fonts.google.com/download?family=Space%20Mono" target="_blank" rel="noopener">&#8595; Download family</a></div><div class="samp" style="font-family:var(--mono);font-size:clamp(.8rem,1.6vw,1rem);letter-spacing:.05em">PHASE 01 &middot; SKETCHED &middot; TECH PACK v1 &middot; 1&ndash;3 WEEKS</div></div>
 </div>
 <p class="note">Fonts open in Google Fonts to download the complete family. <b>GFS Didot</b> is the free revival used here; Vogue's Didot is proprietary &mdash; if the licensed file is available, it substitutes 1:1.</p>
</section>"""

# ------------------------------------------------------------------ APPS ------
apps = f"""
<section class="panel" id="p-apps" role="tabpanel" aria-labelledby="t-apps">
 <p class="kicker">Applications</p>
 <h1 class="h1">The identity evolves with the service</h1>
 <p class="lede" style="margin-top:1rem">Not just a logo: a language that changes state with the phase. The brief speaks in sketch, development in stitch, production in solid with color.</p>
 <div class="sec"><div class="grid g3">
   <div class="phase"><div class="phase__logo">{SVG['state_sketch']}</div><div class="phase__b"><span class="n">Phase 01</span><h3>Sketched</h3><p class="card" style="border:0;padding:0;background:none"><span>Sketch grid, pencil outline, graphite. Everything is drawn.</span></p><p class="muted" style="margin-top:.7rem">Brief &middot; Moodboard &middot; Tech pack</p></div></div>
   <div class="phase"><div class="phase__logo">{SVG['state_stitch']}</div><div class="phase__b"><span class="n">Phase 02</span><h3>Stitched</h3><p class="card" style="border:0;padding:0;background:none"><span>Topstitch, thread. The idea is tested and sewn.</span></p><p class="muted" style="margin-top:.7rem">Sample tag &middot; Fitting &middot; Development</p></div></div>
   <div class="phase"><div class="phase__logo">{SVG['state_born']}</div><div class="phase__b"><span class="n">Phase 03</span><h3>BORN</h3><p class="card" style="border:0;padding:0;background:none"><span>Solid, in color. The product goes out into the world.</span></p><p class="muted" style="margin-top:.7rem">Hangtag &middot; Drop &middot; Campaign</p></div></div>
 </div></div>

 <div class="sec sec--line">
   <p class="eyebrow">The icon per stage</p>
   <div class="grid g4">
     <div><div class="stage stage--sq">{SVG['ic_construccion']}</div><p class="bgnote">Sketched &middot; construction</p></div>
     <div><div class="stage stage--sq">{SVG['ic_doble']}</div><p class="bgnote">Development &middot; double exp.</p></div>
     <div><div class="stage stage--sq" style="background:var(--paper-3)">{SVG['ic_doble_red']}</div><p class="bgnote">BORN &middot; red</p></div>
     <div><div class="stage stage--sq stage--dark">{SVG['ic_negativo']}</div><p class="bgnote">Seal &middot; negative</p></div>
   </div>
 </div>

 <div class="sec sec--line">
   <p class="eyebrow">The journey &middot; three phases</p>
   <div class="grid g3">
     <div class="card"><span class="muted">1&ndash;3 weeks</span><h3 style="margin-top:.4rem">The Briefing</h3><ul class="list"><li>Discovery and the three filters</li><li>Edited moodboard</li><li>Production-ready tech pack</li></ul></div>
     <div class="card"><span class="muted">2&ndash;6 months</span><h3 style="margin-top:.4rem">The Development</h3><ul class="list"><li>Factory pairing and contract</li><li>Sample and documented fitting</li><li>Final approved sample</li></ul></div>
     <div class="card"><span class="muted">4&ndash;8 weeks</span><h3 style="margin-top:.4rem">Production Oversight</h3><ul class="list"><li>Size set and signed PPS</li><li>Order and bulk oversight</li><li>Documented handover</li></ul></div>
   </div>
 </div>

 <div class="fullred">
   <p class="fr-k">The seal</p>
   <h2>Everything is made<br>to be <span class="op">B</span>OR<span class="op">N</span></h2>
   <div class="bigdot"></div>
   <p class="fr-s">Sketched to be BORN &middot; Stitched to be BORN &middot; Made to be BORN</p>
 </div>
</section>"""

# ------------------------------------------------------------------ DOWNLOADS -
DARKBG={"wm_principal_neg","wm_solo_neg","state_sketch","state_stitch"}  # ivory/light marks need dark preview
def ki_png(key):
    bg=""
    if key in {"wm_principal_neg","wm_solo_neg"}: bg=' style="background:var(--ink)"'
    elif key in {"wm_principal_onred"}: bg=' style="background:var(--red)"'
    return (f'<div class="ki"><div class="ki__p"{bg}>{SVG[key]}</div>'
      f'<div class="ki__m"><b>{TITLE[key]}</b><span class="ki__f">PNG &middot; transparent</span>'
      f'<div class="dls"><a class="dl" href="{PNG[key]}" download="{DL[key]}">Download PNG</a>'
      f'<a class="dl dl--ghost" data-open="1" title="Open in a new tab">Open</a></div></div></div>')
def ki_vid(pref,title,dlm,dlw,anim):
    return (f'<div class="ki"><div class="ki__p">{anim}</div>'
      f'<div class="ki__m"><b>{title}</b><span class="ki__f">MP4 + WebM &middot; loop</span>'
      f'<div class="dls"><a class="dl" data-dl="{pref}_mp4" download="{dlm}">MP4</a>'
      f'<a class="dl" data-dl="{pref}_webm" download="{dlw}">WebM</a>'
      f'<a class="dl dl--ghost" data-open="1" title="Open in a new tab">Open</a></div></div></div>')
kit_items="".join(ki_png(k) for k,_,_ in KIT)
kit_items+=ki_vid("ens","Assembly animation","BORN-assembly.mp4","BORN-assembly.webm",ANI['ens'])
kit_items+=ki_vid("bar","Sweep animation","BORN-sweep.mp4","BORN-sweep.webm",ANI['bar'])
desc = f"""
<section class="panel" id="p-desc" role="tabpanel" aria-labelledby="t-desc">
 <p class="kicker">Downloads</p>
 <h1 class="h1">Brand kit</h1>
 <p class="lede" style="margin-top:1rem">Every file, ready for the team. <b>Download</b> saves the piece to your device; if your browser blocks it, <b>Open</b> shows it in a new tab to save by hand.</p>
 <div class="sec"><div class="dls" style="margin-bottom:.4rem"><a class="dl dl--big" href="{ZIP_URI}" download="BORN-Studio-Kit.zip">&#8681; Download everything (ZIP)</a></div>
 <div class="kit">{kit_items}</div>
 <p class="note">Files go to your device's <b>Downloads</b> folder. High-resolution PNG (2700&ndash;4800&nbsp;px), transparent background. Animations as MP4 (universal) and WebM. Vector SVG/PDF for print and embroidery can be exported from these same files.</p></div>
</section>"""

# ------------------------------------------------------------------ EXPLORATION
expl = ('<section class="panel" id="p-expl" role="tabpanel" aria-labelledby="t-expl">'
 '<p class="kicker">Appendix &middot; development</p><h1 class="h1">Logo exploration</h1>'
 '<p class="lede" style="margin-top:1rem">The full lab behind the decision: every route we worked &mdash; double and triple exposure, continuous field, ligatures, progression, signatures, animations and icons. Working material, not the final brand.</p>'
 '<div class="sec"><div class="expl-bar"><b>Exploration board &middot; BORN</b>'
 '<a id="explFull" href="#">Open full screen &rarr;</a></div>'
 '<iframe class="expl-frame" title="BORN logo exploration" loading="lazy" allow="fullscreen" allowfullscreen srcdoc="'+EXPL_ESC+'"></iframe></div></section>')

# ------------------------------------------------------------------ shell -----
TABS=[("brand","Brand"),("logo","Logo"),("color","Color"),("type","Typography"),("apps","Applications"),("desc","Downloads"),("expl","Exploration")]
tabbtns="".join(f'<button class="tab" role="tab" id="t-{k}" aria-controls="p-{k}" aria-selected="{"true" if i==0 else "false"}" data-tab="{k}">{lab}</button>' for i,(k,lab) in enumerate(TABS))
header = f"""
<header class="top"><div class="top__in">
 <a class="brand" href="#" data-tab="brand" aria-label="BORN Studio">{SVG['wm_solo']}</a>
 <button class="menu-btn" id="menuBtn" type="button" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
 <nav class="tabs" role="tablist" aria-label="Sections">{tabbtns}</nav>
</div><div class="bar" id="bar"></div></header>"""
footer = f"""
<footer class="foot"><div class="fm">{SVG['wm_solo']}</div>
 <p>BORN Studio &middot; Full Service Apparel Development<br>Brand Book v1.0 &middot; From idea to life<br>Strategy &amp; brand &mdash; Matisis Consultancy</p></footer>"""

VMAP={"ens_mp4":VID['ens_mp4'],"ens_webm":VID['ens_webm'],"bar_mp4":VID['bar_mp4'],"bar_webm":VID['bar_webm']}
JS = "<script>(function(){var V="+json.dumps(VMAP)+";" + r"""
 document.querySelectorAll('a[data-dl]').forEach(function(a){var u=V[a.getAttribute('data-dl')]; if(u)a.setAttribute('href',u);});
 // Primary Download buttons are native <a download> anchors (most compatible).
 // The ghost "Open" buttons view the asset in a new tab as a fallback where the
 // sandbox blocks downloads.
 function toBlob(uri){var c=uri.split(','),m=(c[0].match(/:(.*?);/)||[])[1]||'application/octet-stream';
   var b=atob(c[1]),n=b.length,u=new Uint8Array(n);while(n--)u[n]=b.charCodeAt(n);return new Blob([u],{type:m});}
 function openTab(uri){try{var url=URL.createObjectURL(toBlob(uri));if(!window.open(url,'_blank'))location.href=url;
   setTimeout(function(){URL.revokeObjectURL(url);},60000);}catch(e){}}
 document.querySelectorAll('a.dl--ghost[data-open]').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();
   var s=a.parentNode.querySelector('a.dl:not(.dl--ghost)');var uri=s?(s.getAttribute('href')||V[s.getAttribute('data-dl')]):'';
   if(uri)openTab(uri);});});
 // open the exploration board full screen (Fullscreen API; fallback: new tab)
 var explFull=document.getElementById('explFull');
 if(explFull)explFull.addEventListener('click',function(e){e.preventDefault();
   var f=document.querySelector('.expl-frame');if(!f)return;
   var req=f.requestFullscreen||f.webkitRequestFullscreen||f.mozRequestFullScreen||f.msRequestFullscreen;
   if(req){try{var pr=req.call(f);if(pr&&pr.catch)pr.catch(function(){explOpen(f);});return;}catch(err){}}
   explOpen(f);});
 function explOpen(f){try{var b=new Blob([f.getAttribute('srcdoc')],{type:'text/html'});var u=URL.createObjectURL(b);
   if(!window.open(u,'_blank')){location.href=u;}setTimeout(function(){URL.revokeObjectURL(u);},60000);}catch(e){}}
 // ---- progressive-enhancement flags + staggered scroll-reveal ----
 var reduce=matchMedia('(prefers-reduced-motion:reduce)').matches;
 var root=document.documentElement; root.classList.add('js'); if(reduce)root.classList.add('reduce');
 // ---- preloader: Sketched -> Stitched -> Inked -> BORN, then a red flood (idea -> life) ----
 var pl=document.getElementById('preload'),plNames=['Sketched','Stitched','Inked','BORN'];
 function playPreload(){if(!pl)return;var slides=[].slice.call(pl.querySelectorAll('.pl-s')),cap=pl.querySelector('.pl-cap');
   if(pl._t)pl._t.forEach(clearTimeout);pl._t=[];pl.classList.remove('hide','done','flood');
   function s(i){slides.forEach(function(x){x.classList.toggle('on',+x.getAttribute('data-i')===i);});}
   s(0);cap.textContent=plNames[0];
   pl._t.push(setTimeout(function(){s(1);cap.textContent=plNames[1];},520));
   pl._t.push(setTimeout(function(){s(2);cap.textContent=plNames[2];},1040));
   pl._t.push(setTimeout(function(){s(3);cap.textContent=plNames[3];},1560));
   pl._t.push(setTimeout(function(){pl.classList.add('flood');s(4);cap.textContent='From idea to life';},2200));
   pl._t.push(setTimeout(function(){pl.classList.add('done');},3050));
   pl._t.push(setTimeout(function(){pl.classList.add('hide');},3950));}
 if(pl){var seen;try{seen=sessionStorage.getItem('born_seen');}catch(e){}
   if(reduce||seen){pl.classList.add('hide');}else{playPreload();try{sessionStorage.setItem('born_seen','1');}catch(e){}}}
 var replayBtn=document.getElementById('replayBtn');
 if(replayBtn)replayBtn.addEventListener('click',function(){if(pl){pl.classList.remove('hide');playPreload();}});
 var RVSEL='.kicker,.h1,.h2,.lede,.prose,.card,.spec,.stage,.stagex,.sw,.ki,.phase,.fullred,.dl-grid,.motion,.animbox';
 var io=(!reduce&&'IntersectionObserver' in window)?new IntersectionObserver(function(es){
   es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target);}});},
   {threshold:.08,rootMargin:'0px 0px -6% 0px'}):null;
 // ---- tabs + sweep transition + mobile menu ----
 var tabs=[].slice.call(document.querySelectorAll('[role=tab]'));
 var panels=[].slice.call(document.querySelectorAll('.panel'));
 var sweep=document.querySelector('.sweepline'),topbar=document.querySelector('.top'),menuBtn=document.getElementById('menuBtn');
 function closeMenu(){if(topbar)topbar.classList.remove('open');if(menuBtn)menuBtn.setAttribute('aria-expanded','false');}
 function show(k){tabs.forEach(function(t){t.setAttribute('aria-selected',t.dataset.tab===k?'true':'false');});
   panels.forEach(function(p){p.classList.toggle('active',p.id==='p-'+k);});window.scrollTo(0,0);
   if(history.replaceState)history.replaceState(null,'','#'+k);}
 function go(k){var cur=document.querySelector('.panel.active');closeMenu();
   if(cur&&cur.id==='p-'+k)return;
   if(sweep&&!reduce){sweep.classList.remove('run');void sweep.offsetWidth;sweep.classList.add('run');}
   var p=document.getElementById('p-'+k);
   var els=p?[].slice.call(p.querySelectorAll(RVSEL)):[];
   els.forEach(function(el){el.classList.add('rv');el.classList.remove('in');el.style.transitionDelay='';}); // hide while still display:none
   show(k);                                                                                                   // now visible, scrolled to top
   if(!io){els.forEach(function(el){el.classList.add('in');});return;}
   els.forEach(function(el,i){el.style.transitionDelay=(Math.min(i,9)*55)+'ms';io.observe(el);});             // cascade in-view, reveal rest on scroll
 }
 if(menuBtn)menuBtn.addEventListener('click',function(){var o=topbar.classList.toggle('open');menuBtn.setAttribute('aria-expanded',o?'true':'false');});
 document.addEventListener('click',function(e){if(topbar&&topbar.classList.contains('open')&&!e.target.closest('.top'))closeMenu();});
 document.body.addEventListener('click',function(e){var el=e.target.closest('[data-tab]');if(!el)return;e.preventDefault();go(el.dataset.tab);});
 var start=(location.hash||'').replace('#','');show(start&&document.getElementById('p-'+start)?start:'brand');
 // ---- interactive stage explorer ----
 document.querySelectorAll('.stagex').forEach(function(sx){
   var slides=[].slice.call(sx.querySelectorAll('.sx')),chips=[].slice.call(sx.querySelectorAll('.chip[data-s]'));
   var auto=sx.querySelector('[data-auto]'),order=['sketch','stitch','ink','born'],i=0,timer=null;
   function set(s){slides.forEach(function(sl){sl.classList.toggle('on',sl.getAttribute('data-s')===s);});
     chips.forEach(function(c){c.setAttribute('aria-pressed',c.getAttribute('data-s')===s?'true':'false');});i=order.indexOf(s);}
   function stop(){if(timer){clearInterval(timer);timer=null;if(auto)auto.style.display='none';}}
   chips.forEach(function(c){c.addEventListener('click',function(){stop();set(c.getAttribute('data-s'));});});
   set('sketch');timer=setInterval(function(){i=(i+1)%order.length;set(order[i]);},1700);});
 // ---- red cursor companion (fine pointers) ----
 var rdot=document.querySelector('.rdot');
 if(rdot&&matchMedia('(hover:hover) and (pointer:fine)').matches){
   var tx=innerWidth/2,ty=innerHeight/2,rx=tx,ry=ty;
   addEventListener('mousemove',function(e){tx=e.clientX;ty=e.clientY;rdot.style.opacity='.9';});
   addEventListener('mouseout',function(e){if(!e.relatedTarget)rdot.style.opacity='0';});
   document.addEventListener('mouseover',function(e){rdot.classList.toggle('big',!!e.target.closest('a,button,.card,.sw,.chip,.stage,.ki'));});
   (function loop(){rx+=(tx-rx)*.2;ry+=(ty-ry)*.2;rdot.style.left=rx+'px';rdot.style.top=ry+'px';rdot.style.transform='translate(-50%,-50%)';requestAnimationFrame(loop);})();
 }
 // ---- copy hex ----
 var toast=document.querySelector('.toast');
 function tst(m){if(!toast)return;toast.textContent=m;toast.classList.add('on');clearTimeout(toast._t);toast._t=setTimeout(function(){toast.classList.remove('on');},1400);}
 document.querySelectorAll('.sw').forEach(function(s){s.addEventListener('click',function(){var h=s.dataset.hex||'';
   if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(h).then(function(){tst(h+'  copied');},function(){tst(h);});}else{tst(h);}});});
 // ---- scroll progress ----
 var bar=document.getElementById('bar');
 addEventListener('scroll',function(){var d=document.documentElement,s=d.scrollHeight-d.clientHeight;bar.style.width=(s>0?(d.scrollTop/s*100):0)+'%';},{passive:true});
})();</script>"""

OVERLAYS = '<div class="sweepline" aria-hidden="true"></div><div class="rdot" aria-hidden="true"></div>'
PRELOAD = ('<div id="preload" aria-hidden="true"><div class="pl-mark">'
  '<div class="pl-s" data-i="0">'+SVG['state_sketch']+'</div>'
  '<div class="pl-s" data-i="1">'+SVG['state_stitch']+'</div>'
  '<div class="pl-s" data-i="2">'+SVG['state_ink']+'</div>'
  '<div class="pl-s" data-i="3">'+SVG['state_born']+'</div>'
  '<div class="pl-s pl-cream" data-i="4">'+SVG['wm_solo_onred']+'</div>'
  '</div><div class="pl-cap">Sketched</div><div class="pl-flood"></div></div>')
body = (PRELOAD + DEFS + header + '<main class="wrap">'+brand+logo+color+typo+apps+desc+expl+'</main>'
        + footer + '<div class="toast" role="status"></div>' + OVERLAYS + JS)
head = "<style>\n"+FONTS+"\n"+CSS+"\n</style>"

artifact = "<title>BORN Studio &mdash; Brand Book</title>\n"+head+"\n"+body
open(f"{W}/artifact.html","w",encoding="utf-8").write(artifact)
landing = ("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
  "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
  "<title>BORN Studio &mdash; From idea to life</title>\n"
  "<meta name=\"description\" content=\"BORN Studio &mdash; Full Service Apparel Development. Brand book.\">\n"
  "<meta name=\"theme-color\" content=\"#F2EEE6\">\n"
  f"<link rel=\"icon\" href=\"{FAVICON}\">\n"+head+"\n</head>\n<body>\n"+body+"\n</body>\n</html>\n")
open("index.html","w",encoding="utf-8").write(landing)
print("index.html:",round(len(landing)/1024),"KB  artifact.html:",round(len(artifact)/1024),"KB")
