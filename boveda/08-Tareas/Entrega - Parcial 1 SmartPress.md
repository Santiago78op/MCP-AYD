---
tema: Primer Parcial — Drivers arquitectónicos y vistas 4+1
fuente: "Primer Parcial. Producción.pdf — Caso SmartPress (AutoParts Guatemala S.A.)"
fecha: 2026-08-22
---

# Primer Parcial — "SmartPress": Sistema de Control de Calidad en Línea de Producción

## 0. Frontera y convenios (declarados antes de responder)

| Punto | Decisión |
|---|---|
| **Frontera del negocio** | Se modela la **gestión del control de calidad en línea de la producción de piezas de precisión**. NO se modela la planta completa: quedan fuera ventas, finanzas, RRHH, compras y la operación del ERP. |
| **Actor vs. trabajador** | Las **áreas y los sistemas externos** son actores de negocio. Las **personas** (operario, supervisor de turno, ingeniero de calidad, director de planta, equipo de TI, científico de datos) son **trabajadores del negocio** y aparecen como actores solo en el plano del **sistema** (CDU expandidos). |
| **Identificadores** | Se usa la convención de la **NT1**: `RFG-0nn` (requerimiento funcional), `CUN-0n` (caso de uso de negocio), `CU-0nn` (caso de uso del sistema), `AC-0n` (atributo de calidad), `RES-x0n` (restricción). Una sola convención en todo el documento. |
| **Taxonomía de calidad** | Se usa la lista de clase de **siete** atributos (rendimiento, escalabilidad, disponibilidad, seguridad, mantenibilidad, usabilidad, fiabilidad). No se mezcla con ISO 9126 ni FURPS. |
| **Clasificación de restricciones** | Se usan **las tres categorías que pide el enunciado** (Técnicas / de Negocio / de Sistema), no las seis de clase. |
| **Planos** | §1 (core y descomposición) está en **plano de negocio** (estereotipos `«actor de negocio»` / `«caso de uso de negocio»`). §2 (CDU expandidos) está en **plano de sistema**, sin estereotipos de negocio. No se mezclan. |
| **Asunción declarada** | El enunciado no nombra explícitamente al proveedor de materia prima ni al ente certificador como interlocutores, pero la etapa 1 ("certificado de calidad del proveedor") y las normas ISO 9001 / IATF 16949 los hacen necesarios: se asumen **actores de negocio**. |

---

# PARTE I — Descubriendo los Drivers Arquitectónicos (40 pts)

## 1. Core del negocio y primera descomposición (20 pts)

### 1.0 Diagrama de contexto — la frontera dibujada

![[02-Diagramas/examen/2-caso-negocio/contexto-smartpress.png]]
`boveda/02-Diagramas/examen/2-caso-negocio/contexto-smartpress.png`

Convenios de clase: **elipse = El Producto** (un solo óvalo, nombra un **sistema**) · **rectángulo = entidad o agente externo** · **flecha = *streamline*, siempre con nombre y en sustantivo**. A diferencia del CDU, aquí las flechas **sí son flujos de información**, no navegabilidad.

| Entidad / agente | Streamline de entrada | Streamline de salida |
|---|---|---|
| Proveedor de materia prima | Certificado de calidad del lote | — |
| Sistema de Control de Máquina (PLC) | Mediciones de sensores (OPC-UA) | Orden de ajuste de parámetros |
| Sistema de medición láser (CMM) | Resultados de inspección dimensional | — |
| Sistemas legacy (ERP / Mantenimiento) | Órdenes de producción y programación | — |
| Área de Mantenimiento | — | Aviso de deriva de sensor |
| Operario de máquina | — | Alerta de desviación en tiempo real |
| Supervisor de turno | — | Tablero de desempeño del turno |
| Ingeniero de Calidad | Configuración del modelo predictivo | Datos históricos de proceso |
| Director de Planta | — | Indicadores de calidad y costo de scrap |
| Cliente (ensambladora automotriz) | — | Expediente de trazabilidad de la pieza |
| Ente certificador (ISO 9001 / IATF 16949) | — | Registro de auditoría inmutable |

> **Cambio de lente, declarado:** en el contexto se dibuja el **producto de software**, así que aparecen las **personas** (operario, supervisor, ingeniero, director) como agentes externos al software. En el core y la descomposición (§1.1 y §1.2) el lente es el **negocio**, y esas mismas personas pasan a ser **trabajadores del negocio**: no son actores ahí. No es una contradicción, son dos planos distintos.

### 1.1 Core del negocio — CDU de negocio de alto nivel

![[02-Diagramas/examen/2-caso-negocio/core-negocio-smartpress.png]]
`boveda/02-Diagramas/examen/2-caso-negocio/core-negocio-smartpress.png`

**Un solo caso de uso de negocio**, con el nombre del negocio completo:

> **«caso de uso de negocio» Gestión del Control de Calidad en Línea de la Producción de Piezas de Precisión (SmartPress)**

**Actores de negocio (7):**

