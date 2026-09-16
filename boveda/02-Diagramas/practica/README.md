---
tema: Diagramas
fuente: "— (Diagramas dibujados a mano para practicar)"
fecha: 2026-09-15
---

# Práctica — diagramas hechos a mano

Acá van **los diagramas que dibuja Julián** (Excalidraw, StarUML, foto de papel — lo que sea),
separados de los generados, que viven en `02-Diagramas/`.

**Convención de nombre:** `<caso>-<tipo>-v<numero>.<ext>`

```
farmahosp-contexto-v1.excalidraw
farmahosp-contexto-v1.png          (la exportación o foto para revisar)
farmahosp-cdu-core-v1.svg
```

Las versiones no se pisan: si la revisión encuentra algo, la corrección es `-v2`.
Así queda visible el progreso — y sirve para repasar los errores antes del examen.

**Flujo:** dibujar → guardar acá → pedir revisión contra la checklist → recién después
comparar contra la referencia de la Entrega.

---

## `referencia/` — las láminas generadas, para comparar sin salir de la carpeta

Adentro de esta carpeta hay una subcarpeta `referencia/` con **una copia de los 23 `.svg`
generados**, ordenada **con las mismas carpetas por sección** que `02-Diagramas/`:

```
referencia/
├── 2-caso-negocio/            core y primera descomposición
├── 3.1-drivers-rf/            el CDU expandido
├── 3.2-drivers-calidad/       resumen + las 8 fichas
├── 3.3-drivers-restriccion/   explícitas e implícitas
├── 3.4-priorizacion/          dos ejes y top 5
├── 4-matrices-trazabilidad/   las tres matrices
└── ejemplos-clase/            los casos de la catedrática
```

Está acá para poder dibujar tu versión al lado y compararla de una, sin salir de `practica/`.

> [!warning] Son **copias**, no los originales
> El original de cada lámina vive en su carpeta de sección (`3.2-drivers-calidad/`,
> `4-matrices-trazabilidad/`, …) y **se genera desde `06-Proyecto-MCP/generar-excalidraw.py`**.
> Si editás algo acá, se pierde al refrescar. Corregí el generador, no la copia.

Refrescar la copia después de regenerar cualquier lámina:

```bash
cd boveda/06-Proyecto-MCP
python3 generar-excalidraw.py --referencia
```

Borra y rehace `referencia/` entera desde los originales, así que nunca queda a medias.

> [!tip] El orden importa para que la práctica sirva
> **Dibujá primero, mirá la referencia después.** Si abrís `referencia/` antes de intentarlo, no
> estás practicando: estás copiando, y el examen no te va a dejar la carpeta abierta.
