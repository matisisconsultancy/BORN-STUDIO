#!/usr/bin/env python3
"""Build the 'Logo final' + 'Kit de descarga' chapters and inject them into
index.html. Each asset is embedded once (JS map) and wired to previews +
download buttons. Also emits tools/_work/artifact.html (body form) for the
Artifact tool. Re-runnable: strips a previous injection first."""
import base64, json, re, os

IDX="index.html"; A="assets/logos"
def datauri(path, mime):
    b=base64.b64encode(open(path,"rb").read()).decode("ascii")
    return f"data:{mime};base64,{b}"

# ---- asset registry -------------------------------------------------------
PNG=lambda k:datauri(f"{A}/{k}.png","image/png")
KIT={
  "wm_principal":PNG("wm_principal"), "wm_sin_slogan":PNG("wm_sin_slogan"),
  "wm_solo":PNG("wm_solo"), "wm_ecorojo_slogan":PNG("wm_ecorojo_slogan"),
  "wm_ecorojo":PNG("wm_ecorojo"),
  "ic_negativo":PNG("ic_negativo"), "ic_construccion":PNG("ic_construccion"),
  "ic_doble":PNG("ic_doble"),
  "an_ensamblaje.mp4":datauri(f"{A}/an_ensamblaje.mp4","video/mp4"),
  "an_ensamblaje.webm":datauri(f"{A}/an_ensamblaje.webm","video/webm"),
  "an_ensamblaje.poster":PNG("an_ensamblaje_poster"),
  "an_barrida.mp4":datauri(f"{A}/an_barrida.mp4","video/mp4"),
  "an_barrida.webm":datauri(f"{A}/an_barrida.webm","video/webm"),
  "an_barrida.poster":PNG("an_barrida_poster"),
}
DIMS={"wm_principal":"4800×1488","wm_sin_slogan":"4800×1200",
  "wm_solo":"4800×1200","wm_ecorojo_slogan":"4800×1488",
  "wm_ecorojo":"4800×1200","ic_negativo":"2700×2700",
  "ic_construccion":"2700×2700","ic_doble":"2700×2700"}

# ---- scoped CSS -----------------------------------------------------------
CSS = """
<style>
.lf-hero{margin:2rem 0 .5rem;padding:clamp(2rem,6vw,4.5rem);background:var(--paper-2);border:1px solid var(--line);border-radius:12px;display:flex;justify-content:center}
.lf-hero img{width:min(760px,94%);height:auto}
.lf-sub{font-family:var(--mono);font-size:.7rem;letter-spacing:.2em;text-transform:uppercase;color:var(--red);margin:2.6rem 0 .2rem}
.lf-grid{display:grid;gap:1.4rem;margin-top:1.2rem}
.lf-motion{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}
.lf-icons{grid-template-columns:repeat(auto-fit,minmax(210px,1fr))}
.lf-vars{grid-template-columns:repeat(auto-fit,minmax(230px,1fr))}
.lf-card{background:var(--paper-2);border:1px solid var(--line);border-radius:12px;overflow:hidden}
.lf-card>video,.lf-card>img{display:block;width:100%;height:auto;background:var(--paper)}
.lf-icons .lf-card>img,.lf-vars .lf-card>img{padding:1.3rem;background:var(--paper)}
.lf-cap{padding:.95rem 1.15rem}
.lf-cap b{font-family:var(--serif6);font-weight:600;font-size:1.06rem;color:var(--ink);display:block;line-height:1.2}
.lf-cap i{font-family:var(--mono);font-style:normal;font-size:.62rem;letter-spacing:.12em;text-transform:uppercase;color:var(--g3)}
.lf-cap p{font-family:var(--sans);font-size:.9rem;line-height:1.5;color:var(--g2);margin:.45rem 0 0}
.kit-grid{display:grid;gap:1.2rem;grid-template-columns:repeat(auto-fill,minmax(232px,1fr));margin-top:1.6rem}
.kit-item{display:flex;flex-direction:column;background:var(--paper-2);border:1px solid var(--line);border-radius:12px;overflow:hidden}
.kit-prev{background:var(--paper);display:flex;align-items:center;justify-content:center;padding:1.1rem;min-height:128px}
.kit-prev img,.kit-prev video{max-width:100%;max-height:150px;width:auto;height:auto}
.kit-meta{padding:.85rem 1.05rem;border-top:1px solid var(--line);display:flex;flex-direction:column;gap:.55rem;flex:1}
.kit-meta b{font-family:var(--sans7);font-size:.93rem;color:var(--ink);line-height:1.25}
.kit-fmt{font-family:var(--mono);font-size:.6rem;letter-spacing:.1em;text-transform:uppercase;color:var(--g3)}
.kit-dls{display:flex;gap:.5rem;flex-wrap:wrap;margin-top:auto}
.kit-dl{font-family:var(--mono);font-size:.62rem;letter-spacing:.08em;text-transform:uppercase;color:var(--paper);background:var(--ink);border:0;border-radius:6px;padding:.55rem .85rem;cursor:pointer;text-decoration:none;transition:background .25s,transform .1s}
.kit-dl:hover{background:var(--red)}
.kit-dl:active{transform:translateY(1px)}
.kit-note{font-family:var(--mono);font-size:.7rem;letter-spacing:.05em;color:var(--g3);margin-top:1.5rem;line-height:1.6}
/* responsive fix: keep wide wordmark SVGs inside their grid cells (no page overflow on mobile) */
.states,.state{min-width:0}
.state svg{max-width:100%}
</style>"""

