# 02 — Competitive Intelligence & Market Benchmark

**Born Apparel Studio · Nuevo sitio web · Fase 2**
Matisis Consultancy · 5 noviembre 2026 · Se apoya en [01](01_auditoria_estrategica.md) y [01b](01b_auditoria_web_actual.md)

> **Método.** 20 sitios revisados en directo el 5 nov 2026 (HTML obtenido con curl/WebFetch y analizado; sin render visual, así que lo que carga por JavaScript, como formularios embebidos, puede faltar). Las citas entre comillas son literales. **No hay datos de tráfico, autoridad ni conversión de ningún sitio**: no se han usado herramientas de pago (Ahrefs y Similarweb requieren autorización en esta sesión) y no se infieren. Upwork y Fiverr bloquearon el acceso (403); de ellos solo hay *snippets* de buscador, marcados como tales.
> **[C]** observado · **[I]** insight · **[H]** hipótesis · **[R]** recomendación.

---

## 1. El entorno competitivo real

**Sector.** Servicios B2B de desarrollo de producto textil para marcas emergentes: el tramo entre "tengo un diseño" y "mi pedido sale de fábrica". **Geografía de venta:** EE. UU. y mercados anglófonos; base de operación en Guadalajara (MX), con fábricas en seis países. **Posición real de Born:** intermediario técnico *del lado de la marca*, sin fábrica propia. [C — 01]

Born compite en **cuatro frentes distintos**, y cada uno pide a la web una respuesta diferente:

```
                     ¿Quién hace el trabajo técnico?
          el propio founder ◄──────────────────────► un tercero experto
                │                                          │
 HERRAMIENTA /  │  Techpacker / tpbuilder                  │  Estudios-agencia
 PLATAFORMA     │  Maker's Row · Sewport                   │  Human B · AJG · Tech Packs Co
 (self-serve)   │  plantillas (incl. la tienda de Born)    │  Franky Dune · Nítido · Blue Associates
                │                                          │  ──► BORN (sin fábrica propia)
 FREELANCE /    │  Upwork · Fiverr                         │
 POR TAREA      │  (tech pack de $15–$250)                 │  Fábricas full-package que venden desarrollo
                │                                          │  Lefty (LA) · Tulum (Medellín)
                │                                          │  Apparel Production Inc (NYC)
```

| Tipo | Quiénes | Por qué compiten con Born | Respuesta que exige a la web |
|---|---|---|---|
| **Directos**: estudios/agencias de desarrollo y gestión | Human B, AJG Fashion Consulting, Tech Packs Co, Franky Dune, Nítido, Blue Associates Sportswear | Misma necesidad, mismo cliente, modelo similar (consulta → desarrollo → retainer) | Diferenciación **específica**, no de categoría |
| **Híbridos**: fábricas que venden desarrollo | Lefty Production Co, Tulum Fashions | Resuelven desarrollo y producción con un solo proveedor | Explicar por qué la **independencia** de la fábrica protege al founder |
| **Indirectos**: marketplaces y herramientas | Upwork, Fiverr, Maker's Row, Sewport, Techpacker | Alternativa barata o DIY; fijan el **ancla de precio** | Mostrar lo que pasa *después* del tech pack |
| **Referentes aspiracionales** (no competidores) | Anderson & Sheppard, ASKET, Pentagram, LAYER | Narrativa de oficio y de proceso | Transferir patrones, no estética |
| **Referentes de conversión** | Lefty (intake), Tulum (formulario de 7 preguntas), Human B (sesión de pago), Designjoy, Metalab, Maker's Row (escalera de precios) | Recorridos comerciales claros | Mecánica de cualificación y precio |

