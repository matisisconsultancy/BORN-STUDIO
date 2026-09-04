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

`deliverables/index.html` es el link que se le pasa al cliente. Una sola página autónoma
—fuentes e imágenes embebidas, sin build, sin red— que funciona offline, por correo o en
cualquier hosting estático.

### Seis secciones

**The range** — puerta, las tres fases, portada del proyecto, índice y una lámina por
estilo: el flat técnico a ancho completo, la ficha, los callouts de construcción, los
colorways y una **galería** con todas las vistas. **Logbook** — la bitácora fechada.
**Tech pack** · **Fitting** · **Handover** — los documentos, cada uno imprime solo a A4.
**System** — cómo se arma una sala nueva.

La cotización y la factura siguen construidas en `build_room.py` (`quote()`, `invoice()`,
`BILLING`): para volver a montar la pestaña basta con devolver `("billing", "Billing")` a
`DOCS` y `BILLING` a `BODY`. Se retiraron de la sala, no del sistema.

### Las fases conceptuales

Justo después de la puerta, **The process** presenta los tres estados del oficio, cada uno
dibujado en su propio registro: *Sketched* sobre la retícula de construcción, *Stitched*
sobre la trama diagonal, *BORN* sobre tinta. Se recorre antes de ver el proyecto, así que
funciona como método y como leyenda de todo lo que viene después.

### Los títulos llevan puesto su estado

Un título en fase *Sketched* se dibuja y no se rellena —tipografía en contorno—; uno en
*Stitched* se rellena de hilo —trama de pespunte recortada contra la letra—; *BORN* es
sólido y a color. Es el mismo sistema del wordmark trasladado a la tipografía, y aparece
tanto en las tres fases como en las bandas de la bitácora. El color del trazo se nombra
en `--ts` según el terreno: no puede ser `currentColor`, porque en estos títulos el color
es justamente lo que se ha quitado.

### La galería *es* el proceso

La navegación de cada estilo son las fases del oficio: **Drawn · Coloured · Visualised ·
Sampled**, y un raíl bajo la lámina marca en cuál de los tres estados —Sketched, Stitched,
BORN— nace la vista que estás mirando. La lámina toma la proporción de su imagen, así que
un flat ancho y una legging alta se ven enteros, sin bandas ni recortes.

Están las **37 imágenes** del deck: 6 flats técnicos, 7 tableros de colorway, 8 renders 3D
y 16 fotografías de muestra.

### Close-up

Clic en la lámina abre a pantalla completa sobre el mismo papel, con **zoom hasta 6×**:
rueda, `+`/`−`, doble clic, teclas `+ − 0`, y **pinch** en táctil. Con zoom se arrastra para
recorrer la prenda. Los flats se exportan a 2200 px porque su texto de callout tiene que
aguantar el acercamiento; en pantalla estrecha se abren ya ajustados a la altura, así que
en un teléfono se lee "RAGLAN SLEEVES" sin hacer nada.

### Dos canales, nunca mezclados

| Canal | Qué dice | Cómo |
|---|---|---|
| **Registro** | en qué fase del oficio estás | *Sketched:* retícula de construcción, filete punteado, grafito · *Stitched:* trama diagonal, filete en pespunte, tinta · *BORN:* papel limpio, filete sólido |
| **Marcador** | si ya ocurrió | contorno · pespunte · sólido + punto rojo |

El registro nunca dice si algo está terminado; el marcador nunca dice en qué fase estás.

### Contrasto: el terreno cambia

El brandbook de BORN hace tomas de color a sangre — *"the page turns Rojo Valentino at the
end"*. El entregable hace lo mismo, y es lo que lo saca de plano:

- **La portada abre en tinta**, partida contra marfil, con la prenda en el lado claro.
- **El proceso son tres actos y el fondo es el argumento:** papel → tinta → Rojo Valentino.
  Una idea en papel, probada en la oscuridad, nacida en color.
- **Cada prenda abre con un póster a sangre:** el número a 15vw en rojo besando el nombre en
  versales Didone **en contorno** —el estado *sketched* a escala de cartel—, la prenda sobre
  una plancha marfil, y debajo la línea de especificación en mono. El lado que ocupa la
  prenda **alterna** en cada estilo, y la hoja técnica de abajo alterna con él: el documento
  zigzaguea.
