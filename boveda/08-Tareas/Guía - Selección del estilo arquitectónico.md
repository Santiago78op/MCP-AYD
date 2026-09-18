---
tema: Guía por entregable
fuente: "Presentación de clase — capturas_U2_F3 (33-39, «call return: SOA») y capturas_U2_F2 (9, 30). NÚCLEO. + la Entrega de la Tarea 2 FarmaHosp §5, que es el molde ya resuelto."
fecha: 2026-09-18
entregable: Selección del estilo arquitectónico
alias: [estilo, seleccion de estilo, elegir estilo, justificar estilo, que estilo uso, soa]
---

# Guía — Selección del estilo arquitectónico

Para cuando el enunciado dice *«seleccione el estilo arquitectónico y justifíquelo»*. Está pensada
para **modo examen**: molde primero, teoría al final.

---

## 1. La respuesta por defecto es SOA — y por qué

Dos razones distintas, y conviene no confundirlas:

| Razón | Peso |
|---|---|
| **A la catedrática le gusta SOA.** Observación de clase (Julián, 2026-09-18) | Es una preferencia, no una regla: **inclina el empate**, no reemplaza la justificación |
| **SOA encaja en casi cualquier caso del curso** | Esta es la razón fuerte, y es estructural — ver abajo |

**Por qué encaja casi siempre, mecánicamente:** todo caso de este curso arranca con un **caso de
negocio** que produce N procesos (`CDU-01`…`CDU-0n`). Y el escalón 2 de su propia lámina dice
*"Desarrolla procesos de negocio como **Servicios**"*. O sea: **el mapeo ya está hecho por el
entregable anterior** — un servicio por proceso, y la justificación se escribe sola. Ningún otro
estilo tiene ese puente directo con el criterio 1.

> [!important] Pero SOA no se contesta a ciegas
> Si el enunciado trae una restricción que la contradice y la contestás igual, se pierde más de lo
> que se gana. Ver §5, *cuándo NO contestar SOA*. La preferencia inclina el empate; **la evidencia
> del enunciado decide**.

---

## 2. El molde de respuesta, en cinco partes

Se responde en este orden. Con las cinco partes el criterio está completo.

### Parte 1 — La decisión, en una línea

> **Arquitectura orientada a servicios (SOA)** con **un servicio de negocio por proceso**
> (`CDU-01`…`CDU-0n`), **cada servicio en capas**, **llamada y retorno** para lo que exige respuesta
> inmediata y **basada en eventos** para lo asíncrono.

Adaptá solo la enumeración de procesos y los complementarios que el caso pida.

### Parte 2 — Los cuatro escalones de la captura 35

Es la lámina *«Funcionamiento de la Arquitectura (SOA)»*. Se recorre escalón por escalón: eso es lo
que convierte la elección en justificación.

| Escalón | Texto de la lámina | Cómo se llena |
|---|---|---|
| 1. Definición | *"Define las necesidades del negocio"* | los N procesos del criterio 1 y los RF del criterio 3 |
| 2. Desarrollo | *"Desarrolla procesos de negocio como Servicios"* | **un servicio por proceso**, nombrados igual que los CDU |
| 3. Evolución | *"Permite que cada Servicio evolucione independientemente"* | el módulo del caso que tiene **otro ciclo de entrega** |
| 4. Distribución | *"Plantea aplicaciones distribuidas, multi-nivel"* | clientes → acceso → servicios → datos |

Y la definición conceptual (captura 33): *"un servicio (cliente) realiza una solicitud (llamada) a
otro servicio (proveedor) y espera una respuesta (retorno)"*.

### Parte 3 — Los complementarios, cada uno con su driver

**Un sistema real no es de un solo estilo.** El principal fija la estructura; los complementarios
resuelven drivers puntuales. **Regla: si no podés nombrar el driver que lo obliga, el estilo sobra.**

| Complementario | Se dispara cuando el enunciado pide… |
|---|---|
| **En capas** (dentro de cada servicio) | mantenibilidad, equipo que ya lo conoce, evolución por partes |
| **Llamada y retorno** (REST síncrono) | una respuesta **antes** de seguir: validaciones, consultas con tiempo límite |
| **Basada en eventos** (bus/cola) | picos, sistemas externos con ventana horaria, notificaciones, sincronización |
| **Cliente-servidor offline-first** | red inestable, operación sin conexión, reconciliación |
| **Tuberías y filtros** | telemetría o datos que pasan por **transformaciones sucesivas** |

