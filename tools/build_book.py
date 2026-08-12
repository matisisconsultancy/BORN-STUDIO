#!/usr/bin/env python3
"""BORN Studio brand book — clean tabbed rebuild.
Sections: Marca / Logo / Color / Tipografia / Aplicaciones / Descargas.
Only the final doble-exposicion logo system. Downloads use real <a download>
anchors (work inside the artifact sandbox). One consistent logo in the chrome
(header + footer + favicon). Emits index.html (standalone) and
tools/_work/artifact.html (body form for the Artifact tool)."""
import base64, os, re, json

W="tools/_work"; A="assets/logos"
rd=lambda p: open(p, encoding="utf-8").read()
def datauri(path, mime):
    return f"data:{mime};base64,"+base64.b64encode(open(path,"rb").read()).decode("ascii")

FONTS = rd(f"{W}/fonts.css")
ROOT  = rd(f"{W}/root.css")
SVG   = {k: rd(f"{W}/{k}.svg") for k in
         ["wm_principal","wm_sin_slogan","wm_solo","wm_ecorojo_slogan","wm_ecorojo",
          "ic_negativo","ic_construccion","ic_doble",
          "wm_principal_neg","wm_principal_onred","wm_solo_neg","wm_solo_onred"]}
PNG   = {k: datauri(f"{A}/{k}.png","image/png") for k in SVG}
# exploration board (development) — embedded in a secondary tab, escaped for srcdoc
EXPL_RAW = rd("logos.html")
EXPL_ESC = EXPL_RAW.replace("&","&amp;").replace('"',"&quot;")
VID   = {
  "ens_mp4":datauri(f"{A}/an_ensamblaje.mp4","video/mp4"),
  "ens_webm":datauri(f"{A}/an_ensamblaje.webm","video/webm"),
  "ens_pos":datauri(f"{A}/an_ensamblaje_poster.png","image/png"),
  "bar_mp4":datauri(f"{A}/an_barrida.mp4","video/mp4"),
  "bar_webm":datauri(f"{A}/an_barrida.webm","video/webm"),
  "bar_pos":datauri(f"{A}/an_barrida_poster.png","image/png"),
}
FAVICON=("data:image/svg+xml,%3Csvg%20xmlns='http://www.w3.org/2000/svg'%20viewBox='0%200%2064%2064'"
 "%3E%3Crect%20width='64'%20height='64'%20rx='13'%20fill='%231B1720'/%3E"
 "%3Ctext%20x='29'%20y='47'%20font-family='Georgia,Times,serif'%20font-size='46'%20font-weight='700'"
 "%20text-anchor='middle'%20fill='%23F2EEE6'%3EB%3C/text%3E"
 "%3Ccircle%20cx='47'%20cy='44'%20r='5'%20fill='%23C4122E'/%3E%3C/svg%3E")