| ID | Actor de negocio | Por qué es actor (interactúa con el negocio en operación) |
|---|---|---|
| A-01 | Proveedor de materia prima | Entrega cada lote con su certificado de calidad (etapa 1). |
| A-02 | Área de Producción | Opera las 25 máquinas; es la fuente del proceso que se controla. |
| A-03 | Sistema de Control de Máquina (PLC) | Entidad externa automatizada: emite mediciones vía OPC-UA y recibe órdenes de ajuste. |
| A-04 | Área de Mantenimiento | Calibra sensores y atiende la deriva detectada. |
| A-05 | Cliente (ensambladora automotriz) | Recibe las piezas y exige trazabilidad digital verificable. |
| A-06 | Ente certificador (ISO 9001 / IATF 16949) | Audita y valida el sistema de control de calidad. |
| A-07 | Sistemas legacy (ERP / Mantenimiento) | Proveen órdenes de producción y programación de mantenimiento. |

**Trabajadores del negocio (NO actores):** operario de máquina, supervisor de turno, ingeniero de calidad, director de planta, equipo de TI interno, científico de datos consultor.

### 1.2 Primera descomposición — 5 procesos de negocio

![[02-Diagramas/examen/2-caso-negocio/descomposicion-smartpress.png]]
`boveda/02-Diagramas/examen/2-caso-negocio/descomposicion-smartpress.png`

| ID | Caso de uso de negocio | Categoría | Actores |
|---|---|---|---|
| CUN-01 | Recepción y calificación de materia prima | Soporte | A-01 Proveedor de materia prima |
| CUN-02 | Preparación y calibración de la máquina | Soporte | A-02 Área de Producción, A-07 Sistemas legacy |
| CUN-03 | **Monitoreo y control en línea del ciclo de producción** | **Núcleo** | A-02 Área de Producción, A-03 PLC, A-04 Área de Mantenimiento |
| CUN-04 | Inspección final y mejora del modelo predictivo | Núcleo | A-08 Sistema de medición láser (CMM) |
| CUN-05 | Trazabilidad, embarque y auditoría de calidad | Gerencial | A-05 Cliente, A-06 Ente certificador |

> **Crecimiento de actores declarado:** en la descomposición aflora **A-08 Sistema de medición láser (CMM)**, contraparte implícita del core (la inspección de la etapa 4). Los actores **pueden crecer** del core a la descomposición; ninguno del core desapareció — los 7 están presentes.

## 2. Drivers de Requisitos Funcionales — CDU expandidos de 2 CUN

Se expanden los dos CUN con mayor peso arquitectónico: **CUN-03** (el núcleo de tiempo real) y **CUN-05** (el que impone inmutabilidad y retención). Sin descripciones textuales, según lo pedido.

### 2.1 CDU expandido de CUN-03 — Monitoreo y control en línea

![[02-Diagramas/examen/3.1-drivers-rf/cdu-expandido-monitoreo.png]]
`boveda/02-Diagramas/examen/3.1-drivers-rf/cdu-expandido-monitoreo.png`

| ID | Caso de uso del sistema | Relación | Actor |
|---|---|---|---|
| CU-001 | Supervisar ciclo de producción en línea | base | Operario de máquina |
| CU-002 | Capturar mediciones de sensores vía OPC-UA | `«include»` de CU-001 | Sistema de Control de Máquina (PLC) |
| CU-003 | Predecir calidad de la pieza (inferencia ML) | `«include»` de CU-001 | — (apoyo) |
| CU-004 | Registrar trazabilidad del ciclo | `«include»` de CU-001 | — (apoyo) |
| CU-005 | Ejecutar acción correctiva sobre la máquina | `«extend»` **[predicción = defectuosa]** | Sistema de Control de Máquina (PLC) |
| CU-006 | Almacenar y reconciliar desde buffer local | `«extend»` **[caída de red]** | — (apoyo) |
| CU-007 | Notificar deriva de sensor a Mantenimiento | `«extend»` **[deriva de sensor]** | — (apoyo) |
| CU-008 | Consultar tablero de estado en tiempo real | asociación | **Personal de piso** (actor padre) |
| CU-009 | Atender alerta de desviación y acción sugerida | asociación | Supervisor de turno |

**Generalización de actores:** `Operario de máquina` y `Supervisor de turno` heredan de **`Personal de piso`**, que concentra el CU compartido (CU-008). Línea llena con triángulo hueco, del hijo al padre.

### 2.2 CDU expandido de CUN-05 — Trazabilidad, embarque y auditoría

![[02-Diagramas/examen/3.1-drivers-rf/cdu-expandido-trazabilidad.png]]
`boveda/02-Diagramas/examen/3.1-drivers-rf/cdu-expandido-trazabilidad.png`

| ID | Caso de uso del sistema | Relación | Actor |
|---|---|---|---|
| CU-010 | Gestionar la trazabilidad de la pieza producida | base | Ingeniero de Calidad |
| CU-011 | Etiquetar pieza con código QR único | `«include»` de CU-010 | — (apoyo) |
| CU-012 | Sellar registro de producción inmutable | `«include»` de CU-010 | — (apoyo) |
| CU-013 | Registrar inspección CMM y correlacionar con producción | `«extend»` **[pieza en el muestreo 5%]** | Sistema de medición láser (CMM) |
| CU-014 | Consultar trazabilidad forense de un lote | base | Auditor externo (ISO / IATF), Cliente |
| CU-015 | Verificar integridad del registro inmutable | `«include»` de CU-014 | — (apoyo) |
| CU-016 | Emitir expediente de calidad del embarque | base | Cliente (ensambladora automotriz) |

