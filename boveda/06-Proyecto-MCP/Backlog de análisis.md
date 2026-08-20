---
tema: Proyecto MCP
fuente: "Análisis de Fable 5 sobre el MCP y la bóveda — sondas reales por stdio + verificación contra capturas. Para implementar por Opus."
fecha: 2026-08-20
---

# Backlog de análisis — hallazgos verificados, pendientes de implementar

Reparto de trabajo acordado: **Fable analiza, Opus implementa.** Cada hallazgo trae la evidencia con
la que se verificó, para no re-derivar nada. Nada de esto está implementado todavía.

**Convención de prioridad:** 🔴 alta (afecta el uso real) · 🟠 media (calidad) · 🟡 baja (pulido).

---

## Parte 1 — MCP: robustez

### 🔴 M-01 · `buscar` es frase-exacta y falla con consultas naturales

**Evidencia (sonda por stdio, 2026-08-20):**

| Consulta real de estudiante | Resultado |
|---|---|
| `"diferencia entre include y extend"` | **0 resultados** — y el tema está cubierto en 3 notas |
| `"priorizar drivers"` | **0 resultados** — es el criterio de 30 puntos |
| `"cuantos actores debe tener un caso de uso"` | **0 resultados** — la regla está en Convenios §2 |
| `"contexto guatemalteco"` | 10 resultados (la frase aparece literal) |

**Causa raíz:** `src/notas.ts` ~línea 187: `if (!clave(linea).includes(termino)) continue;` —
la consulta completa se busca como **subcadena literal** de cada línea. Si la frase no aparece
textual, no hay nada.

**Especificación del arreglo:**

1. Tokenizar la consulta con `clave()`, descartando *stopwords* (`de la el los las un una y o
   que como entre debe tener cuantos cual es en del al por para se`).
2. Buscar en **tres pasadas**, con puntaje decreciente:
   - **frase exacta** en la línea (comportamiento actual) — puntaje máximo;
   - **todos los tokens en la misma línea**;
   - **todos los tokens en el mismo archivo** — reportando la línea que más tokens junta.
3. Bonificar cuando el match cae en el **título de la nota**, en un **alias** del frontmatter o en
   un **encabezado** (`## `): esas coincidencias van primero en la salida.
4. Si una consulta queda sin tokens tras las stopwords, caer al comportamiento actual.

**Criterio de aceptación** (agregar a `pruebas/cobertura.mjs`, ver M-05): las tres consultas que hoy
dan 0 devuelven, respectivamente, algo que contenga `"inclusi"` o `"extensi"`; `"priorizar"`;
`"Convenios"`.

### 🔴 M-02 · `buscar` escanea el glosario dos veces y devuelve duplicados

**Evidencia:** `buscar("plantilla obligatoria")` devuelve la línea `03-Glosario.md:148` **dos
veces**.

**Causa raíz:** en `src/notas.ts` (~149-165) la lista `objetivos` agrega `CARPETAS.glosario`
explícitamente **y además** el listado de la raíz (`listarArchivos(".")`) vuelve a incluir
`03-Glosario.md`. El mismo archivo se recorre dos veces.

**Arreglo:** deduplicar `objetivos` (un `Set` sobre la ruta normalizada) antes del bucle.
**Aceptación:** ninguna consulta devuelve dos veces la misma `ruta:línea`.

### 🔴 M-03 · `leer_nota` no resuelve los alias del frontmatter

**Evidencia:** `leer_nota("drivers")` → error, aunque la nota `Drivers arquitectónicos` declara
`alias: "drivers, driver arquitectonico, ..."`. La sugerencia del error es buena (propone la nota
correcta), pero obliga a una segunda llamada.

**Arreglo:** antes de fallar, resolver contra los `alias` del frontmatter de las notas — la misma
mecánica que ya usa `metodo_tarea` en `src/tareas.ts`. Si un alias matchea una única nota, devolverla
directamente. Si matchea varias, error con las candidatas (comportamiento actual).
**Aceptación:** `leer_nota("drivers")` devuelve la nota; `leer_nota("driver arquitectonico")` también.