**Selección y criterio.** Se priorizó la relevancia: sitio público en inglés, oferta para founders emergentes, gestión más allá del tech pack y al menos un especialista en activewear, uno de Europa/Portugal y uno de LatAm. **Se descartaron:** Indie Source (error SSL), Factory45 (página vacía; además es educación), Sqetch (dominio con spam de casino), Successful Fashion Designer (cerrado), Nimble Made (es una marca de ropa), Appareify, Epsilon y GLC (periféricos). **No se encontró ningún estudio con base en México, modelo comparable y sitio sólido en inglés** (Mexmakers es escueto; Loomex bloqueó el acceso). [H] Es un hueco geográfico real.

---

## 2. Fichas de competidores directos e híbridos

> Formato compacto: lo esencial por dimensión A–F. Detalle completo y URLs en §8.

### 2.1 Human B · Nueva York · *el competidor más cercano en discurso*
- **A. Posicionamiento:** *"Make Better Production Decisions Before You Spend Thousands on Development and Manufacturing."* Tesis: *"Most fashion brands don't fail in production. They fail before it."* FAQ: *"We act as your production department and single point of contact"*: **casi la frase de Born**.
- **B. Relato:** racional, centrado en el riesgo; se presenta como asesor, no como vendedor (*"Our goal isn't to convince every client to outsource"*). Tres testimonios con nombre.
- **C. Arquitectura:** Home · Services · Resources · About · Contact · Blog; 380 URLs, 296 posts; catálogo de consultoría con aspecto de tienda.
- **D. UX/UI:** tarjetas por niveles; erratas visibles ("Managment"); aspecto de plantilla Squarespace.
- **E. Conversión:** **entrada de pago**: Strategy Session $245, Readiness Audit $845, Oversight $1,250, paquetes $800–$975; *"This is not a discovery call. It is a structured working session."* Lead magnet *"5 Production decisions to make before you commit"*. La gestión completa, sin precio y con admisión selectiva.
- **F. SEO:** title "Human B" (sin keywords); `LocalBusiness`, `Organization`.

### 2.2 AJG Fashion Consulting · Austin, TX
- **A.** *"Scale Your Apparel Designs into Manufacturing Realities"*; *"For The Cost of One Salary You Get Our Whole Team"*; segmentos por etapa: Launching, Growing, Scaling; *"plug and play operations team … without the overhead of an in-house production department"*.
- **B.** Mentor + operador; ~9 testimonios con nombre, *Featured In*, "8 Shark Tank Brands". **Cifras que se contradicen entre páginas** (74% / 73% de margen; 80+ / 70+ años de experiencia).
- **C.** Servicios por etapa de marca, con "Success Stories" en la navegación; 96 posts; tienda de plantillas.
- **D.** Proceso de 6 pasos numerados (kick-off → ships); tickers.
- **E.** Una CTA repetida: *"Book Your Free Strategy Call"*; formulario → calendario inmediato → llamada de 30 min; guía descargable. **Sin precios.**
- **F.** `ProfessionalService`, `Person`, `LocalBusiness`; title con keywords.

### 2.3 Tech Packs Co · Los Ángeles + Manila
- **A.** *"Clothing & Textile Product Design, Tech Packs + Development"*; promesa *"60-80% gross profit margin & <10% return rates"*; equipo en Filipinas con un PM en EE. UU.
- **B.** Abre con el dolor (*"bitter disappointment of receiving back samples…"*); testimonios con estrellas; tono comercial, con emojis.
- **C.** 112 URLs, 82 posts; recursos (fabric directory, production planner, examples).
- **D.** **"9 Phases" con entregables por fase**; ejemplo de tech pack descargable.
- **E.** *"Book a Sales Call"*; **precios públicos**: $450 / $1,600 / $2,800 por producto; retainer **$1,500/mes (~18 h), mínimo 3 meses**. Objeción Fiverr resuelta en la FAQ (*"In 1 word - quality"*).
- **F.** Title con keywords; solo `WebSite`.

