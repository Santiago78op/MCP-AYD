---
tema: Entrega
fuente: "Caso FarmaHosp- Tarea 2 Continuación.pdf + Caso 1 - FarmaHosp (enunciado) + Entrega - Caso 1 FarmaHosp (criterios 1-4)"
fecha: 2026-09-17
tarea: Tarea 2 - FarmaHosp (continuación)
estado: en construccion
---

# Tarea 2 — FarmaHosp (continuación) · Entrega

Enunciado: `08-Tareas/enunciados/Caso FarmaHosp- Tarea 2 Continuación.pdf` y [[Caso 1 - FarmaHosp]] ·
Base: [[Entrega - Caso 1 FarmaHosp]] · Tablero: [[Avance - Tarea 2 FarmaHosp]]

> [!important] Qué cambia respecto de la Tarea 1
> La rúbrica de la Tarea 2 **repite los criterios 1-4** del Caso 1 con otros pesos y **agrega dos**:
>
> | # | Criterio | Pts T1 | **Pts T2** | Dónde está |
> |---|---|---|---|---|
> | 1 | Caso de negocio (contexto, core, primera descomposición) | 25 | **20** | [[Entrega - Caso 1 FarmaHosp]] §2 + **§2.4 de este documento** (descripciones textuales) |
> | 2 | Identificación de stakeholders | 25 | **10** | [[Entrega - Caso 1 FarmaHosp]] §1 |
> | 3 | Drivers RF, de calidad, de restricción y top 5 | 30 | **20** | [[Entrega - Caso 1 FarmaHosp]] §3 |
> | 4 | Matrices de trazabilidad | 20 | **10** | [[Entrega - Caso 1 FarmaHosp]] §4 |
> | 5 | **Selección del estilo arquitectónico y su justificación** | — | **10** | **§5 de este documento** |
> | 6 | **Diagrama de bloques y de despliegue** | — | **30** | **§6 de este documento** |
>
> El enunciado pide *"teniendo en cuenta TODO Y SOLO TODO el enunciado"*: cada decisión de §5 y §6
> cita el driver (`AC-nn`), la restricción (`RE-nn`) o el requisito (`RF-nn`) que la obliga. Nada se
> agrega por gusto.
>
> Las instrucciones de la plataforma piden además *"diagramas de casos de uso de alto nivel **con sus
> descripciones textuales**"*: la Entrega del Caso 1 no las tenía. Van en §2.4.

---

## 2.4 Descripciones textuales de los procesos de negocio

**Plantilla usada:** la de *Atender pedido* — la que coincide con la lista de campos que dictó la
catedrática y la única que mostró resuelta: Nombre, Actores, Propósito, Resumen, **curso normal en dos
columnas con una sola numeración intercalada**, Cursos alternos anclados con *"En la línea N"*,
Prioridad, Mejoras y Otras secciones. Ver [[Descripción textual de casos de uso]].

> [!note] Plano de negocio: la columna derecha es "Respuesta del proceso de negocio"
> Quienes actúan en la columna derecha son **trabajadores del negocio** (médico tratante, farmacéutico
> clínico, enfermero de piso, almacenista, jefe de farmacovigilancia, director administrativo): están
> **dentro** de la frontera declarada en [[Entrega - Caso 1 FarmaHosp]] §0. En la columna izquierda
> solo aparecen los **cinco actores** del core: PACIENTE, PROVEEDOR DE MAC, MSPAS, CONTRALORÍA GENERAL DE
> CUENTAS y SISTEMA LEGACY DE ADMISIONES.

### CDU-01 · Adquisición de MAC

| Campo | Contenido |
|---|---|
| **Nombre** | Adquisición de MAC |
| **Actores** | PROVEEDOR DE MAC |
| **Propósito** | Abastecer al hospital de medicamentos de alto costo con número de lote, fecha de vencimiento y factura exactos, verificando su calidad desde la recepción. |
| **Resumen** | El caso de uso se inicia cuando se detecta la necesidad de comprar un MAC (por la proyección de faltantes o por una solicitud urgente del médico). El proceso autoriza y emite la orden de compra, recibe los lotes y controla su calidad. El caso de uso finaliza cuando los lotes conformes quedan ingresados al almacén y el proveedor recibe la conformidad de la recepción. |

| Acción del actor | Respuesta del proceso de negocio |
|---|---|
| | **1.** El Farmacéutico clínico identifica la necesidad de compra a partir de la proyección de faltantes a 7 días. |
| | **2.** El Director Administrativo autoriza la orden de compra; queda registrado quién la autorizó. |
| | **3.** El Almacenista emite la orden de compra al Proveedor de MAC. |
| **4.** El Proveedor de MAC recibe la orden de compra y entrega los lotes con su factura. | |
| | **5.** El Almacenista recibe los lotes y registra número de lote, fecha de vencimiento y factura, leyéndolos de la etiqueta del proveedor, sin transcripción manual. |
| | **6.** El Farmacéutico clínico realiza el control de calidad de recepción (temperatura y humedad). *Si el lote es conforme, pasar a 7. Si no es conforme, ver curso alterno de la línea 6.* |
| | **7.** El Almacenista ubica cada lote en la cámara que le corresponde (2-8 °C, -20 °C o ambiente) y lo deja disponible para su conservación. |
| **8.** El Proveedor de MAC recibe la conformidad de la recepción. | |

**CURSOS ALTERNOS**

- **En la línea 1:** el Médico tratante solicita una **compra urgente o un reemplazo terapéutico** porque no hay stock para su prescripción. La orden se marca como urgente y se continúa en la línea 2.
- **En la línea 6:** el lote **no es conforme**. El Farmacéutico clínico lo rechaza registrando el motivo, el Almacenista lo devuelve y el Proveedor de MAC recibe la notificación de rechazo. Fin del caso de uso para ese lote.

**Prioridad:** Alta.

