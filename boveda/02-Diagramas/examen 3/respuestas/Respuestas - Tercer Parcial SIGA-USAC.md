---
tema: Examen
fuente: "Tercer Parcial. SIGA USAC.pdf (09-examenes/Examen_3), 17/10/2026"
fecha: 2026-10-17
---

# Tercer parcial — SIGA-USAC

**Supuestos declarados.** (1) Las medidas numéricas que el enunciado no da son supuestos del arquitecto.
(2) En el EAC 1 la «Oficina de Inscripciones» se toma como el servicio que informa el estado de pago (la Colecturía Central del req. 3: SOAP, de 2 a 15 s). (3) Cada escenario lleva su prioridad como un par de letras A/M/B (alta, media, baja), en el formato de la tabla de escenarios del ejemplo READM visto en clase. La lámina no define el par: se toma la lectura de Cervantes, Velasco y Castro, donde el primer valor es la **importancia para el negocio** y el segundo la **dificultad técnica**. (4) Los nombres de las tácticas siguen el catálogo de Bass, Clements y Kazman.

**Requerimientos del enunciado que se citan** (req. = requerimiento numerado del enunciado):

| Req. | Nombre | Lo que exige | Dónde se usa |
|---|---|---|---|
| 1 | Alta concurrencia estacional | picos de 15 000 usuarios concurrentes en enero y julio; 800 el resto del semestre | Serie I (desempeño), EAC-01, Serie III |
| 2 | Múltiples canales de acceso | web y app móvil; actas por CSV de hasta 5 MB con confirmación de procesamiento | EAC-02, Serie III |
| 3 | Integración con sistemas externos | consultar el pago en la Colecturía (SOAP, 2 a 15 s) antes de asignar; publicar notas al Portal de Transparencia en ≤ 24 h | EAC-01 |
| 4 | Seguridad y auditoría | cambio de nota registrado con usuario, fecha, hora e IP; actas solo del catedrático asignado; bloqueo y aviso en < 5 s | Serie I (seguridad), EAC-03 |
| 5 | Disponibilidad | 24/7 con 2 h de mantenimiento el domingo; pérdida de notas ≤ 5 min | Serie I (disponibilidad), EAC-02 |
| 6 | Mantenibilidad | Inscripción, Notas y Reportes evolucionan y se despliegan por separado | nota al pie de la Serie I |

**Abreviaturas:** EAC = escenario de atributo de calidad · (A, M) = prioridad (importancia, dificultad) en Alta / Media / Baja · p95 = el 95 % de las solicitudes · API = interfaz con la que se comunica otro sistema · CSV = archivo de texto separado por comas · IP = dirección de red del equipo · s, ms, min, h = segundos, milisegundos, minutos, horas.

## Serie I — Atributos de calidad y tácticas

| Atributo de calidad | Justificación (contexto) | Táctica propuesta | Explicación de la táctica |
|---|---|---|---|
| **1. Desempeño / escalabilidad** | **Req. 1**: picos de **15 000 usuarios concurrentes** en enero y julio contra 800 en promedio; el legado monolítico ya colapsa en inscripción y cierre. | **Múltiples copias de cómputo** (escalamiento horizontal elástico tras un balanceador de carga) | Cuando la CPU supera el 70 % se agregan réplicas del servicio de Inscripción que se reparten la carga, con lo que la respuesta se mantiene en ≤ 2 s (p95) con 15 000 usuarios y las réplicas se liberan al volver a 800. |
| **2. Disponibilidad** | **Req. 5**: operación **24/7** con solo 2 h de mantenimiento semanal y **pérdida de notas ≤ 5 min** ante falla catastrófica. | **Redundancia pasiva** (réplica en espera de la base de notas con replicación continua) | Al caer el nodo principal se activa la réplica, que recibe los cambios cada ≤ 1 min, con lo que la pérdida queda bajo los 5 min exigidos y el servicio vuelve en ≤ 5 min. |
| **3. Seguridad** | **Req. 4**: cada cambio de nota se registra con **usuario, fecha, hora e IP**, las actas son solo del **catedrático asignado** y todo acceso no autorizado se **bloquea y notifica en < 5 s**. | **Autorizar actores** (control de acceso por atributos: rol + asignación al curso) | Cada solicitud sobre un acta se valida contra la asignación catedrático-curso antes de ejecutarse, y si se niega se bloquea, queda registrada con usuario, fecha, hora e IP y se alerta al administrador en < 5 s. |