### 2.4 Franky Dune · Oporto, Portugal
- **A.** *"Product Development Management for fashion brands manufacturing their collections in Portugal"*; volumen mínimo ~150 u./estilo/color.
- **B.** **Voz de fundadora, emocional y en primera persona** (*"My factory ghosted me." / "I feel vulnerable."*).
- **C.** La home está dominada por directorios de pago (€35–€49) y plantillas; 62 posts.
- **E.** Calendly gratuito; consulta de pago €250 y *Strategy Call* €125 **acreditable en la primera factura**. Copy caducado ("Booking now for August 2025").
- **F.** Subpáginas con `<title>` "home".

### 2.5 Nítido Agency · Oporto
- **A.** *"Production in Portugal for fashion brands that care about quality"*; 7 servicios numerados; **plataforma de cliente** (task tracking, acceso móvil).
- **B.** Credibilidad prestada: cita marcas que producen *sus fábricas* (Balenciaga, Victoria Beckham), no clientes propios.
- **E.** *"We are currently not accepting new project enquiries."* Sin precios.
- **F.** Sin H1 útil y sin datos estructurados.

### 2.6 Blue Associates Sportswear · Reino Unido · *especialista activewear*
- **A.** *"Build your sportswear brand with 1 expert team, 30+ years of expertise and 1 monthly fee."* Tagline: *"You build the brand. We build the product."* Especialización por deporte (golf, gym, running, ski…).
- **B.** Autoridad del CEO; marcas de golf con nombre; lenguaje que filtra (*"We don't work with clients chasing the last cent"*).
- **C.** Navegación por deporte; 376 URLs (217 posts, 102 productos).
- **D.** **Plazos por etapa** (Brief & Quote 2–6 semanas … Production 16–24 semanas); regla de coste (PVP ÷ 4 Asia, ÷ 2.65 Europa).
- **E.** Presupuesto gratuito + **1:1 de pago con el CEO, reembolsable** (*"We get around 15-20 enquiries a day… to make sure we are talking to clients that are serious"*). Cuota mensual no publicada.
- **F.** Landings por categoría de deporte; `Organization`, `OnlineStore`.

### 2.7 Tulum Fashions · Medellín + showroom en LA · *híbrido (fábrica)*
- **A.** *"Clothing manufacturer in Medellín, Colombia."* Subtítulo: *"from 150 units per style, in 6–8 weeks, developed with the founder."* Argumento de **nearshoring con datos** (arancel del 12.5% frente al 36–52% de China; misma zona horaria; tabla que incluye México/USMCA).
- **B.** *"No fabricated quotes. No stock photos of strangers in suits."* Sección de lo que **terceros** han publicado sobre ellos.
- **C.** Story · Guides · Los Angeles · Start your collection · **EN/ES**; guías y landings por ciudad.
- **E.** *"Seven questions. We reply within 24 hours."* (categoría, unidades por estilo, etapa…) + WhatsApp. **Precios públicos al céntimo:** desarrollo $466.32/estilo ($207.25 con tech pack propio), muestra $362.69 con 3 rondas de fit; FAQ *"Why we charge for development"*, que nombra los tech packs de marketplace de $100–$500 como coste oculto.
- **F.** **Los datos estructurados más completos del set** (`FAQPage`, `Service`, `Offer`, `OfferCatalog`, `Person`); hreflang en/es.

### 2.8 Lefty Production Co · Los Ángeles · *híbrido (fábrica)*
- **A.** *"One stop shop apparel and accessories design, development & production"*; fabrica en LA; páginas de Swimwear y Athletic Wear.
- **B.** ~8 testimonios largos con nombre; prensa y proyectos notorios; fundadora ex-dueña de marca.
- **C.** Menú enorme y duplicado; 710 URLs (669 posts); páginas por país.
- **E.** Escalera de reserva (Acuity): 15 min gratis → **$55 acreditable en la factura** → **$198 coaching 60 min con la CEO** (frente a los $200 de Born). Formulario de admisión de 15 campos: etapa, presupuesto (*"most projects require a minimum 5k budget"*), unidades por estilo, ¿patrones?, imagen obligatoria.
- **F.** Webflow; `Review`; title sobrecargado de keywords.

---

## 3. Indirectos: qué fijan en la mente del comprador

