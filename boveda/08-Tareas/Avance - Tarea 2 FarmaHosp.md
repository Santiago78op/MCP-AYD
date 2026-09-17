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
| 6 | **Diagrama de bloques y de despliegue** | 30 | Tarea 2 §6 | ✅ **hecho** — 2 láminas verificadas con captura, tablas de trazabilidad, cuentas de hardware, escenarios recorridos |

**Total: 100 pts cubiertos.**

## Lo que falta para entregar

| Pendiente | Por qué | Prioridad |
|---|---|---|
| **Pasar a limpio** en un solo documento (Word/PDF) con los criterios 1-6 | La plataforma recibe un archivo; la bóveda tiene el contenido repartido en dos Entregas | Alta — antes del 18/09 |
| Revisar la Entrega §5 y §6 **con el estudiante** y que la pueda defender | Modo resolver y explicar: estudia el razonamiento | Alta |
| *(Opcional)* Diagrama de componentes separado, con piruletas y dependencias | La rúbrica no lo pide; los componentes ya están dentro del despliegue | Baja |

## Decisiones tomadas (no volver a discutir sin evidencia nueva)

1. **Criterios 1-4 se reutilizan** de la Tarea 1: la rúbrica es la misma con otros pesos.
2. **Estilo principal SOA**: sale de la escalera de la captura 35 y de `RE-05`/`RE-18`.
3. **La réplica de lectura va en el sitio alterno**, porque la SAN de 10 TB no admite una segunda copia de 5 TB.
4. **Componentes dentro del despliegue**, como la captura 57, en vez de lámina aparte.

## Bitácora

| Fecha | Qué se cerró |
|---|---|
| 2026-09-17 | Análisis del enunciado de la Tarea 2: criterios 1-4 repetidos, 5 y 6 nuevos; hueco detectado (descripciones textuales) |
| 2026-09-17 | §2.4 descripciones textuales de CDU-01..07 |
| 2026-09-17 | §5 estilo y justificación, §6 bloques y despliegue: láminas `6-bloques-despliegue/` generadas, miradas y corregidas (cruces de externos, AMQP vs. replicación, rótulo del data center) |