> Fuera a propósito: **mantenibilidad** (req. 6) también es relevante, pero se pidieron tres y se priorizaron las que hacen fallar la operación en un pico; se resuelve con un servicio desplegable por módulo (Inscripción, Notas, Reportes).

## Serie II — Escenarios de atributo de calidad

### Tabla de drivers de atributos de calidad (formato de clase, ejemplo READM)

| ID | Categoría | Escenario | Prioridad |
|---|---|---|---|
| EAC-01 | Disponibilidad | **Fuente de estímulo:** un estudiante. **Estímulo:** solicita la asignación de un curso y la API de verificación de pagos no responde en 3 s o está caída. **Artefacto:** el servicio de Inscripción. **Entorno:** en la primera semana de inscripción, con 15 000 usuarios concurrentes. **Respuesta:** el sistema reserva el cupo como pendiente de verificación y confirma o libera la asignación cuando la API vuelve. **Medida de la respuesta:** el 95 % de las solicitudes se responde en ≤ 4 s y ninguna se pierde. | (A, A) |
| EAC-02 | Fiabilidad | Ocurre un reinicio inesperado del servidor de aplicaciones mientras un catedrático carga un CSV de notas finales, en el cierre de semestre. El sistema no deja ninguna nota parcial en la tabla oficial y reanuda o rechaza el lote completo en ≤ 2 min, notificando al catedrático en ≤ 1 min. | (A, M) |
| EAC-03 | Seguridad | Un atacante con credenciales robadas de un catedrático intenta modificar una nota desde fuera de la red de la USAC, en horario inusual, durante la operación normal. El sistema bloquea el cambio antes de aplicarlo y notifica al administrador de seguridad y al catedrático en ≤ 5 s. | (A, A) |

### EAC-01 «Cuello de botella» — Disponibilidad (con impacto en desempeño) · Prioridad (A, A)

| Parte | Contenido |
|---|---|
| **Fuente del estímulo** | Estudiante (web o app móvil) que solicita una asignación; la falla la origina el sistema externo de verificación de pagos. |
| **Estímulo** | La API de verificación de deudas no responde en **3 s** o está caída mientras el estudiante solicita la asignación. |
| **Artefacto** | Servicio de Inscripción (su componente de integración con la API de pagos). |
| **Entorno** | Operación en pico: primera semana de inscripción, hasta **15 000 usuarios concurrentes**. |
| **Respuesta** | El sistema corta la llamada a los 3 s; consulta la **caché local del estado de pago** (actualizada cada 1 h). Si no hay dato, **reserva el cupo en estado «pendiente de verificación»** (la asignación no se confirma sin el estado de pago, req. 3), encola la verificación y avisa al estudiante. Reintenta con espera creciente. Tras **5 fallos seguidos** deja de llamar a la API por **60 s**. Al responder la API, confirma la asignación o libera el cupo y notifica al estudiante. |
| **Medida de la respuesta** | **95 %** de las solicitudes respondidas en **≤ 4 s**, aun con la API caída · **0** solicitudes perdidas por indisponibilidad de la API · reservas pendientes confirmadas o liberadas en **≤ 30 min** tras volver la API. |

### EAC-02 «Fuga de notas» — Fiabilidad (tolerancia a fallos y recuperabilidad; integridad) · Prioridad (A, M)

| Parte | Contenido |
|---|---|
| **Fuente del estímulo** | Falla interna: reinicio inesperado del servidor de aplicaciones (el catedrático estaba subiendo el acta). |
| **Estímulo** | El servidor se reinicia a mitad del procesamiento de un CSV de notas finales (hasta **5 MB**). |
| **Artefacto** | Servicio de Notas (procesador de cargas masivas) y base de datos de notas. |
| **Entorno** | Operación normal en cierre de semestre (carga alta de actas). |
| **Respuesta** | Cada lote tiene un identificador y se carga primero en una **tabla temporal de preparación** (staging), con un **punto de control** persistido cada 500 filas validadas. Las notas pasan a la tabla oficial en **una sola transacción atómica (todo o nada)**. Al reiniciar, el sistema lee el estado del lote. Si quedó incompleto, retoma desde el último punto de control. Si había filas inválidas o el archivo está corrupto, **rechaza el lote completo**. Las notas oficiales nunca quedan a medias. En todos los casos envía al catedrático la confirmación de procesamiento (req. 2). |
| **Medida de la respuesta** | **0** notas parciales o corruptas en la tabla oficial · lote reanudado o rechazado en **≤ 2 min** después del reinicio · catedrático notificado en **≤ 1 min** tras la recuperación · pérdida máxima de **5 min** de operación (req. 5). |