| Actor | Promesa observada | Implicación para Born |
|---|---|---|
| **Upwork** *(snippets)* | Tarifas de ~$15–$50/h; trabajos de *"$150 fixed-price… factory-ready tech pack"* | **Ancla de precio** con la que llegan los leads de Upwork. La web no debe vender "tech packs" como producto aislado |
| **Fiverr** *(snippets)* | ~2,500 gigs; desde ~$15–$20 | Ancla aún más baja; no se compite en precio de tech pack |
| **Maker's Row** | *"Find Trusted Manufacturers in the USA made easy"*; gratis para marcas; **las fábricas pagan $399–$2,399/mes por visibilidad y sello "Premium"** | [H] Born puede decir cómo elige las fábricas y quién le paga (solo si es cierto y verificable) |
| **Sewport** | *"Get quotes from trusted clothing manufacturers"*; escrow; un testimonio elogia *"the exact no-agent model"* | Se vende como **anti-intermediario**: Born debe demostrar el valor del intermediario (rondas evitadas, fit, graduación) |
| **Techpacker → tpbuilder** | *"factory-ready tech packs, without Excel or Illustrator. Free"* | El documento tiende a costar cero; el valor está en el criterio que lo llena |

---

## 4. Benchmarking comparativo

**Escala observable:** **0** = ausente · **1** = presente pero genérico o parcial · **2** = explícito, específico y respaldado en el propio sitio. Puntúa lo visible el 5 nov 2026, **no el rendimiento**. Born se puntúa en dos columnas: la web actual (observada) y su **material de propuestas** (lo que podría llevar a la web, según 01).

| Criterio | Human B | AJG | Tech Packs Co | Franky Dune | Nítido | Blue Assoc. | Tulum | Lefty | **Born web hoy** | **Born propuestas** |
|---|---|---|---|---|---|---|---|---|---|---|
| 1. Claridad de posicionamiento | 2 | 2 | 1 | 1 | 1 | 2 | 2 | 1 | **0**: streetwear, freelance de tech packs | **2** |
| 2. Diferenciación | 2 | 1 | 1 | 1 | 1 | 2 | 2 | 1 | **0** | **1**: "production department" ya lo usan otros (§5-P4) |
| 3. Narrativa | 2 | 2 | 1 | 1 | 1 | 1 | 2 | 1 | **0**: abre con una cita de Michael Jordan | **2**: Sketched/Stitched/BORN |
| 4. Claridad de la propuesta de valor | 2 | 1 | 2 | 1 | 1 | 1 | 2 | 1 | **1** | **2**: qué incluye cada servicio |
| 5. Arquitectura de información | 1 | 2 | 1 | 1 | 1 | 1 | 2 | 1 | **1** | n/a |
| 6. Visibilidad del proceso | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 1 | **0** | **2**: 5 etapas con resultado |
| 7. Prueba / confianza | 1 | 2 | 2 | 1 | 1 | 2 | 2 | 2 | **1**: testimonios sin resultado; contenido ajeno | **2**: casos con resultado, Upwork 5.0 |
| 8. Transparencia de precios | 2 | 0 | 2 | 1 | 0 | 1 | 2 | 0 | **1**: precios de tienda contradictorios | **2**: escalera completa |
| 9. Mecanismo de conversión | 2 | 2 | 2 | 1 | 0 | 1 | 2 | 1 | **0**: enlaces rotos, 3 destinos distintos | n/a |
| 10. Contenido / SEO | 2 | 2 | 1 | 1 | 0 | 2 | 2 | 2 | **0**: blog vacío, sin H1 | n/a |
| 11. Adaptación móvil* | n/v | n/v | n/v | n/v | 1 | n/v | n/v | n/v | **1**: medido (17.8 MB, LCP 3.7 s) | — |
| 12. Coherencia marca ↔ experiencia | 1 | 1 | 1 | 1 | 2 | 1 | 2 | 0 | **0**: identidad anterior | — |