- **El póster seduce, la hoja especifica.** Ningún tecnicismo se pierde: el código, la
  composición, el gramaje y el rango de tallas van en el póster mismo.

### La fase como sistema, no como capítulo

Una fase no es algo por lo que se pasa una vez: es un juego de propiedades gráficas que
heredan todos los filetes, tintes y marcas del documento. Cada fase posee **una línea**,
**un color** y **una textura**:

| Fase | Línea | Color | Textura |
|---|---|---|---|
| **Sketched** | punteada | grafito | retícula de construcción |
| **Stitched** | pespunte | tinta | trama diagonal |
| **BORN** | sólida | Rojo Valentino | papel limpio |

Y el documento **cruza contigo**:

- **La cabecera siempre dice en qué fase estás.** Al bajar, el nombre, la línea y el color
  del indicador cambian —y con ellos la barra de avance—. Se lee sin buscarlo.
- **La hoja técnica de cada prenda toma la fase de la vista que estás mirando.** Pasas la
  galería de *Drawn* a *Sampled* y la hoja entera cruza: la banda superior cambia de nombre
  y de línea, los filetes pasan de punteado grafito a pespunte tinta, el tinte del fondo se
  desplaza. La fase deja de ser decorativa y pasa a ser operativa.
- **Cada documento declara su fase** bajo la cabecera, con la línea y el color de esa fase:
  el tech pack es *Sketched*, el fitting report y la facturación son *Stitched*, el handover
  es *BORN*.

### La sala se abre

- **Puerta de entrada.** Antes del cliente, una pantalla que dice qué es esto: *The Project
  Room*, con el wordmark madurando al llegar —sketched, stitched, born— que es el argumento
  entero del estudio en tres segundos.
- **Las tres fases se recorren, no se pasan.** La sección se fija en pantalla y el fondo se
  transforma con el scroll: papel con retícula de construcción → tinta con trama diagonal →
  **Rojo Valentino**. Cada estado sostiene su terreno mientras se lee y cruza rápido entre
  uno y otro, así que nada se lee nunca sobre un color a medias.
- **La flecha del menú se arrastra.** El piquete rojo bajo la navegación es un control real:
  se agarra y se desliza por la regla graduada, los destinos se iluminan al pasar, y al
  soltar salta al más cercano y abre esa sección. También responde a las flechas del teclado.
- **La página se vuelve roja al llegar al pie.** No solo el cierre: la cabecera entera cruza
  a Rojo Valentino con el wordmark y la navegación en negativo. El viewport completo se tiñe.

### El rojo cierra

Cada pestaña **abre a sangre y cierra en Rojo Valentino**:

- El **encabezado de cada documento** es un campo a sangre en tinta —en rojo para el
  handover— con el título en versales Didone a escala de cartel y la fase declarada debajo.
  El numeral de la fase se imprime en contorno a escala de portada, sangrado por el borde
  derecho, y deriva contra el scroll; el título entra palabra por palabra desde su propia
  línea de base y se detiene. Lo que hay que leer está quieto cuando se lee.
- El **veredicto** del fitting report es un campo en tinta a sangre.
- Y **todas las pestañas terminan con la página volviéndose roja**. El cierre no es un pie:
  es el final de la frase del estudio, y lo lee la barra de scroll. El Rojo Valentino sube
  desde el pie y se traga el papel cuadriculado; la marca se dibuja, se pespuntea y se pone
  sólida; y lo último que queda en pie es el logotipo terminado —**BORN, con su punto**—
  con la firma del documento debajo. Se puede detener en cualquier estado, y va hacia atrás
  si se sube. Sin JavaScript, con *reduced motion* y al imprimir, todo colapsa al fotograma
  final: la marca terminada sobre rojo.

### Los encabezados de sección

Dentro de cada documento, la etiqueta de sección se escribe una sola vez y en texto plano;
el sistema hace el resto (`heads()` en `build_room.py`). El nombre pasa a la Didone, lo que
seguía al punto medio se queda al lado en cuerpo pequeño —el matiz que necesita el lector
técnico junto al título que necesita quien escanea—, y la sección se numera sola con un
contador CSS. Es un contador y no un número escrito en el marcado a propósito: el tech pack
muestra un estilo a la vez, y una sección que no está en pantalla no debe llevarse un
número. La regla sobre la que abre se dibuja en la línea de su fase —punteada mientras se
dibuja, pespunteada mientras se prueba, sólida cuando ya es BORN— y se traza de izquierda a
derecha al llegar.