### 2.3 Drivers de Requisitos Funcionales derivados

![[02-Diagramas/examen/3.1-drivers-rf/drivers-rf-smartpress.png]]
`boveda/02-Diagramas/examen/3.1-drivers-rf/drivers-rf-smartpress.png`

| ID | Driver RF | CUN | CU del sistema |
|---|---|---|---|
| RFG-001 | Capturar 500 mediciones/s por máquina en 25 máquinas, en tiempo real, vía OPC-UA | CUN-03 | CU-002 |
| RFG-002 | Ejecutar inferencia ML sobre 500 mediciones y predecir la calidad antes de que termine el ciclo | CUN-03 | CU-003 |
| RFG-003 | Enviar orden de ajuste o de paro al PLC cuando la predicción es "defectuosa" | CUN-03 | CU-005 |
| RFG-004 | Registrar trazabilidad completa por pieza (máquina, turno, operario, lote, parámetros, inspección) | CUN-03, CUN-05 | CU-004, CU-010 |
| RFG-005 | Etiquetar cada pieza con un código QR único que porte el expediente | CUN-05 | CU-011 |
| RFG-006 | Sellar los registros de producción de forma inmutable y verificable | CUN-05 | CU-012 |
| RFG-007 | Correlacionar la inspección CMM (15 dimensiones, 5% de piezas) con los datos de producción y reentrenar el modelo | CUN-04, CUN-05 | CU-013 |
| RFG-008 | Consultar trazabilidad forense de un lote sobre el histórico de 7 años | CUN-05 | CU-014, CU-015 |
| RFG-009 | Detectar deriva de sensores y notificar a Mantenimiento antes de que cause defectos | CUN-03 | CU-007 |
| RFG-010 | Presentar tablero de estado y desempeño de turno en tiempo real, con acción correctiva sugerida | CUN-03 | CU-008, CU-009 |
| RFG-011 | Bufferizar localmente y reconciliar al reconectar, sin pérdida de mediciones | CUN-03 | CU-006 |
| RFG-012 | Integrarse con ERP y sistema de mantenimiento legacy (REST, 1-2 s) para órdenes y programación | CUN-02 | — |
| RFG-013 | Registrar el lote de materia prima, sus propiedades y el certificado del proveedor | CUN-01 | — |
| RFG-014 | Actualizar el modelo predictivo (shadow, A/B, canary) sin detener la producción | CUN-04 | — |

---

## 3. Atributos de calidad (10 pts)

![[02-Diagramas/examen/3.2-drivers-calidad/drivers-calidad-smartpress.png]]
![[02-Diagramas/examen/3.2-drivers-calidad/escenarios-calidad-smartpress.png]]
`boveda/02-Diagramas/examen/3.2-drivers-calidad/`

Se infieren **8** (se pedían al menos 5). Cada uno se documenta como escenario de **seis partes** y **lleva una medida numérica**: un atributo de calidad sin número no es un driver, es un deseo.

| ID | Atributo | Fuente | Estímulo | Artefacto | Entorno | Respuesta | **Medida** |
|---|---|---|---|---|---|---|---|
| **AC-01** | Rendimiento (latencia) | Sensores de la máquina | Se completan las 500 mediciones de un ciclo | Motor de inferencia ML | Producción normal, 25 máquinas | Emite la predicción de calidad de la pieza | **< 1 s** para ciclos de 45 s y **< 5 s** para ciclos de 120 s |
| **AC-02** | Rendimiento (tiempo de respuesta de control) | PLC Siemens S7-1500 | Envía una solicitud de ajuste vía OPC-UA | Servicio de control | Red industrial Ethernet/IP, 5 ms | El sistema responde con la orden | **< 200 ms** extremo a extremo |
| **AC-03** | Disponibilidad / fiabilidad | Red industrial | Caída de red de 30 s | Ingesta + buffer local | Planta 24/7, 3 turnos | Conserva el buffer, reconstruye la trazabilidad y sigue operando | **0 mediciones perdidas**, **100 %** de piezas con trazabilidad reconstruida, **0** interrupciones visibles al operario |
| **AC-04** | Escalabilidad | Turno de la noche | El volumen de datos sube 10× | Pipeline de ingesta y almacenamiento | Presupuesto fijo de infraestructura | Absorbe el pico sin degradar | Se mantiene **AC-01** (p95) con **10×** el caudal; sin pérdida de mensajes |
| **AC-05** | Seguridad (integridad y autenticación) | Emisor de una orden de ajuste (o un atacante) | Se emite "reducir temperatura 3 °C" | Canal de comandos al PLC | Red de planta | Solo se ejecutan órdenes firmadas y autenticadas | **100 %** de órdenes firmadas; **0** órdenes aceptadas sin firma válida; **TLS** obligatorio, **0** bytes en texto plano en la red |
| **AC-06** | Seguridad (no repudio) / rendimiento de consulta | Auditor IATF o cliente con reclamo | Consulta forense de un lote de hace 7 años | Repositorio histórico | 1.3 PB acumulados | Devuelve el expediente completo y verificable | **< 10 min** de respuesta; **7 años** de retención; **100 %** de registros con hash verificable |
| **AC-07** | Mantenibilidad | Equipo de TI interno (4 personas: 2 .NET, 1 Angular, 1 DBA) | El científico de datos se retira a los 6 meses | Sistema completo, incluido el pipeline de ML | US$ 20,000 de capacitación | El equipo opera, respalda, recupera y despliega modelos | Curva de traspaso **≤ 6 meses**; despliegue de modelo nuevo con **0 s** de paro de producción |
| **AC-08** | Usabilidad | Operario de máquina que rota de turno | Se le asigna la estación por primera vez | Interfaz de piso | Personal sin perfil técnico | Opera el tablero y atiende alertas sin asistencia | **≤ 3 horas** de capacitación |