\* Solo se comprobó la meta *viewport* de los competidores (todos la tienen; la de Nítido bloquea el zoom). No se midió rendimiento ajeno: *n/v* = no verificado.

**Limitaciones.** La escala mide presencia y especificidad, no eficacia comercial. Una puntuación alta no significa que el sitio convierta mejor. Las puntuaciones de competidores fueron asignadas por un único analista sobre HTML estático.

---

## 5. Patrones del mercado

| # | Patrón | Dónde | Lectura |
|---|---|---|---|
| P1 | **"Avoid costly mistakes"** como promesa dominante | Human B, AJG, Tech Packs Co, Franky Dune | **Saturado.** El miedo es real (también en la Proposal de Born), pero el mensaje es intercambiable |
| P2 | **Llamada gratuita** como primer paso por defecto | Tech Packs Co, AJG, Franky Dune, Lefty, Blue | Estándar de la categoría |
| P3 | **Primera sesión de pago, acreditable o reembolsable**, como filtro | Human B ($245), Franky Dune (€125 acreditable), Lefty ($55 acreditable), Blue (reembolsable) | Tendencia emergente; justificada explícitamente como filtro |
| P4 | **"Your production department / in-house team without the overhead"** | Human B, AJG, Blue | **La frase central de Born ya está ocupada.** Diferenciarse por concreción, no por la frase |
| P5 | **Retainer mensual con mínimo** | Tech Packs Co ($1,500/mes, 3 meses), AJG y Blue (sin cifra) | El formato de Born es estándar; solo uno publica la cifra |
| P6 | **El sourcing como "red", no como entregable con precio** | todos los estudios | Hueco (ver §6) |
| P7 | **Productos digitales baratos** junto al servicio | Franky Dune, Blue, Tech Packs Co, Lefty, AJG | Muy repetido; en Franky Dune **domina la home** y diluye la agencia |
| P8 | **Prueba = testimonios + cifras autodeclaradas**; la verificación de terceros es rara | todos excepto Tulum | Las cifras incoherentes (AJG) restan credibilidad: el mismo riesgo que tiene Born (V4) |
| P9 | **Blogs de volumen** (200–670 posts) | Lefty, Human B, Blue | [H] SEO por volumen, poco profundo en decisiones concretas |
| P10 | **Nearshoring y aranceles** como argumento | Tulum, Apparel Production Inc | Tema vivo para marcas de EE. UU.; México tiene ventaja USMCA |

**Estándares mínimos (lo que se espera encontrar):** proceso numerado, testimonios con nombre, FAQ con objeciones, una CTA repetida, title y H1 propios por página, datos estructurados de negocio.

**Fricciones a evitar (observadas en el set):** copy caducado (Franky Dune), menús duplicados (Lefty), erratas (Human B), cifras que se contradicen (AJG), CTA hacia un servicio que no admite clientes (Nítido), superlativos inverificables (*"World's #1"*, Sewport) y urgencia falsa con precio tachado (Designjoy).

---

## 6. Necesidades insuficientemente atendidas y oportunidades