def cap(b,i,p):  return f'<div class="lf-cap"><b>{b}</b><i>{i}</i><p>{p}</p></div>'

# ---- Section 15: Logo final ----------------------------------------------
lf = []
lf.append('<section class="ch" id="c15"><div class="ch__head"><span class="ch__n">15</span>'
  '<h2 class="ch__t">Logo final</h2><span class="ch__k">La decisi&oacute;n &mdash; doble exposici&oacute;n</span></div>')
lf.append('<p class="prose reveal">Tras la ronda de exploraci&oacute;n, la marca se resuelve en una sola direcci&oacute;n: '
  'la <b>doble exposici&oacute;n</b> &mdash; la palabra <b>BORN</b> resuelta en negro con su <b>proceso-fantasma</b> '
  '(el boceto de construcci&oacute;n) ghosteando detr&aacute;s, cerrada con el <b>punto rojo</b>. Lo &uacute;nico que '
  'nace en color es el punto. El sistema se despliega en un lockup principal, sus variantes y un isotipo.</p>')
lf.append('<div class="lf-hero reveal"><img data-img="wm_principal" alt="BORN &mdash; logo principal"></div>')
lf.append('<p class="prose reveal" style="margin-top:1rem">Lockup principal: <b>BORN</b> + punto rojo + <em>From idea to life</em>, '
  'con el boceto detr&aacute;s. De aqu&iacute; se derivan todas las aplicaciones.</p>')

lf.append('<p class="lf-sub reveal">Firmas en movimiento</p>')
lf.append('<div class="lf-grid lf-motion reveal">')
lf.append('<div class="lf-card"><video data-video="ensamblaje" autoplay muted loop playsinline></video>'
  + cap("Ensamblaje","Anim &middot; 6s loop","El boceto se dibuja y se ensambla hasta quedar la palabra final, y nace el punto rojo.")+'</div>')
lf.append('<div class="lf-card"><video data-video="barrida" autoplay muted loop playsinline></video>'
  + cap("Barrida","Anim &middot; 5s loop","Primero el sketch, luego una barrida imprime las letras sobre el proceso y al final cae el punto rojo.")+'</div>')
lf.append('</div>')

lf.append('<p class="lf-sub reveal">Isotipo &mdash; la B</p>')
lf.append('<div class="lf-grid lf-icons reveal">')
lf.append('<div class="lf-card"><img data-img="ic_negativo" alt="Icono negativo">'
  + cap("Negativo","Principal","La B en negativo: doble exposici&oacute;n dentro del cuadro tinta. El m&aacute;s catchy &mdash; favicon, avatar, app y sello.")+'</div>')
lf.append('<div class="lf-card"><img data-img="ic_construccion" alt="Icono construcci&oacute;n">'
  + cap("Construcci&oacute;n","Desarrollo","S&oacute;lo el contorno de construcci&oacute;n. Para etapas de desarrollo &mdash; portada de tech pack, work in progress.")+'</div>')