# ---------------------------------------------------------------- CSS --------
CSS = ROOT + r"""
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{background:var(--paper);color:var(--ink);font-family:var(--sans);
  -webkit-font-smoothing:antialiased;line-height:1.6}
img,svg,video{display:block;max-width:100%}
a{color:inherit}
.wrap{max-width:1120px;margin:0 auto;padding:0 clamp(1.25rem,5vw,3rem)}
/* ---- top bar ---- */
.top{position:sticky;top:0;z-index:50;background:rgba(242,238,230,.9);
  backdrop-filter:blur(10px);border-bottom:1px solid var(--line)}
.top__in{display:flex;align-items:center;gap:1.2rem;max-width:1120px;margin:0 auto;
  padding:.7rem clamp(1.25rem,5vw,3rem);flex-wrap:wrap}
.brand{display:flex;align-items:center;gap:.6rem;text-decoration:none;flex:0 0 auto}
.brand .mark{width:34px;height:34px}
.brand .mark svg{width:100%;height:100%}
.brand b{font-family:var(--word);font-weight:400;font-size:1.15rem;letter-spacing:.02em;line-height:1}
.brand span{font-family:var(--mono);font-size:.54rem;letter-spacing:.24em;text-transform:uppercase;color:var(--g3);display:block;margin-top:2px}
.tabs{display:flex;gap:.2rem;margin-left:auto;flex-wrap:wrap}
.tab{font-family:var(--mono);font-size:.68rem;letter-spacing:.12em;text-transform:uppercase;
  color:var(--g2);background:none;border:0;cursor:pointer;padding:.55rem .8rem;border-radius:7px;
  white-space:nowrap;transition:color .2s,background .2s}
.tab:hover{color:var(--ink);background:var(--paper-2)}
.tab[aria-selected=true],.tab[aria-selected=true]:hover{color:var(--paper);background:var(--ink)}
.bar{height:2px;background:var(--red);width:0;transition:width .15s linear}
/* ---- panels ---- */
.panel{display:none;padding:clamp(2.4rem,6vw,4.5rem) 0 clamp(3rem,8vw,6rem);animation:fade .5s var(--ease)}
.panel.active{display:block}
@keyframes fade{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
@media(prefers-reduced-motion:reduce){.panel{animation:none}}
.kicker{font-family:var(--mono);font-size:.66rem;letter-spacing:.22em;text-transform:uppercase;color:var(--red);margin-bottom:.7rem}
.h1{font-family:var(--serif);font-weight:900;font-size:clamp(2.2rem,6vw,4rem);line-height:.98;letter-spacing:-.02em;text-wrap:balance}
.h2{font-family:var(--serif);font-weight:900;font-size:clamp(1.5rem,3.4vw,2.3rem);line-height:1.05;letter-spacing:-.01em;margin:0 0 .2rem}
.h3{font-family:var(--serif6);font-weight:600;font-size:1.2rem;margin:0 0 .3rem}
.lede{font-family:var(--serif6);font-weight:600;font-size:clamp(1.15rem,2vw,1.5rem);line-height:1.4;color:var(--g2);max-width:34ch}
.prose{font-size:clamp(1rem,1.3vw,1.12rem);line-height:1.65;color:var(--g2);max-width:64ch}
.prose b,.prose strong{color:var(--ink)}
.sec{margin-top:clamp(2.6rem,6vw,4.5rem)}
.sec--line{border-top:1px solid var(--line);padding-top:clamp(2.2rem,5vw,3.4rem)}
.eyebrow{font-family:var(--mono);font-size:.64rem;letter-spacing:.2em;text-transform:uppercase;color:var(--g3);margin-bottom:1.1rem}
.grid{display:grid;gap:1.2rem}
.g2{grid-template-columns:repeat(auto-fit,minmax(260px,1fr))}
.g3{grid-template-columns:repeat(auto-fit,minmax(210px,1fr))}
.g4{grid-template-columns:repeat(auto-fit,minmax(170px,1fr))}
.card{background:var(--paper-2);border:1px solid var(--line);border-radius:12px;padding:1.4rem 1.5rem}
.card h3{font-family:var(--serif6);font-weight:600;font-size:1.08rem;margin-bottom:.4rem}
.card p{font-size:.93rem;color:var(--g2);line-height:1.55}
.muted{font-family:var(--mono);font-size:.62rem;letter-spacing:.1em;text-transform:uppercase;color:var(--g3)}
/* at a glance table */
.dl-grid{display:grid;grid-template-columns:max-content 1fr;gap:.6rem 1.6rem;font-size:1rem}
.dl-grid dt{font-family:var(--mono);font-size:.64rem;letter-spacing:.12em;text-transform:uppercase;color:var(--g3);align-self:center}
.dl-grid dd{color:var(--ink);font-family:var(--serif6);font-weight:600;font-size:1.05rem}
/* lists */
.list{list-style:none;display:grid;gap:.55rem}
.list li{padding-left:1.4rem;position:relative;color:var(--g2);line-height:1.5}
.list li::before{content:'';position:absolute;left:0;top:.62em;width:8px;height:2px;background:var(--red)}
.list--no li::before{background:var(--g4);width:8px;height:8px;border-radius:50%;top:.5em}
/* hero (Marca) */
.hero{text-align:center;padding:clamp(1rem,4vw,2.5rem) 0 0}
.hero .lock{width:min(680px,92%);margin:1.6rem auto 1.2rem}
.hero .claim{font-family:var(--serif);font-weight:900;font-size:clamp(1.3rem,3vw,2rem);letter-spacing:-.01em}
.hero .claim .r{color:var(--red)}
.hero .tag{font-family:var(--mono);font-size:.7rem;letter-spacing:.28em;text-transform:uppercase;color:var(--g3);margin-top:.7rem}
/* logo displays */
.stage{background:var(--paper-2);border:1px solid var(--line);border-radius:14px;
  display:flex;align-items:center;justify-content:center;padding:clamp(1.8rem,5vw,3.4rem)}
.stage svg{width:100%;height:auto}
.stage--sq{aspect-ratio:1/1;max-width:none}
.stage--sq svg{width:70%}
.stage--dark{background:var(--ink);border-color:transparent}
.stage--red{background:var(--red);border-color:transparent}
.bgnote{font-family:var(--mono);font-size:.6rem;letter-spacing:.1em;text-transform:uppercase;color:var(--g3);margin-top:.5rem}
.expl-bar{display:flex;align-items:center;justify-content:space-between;gap:1rem;flex-wrap:wrap;
  background:var(--ink);color:var(--paper);border-radius:12px 12px 0 0;padding:.75rem 1.1rem;margin-top:1.4rem}
.expl-bar b{font-family:var(--mono);font-size:.66rem;letter-spacing:.14em;text-transform:uppercase;font-weight:400}
.expl-bar a{font-family:var(--mono);font-size:.62rem;letter-spacing:.1em;color:var(--paper);text-decoration:none;
  border:1px solid rgba(242,238,230,.4);padding:.35rem .75rem;border-radius:6px}
.expl-bar a:hover{background:var(--paper);color:var(--ink)}
.expl-frame{width:100%;height:80vh;min-height:540px;border:1px solid var(--line);border-top:0;
  border-radius:0 0 12px 12px;background:#fff;display:block}
@media(max-width:620px){.expl-frame{height:72vh;min-height:440px}.expl-bar a{display:none}}
.capt{margin-top:.7rem}
.capt b{font-family:var(--serif6);font-weight:600;font-size:1.02rem;display:block}
.capt span{font-family:var(--mono);font-size:.6rem;letter-spacing:.1em;text-transform:uppercase;color:var(--g3)}
.capt p{font-size:.88rem;color:var(--g2);line-height:1.5;margin-top:.35rem}
.motion{display:grid;gap:1.4rem;grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}
.motion video{width:100%;border:1px solid var(--line);border-radius:12px;background:var(--paper-2)}
/* color swatches */
.sw{border:1px solid var(--line);border-radius:12px;overflow:hidden;cursor:pointer;background:var(--paper-2)}
.sw__c{height:104px}
.sw__m{padding:.7rem .85rem}
.sw__m b{font-family:var(--serif6);font-weight:600;font-size:.95rem;display:block}
.sw__m span{font-family:var(--mono);font-size:.66rem;color:var(--g3);letter-spacing:.05em}
/* type specimens */
.spec{border-top:1px solid var(--line);padding:1.3rem 0;display:grid;gap:.3rem}
.spec .meta{font-family:var(--mono);font-size:.62rem;letter-spacing:.12em;text-transform:uppercase;color:var(--g3)}
.spec .samp{color:var(--ink);line-height:1.1}
/* phases */
.phase{border:1px solid var(--line);border-radius:12px;padding:1.4rem 1.5rem;background:var(--paper-2)}
.phase .n{font-family:var(--mono);font-size:.62rem;letter-spacing:.14em;text-transform:uppercase;color:var(--red)}
.phase h3{font-family:var(--serif);font-weight:900;font-size:1.5rem;margin:.2rem 0 .5rem}
/* downloads */
.kit{display:grid;gap:1.2rem;grid-template-columns:repeat(auto-fill,minmax(230px,1fr))}
.ki{display:flex;flex-direction:column;background:var(--paper-2);border:1px solid var(--line);border-radius:12px;overflow:hidden}
.ki__p{background:var(--paper);display:flex;align-items:center;justify-content:center;padding:1.1rem;min-height:130px}
.ki__p img,.ki__p video{max-width:100%;max-height:150px;width:auto;height:auto}
.ki__m{padding:.85rem 1.05rem;border-top:1px solid var(--line);display:flex;flex-direction:column;gap:.55rem;flex:1}
.ki__m b{font-family:var(--sans7);font-size:.93rem}
.ki__f{font-family:var(--mono);font-size:.6rem;letter-spacing:.1em;text-transform:uppercase;color:var(--g3)}
.dls{display:flex;gap:.5rem;flex-wrap:wrap;margin-top:auto}
.dl{font-family:var(--mono);font-size:.62rem;letter-spacing:.08em;text-transform:uppercase;color:var(--paper);
  background:var(--ink);border-radius:6px;padding:.55rem .85rem;text-decoration:none;transition:background .2s,color .2s;cursor:pointer}
.dl:hover{background:var(--red)}
.dl--ghost{background:transparent;color:var(--g2);border:1px solid var(--line)}
.dl--ghost:hover{background:var(--paper-3);color:var(--ink)}
.note{font-family:var(--mono);font-size:.7rem;letter-spacing:.04em;color:var(--g3);line-height:1.6;margin-top:1.5rem}
/* footer */
.foot{border-top:1px solid var(--line);padding:clamp(2.4rem,6vw,4rem) 0;text-align:center}
.foot .fm{width:min(320px,64%);margin:0 auto 1.2rem}
.foot p{font-family:var(--mono);font-size:.66rem;letter-spacing:.1em;color:var(--g3);line-height:1.9}
.toast{position:fixed;left:50%;bottom:24px;transform:translateX(-50%) translateY(20px);opacity:0;
  background:var(--ink);color:var(--paper);font-family:var(--mono);font-size:.7rem;letter-spacing:.1em;
  padding:.6rem 1rem;border-radius:8px;pointer-events:none;transition:.3s;z-index:60}
.toast.on{opacity:1;transform:translateX(-50%) translateY(0)}
@media(max-width:620px){
  .tabs{width:100%;margin-left:0;overflow-x:auto;-webkit-overflow-scrolling:touch}
  .brand{flex:1 1 100%}
}
"""

