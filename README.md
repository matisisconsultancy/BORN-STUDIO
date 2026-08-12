# BORN Studio — Identidad de marca

Landing page / brand book de **BORN Studio**, un *Full Service Apparel Development Studio*.

> **Sketched. Stitched. BORN.** — *From idea to life.*

`index.html` es una **página estática autónoma** (todas las fuentes van embebidas como
data-URI; CSS y JS en línea). No necesita build ni dependencias: se puede abrir
directamente o servir desde cualquier hosting estático.

## El concepto

El logotipo **es** el proceso. Cada letra de **BORN** vive una fase del oficio:

| Estado | Letra | Lenguaje |
|---|---|---|
| **Sketched** | B | contorno a lápiz |
| **Stitched** | O | pespunte / hilo |
| **Inked** | R | sólido |
| **BORN** | N | nace en color |

El boceto empieza en blanco y negro y **cobra vida con color** — de ahí la paleta:
grafito monocromo → **rojo Valentino**. En el hero, el wordmark se anima al cargar
recorriendo los cuatro estados hasta asentarse en la firma.

## Sistema

- **Tipografía:** tres familias — **Bodoni Moda** (display y subtítulos, Didone),
  **Jost** (cuerpo) y **Space Mono** (registro técnico); más **Didot** (código Vogue)
  reservado al wordmark.
- **Color:** marfil `#F2EEE6`, tinta `#1B1720`, grafitos, y **Rojo Valentino
  `#C4122E` (Pantone 3546 C)**.
- **Isotipo:** la **B** de cuatro estados (animada) para favicon, avatar y sello.
- **Sistema por fases:** cada fase del servicio comunica en su estado (sketch /
  stitch / born).

El documento recorre 17 capítulos: la marca, origen, posicionamiento, esencia,
arquitectura verbal, voz, **logotipo** (lockups e isotipo), **color**,
**tipografía**, sistema por fases, aplicaciones, journey, el sello, guardrails,
**logo final**, **kit de descarga** y el tablero de **exploración**.

## Logo final (la decisión)

La marca se resuelve en la **doble exposición**: la palabra **BORN** en negro con su
**proceso-fantasma** (el boceto de construcción) detrás, cerrada con el **punto rojo** —
lo único que nace en color. El sistema:

- **Lockup principal** — `BORN` + punto + *From idea to life*, con el boceto detrás.
- **Variantes** — sin slogan, `BORN` solo (reducida), y eco rojo (líneas del proceso en rojo) con/sin slogan.
- **Isotipo** — la **B** en tres registros: **negativo** (principal, el más *catchy*),
  **construcción** (sketch, para tech packs y etapas de desarrollo) y **doble exposición** (alterno).
- **Firmas en movimiento** — *Ensamblaje* (el boceto se dibuja y se ensambla) y *Barrida*
  (el sketch se imprime letra a letra y cae el punto rojo).

## Kit de descarga (`assets/logos/`)

Todos los archivos viven embebidos en el brandbook (descarga con un clic) **y** como
archivos sueltos en `assets/logos/`:

- **Logos e isotipos** — PNG de alta resolución (2700–4800 px), fondo transparente.
- **Animaciones** — `MP4` (H.264, universal) y `WebM` (VP9), loop de 1600×600, con póster.

### Pipeline reproducible (`tools/`)

Los assets se derivan del artefacto aprobado (`logos.html`), sin dependencias de build permanentes:

```bash
python3 tools/extract_logos.py   # extrae SVGs/estilos elegidos -> tools/_work/
node    tools/render_png.cjs      # SVGs -> PNG alta resolución (Chromium)
node    tools/record_anim.cjs     # anima -> frames deterministas (Chromium)
# frames -> MP4/WebM/póster con el ffmpeg de imageio-ffmpeg
python3 tools/build_kit.py        # inyecta 'Logo final' + 'Kit de descarga' en index.html
```

Requiere Chromium (Playwright), `pillow` e `imageio-ffmpeg`. `tools/_work/` es intermedio
regenerable (no versionado).

## Uso

```bash
# abrir directamente
open index.html
# o servir en local
python3 -m http.server 8000    # → http://localhost:8000
```

Para publicar: sube `index.html` a cualquier hosting estático (GitHub Pages,
Netlify, Vercel…). Al ser un único archivo autónomo, no hay pasos de build.

### Notas de licencia
- La tipografía del wordmark usa **GFS Didot** (revival libre de Didot); la de
  Vogue es un Didot propietario. Si se dispone del archivo licenciado, se sustituye 1:1.
- El **Rojo Valentino** se aproxima con el hex de pantalla de Pantone 3546 C; para
  impresión, usar el valor Pantone directo.

---

Estrategia y marca — **Matisis Consultancy** · para María, fundadora de BORN Studio.