**Mejoras**

- Recibir del proveedor el lote, el vencimiento y la factura en formato electrónico: elimina la transcripción manual que originó los 3 errores de medicación del enunciado.
- Que el proveedor pueda notificar **retiros de lote** por la misma vía.

### CDU-02 · Almacenamiento y conservación de MAC

| Campo | Contenido |
|---|---|
| **Nombre** | Almacenamiento y conservación de MAC |
| **Actores** | *Ninguno* — caso de uso **de apoyo** (excepción de los convenios de clase; declarada en [[Entrega - Caso 1 FarmaHosp]] §2.3) |
| **Propósito** | Conservar cada lote en condiciones válidas y mantener un inventario confiable, rotado y auditable. |
| **Resumen** | El caso de uso se inicia cuando un lote ingresa a una cámara desde la Adquisición. El proceso vigila la temperatura y la humedad de la cámara, rota el inventario y anticipa faltantes. El caso de uso finaliza cuando el lote sale del almacén hacia la Dispensación o se da de baja por vencimiento o por ruptura de la cadena de frío. |

| Acción del actor | Respuesta del proceso de negocio |
|---|---|
| *(sin actor: proceso de apoyo)* | **1.** El Almacenista registra la ubicación del lote en su cámara. |
| | **2.** Los sensores de la cámara registran temperatura y humedad cada 5 minutos, y el proceso conserva esas lecturas como evidencia inalterable. *Si la temperatura sale del rango, ver curso alterno de la línea 2.* |
| | **3.** El Farmacéutico clínico revisa la proyección de faltantes a 7 días según las prescripciones programadas. *Si se anticipa un faltante, se origina una Adquisición (CDU-01).* |
| | **4.** El Almacenista rota el inventario: despacha primero los lotes válidos más próximos a vencer. |
| | **5.** El Almacenista da de baja los lotes vencidos; queda registrado quién dio de baja cada uno. |
| | **6.** El lote queda disponible para la Dispensación (CDU-04). |

**CURSOS ALTERNOS**

- **En la línea 2:** **ruptura de la cadena de frío** (escenario del enunciado: de 2 °C a 10 °C durante 15 minutos). El proceso registra el incidente con timestamp exacto, determina qué lotes estaban en la cámara, alerta al Farmacéutico de guardia por SMS y correo, bloquea esos lotes para la dispensación y entrega al Director Administrativo el reporte de pérdida estimada en quetzales. Ver sección *Decidir sobre un lote fuera de temperatura*.

**Prioridad:** Alta.

**Mejoras**