### EAC-03 «Intento de suplantación» — Seguridad (integridad y no repudio) · Prioridad (A, A)

| Parte | Contenido |
|---|---|
| **Fuente del estímulo** | Atacante externo con **credenciales válidas robadas** de un catedrático. |
| **Estímulo** | Intenta **modificar una nota** desde una IP fuera de la red de la USAC, en horario inusual (por ejemplo, a las 03:00) y desde una sede distinta a la habitual. |
| **Artefacto** | Servicio de Notas: su componente de autorización y detección de anomalías, y los datos de actas. |
| **Entorno** | Operación normal, sistema en línea, sesión ya autenticada. |
| **Respuesta** | Antes de confirmar el cambio, el sistema calcula un **puntaje de riesgo** (IP y geolocalización, horario, dispositivo, sede habitual). Si supera el umbral, **retiene la operación sin aplicarla** y suspende la sesión. Registra el intento con usuario, fecha, hora e IP (req. 4). **Notifica al administrador de seguridad y al catedrático**, y este confirma por un segundo factor si fue él o lo niega. Si confirma, se aplica el cambio. Si lo niega o no responde en **24 h**, se descarta, se revocan las sesiones y se fuerza el cambio de contraseña. |
| **Medida de la respuesta** | **100 %** de las modificaciones anómalas bloqueadas **antes** de consumarse · notificación a los dos en **≤ 5 s** (req. 4) · **100 %** de los intentos en la bitácora · falsos positivos **≤ 2 %** de las operaciones legítimas. |

## Serie III — Tradeoff

### a) El conflicto

**El EAC-03 (Seguridad) entra en conflicto con el atributo de Desempeño**, porque para bloquear la modificación *antes* de que se consume, cada cambio de nota debe evaluarse en línea: puntaje de riesgo, consulta de geolocalización e historial, y escritura en la bitácora de auditoría. Ese trabajo sincrónico se suma al tiempo de respuesta de **cada** operación, y se multiplica en el cierre de semestre, cuando miles de catedráticos cargan notas a la vez (req. 1 y 2). Si se evalúa todo a fondo, el sistema se vuelve lento justo en el pico. Si se evalúa poco para ganar velocidad, pasan las suplantaciones.

### b) Decisión de diseño: evaluación de riesgo en dos niveles (táctica combinada con eventos)

1. **Nivel sincrónico, liviano**: reglas en memoria antes del commit, que comparan la IP contra la red de la USAC, el horario habitual y la sede del catedrático (datos en caché). Agrega **≤ 50 ms**, y solo lo que supera el umbral se **retiene** y pide confirmación por segundo factor (autenticación escalonada).
2. **Nivel asíncrono, profundo**: cada cambio de nota publica un evento `NotaModificada` en el **bus de eventos** (publicador/suscriptor). Un servicio de seguridad suscrito hace el análisis pesado (historial, patrones, correlación) y escribe la auditoría **fuera del camino de la respuesta**. Si detecta algo, revierte y notifica.

**Por qué balancea sin sacrificar ninguno:**
- **Desempeño**: el ~99 % de las operaciones legítimas solo paga el chequeo liviano (≤ 50 ms) y la auditoría no las espera, así se sostiene ≤ 2 s (p95) en el pico.
- **Seguridad**: lo anómalo sigue bloqueándose **antes** del commit, que es lo que exige el EAC-03, y la notificación en ≤ 5 s sale por el bus.
- **El costo aceptado**: un análisis profundo tardío solo puede **revertir**, no prevenir, y el umbral del nivel liviano debe calibrarse para mantener los falsos positivos ≤ 2 %.

## Referencias

- Enunciado del tercer parcial, *SIGA-USAC: Sistema Integrado de Gestión Académica*. Análisis y Diseño de Sistemas II, sección P, USAC, 2026.
- Material de clase, *Calidad del Software Parte II*: ejemplo del Sistema de Transporte READM (tabla de escenarios EAC con prioridad).
- Cervantes, H., Velasco, P. y Castro, L. *Arquitectura de software: conceptos y ciclo de desarrollo*. Cengage Learning, 2016.
- Bass, L., Clements, P. y Kazman, R. *Software Architecture in Practice*. Addison-Wesley, 3.ª ed., 2012.
