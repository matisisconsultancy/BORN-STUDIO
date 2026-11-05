# 01 — Strategic Project Audit

**Born Apparel Studio · Nuevo sitio web · Fase 1: auditoría documental**
Matisis Consultancy · 5 noviembre 2026 · Documento de trabajo, pendiente de validación con María

> Convención usada en todo el documento
> **[C] Confirmado**: está en un documento fuente (citado). **[I] Insight**: interpretación fundamentada. **[H] Hipótesis**: pendiente de validar. **[R] Recomendación**: decisión propuesta.

---

## 1. Diagnóstico ejecutivo

**Qué es.** Born Apparel Studio es un estudio de desarrollo de producto textil para marcas emergentes: convierte una idea o un tech pack en una prenda lista para producción y gestiona la relación con la fábrica del lado de la marca. No corta ni cose, no compra material por el cliente, no invierte capital. [C — Brandbook v1.0 §03; BORN_Brand_Rules.md]

**Cómo gana dinero.** Honorarios profesionales en dólares, separados de los costes de fábrica (que paga el cliente). Una escalera de servicios [C — Services Deck; Production Proposal]:

| Peldaño | Servicio | Precio publicado | Fase de marca |
|---|---|---|---|
| Entrada | 1:1 Production Consultancy con María | $200 / 60 min · $850 / 5 sesiones | — |
| Diseño | Collection Design | $200 / estilo (caso AS FOUND) | Sketched |
| Diseño | Technical Development (tech pack) | $250 / estilo (caso AS FOUND) | Sketched |
| Fábrica | Factory Match · Factory Sourcing & Comparison | $750 · $1,500 | Stitched |
| **Flagship** | Project Based Production Partnership (1–4 estilos, hasta 3 rondas por estilo) | $2,500 → $8,400 | Stitched → Born |
| **Flagship** | Collection Production Partnership (5–6 estilos) | $3,000/mes, mínimo 3 meses | Stitched → Born |
| Continuidad | Ongoing Production Support / Custom Scope | a medida | Born |

**A quién sirve.** Founder emergente con visión y capital inicial, sin red de fábricas ni criterio técnico [C — Brand Rules]. En la práctica: marcas de activewear, loungewear, golf y swimwear, mayoritariamente anglófonas [C — casos Party Wave, Skratch, ZOFAD, Twolip, LAYO, AS FOUND; Estrategia de Contenido §Upwork].

**Qué vende de verdad.** *Confianza*: el tech pack, la muestra y la supervisión son sus formas tangibles [C — Brandbook §04]. Formulado comercialmente: *"El cliente no compra un tech pack. Compra la certeza de que su primer producto va a existir, sin que el negocio se le rompa en el camino."* [C — Presentación Etapa 1, p. 4]

**Qué la diferencia.** Criterio técnico de piso de fábrica (María aprendió en producción en Portugal, España, Los Ángeles y Austria), aplicado con tres filtros —**viabilidad, costo, usabilidad**— y desde el lado de la marca en la relación con la fábrica. [C — Brand Rules; Production Proposal p. 3 y 9]

**Situación digital.** La web actual habla de otro negocio. Según la auditoría de octubre: identidad anterior, nicho streetwear, plantillas de $10–$100 y tech packs desde $150, y un "Book a call" que manda a Upwork. [C — Estrategia de Contenido p. 6, verificación en curso, ver 02] Hoy conviven **tres versiones de BORN**: la web (un servicio de tech packs), Upwork (un equipo de desarrollo, que es lo que más vende: $70K+, 5.0) y las propuestas (un departamento de producción, que es hacia donde va la marca). [C — Estrategia de Contenido p. 7]

**[I] La conclusión que ordena todo lo demás:** el reto de la web no es de estética, sino de **coherencia de oferta**. La identidad (Etapa 1) ya está resuelta y es sólida. Lo que falta decidir es qué negocio se presenta en la puerta: si la web no fija una sola oferta principal, el buen diseño servirá para comunicar con elegancia una contradicción.