# ---------------------------------------------------------------- helpers ----
def stage(svg, cls=""):  return f'<div class="stage {cls}">{svg}</div>'
def capt(b,s,p=""):
    p=f'<p>{p}</p>' if p else ''
    return f'<div class="capt"><b>{b}</b><span>{s}</span>{p}</div>'

# ---------------------------------------------------------------- MARCA -------
marca = f"""
<section class="panel active" id="p-marca" role="tabpanel" aria-labelledby="t-marca">
 <div class="hero">
   <p class="kicker">Brand Book &middot; v1.0</p>
   <h1 class="h1">La marca es el proceso</h1>
   <div class="lock">{SVG['wm_principal']}</div>
   <p class="claim">Sketched. Stitched. <span class="r">BORN.</span></p>
   <p class="tag">From idea to life</p>
 </div>

 <div class="sec sec--line">
   <p class="eyebrow">01 &middot; La marca de un vistazo</p>
   <dl class="dl-grid">
     <dt>Nombre</dt><dd>BORN Studio</dd>
     <dt>Categor&iacute;a</dt><dd>Full Service Apparel Development Studio</dd>
     <dt>Master claim</dt><dd>Sketched. Stitched. BORN.</dd>
     <dt>Tagline</dt><dd>From idea to life</dd>
     <dt>Esencia</dt><dd>Maduraci&oacute;n de una idea hasta un producto manufacturable</dd>
     <dt>Arquetipo</dt><dd>Creator + Caregiver</dd>
     <dt>Cliente ideal</dt><dd>Founder emergente con visi&oacute;n y capital, sin red de f&aacute;bricas</dd>
     <dt>Tres filtros</dt><dd>Viabilidad &middot; Costo &middot; Usabilidad</dd>
   </dl>
 </div>

 <div class="sec sec--line">
   <p class="eyebrow">02 &middot; Origen</p>
   <h2 class="h2">Un estudio de f&aacute;brica que hace dise&ntilde;o estrat&eacute;gico</h2>
   <p class="prose" style="margin-top:1rem">Mar&iacute;a aprendi&oacute; el oficio en los pisos de producci&oacute;n de Portugal, Espa&ntilde;a, Los &Aacute;ngeles y Austria. No en el escritorio: en la m&aacute;quina. Sabe c&oacute;mo se corta, c&oacute;mo se cose, d&oacute;nde se rompen las cosas y qu&eacute; vuelve un tech pack ejecutable. El dise&ntilde;ador t&iacute;pico dibuja algo bonito y le tira el problema a la f&aacute;brica; <b>Mar&iacute;a sabe cu&aacute;nto vale ese problema antes de dibujar</b>, y c&oacute;mo prevenirlo. Esa es la diferencia entera.</p>
 </div>

 <div class="sec sec--line">
   <p class="eyebrow">03 &middot; Posicionamiento</p>
   <div class="grid g2" style="margin-top:.6rem">
     <div class="card"><h3>BORN es&hellip;</h3>
       <ul class="list"><li>Un estudio que lleva una idea hasta un producto manufacturable</li>
       <li>Discovery, tech pack, factory match, muestras, fitting y supervisi&oacute;n de bulk</li>
       <li>Criterio t&eacute;cnico de piso de f&aacute;brica</li>
       <li>Una marca de producto: est&eacute;tica, voz y touchpoints consistentes</li></ul></div>
     <div class="card"><h3>BORN no es&hellip;</h3>
       <ul class="list list--no"><li>Una f&aacute;brica &mdash; no corta ni cose</li>
       <li>Una agencia de sourcing &mdash; no compra material por el cliente</li>
       <li>Una incubadora &mdash; no invierte capital ni toma equity</li>
       <li>Un estudio creativo &mdash; no dirige la est&eacute;tica conceptual</li></ul></div>
   </div>
 </div>

 <div class="sec sec--line">
   <p class="eyebrow">04 &middot; Esencia y promesa</p>
   <h2 class="h2">Tres filtros contra tres miedos</h2>
   <div class="grid g3" style="margin-top:1.2rem">
     <div class="card"><h3>01 &middot; Viabilidad</h3><p>&iquest;Puede existir en el mundo f&iacute;sico?</p></div>
     <div class="card"><h3>02 &middot; Costo</h3><p>&iquest;Deja margen sin sacrificar calidad?</p></div>
     <div class="card"><h3>03 &middot; Usabilidad</h3><p>&iquest;Funciona en el cuerpo, no solo en la muestra?</p></div>
   </div>
   <p class="prose" style="margin-top:1.3rem">El producto real que vende BORN es la <b>confianza</b>. El tech pack, la muestra y la supervisi&oacute;n son sus manifestaciones tangibles. La promesa &mdash; <b>From idea to life</b> &mdash; el cliente entrega una idea; BORN le entrega vida.</p>
 </div>

 <div class="sec sec--line">
   <p class="eyebrow">05 &middot; Arquitectura verbal</p>
   <h2 class="h2">El claim es el proceso</h2>
   <p class="prose" style="margin-top:1rem"><b>Sketched</b> es contorno &mdash; la idea en el papel. <b>Stitched</b> es pespunte &mdash; se prueba con hilo y aguja. <b>BORN</b> es s&oacute;lido y con vida &mdash; sale al mundo con la firma del estudio. El tagline <em>From idea to life</em> traduce el oficio a promesa emocional.</p>
 </div>

 <div class="sec sec--line">
   <p class="eyebrow">06 &middot; Voz y tono</p>
   <div class="grid g2" style="margin-top:.6rem">
     <div class="card"><h3>Creator</h3><p>Empuja la idea hacia su mejor versi&oacute;n. Nunca solo ejecuta el brief: lo interroga, lo mejora, lo lleva un paso m&aacute;s all&aacute;.</p></div>
     <div class="card"><h3>Caregiver</h3><p>Protege al founder de los errores costosos. Dice &laquo;esto no lo hagas&raquo; cuando lo ve, aunque cueste la venta.</p></div>
   </div>
   <p class="muted" style="margin-top:1.1rem">Tono &middot; Directo &middot; C&aacute;lido &middot; Editorial &middot; Biling&uuml;e &middot; Preciso &middot; Con criterio</p>
 </div>
</section>"""