### Justificación con foco arquitectónico

| ID | Qué decisión de arquitectura fuerza |
|---|---|
| AC-01 | Obliga a **procesamiento en el borde** (inferencia en planta, no en la nube): la latencia a internet es impredecible y no cabe en la ventana del ciclo. |
| AC-02 | Obliga a **separar el canal de control del canal de analítica**: el lazo de control no puede compartir cola ni recursos con la ingesta masiva. |
| AC-03 | Obliga a **store-and-forward con buffer local en el borde** y **reconciliación idempotente**: la red se cae, y el registro no puede depender de que esté arriba. |
| AC-04 | Obliga a **desacoplar la ingesta con una cola** y a **particionar por máquina y por tiempo**; descarta la escritura sincrónica contra una base transaccional. |
| AC-05 | Obliga a un **broker de comandos con firma digital y autenticación mutua** sobre OPC-UA; el riesgo es de seguridad **física** (daño a máquina, lesiones), no solo de datos. |
| AC-06 | Obliga a **almacenamiento por niveles** (caliente / tibio / frío) más **registro inmutable con hash encadenado (WORM)** e índices de trazabilidad separados de los datos crudos. |
| AC-07 | **Limita** la libertad tecnológica: el número de componentes y de tecnologías distintas está acotado por lo que 4 personas pueden operar. Empuja a servicios gestionados sobre stack conocido. |
| AC-08 | Obliga a una **capa de presentación de piso deliberadamente reducida**, distinta del tablero del supervisor y de la consola del ingeniero de calidad. |

---

## 4. Drivers de Restricción (10 pts)

Las restricciones **no se priorizan**: todas son obligatorias. Clasificadas en las tres categorías del enunciado.

![[02-Diagramas/examen/3.3-drivers-restriccion/restricciones-tecnicas-smartpress.png]]
![[02-Diagramas/examen/3.3-drivers-restriccion/restricciones-negocio-smartpress.png]]
![[02-Diagramas/examen/3.3-drivers-restriccion/restricciones-sistema-smartpress.png]]
`boveda/02-Diagramas/examen/3.3-drivers-restriccion/`

### 4.1 Técnicas (tecnologías, plataformas)

| ID | Restricción | Origen |
|---|---|---|
| RES-T01 | El protocolo de comunicación con las máquinas debe ser **OPC-UA**; no se puede sustituir | Junta Directiva |
| RES-T02 | Los PLC son **Siemens S7-1500**, 25 máquinas, 500 mediciones/s cada una | Infraestructura |
| RES-T03 | Red industrial **Ethernet/IP**, 5 ms de latencia, con **caídas esporádicas** | Infraestructura |
| RES-T04 | Internet de **100 Mbps compartido** con toda la planta; **no se puede depender únicamente de la nube** para el procesamiento en tiempo real | Infraestructura / Junta |
| RES-T05 | Data center local acotado: **4 servidores VMware, 64 vCPU, 256 GB RAM, 20 TB SAN** | Infraestructura |
| RES-T06 | **No se pueden almacenar los datos crudos de sensores en la base transaccional** | Junta Directiva |
| RES-T07 | La base de datos **debe soportar particionamiento y retención** (1.3 PB a 7 años) | Junta Directiva |
| RES-T08 | **No se puede diseñar un monolito**: ingesta, ML y trazabilidad tienen requisitos distintos de rendimiento y escalamiento | Junta Directiva |
| RES-T09 | Los datos de producción **deben viajar cifrados**; nada en texto plano por la red | Política de seguridad |
| RES-T10 | A la nube **solo pueden salir análisis agregados**; los datos crudos no salen de la planta | Política de seguridad |
| RES-T11 | Stack disponible del equipo: **.NET, SQL Server, Azure, Angular**; ML en **Python / TensorFlow / Scikit-learn** | Equipo y habilidades |

### 4.2 De Negocio (presupuesto, tiempo, leyes o normativos)

| ID | Restricción | Origen |
|---|---|---|
| RES-N01 | Presupuesto de infraestructura: **US$ 150,000** para el próximo año (hardware, licencias y cloud) | Presupuesto |
| RES-N02 | Presupuesto de capacitación: **US$ 20,000** | Presupuesto |
| RES-N03 | Equipo interno de **4 personas**, sin experiencia en Big Data ni ML | Equipo |
| RES-N04 | El científico de datos es consultor y está disponible **solo 6 meses** | Equipo |
| RES-N05 | La planta opera **24/7 en 3 turnos**: **no se puede parar la producción** para mantenimiento ni actualizaciones | Junta Directiva |
| RES-N06 | **ISO 9001**: trazabilidad de **toda** acción que afecte la calidad | Regulación |
| RES-N07 | **IATF 16949**: los sistemas de control de calidad deben ser **validados** y los cambios **gestionados formalmente** | Regulación |
| RES-N08 | Retención legal de datos de producción: **7 años** | Regulación |
| RES-N09 | Confidencialidad: los datos de producción **no pueden salir de la planta** en texto plano | Política de la empresa |
| RES-N10 | La capacitación de un operario **no puede exceder 3 horas** | Junta Directiva |
| RES-N11 | Contexto de urgencia: **US$ 2.5 millones** en penalizaciones en 6 meses justifican el proyecto y acotan el plazo | Caso de negocio |

