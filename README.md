# BORN Studio — Identidad de marca

Sitio estático de identidad de marca para **BORN Studio**, un *Full Service
Apparel Development Studio*. Primera traducción visual del brief estratégico
cerrado por Matisis Consultancy (Julio 2026).

> **Sketched. Stitched. BORN.** — *From idea to life.*

## Principio de diseño

El encargo pedía una página **visualmente tan impactante que el logotipo se
vuelva un factor secundario**. La marca la carga el sistema, no el logo: el
master claim funciona como héroe tipográfico y la palabra **BORN** se repite
como elemento gráfico central en cada sección.

La dirección visual es una mezcla de las rutas *editorial-de-moda* y *casa de
moda emergente* del brief. Se evitan deliberadamente las dos anti-referencias:
la estética fría de agencia de branding (grid mínimo, sans fría, mucho blanco)
y la estética literal de fábrica textil (azules corporativos, retículas
industriales).

## Sistema visual

| Elemento | Decisión |
|---|---|
| **Tipografía display / cuerpo** | Fraunces (serif variable, editorial y cálida, *con criterio*) |
| **Tipografía técnica** | IBM Plex Mono — labels, specs y registro *tech-pack* |
| **Paleta** | Papel/hueso cálido, tinta cálida casi negra, un solo acento fuerte: el **rojo hilo** (`#D1442A`) |
| **Motivo** | Pespunte (*running stitch*) — línea punteada roja que subraya BORN y marca el progreso de scroll |
| **Ritmo** | Secciones en papel alternadas con secciones invertidas (journey y sello) para dar cadencia de revista |

Todos los atributos del brief se leen al primer vistazo: **editorial**,
**artesanal sin ser rústico**, **bilingüe con precisión** (inglés para los
artefactos de marca, español para la prosa), **con temperatura** y **con
criterio**.

## Contenido

La página recorre la arquitectura de marca del brief:

1. **Hero** — master claim + promesa
2. **La esencia** — el insight fundacional (estudio de fábrica que hace diseño)
3. **El oficio en tres tiempos** — Sketched · Stitched · BORN
4. **Los tres filtros** — viabilidad técnica · optimización de costos · usabilidad real
5. **El journey** — Fase 01 / 02 / 03, modular, estilo tech-pack
6. **Quién habla** — arquetipo Creator + Caregiver y atributos de tono
7. **El sello** — sistema léxico (*…to be BORN*)

## Estructura

```
.
├── index.html          # Página completa (una sola vista)
├── css/styles.css      # Sistema visual y tokens de diseño
├── js/main.js          # Reveal on scroll, hero y progreso (sin dependencias)
└── assets/favicon.svg
```

## Desarrollo

Es un sitio estático puro. Cualquier servidor de archivos sirve:

```bash
python3 -m http.server 8000
# → http://localhost:8000
```

Las fuentes se cargan desde Google Fonts con una pila de fallback serif/mono,
de modo que el layout se sostiene aunque la red falle.

---

Estrategia y marca — **Matisis Consultancy** · para María, fundadora de BORN Studio.