# ---------------------------------------------------------------- LOGO --------
logo = f"""
<section class="panel" id="p-logo" role="tabpanel" aria-labelledby="t-logo">
 <p class="kicker">El logotipo</p>
 <h1 class="h1">Doble exposici&oacute;n</h1>
 <p class="lede" style="margin-top:1rem">La palabra <b>BORN</b> resuelta en negro con su proceso-fantasma detr&aacute;s, cerrada con el punto rojo. Lo &uacute;nico que nace en color es el punto.</p>

 <div class="sec">
   {stage(SVG['wm_principal'])}
   {capt('Lockup principal','BORN + punto + slogan','El boceto de construcci&oacute;n ghostea detr&aacute;s de la palabra. De aqu&iacute; se derivan todas las aplicaciones.')}
 </div>

 <div class="sec sec--line">
   <p class="eyebrow">Firmas en movimiento</p>
   <div class="motion">
     <div><video data-v="ens" autoplay muted loop playsinline></video>{capt('Ensamblaje','Anim &middot; 6s','El boceto se dibuja y se ensambla hasta la palabra final, y nace el punto rojo.')}</div>
     <div><video data-v="bar" autoplay muted loop playsinline></video>{capt('Barrida','Anim &middot; 5s','Primero el sketch; una barrida imprime las letras sobre el proceso y al final cae el punto rojo.')}</div>
   </div>
 </div>

 <div class="sec sec--line">
   <p class="eyebrow">Isotipo &mdash; la B</p>
   <div class="grid g3">
     <div><div class="stage stage--sq">{SVG['ic_negativo']}</div>{capt('Negativo','Principal','El m&aacute;s catchy &mdash; favicon, avatar, app y sello.')}</div>
     <div><div class="stage stage--sq">{SVG['ic_construccion']}</div>{capt('Construcci&oacute;n','Desarrollo','Para tech packs y work in progress.')}</div>
     <div><div class="stage stage--sq">{SVG['ic_doble']}</div>{capt('Doble exposici&oacute;n','Alterno','La versi&oacute;n que lo cuenta todo.')}</div>
   </div>
 </div>

 <div class="sec sec--line">
   <p class="eyebrow">Variantes del lockup</p>
   <div class="grid g2">
     <div>{stage(SVG['wm_sin_slogan'])}{capt('Sin slogan','Negro + punto','El principal sin el tagline.')}</div>
     <div>{stage(SVG['wm_solo'])}{capt('BORN solo','Reducida','La m&aacute;s discreta: s&oacute;lo palabra y punto.')}</div>
     <div>{stage(SVG['wm_ecorojo_slogan'])}{capt('Eco rojo + slogan','L&iacute;neas rojas','El proceso-fantasma en rojo, con slogan.')}</div>
     <div>{stage(SVG['wm_ecorojo'])}{capt('Eco rojo','L&iacute;neas rojas','Proceso en rojo, sin slogan.')}</div>
   </div>
 </div>

 <div class="sec sec--line">
   <p class="eyebrow">Negativos y fondos de color</p>
   <p class="prose" style="margin-bottom:1.4rem">El logo funciona sobre papel, sobre tinta y sobre el rojo. En negativo, la palabra pasa a marfil; el punto se mantiene rojo sobre oscuro y pasa a tinta sobre rojo para conservar el contraste.</p>
   <div class="grid g3">
     <div><div class="stage">{SVG['wm_principal']}</div><p class="bgnote">Positivo &middot; sobre papel</p></div>
     <div><div class="stage stage--dark">{SVG['wm_principal_neg']}</div><p class="bgnote">Negativo &middot; sobre tinta</p></div>
     <div><div class="stage stage--red">{SVG['wm_principal_onred']}</div><p class="bgnote">Sobre rojo Valentino</p></div>
   </div>
   <div class="grid g3" style="margin-top:1.2rem">
     <div><div class="stage stage--sq">{SVG['ic_negativo']}</div><p class="bgnote">Isotipo negativo</p></div>
     <div><div class="stage stage--dark">{SVG['wm_solo_neg']}</div><p class="bgnote">BORN solo &middot; negativo</p></div>
     <div><div class="stage stage--red">{SVG['wm_solo_onred']}</div><p class="bgnote">BORN solo &middot; sobre rojo</p></div>
   </div>
 </div>

 <div class="sec sec--line">
   <p class="eyebrow">Usos incorrectos</p>
   <ul class="list list--no" style="max-width:60ch">
     <li>No deformar ni cambiar las proporciones</li>
     <li>No rotar el lockup</li>
     <li>No recolorear la palabra &mdash; s&oacute;lo el punto es rojo</li>
     <li>No quitar el aire alrededor del logo</li>
   </ul>
 </div>
</section>"""

