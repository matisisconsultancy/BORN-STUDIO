# 01b — Auditoría de la web actual (bornapparelstudio.com)

**Anexo de [01](01_auditoria_estrategica.md) · base para el entregable 09 (Technical Audit & Migration)**
Observación directa el 5 nov 2026: curl, DNS sobre HTTPS, parseo de 22 páginas, medición con Chromium/Playwright y búsqueda web. No incluye analítica ni Search Console (sin acceso).

---

## 0. Hallazgo crítico: contenido de otra empresa publicado como propio

Tres páginas indexadas contienen texto de **Spec to Sample**, una agencia australiana. Verificado dos veces el 5 nov 2026:

| URL | Texto observado (extracto literal) |
|---|---|
| `/pages/faq` | *"We are located in Moorabbin, Victoria 3189, Australia."* · *"…even though Spec to Sample represents your brand…"* · *"we charge AUD $150-$180+GST per hour"* |
| `/pages/supply-chain` | *"Spec to Sample has visited all facilities…"* · *"Dani, the Director, has worked closely with this supplier for over six years."* · *"In the Australian market, they currently work with over 43 of our clients."* |
| `/pages/design-services` | *"Spec to Sample offers Hang Tag, Care Label, and Packaging design services…"* · *"Technical Packs are from AUD $350+gst"* |

**Implicaciones:** (1) riesgo legal y reputacional por copia de contenido y por atribuirse oficinas, clientes y años de un tercero; (2) un founder que llegue a la FAQ lee que el estudio está en Australia y cobra en AUD; (3) contenido duplicado a efectos SEO. Estas páginas no están en el menú, pero sí en el sitemap.
**[R] Prioridad inmediata, independiente del rediseño:** despublicar o reescribir esas tres páginas ya, y avisar a María. Es una acción de 15 minutos en Shopify y no requiere esperar a la web nueva.

---

## 1. Infraestructura

| Elemento | Estado observado |
|---|---|
| Plataforma | **Shopify** (cabecera `powered-by: Shopify`; tienda `bornapparelstudio.myshopify.com`) |
| Tema | "Header Copy of Dawn" (Dawn 15.2.0), con un `custom-script.js` propio |
| Dominio canónico | `https://bornapparelstudio.com` (http y www redirigen con 301) |
| DNS | NS en Google Cloud DNS; A → 23.227.38.65 (Shopify); `www` CNAME → `shops.myshopify.com` |
| Email | Google Workspace (MX `smtp.google.com`, SPF Google). **No tocar MX/SPF en la migración** |
| Registro / WHOIS | No verificado (sin herramienta) |
| Tienda | Guadalajara, Jalisco, MX · USD · 31 productos · 4 colecciones · RFC mexicano en la información de contacto |
| Idiomas | Solo `en`; sin hreflang |
| Analítica | Solo los píxeles nativos de Shopify. **No hay GA4, GTM, Meta pixel ni Klaviyo**. No hay base de medición previa |
| Librerías | jQuery 3.6.4, OwlCarousel 2.3.4, AOS 2.3.1 (CDN) |
| Reserva | Calendly (`calendly.com/bornstudio`, `/discovery-meeting`); un enlace a un servicio de consulta en Upwork |

## 2. Inventario de URLs (base del mapa de redirecciones)

- **Páginas (13):** contact, faq, our-portfolio, design-services, supply-chain, our-team, production-consultancy, sample-control, production-management, factory-sourcing, tech-packs, sketches-mock-ups, data-sharing-opt-out
- **Colecciones (4 + all):** frontpage ("How to guides"), tools-templates, streetwear-mock-ups-library, custom-services, all
- **Productos (31):** 3 tech packs a medida ($150 / $200 / $250), sketches a medida ($180), consulta 1:1 ($120 / 60 min), starter kit ($100), 5 plantillas ($10–$15), 9 guías de medición ($10) y 11 bundles de sketches ($25)
- **Blog:** `/blogs/news`, **0 artículos**
- **Políticas:** privacy, terms, refund, contact-information (`shipping-policy` → 404)
- Varios *handles* de producto no coinciden con su título (p. ej. `ladies-plus-size-chart-and-grade` es la plantilla BOM): hay que revisarlos uno a uno al mapear los 301

<details><summary>Inventario completo (sitemap + URLs vivas fuera del sitemap)</summary>

```
/
/pages/contact  /pages/faq  /pages/our-portfolio  /pages/design-services  /pages/supply-chain
/pages/our-team  /pages/production-consultancy  /pages/sample-control  /pages/production-management
/pages/factory-sourcing  /pages/tech-packs  /pages/sketches-mock-ups  /pages/data-sharing-opt-out
/pages/our-portfolio-1 (ya redirige a /pages/our-portfolio)
/collections/frontpage  /collections/tools-templates  /collections/streetwear-mock-ups-library
/collections/custom-services  /collections/all
/blogs/news
/products/croqui-fashion-drawing-template-ladies-standard-curvy   /products/cost-sheet-template
/products/size-chart-expansion-ladies-plus   /products/ladies-plus-size-chart-and-grade
/products/techpacktemplatebonus   /products/selling-mock-ups
/products/measurement-sample-control-sheet-template-xlsx   /products/bornstudio_po_template-xlsx
/products/t-shirt   /products/activewear-bottoms-sketches-bundle   /products/hoodies-sketches-bundle
/products/hats-sketches-bundle   /products/fleece-pants-sketches-bundle   /products/woven-pants-sketches-bundle
/products/woven-shirts-sketches-bundle   /products/shorts-sketches-bundle   /products/vests-sketches-bundle
/products/knit-tops-sweaters-measurement-guidelines   /products/woven-shirts-measurement-guidelines
/products/bottoms-pants-shorts-etc-measurement-guidelines   /products/jackets-sportcoats-measurement-guidelines
/products/vests-how-to-measure-guide   /products/outerwear-how-to-measure-guide
/products/underwear-how-to-measure-guide   /products/socks-how-to-measure-guide
/products/robes-how-to-measure-guide
/products/custom-basic-tech-pack   /products/custom-standard-tech-pack
/products/custom-streetwear-tech-pack-advanced   /products/custom-sketches-mock-ups
/products/1-1-fashion-production-consultancy-call
/policies/privacy-policy  /policies/terms-of-service  /policies/refund-policy  /policies/contact-information
/agents.md
```
</details>