---

## 2. Auditoría de documentación

### 2.1 Fuentes revisadas (acceso real, 5 nov 2026)

| # | Fuente | Ubicación | Qué aporta |
|---|---|---|---|
| S1 | Propuesta Matisis → Born: *Marca, Ecosistema Digital y Estrategia de Crecimiento* | Canva "Born Studio" (creado 7 abr 2026, 8 pp.) | **Alcance contractual de la web**, objetivos 2026, presupuesto |
| S2 | Propuesta Estratégica Rebranding Fase I (ES) / Strategic Brief (EN) | Dropbox `03-trabajo/documentos/born.docx` · `04-recibido/development/born_studio_strategic_brief_en.docx` | Esencia, propósito, visión, posicionamiento, storytelling, vocabulario; "8 preguntas estratégicas" |
| S3 | Brand Book v1.0 (web) + historial de versiones | Este repo: `index.html`, `tools/build_book.py`, git (v1 ES 13 jul → v2 EN 12 ago) | Decisiones finales: claim, tagline, Es/No es, voz, sistema por fases, journey, guardrails, logo |
| S4 | Tablero de exploración de logotipo | Este repo: `logos.html` | 53 rutas, la elegida (doble exposición) |
| S5 | BORN_Brand_Rules.md | Drive / Dropbox `03_tu_claude_documentos` | **Reglas vigentes**: nombre, origen, voz, color, prohibiciones |
| S6 | Presentación Etapa 1 (entrega 19 oct 2026) | Drive / Dropbox `00_empieza_aqui` | Qué se entregó, recorrido del cliente, "lo que sigue" |
| S7 | Estrategia de Contenido Instagram (oct 2026) | Drive / Dropbox `07_redes_sociales` | **Auditoría de IG, Upwork y web actual**; rol de cada canal; "una sola versión de la verdad" |
| S8 | Calendario editorial y de contenido (nov 2026 – abr 2027) | Drive / Dropbox | Temas mensuales que la web debería poder alojar |
| S9 | Services Deck · Services One-Pager | Drive / Dropbox `02_documentos_clientes` | Oferta, precios, pruebas, contacto |
| S10 | Production Partnership Proposal (18 pp.) | Drive / Dropbox | Detalle de servicio flagship, FAQ, riesgos, casos |
| S11 | Design Proposal AS FOUND (sept 2026) | Drive / Dropbox | Precios de diseño/tech pack, tono real de María con clientes |
| S12 | Templates + RULES.md (12 documentos) | Drive / Dropbox | Sistema documental; muestra cómo se habla en cada fase |
| S13 | Project Room (LAYO demo en repo; Cielo Essie en Drive) + feedback de María | Repo `deliverables/`; Dropbox `04-recibido/feedback/project-room` | Experiencia de cliente post-venta; requisitos de María |
| S14 | Deck LAYO Capsule Design Stage | Repo `source/` | Trabajo real de diseño (flats, renders, fotos de muestra) |
| S15 | Instrucciones de rediseño de plantillas (María) | Dropbox `04-recibido/feedback/re-design` | Prioridades y lenguaje de la clienta |

**Sin acceso o no encontrado** (no se asume su contenido):
- **Gmail**: el conector no tiene el permiso necesario; no se revisaron correos ni conversaciones con María.
- **Contrato/aceptación firmada** de la propuesta S1: la carpeta `01-contratos` de Dropbox está vacía.
- **Briefing inicial de María** (las "ocho preguntas" que S2 responde): solo existe indirectamente, a través de las respuestas.
- **Analítica** de la web actual (GA, Shopify Analytics, Search Console): no disponible.
- **Perfil de Upwork**: solo a través de las cifras de S7 (revisado con sesión iniciada el 18 oct 2026).

### 2.2 Decisiones confirmadas (no se reabren)

