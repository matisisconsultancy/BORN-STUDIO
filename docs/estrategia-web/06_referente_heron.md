# 06 — Referente: heronaiapp.com → lenguaje de experiencia para BORN

**Análisis en Chromium (Playwright) · 5 nov 2026** · escritorio 1440×900 y móvil 390×844, recorrido completo con scroll real.
Diseño de Bearplus (agencia), hecho en Webflow; distintivo de *Site of the Day* visible en la página.

> **Regla de uso:** se replica el **lenguaje y la mecánica** (cómo se cuenta, cómo reacciona al scroll, cómo se organiza la retícula), **no** su código, ilustraciones, textos ni composición exacta. Todo se reconstruye con la identidad, el contenido y los activos de BORN.

---

## 1. Por qué funciona tan bien para BORN

Heron cuenta la historia de su producto con el **dibujo técnico de un arquitecto**. BORN tiene el equivalente exacto en el **dibujo técnico de una prenda**. Casi todas sus decisiones tienen un paralelo literal en la marca:

| Heron | Qué hace | Equivalente BORN (ya existe en la marca) |
|---|---|---|
| Alzado en línea que se convierte en render | El edificio pasa de plano a realidad | **Sketched → Stitched → BORN**: flat técnico → colorway → render 3D → foto de muestra (la secuencia del deck de LAYO) |
| Línea roja que barre la pantalla con % de carga | Preloader técnico | La **cinta métrica** y el punto rojo que *nace* al final |
| Fondo papel con grano, filetes capilares, cruces `+` en las esquinas | Hoja de dibujo | La **hoja de patrón** del Project Room: costura + margen de costura, piquetes, retícula |
| Un único acento rojo | Lo vivo, lo que importa | **"El rojo se gana"** (Rojo Valentino) |
| Mono para datos (`TYPE : TECHNOLOGY…`, `001 INITIALIZE…`) | Registro técnico | **Space Mono solo para datos** (regla de marca) |
| Plano que se construye muro a muro con el scroll | La construcción como relato | Piezas de patrón que se ensamblan en la prenda |
| Marcadores rojos clicables `[CLICK ON VIOLATION]` | El producto detecta problemas | Las **notas de fitting / fuera de tolerancia** (Fitting Report) |
| Observe → Advise → Act → Learn en scroll horizontal | El método como secuencia | Las fases con sus entregables |
| Wordmark gigante en contorno en el pie | La marca dibujada | El wordmark **en estado *sketched*** (`state_sketch.svg` ya existe) |

**[I]** Heron demuestra lo que la estrategia pedía (02 G7): *mostrar el proceso, no prometerlo*. Para Heron es una metáfora; para BORN es literal, porque el plano de una prenda es su trabajo real.

---

## 2. Anatomía del referente (orden de la página)

| # | Sección | Mecánica observada | Valor |
|---|---|---|---|
| 1 | **Preloader** | Alzado en línea + línea roja horizontal con contador (99%, 100%); bloque de ficha técnica en mono (TYPE / FOUNDED / FOCUS / LOCATION) y log numerado `001…010` | Primera impresión técnica y artesanal |
| 2 | **Transición a render** | El dibujo en línea se rellena hasta un render fotorrealista; aparece la cabecera | El concepto de marca en 3 segundos |
| 3 | **Hero partido** | Titular grande · texto descriptivo · enlace *Discover more* · cinta (*marquee*) de beneficios en mono · ilustración con un círculo rojo · manifiesto · *Learn more* · carrusel de logos de clientes | Mucha información con jerarquía clara en una retícula de celdas |
| 4 | **Problemas [01]–[04]** | Cuatro columnas con icono de alambre, etiqueta (MANUAL, DISJOINTED…), título y texto | Objeciones/dolores escaneables |
| 5 | **Frase cinética** | "RIGHT THERE WITH YOU" / "FOR THE WHOLE DESIGN": revelado letra a letra, fijado en pantalla | Pausa emocional |
| 6 | **Plano que se construye** | Fijado en pantalla: los muros aparecen, luego mobiliario y cotas; un panel *Introduction* con 3 textos que avanzan (`[SCROLL TO CONTINUE]`); al final, **marcadores rojos 01–03** clicables | Relato + interacción con el producto |
| 7 | **Producto [01] [02]** | Dos módulos con imagen de interfaz y *Learn more* | Oferta |
| 8 | **Método** | Fijado: OBSERVE → ADVISE → ACT → LEARN; una barra negra con la etiqueta avanza sobre una línea roja; los planos cambian | Proceso en 4 tiempos |
| 9 | **Use cases** | Acordeón de perfiles (Architects, Interior designers…) con imagen | "Esto es para ti" |
| 10 | **CTA final** | Ilustración + "See what Heron can do" + botón rojo | Conversión |
| 11 | **Pie** | Retícula con columnas de enlaces, suscripción, dirección, isotipo en línea y **wordmark gigante en contorno** | Cierre de marca |