### El lenguaje: la hoja de patrón

El vocabulario no es "editorial" en general — es **patronaje**. Es lo que hace que esto no
se parezca a cualquier otro documento:

- **La costura.** Cada división es una línea sólida con su compañera punteada 5 px debajo:
  línea de costura y margen de costura. Un solo detalle, en toda la página.
- **El hilo (*grainline*).** La flecha de doble punta abre cada sección, en vez de un
  numerito o una etiqueta.
- **El piquete (*notch*).** Lo activo se marca con un corte en el filete, no con un
  subrayado.
- **La regla graduada.** El borde inferior del header está graduado y el avance de lectura
  lo va llenando en rojo: una cinta métrica. El código de estilo también se apoya en una.
- **La ficha técnica como layout.** El índice del estilo vive en su propio canal a la
  izquierda, el nombre arranca en el borde de texto, las medidas van a la derecha.

### La regla de voz

**Una etiqueta es algo que dice una persona**, así que va en la tipografía de texto, en
caja baja. **La monoespaciada se reserva para lo que produjo una máquina**: códigos,
medidas, fechas, dinero. Nada más se compone en ella. Antes había versalitas espaciadas en
mono en cada bloque de la página — es la señal más reconocible de "documento generado", y
ya no queda ninguna.

### Decisiones de diseño

- **Los dibujos flotan, las fotografías se enmarcan.** Flats, colorways y renders van con
  `mix-blend-mode: multiply` sobre el marfil: el blanco desaparece y la prenda queda sobre
  el papel sin caja. Solo las fotografías llevan marco, porque solo ellas son de un objeto
  que ya existe.
- **Sin tarjetas.** La estructura sale del espacio, la alineación y la escala. Los filetes
  son capilares y solo aparecen donde hay una división real. El borde se reserva para dos
  cosas: la acción abierta del cliente y una hoja que se va a imprimir.
- **Contraste de escala.** Bodoni a 12rem contra Space Mono a 11px, sin nada compitiendo
  en medio.
- **El rojo es escaso.** Solo marca lo vivo, lo que espera al cliente y lo fuera de
  tolerancia.
- **Responsive de verdad.** Nada se oculta: cambia cuánto sitio recibe cada parte y a qué
  ancho se compone el texto. En móvil la navegación es una tira que se desliza, la portada
  antepone la imagen, la bitácora conserva su espina y las tablas anchas se desplazan con
  el borde difuminado como señal.

### La bitácora

Entradas fechadas con **anatomía idéntica** —fecha, tipo, titular, cuerpo— y **carga
distinta según el tipo de información**. Nueve tipos: `Note` · `Decision` · `Materials` ·
`Colour` · `Release` · `Sample` · `Measure` · `Approval` · `Watch`. Una `Decision` muestra
elegido contra considerado, el porqué y lo que costó. Una `Measure` muestra solo los puntos
fuera de tolerancia con su causa —patrón o fábrica— y enlaza al POM completo.

### Datos y pipeline

El contenido vive en `tools/room_data.py`, que **no sabe nada de cómo se ve nada**.
`tools/build_room.py` es el motor. Abrir una sala nueva es copiar el primero, reemplazar
`PROJECT`, `STYLES` y `ENTRIES`, y compilar.

```bash
python3 tools/extract_layo.py    # deck aprobado -> deliverables/assets/*.jpg (37)
python3 tools/build_room.py      # -> deliverables/index.html
```

Cada imagen se emite **una sola vez** como regla de hoja de estilo y cada uso la referencia,
así una foto que aparece en seis sitios pesa una. Requiere `pymupdf` y `pillow`.

La demo va montada sobre el entregable real de **LAYO**: style numbers, calidades, Pantones
TCX, flats, renders y fotografía salen de `source/BORN_LayoCapsule_DesignStage.pdf`.

---

Estrategia y marca — **Matisis Consultancy** · para María, fundadora de BORN Studio.
