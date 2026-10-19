# Born Apparel Studio — Brand Book

Edición final · octubre 2026 · https://matisisconsultancy.github.io/BORN-STUDIO/

La guía definitiva de la marca de **Born Apparel Studio**, un *Full Service Apparel
Development Studio*. El logo es el wordmark **BORN** (BORN Studio); en texto corrido
el nombre siempre es Born Apparel Studio.

> **Sketched. Stitched. BORN.** — *From idea to life.*

## Qué hay aquí

| Pestaña | Contenido |
|---|---|
| Brand | Datos de marca, origen, posicionamiento, propuesta de valor (Strategic Process and Design), atributos visuales, arquitectura verbal, voz |
| Logo | Lockup principal, concepto, firmas animadas, marca por etapa (Sketched · Stitched · BORN), isotipo, negativos, variantes, usos incorrectos |
| Color | Paper, grafitos, Ink y Rojo Valentino `#C4122E` (Pantone 3546 C). El rojo se gana |
| Typography | Bodoni Moda (voz), Jost (lectura), Space Mono (dato técnico), GFS Didot (solo el wordmark) |
| Applications | La identidad por fase del servicio y el recorrido del cliente |
| Downloads | Kit de marca completo, logos en SVG, tipografías y cada logo o animación por separado |

**Lo que no está aquí:** plantillas, manuales y entregables de clientes. Son archivos
de trabajo y viven en el Drive del estudio.

## Archivos

- `index.html` — página autónoma (fuentes, CSS, JS y logos embebidos).
- `downloads/` — kit público: `BORN-Brand-Kit.zip`, `BORN-Logos-SVG.zip`, `BORN-Fonts.zip`.
- `assets/logos/` — PNG de alta resolución y animaciones MP4/WebM.
- `tools/src/` — SVG fuente de cada logo, tokens de color y fuentes.

## Regenerar

```bash
python3 tools/build_downloads.py <ruta a 01_Marca de la entrega>   # downloads/
python3 tools/build_book.py                                          # index.html
```

Los logos son definitivos. El pipeline que los derivó del tablero de exploración
(`logos.html`, `tools/extract_logos.py` y siguientes) quedó en el historial de git.

### Licencias
- Tipografías bajo SIL Open Font License. **GFS Didot** es el revival libre de Didot;
  si se dispone del Didot licenciado, se sustituye 1:1.
- Para impresión, usar Pantone 3546 C directo.

---

Estrategia y marca — **Matisis Consultancy** · para María Batres, fundadora de Born Apparel Studio.