| Decisión | Fuente | Nota para la web |
|---|---|---|
| Nombre en texto: **Born Apparel Studio**; logo: wordmark BORN | S5 | El brandbook y este repo todavía dicen "BORN Studio" (ver vacío V1) |
| Categoría: **Full Service Apparel Development Studio** | S3, S5 | |
| Master claim **Sketched. Stitched. BORN.** · Tagline **From idea to life** | S3, S5, S6 | Sustituye al tagline recomendado en S2 ("Donde nacen las colecciones") |
| Anclas de fase: *Sketched / Stitched / Made to be BORN · Born to be made* | S5, S6 | Base natural para la arquitectura narrativa |
| Origen: **la fábrica primero**; teatro y ópera, un plus | S5, S7 p. 15 | Revierte S2, que ponía el teatro como eje |
| Arquetipo Creator + Caregiver; voz directa, cálida, editorial, precisa, con criterio | S3, S5 | |
| Identidad visual: doble exposición, paper/ink/grafitos, **el rojo se gana**, Didot/Bodoni/Jost/Space Mono | S3, S5, S6 | Ya está el sistema web (tokens en `tools/src/root.css`) |
| Idioma de la marca: **inglés**, sin emojis, CTA única | S5, S7 p. 14 | Choca con "dos idiomas" del alcance S1 (ver D3) |
| Recorrido comercial: Upwork / Instagram → **Consulta 1:1** → Client Brief → Proposal → Kickoff | S7 p. 9 | La web es "el destino de cada enlace" y su KPI son consultas agendadas y briefs |
| Precios estándar (escalera) | S9, S10 | |
| Pruebas utilizables: 10+ años, 15+ founders, 6 relaciones de fábrica en 6 países; casos Party Wave ($40K en ventas), Skratch (2 muestras a PPS), ZOFAD, Twolip; Upwork 5.0 / $70K+ / 63 reseñas | S9, S10, S7 | Se usan **solo** tras confirmar las cifras (ver V4) y los permisos de los clientes |

### 2.3 Vacíos e inconsistencias detectados

| # | Hallazgo | Evidencia | Por qué importa para la web |
|---|---|---|---|
| V1 | **Tres nombres en circulación**: "BORN Studio" (brief, brandbook, repo, Project Room demo, `hello@bornstudio.co`), "Born Apparel Studio" (reglas, documentos, dominio) y "Born · Fashion Product Development" (web actual) | S2, S3, S5, S7, `tools/room_data.py` | La claridad de entidad es la base del SEO/GEO. Hay que corregir el brandbook y la demo |
| V2 | **Tres definiciones de la oferta**: (a) viaje completo de idea a bulk, en 3 fases (brandbook); (b) *"From finished tech packs to production ready garments"*, departamento de producción externo (Services/Proposal); (c) diseño + tech pack por estilo (AS FOUND) | S3, S9–S11 | Decide el titular, el sitemap y la conversión principal |
| V3 | **"No es un estudio de diseño creativo"** (brandbook), pero vende *Collection Design — "We create the product vision"* | S3 §03 vs S9 p. 6 | Hay que redactar el límite con precisión: diseño al servicio de la manufactura, no dirección estética |
| V4 | **Cifras que no coinciden**: años (9+/10+/12+), fundación (2018/2022), fábricas (6 vs 50+), consulta ($60/30, $120/60, $200/60), equipo (Olivia y Yordanka vs Andrea y Giorgia) | S7 p. 15 (listado ya abierto con María) | Una web que se contradice con Upwork destruye la confianza que pretende construir. Bloquea la redacción |
| V5 | **Cuatro modelos de proceso**: 3 fases con plazos (brandbook), 5 fases (brief: conversación → producción), 5 servicios-ecosistema, 5 etapas dentro de la Partnership; plazos de 2–6 meses vs "3 a 5 meses" | S2, S3, S9, S10 | La web necesita **un** mapa de proceso canónico (S2 §25: "dibujarlo, no prometerlo") |
| V6 | **El alcance S1 apunta a "fundadores de marcas de streetwear"** (lead magnet, contenido), mientras que la estrategia posterior concluye que el streetwear es el nicho de la web antigua y que la marca va hacia activewear/loungewear | S1 vs S7 p. 6–7 | Ajuste del alcance aprobado: debe validarse explícitamente |
| V7 | **"Ecosistema de productos digitales" como motor de ingresos** (S1) frente a *"Más tienda que estudio: plantillas de $10–$100 compiten con el servicio completo"* (S7) | S1 vs S7 p. 6 | Es la decisión de arquitectura más grande: ¿tienda dentro, aparte o fuera? |
| V8 | **Visión "Iberoamérica" en español** (S2) frente a un mercado real en EE. UU. y en inglés (S5, S7, precios en USD) | S2 §04 vs S5 | Afecta al idioma, al SEO y a la geografía de las búsquedas |
| V9 | **La web no aparece en "Lo que sigue"** de la entrega de la Etapa 1 (sí aparecen Claude, redes e imprenta) | S6 p. 20 | Calendario y orden de fases sin documentar |
| V10 | **Project Room demo con datos ilustrativos** (EUR, IBAN/IVA de relleno, proveedores y POMs no sacados del deck) | `tools/room_data.py`; README | No puede usarse como caso público. Sí como demostración de la experiencia de servicio, si María lo aprueba |
| V11 | **Sin permisos documentados** para mostrar clientes, logos, fotos o cifras de terceros (Party Wave, Skratch, LAYO…) | — | Los casos son el contenido de mayor rendimiento (S7 p. 3); sin permiso no hay casos |