### 4.3 De Sistema (interacción con otros sistemas)

| ID | Restricción | Origen |
|---|---|---|
| RES-S01 | Integración con el **ERP legacy (Oracle Forms)** por **API REST lenta: 1-2 s** de respuesta | Expectativa 8 |
| RES-S02 | Integración con el **sistema de mantenimiento legacy**, con la misma limitación | Expectativa 8 |
| RES-S03 | Integración con **25 PLC** simultáneos vía OPC-UA, en modo lectura y escritura | Infraestructura |
| RES-S04 | Integración con el **CMM**: inspección **destructiva**, **3 min por pieza**, solo **5 %** de las piezas | Etapa 4 |
| RES-S05 | El **código QR** es el contrato de trazabilidad con el cliente: su contenido y su verificación son externos al sistema | Etapa 5 |

---

# PARTE II — Análisis de Tensiones y Conflictos (40 pts)

Se presentan **6** conflictos (se pedían al menos 4).

### Conflicto 1 — El lazo de control no cabe en la ventana de tiempo
**Drivers en tensión:** RFG-003 / AC-02 (**< 200 ms** de respuesta al PLC) **vs.** AC-01 / RFG-002 (la inferencia ML tarda **2-5 s**) **vs.** RES-T04 (no depender de la nube).

**1. Descripción.** El enunciado pide dos tiempos incompatibles sobre el mismo camino: el PLC exige respuesta en menos de 200 ms, pero la predicción que **origina** la orden de ajuste tarda entre 2 y 5 segundos. Para un ciclo de 45 s, un modelo de 5 s consume el 11 % del ciclo y la pieza ya está formándose. Si además la inferencia se hiciera en la nube, la latencia sería impredecible. El conflicto es **RF vs. AC** y también **AC vs. AC**: la funcionalidad "retroalimentación automática en tiempo real" y el atributo de latencia no pueden satisfacerse por el mismo camino de ejecución.

**2. Consecuencias de no resolverlo.** El CU-005 "Ejecutar acción correctiva" se dispara **tarde**: la máquina sigue inyectando mientras espera la orden y produce exactamente las piezas defectuosas que el proyecto existe para evitar. Se conserva el problema original —detección tardía— con un sistema nuevo encima, y no se recuperan los US$ 2.5 millones de penalizaciones.

**3. Vistas afectadas.**
- **Vista de Procesos:** es la vista dominante. Obliga a separar en **dos hilos con presupuestos de tiempo distintos**: un lazo duro de control (< 200 ms) y un lazo blando de predicción (segundos). Define concurrencia, colas y prioridades.
- **Vista de Escenarios:** el escenario de CU-001 → CU-003 → `«extend»` CU-005 deja de ser una secuencia lineal y debe reescribirse como predicción anticipada dentro del ciclo, no al final.

---

### Conflicto 2 — El volumen no cabe donde puede estar
**Drivers en tensión:** RFG-004 / RFG-008 (**1.3 PB a 7 años**) **vs.** RES-T05 (**20 TB de SAN**) y RES-N01 (**US$ 150,000**) **vs.** RES-T10 / RES-N09 (los datos crudos **no salen de la planta**).

**1. Descripción.** Se generan 5 TB/día crudos y 500 GB/día procesados. El almacenamiento local disponible (20 TB) se agota en **4 días** de datos crudos o en **40 días** de datos procesados. La salida natural sería la nube, pero la política de seguridad solo permite subir **agregados**, y el presupuesto de US$ 150,000 debe cubrir además hardware y licencias. Es un conflicto **Restricción vs. Restricción**, con AC-06 (retención de 7 años) atrapado en el medio.

**2. Consecuencias de no resolverlo.** O se descartan los datos crudos —y entonces el Ingeniero de Calidad no puede reentrenar el modelo, que es la necesidad oculta que sostiene todo el valor del sistema—, o se incumple la retención de 7 años y la trazabilidad de IATF 16949, con riesgo de perder la certificación y, con ella, a los clientes ensambladores.

**3. Vistas afectadas.**
- **Vista Lógica:** obliga a partir el modelo de datos en **dos repositorios distintos** (crudo comprimido/serie de tiempo vs. maestro de trazabilidad relacional) y a definir qué se agrega, cuándo y con qué pérdida.
- **Vista de Procesos:** la agregación y la compresión pasan a ser procesos en streaming con su propia ventana y su propio presupuesto de CPU, no un trabajo nocturno.

---

### Conflicto 3 — Parar la máquina vs. no parar la máquina
**Drivers en tensión:** RFG-003 ("detener la máquina inmediatamente") **vs.** la necesidad oculta del **Operario** (cada parada reduce su bono) y RES-N05 (**no se puede parar la producción**).

