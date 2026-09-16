---
tema: Diagramas
fuente: "— (Índice de las láminas generadas para las entregas)"
fecha: 2026-09-15
---

# 02-Diagramas — dónde está cada lámina

**Cada carpeta lleva el número de la sección de `Entrega - Caso 1 FarmaHosp.md` que la usa.**
Si sabés qué sección estás escribiendo, ya sabés en qué carpeta buscar — no hace falta recordar
cómo se llama el archivo.

| Carpeta | Sección de la Entrega | Criterio de la rúbrica | Qué hay |
|---|---|---|---|
| `2-caso-negocio/` | §2 | 1 — caso de negocio (25 pts) | Contexto (`.mdj` de StarUML), core y primera descomposición |
| `3.1-drivers-rf/` | §3.1 | 3 — drivers RF | El CDU expandido de prescripción |
| `3.2-drivers-calidad/` | §3.2 | 3 — atributos de calidad | Resumen de los 8 `AC-nn` + una ficha por driver |
| `3.3-drivers-restriccion/` | §3.3 | 3 — restricciones | Las 8 explícitas y las 10 implícitas |
| `3.4-priorizacion/` | §3.4 | 3 — los 5 más críticos | La matriz de dos ejes y el top 5 |
| `4-matrices-trazabilidad/` | §4 | 4 — trazabilidad (20 pts) | Las tres matrices (la 2 en dos vistas) |
| `ejemplos-clase/` | — | — | Los casos que resolvió la catedrática y las demostraciones en otro dominio |
| `herramientas/` | — | — | Evidencia sobre las herramientas (la marca de agua de StarUML) |
| `practica/` | — | — | **Lo que dibuja Julián a mano.** Tiene su propio README y su convención de versiones |
| `practica/referencia/` | — | — | Copia de los 23 `.svg` generados, **con las mismas carpetas por sección**, para dibujar al lado y comparar |
| `examen/` | — | — | **Misma estructura que `practica/`, para el día del parcial.** Carpetas de trabajo por sección ya creadas + su `referencia/`. Su README tiene la regla de alcance, el orden por puntaje y el chequeo de 30 segundos |

## Qué son los tres archivos de cada lámina

| Extensión | Para qué |
|---|---|
| `.excalidraw` | El editable. Se abre en excalidraw.com o en el plugin de Obsidian |
| `.svg` | **El que se entrega.** Vectorial, sin marca de agua, escala sin pixelarse |
| `-verificacion.png` | La captura del paso 4 del checklist de `estilo-diagramas.md`: la prueba de que la lámina se miró, no solo se generó |

## Cómo se regeneran

Todo sale de `06-Proyecto-MCP/generar-excalidraw.py`, que es **determinista** — mismas coordenadas,
mismos bytes, en cualquier máquina. Acepta el nombre de una lámina o el de una carpeta entera:

```bash
cd boveda/06-Proyecto-MCP
python3 generar-excalidraw.py 4-matrices-trazabilidad   # el lote entero
python3 generar-excalidraw.py matriz-3-cdu-rf           # una sola
python3 generar-excalidraw.py                           # lista lo disponible
python3 generar-excalidraw.py --referencia              # refresca practica/ y examen/
python3 generar-excalidraw.py --referencia examen      # solo una de las dos
```

Cuando regeneres cualquier lámina, corré también `--referencia`: las copias de `practica/` y
`examen/` no se actualizan solas.

El diagrama de contexto es la excepción: se emite con `generar-mdj.py contexto-farmahosp`, porque
StarUML valida la semántica UML que el `.excalidraw` no puede validar.

## Lo que hay que saber antes de tocar esto

- **No todo lo de acá es un diagrama.** Los drivers de calidad, las restricciones, la priorización
  y las matrices **son tablas**: se tabulan, no se dibujan. Un atributo de calidad **no es un caso
  de uso** — dibujarlo como tal invalida el artefacto.
- **Los datos viven en el generador**, copiados de la Entrega. Si corregís una celda en la Entrega,
  cambiás la constante correspondiente en `generar-excalidraw.py` y regenerás. La Entrega manda.
- **Nada se da por terminado sin mirar la imagen** (`estilo-diagramas.md` §7, paso 4). Un diagrama
  con el código perfecto puede verse mal.
