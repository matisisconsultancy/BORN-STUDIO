# 05 — Sitemap y guion por página

**Born Apparel Studio · bornapparelstudio.com · v1 para revisión** · 5 noviembre 2026
Se apoya en [02](02_inteligencia_competitiva.md), [03](03_publicos_oportunidades_y_decisiones.md) y [09 §14](09_viabilidad_tecnica_y_arquitectura.md) (web en código + tienda Shopify enlazada).

**Supuestos de trabajo** (corregibles si María dice otra cosa):
- Web **solo en inglés** (confirmado por Matisis).
- Portada centrada en *your outsourced production department*, con diseño y tech packs como puerta de entrada.
- **Un único llamado principal: *Book a 1:1 consultation*.**
- Tienda en `shop.bornapparelstudio.com`.
- Lead magnet alojado en Shopify.
- Los precios son los de las propuestas vigentes; el de la consulta está pendiente (D9).

---

## 1. Sitemap

```
bornapparelstudio.com
│
├── /                              Home
├── /how-we-work                   El proceso: Sketched → Stitched → BORN · los tres filtros · qué no hacemos
├── /services                      Índice por situación: "Where is your product today?"
│   ├── /services/design-and-tech-packs        Sketched · Collection design + technical development
│   ├── /services/factory-pairing              Stitched · Factory match · Sourcing & comparison
│   ├── /services/production-partnership       Stitched → BORN · flagship (proyecto y colección)
│   └── /services/consultation                 1:1 con Maria
├── /pricing                       La escalera completa · qué no incluye
├── /work                          Casos (filtro por categoría: activewear · loungewear · golf · swim)
│   └── /work/[case]               Plantilla de caso
├── /about                         Maria (la fábrica primero) · el equipo · las cifras
├── /faq                           Preguntas frecuentes (objeciones de la Production Proposal)
├── /free-guide                    Lead magnet → formulario en la tienda
├── /book                          Reservar la consulta · qué pasa en la llamada
│   └── /book/brief                Client brief (opcional, antes o después de reservar)
├── /contact                       Email, redes, ubicación
├── /privacy · /terms              Legales del sitio (formularios y analítica)
├── /journal                       [Fase posterior: se publica con el primer artículo]
│
└── ↗ shop.bornapparelstudio.com   Tienda Shopify (templates · guía gratuita · emails)
```

**Profundidad máxima: 2 niveles.** Todas las páginas quedan a un clic de la navegación o del pie.

## 2. Navegación

**Cabecera (desktop):** `How we work` · `Services ▾` · `Work` · `Pricing` · `About` · `Shop ↗`  **[Book a consultation]**
**Cabecera (móvil):** wordmark + botón *Book* siempre visible + menú. El menú repite el orden anterior y añade el indicador de fase.
**Pie:**

| Studio | Services | Resources | Contact |
|---|---|---|---|
| How we work | Design & tech packs | Free guide | Email |
| Work | Factory pairing | FAQ | Instagram |
| About | Production partnership | Shop ↗ | Upwork reviews ↗ |
| Pricing | 1:1 consultation | — | Privacy · Terms |

**Navegación contextual:** cada página de servicio enlaza al paso anterior y al siguiente del proceso (p. ej. Factory pairing ← Design & tech packs | Production partnership →), a su fase en `/how-we-work`, a sus casos filtrados y a su fila en `/pricing`.

## 3. Prioridad para el 20 de noviembre

| Página | Prioridad | Condición |
|---|---|---|
| Home, How we work, Services (×5), Pricing, About, Book, Contact, 404 | **Imprescindible** | Contenido base ya existe en las propuestas |
| Work + plantilla de caso | **Imprescindible** | Se publica con los casos que tengan permiso (mínimo 2); si no hay permiso, casos anonimizados por categoría |
| FAQ, Free guide, Book/brief, Privacy/Terms | **Imprescindible** | Free guide depende del tema confirmado; legales, de un texto que debe validar María |
| Journal | **Fase posterior** | Sin artículos no se publica (una sección vacía resta confianza) |
| Project Room (demo) | **Futuro** | Fuera de alcance |

---

## 4. Guion por página

> Formato: **objetivo · público · mensaje · secciones en orden · llamado · SEO**. **Fuente** indica de dónde sale el contenido existente; **Falta** indica lo que tiene que dar María.

### Home `/`
- **Objetivo:** en 5 segundos, que el visitante entienda qué es Born y que no es una fábrica ni un freelance de tech packs; llevarlo a la consulta o a su servicio.
- **Público:** A (diseño listo) y B (idea); también quien llega desde Upwork o Instagram.
- **Mensaje:** *Your outsourced production department. From idea to life.*
- **Secciones:**
  1. **Hero:** titular, subtítulo (*"We manage development and production preparation for emerging apparel brands, on your side of the factory relationship."*), botón *Book a consultation* y enlace secundario *See how we work*. El wordmark madura (sketched → stitched → BORN).
  2. **"Where is your product today?"**: cuatro entradas (*I have an idea · I have designs · I have tech packs · I have a sample*), cada una a su servicio.
  3. **El proceso en una línea:** Sketched → Stitched → BORN, con el entregable de cada fase → `/how-we-work`.
  4. **Prueba:** cifras oficiales + 2–3 casos + reseña de Upwork verificable.
  5. **Los tres filtros:** viabilidad, costo, usabilidad.
  6. **Maria:** retrato, dos líneas ("learned on production floors in Portugal, Spain, Los Angeles and Austria") → `/about`.
  7. **Escalera de inversión resumida** (desde $X) → `/pricing`.
  8. **Cierre a sangre en rojo:** *From idea to life* + *Book a consultation*.