**1. Descripción.** El enunciado ordena detener la máquina cuando la predicción sea "pieza defectuosa", pero el operario es evaluado y bonificado por producción, y la Junta prohíbe parar la planta. Cada **falso positivo** del modelo es una parada injustificada. El Ingeniero de Calidad lo dice explícitamente: quiere reducir falsos positivos. Es un conflicto **RF vs. Restricción de negocio**, agravado porque el actor que debe obedecer la alerta tiene un incentivo económico para ignorarla.

**2. Consecuencias de no resolverlo.** El operario aprende a desestimar o silenciar el sistema —o la planta lo desactiva por presión de producción— y SmartPress se convierte en un tablero decorativo. El control de calidad vuelve al muestreo 1 de 100 al final de la línea y los reclamos continúan. Alternativamente, si la política es agresiva, la planta pierde disponibilidad productiva sin que baje la tasa real de defectos.

**3. Vistas afectadas.**
- **Vista de Escenarios:** el `«extend» [predicción = defectuosa]` de CU-005 no puede ser una condición binaria; hay que modelar los escenarios de **umbral, confianza y confirmación humana** (CU-009 "Atender alerta de desviación") y el escenario de falso positivo.
- **Vista de Procesos:** la política de decisión (ajustar parámetros vs. detener) es un componente en el camino de control con su propia lógica de estado y su modo *shadow*.

---

### Conflicto 4 — La inmutabilidad frena la ingesta
**Drivers en tensión:** AC-06 / RFG-006 (registro inmutable, verificable, forense en < 10 min) **vs.** AC-04 (pico de **10×** en el turno de noche) y RES-T06 (nada crudo en la base transaccional).

**1. Descripción.** Sellar cada registro de forma inmutable y verificable (hash, firma, encadenamiento, WORM) tiene un costo por escritura. A 12,500 mediciones por segundo en régimen normal, y 10× en el pico, ese costo se multiplica hasta hacer que la ingesta no siga el ritmo del proceso físico. Es un conflicto **AC vs. AC**: seguridad/no repudio contra rendimiento y escalabilidad.

**2. Consecuencias de no resolverlo.** La cola de ingesta crece hasta desbordarse y se pierden mediciones justo en el turno de mayor carga. Se rompe RFG-004: hay piezas sin expediente completo. Ante un reclamo del cliente no se puede reconstruir el lote, que es **precisamente la pérdida de trazabilidad que originó el proyecto**, y se incumple IATF 16949.

**3. Vistas afectadas.**
- **Vista Lógica:** obliga a distinguir qué se sella (el **expediente de la pieza**, granularidad baja) de qué no (cada medición cruda, granularidad altísima), y a definir la relación entre ambos.
- **Vista de Procesos:** el sellado se mueve fuera del camino crítico de ingesta, a un proceso asincrónico por lotes con su propia garantía de completitud.

---

### Conflicto 5 — Un sistema distribuido para un equipo que no puede operarlo
**Drivers en tensión:** RES-T08 (**no monolito**) y las exigencias de Big Data + ML **vs.** AC-07 / RES-N03 / RES-N04 (**4 personas .NET/SQL**, científico de datos por **6 meses**, **US$ 20,000** de capacitación).

**1. Descripción.** La Junta prohíbe el monolito y el caso exige un pipeline de streaming, un almacén de series de tiempo, un motor de ML con despliegue canary y un almacén histórico de petabytes. Nada de eso está en el stack del equipo. El consultor que sí lo domina se va a los 6 meses. Es un conflicto **Restricción técnica vs. Atributo de mantenibilidad**: la arquitectura correcta en papel es inoperable por la organización que la recibe.

**2. Consecuencias de no resolverlo.** Al mes 7 nadie puede reentrenar el modelo ni diagnosticar la caída de un componente. El modelo se degrada silenciosamente con el desgaste de moldes y sensores, la tasa de falsos negativos sube y los reclamos regresan — ahora con un sistema caro que la planta ya no entiende. Es el escenario de riesgo más probable de todo el caso.

**3. Vistas afectadas.**
- **Vista Lógica:** acota el **número de componentes y de tecnologías distintas**. Empuja a un particionamiento mínimo (3 servicios, no 15) y a servicios gestionados sobre el stack conocido en lugar de plataformas nuevas.
- **Vista de Escenarios:** el escenario de RFG-014 (actualizar el modelo sin detener producción) debe ser ejecutable **por el equipo interno**, no por el consultor; eso cambia el diseño del pipeline de despliegue.

---

### Conflicto 6 — Firmar cuesta tiempo
**Drivers en tensión:** AC-05 (**100 %** de órdenes firmadas y autenticadas) **vs.** AC-02 (**< 200 ms** de respuesta al PLC) y RES-T01 (no se puede cambiar OPC-UA).

**1. Descripción.** Autenticar y firmar cada orden de ajuste añade handshake, verificación de certificado y validación criptográfica al camino que ya tiene solo 200 ms de presupuesto, sobre un protocolo que no se puede sustituir por otro más liviano. Es un conflicto **AC vs. AC** con una restricción técnica que impide la salida fácil.

**2. Consecuencias de no resolverlo.** Si se sacrifica la seguridad, una orden falsificada o errónea puede **dañar una máquina o causar lesiones** —el propio enunciado lo advierte— y la responsabilidad es civil y penal, no solo de calidad. Si se sacrifica la latencia, se cae en el Conflicto 1 y la retroalimentación llega tarde.