---

## 3. Propuesta y alcance

### 3.1 Lo que dice la propuesta S1 (texto literal resumido)

**Objetivos 2026**
1. Construir una identidad independiente de la reputación personal de María, para escalar, cobrar precios premium y ser reconocido "antes de que se lea una sola palabra".
2. Diferenciarse en un mercado que se comoditiza (tech packs, sourcing y consultoría en plataformas freelance y agencias offshore), con un posicionamiento que vuelva irrelevante la competencia por precio.
3. Construir un sistema de conversión más allá de Upwork y Calendly: captación de emails, nurturing y recorrido post-compra.
4. Activar la autoridad de contenido de María (nueve años de conocimiento) como motor de distribución propio.

**Workstream Web** (precio de alianza del paquete completo, Branding + Web + RSS: **2,200 USD**, 50/50; lista 2,700 USD)
- Rediseño web UX/UI orientado a conversión, **construido sobre la infraestructura de Shopify existente**; arquitectura que refleje el **modelo híbrido (servicios + educación + autoridad)**, con flujos claros para cada tipo de cliente y páginas de servicio optimizadas.
- Lead magnet (guía o checklist) más una secuencia de bienvenida/nurturing de 4–5 emails, "a definir según la conveniencia para el proyecto".
- Estudio e implementación de palabras clave para SEO.
- **Dos idiomas incluidos.**
- **No incluye:** hosting, fotografía de producto, dominio, publicidad ni mantenimiento web pasados 6 meses.
- Del workstream de Contenido: estrategia del ecosistema de productos digitales (bundles, precios, copy SEO de producto).

### 3.2 Lectura crítica