### Parte 4 — Los descartados, con evidencia

Descartar bien vale tanto como elegir. El repertorio rápido:

| Estilo | Se descarta cuando… |
|---|---|
| **Monolítico** | hay módulos con ciclos de entrega distintos *(y a veces el enunciado lo prohíbe con todas las letras)* |
| **Microservicios** | el equipo es chico o la infraestructura es fija: cada microservicio suma despliegue, monitoreo y base propia |
| **Peer to peer** | hace falta **una sola verdad auditable** o consistencia fuerte |
| **Microkernel** | no hay un núcleo estable con extensiones enchufables, sino N procesos del mismo peso |
| **REST como estilo único** | se usa REST de **protocolo**, pero no resuelve la asincronía |

### Parte 5 — Cómo atiende a los drivers más críticos

Una fila por driver del top 5: *driver → táctica → dónde se ve en el diagrama*. Es lo que impide que
la elección quede decorativa.

---

## 3. La carta de las dos familias

La captura 34 dice: *"Es **event-based** porque puede usar motores de orquestación/coreografía e
invocar servicios de forma asíncrona"*. Y en el árbol C&C SOA cuelga de **call-return**.

**Eso es una ventaja para contestar:** SOA te habilita a defender lo **síncrono** y lo **asíncrono**
en la misma respuesta, sin contradecirte. Si el caso tiene una validación que corre contra reloj y un
reporte que espera una ventana horaria, los dos caben.

> [!warning] Y también es la trampa
> Si preguntan *"¿a qué familia pertenece SOA?"* hay **dos respuestas de clase** y ella no eligió
> (duda #24 de [[Preguntas pendientes para clase]]). Contestá **call-return según el árbol C&C, y
> agregá que la captura 34 la declara también event-based**. Nombrar las dos es más seguro que
> apostar a una.

---

## 4. Checklist de rigor

- [ ] ¿La definición de estilo es **textual de clase**, con su fuente?
- [ ] ¿Los cuatro escalones de la captura 35 están **recorridos**, no solo mencionados?
- [ ] ¿Cada estilo elegido cita el **driver o la restricción** que lo obliga?
- [ ] ¿Están los **descartados**, con su evidencia?
- [ ] ¿Se dice cómo se atienden los **drivers más críticos**?
- [ ] ¿Ningún estilo entró «porque sí»?

---

## 5. Cuándo NO contestar SOA

Tres señales. Si aparece alguna, SOA cuesta puntos y hay que contestar otra cosa:

| Señal en el enunciado | Qué contestar |
|---|---|
| Pide **un solo desplegable**, o el equipo/infraestructura no sostiene servicios separados | **En capas** (es *"una especialización de la arquitectura cliente-servidor"*, lámina 10) |
| **No hay procesos de negocio separables**: es un único flujo de transformación de datos | **Tuberías y filtros**, o flujo de datos |
| Es un **cliente y un servidor**, sin más | **Cliente-servidor** — y recordá que cliente y servidor son **roles, no máquinas** |

Y la regla general: **si el enunciado prohíbe algo con la palabra «no se puede», eso manda sobre
cualquier preferencia.** La restricción se cita textual y decide.

---

## Notas relacionadas

- [[Arquitectura orientada a servicios]] — las siete láminas, con la escalera y las dos familias
- [[Estilos arquitectónicos]] §2 bis — cuánto le dedicó a cada estilo (**capas 17, SOA 7**): para
  repartir el **estudio**, que es otra cosa que elegir la **respuesta**
- [[Catálogo de estilos arquitectónicos]] — el árbol C&C y las familias
- [[Arquitectura en capas]] — el complementario que casi siempre acompaña
- [[Entrega - Tarea 2 FarmaHosp]] §5 — el molde **ya resuelto**, con las cinco partes llenas
- [[_Método para resolver una tarea]] — los parámetros de forma del documento

## Preguntas de repaso

1. ¿Por qué SOA encaja en casi cualquier caso del curso? ¿Cuál es el puente con el criterio 1?
2. Nombrá los cuatro escalones de la lámina de funcionamiento de SOA.
3. ¿Qué hay que poder decir de cada estilo complementario para que no sobre?
4. ¿A qué familia pertenece SOA? ¿Por qué la respuesta tiene dos partes?
5. Dá las tres señales de que **no** hay que contestar SOA, y qué se contesta en cada caso.
6. ¿Qué manda sobre la preferencia de la catedrática?