**3. Vistas afectadas.**
- **Vista de Procesos:** obliga a decidir dónde vive la verificación (sesión OPC-UA persistente con autenticación mutua establecida **una vez**, en lugar de por mensaje) y a medir el presupuesto de tiempo por etapa.
- **Vista de Escenarios:** hay que documentar el escenario de **orden ilegítima rechazada** y el de **degradación segura** (qué hace la máquina si no puede verificar la firma: se asume que no ejecuta).

---

# PARTE III — Defensa del Diseño (20 pts)

## 1. ¿Está de acuerdo con la tabla única `SensorReadings`? (5 pts)

**No. La decisión es incorrecta y viola restricciones explícitas del cliente.**

| # | Razón | Driver violado |
|---|---|---|
| 1 | **Está prohibida por el cliente.** La Junta Directiva dice textualmente que no se pueden almacenar todos los datos crudos de sensores en la base transaccional. No es una discusión técnica: es una restricción, y las restricciones son obligatorias. | RES-T06 |
| 2 | **La base debe soportar particionamiento y retención**, y una tabla plana sin estrategia de partición no lo hace. | RES-T07 |
| 3 | **El volumen no cabe.** 25 × 500 × 86,400 = **1,080 millones de filas/día**, ~5 TB/día crudos, 1.3 PB a 7 años, contra **20 TB de SAN** y US$ 150,000 de presupuesto. La tabla se llena en días. | RES-T05, RES-N01, RES-N08 |
| 4 | **Los índices son el problema, no la solución.** A 12,500 inserciones/s —125,000 en el pico de 10×— el mantenimiento de un índice B-tree sobre `Timestamp` y `MachineID` degrada la escritura y produce fragmentación y contención de página. El argumento del equipo está invertido. | AC-04 |
| 5 | **El formato es EAV** (`SensorName`, `Value`): una fila por medición, con el nombre del sensor repetido mil millones de veces al día. Sin tipado, sin compresión columnar, con el peor factor de expansión posible. | AC-04, RES-T05 |
| 6 | **La consulta forense se vuelve inviable.** Reconstruir un lote de hace 7 años exige recorrer miles de millones de filas EAV: no hay forma de cumplir los **< 10 minutos**. | AC-06, RFG-008 |
| 7 | **Compromete el lazo de tiempo real.** Si la ingesta escribe sincrónicamente contra la misma instancia transaccional que sirve la trazabilidad, la contención de escritura se propaga al camino de control. | AC-01, AC-02 |
| 8 | **Es la decisión que el Conflicto 5 predice:** "usamos lo que ya sabemos" es mantenibilidad mal entendida — se optimiza la comodidad del equipo hoy a costa de que el sistema no funcione mañana. | AC-07 |

**Contrapropuesta, en una línea por capa:**

| Capa | Decisión |
|---|---|
| Ingesta | Cola/stream en el borde de planta, desacoplada del lazo de control (AC-02, AC-04). |
| Crudo (caliente) | Almacén de **series de tiempo columnar comprimido**, particionado por máquina y por ventana de tiempo; retención corta (7-30 días). |
| Agregado (tibio) | Resúmenes por ciclo y por pieza —los ~500 GB/día— con retención media; es lo único que puede subir agregado a la nube (RES-T10). |
| Trazabilidad (maestro) | **SQL Server sí, pero para el expediente de la pieza**: lote, máquina, turno, operario, parámetros nominales, resultado. Millones de filas al día, no miles de millones. Aquí el equipo usa lo que sabe. |
| Histórico (frío) | Archivo **WORM** particionado por año, con hash encadenado y un índice de trazabilidad que permita llegar al lote sin recorrer el crudo (AC-06). |

## 2. Matriz de trazabilidad: requerimientos vs. CDU (15 pts)

Formato de la **NT1, figura 1, pág. 91**. Se incluyen los drivers de calidad y de restricción que **controlan específicamente la situación de la Parte III.1**, marcados con ▲ en la columna de control.

### 2.1 Matriz principal — Drivers RF vs. Casos de uso

![[02-Diagramas/examen/4-matrices-trazabilidad/matriz-rf-cdu-smartpress.png]]
`boveda/02-Diagramas/examen/4-matrices-trazabilidad/matriz-rf-cdu-smartpress.png`

| Requerimiento | CU-001 | CU-002 | CU-003 | CU-004 | CU-005 | CU-006 | CU-007 | CU-008 | CU-010 | CU-011 | CU-012 | CU-013 | CU-014 | CU-015 | CU-016 |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| RFG-001 Capturar 500 med/s vía OPC-UA | X | **X** | | | | X | | | | | | | | | |
| RFG-002 Inferencia ML dentro del ciclo | X | | **X** | | | | | | | | | | | | |
| RFG-003 Orden de ajuste/paro al PLC | X | | | | **X** | | | | | | | | | | |
| RFG-004 Trazabilidad completa por pieza | X | | | **X** | | X | | | **X** | | X | | X | | X |
| RFG-005 Etiquetado QR único | | | | | | | | | X | **X** | | | X | | X |
| RFG-006 Sellado inmutable y verificable | | | | X | | | | | X | | **X** | | | X | |
| RFG-007 Correlacionar CMM y reentrenar | | | X | X | | | | | X | | | **X** | | | |
| RFG-008 Consulta forense a 7 años | | | | X | | | | | | | X | | **X** | X | |
| RFG-009 Detectar deriva de sensores | X | X | | | | | **X** | | | | | X | | | |
| RFG-010 Tablero en tiempo real | X | | X | | | | X | **X** | | | | | | | |
| RFG-011 Buffer local y reconciliación | X | X | | X | | **X** | | | | | | | | | |
| RFG-014 Actualizar modelo sin parar | | | X | | | | | | | | | X | | | |