| Tema | Compromiso | Restricción / riesgo | [I]/[R] |
|---|---|---|---|
| Plataforma | Shopify existente | Shopify es fuerte en tienda y débil como CMS editorial (casos, método, blog multi-idioma). No se ha verificado ni el plan ni el tema actual | [R] Validar Shopify como restricción **contractual** o como suposición; en 09 se comparan alternativas sin salir del alcance |
| Modelo híbrido | servicios + educación + autoridad | Si "educación" significa una tienda de plantillas baratas en la home, choca con V7 | [R] Separar jerárquicamente: el servicio en la puerta, la educación como prueba de criterio, los productos como canal secundario |
| Dos idiomas | incluido | La marca decidió solo inglés; el español tiene sentido si se quiere captar LatAm/España | [H] Inglés principal + español como segundo idioma completo es viable; validar si es necesario |
| Lead magnet + nurturing | a definir | Requiere herramienta de email (Shopify Email / Klaviyo) no presupuestada | [R] Definir un único lead magnet ligado al primer tema editorial (tech pack) y no al streetwear |
| SEO | estudio + implementación de keywords | No incluye producción continua de contenido | [I] El impacto SEO dependerá del calendario editorial (S8), no del lanzamiento |
| Fotografía | excluida | La marca exige retrato de María y oficio real (S2 §21: 40/40/20) | **Riesgo alto**: sin material propio la web cae en stock, que es justo lo que la auditoría critica |
| Precio | 2,200 USD paquete completo, con la Etapa 1 ya entregada (de alcance amplio) | El esfuerzo invertido en la Etapa 1 supera con creces una lectura literal de la propuesta | [R] Proteger el alcance de la web: lo que no esté en 3.1 se clasifica como opcional (ver 10) |
| Estado de aprobación | — | No hay firma localizada; la propuesta caducaba a los 30 días | [H] Se presume aceptada porque la Etapa 1 se ejecutó; confirmar por escrito |

### 3.3 Oportunidades que el alcance permite sin ampliarlo
- Reutilizar el sistema visual ya construido (tokens, wordmark por fase, cinta métrica, motion) como lenguaje de la web: el coste de diseño es bajo y la coherencia, alta.
- Convertir el **Client Brief** (ya diseñado como plantilla) en el formulario de cualificación de la web: es el siguiente paso documentado tras la consulta.
- Reutilizar los textos aprobados de la Production Proposal (FAQ, riesgos, "two paths"), que ya están escritos en la voz de marca.

---

## 4. Respuesta a las 10 preguntas del diagnóstico

| # | Pregunta | Respuesta | Tipo |
|---|---|---|---|
| 1 | ¿Qué es? | Estudio de desarrollo de producto textil que actúa como departamento de producción externo de marcas emergentes | C |
| 2 | ¿Modelo de negocio? | Honorarios por servicio en una escalera de valor creciente; flagship de $2,500 por estilo o $3,000/mes; los costes de terceros, aparte | C |
| 3 | ¿Servicios? | Consultoría 1:1, diseño de colección, tech pack, factory pairing, production partnership (proyecto/colección), soporte continuo | C |
| 4 | ¿Públicos? | Founder primerizo con capital y sin red de fábricas (principal); equipos con experiencia que solo necesitan fábrica (Path 01); marcas establecidas que buscan socio para una cápsula (S2, sin evidencia en casos actuales) | C / H |
| 5 | ¿Posicionamiento? | Del lado de la marca frente a la fábrica, con criterio de piso de producción y tres filtros | C |
| 6 | ¿Atributos y valores? | Riguroso, sensible, hecho a mano, editorial, pragmático, premium sin distancia; valores: criterio, honestidad técnica, método, cuidado, cercanía, viabilidad | C (S2) |
| 7 | ¿Qué la diferencia hoy? | Origen en la fábrica, relación 1:1 senior y reputación verificable en Upwork. La identidad nueva aún no está en el mercado | C / I |
| 8 | ¿Qué debe resolver la web? | Ser el destino propio de Upwork e IG; probar criterio antes del contacto; cualificar y convertir en consulta y brief; sacar a la marca de la dependencia de Upwork | C (S1, S7) |
| 9 | ¿Objetivos y límites del alcance? | Ver 3.1–3.2: Shopify, dos idiomas, lead magnet, SEO; sin fotografía ni mantenimiento | C |
| 10 | ¿Qué está confirmado y qué abierto? | Confirmado: tabla 2.2. Abierto: V1–V11 y decisiones D1–D8 (ver 03 §4) | — |