- Evidencia criptográfica de que las lecturas de temperatura no fueron manipuladas (acuerdo de calidad #8).

**Sección: Decidir sobre un lote fuera de temperatura**

1. El Farmacéutico de guardia evalúa físicamente los lotes bloqueados.
2. La política del hospital indica descartarlos.
3. Si el fabricante soporta la exposición (por ejemplo, hasta 30 minutos), el Farmacéutico jefe puede sobrescribir la regla con justificación y firma; la decisión queda auditada.
4. Los lotes se desbloquean o se dan de baja, según la decisión registrada.

### CDU-03 · Prescripción del tratamiento

| Campo | Contenido |
|---|---|
| **Nombre** | Prescripción del tratamiento |
| **Actores** | PACIENTE · SISTEMA LEGACY DE ADMISIONES |
| **Propósito** | Indicar al paciente el MAC adecuado, validado contra protocolo, interacciones, contraindicaciones y disponibilidad real en el inventario del hospital. |
| **Resumen** | El caso de uso se inicia cuando el paciente es evaluado por el médico tratante. El proceso identifica al paciente, selecciona el medicamento y lo valida clínicamente y contra el inventario. El caso de uso finaliza cuando la prescripción validada queda enviada a la farmacia y el paciente recibe la indicación de su tratamiento. |

| Acción del actor | Respuesta del proceso de negocio |
|---|---|
| **1.** El Paciente se presenta a su consulta o está hospitalizado y es evaluado. | |
| | **2.** El Médico tratante solicita la identificación y los datos demográficos del paciente. |
| **3.** El Sistema legacy de admisiones provee la identidad y los datos demográficos del paciente. | |
| | **4.** El Médico tratante selecciona el MAC (dosis, vía de administración y frecuencia) con la sugerencia según el protocolo y su patrón de prescripción. |
| | **5.** La prescripción se valida contra protocolos clínicos, interacciones medicamentosas y contraindicaciones o alergias. *Si no hay alertas, pasar a 6. Si hay alertas, ver curso alterno de la línea 5.* |
| | **6.** Se verifica la disponibilidad del MAC en el inventario del hospital. *Si hay stock, pasar a 7. Si no hay, ver curso alterno de la línea 6.* |
| | **7.** El Médico tratante emite la prescripción, que queda enviada a la Dispensación (CDU-04). |
| **8.** El Paciente recibe la indicación de su tratamiento. | |

**CURSOS ALTERNOS**

- **En la línea 3:** el sistema legacy **no está disponible** (fuera de 7:00-17:00 o lento). Se usa la identidad ya registrada del paciente y la verificación queda pendiente hasta que el legacy responda. Continúa en la línea 4.
- **En la línea 5:** hay alerta de protocolo, interacción o contraindicación. El Médico tratante ajusta la prescripción (volver a 4) o la mantiene con justificación registrada (pasar a 6).
- **En la línea 6:** **no hay stock**. El Médico tratante solicita, desde la misma prescripción, una compra urgente (origina CDU-01) o un reemplazo terapéutico (volver a 4).

**Prioridad:** Alta.

**Mejoras**

- Que el proceso recuerde las preferencias de marca de cada médico, para prescribir en menos de 5 minutos.

**Sección: Acceso de urgencia a diagnóstico sensible**

1. El Médico de urgencias necesita ver un diagnóstico de confidencialidad máxima (VIH, cáncer) de un paciente que no es suyo.
2. Registra la justificación de la emergencia.
3. Accede al diagnóstico; el acceso queda registrado con quién, cuándo y por qué.

### CDU-04 · Dispensación del MAC

| Campo | Contenido |
|---|---|
| **Nombre** | Dispensación del MAC |
| **Actores** | PACIENTE |
| **Propósito** | Asignar nominalmente al paciente un lote válido del inventario del hospital y entregarlo etiquetado para su administración. |
| **Resumen** | El caso de uso se inicia cuando llega a la farmacia una prescripción validada. El proceso verifica disponibilidad, asigna un lote específico, genera su etiqueta y registra la dispensación. El caso de uso finaliza cuando el lote etiquetado queda entregado para su administración y el paciente puede verificar por QR qué se le asignó. |

| Acción del actor | Respuesta del proceso de negocio |
|---|---|
| | **1.** El Farmacéutico clínico recibe la orden de dispensación. *Si no puede dispensar a tiempo en una urgencia, ver curso alterno de la línea 1.* |
| | **2.** El Farmacéutico clínico verifica la disponibilidad en el inventario del hospital (no en farmacia externa). |
| | **3.** El Farmacéutico clínico asigna un lote específico al paciente. |
| | **4.** El Farmacéutico clínico genera la etiqueta con código de barras/QR del lote asignado. |
| | **5.** Para oncológicos y opioides, el Farmacéutico clínico registra su parte del doble registro, que deberá coincidir con el del Enfermero de piso. |
| | **6.** El Farmacéutico clínico entrega el medicamento etiquetado a enfermería. |
| **7.** El Paciente puede escanear el código QR y verificar que el medicamento y la dosis asignados son los correctos. | |

**CURSOS ALTERNOS**

- **En la línea 1:** urgencia con el farmacéutico ocupado (escenario del sábado 6:00 PM). Ver sección *Dispensación de urgencia*.
- **En la línea 2:** **la farmacia pierde la conexión** (Wi-Fi inestable del sótano). La dispensación continúa con el inventario local de la farmacia y se concilia automáticamente cuando la conexión regresa, sin duplicar registros. Continúa en la línea 3.

**Prioridad:** Alta.

**Mejoras**

- Proyección de faltantes visible en la misma pantalla de dispensación.

**Sección: Dispensación de urgencia**

1. **Opción A:** el Enfermero de piso toma el medicamento de la gaveta de *dispensación inmediata* y lo escanea; queda registrado quién lo tomó y por qué.
2. **Opción B:** se autoriza el préstamo del medicamento de otro paciente que lo tiene prescrito para el día siguiente, y se genera la notificación para reponerlo antes de que ese paciente lo necesite.
3. **Opción C:** se reserva el lote (dispensación virtual) sin retiro físico inmediato; el Farmacéutico clínico valida la entrega física dentro de las 12 horas siguientes.

### CDU-05 · Administración del MAC al paciente

| Campo | Contenido |
|---|---|
| **Nombre** | Administración del MAC al paciente |
| **Actores** | PACIENTE |
| **Propósito** | Aplicar el medicamento correcto al paciente correcto, con registro completo y trazable del acto. |
| **Resumen** | El caso de uso se inicia cuando el enfermero va a aplicar una dosis dispensada. El proceso identifica al paciente, al medicamento y al enfermero, valida que coincidan y registra la aplicación. El caso de uso finaliza cuando el paciente recibió el medicamento y la administración quedó registrada. |

| Acción del actor | Respuesta del proceso de negocio |
|---|---|
| | **1.** El Enfermero de piso escanea la pulsera del paciente. |
| | **2.** El Enfermero de piso escanea el código de barras del medicamento dispensado. |
| | **3.** El Enfermero de piso se autentica con su credencial biométrica en la tablet. |
| | **4.** Se valida que paciente y medicamento coinciden, en menos de 500 ms. *Si coinciden, pasar a 5. Si no, ver curso alterno de la línea 4.* |
| | **5.** Para oncológicos y opioides, el registro del Enfermero de piso se compara con el del Farmacéutico clínico. *Si la discrepancia supera los 5 minutos, se activa una alerta de seguridad.* |
| | **6.** El Enfermero de piso aplica el medicamento. |
| **7.** El Paciente recibe el medicamento. | |
| | **8.** El Enfermero de piso registra hora, fecha, sitio de aplicación y reacciones adversas inmediatas, por dictado de voz si es necesario. *Si hay reacción adversa, se origina el Seguimiento (CDU-06).* |

**CURSOS ALTERNOS**

- **En la línea 1 o 2:** **el escáner falla** (5 % de lecturas). El Enfermero de piso ingresa el código manualmente. Continúa en la línea siguiente.
- **En la línea 4:** paciente y medicamento **no coinciden** (escenario del metotrexato, cama 302 vs. 304). El proceso muestra la alerta de ALTO y el Enfermero de piso detiene la administración. Fin del caso de uso.
- **En la línea 6:** **no hay conexión**. La administración se registra offline y la trazabilidad se concilia automáticamente al volver la conexión, sin duplicar registros. Continúa en la línea 7.

**Prioridad:** Alta.

**Mejoras**

- Registro de reacciones adversas por voz a texto: escribir en la tablet con el paciente en shock es inviable.

### CDU-06 · Seguimiento y farmacovigilancia

| Campo | Contenido |
|---|---|
| **Nombre** | Seguimiento y farmacovigilancia |
| **Actores** | PACIENTE · MSPAS |
| **Propósito** | Vigilar la respuesta del paciente al tratamiento, ajustar la dosis y cumplir con el reporte obligatorio de efectos adversos. |
| **Resumen** | El caso de uso se inicia cuando se registra un efecto adverso o llega un control de seguimiento del paciente. El proceso notifica al médico, analiza el caso, cruza reportes del mismo lote y genera el reporte oficial. El caso de uso finaliza cuando el MSPAS recibe el reporte y el paciente tiene su tratamiento ajustado. |

| Acción del actor | Respuesta del proceso de negocio |
|---|---|
| **1.** El Paciente presenta o reporta un efecto adverso en los días posteriores a la administración. | |
| | **2.** El Enfermero de piso o el Médico tratante registra el efecto adverso. |
| | **3.** El Médico tratante es notificado, evalúa al paciente y ajusta la dosis según la respuesta. |
| | **4.** El Jefe de Farmacovigilancia analiza el caso y lo cruza con otros reportes del mismo lote. *Si detecta un patrón, ver curso alterno de la línea 4.* |
| | **5.** El Jefe de Farmacovigilancia genera el reporte en el formato XML con la DTD definida por el MSPAS, dentro de las 24 horas. |
| **6.** El MSPAS recibe el reporte en su sistema nacional de farmacovigilancia. | |
| **7.** El Paciente recibe el aviso de su próxima dosis por SMS o WhatsApp. | |

**CURSOS ALTERNOS**

- **En la línea 4:** **patrón de efectos adversos** (por ejemplo, 5 pacientes del mismo lote con náuseas) o **alerta nacional** del MSPAS. Se genera una alerta temprana y el lote se bloquea en el almacén (CDU-02).
- **En la línea 6:** el sistema nacional **no está recibiendo** (solo recibe de 8:00 a 16:00; el incidente fue a las 19:30). El reporte queda registrado con su fecha y hora, lo que cumple el plazo legal, y se entrega al abrirse la ventana. Continúa en la línea 7.

**Prioridad:** Alta.

**Mejoras**

- Exportación en HL7 FHIR para compartir con otros hospitales.

### CDU-07 · Control y auditoría de la gestión de MAC

| Campo | Contenido |
|---|---|
| **Nombre** | Control y auditoría de la gestión de MAC |
| **Actores** | CONTRALORÍA GENERAL DE CUENTAS |
| **Propósito** | Dar transparencia financiera y trazabilidad forense completa de cada lote, sobre registros que nadie puede alterar. |
| **Resumen** | El caso de uso se inicia cuando la Contraloría General de Cuentas solicita, sin previo aviso, la trazabilidad de un lote. El proceso reúne el historial inmutable del lote desde la compra hasta la administración. El caso de uso finaliza cuando la Contraloría recibe el informe forense, en menos de 10 minutos. |

| Acción del actor | Respuesta del proceso de negocio |
|---|---|
| **1.** La Contraloría General de Cuentas solicita la trazabilidad completa de un lote. | |
| | **2.** El Director Administrativo solicita el informe forense del lote. |
| | **3.** El proceso reúne del historial inmutable: fecha de compra, proveedor y factura; ingreso al almacén y temperaturas; pacientes a los que se administró; hora, fecha, enfermero y médico; devoluciones, caducidades y ajustes. *Si algún registro no pasa la verificación de integridad, ver curso alterno de la línea 3.* |
| | **4.** El Director Administrativo revisa y entrega el informe forense, en menos de 10 minutos. |
| **5.** La Contraloría General de Cuentas recibe el informe forense. | |

**CURSOS ALTERNOS**

- **En la línea 3:** un registro **no coincide** con su huella de integridad. El informe lo marca como evidencia de manipulación y se entrega igual, con la anomalía declarada.

**Prioridad:** Alta.

**Mejoras**

- Tablero de control del Director Administrativo: costo por paciente, por servicio y % de desperdicio, con quién autorizó cada compra y quién dio de baja cada lote vencido.

---

## 5. Selección del estilo arquitectónico y su justificación  ·  criterio 5 — 10 pts

### 5.1 La decisión, en una línea

> **Arquitectura orientada a servicios (SOA)** con **un servicio de negocio por proceso** (CDU-01 a
> CDU-07), **cada servicio organizado en capas**, comunicación de **llamada y retorno** para lo que
> exige respuesta inmediata y **basada en eventos** (bus) para lo asíncrono, clientes
> **cliente-servidor offline-first**, y un **pipeline de tuberías y filtros** para la telemetría de
> las cámaras.

Un sistema real no es de un solo estilo: el estilo **principal** fija la estructura (SOA) y los
**complementarios** resuelven drivers concretos donde el principal no alcanza. Taxonomía usada: la
**lista de 9 estilos** y las **familias** de clase (árbol C&C). Ver [[Estilos arquitectónicos]] y
[[Catálogo de estilos arquitectónicos]].

### 5.2 Por qué SOA — la definición de clase aplicada al caso

La lámina *"Funcionamiento de la Arquitectura (SOA)"* (captura 35) describe **cuatro escalones**, y
FarmaHosp los cumple uno por uno:

| Escalón de la clase | Texto de la lámina | En FarmaHosp | Driver que lo exige |
|---|---|---|---|
| 1. Definición | *"Define las necesidades del negocio"* | Los 7 procesos del caso de negocio (CDU-01..07) y los 37 RF | criterio 1 y 3 |
| 2. Desarrollo | *"Desarrolla procesos de negocio como Servicios"* | **Un servicio por proceso**: Adquisición, Almacenamiento e Inventario, Prescripción, Dispensación, Administración, Farmacovigilancia, Auditoría y Tablero | `RE-05` |
| 3. Evolución | *"Permite que cada Servicio evolucione independientemente"* | Farmacovigilancia tiene **otro ciclo de entregas** que inventario; se entrega por incrementos: dispensación y almacén → prescripción → farmacovigilancia | `RE-05` · `RE-18` · `AC-07` |
| 4. Distribución | *"Plantea aplicaciones distribuidas, multi-nivel"* | Clientes (Toughpad, farmacia, portal) → acceso → servicios → datos, repartidos en nodos | `AC-05` · `AC-02` |

Y la definición conceptual (captura 33): *"un servicio (cliente) realiza una solicitud (llamada) a otro
servicio (proveedor) y espera una respuesta (retorno)"*. SOA además es **de dos familias**:
*"Es event-based porque puede usar motores de orquestación/coreografía e invocar servicios de forma
asíncrona"* (captura 34). Esa doble pertenencia es exactamente lo que FarmaHosp necesita: validar al
paciente **ya** (síncrono) y reportar al MSPAS **cuando abra la ventana** (asíncrono).

### 5.3 Los estilos complementarios — cada uno con su driver

| Estilo (familia de clase) | Dónde se aplica | Driver que resuelve | Por qué este y no otro |
|---|---|---|---|
| **En capas** (llamada y retorno) | **Dentro de cada servicio**: capa de API (controlador REST), capa de lógica de negocio, capa de acceso a datos | `AC-07` mantenibilidad | Es la estructura que el equipo interno ya conoce (Spring Boot); la clase: *"Soporta fácilmente la evolución del sistema, los cambios sólo afectan a las capas vecinas"* |
| **Llamada y retorno** (REST síncrono) | Validación paciente-medicamento, consulta de inventario, autenticación | `AC-01` < 500 ms · `RF-14` · `RF-24` | Hace falta la respuesta **antes** de seguir: *"Interacción por invocación síncrona"* (captura 30) |
| **Basada en eventos** (bus de eventos) | Reportes al MSPAS, notificaciones, sincronización offline, ruptura de cadena de frío, absorción del pico | `AC-05` pico 10x · `AC-06` legacy y MSPAS · `RF-07` · `RF-29` | El emisor **no espera**: la cola absorbe el pico y guarda lo que no puede entregarse (MSPAS solo recibe de 8 a 16) |
| **Cliente-servidor offline-first** | App de enfermería en la Toughpad y app de farmacia, con base local y bandeja de sincronización | `AC-02` offline ≥ 4 h · `RE-16` Wi-Fi inestable · `RF-26` | El cliente guarda y opera solo; al volver la red **reconcilia con identificador único** y el servidor descarta duplicados |
| **Tuberías y filtros** (flujo de datos) | Telemetría de cámaras: *recibir → validar → sellar con hash encadenado → detectar ruptura → publicar evento* | `AC-08` integridad · `RF-05` · `RF-06` · 500,000 lecturas/día | *"Adecuada para sistemas con transformaciones de datos en pasos sucesivos"* (captura 15); cada filtro se cambia sin tocar los demás |

### 5.4 Los estilos descartados — tan importante como el elegido

| Estilo de la lista de clase | ¿Por qué no? | Evidencia |
|---|---|---|
| **Monolítico** | **Prohibido** | `RE-05`: *"No se puede diseñar un sistema monolítico, porque el módulo de farmacovigilancia tiene ciclos de entrega diferentes…"* |
| **Microservicios** | Demasiada granularidad para **3 personas** de TI y **32 vCPU sin autoescalado**: cada microservicio suma despliegue, monitoreo y base propia | `AC-07` · `RE-13` · `RE-17` · `STK-08` |
| **Peer to peer** | Sin un centro no hay **una sola verdad auditable** ni inventario con consistencia fuerte | `AC-03` · `RE-01` (ACID en inventario) |
| **Microkernel** | No hay un núcleo estable con extensiones enchufables: hay siete procesos con el mismo peso | — |
| **Monolito en capas puro** | Capas sin servicios sigue siendo un despliegue único | `RE-05` |
| **REST como estilo único** | Se usa REST como **protocolo** de la llamada y retorno, pero no resuelve la asincronía | `AC-06` · `RF-29` |

### 5.5 Cómo atiende la arquitectura a los 5 drivers más críticos

| # | Driver (top 5 de §3.4) | Táctica arquitectónica | Dónde se ve en §6 |
|---|---|---|---|
| 1 | `AC-02` offline ≥ 4 h sin duplicar | Base local cifrada en la Toughpad y en la farmacia + **bandeja de salida** con **identificador único generado en el cliente**; el Servicio de Sincronización reconcilia de forma **idempotente** (la misma operación dos veces se guarda una) | Bloques: *Sincronización offline*. Despliegue: *BD local* en Toughpad y estación de farmacia |
| 2 | `AC-01` validación < 500 ms / < 2 s | La Toughpad descarga al inicio del turno las **administraciones programadas** de sus pacientes: la validación se hace **localmente**, sin viajar por la red; en línea se confirma contra la **caché** | Despliegue: *Validación local* en Toughpad y *Caché* en el data center |
| 3 | `AC-05` pico 10x con presupuesto fijo | **Dos instancias** de cada servicio tras un **balanceador**, **caché** de lecturas, **bus** que absorbe las escrituras no críticas, **prioridad de tráfico** para dispensación y administración, y la **réplica del sitio alterno** para informes y tablero | Bloques: *Acceso* y *Bus*. Despliegue: VM-03/04, VM-09 |
| 4 | `AC-07` mantenible por el equipo interno | Stack que el interno ya domina: **Java + Spring Boot + Angular**; **PostgreSQL** en lugar de Oracle (open source, ACID, su PL/pgSQL es cercano a PL/SQL y es lo que prefiere la consultora); la **misma plantilla de capas** en los 7 servicios; contratos **OpenAPI** como documentación viva | §5.6 |
| 5 | `AC-03` inmutabilidad y trazabilidad total | **Bitácora de eventos de solo inserción** (sin UPDATE ni DELETE, ni para el administrador) con **hash encadenado**; el informe forense se arma sobre la **réplica** para no degradar la operación | Bloques: *Bitácora inmutable*. Despliegue: VM-10 y sitio alterno |

Los que no entraron al top 5 también se atienden: `AC-04` ABAC en el **Servicio de Identidad y
Acceso** con caché de decisiones; `AC-06` **adaptadores de integración** con cola (*guardar y
reenviar*) y copia nocturna de pacientes del legacy; `AC-08` filtro *Sellar* del pipeline de
telemetría.

### 5.6 Stack tecnológico — lo decide el conflicto `STK-08` vs `STK-09`

| Pieza | Elección | Restricción o driver | Descartado y por qué |
|---|---|---|---|
| Lenguaje y framework de servicios | **Java 17 + Spring Boot 3** | `RE-17` · `AC-07` (el interno sabe Java 8 y Spring Boot) | Python/Django: el interno no lo puede mantener solo |
| Base de datos | **PostgreSQL 16** (primaria + réplica en sitio alterno) | `RE-01` ACID · `RE-03` sin licencias | Oracle Enterprise: `RE-03` · MongoDB: sin ACID multi-documento para inventario (`RE-01`) y fuera del perfil del interno |
| Web | **Angular** | `AC-07` | React: el interno no lo conoce |
| App de enfermería | **Android nativa** (Java/Kotlin) con **SQLite cifrado** | `RE-14` Android 9, 3 GB · `RE-04` Toughpad · `RE-07` ≤ 2 h de capacitación | Frameworks multiplataforma pesados: 3 GB de RAM |
| Bus de eventos | **RabbitMQ** | `AC-05` · `AC-06` · `RE-03` | Kafka: lo conoce la consultora, pero su operación es excesiva para 3 personas y para ~6 lecturas de sensor por segundo |
| Caché | **Redis** | `AC-01` · `AC-05` | — |
| Identidad | **Keycloak** (federado con LDAP + OTP por SMS de respaldo) | `RE-08` sin punto único de falla · `RE-06` sin texto plano · `AC-04` | Autenticar solo contra LDAP: `RE-08` |
| Balanceo y prioridad de tráfico | **Nginx** | `AC-05` · entorno: 50 Mbps compartidos | — |
| Observabilidad | **Prometheus + Grafana** | `STK-13` | — |

**Todo es open source** (`RE-03`) y **todo lo sensible reside en el data center local** (`RE-02`); a
la nube pública solo sale el **análisis estadístico con datos anonimizados**.

---

## 6. Diagrama de bloques y de despliegue  ·  criterio 6 — 30 pts

Dos láminas, en el orden de la clase: **primero el alto nivel, después el detalle** — *"Suele ser el
primer paso antes de un diseño más detallado (ej. con diagramas de componentes)"* (captura 13). Ver
[[Diagrama de bloques de alto nivel]], [[Diagrama de componentes]] y [[Diagrama de despliegue]].

| # | Lámina | Qué responde | Archivo |
|---|---|---|---|
| 6.1 | **Diagrama de bloques** | ¿Cuáles son las partes grandes, cómo se conectan y qué fluye entre ellas? | `02-Diagramas/6-bloques-despliegue/bloques-farmahosp.svg` |
| 6.2 | **Componentes** (tabla) | ¿De qué piezas de software está hecho y qué interfaces ofrece cada una? | tabla de §6.2; dibujados **dentro de los nodos** de 6.3 |
| 6.3 | **Diagrama de despliegue** | ¿En qué hardware corre cada pieza y por qué red se hablan? | `02-Diagramas/6-bloques-despliegue/despliegue-farmahosp.svg` |

*(La rúbrica pide bloques y despliegue. Los componentes se dibujan **dentro de los nodos** del
despliegue, como en el ejemplo del parque: *"Diagrama de Despliegue Incluye: • Componentes •
Distribución"* (captura 57). La tabla de §6.2 define sus interfaces. Un diagrama de componentes
separado, con piruletas y dependencias, queda como **mejora opcional**: ver el tablero.)*

### 6.1 Diagrama de bloques de alto nivel

**Definición de clase aplicada:** *"representación del funcionamiento de un sistema, que se hace
mediante bloques y sus relaciones, y que, además, definen la organización de todo el proceso interno,
sus entradas y sus salidas"* (captura 14). Por eso la lámina se lee de **izquierda (entradas) a
derecha (salidas)** y **todas las flechas llevan nombre** con lo que fluye.

**Bloques, por banda:**

| Banda | Bloque | Responsabilidad | Traza |
|---|---|---|---|
| **Entradas** | Enfermería (Toughpad + escáner Bluetooth) | Administrar y validar offline | `RF-23..27` · `RE-04` · `RE-14` · `RE-15` |
| | Farmacia (estación offline, sótano) | Dispensar aunque falle el Wi-Fi | `RF-17..22` · `RE-16` |
| | Portal clínico y administrativo | Prescribir, farmacovigilancia, tablero | `RF-10..16` · `RF-28..35` |
| | Paciente (consulta QR) | Verificar su medicamento | `RF-32` |
| | Sensores IoT de cámaras (vía gateway) | Lecturas cada 5 min | `RF-05` |
| **Acceso** | Balanceador y API Gateway | Reparte carga, prioriza dispensación y administración | `AC-05` |
| | Identidad y acceso | LDAP + OTP de respaldo, ABAC | `RE-08` · `AC-04` · `RE-12` |
| **Servicios de negocio (SOA)** | Adquisición · Almacenamiento e Inventario · Prescripción · Dispensación · Administración · Farmacovigilancia · Auditoría y Tablero | Un servicio por proceso CDU-01..07, cada uno en capas | `RE-05` · `AC-07` |
| **Servicios de soporte** | Sincronización offline | Reconciliación idempotente | `AC-02` · `RF-26` |
| | Pipeline de telemetría (tuberías y filtros) | Recibir → validar → sellar → detectar → publicar | `AC-08` · `RF-05` · `RF-06` |
| | Integración | Adaptadores legacy SOAP, MSPAS XML/DTD, HL7 FHIR | `AC-06` · `RF-29` · `RF-37` |
| | Notificaciones | SMS, WhatsApp, correo | `RF-07` · `RF-31` |
| **Bus de eventos** | — | Desacopla y absorbe picos | `AC-05` · `AC-06` |
| **Datos** | Base transaccional PostgreSQL | Inventario ACID | `RE-01` |
| | Bitácora inmutable | Solo inserción + hash encadenado | `AC-03` · `AC-08` |
| | Caché | Lecturas rápidas | `AC-01` · `AC-05` |
| | Réplica en sitio alterno | Respaldo y lecturas de informes | escenario de caída · `RF-33` |
| **Salidas (externos)** | Legacy de admisiones · Sistema nacional MSPAS · LDAP · Pasarela SMS/WhatsApp · Nube (solo anonimizado) | — | `AC-06` · `RE-02` · `RE-08` |

![[02-Diagramas/6-bloques-despliegue/bloques-farmahosp.svg]]

### 6.2 Los componentes y sus interfaces

**Definición de clase aplicada:** un componente es *"una unidad software que puede ser reemplazada y
actualizada de forma independiente"* y se define *"en términos de los servicios que ofrecen (interfaces
de salida) y los servicios que requieren"* (PDF Tema 5). Notación de la clase: interfaz **provista =
círculo**, dependencia **punteada** del que usa hacia la interfaz (capturas 35, 36 y 57).

**Componentes y sus interfaces provistas:**

| Componente | Interfaz provista | La usan | Traza |
|---|---|---|---|
| `SvcAdquisicion` | `IOrdenCompra` | `SvcInventario` (faltantes), `SvcPrescripcion` (compra urgente) | `RF-01..04` |
| `SvcInventario` | `IInventario` | `SvcPrescripcion`, `SvcDispensacion` | `RF-05..09` · `RF-14` · `RE-01` |
| `SvcPrescripcion` | `IPrescripcion` | `SvcDispensacion` | `RF-10..16` |
| `SvcDispensacion` | `IDispensacion` | `SvcAdministracion` (doble registro) | `RF-17..22` |
| `SvcAdministracion` | `IAdministracion` | `AppEnfermeria` | `RF-23..27` |
| `SvcFarmacovigilancia` | `IFarmacovigilancia` | `SvcAdministracion` (reacción adversa) | `RF-28..32` |
| `SvcAuditoria` | `IAuditoria` | `PortalWeb` | `RF-33..37` |
| `SvcSincronizacion` | `ISincronizacion` | `AppEnfermeria`, `AppFarmacia` | `AC-02` · `RF-26` |
| `SvcIdentidad` | `IAutenticacion` · `IAutorizacion` | todos los clientes y servicios | `RE-08` · `AC-04` |
| `SvcIntegracion` | `IAdmisiones` · `IReporteMSPAS` | `SvcPrescripcion`, `SvcFarmacovigilancia` | `AC-06` · `RF-29` · `RF-37` |
| `SvcNotificacion` | `INotificacion` | `SvcInventario`, `SvcFarmacovigilancia` | `RF-07` · `RF-31` |
| `PipelineTelemetria` | `ILectura` | `GatewayIoT` | `RF-05` · `AC-08` |
| `BitacoraInmutable` | `IRegistroEvento` | todos los servicios de negocio | `AC-03` |


### 6.3 Diagrama de despliegue

**Definición de clase aplicada:** *"Se utilizará para representar la arquitectura física sobre la que
un sistema software es desplegado. Por tanto, describe tanto dispositivos hardware como software"* (PDF
Tema 5). Notación: **nodo = cubo**, `«device»` para hardware, `«executionEnvironment»` para software
**siempre dentro de un dispositivo** — una **máquina virtual** es el ejemplo del propio PDF —,
componentes dentro del nodo, **conexión = línea llena** con el protocolo como estereotipo, y las zonas
**FrontEnd / BackEnd** como en la captura 58.