lf.append('<div class="lf-card"><img data-img="ic_doble" alt="Icono doble exposici&oacute;n">'
  + cap("Doble exposici&oacute;n","Alterno","La B s&oacute;lida con su proceso-fantasma y el punto. La versi&oacute;n que lo cuenta todo.")+'</div>')
lf.append('</div>')

lf.append('<p class="lf-sub reveal">Variantes del lockup</p>')
lf.append('<div class="lf-grid lf-vars reveal">')
lf.append('<div class="lf-card"><img data-img="wm_sin_slogan" alt="Sin slogan">'+cap("Sin slogan","Negro + punto","El principal sin <em>From idea to life</em>.")+'</div>')
lf.append('<div class="lf-card"><img data-img="wm_solo" alt="BORN solo">'+cap("BORN solo","Reducida","La m&aacute;s discreta: s&oacute;lo la palabra y el punto, sin proceso ni slogan.")+'</div>')
lf.append('<div class="lf-card"><img data-img="wm_ecorojo_slogan" alt="Eco rojo con slogan">'+cap("Eco rojo + slogan","L&iacute;neas rojas","El proceso-fantasma en rojo, con slogan.")+'</div>')
lf.append('<div class="lf-card"><img data-img="wm_ecorojo" alt="Eco rojo">'+cap("Eco rojo","L&iacute;neas rojas","Proceso en rojo, sin slogan.")+'</div>')
lf.append('</div>')
lf.append('</section>')

# ---- Section 16: Kit de descarga -----------------------------------------
def kit_img(key,title,fmt):
    return ('<div class="kit-item"><div class="kit-prev"><img data-img="'+key+'" alt=""></div>'
      '<div class="kit-meta"><b>'+title+'</b><span class="kit-fmt">'+fmt+'</span>'
      '<div class="kit-dls"><a class="kit-dl" href="#" data-dl="'+key+'" data-name="'+DL[key]+'">PNG</a></div></div></div>')
def kit_vid(base,title):
    return ('<div class="kit-item"><div class="kit-prev"><img data-img="'+base+'.poster" alt=""></div>'
      '<div class="kit-meta"><b>'+title+'</b><span class="kit-fmt">Video &middot; 1600&times;600 &middot; loop</span>'
      '<div class="kit-dls">'
      '<a class="kit-dl" href="#" data-dl="'+base+'.mp4" data-name="'+DL[base+".mp4"]+'">MP4</a>'
      '<a class="kit-dl" href="#" data-dl="'+base+'.webm" data-name="'+DL[base+".webm"]+'">WebM</a>'
      '</div></div></div>')

DL={"wm_principal":"BORN-logo-principal.png","wm_sin_slogan":"BORN-logo-sin-slogan.png",
  "wm_solo":"BORN-logo-solo.png","wm_ecorojo_slogan":"BORN-logo-eco-rojo-slogan.png",
  "wm_ecorojo":"BORN-logo-eco-rojo.png","ic_negativo":"BORN-icono-negativo.png",
  "ic_construccion":"BORN-icono-construccion.png","ic_doble":"BORN-icono-doble-exposicion.png",
  "an_ensamblaje.mp4":"BORN-animacion-ensamblaje.mp4","an_ensamblaje.webm":"BORN-animacion-ensamblaje.webm",
  "an_barrida.mp4":"BORN-animacion-barrida.mp4","an_barrida.webm":"BORN-animacion-barrida.webm"}

kt=[]
kt.append('<section class="ch" id="c16"><div class="ch__head"><span class="ch__n">16</span>'
  '<h2 class="ch__t">Kit de descarga</h2><span class="ch__k">Todos los archivos, listos para el equipo</span></div>')
kt.append('<p class="prose reveal">Cada pieza en <b>PNG de alta resoluci&oacute;n</b> con fondo transparente, y las '
  'animaciones en <b>MP4</b> (universal) y <b>WebM</b>. Todo vive dentro de este documento &mdash; un solo enlace lo tiene todo. '
  'Pasa el archivo a tu equipo y descarga con un clic.</p>')