### 🔴 M-05 · Regresión: agregar los casos nuevos a `cobertura.mjs`

Cuando M-01/M-02/M-03 estén hechos, agregar estos casos (formato del archivo existente):

```
["buscar", { consulta: "diferencia entre include y extend" }, "inclusi"],
["buscar", { consulta: "priorizar drivers" }, "priorizar"],
["buscar", { consulta: "cuantos actores debe tener un caso de uso" }, "Convenios"],
["leer_nota", { nombre: "drivers" }, "factores cr"],
```

Y un caso negativo de duplicados si el harness lo permite (o verificarlo en `verificaciones.ts`).

### 🟠 M-04 · Resultados de `buscar` sin agrupar: un archivo puede acaparar la salida

**Evidencia:** `buscar("paso 0")` → 19 coincidencias, muchas del mismo archivo; el tope global es 40
y se llena por orden de recorrido, no por relevancia.

**Arreglo:** tope de **2-3 líneas por archivo** en la salida (indicando "+N más en esta nota"), y
orden por puntaje de M-01. Mantener el tope global.

### 🟡 M-06 · `obtener_flashcards`: opción de orden aleatorio

Hoy devuelve las primeras N en orden del archivo. Para armar quizzes variados, un parámetro opcional
`aleatorio: true` que muestree sin repetir. Baja prioridad: el cliente puede pedir todas y elegir.

### 🟡 M-07 · `metodo_tarea` devuelve el frontmatter crudo

La salida arranca con el YAML (`---\ntema: ...`). Inofensivo para un cliente LLM, pero limpio sería
quitarlo y conservar solo `entregable`/`alias` en la cabecera formateada que ya imprime.

**Lo que se sondeó y está bien (no tocar):** las sugerencias de `leer_nota` ante error; el matcheo
parcial de `glosario` (`"driver"` → 4 entradas, `"cun"` → 4); la resolución de `metodo_tarea`
(`"priorizar"` → guía de drivers, `"caso 1"` → plan); el matcheo parcial de `obtener_flashcards`;
el corte en el **primer** `::` del parser de flashcards.

---

## Parte 2 — Bóveda: comprensión fina

### 🔴 F-02 · Calibración epistémica: hay inferencias nuestras etiquetadas como "de clase"

La jerarquía núcleo/complemento **depende de que las etiquetas sean confiables**. Tres archivos de
flashcards declaran *"Todas son de clase"* y contienen tarjetas cuya **respuesta es lectura nuestra**
(correcta, pero no verbatim de una diapositiva):

| Archivo | Tarjeta / claim | Qué es en realidad |
|---|---|---|
| `Flashcards - Drivers arquitectónicos y contexto` | *"El filtro es estructural: si el requisito cambia y hay que cambiar la estructura, es driver"* | **derivación nuestra** de "factores críticos que determinan su estructura fundamental" |
| ídem | *"Un driver de calidad sin número no es un driver, es un deseo"* | **editorial nuestro**; lo verbatim es que todos sus ejemplos llevan número |
| `Flashcards - Ejemplos resueltos y descripción textual` | *"3 a 5 procesos"* como escala | **patrón inducido** de 2 ejemplos (5 y 5) + 1 de 3; ella nunca dictó un rango |
| ídem | *"conviene la de la NT1"* para IDs | **consejo nuestro**, no indicación de ella |

**Arreglo (sin borrar contenido — las lecturas son valiosas):**
1. Cambiar la cabecera de los 3 archivos a: *"Salen de las diapositivas de clase; las respuestas
   marcadas «(lectura nuestra)» derivan de ellas pero no son texto de la catedrática."*