# ---------------------------------------------------------------- COLOR -------
SWATCHES=[("Paper","#F1F1EC","Fondo &middot; el papel"),("Graphite 40","#ABABB0","Desarrollo"),
 ("Graphite 60","#78787E","Desarrollo"),("Graphite 80","#3C3C40","Desarrollo"),
 ("Ink","#151517","Texto &middot; tinta"),("Rojo Valentino","#C4122E","Pantone 3546 C &middot; la vida")]
sw_html="".join(
  f'<div class="sw" data-hex="{hx}"><div class="sw__c" style="background:{hx}"></div>'
  f'<div class="sw__m"><b>{n}</b><span>{hx}</span></div></div>' for n,hx,_ in SWATCHES)
color = f"""
<section class="panel" id="p-color" role="tabpanel" aria-labelledby="t-color">
 <p class="kicker">Color</p>
 <h1 class="h1">De blanco y negro a la vida</h1>
 <p class="lede" style="margin-top:1rem">Un boceto empieza a l&aacute;piz. El color llega cuando la idea cobra vida: grafito monocromo como mundo del desarrollo, y un &uacute;nico rojo que se gana al llegar a BORN.</p>
 <div class="sec"><div class="grid g3">{sw_html}</div>
 <p class="note">Toca un color para copiar el hex. Para impresi&oacute;n, usar el Pantone 3546 C directo.</p></div>
</section>"""

# ---------------------------------------------------------------- TIPOGRAFIA --
typo = f"""
<section class="panel" id="p-tipo" role="tabpanel" aria-labelledby="t-tipo">
 <p class="kicker">Tipograf&iacute;a</p>
 <h1 class="h1">Una Didot y tres compa&ntilde;eras</h1>
 <p class="lede" style="margin-top:1rem">El wordmark se compone en <b>Didot</b> &mdash; la tipograf&iacute;a de Vogue. El sistema se apoya en tres familias.</p>
 <div class="sec">
   <div class="spec"><span class="meta">Wordmark &middot; Didot (GFS Didot)</span><div class="samp" style="font-family:var(--word);font-size:clamp(2.4rem,7vw,4.5rem)">BORN.</div></div>
   <div class="spec"><span class="meta">Display &middot; Bodoni Moda 900</span><div class="samp" style="font-family:var(--serif);font-weight:900;font-size:clamp(1.8rem,5vw,3rem)">Sketched. Stitched. BORN.</div></div>
   <div class="spec"><span class="meta">Subhead &middot; Bodoni Moda 600</span><div class="samp" style="font-family:var(--serif6);font-weight:600;font-size:clamp(1.3rem,3vw,1.9rem)">Full Service Apparel Development</div></div>
   <div class="spec"><span class="meta">Body &middot; Jost 400</span><div class="samp" style="font-family:var(--sans);font-size:clamp(1.05rem,2vw,1.35rem);line-height:1.5">El estudio donde una idea de moda pasa por maduraci&oacute;n hasta volverse un producto manufacturable.</div></div>
   <div class="spec"><span class="meta">Technical &middot; Space Mono 400</span><div class="samp" style="font-family:var(--mono);font-size:clamp(.8rem,1.6vw,1rem);letter-spacing:.05em">FASE 01 &middot; SKETCHED &middot; TECH PACK v1 &middot; 1&ndash;3 SEMANAS</div></div>
 </div>
</section>"""