- **SEO:** title *Apparel Development & Production Studio for Emerging Brands | Born Apparel Studio*; `Organization` + `ProfessionalService`.
- **Fuente:** Services Deck, Production Proposal, Brand Book. **Falta:** cifras oficiales, retrato, permisos de casos.

### How we work `/how-we-work`
- **Objetivo:** mostrar el método, no prometerlo. Es la página diferencial frente a la competencia (02 G7).
- **Mensaje:** *Every stage ends with an outcome.*
- **Secciones:** introducción (*the brand's side of the table*) → **mapa interactivo de las tres fases** con, por cada fase: pasos, entregables, plazos, decisiones del cliente y servicio asociado → los tres filtros → **qué no hacemos** (no cortamos ni cosemos, no compramos material, no invertimos) y por qué te protege → "Where we step in" (los 8 riesgos) → llamado.
- **SEO:** *apparel product development process*, *how clothing production works*. Datos estructurados `HowTo` si encaja.
- **Fuente:** Production Proposal (5 etapas, 8 riesgos), Brand Book (fases y plazos). **Decisión:** unificar los plazos (brandbook: 2–6 meses; propuesta: 3–5 meses), ver V5.

### Services `/services`
- **Objetivo:** que cada visitante se ubique en 10 segundos.
- **Secciones:** *Enter wherever your brand is today* → cuatro tarjetas-fase (servicio, para quién, resultado, desde $) → comparador *Two paths, one destination* (Factory pairing frente a Production partnership) → llamado.
- **Fuente:** Services Deck pp. 6–7, Production Proposal p. 4.

### Design & tech packs `/services/design-and-tech-packs` (Sketched)
- **Para quién:** B (idea o referencias).
- **Mensaje:** diseño al servicio de la fabricación: *designed to be made*.
- **Secciones:** problema → qué incluye (sketches, revisiones, tech pack con BOM, POM, graduación, costuras, etiquetado) → **ejemplo de tech pack** (imagen real con permiso o el template de Born) → plazos → precio por estilo → siguiente paso (Factory pairing) → FAQ → llamado.
- **Fuente:** Design Proposal AS FOUND ($200 + $250 por estilo). **Decisión:** precio público por estilo; los tech packs de $150–$250 de la tienda actual se retiran o se unifican.

### Factory pairing `/services/factory-pairing` (Stitched)
- **Para quién:** C (equipo con experiencia) y A.
- **Mensaje:** *The right factory, chosen for your product, not ours.*
- **Secciones:** problema (elegir por precio) → **Factory Match $750** y **Sourcing & Comparison $1,500** → **ejemplo anonimizado del informe comparativo** (hueco de mercado G1) → los seis países y para qué sirve cada uno (sin nombrar fábricas) → qué no incluye (Born no negocia ni garantiza el precio final) → llamado.
- **Fuente:** Production Proposal p. 11. **Falta:** confirmar si existe un informe comparativo real que se pueda anonimizar.

### Production partnership `/services/production-partnership` (flagship)
- **Para quién:** A.
- **Mensaje:** *Your outsourced production department, up to production readiness.*
- **Secciones:** "You already built the brand" (antes → después) → las 5 etapas con su resultado → qué incluye (9 bloques) → **dónde termina** (PPS aprobado, graduación validada, tech pack final, hasta 3 rondas por estilo) → dos modelos: por proyecto ($2,500–$8,400) y por colección ($3,000/mes, 3 meses mínimo) → después del bulk → qué no incluye → FAQ → llamado.
- **Fuente:** Production Proposal pp. 2–17 (texto aprobado, en la voz de la marca).

### 1:1 consultation `/services/consultation`
- **Para quién:** todos; la puerta de entrada (también para el comprador por precio, D).
- **Secciones:** para qué sirve (una decisión concreta) → formato (60 min, notas) → sesión suelta o paquete de 5 → **acreditable** en un proyecto posterior [decisión] → reservar.
- **Decisión pendiente (D9):** precio ($120 / $200 / gratis) y herramienta (Calendly o Cal.com).

### Pricing `/pricing`
- **Objetivo:** transparencia como diferencial (solo 3 de 8 competidores publican precios).
- **Secciones:** escalera acumulativa (Consultation → Design & tech packs → Factory pairing → Production partnership por proyecto → por colección) → **qué no incluyen nuestros honorarios** (muestras, telas, envíos, inspecciones, producción) → formas de pago → *Custom scope* → llamado.
- **SEO:** *apparel product development cost*, *how much does a tech pack cost*.

### Work `/work` y plantilla `/work/[case]`
- **Índice:** filtro por categoría y tarjetas con marca, categoría, fase y resultado en una línea.
- **Plantilla de caso:** ficha técnica lateral (marca, categoría, fases contratadas, estilos, rondas de muestra, región de fábrica, plazo) → la idea de origen → **la decisión clave** (lo que Born vio o dijo que no) → el resultado → imágenes (proceso + producto) → caso siguiente → llamado.
- **Fuente:** Party Wave, Skratch, ZOFAD, Twolip (propuesta); LAYO y AS FOUND (material de diseño). **Falta:** permisos y fotos. Sin permiso, se anonimiza: *"A golf brand, US"*.

### About `/about`
- **Mensaje:** *Led by someone who has already done this.*
- **Secciones:** Maria en la fábrica (Portugal, España, LA, Austria) → el teatro y la ópera como estándar añadido → cómo trabaja (1:1, equipo senior pequeño) → equipo → cifras oficiales → valores en la práctica (honestidad técnica: *"we'll tell you not to"*) → Upwork y reseñas → llamado.
- **Falta:** cifras oficiales, equipo actual, fotos reales (retrato y fábrica).

### FAQ `/faq`
- **Contenido:** las preguntas de la Production Proposal (usar mi fábrica, hablar con la fábrica, plazos, rondas extra, inspecciones, precio de 5–6 estilos, después de producción) + las nuevas (*¿sois una fábrica?*, *¿trabajáis con marcas fuera de EE. UU.?*, *¿cuál es el mínimo?*, *¿por qué cobráis la consulta?*). Datos estructurados `FAQPage`.

### Free guide `/free-guide`
- **Objetivo:** captar emails de founders que aún no están listos para la consulta.
- **Secciones:** la promesa de la guía + vista previa de 3 puntos → botón *Get the free guide* (formulario en la tienda) → qué recibirás (guía + 4 emails) → enlace a la consulta.
- **Decisión:** tema (propuesto: *The tech pack checklist: 10 things to confirm before you send it to a factory*).

### Book `/book` y `/book/brief`
- **Book:** qué pasa en la llamada, precio y duración, qué preparar → calendario integrado.
- **Brief:** formulario en dos pasos. Paso 1: nombre, email, marca, web/Instagram, etapa (idea / diseño / tech pack / muestra), categoría. Paso 2: número de estilos, unidades por estilo, horizonte de lanzamiento, presupuesto orientativo y enlace a archivos (Drive o Dropbox), en lugar de adjuntos.
- **Mensaje de confirmación:** cuándo responde Born y qué sigue.

### Contact, Privacy, Terms, 404
- **Contact:** email, Instagram, Upwork, ubicación (Guadalajara, MX · trabajando con marcas de EE. UU. y Europa) y botón de reserva.
- **Legales:** política de privacidad del sitio (formularios y analítica). **Falta** un texto validado por María; los legales de compra siguen en la tienda.
- **404:** wordmark en estado *sketched* + enlaces a Home, Services y Book.

---

## 5. Redirecciones (dominio principal → nuevas rutas)

| URL antigua | Destino |
|---|---|
| `/products/*` · `/collections/*` · `/cart` · `/account` · `/policies/*` | `shop.bornapparelstudio.com/` + la misma ruta |
| `/pages/tech-packs` · `/pages/sketches-mock-ups` · `/pages/design-services` | `/services/design-and-tech-packs` |
| `/pages/factory-sourcing` · `/pages/supply-chain` | `/services/factory-pairing` |
| `/pages/production-management` · `/pages/sample-control` | `/services/production-partnership` |
| `/pages/production-consultancy` | `/services/consultation` |
| `/pages/our-team` | `/about` |
| `/pages/our-portfolio` · `/pages/our-portfolio-1` | `/work` |
| `/pages/faq` | `/faq` |
| `/pages/contact` | `/contact` |
| `/blogs/news` | `/` (hasta que exista el journal) |

## 6. Contenido editable por María (archivos de contenido)

| Archivo | Qué contiene |
|---|---|
| `site` | Cifras oficiales, email, redes, enlace de reserva, enlace a la tienda |
| `pricing` | Todos los precios (una sola fuente para toda la web) |
| `services/*` | Textos de cada servicio |
| `cases/*` | Un archivo por caso (ficha + texto + imágenes) |
| `faq` | Preguntas y respuestas |
| `team` | Equipo |
| `pages/*` | Textos de Home, How we work, About, Free guide |

Los precios y cifras se escriben **una sola vez** y se reutilizan en todas las páginas: así no vuelve a pasar que la web diga cosas distintas en sitios distintos (V4).

---

## 7. Para revisar contigo antes de diseñar

1. ¿Te encaja la navegación (6 elementos + botón)?
2. ¿*Pricing* como página propia, o integrada en *Services*? Recomiendo propia: es un diferencial y una búsqueda frecuente.
3. ¿Mantener *Work* aunque al principio haya pocos casos con nombre?
4. Los plazos oficiales del proceso (2–6 meses o 3–5 meses).
5. El precio de la consulta.