**X** = el caso de uso realiza el requerimiento · **X en negrita** = caso de uso principal (dueño del requerimiento).

### 2.2 Matriz de control — Drivers de calidad y restricción vs. Casos de uso

![[02-Diagramas/examen/4-matrices-trazabilidad/matriz-control-smartpress.png]]
`boveda/02-Diagramas/examen/4-matrices-trazabilidad/matriz-control-smartpress.png`

Esta es la que responde a la pregunta: **son los drivers que, de haberse trazado, habrían impedido la decisión de la tabla única.**

| Driver | Tipo | CU-002 | CU-003 | CU-004 | CU-005 | CU-012 | CU-013 | CU-014 | CU-015 | Control sobre `SensorReadings` |
|---|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|---|
| AC-01 Inferencia < 1 s / < 5 s | Calidad | X | **X** | | | | | | | ▲ La escritura sincrónica en la tabla única roba tiempo al ciclo de inferencia |
| AC-02 Respuesta al PLC < 200 ms | Calidad | X | | | **X** | | | | | ▲ Contención de escritura en la misma instancia degrada el lazo de control |
| AC-03 Caída de red 30 s sin pérdida | Calidad | X | | X | | | | | | Exige buffer en el borde, no una tabla central única |
| AC-04 Pico de 10× sin degradación | Calidad | **X** | | X | | | | | | ▲ 125,000 filas/s con índices B-tree: el diseño no escala |
| AC-05 Órdenes firmadas y autenticadas | Calidad | | | | **X** | X | | | X | Canal de comandos separado del almacén de datos |
| AC-06 Forense < 10 min sobre 7 años | Calidad | | | X | | **X** | | **X** | X | ▲ Imposible sobre EAV plano: exige niveles e índice de trazabilidad |
| AC-07 Mantenible por 4 personas | Calidad | X | X | X | | X | X | X | | ▲ Justifica SQL Server **para el maestro**, no para el crudo |
| RES-T06 Nada crudo en la transaccional | Restricción | **X** | | **X** | | | | | | ▲ **Prohibición explícita: la decisión la viola de frente** |
| RES-T07 BD con particionamiento y retención | Restricción | X | | **X** | | X | | X | | ▲ Una tabla plana no cumple |
| RES-T05 20 TB de SAN | Restricción | X | | X | | | | X | | ▲ 5 TB/día agotan la SAN en 4 días |
| RES-N08 Retención 7 años (1.3 PB) | Restricción | | | X | | X | | **X** | X | ▲ Obliga a archivo frío por niveles |
| RES-N06/N07 ISO 9001 / IATF 16949 | Restricción | | | X | X | **X** | X | X | **X** | ▲ Exige inmutabilidad y validación, que la tabla plana no ofrece |
| RES-T10 Solo agregados a la nube | Restricción | X | | X | | | | | | Define qué capa puede salir de la planta |

### 2.3 Lectura de la matriz

1. **RES-T06 cruza CU-002 y CU-004** — los dos casos de uso que la tabla única pretendía servir. La celda está marcada: si el equipo hubiera consultado la matriz, la restricción habría bloqueado la decisión antes de escribir la primera línea de SQL.
2. **La columna CU-004 concentra 9 drivers de control.** Un caso de uso con esa densidad de restricciones no admite una decisión de almacenamiento tomada "porque ya lo sabemos": es un punto de arquitectura, no de implementación.
3. **AC-07 aparece a favor y en contra.** La mantenibilidad justifica usar SQL Server, pero solo donde el volumen lo permite (el maestro de trazabilidad). Trazado a nivel de caso de uso, el argumento del equipo se salva a medias en lugar de perderse entero.
4. **Cobertura inversa:** todos los RF del §2.3 tienen al menos un CU que los realiza, y todo CU de los dos diagramas expandidos aparece en al menos una fila. No hay requerimiento huérfano ni caso de uso sin origen.

---

## Lo que quedó fuera, y por qué

| Omisión | Razón |
|---|---|
| CDU expandidos de CUN-01, CUN-02 y CUN-04 | El enunciado pide **solamente 2 CUN**. |
| Descripciones textuales de los casos de uso | El enunciado las excluye explícitamente ("no hacer descripciones textuales"). |
| Vistas de Desarrollo y Física del 4+1 | La Parte II acota el análisis a **Lógica, Procesos y Escenarios**. |
| Priorización de los drivers de calidad | No se pide en este parcial; y las restricciones no se priorizan por definición. |
| Diseño de la arquitectura (componentes, despliegue) | El parcial pide **identificar drivers**, que son el insumo del diseño, no el diseño. La contrapropuesta de la Parte III.1 se limita a lo necesario para defender la respuesta. |