# ---------------------------------------------------------------- APLICACIONES
apps = f"""
<section class="panel" id="p-apps" role="tabpanel" aria-labelledby="t-apps">
 <p class="kicker">Aplicaciones</p>
 <h1 class="h1">La identidad evoluciona con el servicio</h1>
 <p class="lede" style="margin-top:1rem">No es solo un logo: es un lenguaje que cambia de estado seg&uacute;n la fase. El brief habla en boceto, el desarrollo en puntada, la producci&oacute;n en s&oacute;lido con color.</p>
 <div class="sec"><div class="grid g3">
   <div class="phase"><span class="n">Fase 01</span><h3>Sketched</h3><p class="card"><span>Ret&iacute;cula de boceto, contorno a l&aacute;piz, grafito. Todo se dibuja.</span></p><p class="muted" style="margin-top:.7rem">Brief &middot; Moodboard &middot; Tech pack</p></div>
   <div class="phase"><span class="n">Fase 02</span><h3>Stitched</h3><p class="card"><span>Puntadas, pespunte, hilo. La idea se prueba y se cose.</span></p><p class="muted" style="margin-top:.7rem">Sample tag &middot; Fitting &middot; Desarrollo</p></div>
   <div class="phase"><span class="n">Fase 03</span><h3>BORN</h3><p class="card"><span>S&oacute;lido, con color. El producto sale al mundo.</span></p><p class="muted" style="margin-top:.7rem">Hangtag &middot; Drop &middot; Campa&ntilde;a</p></div>
 </div></div>

 <div class="sec sec--line">
   <p class="eyebrow">El journey &middot; tres fases</p>
   <div class="grid g3">
     <div class="card"><span class="muted">1&ndash;3 semanas</span><h3 style="margin-top:.4rem">The Briefing</h3><ul class="list"><li>Discovery y tres filtros</li><li>Moodboard editado</li><li>Tech pack production-ready</li></ul></div>
     <div class="card"><span class="muted">2&ndash;6 meses</span><h3 style="margin-top:.4rem">The Development</h3><ul class="list"><li>Factory pairing y contrato</li><li>Muestra y fitting documentado</li><li>Muestra final aprobada</li></ul></div>
     <div class="card"><span class="muted">4&ndash;8 semanas</span><h3 style="margin-top:.4rem">Production Oversight</h3><ul class="list"><li>Size set y PPS firmado</li><li>Orden y supervisi&oacute;n del bulk</li><li>Handover documentado</li></ul></div>
   </div>
 </div>

 <div class="sec sec--line">
   <p class="eyebrow">El sello</p>
   <h2 class="h2">Todo est&aacute; hecho para nacer</h2>
   <p class="prose" style="margin-top:1rem">Un <b>BORN</b> es cualquier deliverable con la firma del estudio: un tech pack completo, una muestra aprobada, una carpeta de sketches finalizados. <em>Sketched to be BORN. Stitched to be BORN. Made to be BORN.</em></p>
 </div>
</section>"""

# ---------------------------------------------------------------- DESCARGAS ---
def ki_png(key,title):
    bg=""
    if key in DARKBG: bg=' style="background:var(--ink)"'
    elif key in REDBG: bg=' style="background:var(--red)"'
    return (f'<div class="ki"><div class="ki__p"{bg}><img alt="{title}" data-src="{key}"></div>'
      f'<div class="ki__m"><b>{title}</b><span class="ki__f">PNG &middot; transparente</span>'
      f'<div class="dls"><a class="dl" href="{PNG[key]}" download="{DL[key]}">Descargar PNG</a>'
      f'<a class="dl dl--ghost" data-open="1" title="Abrir en pesta&ntilde;a nueva">Abrir</a></div></div></div>')
def ki_vid(pref,title,dlm,dlw):
    return (f'<div class="ki"><div class="ki__p"><video data-v="{pref}" autoplay muted loop playsinline preload="metadata"></video></div>'
      f'<div class="ki__m"><b>{title}</b><span class="ki__f">Video &middot; 1600&times;600 &middot; loop</span>'
      f'<div class="dls"><a class="dl" data-dl="{pref}_mp4" download="{dlm}">MP4</a>'
      f'<a class="dl" data-dl="{pref}_webm" download="{dlw}">WebM</a>'
      f'<a class="dl dl--ghost" data-open="1" title="Abrir en pesta&ntilde;a nueva">Abrir</a></div></div></div>')
DL={"wm_principal":"BORN-logo-principal.png","wm_sin_slogan":"BORN-logo-sin-slogan.png",
  "wm_solo":"BORN-logo-solo.png","wm_ecorojo_slogan":"BORN-logo-eco-rojo-slogan.png",
  "wm_ecorojo":"BORN-logo-eco-rojo.png","ic_negativo":"BORN-icono-negativo.png",
  "ic_construccion":"BORN-icono-construccion.png","ic_doble":"BORN-icono-doble-exposicion.png",
  "wm_principal_neg":"BORN-logo-principal-negativo.png","wm_solo_neg":"BORN-logo-solo-negativo.png",
  "wm_principal_onred":"BORN-logo-principal-sobre-rojo.png"}