**Nodos de hardware y lo que corre en cada uno:**

| Nodo | Tipo | Contiene | Conexión | Traza |
|---|---|---|---|---|
| **Toughpad Panasonic** (Android 9, 3 GB, 32 GB) | `«device»` → `«executionEnvironment» Android 9` | App de Enfermería · Validación local · BD local cifrada (SQLite) · Bandeja de sincronización | `«wifi / HTTPS»` al data center · `«Bluetooth»` al escáner | `RE-04` · `RE-14` · `AC-01` · `AC-02` |
| **Escáner de código de barras** | `«device»` | — (entrada manual de respaldo en la app) | `«Bluetooth»` | `RE-15` · `RF-25` |
| **Estación de farmacia** (PC del sótano) | `«device»` → `«executionEnvironment» Navegador` | App de Farmacia offline · BD local (IndexedDB) · Bandeja de sincronización | `«wifi inestable / HTTPS»` · `«USB»` a impresora | `RE-16` · `AC-02` |
| **Impresora de etiquetas** | `«device»` | — | `«USB»` | `RF-18` |
| **PC clínica y administrativa** | `«device»` → `«executionEnvironment» Navegador` | Portal web (Angular) | `«Ethernet 1 Gbps / HTTPS»` | `RF-10..16` · `RF-28..35` |
| **Smartphone del paciente** | `«device»` → `«executionEnvironment» Navegador` | Consulta QR | `«Internet / HTTPS»` | `RF-32` |
| **Sensores IoT** (cada cámara) | `«device»` | — | `«MQTT»` al gateway | `RF-05` |
| **Gateway IoT** | `«device»` | Buffer local (guardar y reenviar) | `«MQTT / TLS»` al data center | `AC-08` · escenario de caída |
| **Servidor de virtualización VMware** — data center principal (32 vCPU / 128 GB / SAN 10 TB) | `«device»` con 11 `«executionEnvironment»` (VM-01 a VM-11) | ver tabla de VMs | — | `RE-13` |
| **Servidor de respaldo** — sitio alterno (la *"réplica en otra ubicación"* del enunciado) | `«device»` → VM | PostgreSQL réplica (lectura para informes y tablero) · Servicios en espera | `«replicación en streaming / TCP»` | escenario de caída · `RF-33` |
| **Servidor legacy de admisiones** | `«device»` externo | COBOL con interfaz SOAP | `«SOAP / HTTPS»` | `AC-06` |
| **Sistema nacional de farmacovigilancia** (MSPAS) | `«device»` externo | Recepción XML/DTD, 8:00-16:00 | `«Internet / HTTPS»` | `RE-09` · `RF-29` |
| **Directorio activo (LDAP)** | `«device»` | — | `«LDAPS»` | `RE-08` |
| **Pasarela SMS / WhatsApp** | `«device»` externo | — | `«Internet / HTTPS»` | `RF-07` · `RF-31` · OTP de `RE-08` |
| **Nube pública** | `«device»` externo | Analítica estadística **anonimizada** | `«Internet / HTTPS»` | `RE-02` · `RF-36` |