| # | Hueco observado | Evidencia | Oportunidad para Born | Tipo |
|---|---|---|---|---|
| G1 | **Nadie vende el emparejamiento con fábrica como producto con precio y entregable** | §2, P6 | Factory Match $750 / Sourcing & Comparison $1,500 con un **informe comparativo de ejemplo (anonimizado)**. Además es una primera compra de bajo riesgo para los leads de Upwork | Diferenciación de oferta |
| G2 | **"Production ready" nunca se define como meta medible** | §2 | Definir el final: *PPS aprobado, graduación validada, tech pack final; hasta 3 rondas por estilo*. Convierte "departamento de producción" (P4) en algo verificable | Diferenciación de discurso |
| G3 | **Casi nadie dice lo que no hace ni por qué eso protege al cliente** | Solo Tulum y Human B, parcialmente | *"We don't sew, buy your materials or own a factory, so we pick the right one, not ours"* (Es/No es del brandbook), frente a los híbridos | Diferenciación de discurso [H a validar] |
| G4 | **Profundidad en activewear/loungewear/golf/swim en estudios de EE. UU.** | Blue (UK) y Tulum (swim) lo tienen; los generalistas de EE. UU., no | Páginas por categoría: telas, fit, países recomendados, casos | SEO + relevancia |
| G5 | **La red multi-país rara vez se explica por producto** | Solo Tulum y APNY | "Por qué este país para esta prenda": seis países con criterio, sin nombrar fábricas | Prueba de criterio |
| G6 | **Ningún estudio con base en México y buen sitio en inglés** | §1 | Misma zona horaria que EE. UU., bilingüe, nearshoring USMCA (con datos verificados, sin prometer aranceles) | Posicionamiento geográfico [H] |
| G7 | **Ningún proceso muestra a la vez pasos + entregables + plazos + decisiones del cliente** | Cada uno muestra una parte | Mapa Sketched → Stitched → BORN con las cuatro capas: el **activo visual** de la web | UX diferencial |
| G8 | **Verificación de la prueba** | P8 | Reseñas enlazadas a Upwork, casos con resultado y cifras consistentes en todos los canales | Confianza |
| G9 | **Experiencia post-venta visible** | Solo Nítido menciona plataforma | Project Room como demostración de la experiencia de servicio | Diferenciación de servicio (fase posterior) |

**Amenazas:** (1) el ancla de precio de Upwork y Fiverr, si la web sigue vendiendo tech packs; (2) que la frase "production department" suene a lo mismo que dicen Human B y AJG; (3) que los marketplaces se vendan como anti-intermediario; (4) Lefty en la misma franja de precio para founders de activewear y swim; (5) el contenido de terceros en la web actual (01b §0), riesgo propio y no de mercado.

---

## 7. Referencias UX/UI y de conversión transferibles

| Patrón | Fuente | Cómo se traduce a Born | Qué no copiar |
|---|---|---|---|
| Página de **Process** en la navegación principal, con fases numeradas | LAYER (layerdesign.com/process) | Sketched / Stitched / BORN como macrofases, con subpasos numerados, entregables, plazos y precio | Fases abstractas sin entregables; CTA solo con mailto |
| **Relato de artefactos reales** (patrón, marcada, prueba, graduación) | Anderson & Sheppard, *The Bespoke Process* | Coherente con el lenguaje de patronaje del sistema visual; cada fase nombra su objeto | Muro de texto (40+ párrafos) |
| **Build sheet** por prenda (tabla de proceso, país, "last visited") | ASKET, página de producto | Ficha por caso: categoría, tela, región de fábrica, rondas de muestra, plazo | Márgenes o fábricas bajo NDA |
| **Plantilla fija de caso** con bloque de datos, filtros y "next project" | Pentagram /work | Casos filtrables por categoría (golf, swim…) con metadatos de fase | Casos solo en vídeo; créditos de equipos grandes |
| **Escalera de precios acumulativa** ("Everything in X, plus") | Maker's Row /pricing | Consulta → Factory pairing → Partnership por proyecto → Partnership de colección | Toggles de suscripción |
| **Formulario por etapa + presupuesto + volumen + imagen** | Lefty (intake), Tulum (7 preguntas, respuesta en 24 h) | Client Brief web: etapa, categoría, estilos, unidades por estilo, horizonte de lanzamiento, adjuntos | 15 campos de golpe: dividir en 2 pasos |
| **El mínimo dentro de la etiqueta** | Lefty ("most projects require a minimum 5k budget") | Indicar el rango de inversión junto al formulario | Página de rechazo |
| **Consulta de pago acreditable** | Lefty ($55), Franky Dune (€125), Human B ($245, "not a discovery call") | $200 acreditables en el primer proyecto [H a validar con María] | — |
| **Fundador como activo + lista de exclusiones** | Designjoy | *"You work directly with Maria"* + "What we don't do" | Descuentos tachados, urgencia falsa |
| **Prueba de terceros y anti-stock** | Tulum (*"No fabricated quotes. No stock photos"*) | Reseñas enlazadas a la fuente, fotos reales de fábricas y fittings | — |