2. Agregar el marcador **«(lectura nuestra)»** al final de las ~4 respuestas listadas.
3. En `08-Tareas/Ejemplos resueltos…`, la regla 2 ("3 a 5 procesos") debe decir **"patrón observado
   en sus ejemplos, no regla dictada"**.

**Aceptación:** `grep -l "Todas son de clase" 04-Flashcards/` → 0 archivos con esa frase absoluta;
las 4 tarjetas llevan el marcador.

### 🟠 F-01 · Las formas del estereotipo están dispersas y nadie las reconcilia completo

El material de clase usa **siete** grafías para dos relaciones, y la bóveda las cita fielmente
(bien), pero solo hay una reconciliación parcial (extender/extiende/extend, en Ejemplos resueltos).
Conteo actual en la bóveda: `«include»` 47 · `«extend»` 35 · `«includes»` 7 · `«extends»` 5 ·
`«extender»` 5 · `«extiende»` 3 · `«incluye»` 1.

**Arreglo:** una tabla corta en `01-Notas/Relaciones y dependencias en UML.md` (junto a "La tabla
resumen de la clase"):

| Forma | Dónde aparece en el material |
|---|---|
| `«extiende»` / `«incluye»` | la tabla *Resumen de los Tipos de Relaciones* |
| `«extends»` / `«include»` | las diapositivas de definición (Extensión / Inclusión) |
| `«extender»` | el expandido del restaurante (con guardas `{...}`) |
| `«includes»` / `«extends»` | el expandido *Procesamiento de Pedido* |

Con la regla: **todas nombran la misma relación; en una entrega se elige UNA pareja y se es
consistente; al citar una diapositiva, se cita textual.** Cross-link desde
[[Relación de inclusión include]] y [[Relación de extensión extend]].

### 🟠 F-04 · La regla espejo (actor sin CU) no está en la nota canónica de convenios

La regla existe — diapositiva 30: *"cada actor se involucra con al menos un caso de uso"* — y está
en `Caso de uso del negocio.md:48` y en la checklist de `Guía - Diagrama de casos de uso del
negocio.md:156` ("un actor suelto es un error"). Pero **`Convenios del diagrama de CUN` §2 solo
cubre la dirección CU-sin-actor**. Quien lea la nota canónica de reglas de dibujo no ve la mitad
espejo.

**Arreglo:** en Convenios §2, añadir la regla espejo con la cita de la diapositiva y el cross-link.
Nota fina: en la generalización de actores del hospital, el padre *Cliente* **sí** tiene CU propio
(*Despachar medicamentos*), así que la regla no tiene la excepción simétrica del lado del actor —
vale decirlo.

### 🟡 F-03 · Áreas-como-actores: la conclusión está, la base doctrinal no está conectada

`Ejemplos resueltos` justifica "las áreas son actores" **empíricamente** (el hospital de ella). La
base doctrinal ya vive en `Actor del negocio.md:24`: los candidatos incluyen *"otras partes de la
organización, si ésta es grande"* — eso es exactamente Contabilidad/Ventas/Almacén como actores.
**Arreglo:** una línea en Ejemplos resueltos §4 citando esa viñeta y enlazando [[Actor del negocio]].
Convierte una induction en una regla con dos fuentes.

---

## Parte 3 — Orden de implementación sugerido

1. **M-02** (bug de 3 líneas) → **M-03** (mecánica ya existe en `tareas.ts`) → **M-01+M-04** (el
   grueso) → **M-05** (regresión).
2. **F-02** (integridad de etiquetas: es lo que protege la jerarquía de fuentes) → **F-01** →
   **F-04** → **F-03**.
3. Al cerrar: `npm run build` + los cuatro audits + validar Mermaid + espejar al repo + commit.

Lo que NO hay que hacer: no re-dibujar en Mermaid los diagramas de ella (ver la advertencia en
`CLAUDE.md` §Procesar capturas); no agregar herramientas nuevas al MCP (las 12 cubren los casos de
uso; el problema es la calidad de `buscar`, no la falta de superficie).