Se trasladará a la matriz de redirecciones del entregable 09.

## 3. Contenido y mensaje

| Aspecto | Observado | Brecha frente a la estrategia |
|---|---|---|
| H1 de la home | *"Welcome to Born Studio® Develop your Streetwear Brand effortlessly"* | Nicho y nombre equivocados (V1, V6) |
| Meta description | *"Streetwear & Loungewear Development from scratch to release \| Tech Pack Experts"* | Posiciona como freelance de tech packs |
| Logo | "Born · Fashion Product Development" en sans (también og:image de todas las páginas) | Identidad anterior |
| Origen (`/our-team`) | Abre con una cita de Michael Jordan; el relato empieza en el teatro y la ópera (2014); fundación en 2022 | Revierte la decisión "la fábrica primero" |
| Equipo | Maria, Olivia y Yordanka | Las propuestas dicen PM + 2 diseñadores (Andrea y Giorgia) (V4) |
| Años | "9+" en 8 páginas y "over 10 years" en una | (V4) |
| Oferta | Retainers de $750 / $1,400 / $2,220 al mes (sample control, production management) que no figuran en ningún documento nuevo | Una cuarta lista de precios (V4) |
| Prueba | Testimonios (dos marcados como "Upwork review"); logos Wckdthghts, HeadingPrints, Proper, Rebalance | Hay prueba, pero sin casos con resultado |
| CTA | "BOOK A CALL" a Calendly (gratuito); un enlace roto en la home; seis "BOOK YOUR SERVICE HERE" que apuntan a `#` | CTA dispersa y fricción por enlaces muertos |
| Contacto | Formulario por defecto de Shopify (4 campos) | Sin cualificación |

## 4. SEO técnico observable

- Las páginas `/pages/*` y las colecciones **no tienen meta description**; título genérico con el patrón "X – Bornapparelstudio".
- Las páginas de servicio **no tienen H1**; `/our-team` y `/our-portfolio` tienen varios.
- JSON-LD: `Organization` y `WebSite` en la home, `Product` en productos. No hay `ProfessionalService`, `Person`, `FAQPage` ni `Review`.
- og:image es el logo antiguo en todas las páginas.
- **136 de 161 imágenes sin alt**; dos `.heic` (no se muestran en la mayoría de navegadores).
- Enlaces internos con el dominio `myshopify.com` escrito a mano.
- Un portfolio antiguo de Adobe sigue apareciendo en buscadores y devuelve 404.

## 5. Rendimiento (laboratorio, 1 medición, solo home; no son datos de campo)

| Métrica | Móvil (emulado, sin throttling) | Escritorio |
|---|---|---|
| LCP | 3.67 s | 2.69 s |
| Load | 6.9 s | 3.1 s |
| Peticiones | 171 | 168 |
| Peso transferido | ~17.8 MB | ~17.9 MB |

El peso se explica sobre todo por **un vídeo `.mov` de 165.6 MB** incrustado en la home (más uno de 2.5 MB). Con throttling móvil real, los valores serían peores. Margen de mejora claro y medible.

## 6. Canales enlazados

- **Linktree** `bornapparelstudio`: "BOOK A FREE CALL" (Calendly), Upwork, portfolio y un canal de YouTube `@BornApparelStudio` (DIY tutorials). El canal de YouTube no aparece en ningún otro documento.
- Pie de la web: Instagram `_bornstudio`, Facebook, Pinterest.
- Instagram no se pudo verificar (muro de inicio de sesión).

## 7. Riesgos para la migración (adelanto de 09)

1. **Checkout de productos digitales**: cualquier cambio de plataforma o de estructura debe preservar las descargas ya compradas (sin app de descargas visible, probablemente funciona con el sistema nativo de Shopify; sin verificar).
2. **~50 URLs indexables** que necesitan 301 a destinos equivalentes (servicios → servicios, guías → recursos).
3. **DNS mixto**: web en Shopify y correo en Google Workspace. Solo se cambian A/CNAME, nunca MX/TXT.
4. **Sin línea base analítica**: hay que instalar GA4 (o equivalente) y Search Console **antes** del rediseño para tener un antes y un después.
5. **Contenido de terceros**: no puede migrarse nada de las tres páginas de la sección 0.
6. **Precio de consulta**: hoy $120 en Shopify, $200 en las propuestas y gratuita en Calendly ("free call"). La web nueva no puede salir sin decidir esto (D5, D9).