---

## 8. Implicaciones para la futura web

1. **La frase no basta; la concreción diferencia.** "Your outsourced production department" se mantiene como titular de categoría (está aprobado en S9/S10), pero se respalda con lo que nadie define: dónde termina (PPS/production ready), cuántas rondas, en qué países y quién trabaja (María, 1:1). → afecta a D1 (03 §4).
2. **Publicar precios es una ventaja real**, compartida solo por 3 de 8. La escalera de Born es más completa que la de cualquiera (de $200 a $3,000/mes). → página Investment.
3. **El sourcing con precio es el hueco más claro del mercado**, y además es el mejor producto puente desde Upwork. → servicio con entregable visible.
4. **La independencia de la fábrica es el argumento frente a los híbridos y los marketplaces.** [H] Validar con María que es cierto en todos los casos (comisiones de fábricas, etc.) antes de usarlo.
5. **El proceso es el activo visual (G7).** El sistema de fases ya existe en la marca; ningún competidor lo muestra completo.
6. **Especialización por categoría (G4) y geografía (G6)** son las dos vías de SEO/GEO con menos competencia observada. No se aportan datos de volumen de búsqueda: requieren herramienta (Ahrefs, Search Console) en la fase 8.
7. **Los productos digitales no deben estar en la puerta.** Donde dominan la home (Franky Dune), diluyen la agencia. → refuerza D2.
8. **Coherencia de cifras = credibilidad.** AJG muestra el coste de la incoherencia; Born tiene el mismo riesgo abierto (V4/D5).

---

## 9. Fuentes (acceso: 5 nov 2026)

**Directos e híbridos**
- Human B: https://www.humanb.com/ · /services · /fashion-product-development · /faq · /fashion-business-consulting · /production-process
- AJG Fashion Consulting: https://ajgfashionconsulting.com/ · /launching-brands · /faqs · /contact · /clothingmanufacturers
- Tech Packs Co: https://www.techpacks.co/ · /tech-pack-services · /product-development-services · /why-us · /contact
- Franky Dune: https://www.frankydune.com/ · /services · /fashion-consulting · /11-fashion-production-call · /faqs · /about
- Nítido Agency: https://nitidoagency.com/ · /Services · /Project-Management · /Projects · /Contact-Us
- Blue Associates Sportswear: https://www.blueassociatessportswear.com/ · /pages/sportswear-services · /pages/how-long-does-it-take · /pages/golf-apparel-production · /pages/contact-us
- Tulum Fashions: https://tulumfashions.net/ · /development/
- Lefty Production Co: https://leftyproductionco.com/ · /consulting · /development · /contact · https://meetlefty.as.me/schedule.php

**Indirectos**
- Maker's Row: https://makersrow.com/ · /pricing
- Sewport: https://sewport.com/
- Techpacker / tpbuilder: https://techpacker.com/ · https://tpbuilder.ai/
- Upwork (403; snippets): https://www.upwork.com/hire/tech-pack-designers/
- Fiverr (403; snippets): https://www.fiverr.com/categories/graphics-design/fashion-design/technical-drawing

**Aspiracionales y de conversión**
- Anderson & Sheppard: https://www.anderson-sheppard.co.uk/house-style/the-bespoke-process/
- ASKET: https://www.asket.com/en-us/mens-wool-coat-dark-navy
- Pentagram: https://www.pentagram.com/work
- LAYER: https://layerdesign.com/process/
- Designjoy: https://www.designjoy.co/
- Metalab: https://www.metalab.com/contact

**Revisados y descartados:** apparelproductionny.com, mexmakers.net, epsilongs.com, glctextile.pt, appareify.com, nimble-made.com; sin acceso: indiesource.com (SSL), loomexgroup.com (406/503); factory45.co (vacío), sqetch.co (contenido ajeno).