TITLES={"wm_principal":"Logo principal","wm_sin_slogan":"Logo sin slogan","wm_solo":"BORN solo",
  "wm_ecorojo_slogan":"Eco rojo + slogan","wm_ecorojo":"Eco rojo","ic_negativo":"Icono negativo",
  "ic_construccion":"Icono construcci&oacute;n","ic_doble":"Icono doble exp.",
  "wm_principal_neg":"Principal negativo","wm_solo_neg":"BORN solo negativo","wm_principal_onred":"Principal sobre rojo"}
# dark preview background for negative/on-red assets so they are visible in the card
DARKBG={"wm_principal_neg","wm_solo_neg"}
REDBG={"wm_principal_onred"}
kit_items="".join(ki_png(k,TITLES[k]) for k in
  ["wm_principal","wm_principal_neg","wm_principal_onred","wm_sin_slogan","wm_solo","wm_solo_neg",
   "wm_ecorojo_slogan","wm_ecorojo","ic_negativo","ic_construccion","ic_doble"])
kit_items+=ki_vid("ens","Animaci&oacute;n ensamblaje","BORN-animacion-ensamblaje.mp4","BORN-animacion-ensamblaje.webm")
kit_items+=ki_vid("bar","Animaci&oacute;n barrida","BORN-animacion-barrida.mp4","BORN-animacion-barrida.webm")
desc = f"""
<section class="panel" id="p-desc" role="tabpanel" aria-labelledby="t-desc">
 <p class="kicker">Descargas</p>
 <h1 class="h1">Kit de marca</h1>
 <p class="lede" style="margin-top:1rem">Todos los archivos, listos para el equipo. <b>Descargar</b> guarda la pieza en tu carpeta de Descargas; si tu navegador la bloquea, <b>Abrir</b> la muestra en una pesta&ntilde;a nueva para guardarla a mano.</p>
 <div class="sec"><div class="kit">{kit_items}</div>
 <p class="note">Las descargas van a la carpeta <b>Descargas</b> de tu dispositivo. PNG de alta resoluci&oacute;n (2700&ndash;4800&nbsp;px), fondo transparente &mdash; sirven sobre cualquier color. Animaciones en MP4 (universal) y WebM. Para imprenta o bordado podemos exportar vectorial (SVG/PDF) desde estos mismos archivos.</p></div>
</section>"""

# ---------------------------------------------------------------- EXPLORACION -
expl = ('<section class="panel" id="p-expl" role="tabpanel" aria-labelledby="t-expl">'
 '<p class="kicker">Anexo &middot; desarrollo</p>'
 '<h1 class="h1">Exploraci&oacute;n de logotipo</h1>'
 '<p class="lede" style="margin-top:1rem">El laboratorio completo detr&aacute;s de la decisi&oacute;n: todas las rutas trabajadas &mdash; doble y triple exposici&oacute;n, campo continuo, ligaduras, progresi&oacute;n, firmas, animaciones e iconos. Material de trabajo, no la marca final.</p>'
 '<div class="sec"><div class="expl-bar"><b>Tablero de exploraci&oacute;n &middot; BORN</b>'
 '<a href="logos.html" target="_blank" rel="noopener">Abrir en pantalla completa &rarr;</a></div>'
 '<iframe class="expl-frame" title="Exploraci&oacute;n de logotipo BORN" loading="lazy" srcdoc="'
 + EXPL_ESC + '"></iframe></div></section>')

# ---------------------------------------------------------------- shell -------
TABS=[("marca","Marca"),("logo","Logo"),("color","Color"),("tipo","Tipograf&iacute;a"),("apps","Aplicaciones"),("desc","Descargas"),("expl","Exploraci&oacute;n")]
tabbtns="".join(
  f'<button class="tab" role="tab" id="t-{k}" aria-controls="p-{k}" aria-selected="{"true" if i==0 else "false"}" data-tab="{k}">{lab}</button>'
  for i,(k,lab) in enumerate(TABS))

header = f"""
<header class="top">
 <div class="top__in">
   <a class="brand" href="#" data-tab="marca" aria-label="BORN Studio"><span class="mark">{SVG['ic_negativo']}</span>
     <span><b>BORN</b><span>Studio</span></span></a>
   <nav class="tabs" role="tablist" aria-label="Secciones">{tabbtns}</nav>
 </div>
 <div class="bar" id="bar"></div>
</header>"""

footer = f"""
<footer class="foot">
 <div class="fm">{SVG['wm_solo']}</div>
 <p>BORN Studio &middot; Full Service Apparel Development<br>Brand Book v1.0 &middot; From idea to life<br>Estrategia &amp; marca &mdash; Matisis Consultancy</p>
</footer>"""