kt.append('<div class="kit-grid reveal">')
for k,t in [("wm_principal","Logo principal"),("wm_sin_slogan","Logo sin slogan"),("wm_solo","BORN solo"),
            ("wm_ecorojo_slogan","Eco rojo + slogan"),("wm_ecorojo","Eco rojo"),
            ("ic_negativo","Icono negativo"),("ic_construccion","Icono construcci&oacute;n"),("ic_doble","Icono doble exp.")]:
    kt.append(kit_img(k,t,"PNG &middot; "+DIMS[k]+" &middot; transparente"))
kt.append(kit_vid("an_ensamblaje","Animaci&oacute;n ensamblaje"))
kt.append(kit_vid("an_barrida","Animaci&oacute;n barrida"))
kt.append('</div>')
kt.append('<p class="kit-note reveal">PNG a 300&ndash;4800&nbsp;px, fondo transparente &mdash; sirven sobre cualquier color. '
  'Para imprenta o bordado podemos exportar tambi&eacute;n vectorial (SVG/PDF) desde estos mismos archivos.</p>')
kt.append('</section>')

# ---- JS wiring ------------------------------------------------------------
JS = ("<script>(function(){var K="+json.dumps(KIT)+";"
  "document.querySelectorAll('[data-img]').forEach(function(e){var s=K[e.getAttribute('data-img')];if(s)e.src=s;});"
  "document.querySelectorAll('video[data-video]').forEach(function(v){var k=v.getAttribute('data-video');"
  "[['webm','video/webm'],['mp4','video/mp4']].forEach(function(f){var u=K['an_'+k+'.'+f[0]];if(u){var s=document.createElement('source');s.src=u;s.type=f[1];v.appendChild(s);}});"
  "v.load();var pv=v.play();if(pv&&pv.catch)pv.catch(function(){});});"
  "document.querySelectorAll('[data-dl]').forEach(function(b){b.addEventListener('click',function(e){e.preventDefault();"
  "var u=K[b.getAttribute('data-dl')];if(!u)return;var a=document.createElement('a');a.href=u;a.download=b.getAttribute('data-name');"
  "document.body.appendChild(a);a.click();a.remove();});});})();</script>")

BLOCK = "<!--KIT:START-->"+CSS+"".join(lf)+"".join(kt)+JS+"<!--KIT:END-->"

# ---- inject into index.html ----------------------------------------------
html=open(IDX,encoding="utf-8").read()
# remove prior injection if re-running
html=re.sub(r'<!--KIT:START-->.*?<!--KIT:END-->','',html,flags=re.S)
# rename existing exploration chapter c15 -> c17 (appendix)
html=html.replace('<section class="ch" id="c15">','<section class="ch" id="c17">',1)
html=html.replace('<div class="ch__head"><span class="ch__n">15</span><h2 class="ch__t">Exploraci&oacute;n de logotipo</h2>',
                  '<div class="ch__head"><span class="ch__n">17</span><h2 class="ch__t">Exploraci&oacute;n de logotipo</h2>',1)
# nav: replace the single Exploracion link with the three new ones
html=html.replace('<a href="#c15">Exploraci&#243;n</a>',
  '<a href="#c15">Logo final</a><a href="#c16">Descargas</a><a href="#c17">Exploraci&#243;n</a>',1)
# insert new sections before the exploration appendix (now id c17)
anchor='<section class="ch" id="c17">'
assert anchor in html, "c17 anchor missing"
html=html.replace(anchor, BLOCK+anchor,1)
open(IDX,"w",encoding="utf-8").write(html)

# ---- emit artifact body form ---------------------------------------------
# NOTE: the exploration iframe srcdoc embeds all of logos.html, which contains
# its OWN literal </style> and </body>. The head <style> is the FIRST style and
# closes before the srcdoc (non-greedy is correct). The real </body> is the LAST
# one in the file, so the body match MUST be greedy or it truncates the doc
# (dropping the footer and the reveal script -> a blank-looking page).
style=re.search(r'(<style>.*?</style>)',html,re.S).group(1)
body=re.search(r'<body>(.*)</body>',html,re.S).group(1)   # greedy: last </body>
art="<title>BORN Studio &mdash; Brand Book</title>\n"+style+"\n"+body
open("tools/_work/artifact.html","w",encoding="utf-8").write(art)

print("index.html:",round(len(html)/1024),"KB   artifact.html:",round(len(art)/1024),"KB")
print("KIT keys:",len(KIT),"  block:",round(len(BLOCK)/1024),"KB")