**Las máquinas virtuales del data center — la prueba de que cabe en el hardware fijo (`RE-13`):**

| VM | Qué corre | vCPU | RAM | Por qué |
|---|---|---|---|---|
| VM-01, VM-02 | Balanceador y API Gateway (Nginx) | 1 + 1 | 2 + 2 GB | `AC-05` · sin punto único de falla |
| VM-03, VM-04 | Servidor de aplicaciones (JRE 17): los **7 servicios de negocio + Sincronización** | 5 + 5 | 14 + 14 GB | `AC-05`: dos instancias de cada servicio |
| VM-05, VM-06 | Identidad y acceso (Keycloak + ABAC) | 1 + 1 | 4 + 4 GB | `RE-08`: sin punto único de falla |
| VM-07, VM-08 | Integración y eventos: RabbitMQ, Integración, Notificaciones, Pipeline de telemetría | 2 + 2 | 8 + 8 GB | `AC-06` · `AC-05` |
| VM-09 | Caché (Redis) | 1 | 8 GB | `AC-01` · `AC-05` |
| VM-10 | PostgreSQL primaria + Bitácora inmutable | 8 | 48 GB | `RE-01` · `AC-03` |
| VM-11 | Observabilidad (Prometheus + Grafana) | 1 | 4 GB | `STK-13` |
| **Total** | | **28 de 32** | **116 de 128 GB** | queda margen para el hipervisor |