VMAP = {
  "ens_mp4":VID['ens_mp4'],"ens_webm":VID['ens_webm'],"ens_pos":VID['ens_pos'],
  "bar_mp4":VID['bar_mp4'],"bar_webm":VID['bar_webm'],"bar_pos":VID['bar_pos'],
}
JS = "<script>(function(){var V="+json.dumps(VMAP)+";" + r"""
 // wire videos (embed each clip once, in V) and video download links
 document.querySelectorAll('video[data-v]').forEach(function(v){
   var k=v.getAttribute('data-v'); v.setAttribute('poster',V[k+'_pos']||'');
   [['webm','video/webm'],['mp4','video/mp4']].forEach(function(f){
     var u=V[k+'_'+f[0]]; if(u){var s=document.createElement('source');s.src=u;s.type=f[1];v.appendChild(s);} });
   v.load(); var pr=v.play&&v.play(); if(pr&&pr.catch)pr.catch(function(){});
 });
 document.querySelectorAll('a[data-dl]').forEach(function(a){var u=V[a.getAttribute('data-dl')]; if(u)a.setAttribute('href',u);});
 // ---- robust downloads: data-URI -> Blob object URL (avoids sandbox/size limits on data: links) ----
 function toBlob(uri){var c=uri.split(','),m=(c[0].match(/:(.*?);/)||[])[1]||'application/octet-stream';
   var b=atob(c[1]),n=b.length,u=new Uint8Array(n);while(n--)u[n]=b.charCodeAt(n);return new Blob([u],{type:m});}
 function saveAs(uri,name){try{var url=URL.createObjectURL(toBlob(uri));var a=document.createElement('a');
   a.href=url;a.download=name||'download';a.rel='noopener';document.body.appendChild(a);a.click();
   setTimeout(function(){URL.revokeObjectURL(url);a.remove();},4000);return true;}catch(e){return false;}}
 function openTab(uri){try{var url=URL.createObjectURL(toBlob(uri));var w=window.open(url,'_blank','noopener');
   if(!w){var a=document.createElement('a');a.href=url;a.target='_blank';a.rel='noopener';document.body.appendChild(a);a.click();a.remove();}
   setTimeout(function(){URL.revokeObjectURL(url);},60000);return true;}catch(e){return false;}}
 function uriFor(a){var u=a.getAttribute('href')||(a.getAttribute('data-dl')?V[a.getAttribute('data-dl')]:'');
   if(u)return u; var sib=a.parentNode.querySelector('a.dl:not(.dl--ghost)');
   return sib?(sib.getAttribute('href')||V[sib.getAttribute('data-dl')]||''):'';}
 function nameFor(a){var n=a.getAttribute('download'); if(n)return n;
   var sib=a.parentNode.querySelector('a.dl:not(.dl--ghost)'); return sib?sib.getAttribute('download'):'download';}
 document.querySelectorAll('a.dl').forEach(function(a){a.addEventListener('click',function(e){
   var uri=uriFor(a); if(!uri)return; e.preventDefault();
   if(a.hasAttribute('data-open')){openTab(uri);return;}
   if(!saveAs(uri,nameFor(a))) openTab(uri);
 });});
 var tabs=[].slice.call(document.querySelectorAll('[role=tab]'));
 var panels=[].slice.call(document.querySelectorAll('.panel'));
 function show(k){
   tabs.forEach(function(t){t.setAttribute('aria-selected', t.dataset.tab===k?'true':'false');});
   panels.forEach(function(p){p.classList.toggle('active', p.id==='p-'+k);});
   window.scrollTo(0,0);
   if(history.replaceState) history.replaceState(null,'','#'+k);
 }
 document.body.addEventListener('click',function(e){
   var el=e.target.closest('[data-tab]'); if(!el) return;
   e.preventDefault(); show(el.dataset.tab);
 });
 var start=(location.hash||'').replace('#',''); if(start&&document.getElementById('p-'+start)) show(start);
 // lazy-set download previews from their anchor href (single data-URI copy)
 document.querySelectorAll('img[data-src]').forEach(function(img){
   var a=img.closest('.ki').querySelector('a.dl'); if(a) img.src=a.getAttribute('href');
 });
 // copy hex swatches
 var toast=document.querySelector('.toast');
 function tst(m){if(!toast)return;toast.textContent=m;toast.classList.add('on');clearTimeout(toast._t);toast._t=setTimeout(function(){toast.classList.remove('on');},1400);}
 document.querySelectorAll('.sw').forEach(function(s){s.addEventListener('click',function(){
   var h=s.dataset.hex||'';
   if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(h).then(function(){tst(h+'  copiado');},function(){tst(h);});}else{tst(h);}
 });});
 // scroll progress
 var bar=document.getElementById('bar');
 addEventListener('scroll',function(){var d=document.documentElement,s=d.scrollHeight-d.clientHeight;bar.style.width=(s>0?(d.scrollTop/s*100):0)+'%';},{passive:true});
 // play visible videos on the Logo tab
 document.querySelectorAll('.motion video').forEach(function(v){var p=v.play&&v.play();if(p&&p.catch)p.catch(function(){});});
})();</script>"""

body = ("<a class=\"brand\" style=\"display:none\"></a>" + header +
        '<main class="wrap">' + marca + logo + color + typo + apps + desc + expl + "</main>" +
        footer + '<div class="toast" role="status"></div>' + JS)

head = ("<style>\n"+FONTS+"\n"+CSS+"\n</style>")

# artifact body form (no html/head wrapper; title + style + body)
artifact = "<title>BORN Studio &mdash; Brand Book</title>\n"+head+"\n"+body
open(f"{W}/artifact.html","w",encoding="utf-8").write(artifact)

# full standalone
landing = ("<!DOCTYPE html>\n<html lang=\"es\">\n<head>\n<meta charset=\"utf-8\">\n"
  "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
  "<title>BORN Studio &mdash; From idea to life</title>\n"
  "<meta name=\"description\" content=\"BORN Studio &mdash; Full Service Apparel Development. Brand book.\">\n"
  "<meta name=\"theme-color\" content=\"#F2EEE6\">\n"
  f"<link rel=\"icon\" href=\"{FAVICON}\">\n"
  + head + "\n</head>\n<body>\n" + body + "\n</body>\n</html>\n")
open("index.html","w",encoding="utf-8").write(landing)
print("index.html:",round(len(landing)/1024),"KB  artifact.html:",round(len(artifact)/1024),"KB")