**Técnica:** Webflow + **GSAP** (ScrollTrigger, SplitText, TextPlugin) + **Lenis** (scroll suave) + Barba (transiciones de página) + Swiper. Analítica: Clarity, Mixpanel, GA. Tipografías: BT Grotesk (todo en mayúsculas) y Geist Mono. Móvil: mantiene la misma narrativa en una columna, con los planos fijados a ancho completo.

---

## 3. La versión BORN, sección por sección

| # | BORN | Contenido | Interacción | Activos necesarios |
|---|---|---|---|---|
| 1 | **Preloader "Sketched"** | El wordmark BORN se dibuja en contorno mientras la **cinta métrica** mide 0 → 100; al llegar, cae el **punto rojo**. Debajo, el **title block de un tech pack** en mono: `STUDIO : BORN APPAREL STUDIO · FOCUS : APPAREL DEVELOPMENT & PRODUCTION · BASE : GUADALAJARA, MX · CLIENTS : US · EU` y un log `001 BRIEF RECEIVED … 010 PPS APPROVED` | Una vez por sesión; se puede saltar; *reduced motion* = fotograma final | Ya existe (animaciones *Ensamblaje* y *Barrida*) |
| 2 | **Una prenda nace** | La misma prenda pasa de **flat técnico → colorway → render → foto de la muestra** con el scroll, marcando la fase en el lateral | Fijado en pantalla, 4 estados | **Una prenda con permiso** (ver §5) |
| 3 | **Hero** | *Your outsourced production department.* + texto (*We manage development and production preparation for emerging apparel brands, on your side of the factory relationship.*) + **Book a consultation** + cinta `VIABILITY · COST · USABILITY` + manifiesto + **franja de logos** de clientes | Cinta en bucle lento | Logos (8 ya en las plantillas: Party Wave, Skratch, Cloud Nine, Good Boy, Rebalance, Twolip, Viva Cuerpo, ZOFAD), con permiso para la web |
| 4 | **Where we step in [01]–[04]** | 4 de los 8 riesgos de la Production Proposal (*fábrica elegida por precio · aprobar una muestra que no está lista · construcción que no sabías cuestionar · un detalle que llega al bulk*) | Iconos en línea de prendas y patrones | Iconos SVG propios |
| 5 | **Frase cinética** | *On your side* / *of the factory.* (en Bodoni, revelado palabra a palabra) | Fijado breve | — |
| 6 | **El fitting interactivo** | Las **piezas de patrón** se ensamblan en la prenda; 3 textos de introducción avanzan; aparecen **marcadores rojos** sobre la prenda: `01 · Shoulder seam twists +0.8 cm` · `02 · Thumb hole sits 1 cm low` · `03 · Waistband rolls at CB`; al tocarlos, se abre la nota de fitting con la corrección | *Click on the issue* (lenguaje del Fitting Report) | Flat/patrón en SVG por capas + 3 notas reales (o ilustrativas, declaradas como tales) |
| 7 | **Servicios [01]–[03]** | Design & tech packs · Factory pairing · Production partnership (+ consulta) con precio y *Learn more* | Módulos en retícula | Imágenes reales de cada fase |
| 8 | **El método** | **Sketched → Stitched → BORN** (+ *Born to be made*) con entregables y plazos oficiales; la barra que avanza es la **cinta métrica** | Horizontal fijado | — |
| 9 | **Who it's for** | Acordeón por situación (*I have an idea / designs / tech packs / a sample*) o por categoría (activewear, loungewear, golf, swim) | Acordeón con imagen | Fotos por categoría |
| 10 | **Prueba** | Casos (Party Wave $40,000; Skratch, 2 samples to PPS) + reseña de Upwork | — | Permisos |
| 11 | **Cierre en rojo** | *From idea to life.* + **Book a 1:1 consultation**; la página se vuelve Rojo Valentino (como en el brandbook) | Transición de fondo | Ya existe en el sistema |
| 12 | **Pie** | Retícula de enlaces + **wordmark BORN gigante en estado *sketched*** con sus líneas de construcción | Se dibuja al llegar | `state_sketch.svg` |