> [!warning] Por qué la réplica de lectura NO está en el data center principal
> La SAN tiene **10 TB** y el enunciado estima **5 TB de datos + 2 TB de logs + 100 GB de imágenes**
> el primer año: **7.1 TB**. Una réplica completa en la misma SAN sumaría otros 5 TB — **no cabe**.
> Por eso las lecturas pesadas (informe forense `RF-33`, tablero `RF-34`) van contra la **réplica del
> sitio alterno**, que el enunciado ya da por existente. El pico del lunes no depende de esa réplica:
> lo absorben la caché, el bus y las dos instancias.

> [!note] Supuestos declarados (el enunciado no los da)
> - Existe un enlace de red entre el data center principal y el sitio alterno.
> - Los PCs de la farmacia, del personal clínico y administrativo, y la impresora de etiquetas ya existen.
> - El gateway IoT es parte del equipamiento de las cámaras con sensores.

![[02-Diagramas/6-bloques-despliegue/despliegue-farmahosp.svg]]

### 6.4 Cómo se comporta en los escenarios críticos del enunciado

La prueba de que la arquitectura **no es decorativa**: cada escenario, recorrido sobre los nodos.

| Escenario del enunciado | Qué pasa en la arquitectura |
|---|---|
| **La cadena de frío se rompe** (3:00 AM) | Sensores → Gateway IoT → Pipeline de telemetría: *sellar* guarda la lectura con hash, *detectar* ve la ruptura y *publica* el evento → Inventario bloquea los lotes, Notificaciones envía SMS y correo, Auditoría calcula la pérdida |
| **Urgencia oncológica** (sábado 6:00 PM) | Dispensación ofrece las opciones A/B/C; cada una se registra en la Bitácora inmutable con quién y por qué |
| **Error de medicación** (cama 302/304) | La validación ocurre **en la Toughpad** contra las administraciones programadas del turno: < 500 ms sin depender de la red |
| **Auditoría de la Contraloría** | Auditoría consulta la Bitácora inmutable sobre la réplica del sitio alterno: informe < 10 min sin frenar la operación |
| **Caída del servidor central** (lunes 8:30) | Toughpads y farmacia **siguen operando offline**; el gateway guarda las lecturas; al volver, Sincronización concilia sin duplicar. El balanceador reparte entre VM-03 y VM-04 para evitar el colapso |
| **Farmacovigilancia** (19:30, MSPAS cerrado) | El reporte se registra con fecha y hora y queda en la cola del bus; Integración lo entrega a las 8:00 |

### Checklist del criterio 6

- [x] Diagrama de bloques: entradas arriba, salidas a la derecha, **todas las flechas con nombre**
- [x] Despliegue: cubos, `«device»` / `«executionEnvironment»` **dentro** de un dispositivo, componentes adentro del nodo
- [x] Toda conexión con **protocolo** como estereotipo
- [x] FrontEnd y BackEnd marcados (y los sistemas externos aparte)
- [x] **Cada nodo y cada componente trazan a un RF, AC o RE** (tablas de §6.1 y §6.3, captura 42)
- [x] Las cuentas de hardware cierran: 28/32 vCPU, 116/128 GB, 7.1/10 TB
- [x] Los dos diagramas y las tablas usan **los mismos nombres**
- [x] Paso 4 del checklist de `estilo-diagramas.md`: las dos láminas **se miraron** (capturas `-verificacion.png`) y se corrigieron los cruces
