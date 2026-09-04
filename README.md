# BORN Studio — Identidad de marca

Landing page / brand book de **BORN Studio**, un *Full Service Apparel Development Studio*.

> **Sketched. Stitched. BORN.** — *From idea to life.*

`index.html` es una **página estática autónoma** (todas las fuentes van embebidas como
data-URI; CSS y JS en línea). No necesita build ni dependencias: se puede abrir
directamente o servir desde cualquier hosting estático.

Está organizada en **pestañas**: **Marca · Logo · Color · Tipografía · Aplicaciones ·
Descargas**. El logo final (doble exposición) se aplica de forma consistente en el
header, el footer y el favicon.

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
python3 tools/make_negatives.py  # recolorea negativos y versiones sobre color
node    tools/render_png.cjs      # SVGs -> PNG alta resolución (Chromium)
node    tools/record_anim.cjs     # anima -> frames deterministas (Chromium)
# frames -> MP4/WebM/póster con el ffmpeg de imageio-ffmpeg
python3 tools/build_book.py       # arma el brandbook con pestañas -> index.html
```

`build_book.py` reúne fuentes, tokens, texto y los assets finales en una sola página
con pestañas y descargas por enlace directo. Requiere Chromium (Playwright), `pillow` e
`imageio-ffmpeg`. `tools/_work/` es intermedio regenerable (no versionado).

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

## El Project Room — el sistema de entrega (`deliverables/`)

`deliverables/index.html` es el link que se le pasa al cliente: una **bitácora del
desarrollo** más los documentos compilados que la sostienen. Una sola página autónoma
—fuentes e imágenes embebidas, sin build, sin red— que funciona offline, por correo o
en cualquier hosting estático.

### La regla que sostiene todo: dos canales, nunca mezclados

| Canal | Qué dice | Cómo |
|---|---|---|
| **Registro** | en qué fase del oficio estás | *Sketched:* retícula de construcción, filete punteado, grafito · *Stitched:* trama diagonal, filete en pespunte, tinta · *BORN:* papel limpio, filete sólido, punto rojo |
| **Marcador** | si ya ocurrió | contorno (no empieza) · pespunte (vivo) · sólido + punto rojo (firmado) |

El registro **nunca** dice si algo está terminado; el marcador **nunca** dice en qué fase
estás. Separarlos es lo que permite responder las dos preguntas de un vistazo sin leyenda.
Bajar por la bitácora es ver nacer la prenda.

### La bitácora

Entradas fechadas con **anatomía idéntica** —fecha, tipo, titular, cuerpo— para que la
página se escanee, y **carga distinta según el tipo de información** para que la densidad
siga al contenido y no a la plantilla. Nueve tipos:

`Note` · `Decision` · `Materials` · `Colour` · `Release` · `Sample` · `Measure` ·
`Approval` · `Watch`

Una `Decision` muestra elegido contra considerado, el porqué y lo que costó o ahorró.
Una `Measure` muestra **solo los puntos fuera de tolerancia**, con la desviación y si la
causa es el patrón o la fábrica — el POM graduado completo vive en el tech pack, a un clic.
Un `Watch` nunca aparece sin la acción que lo elimina.

### Documentos compilados

La bitácora cuenta la historia; los documentos tienen el detalle, y cada uno imprime solo
a A4. **Tech pack** (flat, BOM, POM graduado con tolerancias, construcción, por estilo) ·
**Fitting report** · **Quote** · **Invoice** · **Handover**.

### La pestaña System

Los registros, los estados, los nueve tipos de entrada, las seis reglas que mantienen el
sistema honesto y el snippet para añadir una entrada. Es lo que permite al equipo de María
producir entregas nuevas coherentes sin rediseñar nada.

### Datos y pipeline

Todo el contenido vive en `tools/room_data.py`, que **no sabe nada de cómo se ve nada**.
`tools/build_room.py` es el motor. Abrir una sala nueva es copiar el primero, reemplazar
`PROJECT`, `STYLES` y `ENTRIES`, y compilar.

```bash
python3 tools/extract_layo.py    # deck aprobado -> deliverables/assets/*.jpg
python3 tools/build_room.py      # -> deliverables/index.html
```

La demo va montada sobre el entregable real de **LAYO** (capsule de seis estilos): style
numbers, calidades, Pantones TCX, flats, renders 3D y fotografía de muestra salen de
`source/BORN_LayoCapsule_DesignStage.pdf`. Requiere `pymupdf` y `pillow`.

---

Estrategia y marca — **Matisis Consultancy** · para María, fundadora de BORN Studio.