**Cómo lo mejoramos con el estilo BORN:**
- **Tipografía editorial, no grotesca en mayúsculas:** Bodoni para la voz, Jost para leer, Space Mono solo para datos. Es lo que separa a BORN de una estética SaaS.
- **El rojo se gana:** un solo rojo, solo en el punto, lo activo, lo fuera de tolerancia y el cierre.
- **Fotografía real, no renders generados:** Heron usa arquitectura brutalista ilustrada; BORN enseña muestras reales (los dibujos flotan, las fotos se enmarcan).
- **La voz:** directa, cálida y precisa, en lugar del tono de producto de software.
- **El sistema por fases:** cada sección toma su registro (punteado / pespunte / sólido), como ya hace el Project Room.

---

## 4. Qué no copiar

- **Ilustraciones, textos, composición exacta, código o marca de Heron/Bearplus.** Solo patrones y mecánicas.
- **El *scroll* secuestrado** (Lenis con contenedor fijo): la página dejó de responder a `scrollTo` en la prueba. Se usa el scroll nativo, con animaciones atadas a él.
- **Todo en mayúsculas** y un tono de producto de software.
- **El exceso de librerías** (Barba, Swiper, jQuery): con GSAP y CSS basta.
- **El banner de cookies que tapa el contenido** durante todo el recorrido.

---

## 5. Viabilidad (encaja con la opción E: web en código)

| Aspecto | Evaluación |
|---|---|
| Desarrollo con Claude Code | **Viable**: secuencias con GSAP + ScrollTrigger sobre SVG/imágenes, sin Webflow |
| Librerías | GSAP (licencia gratuita con condiciones, **verificar los términos vigentes**); sin Lenis ni Barba |
| Rendimiento | Riesgo medio: secuencias de imágenes pesadas. Se mitiga con SVG para los dibujos, imágenes AVIF/WebP, carga diferida y un **presupuesto de peso por página**. No medí el peso de Heron |
| Accesibilidad | Obligatorio: `prefers-reduced-motion` → estados finales estáticos; todo el texto legible sin animación; el preloader se puede saltar; los marcadores, operables con teclado |
| Móvil | Viable: misma narrativa en una columna (como Heron); secuencias más cortas |
| Edición por María | Textos, precios, casos y notas de fitting en archivos de contenido; **las secuencias animadas son código** (cambiar la prenda protagonista requiere a Matisis) |
| Calendario (20 nov) | **Ajustado.** Prioridad: preloader (reutiliza las animaciones existentes), hero, método, cierre rojo y pie. La secuencia "una prenda nace" (2) y el fitting interactivo (6) dependen de los activos; si no llegan a tiempo, salen en versión estática y se animan en la 2.ª revisión |

**El activo crítico es una prenda con permiso de uso** en sus cuatro estados (flat → colorway → render → foto). Opciones, por orden:
1. Una prenda de **LAYO** (el deck tiene exactamente esa secuencia), con permiso escrito.
2. Una prenda de otro cliente con permiso (Party Wave, Skratch…).
3. Una prenda de la **propia línea de activewear de María** (es suya: sin permisos).
4. Si no hay nada a tiempo: una **prenda dibujada por Matisis** para la web (flat y patrón en SVG), sin render ni foto, que se completa después.

---

## 6. Decisiones para avanzar

1. ¿Aprobáis esta traducción sección por sección como estructura de la Home?
2. ¿Qué prenda protagoniza la web (§5)? Es lo que más condiciona el calendario.
3. ¿Se pueden usar en la web los 8 logos de clientes de las plantillas?
4. ¿Notas de fitting reales (de un Fitting Report) o ilustrativas, declaradas como tales?
