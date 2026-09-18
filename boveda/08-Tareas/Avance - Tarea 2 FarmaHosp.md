---
tema: Control de avance
fuente: "Rúbrica de Caso FarmaHosp- Tarea 2 Continuación.pdf"
fecha: 2026-09-17
tarea: Tarea 2 - FarmaHosp (continuación)
---

# Avance — Tarea 2 FarmaHosp (continuación)

Tablero contra la rúbrica. **Entrega: 18 de septiembre de 2026.** Modo de trabajo: **resolver y
explicar** (elegido el 2026-09-17). Individual (el enunciado dice "en grupo"; el estudiante la hace solo).

Entrega: [[Entrega - Tarea 2 FarmaHosp]] · Base: [[Entrega - Caso 1 FarmaHosp]] · Tablero anterior: [[Avance - Caso 1 FarmaHosp]]

---

## Estado por criterio de la rúbrica

| # | Criterio | Pts | Dónde | Estado |
|---|---|---|---|---|
| 1 | Caso de negocio: contexto, core, primera descomposición | 20 | Caso 1 §2 | ✅ hecho en la Tarea 1 |
| 1 | **+ descripciones textuales** de los procesos (pedido de la plataforma) | — | Tarea 2 §2.4 | ✅ **hecho** — los 7 CDU con la plantilla *Atender pedido* |
| 2 | Stakeholders | 10 | Caso 1 §1 | ✅ hecho en la Tarea 1 |
| 3 | Drivers RF, de calidad, de restricción y top 5 | 20 | Caso 1 §3 | ✅ hecho en la Tarea 1 |
| 4 | Matrices de trazabilidad | 10 | Caso 1 §4 | ✅ hecho en la Tarea 1 |
| 5 | **Estilo arquitectónico y justificación** | 10 | Tarea 2 §5 | ✅ **hecho** — SOA + capas + llamada y retorno + eventos + cliente-servidor offline + tuberías y filtros; descartados con evidencia; top 5 atendido; stack |
| 6 | **Diagrama de bloques y de despliegue** | 30 | Tarea 2 §6 | ✅ **hecho** — 3 láminas (bloques, componentes, despliegue) verificadas con captura, tablas de trazabilidad, cuentas de hardware, escenarios recorridos |

**Total: 100 pts cubiertos.**

## Lo que falta para entregar

| Pendiente | Estado |
|---|---|
| **Pasar a limpio** en un solo documento | ✅ **hecho** — `Entrega - Tarea 2 FarmaHosp.docx`, criterios 1-6 y las 7 láminas |
| Revisar §5 y §6 con el estudiante y que la pueda defender | ✅ **hecho** — se recorrió el razonamiento el 18/09 |
| **Subirlo a la plataforma** | ⬜ lo hace el estudiante |

El `.docx` se **regenera** con `python3 06-Proyecto-MCP/generar-entrega-docx.py`: lee las láminas de
`02-Diagramas/`, las convierte a PNG 2× y arma el documento con los parámetros de forma del paso 6
de [[_Método para resolver una tarea]].

## Decisiones tomadas (no volver a discutir sin evidencia nueva)

1. **Criterios 1-4 se reutilizan** de la Tarea 1: la rúbrica es la misma con otros pesos.
2. **Estilo principal SOA**: sale de la escalera de la captura 35 y de `RE-05`/`RE-18`.
3. **La réplica de lectura va en el sitio alterno**, porque la SAN de 10 TB no admite una segunda copia de 5 TB.
4. **Los componentes aparecen dos veces**: con sus interfaces en la lámina de componentes y dentro de los nodos del despliegue, como en la captura 57.

## Bitácora

| Fecha | Qué se cerró |
|---|---|
| 2026-09-17 | Análisis del enunciado de la Tarea 2: criterios 1-4 repetidos, 5 y 6 nuevos; hueco detectado (descripciones textuales) |
| 2026-09-17 | §2.4 descripciones textuales de CDU-01..07 |
| 2026-09-17 | Lámina de componentes agregada: piruletas, dependencias punteadas y grupo de servicios de negocio; corregido que `IOrdenCompra` colgaba del componente equivocado |
| 2026-09-17 | §5 estilo y justificación, §6 bloques y despliegue: láminas `6-bloques-despliegue/` generadas, miradas y corregidas (cruces de externos, AMQP vs. replicación, rótulo del data center) |
| 2026-09-18 | Se recorrió §5 y §6 con el estudiante: escalera de SOA, cuentas de hardware y por qué la réplica va al sitio alterno |
| 2026-09-18 | **Diagrama de contexto rehecho**: el render de StarUML traía marca de agua *UNREGISTERED*, rótulos encimados y sin tildes. Ahora sale de `generar-excalidraw.py`. Tres vueltas de generar → mirar → corregir |
| 2026-09-18 | **La diagonal de negocio, corregida** en el core y en la primera descomposición: cruza la cabeza del actor y corta el borde derecho de la elipse, como en la lámina de la cátedra |
| 2026-09-18 | Conteo del contexto: **27 streamlines**, no 25 — el mermaid de trabajo omitía dos retornos que la tabla sí lista |
| 2026-09-18 | **Entrega en limpio**: sin carátula, sin checklists ni comentarios sobre la rúbrica, monocroma, saltos solo de nivel 1. Los parámetros quedaron en el paso 6 del método |
