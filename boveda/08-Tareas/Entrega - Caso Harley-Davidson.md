---
tema: Entrega de tarea
fuente: "Generado por 06-Proyecto-MCP/generar-entrega-hd.py — no editar a mano: cambiar el generador y volver a correrlo"
fecha: 2026-10-13
tarea: Caso Harley-Davidson
alias: [entrega harley, entrega HD, CasoHD]
---

# Caso Harley-Davidson, proyecto SiL'K · Entrega

Análisis y Diseño de Sistemas II (785) · ECYS, USAC · MBA. MSc. Claudia Rojas de Morán

Grupo 2 · 13 de octubre de 2026

| Integrante | Carné |
|---|---|
| Santiago Julián Barrera Reyes | 201905884 |
| Jemima Solmaira Chavajay Quiejú | 201801521 |
| Elías Abraham Vasquez Soto | 201900131 |
| Byron Josué Par Rancho | 201701078 |


### Índice y correspondencia con la rúbrica

| # | Criterio de la rúbrica | Pts | Sección |
|---|---|---|---|
| 1 | Caso de negocio: diagrama de contexto, CDU core y CDU primera descomposición | 15 | §1 |
| 2 | Identificación de stakeholders | 10 | §2 |
| 3 | Drivers RF, de atributos de calidad y de restricción | 20 | §3 |
| 4 | Matrices de trazabilidad acopladas a los criterios 1, 2 y 3 (cuatro) | 15 | §4 |
| 5 | Estilos arquitectónicos, diagrama de bloques y diagrama de despliegue | 20 | §5 |
| 6 | Drivers de calidad y de restricción en los pasos para definir la arquitectura, y modelo de calidad | 20 | §6 |
|  | **Total** | **100** |  |


### Declaraciones que condicionan todo el documento

> **Frontera del negocio**
>
> **El negocio** es la **gestión de suministros y compras de Harley-Davidson**: el ámbito que el propio caso dibuja en su anexo 6a. No es la empresa entera, y **no es el concurso de proveedores de software** que da título al caso: ese relato es la fuente de los stakeholders, los requisitos y las restricciones.
>
> **Consecuencia:** quienes ejecutan las compras (compradores, dirección de compras, recepcionistas) son **trabajadores del negocio**. Son **actores** las entidades de afuera: el proveedor y las **áreas** que piden, reciben y pagan. Regla de clase aplicada: las áreas son actores, las personas son trabajadores.
>
> **Cambio de lente:** frente al **software** SiL'K, esos mismos trabajadores pasan a ser entidades externas. Por eso el comprador no aparece en el core (§1.2) y sí en el diagrama de contexto (§1.1) y en los CDU expandidos (§3.1).

> **Cómo se leyó la consigna**
>
> **«Traer el caso al presente»:** se actualiza la **tecnología** (la «red Internet de Suministros» de 1998 pasa a ser portal web, API y nube). Los **hechos** del caso (organización, ámbito, fases, cifras) no se tocan. Lo que el caso no dice y hace falta va rotulado como **supuesto**.
>
> **«Los pasos para definir la arquitectura»:** los siete de la lámina de clase *Pasos para la definición de una Arquitectura de software* (§6.1).
>
> **«EaC»:** los **escenarios de atributos de calidad**, con identificador `EAC-nn`, seis partes y prioridad en pares, tal como en el ejemplo de clase del Sistema de Transporte (§3.2).
>
> **«Modelo de calidad»:** según la indicación de la catedrática, el pensamiento ISO como **familia de normas**, con ISO/IEC 9126 y la serie ISO/IEC 25000 como normas concretas (§6.4).
>
> **Identificadores:** `STK-nn` stakeholder · `CDU-nn` proceso de negocio · `CU-nn` caso de uso del sistema · `RF-nn` driver funcional · `EAC-nn` escenario de atributo de calidad (driver de calidad) · `RE-nn` driver de restricción.


## 1. Caso de negocio (criterio 1, 15 pts)

Es el **paso 0** del método de clase: antes de diseñar, delimitar el negocio y lo que el producto intercambia con su entorno. Tres diagramas, de afuera hacia adentro.

La notación es la de clase: en el diagrama de contexto, la **elipse** es El Producto, cada **rectángulo** es una entidad o agente externo y cada **flecha** es un flujo con nombre.


### 1.1 Diagrama de contexto

**El Producto** es el software SiL'K. Las entidades son todo lo que intercambia información con él: personas, áreas y sistemas. Cada flecha es un *streamline* con nombre, en sustantivo: son **19**.

| Entidad | Entrega a SiL'K | Recibe de SiL'K |
|---|---|---|
| Empleado solicitante | Solicitud de pedido | Estado de la solicitud |
| Responsable de área (aprobador) | Decisión de aprobación | Solicitud por aprobar |
| Dirección de Compras | Contratos y reglas de compra | Gasto consolidado |
| Comprador | Pedido de compra y evaluación | Propuestas y alertas de plazo |
| Ingeniería (Centro de Desarrollo de Productos) | Plan y coste objetivo | Preparación de las piezas |
| Suministrador | Confirmación, envío y factura | Pedido, demanda y resultados |
| Recepción y Logística | Recepción de material | Entregas previstas |
| Sistema MRP/DRP de planta | Requisitos de material | Pedidos en firme y fechas |
| Sistema de Cuentas de Acreedores | Estado del pago | Factura conciliada |
| Sistemas de compras locales (en retiro) | Histórico de pedidos | Ninguno: solo emiten, se migran y se apagan |

![[02-Diagramas/caso-hd/1-caso-negocio/contexto-hd.svg]]

*Figura 1. Diagrama de contexto de SiL'K: diez entidades y diecinueve flujos.*


### 1.2 CDU de alto nivel (core)

Una sola elipse con el nombre del negocio completo y todos sus actores alrededor. Las asociaciones van **sin punta**: la comunicación se inicia en los dos sentidos.

![[02-Diagramas/caso-hd/1-caso-negocio/cdu-core-hd.svg]]

*Figura 2. CDU core: el negocio y sus seis actores.*

| Actor del negocio | Por qué está afuera | Qué obtiene del negocio |
|---|---|---|
| Proveedor (suministrador) | Otra empresa. El caso lo llama «una extensión de nosotros mismos», pero no pertenece a Harley-Davidson | Pedidos, demanda prevista, sus resultados y el pago |
| Áreas solicitantes | Los más de 2.000 empleados que generan solicitudes no son de Compras | El material o servicio pedido |
| Fabricación (centros de producción) | Compras le sirve; su planificación (MRP/DRP) origina la demanda de piezas | Piezas a tiempo para no parar la línea |
| Desarrollo de Productos (Ingeniería) | Área distinta de Compras, con la que comparte los proyectos de nuevos modelos | Piezas y suministradores listos para el lanzamiento |
| Logística | Mueve el material del almacén del suministrador al de Harley-Davidson | Entregas previstas y recepciones registradas |
| Cuentas de Acreedores Comerciales | Área de Finanzas que paga; fue encuestada como parte implicada externa a Compras | Facturas conciliadas para pagar |

**Trabajadores del negocio** (dentro de la frontera, no son actores): comprador, comprador de desarrollo, dirección de compras, planificación y control de compras, y recepcionista de almacén.


### 1.3 CDU primera descomposición

Un solo diagrama, con **cuatro procesos** y el **mismo juego de actores** que el core: ninguno desaparece. Los procesos salen de las tres fases del anexo 6b; la fase 1 se partió en dos porque sus actores son distintos (quien pide no es quien recibe ni quien paga).

| Proceso | Origen en el caso | Actores | Resultado de valor |
|---|---|---|---|
| **CDU-01** Requisición y emisión del pedido de compra | anexo 6b, fase 1 a-b · anexo 6a: Requisitos, Realización de pedidos | Áreas solicitantes · Fabricación · Proveedor | Un pedido en firme en manos del suministrador |
| **CDU-02** Recepción, seguimiento y pago al suministrador | anexo 6b, fase 1 c-d · anexo 6a: Logística de entrada, Recepción | Proveedor · Logística · Cuentas de Acreedores | Material recibido y factura pagada sin discrepancias |
| **CDU-03** Gestión de la información y la relación con suministradores | anexo 6b, fase 2 | Proveedor | Un suministrador evaluado e informado, tratado como socio |
| **CDU-04** Seguimiento de compras en proyectos de nuevos productos | anexo 6b, fase 3 · anexo 6a: Desarrollo | Desarrollo de Productos · Proveedor | Piezas y suministradores listos en coste y plazo para el lanzamiento |

![[02-Diagramas/caso-hd/1-caso-negocio/cdu-descomposicion-hd.svg]]

*Figura 3. Primera descomposición: cuatro procesos de negocio.*

> **Lo que quedó fuera del negocio, y por qué**
>
> El anexo 6a marca tres actividades como «no entra dentro del ámbito del proyecto SiL'K»: **Pedido / Programación** (pedidos de los clientes), **Movimiento interno de materiales** y **Distribución** (producto acabado al cliente). No se modelan. Por eso el **cliente** y el **concesionario** no son actores de este negocio.


## 2. Identificación de stakeholders (criterio 2, 10 pts)

**Stakeholder** es toda persona, grupo u organización con un interés en el sistema. Se identificaron con cuatro barridos sobre el caso: el anexo 4 (promotores, comité y equipo), los grupos de gobierno (págs. 3, 4 y 9), las partes encuestadas (pág. 8) y los externos. Entra a la lista quien aporta **un interés propio** que ningún otro trae. El tipo de interés anticipa la clase de driver que aporta en el §3.

| Id | Stakeholder | Interés | Posición | Interés propio (concern) | Fuente |
|---|---|---|---|---|---|
| STK-01 | Garry Berryman, vicepresidente de Gestión de Materiales (promotor) | paga · patrocina | interno | Que la Estrategia de Gestión de Suministros se cumpla: el personal de compras al 70 % en gestión de proveedores y 34 M USD de ahorro en cinco años | págs. 4-7, anexo 4 |
| STK-02 | Dave Storm, vicepresidente de Planificación y Servicios de Información (promotor) | paga · patrocina | interno | Que SiL'K encaje en la estrategia de sistemas de toda la compañía y dé una visión consolidada | pág. 3, anexo 4 |
| STK-03 | Grupo de Unidad de Compras (PUG) | decide · usa | interno | Un proceso de compras común a los centros y divisiones, y los recursos que cede al proyecto | págs. 4, 7 |
| STK-04 | Pat Davidson, directora de Planificación y Control de Compras | usa · dueña del proceso | interno | Planificar y controlar las compras de toda la empresa con datos únicos | pág. 1, anexo 4 |
| STK-05 | Dave Cotteleer, director del proyecto SiL'K | dirige el proyecto | interno | Una implantación sin riesgos, dentro del ámbito y en tres fases | págs. 9-11 |
| STK-06 | Compradores de los centros y divisiones (unas 200 personas: MRO, OE, P&A, Artículos Varios) | usa | interno, trabajador | Dejar de gastar el 85 % del tiempo en tareas no estratégicas: revisar existencias, acelerar pedidos, registrar datos | pág. 8, anexo 5 |
| STK-07 | Empleados solicitantes (más de 2.000 generan solicitudes de pedido) | usa (ocasional) | interno | Pedir lo que necesitan sin formación previa y saber en qué estado está | pág. 8 |
| STK-08 | Suministradores estratégicos, Consejo Asesor de Suministradores (16) | usa (externo) | externo, actor | Acceso a sus datos de calidad, costes y plazos y a la demanda prevista; ser tratados como socios, no como vendedores | págs. 5, 10, anexo 3 |
| STK-09 | Grupo de Integración de Arquitecturas, Karen Kaminski | regula (técnico) | interno | Que la solución cumpla las normas de hardware y software y sea compatible con la arquitectura existente | págs. 9, 12 |
| STK-10 | Dirección de Sistemas del Grupo de Fabricación (Cory Mason, Tom Cullen) y su Círculo de Tecnologías de la Información | decide la inversión · opera | interno | Aprobar la inversión y operar la solución sin afectar a la producción | págs. 3, 6, 12 |
| STK-11 | Gestión del Cambio, Julie Anding | acompaña la adopción | interno | Que las 800 personas del público objetivo adopten el nuevo proceso: formación y comunicación | págs. 10, 14 |
| STK-12 | Innovación de Procesos, Chuck Braunschweig | diseña el proceso | interno | Un flujo de proceso común, construido sobre las similitudes entre centros | pág. 8 |
| STK-13 | Cuentas de Acreedores Comerciales (Finanzas) | usa · paga a proveedores | externo, actor | Pagar solo facturas conciliadas con pedido y recepción | pág. 8, anexo 6b |
| STK-14 | Logística y recepción | usa | externo, actor | Saber qué llega y cuándo, y registrar la recepción en el muelle | pág. 8, anexo 6a |
| STK-15 | Fabricación, centros de producción | usa · depende del resultado | externo, actor | Que las líneas de producción no dejen de funcionar | pág. 6 |
| STK-16 | Ingeniería, Centro de Desarrollo de Productos y equipos de plataforma | usa | externo, actor | Integrar a Compras y a los suministradores en el desarrollo de nuevos productos | págs. 4-5, anexo 6b |
| STK-17 | Proveedor del software (el finalista elegido) | construye · da soporte | externo | Implantar su paquete sin personalizaciones que no pueda mantener; relación a largo plazo | págs. 11-14, anexo 10 |

> **Dos poblaciones con la misma palabra**
>
> La traducción del caso llama «suministrador» tanto a los **proveedores de piezas** de Harley-Davidson (`STK-08`, actor del negocio) como a los **proveedores de software** que concursan (`STK-17`, que no es actor: no participa en la operación de las compras). En este documento «suministrador» es siempre el primero.

> **Lo que quedó fuera, y por qué**
>
> **Recursos Humanos** fue encuestado (pág. 8), pero su interés (la formación) ya lo trae Gestión del Cambio: entra como restricción `RE-10`. Los **proveedores de software no elegidos** y la **empresa de estudios del sector** intervienen solo en la selección, no en el sistema. Los miembros del equipo con nombre propio (Carter, Jarosz, Christianson, Doman, Peissig, Pues, Sarder, Walker) se agrupan en `STK-06`: representan a su centro o división, con el mismo interés.


## 3. Drivers arquitectónicos (criterio 3, 20 pts)

Los **drivers arquitectónicos** son los factores críticos que guían el diseño; hay tres tipos. Los **RF** moldean la estructura y se entregan como casos de uso expandidos. Los **de calidad** definen cómo debe comportarse el sistema y se entregan como escenarios con número. Los **de restricción** son condiciones impuestas desde afuera y se entregan como listado por categoría.


### 3.1 Drivers de requerimientos funcionales

Salen de las doce actividades de las tres fases (anexo 6b), de los diez criterios funcionales de la especificación (anexo 10) y de los beneficios esperados (anexo 3).

| Id | El sistema debe… | Proceso | Fuente |
|---|---|---|---|
| RF-01 | Registrar una solicitud de pedido por cualquier empleado autorizado | CDU-01 | anexo 6b, fase 1a |
| RF-02 | Importar los requisitos de material planificados (MRP/DRP) de cada centro | CDU-01 | anexo 6a «Requisitos» |
| RF-03 | Aprobar la solicitud según las reglas de autorización | CDU-01 | anexo 6b, fase 1a |
| RF-04 | Crear el pedido de compra y enviarlo al suministrador | CDU-01 | anexo 6b, fase 1b |
| RF-05 | Agrupar la demanda de centros y divisiones contra los contratos vigentes | CDU-01 | anexo 3 |
| RF-06 | Registrar la recepción de material contra el pedido | CDU-02 | anexo 6b, fase 1c |
| RF-07 | Seguir el estado y los plazos de cada pedido | CDU-02 | anexo 6b, fase 1c |
| RF-08 | Conciliar factura, pedido y recepción, y resolver discrepancias | CDU-02 | anexo 6b, fase 1d · anexo 5 |
| RF-09 | Enviar la factura conciliada a Cuentas de Acreedores para su pago | CDU-02 | anexo 6b, fase 1d |
| RF-10 | Mantener un registro único de suministradores y sus contactos | CDU-03 | anexo 6b, fase 2c · anexo 3 |
| RF-11 | Publicar al suministrador sus resultados y la demanda prevista | CDU-03 | anexo 3 |
| RF-12 | Evaluar los resultados del suministrador en calidad, costes y plazos | CDU-03 | anexo 6b, fase 2a |
| RF-13 | Intercambiar documentos de compra con el suministrador por Internet | CDU-03 | anexo 6b, fase 2b |
| RF-14 | Consolidar los datos de compras de toda la empresa para decidir | CDU-03 | anexo 3 |
| RF-15 | Planificar la participación de Compras y de suministradores en cada proyecto | CDU-04 | anexo 6b, fase 3b-c |
| RF-16 | Gestionar el coste objetivo de las piezas compradas de un proyecto | CDU-04 | anexo 6b, fase 3d |
| RF-17 | Controlar la preparación para la creación y el lanzamiento | CDU-04 | anexo 6b, fase 3e |
| RF-18 | Intercambiar datos con los sistemas existentes de Harley-Davidson | todos | anexo 10, criterio 8 · pág. 12 |

**Alcance por fases.** Como en el ejemplo de clase, el alcance se reparte en entregas; aquí son las tres fases del anexo 6b.

| Fase | Tema principal | Requerimientos que incluye |
|---|---|---|
| 1 | Procesos y sistemas de transacciones | RF-01 a RF-09, RF-18 |
| 2 | Información sobre suministradores | RF-10 a RF-14 |
| 3 | Seguimiento de proyectos | RF-15 a RF-17 |

**Casos de uso del sistema.** Cada uno nombra una meta completa del actor; ninguno es un «crear / editar / consultar».

| Id | Caso de uso | Proceso | Actores |
|---|---|---|---|
| CU-01 | Solicitar material o servicio | CDU-01 | Empleado solicitante |
| CU-02 | Emitir pedido de compra | CDU-01 | Comprador · Suministrador |
| CU-03 | Generar propuestas de pedido desde MRP/DRP | CDU-01 | Sistema MRP/DRP de planta |
| CU-04 | Aprobar solicitud de pedido | CDU-01 | Responsable de área |
| CU-05 | Recibir material contra pedido | CDU-02 | Recepcionista de almacén |
| CU-06 | Seguir el estado del pedido | CDU-02 | Comprador |
| CU-07 | Conciliar factura, pedido y recepción | CDU-02 | Suministrador · Sistema de Cuentas de Acreedores |
| CU-08 | Incorporar suministrador a la base de aprovisionamiento | CDU-03 | Comprador |
| CU-09 | Seguir su desempeño y la demanda prevista | CDU-03 | Suministrador |
| CU-10 | Evaluar resultados del suministrador | CDU-03 | Comprador |
| CU-11 | Analizar el gasto consolidado de la empresa | CDU-03 | Director de Compras |
| CU-12 | Planificar la participación de Compras en el proyecto | CDU-04 | Comprador de desarrollo · Ingeniero |
| CU-13 | Acordar el coste objetivo de una pieza | CDU-04 | Comprador de desarrollo · Ingeniero · Suministrador |
| CU-14 | Controlar la preparación para el lanzamiento | CDU-04 | Comprador de desarrollo |

| Id | Caso de uso de apoyo | Relación | Cuándo |
|---|---|---|---|
| CU-15 | Agrupar demanda contra contrato vigente | «include» de CU-02 y CU-03 | reutilizar: dos casos base lo comparten |
| CU-16 | Solicitar cotización a suministradores | «extend» de CU-02 | [no hay contrato vigente] |
| CU-17 | Resolver discrepancia de factura | «extend» de CU-07 | [factura, pedido y recepción no coinciden] |
| CU-18 | Reclamar retraso al suministrador | «extend» de CU-06 | [plazo de entrega vencido] |
| CU-19 | Calcular indicadores de calidad, coste y plazo | «include» de CU-09, CU-10 y CU-11 | reutilizar: tres casos base lo comparten |
| CU-20 | Escalar riesgo de lanzamiento | «extend» de CU-14 | [hito de preparación incumplido] |

> **Cómo leer las relaciones**
>
> **«include»**: el caso base lo ejecuta **siempre**; la flecha va del base al incluido. Aquí se usa para **reutilizar**: dos o tres casos base comparten el incluido.
>
> **«extend»**: ocurre **a veces**, bajo la condición entre corchetes; la flecha va de la extensión al base.
>
> Los cuatro diagramas están en el **plano del sistema**: actores y casos de uso sin la barra de negocio.

**Descripciones textuales.** Cada caso de uso se describe con la plantilla de clase: curso normal en dos columnas con una sola numeración, y cursos alternos anclados a la línea donde ocurren. Van agrupados por proceso, después de su diagrama.


#### CDU-01 Requisición y emisión del pedido de compra

![[02-Diagramas/caso-hd/3-drivers-rf/cdu-expandido-hd-01-requisicion.svg]]

*Figura 4. CDU-01 expandido.*


##### CU-01 Solicitar material o servicio

| Campo | Contenido |
|---|---|
| **Actores** | Empleado solicitante (inicia) |
| **Propósito** | Pedir un material o un servicio sin necesidad de formación previa y saber quién lo aprueba. |
| **Resumen** | Se inicia cuando el Empleado solicitante necesita un artículo. El sistema guía la solicitud y la deja pendiente de aprobación. Finaliza cuando el Responsable de área recibe el aviso. |
| **Requerimientos** | RF-01 |
| **Prioridad** | Alta |

| Acción del actor | Respuesta del sistema |
|---|---|
| **1.** El Empleado solicitante busca el artículo o servicio en el catálogo e indica cantidad, fecha requerida y centro de coste. |  |
|  | **2.** El sistema valida los datos y determina quién debe aprobar según las reglas de autorización. |
| **3.** El Empleado solicitante confirma la solicitud. |  |
|  | **4.** El sistema registra la solicitud con un número único, la deja pendiente de aprobación y avisa al Responsable de área. |

- **En la línea 1:** el artículo no está en el catálogo. El Empleado solicitante lo describe en texto libre y se continúa en la línea 2.
- **En la línea 2:** faltan datos obligatorios. El sistema señala los campos y se vuelve a la línea 1.


##### CU-02 Emitir pedido de compra

| Campo | Contenido |
|---|---|
| **Actores** | Comprador (inicia) · Suministrador |
| **Propósito** | Convertir la demanda aprobada en un pedido en firme con el suministrador asignado, al precio del contrato. |
| **Resumen** | Se inicia cuando el Comprador toma solicitudes aprobadas o propuestas generadas desde MRP/DRP. El sistema agrupa la demanda contra el contrato vigente y emite el pedido. Finaliza cuando el Suministrador lo recibe y confirma. |
| **Requerimientos** | RF-04, RF-05, RF-13 |
| **Prioridad** | Alta |

| Acción del actor | Respuesta del sistema |
|---|---|
| **1.** El Comprador selecciona las solicitudes aprobadas y las propuestas pendientes. |  |
|  | **2.** El sistema agrupa la demanda por suministrador y contrato vigente (incluye CU-15). |
| **3.** El Comprador revisa cantidades, fechas de entrega y centro de destino, y confirma. |  |
|  | **4.** El sistema registra el pedido de compra con su número único y lo envía al Suministrador. |
| **5.** El Suministrador recibe el pedido y confirma fecha y cantidad. |  |
|  | **6.** El sistema deja el pedido en firme y devuelve la fecha confirmada al sistema MRP/DRP del centro. |

- **En la línea 2:** no hay contrato vigente para el artículo. Se extiende con CU-16 y, con la oferta elegida, se continúa en la línea 3.
- **En la línea 5:** el Suministrador propone otra fecha. El sistema avisa al Comprador, que acepta o renegocia; con la fecha acordada se continúa en la línea 6.


##### CU-03 Generar propuestas de pedido desde MRP/DRP

| Campo | Contenido |
|---|---|
| **Actores** | Sistema MRP/DRP de planta (inicia) |
| **Propósito** | Transformar los requisitos de material planificados por cada centro en propuestas de pedido listas para emitir. |
| **Resumen** | Se inicia cuando el Sistema MRP/DRP de un centro envía sus requisitos de material. El sistema los valida, los agrupa y genera propuestas. Finaliza cuando las propuestas quedan en la bandeja del Comprador. |
| **Requerimientos** | RF-02, RF-04, RF-05, RF-18 |
| **Prioridad** | Alta |

| Acción del actor | Respuesta del sistema |
|---|---|
| **1.** El Sistema MRP/DRP de planta envía los requisitos de material planificados: pieza, cantidad y fecha. |  |
|  | **2.** El sistema valida cada pieza contra el registro de suministradores y descarta lo que ya está cubierto por pedidos en firme. |
|  | **3.** El sistema agrupa la demanda contra el contrato vigente (incluye CU-15). |
|  | **4.** El sistema genera las propuestas de pedido y las deja en la bandeja del Comprador. |
| **5.** El Sistema MRP/DRP de planta recibe el acuse de los requisitos procesados. |  |

- **En la línea 1:** el envío llega incompleto. El sistema rechaza el lote y pide el reenvío. Fin del caso de uso para ese lote.
- **En la línea 2:** una pieza no tiene suministrador asignado. El sistema genera la propuesta marcada «sin fuente» y alerta al Comprador; se continúa en la línea 3 con las demás.


##### CU-04 Aprobar solicitud de pedido

| Campo | Contenido |
|---|---|
| **Actores** | Responsable de área (inicia) |
| **Propósito** | Autorizar o rechazar una solicitud de pedido dejando constancia de quién decidió. |
| **Resumen** | Se inicia cuando el Responsable de área abre una solicitud pendiente. El sistema le muestra el detalle y registra su decisión. Finaliza cuando la solicitud aprobada llega a la bandeja del Comprador. |
| **Requerimientos** | RF-03 |
| **Prioridad** | Alta |

| Acción del actor | Respuesta del sistema |
|---|---|
| **1.** El Responsable de área abre una solicitud pendiente de aprobación. |  |
|  | **2.** El sistema muestra el detalle, el importe estimado y el presupuesto disponible del centro de coste. |
| **3.** El Responsable de área aprueba la solicitud. |  |
|  | **4.** El sistema registra la decisión con fecha y autor, pasa la solicitud a la bandeja del Comprador y actualiza el estado para el Empleado solicitante. |

- **En la línea 2:** el importe supera el límite del Responsable de área. El sistema deriva la solicitud al nivel siguiente y se continúa en la línea 1 con ese aprobador.
- **En la línea 3:** el Responsable de área rechaza la solicitud e indica el motivo. El sistema lo registra y avisa al Empleado solicitante. Fin del caso de uso.


##### CU-15 Agrupar demanda contra contrato vigente

| Campo | Contenido |
|---|---|
| **Actores** | Ninguno: caso de uso de apoyo, incluido por CU-02 y CU-03 |
| **Propósito** | Aprovechar los contratos de toda la empresa agrupando la demanda de centros y divisiones. |
| **Resumen** | Se inicia cuando un caso de uso base le entrega líneas de demanda. El sistema busca el contrato vigente y agrupa. Finaliza cuando devuelve los grupos al caso base. |
| **Requerimientos** | RF-05 |
| **Prioridad** | Alta |

| Acción del actor | Respuesta del sistema |
|---|---|
|  | **1.** El sistema recibe del caso de uso base las líneas de demanda. |
|  | **2.** El sistema busca el contrato vigente para cada artículo y suministrador. |
|  | **3.** El sistema agrupa las líneas de todos los centros y divisiones bajo un mismo contrato y aplica su precio y condiciones. |
|  | **4.** El sistema devuelve los grupos al caso de uso base. |

- **En la línea 2:** no existe contrato vigente. El sistema devuelve la línea marcada «sin contrato» al caso de uso base.


##### CU-16 Solicitar cotización a suministradores

| Campo | Contenido |
|---|---|
| **Actores** | Comprador (desde CU-02) · Suministrador |
| **Propósito** | Obtener precio y plazo cuando un artículo no tiene contrato vigente. Extiende a CU-02 bajo la condición [no hay contrato vigente]. |
| **Resumen** | Se inicia en la línea 2 de CU-02 cuando no hay contrato vigente. El sistema pide ofertas y las compara. Finaliza cuando la oferta elegida vuelve a CU-02. |
| **Requerimientos** | RF-04, RF-13 |
| **Prioridad** | Media |

| Acción del actor | Respuesta del sistema |
|---|---|
| **1.** El Comprador selecciona los suministradores candidatos del registro. |  |
|  | **2.** El sistema envía la solicitud de cotización con su plazo de respuesta. |
| **3.** El Suministrador responde con precio y plazo de entrega. |  |
|  | **4.** El sistema compara las ofertas recibidas y las muestra al Comprador. |
| **5.** El Comprador elige una oferta. |  |
|  | **6.** El sistema registra la oferta elegida y devuelve el control a la línea 3 de CU-02. |

- **En la línea 3:** ningún Suministrador responde dentro del plazo. El sistema avisa al Comprador, que amplía el plazo o cambia los candidatos; se continúa en la línea 2.


#### CDU-02 Recepción, seguimiento y pago al suministrador

![[02-Diagramas/caso-hd/3-drivers-rf/cdu-expandido-hd-02-recepcion.svg]]

*Figura 5. CDU-02 expandido.*


##### CU-05 Recibir material contra pedido

| Campo | Contenido |
|---|---|
| **Actores** | Recepcionista de almacén (inicia) |
| **Propósito** | Registrar en el muelle lo que llega, contra el pedido, aunque no haya red. |
| **Resumen** | Se inicia cuando llega una entrega al muelle. El sistema muestra lo pendiente del pedido y registra lo recibido. Finaliza cuando la recepción queda registrada y publicada. |
| **Requerimientos** | RF-06, RF-18 |
| **Prioridad** | Alta |

| Acción del actor | Respuesta del sistema |
|---|---|
| **1.** El Recepcionista de almacén lee el código del pedido en el documento de entrega. |  |
|  | **2.** El sistema muestra las líneas pendientes de ese pedido. |
| **3.** El Recepcionista de almacén registra las cantidades recibidas y su estado. |  |
|  | **4.** El sistema registra la recepción, actualiza lo pendiente del pedido y publica el evento «material recibido». |

- **En la línea 1:** no hay conexión. La aplicación guarda el registro en su cola local y lo sincroniza al volver la red; se continúa en la línea 3.
- **En la línea 3:** la cantidad no coincide o el material llega dañado. El sistema registra la diferencia y avisa al Comprador; se continúa en la línea 4.


##### CU-06 Seguir el estado del pedido

| Campo | Contenido |
|---|---|
| **Actores** | Comprador (inicia) |
| **Propósito** | Saber en qué estado está cada pedido sin perseguirlo por correo o teléfono. |
| **Resumen** | Se inicia cuando el Comprador revisa sus pedidos abiertos. El sistema muestra el estado y los plazos. Finaliza cuando el Comprador ha visto el historial del pedido. |
| **Requerimientos** | RF-07, RF-13 |
| **Prioridad** | Alta |

| Acción del actor | Respuesta del sistema |
|---|---|
| **1.** El Comprador abre la lista de pedidos abiertos de su cartera. |  |
|  | **2.** El sistema muestra el estado, la fecha confirmada y los pedidos próximos a vencer. |
| **3.** El Comprador abre un pedido. |  |
|  | **4.** El sistema muestra su historial: confirmación, aviso de envío y recepciones. |

- **En la línea 2:** un pedido tiene el plazo de entrega vencido sin recepción. Se extiende con CU-18.


##### CU-07 Conciliar factura, pedido y recepción

| Campo | Contenido |
|---|---|
| **Actores** | Suministrador (inicia) · Sistema de Cuentas de Acreedores |
| **Propósito** | Pagar solo las facturas que coinciden con el pedido y con lo recibido. |
| **Resumen** | Se inicia cuando el Suministrador presenta una factura. El sistema la compara con el pedido y la recepción. Finaliza cuando el Suministrador conoce el estado del pago. |
| **Requerimientos** | RF-08, RF-09, RF-13, RF-18 |
| **Prioridad** | Alta |

| Acción del actor | Respuesta del sistema |
|---|---|
| **1.** El Suministrador presenta la factura por el portal o por la interfaz de su sistema. |  |
|  | **2.** El sistema comprueba que la factura no sea repetida y localiza su pedido y sus recepciones. |
|  | **3.** El sistema compara cantidades y precios de la factura, el pedido y la recepción. |
|  | **4.** El sistema marca la factura como conciliada y la envía al Sistema de Cuentas de Acreedores. |
| **5.** El Sistema de Cuentas de Acreedores devuelve el estado del pago. |  |
|  | **6.** El sistema informa al Suministrador del estado del pago. |

- **En la línea 2:** la factura ya fue presentada. El sistema la rechaza indicando la original. Fin del caso de uso.
- **En la línea 3:** factura, pedido y recepción no coinciden. Se extiende con CU-17.


##### CU-17 Resolver discrepancia de factura

| Campo | Contenido |
|---|---|
| **Actores** | Comprador (inicia) |
| **Propósito** | Decidir qué se hace con una factura que no coincide. Extiende a CU-07 bajo la condición [factura, pedido y recepción no coinciden]. |
| **Resumen** | Se inicia en la línea 3 de CU-07 cuando hay diferencias. El sistema las muestra y registra la decisión. Finaliza cuando la factura vuelve a CU-07 o queda rechazada. |
| **Requerimientos** | RF-08 |
| **Prioridad** | Media |

| Acción del actor | Respuesta del sistema |
|---|---|
|  | **1.** El sistema muestra al Comprador la diferencia línea por línea. |
| **2.** El Comprador acepta la diferencia o pide una corrección al Suministrador. |  |
|  | **3.** El sistema registra la decisión y su motivo. |
|  | **4.** El sistema devuelve la factura a la línea 4 de CU-07. |

- **En la línea 2:** el Comprador rechaza la factura. El sistema avisa al Suministrador con el motivo. Fin del caso de uso para esa factura.


##### CU-18 Reclamar retraso al suministrador

| Campo | Contenido |
|---|---|
| **Actores** | Comprador (desde CU-06) · Suministrador |
| **Propósito** | Reclamar una entrega atrasada y dejar el retraso registrado. Extiende a CU-06 bajo la condición [plazo de entrega vencido]. |
| **Resumen** | Se inicia en la línea 2 de CU-06 cuando un plazo venció. El sistema envía el reclamo y recibe la nueva fecha. Finaliza cuando la fecha comprometida queda actualizada. |
| **Requerimientos** | RF-07, RF-12, RF-13 |
| **Prioridad** | Media |

| Acción del actor | Respuesta del sistema |
|---|---|
|  | **1.** El sistema señala el pedido con plazo vencido y propone el reclamo. |
| **2.** El Comprador confirma el reclamo. |  |
|  | **3.** El sistema envía el reclamo al Suministrador y lo registra. |
| **4.** El Suministrador responde con la nueva fecha y la causa del retraso. |  |
|  | **5.** El sistema actualiza la fecha comprometida, registra el retraso para la evaluación del suministrador y avisa al centro de producción. |

- **En la línea 4:** el Suministrador no responde en dos días hábiles. El sistema escala el reclamo a la Dirección de Compras. Fin del caso de uso.


#### CDU-03 Gestión de la información y la relación con suministradores

![[02-Diagramas/caso-hd/3-drivers-rf/cdu-expandido-hd-03-suministradores.svg]]

*Figura 6. CDU-03 expandido.*


##### CU-08 Incorporar suministrador a la base de aprovisionamiento

| Campo | Contenido |
|---|---|
| **Actores** | Comprador (inicia) |
| **Propósito** | Dar de alta a un suministrador una sola vez para toda la empresa. |
| **Resumen** | Se inicia cuando el Comprador incorpora un suministrador nuevo. El sistema comprueba que no exista y crea su registro. Finaliza cuando el registro queda disponible para todos los centros. |
| **Requerimientos** | RF-10 |
| **Prioridad** | Alta |

| Acción del actor | Respuesta del sistema |
|---|---|
| **1.** El Comprador registra los datos del suministrador, sus contactos, las piezas que suministra y los centros que atiende. |  |
|  | **2.** El sistema comprueba que el suministrador no exista ya y valida los datos. |
| **3.** El Comprador confirma el alta. |  |
|  | **4.** El sistema crea el registro único, habilita el acceso al portal para sus contactos y lo deja disponible para todos los centros. |

- **En la línea 2:** el suministrador ya existe. El sistema muestra el registro existente para actualizarlo. Fin del caso de uso.


##### CU-09 Seguir su desempeño y la demanda prevista

| Campo | Contenido |
|---|---|
| **Actores** | Suministrador (inicia) |
| **Propósito** | Que el suministrador conozca cómo lo evalúa Harley-Davidson y qué demanda viene. |
| **Resumen** | Se inicia cuando el Suministrador entra al portal. El sistema calcula sus indicadores y muestra la demanda prevista. Finaliza cuando el Suministrador ha visto sus datos. |
| **Requerimientos** | RF-11, RF-12, RF-13 |
| **Prioridad** | Alta |

| Acción del actor | Respuesta del sistema |
|---|---|
| **1.** El Suministrador entra al portal y se autentica con doble factor. |  |
|  | **2.** El sistema calcula sus indicadores de calidad, coste y plazo (incluye CU-19). |
|  | **3.** El sistema muestra sus resultados y la demanda prevista de las piezas que suministra. |
| **4.** El Suministrador abre el detalle de un indicador o de un periodo. |  |
|  | **5.** El sistema muestra los pedidos y las recepciones que componen ese indicador. |

- **En la línea 4:** el Suministrador intenta ver datos de otro suministrador. El sistema rechaza la petición y la registra en la bitácora. Fin del caso de uso.


##### CU-10 Evaluar resultados del suministrador

| Campo | Contenido |
|---|---|
| **Actores** | Comprador (inicia) |
| **Propósito** | Evaluar al suministrador con datos, no con impresiones. |
| **Resumen** | Se inicia cuando el Comprador evalúa un suministrador en un periodo. El sistema calcula los indicadores y registra la evaluación. Finaliza cuando la evaluación queda publicada al suministrador. |
| **Requerimientos** | RF-12 |
| **Prioridad** | Media |

| Acción del actor | Respuesta del sistema |
|---|---|
| **1.** El Comprador selecciona el suministrador y el periodo. |  |
|  | **2.** El sistema calcula los indicadores de calidad, coste y plazo (incluye CU-19). |
| **3.** El Comprador agrega su valoración y las acciones de mejora acordadas. |  |
|  | **4.** El sistema registra la evaluación y la publica al suministrador. |

- **En la línea 2:** no hay datos suficientes en el periodo. El sistema lo indica y propone ampliar el periodo; se continúa en la línea 1.


##### CU-11 Analizar el gasto consolidado de la empresa

| Campo | Contenido |
|---|---|
| **Actores** | Director de Compras (inicia) |
| **Propósito** | Ver el gasto de toda la empresa en un solo lugar para decidir. |
| **Resumen** | Se inicia cuando el Director de Compras consulta el gasto. El sistema consolida los datos de todos los centros. Finaliza cuando el Director de Compras ha visto el detalle que necesita. |
| **Requerimientos** | RF-14 |
| **Prioridad** | Media |

| Acción del actor | Respuesta del sistema |
|---|---|
| **1.** El Director de Compras elige el periodo, la división y el centro. |  |
|  | **2.** El sistema consolida el gasto de todos los centros y calcula los indicadores (incluye CU-19). |
|  | **3.** El sistema muestra el gasto por suministrador, categoría y centro, y las oportunidades de agrupar demanda. |
| **4.** El Director de Compras profundiza en un suministrador o una categoría. |  |
|  | **5.** El sistema muestra el detalle. |

- **En la línea 2:** un centro todavía no migró. El sistema usa su histórico e indica qué datos provienen del sistema de compras local; se continúa en la línea 3.


##### CU-19 Calcular indicadores de calidad, coste y plazo

| Campo | Contenido |
|---|---|
| **Actores** | Ninguno: caso de uso de apoyo, incluido por CU-09, CU-10 y CU-11 |
| **Propósito** | Calcular de una sola forma los indicadores que usan el suministrador, el comprador y la dirección. |
| **Resumen** | Se inicia cuando un caso de uso base le entrega suministrador y periodo. El sistema calcula los tres indicadores. Finaliza cuando los devuelve al caso base. |
| **Requerimientos** | RF-12 |
| **Prioridad** | Alta |

| Acción del actor | Respuesta del sistema |
|---|---|
|  | **1.** El sistema recibe del caso de uso base el suministrador y el periodo. |
|  | **2.** El sistema toma las recepciones, los rechazos, los precios y las fechas de entrega del periodo. |
|  | **3.** El sistema calcula calidad (recepciones conformes), coste (variación frente al precio de contrato) y plazo (entregas a tiempo). |
|  | **4.** El sistema devuelve los indicadores al caso de uso base. |

- **En la línea 2:** no hay datos en el periodo. El sistema devuelve los indicadores marcados «sin datos».


#### CDU-04 Seguimiento de compras en proyectos de nuevos productos

![[02-Diagramas/caso-hd/3-drivers-rf/cdu-expandido-hd-04-proyectos.svg]]

*Figura 7. CDU-04 expandido.*


##### CU-12 Planificar la participación de Compras en el proyecto

| Campo | Contenido |
|---|---|
| **Actores** | Ingeniero del Centro de Desarrollo (inicia) · Comprador de desarrollo |
| **Propósito** | Integrar a Compras y a los suministradores desde el inicio de un proyecto de nuevo producto. |
| **Resumen** | Se inicia cuando arranca un proyecto de nuevo producto. El sistema registra piezas, hitos y responsables. Finaliza cuando queda el calendario de compras del proyecto. |
| **Requerimientos** | RF-15, RF-18 |
| **Prioridad** | Media |

| Acción del actor | Respuesta del sistema |
|---|---|
| **1.** El Ingeniero del Centro de Desarrollo comparte el plan del proyecto y la lista de piezas compradas. |  |
|  | **2.** El sistema registra el proyecto, sus piezas y sus hitos. |
| **3.** El Comprador de desarrollo asigna a cada pieza un suministrador candidato y un comprador responsable. |  |
|  | **4.** El sistema registra la asignación de recursos y el calendario de compras del proyecto. |

- **En la línea 3:** una pieza no tiene suministrador en la base. El Comprador de desarrollo lo incorpora con CU-08 y se continúa en la línea 3.


##### CU-13 Acordar el coste objetivo de una pieza

| Campo | Contenido |
|---|---|
| **Actores** | Ingeniero del Centro de Desarrollo (inicia) · Comprador de desarrollo · Suministrador |
| **Propósito** | Fijar el coste objetivo de una pieza comprada antes de que el diseño quede cerrado. |
| **Resumen** | Se inicia cuando una pieza del proyecto necesita coste objetivo. El sistema registra la propuesta y la oferta. Finaliza cuando el coste acordado queda registrado. |
| **Requerimientos** | RF-16 |
| **Prioridad** | Media |

| Acción del actor | Respuesta del sistema |
|---|---|
| **1.** El Ingeniero del Centro de Desarrollo propone el coste objetivo de la pieza. |  |
|  | **2.** El sistema lo registra y lo comunica al Suministrador candidato. |
| **3.** El Suministrador responde con su oferta. |  |
|  | **4.** El sistema compara la oferta con el coste objetivo. |
| **5.** El Comprador de desarrollo acuerda el coste con las partes. |  |
|  | **6.** El sistema registra el coste objetivo acordado. |

- **En la línea 4:** la oferta supera el coste objetivo. El sistema muestra la diferencia; el Comprador de desarrollo renegocia y se vuelve a la línea 3, o pide revisar el diseño y se vuelve a la línea 1.


##### CU-14 Controlar la preparación para el lanzamiento

| Campo | Contenido |
|---|---|
| **Actores** | Comprador de desarrollo (inicia) |
| **Propósito** | Saber, pieza por pieza, si los suministradores llegan a tiempo al lanzamiento. |
| **Resumen** | Se inicia cuando el Comprador de desarrollo revisa un proyecto. El sistema muestra los hitos de preparación. Finaliza cuando el avance queda registrado. |
| **Requerimientos** | RF-17 |
| **Prioridad** | Media |

| Acción del actor | Respuesta del sistema |
|---|---|
| **1.** El Comprador de desarrollo abre el proyecto. |  |
|  | **2.** El sistema muestra, por pieza y suministrador, los hitos de preparación y su estado. |
| **3.** El Comprador de desarrollo actualiza el estado de un hito. |  |
|  | **4.** El sistema registra el avance y recalcula el estado del proyecto. |

- **En la línea 2:** un hito de preparación está incumplido. Se extiende con CU-20.


##### CU-20 Escalar riesgo de lanzamiento

| Campo | Contenido |
|---|---|
| **Actores** | Comprador de desarrollo (inicia) |
| **Propósito** | Hacer visible a tiempo un riesgo para la fecha de lanzamiento. Extiende a CU-14 bajo la condición [hito de preparación incumplido]. |
| **Resumen** | Se inicia en la línea 2 de CU-14 cuando un hito está incumplido. El sistema registra el riesgo y lo comunica. Finaliza cuando el riesgo queda abierto y asignado. |
| **Requerimientos** | RF-17 |
| **Prioridad** | Media |

| Acción del actor | Respuesta del sistema |
|---|---|
|  | **1.** El sistema señala el hito incumplido y su efecto sobre la fecha de lanzamiento. |
| **2.** El Comprador de desarrollo describe el riesgo y propone una acción. |  |
|  | **3.** El sistema registra el riesgo y lo comunica al equipo del proyecto. |
|  | **4.** El sistema mantiene el riesgo abierto hasta que el hito se cumpla. |

- **En la línea 2:** el Comprador de desarrollo reprograma el hito sin riesgo para el lanzamiento. El sistema registra la nueva fecha. Fin del caso de uso.


### 3.2 Drivers de atributos de calidad

> **Qué taxonomía se usa**
>
> Las categorías siguen el ejemplo de clase (desempeño, disponibilidad, seguridad, usabilidad, modificabilidad) y la lista de drivers de calidad de clase (escalabilidad, fiabilidad). Se agregan **compatibilidad** y **portabilidad** porque el caso las evalúa por su nombre (anexo 10). La tabla ubica cada una en el modelo ISO/IEC 25010 que se determina en el §6.4.
>
> **Prioridad:** el par (importancia para el negocio, dificultad técnica), cada uno en A alta, M media o B baja, como en el ejemplo de clase.
>
> **De dónde salen los números:** el caso da cifras de **negocio** (34 M USD, 70 %, 85 %), no de comportamiento del sistema. Las medidas son **supuestos de diseño**, derivados de los volúmenes del caso (200 compradores, 800 usuarios objetivo, más de 2.000 solicitantes).

| Id | Categoría | Característica ISO/IEC 25010 | Motivo en el caso | Medida de la respuesta | Prioridad | Stakeholders | Fuente |
|---|---|---|---|---|---|---|---|
| EAC-01 | Disponibilidad | Fiabilidad › disponibilidad | La compra no puede parar la producción | 99,9 % mensual; conmutación en ≤ 15 min; la recepción sigue sin conexión y sincroniza sin pérdida | (A, A) | STK-15, STK-10, STK-14 | pág. 6 |
| EAC-02 | Desempeño | Eficiencia de desempeño › comportamiento temporal | Operación interactiva del comprador y del solicitante | ≤ 2 s en el percentil 95 con 800 usuarios concurrentes | (A, M) | STK-06, STK-07 | pág. 10 (800 usuarios) |
| EAC-03 | Escalabilidad | Eficiencia de desempeño › capacidad | De 200 compradores a toda la empresa y sus suministradores | De 800 a 3.000 usuarios agregando nodos, con 0 cambios de código y sin salir de EAC-02 | (M, M) | STK-02, STK-10 | pág. 8 · Plan 2003 |
| EAC-04 | Seguridad | Seguridad › confidencialidad, autenticidad, responsabilidad | Suministradores externos entran por Internet | 100 % de accesos externos con doble factor; TLS 1.3; AES-256 en reposo; 0 lecturas de datos de otro suministrador | (A, A) | STK-08, STK-09, STK-13 | anexo 6b, fase 2 |
| EAC-05 | Usabilidad | Usabilidad › capacidad de aprendizaje, operabilidad | 2.000 solicitantes ocasionales; el caso evalúa «facilidad de uso» | Primera solicitud sin formación en ≤ 3 min y ≤ 5 pasos, lograda por el 90 % de los solicitantes | (A, M) | STK-07, STK-11, STK-06 | anexo 10 |
| EAC-06 | Compatibilidad | Compatibilidad › interoperabilidad, coexistencia | Un proveedor fue eliminado por «incompatibilidad arquitectónica» | 100 % de las interfaces por API o mensajería estándar; un sistema de planta más se integra en ≤ 10 días-persona sin tocar los servicios de negocio | (A, A) | STK-09, STK-10, STK-05 | págs. 9, 12 · anexo 10 |
| EAC-07 | Modificabilidad | Mantenibilidad › modularidad, capacidad de ser modificado | «Reducción del mantenimiento del sistema y de los costes de obsolescencia» | Un cambio de regla de aprobación llega a producción en ≤ 1 día hábil tocando 1 servicio; ≥ 80 % de cobertura de pruebas en los adaptadores | (M, M) | STK-10, STK-17, STK-02 | anexo 3 |
| EAC-08 | Portabilidad | Portabilidad › adaptabilidad, capacidad de ser instalado | El caso califica la «portabilidad de plataformas» | El mismo paquete de despliegue se levanta en otra nube o centro de datos en ≤ 5 días hábiles con 0 cambios de código | (B, M) | STK-09 | anexo 10 |
| EAC-09 | Fiabilidad | Fiabilidad › tolerancia a fallos · Seguridad › integridad | «Eliminación de registros duplicados» y «corrección de errores» | 0 pedidos o facturas duplicados ante reintentos; 100 % de las facturas conciliadas a tres bandas antes del pago | (A, M) | STK-13, STK-06, STK-12 | anexo 3 |

> **Prioridad**
>
> Con los dos ejes (importancia para el negocio y dificultad técnica) los que más pesan en el diseño son **EAC-01, EAC-04 y EAC-06**, los tres (A, A),  seguidos de EAC-02, EAC-05 y EAC-09, que son (A, M). Las restricciones no se priorizan: todas son obligatorias.

**Escenarios de atributos de calidad (EaC).** Cada driver se especifica en seis partes: quién o qué lo provoca (fuente de estímulo), qué ocurre (estímulo), sobre qué parte (artefacto), en qué condiciones (entorno), qué hace el sistema (respuesta) y cómo se comprueba (medida de la respuesta). Sin medida no es un driver. El formato de seis partes es el de Bass, Clements y Kazman (2021) y el del ejemplo visto en clase.

| ID | Categoría | Escenario | Prioridad |
|---|---|---|---|
| EAC-01 | Disponibilidad | **Fuente de estímulo:** La infraestructura de la plataforma.<br>**Estímulo:** Falla un nodo de aplicación o la base de datos primaria.<br>**Artefacto:** Clúster de contenedores y servidor de base de datos.<br>**Entorno:** Operación normal, turno de planta con recepciones en curso.<br>**Respuesta:** El tráfico pasa a los nodos sanos y la base en espera toma el relevo; la tableta de recepción sigue registrando en su cola local.<br>**Medida de la respuesta:** 99,9 % mensual · relevo en ≤ 15 min · 0 recepciones perdidas. | (A, A) |
| EAC-02 | Desempeño | **Fuente de estímulo:** Comprador.<br>**Estímulo:** Emite un pedido de compra con 20 líneas.<br>**Artefacto:** Servicio Requisición y Pedido.<br>**Entorno:** Carga pico: 800 usuarios concurrentes.<br>**Respuesta:** El pedido queda registrado y enviado al suministrador.<br>**Medida de la respuesta:** ≤ 2 s en el percentil 95. | (A, M) |
| EAC-03 | Escalabilidad | **Fuente de estímulo:** Dirección de Sistemas.<br>**Estímulo:** Se incorporan los 2.000 solicitantes y los suministradores de la fase 2.<br>**Artefacto:** Plataforma completa.<br>**Entorno:** Crecimiento planificado entre fases.<br>**Respuesta:** Se agregan nodos al clúster; los servicios no cambian.<br>**Medida de la respuesta:** De 800 a 3.000 usuarios · 0 cambios de código · EAC-02 se mantiene. | (M, M) |
| EAC-04 | Seguridad | **Fuente de estímulo:** Usuario de un suministrador, autenticado.<br>**Estímulo:** Intenta consultar pedidos de otro suministrador.<br>**Artefacto:** API Gateway y Servicio Suministradores.<br>**Entorno:** Acceso por Internet.<br>**Respuesta:** La petición se rechaza y queda en la bitácora de auditoría.<br>**Medida de la respuesta:** 0 lecturas cruzadas · rechazo y registro en ≤ 1 s · 100 % de accesos externos con doble factor. | (A, A) |
| EAC-05 | Usabilidad | **Fuente de estímulo:** Empleado solicitante sin formación.<br>**Estímulo:** Necesita pedir un artículo por primera vez.<br>**Artefacto:** Aplicación web SiL'K.<br>**Entorno:** Uso ocasional, desde su PC de oficina.<br>**Respuesta:** Completa la solicitud guiado por el catálogo y ve a quién le toca aprobarla.<br>**Medida de la respuesta:** ≤ 3 min · ≤ 5 pasos · 90 % lo logra al primer intento. | (A, M) |
| EAC-06 | Compatibilidad | **Fuente de estímulo:** Equipo de Sistemas.<br>**Estímulo:** Hay que conectar el MRP/DRP de un centro más.<br>**Artefacto:** Servicio de Integración (adaptadores).<br>**Entorno:** Mantenimiento, con la solución en producción.<br>**Respuesta:** Se agrega un adaptador; los servicios de negocio no se modifican.<br>**Medida de la respuesta:** ≤ 10 días-persona · 0 servicios de negocio modificados. | (A, A) |
| EAC-07 | Modificabilidad | **Fuente de estímulo:** Dirección de Compras.<br>**Estímulo:** Cambia el límite de aprobación de un tipo de compra.<br>**Artefacto:** Servicio Requisición y Pedido.<br>**Entorno:** Mantenimiento.<br>**Respuesta:** La regla se cambia por configuración, se prueba y se despliega.<br>**Medida de la respuesta:** ≤ 1 día hábil · 1 servicio tocado. | (M, M) |
| EAC-08 | Portabilidad | **Fuente de estímulo:** Grupo de Integración de Arquitecturas.<br>**Estímulo:** Cambia la norma de infraestructura y hay que mover la plataforma.<br>**Artefacto:** Paquete de despliegue.<br>**Entorno:** Cambio planificado.<br>**Respuesta:** La misma definición de infraestructura levanta la solución en el nuevo entorno.<br>**Medida de la respuesta:** ≤ 5 días hábiles · 0 cambios de código. | (B, M) |
| EAC-09 | Fiabilidad | **Fuente de estímulo:** Sistema del suministrador.<br>**Estímulo:** Reenvía la misma factura tras un corte de red.<br>**Artefacto:** Servicio Recepción y Facturas y cola de reintentos.<br>**Entorno:** Red inestable.<br>**Respuesta:** El segundo envío se reconoce como repetido y no genera otro registro.<br>**Medida de la respuesta:** 0 duplicados · 100 % de facturas conciliadas antes del pago. | (A, M) |


### 3.3 Drivers de restricción

Por las seis categorías de clase. El caso no cita ninguna norma legal: las dos regulatorias son **supuestos** de traer el caso al presente, y van rotuladas.

| Id | Categoría | Restricción | Fuente | Stakeholders |
|---|---|---|---|---|
| RE-01 | Tecnológica | Compatible con la arquitectura de sistemas existente y con las normas de hardware y software del grupo de Integración de Arquitecturas | pág. 9, nota 12 · pág. 12 | STK-09 |
| RE-02 | Tecnológica | La solución parte de un paquete de mercado: el proyecto selecciona software, no lo desarrolla desde cero | págs. 1, 10 | STK-05, STK-17 |
| RE-03 | Tecnológica | Los suministradores acceden por Internet (la «red Internet de Suministros») | anexo 6b, fase 2 | STK-08, STK-01 |
| RE-04 | De negocio | No es un ERP completo: el ámbito está delimitado y no se aceptan funcionalidades adicionales | pág. 11 · anexo 6a | STK-05, STK-03 |
| RE-05 | De negocio | Implantación en tres fases: transacciones, información sobre suministradores, seguimiento de proyectos | anexo 6b | STK-05, STK-03 |
| RE-06 | De negocio | El coste total tiene que caber en la propuesta de valor de 34 M USD en cinco años | pág. 7 · anexo 10 | STK-01, STK-03, STK-10 |
| RE-07 | De negocio | El proveedor debe poder dar soporte a largo plazo (uno fue eliminado por su pequeño tamaño) | pág. 12 | STK-17, STK-01 |
| RE-08 | Organizacional | Un único proceso común para todos los centros y las cuatro divisiones de compras | págs. 4, 8 · anexo 3 | STK-12, STK-04, STK-03 |
| RE-09 | Organizacional | La inversión la aprueba el Círculo de Tecnologías de la Información del Grupo de Fabricación | pág. 3 | STK-10, STK-05 |
| RE-10 | Organizacional | La formación y la gestión del cambio son parte de la implantación (800 personas; el cambio lo dirigen las personas en un 50-75 % y la tecnología solo en un 5-10 %) | pág. 10 · anexo 9 | STK-11, STK-04 |
| RE-11 | Ambiental / física | Usuarios repartidos en siete centros de tres estados y filiales en cinco países | pág. 2 · anexo 2a | STK-06, STK-02 |
| RE-12 | Ambiental / física | La implantación no puede interrumpir las líneas de producción | pág. 6 | STK-15, STK-10 |
| RE-13 | De integración | Interconexión con los sistemas en funcionamiento (MRP/DRP de planta, cuentas de acreedores, ingeniería) y con las iniciativas de tecnología en marcha | pág. 12 | STK-09, STK-10 |
| RE-14 | De integración | Coexistencia con los sistemas de compras locales de cada centro mientras dura la migración por fases | pág. 4 · anexo 6b | STK-06, STK-15 |
| RE-15 | Regulatoria (supuesto) | Control interno financiero de una empresa cotizada: segregación de funciones y rastro de auditoría en aprobaciones y pagos | supuesto «al presente», pág. 2 (cotiza desde 1986) | STK-13, STK-02 |
| RE-16 | Regulatoria (supuesto) | Protección de los datos personales de los contactos de suministradores en las filiales europeas | supuesto «al presente», pág. 2 (filiales en Europa) | STK-08, STK-02 |


## 4. Matrices de trazabilidad (criterio 4, 15 pts)

Las cuatro matrices cruzan los artefactos de los criterios 1, 2 y 3: los **procesos y casos de uso** (criterio 1 y su expansión), los **stakeholders** (criterio 2) y los **requerimientos** (criterio 3).

Están **acopladas**: la matriz 3 no se llenó a mano, se **derivó** de la 1 y la 2 (un stakeholder se relaciona con un caso de uso si le interesa algún requisito que ese caso realiza). Así no pueden contradecirse.


### 4.1 Matriz 1: Stakeholders vs. Requerimientos

| Stakeholder \ RF- | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| STK-01 VP Gestión de Materiales |  |  |  |  | X |  |  |  |  |  | X | X |  | X | X |  |  |  |
| STK-02 VP Servicios de Información |  |  |  |  |  |  |  |  |  |  |  |  |  | X |  |  |  | X |
| STK-03 Grupo de Unidad de Compras |  |  |  |  | X |  |  |  |  |  |  | X |  | X |  |  |  |  |
| STK-04 Dir. Planif. y Control de Compras |  | X |  | X | X |  | X |  |  |  |  |  |  | X |  |  |  |  |
| STK-05 Director del proyecto |  |  |  |  |  |  |  |  |  |  |  |  | X |  |  |  |  | X |
| STK-06 Compradores |  | X | X | X | X | X | X | X |  | X |  | X | X |  |  |  |  |  |
| STK-07 Empleados solicitantes | X |  | X |  |  |  | X |  |  |  |  |  |  |  |  |  |  |  |
| STK-08 Suministradores |  |  |  | X |  |  |  |  | X | X | X |  | X |  |  | X |  |  |
| STK-09 Integración de Arquitecturas |  |  |  |  |  |  |  |  |  |  |  |  | X |  |  |  |  | X |
| STK-10 Sistemas del Grupo de Fabricación |  | X |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | X |
| STK-11 Gestión del Cambio |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| STK-12 Innovación de Procesos | X |  |  | X |  | X |  | X |  |  |  |  |  |  |  |  |  |  |
| STK-13 Cuentas de Acreedores |  |  |  |  |  |  |  | X | X |  |  |  |  |  |  |  |  |  |
| STK-14 Logística |  |  |  |  |  | X | X |  |  |  |  |  |  |  |  |  |  |  |
| STK-15 Fabricación |  | X |  |  |  | X | X |  |  |  |  |  |  |  |  |  |  |  |
| STK-16 Ingeniería |  |  |  |  |  |  |  |  |  |  |  |  |  |  | X | X | X |  |
| STK-17 Proveedor del software |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | X |

Los requerimientos de calidad y de restricción también tienen dueño:

| Stakeholder | EAC-01 | EAC-02 | EAC-03 | EAC-04 | EAC-05 | EAC-06 | EAC-07 | EAC-08 | EAC-09 |
|---|---|---|---|---|---|---|---|---|---|
| STK-01 VP Gestión de Materiales |  |  |  |  |  |  |  |  |  |
| STK-02 VP Servicios de Información |  |  | X |  |  |  | X |  |  |
| STK-03 Grupo de Unidad de Compras |  |  |  |  |  |  |  |  |  |
| STK-04 Dir. Planif. y Control de Compras |  |  |  |  |  |  |  |  |  |
| STK-05 Director del proyecto |  |  |  |  |  | X |  |  |  |
| STK-06 Compradores |  | X |  |  | X |  |  |  | X |
| STK-07 Empleados solicitantes |  | X |  |  | X |  |  |  |  |
| STK-08 Suministradores |  |  |  | X |  |  |  |  |  |
| STK-09 Integración de Arquitecturas |  |  |  | X |  | X |  | X |  |
| STK-10 Sistemas del Grupo de Fabricación | X |  | X |  |  | X | X |  |  |
| STK-11 Gestión del Cambio |  |  |  |  | X |  |  |  |  |
| STK-12 Innovación de Procesos |  |  |  |  |  |  |  |  | X |
| STK-13 Cuentas de Acreedores |  |  |  | X |  |  |  |  | X |
| STK-14 Logística | X |  |  |  |  |  |  |  |  |
| STK-15 Fabricación | X |  |  |  |  |  |  |  |  |
| STK-16 Ingeniería |  |  |  |  |  |  |  |  |  |
| STK-17 Proveedor del software |  |  |  |  |  |  | X |  |  |

| Stakeholder | RE-01 | RE-02 | RE-03 | RE-04 | RE-05 | RE-06 | RE-07 | RE-08 | RE-09 | RE-10 | RE-11 | RE-12 | RE-13 | RE-14 | RE-15 | RE-16 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| STK-01 VP Gestión de Materiales |  |  | X |  |  | X | X |  |  |  |  |  |  |  |  |  |
| STK-02 VP Servicios de Información |  |  |  |  |  |  |  |  |  |  | X |  |  |  | X | X |
| STK-03 Grupo de Unidad de Compras |  |  |  | X | X | X |  | X |  |  |  |  |  |  |  |  |
| STK-04 Dir. Planif. y Control de Compras |  |  |  |  |  |  |  | X |  | X |  |  |  |  |  |  |
| STK-05 Director del proyecto |  | X |  | X | X |  |  |  | X |  |  |  |  |  |  |  |
| STK-06 Compradores |  |  |  |  |  |  |  |  |  |  | X |  |  | X |  |  |
| STK-07 Empleados solicitantes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| STK-08 Suministradores |  |  | X |  |  |  |  |  |  |  |  |  |  |  |  | X |
| STK-09 Integración de Arquitecturas | X |  |  |  |  |  |  |  |  |  |  |  | X |  |  |  |
| STK-10 Sistemas del Grupo de Fabricación |  |  |  |  |  | X |  |  | X |  |  | X | X |  |  |  |
| STK-11 Gestión del Cambio |  |  |  |  |  |  |  |  |  | X |  |  |  |  |  |  |
| STK-12 Innovación de Procesos |  |  |  |  |  |  |  | X |  |  |  |  |  |  |  |  |
| STK-13 Cuentas de Acreedores |  |  |  |  |  |  |  |  |  |  |  |  |  |  | X |  |
| STK-14 Logística |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| STK-15 Fabricación |  |  |  |  |  |  |  |  |  |  |  | X |  | X |  |  |
| STK-16 Ingeniería |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| STK-17 Proveedor del software |  | X |  |  |  |  | X |  |  |  |  |  |  |  |  |  |

**Lectura:** ningún requerimiento queda sin stakeholder y ningún stakeholder queda sin requerimiento. `STK-11` (Gestión del Cambio) no pide funciones: su fila en RF está vacía y su interés aparece en EAC-05 y RE-10.


### 4.2 Matriz 2: Requerimientos vs. Casos de Uso

| Requerimiento | CU-01 | CU-02 | CU-03 | CU-04 | CU-05 | CU-06 | CU-07 | CU-08 | CU-09 | CU-10 | CU-11 | CU-12 | CU-13 | CU-14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Proceso de negocio (criterio 1)** | **P01** | **P01** | **P01** | **P01** | **P02** | **P02** | **P02** | **P03** | **P03** | **P03** | **P03** | **P04** | **P04** | **P04** |
| RF-01 Solicitud de pedido | X |  |  |  |  |  |  |  |  |  |  |  |  |  |
| RF-02 Requisitos MRP/DRP |  |  | X |  |  |  |  |  |  |  |  |  |  |  |
| RF-03 Aprobación |  |  |  | X |  |  |  |  |  |  |  |  |  |  |
| RF-04 Pedido de compra |  | X | X |  |  |  |  |  |  |  |  |  |  |  |
| RF-05 Agrupar demanda |  | X | X |  |  |  |  |  |  |  |  |  |  |  |
| RF-06 Recepción |  |  |  |  | X |  |  |  |  |  |  |  |  |  |
| RF-07 Seguimiento de plazos |  |  |  |  |  | X |  |  |  |  |  |  |  |  |
| RF-08 Conciliar factura |  |  |  |  |  |  | X |  |  |  |  |  |  |  |
| RF-09 Envío a pago |  |  |  |  |  |  | X |  |  |  |  |  |  |  |
| RF-10 Registro de suministradores |  |  |  |  |  |  |  | X |  |  |  |  |  |  |
| RF-11 Publicar resultados y demanda |  |  |  |  |  |  |  |  | X |  |  |  |  |  |
| RF-12 Evaluar suministrador |  |  |  |  |  |  |  |  | X | X |  |  |  |  |
| RF-13 Documentos por Internet |  | X |  |  |  | X | X |  | X |  |  |  |  |  |
| RF-14 Consolidar datos |  |  |  |  |  |  |  |  |  |  | X |  |  |  |
| RF-15 Planificar proyecto |  |  |  |  |  |  |  |  |  |  |  | X |  |  |
| RF-16 Coste objetivo |  |  |  |  |  |  |  |  |  |  |  |  | X |  |
| RF-17 Preparación de lanzamiento |  |  |  |  |  |  |  |  |  |  |  |  |  | X |
| RF-18 Integración con existentes |  |  | X |  | X |  | X |  |  |  |  | X |  |  |

La primera fila ubica cada caso de uso en su proceso de negocio del criterio 1: P01 a P04 son CDU-01 a CDU-04.

**Lectura:** todo requerimiento lo realiza al menos un caso de uso (ninguna fila vacía) y todo caso de uso responde a algún requerimiento (ninguna columna vacía). RF-13 y RF-18 cruzan cuatro casos cada uno: el intercambio con el suministrador y la integración con lo existente son **transversales**, y eso es lo que justifica en el §5 un Servicio de Integración y un API Gateway propios. Los casos de apoyo CU-15 a CU-20 heredan la traza de su caso base.


### 4.3 Matriz 3: Stakeholders vs. Casos de Uso

| Stakeholder | CU-01 | CU-02 | CU-03 | CU-04 | CU-05 | CU-06 | CU-07 | CU-08 | CU-09 | CU-10 | CU-11 | CU-12 | CU-13 | CU-14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Proceso de negocio (criterio 1)** | **P01** | **P01** | **P01** | **P01** | **P02** | **P02** | **P02** | **P03** | **P03** | **P03** | **P03** | **P04** | **P04** | **P04** |
| STK-01 VP Gestión de Materiales |  | X | X |  |  |  |  |  | X | X | X | X |  |  |
| STK-02 VP Servicios de Información |  |  | X |  | X |  | X |  |  |  | X | X |  |  |
| STK-03 Grupo de Unidad de Compras |  | X | X |  |  |  |  |  | X | X | X |  |  |  |
| STK-04 Dir. Planif. y Control de Compras |  | X | X |  |  | X |  |  |  |  | X |  |  |  |
| STK-05 Director del proyecto |  | X | X |  | X | X | X |  | X |  |  | X |  |  |
| STK-06 Compradores |  | X | X | X | X | X | X | X | X | X |  |  |  |  |
| STK-07 Empleados solicitantes | X |  |  | X |  | X |  |  |  |  |  |  |  |  |
| STK-08 Suministradores |  | X | X |  |  | X | X | X | X |  |  |  | X |  |
| STK-09 Integración de Arquitecturas |  | X | X |  | X | X | X |  | X |  |  | X |  |  |
| STK-10 Sistemas del Grupo de Fabricación |  |  | X |  | X |  | X |  |  |  |  | X |  |  |
| STK-11 Gestión del Cambio |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| STK-12 Innovación de Procesos | X | X | X |  | X |  | X |  |  |  |  |  |  |  |
| STK-13 Cuentas de Acreedores |  |  |  |  |  |  | X |  |  |  |  |  |  |  |
| STK-14 Logística |  |  |  |  | X | X |  |  |  |  |  |  |  |  |
| STK-15 Fabricación |  |  | X |  | X | X |  |  |  |  |  |  |  |  |
| STK-16 Ingeniería |  |  |  |  |  |  |  |  |  |  |  | X | X | X |
| STK-17 Proveedor del software |  |  | X |  | X |  | X |  |  |  |  | X |  |  |

**Lectura:** derivada de las matrices 1 y 2. La fila de `STK-06` (compradores) es la más densa: son los usuarios principales. La de `STK-11` queda vacía por la razón ya dicha. Las columnas CU-02, CU-06 y CU-07 concentran más interesados: son los casos de la fase 1, y por eso la fase 1 va primero.


### 4.4 Matriz 4: Requerimientos vs. Requerimientos

Matriz cuadrada de **dependencia**, con la plantilla de la nota técnica de trazabilidad: las columnas originan la dependencia y las filas dependen. Se lee **«la fila depende de la columna»**. La diagonal no aplica.

| Depende ↓ / de → | 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RF-01 Solicitud de pedido | - |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| RF-02 Requisitos MRP/DRP |  | - |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | X |
| RF-03 Aprobación | X |  | - |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| RF-04 Pedido de compra |  | X | X | - | X |  |  |  |  | X |  |  |  |  |  |  |  |  |
| RF-05 Agrupar demanda |  |  |  |  | - |  |  |  |  | X |  |  |  |  |  |  |  |  |
| RF-06 Recepción |  |  |  | X |  | - |  |  |  |  |  |  |  |  |  |  |  |  |
| RF-07 Seguimiento de plazos |  |  |  | X |  |  | - |  |  |  |  |  | X |  |  |  |  |  |
| RF-08 Conciliar factura |  |  |  | X |  | X |  | - |  |  |  |  |  |  |  |  |  |  |
| RF-09 Envío a pago |  |  |  |  |  |  |  | X | - |  |  |  |  |  |  |  |  | X |
| RF-10 Registro de suministradores |  |  |  |  |  |  |  |  |  | - |  |  |  |  |  |  |  |  |
| RF-11 Publicar resultados y demanda |  |  |  |  |  |  |  |  |  | X | - | X | X |  |  |  |  |  |
| RF-12 Evaluar suministrador |  |  |  |  |  | X | X | X |  | X |  | - |  |  |  |  |  |  |
| RF-13 Documentos por Internet |  |  |  |  |  |  |  |  |  | X |  |  | - |  |  |  |  |  |
| RF-14 Consolidar datos |  |  |  | X |  |  |  | X |  |  |  | X |  | - |  |  |  |  |
| RF-15 Planificar proyecto |  |  |  |  |  |  |  |  |  | X |  |  |  |  | - |  |  | X |
| RF-16 Coste objetivo |  |  |  |  |  |  |  |  |  |  |  |  |  |  | X | - |  |  |
| RF-17 Preparación de lanzamiento |  |  |  |  |  |  |  |  |  |  |  | X |  |  | X |  | - |  |
| RF-18 Integración con existentes |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | - |

**Lectura:** las columnas más marcadas son **RF-10** (registro único de suministradores, seis dependientes), **RF-04** (pedido de compra, cuatro) y **RF-18** (integración, tres). Son la base de todo lo demás, y confirman el orden de las fases: primero las transacciones, y el registro de suministradores antes que su evaluación. RF-01, RF-10 y RF-18 no dependen de nadie: por ahí se empieza a construir.


## 5. Estilos arquitectónicos y diagrama de despliegue (criterio 5, 20 pts)


### 5.1 La decisión

**Estilo principal: arquitectura orientada a servicios (SOA), con un servicio por proceso de negocio** (CDU-01 a CDU-04), más un servicio de integración; **en capas** por dentro y **basada en eventos** entre servicios. Es la misma combinación del ejemplo de clase (perspectiva lógica capas/SOA y bloques basados en eventos). Un **estilo arquitectónico** establece las restricciones sobre la arquitectura de una familia de diseños; se elige en función de los drivers, no por preferencia.


### 5.2 Por qué SOA, en función de los criterios anteriores

| Escalón de la lámina «Funcionamiento de la Arquitectura (SOA)» | Cómo se cumple en SiL'K | Criterio que lo respalda |
|---|---|---|
| *«Define las necesidades del negocio»* | La Estrategia de Gestión de Suministros y el negocio delimitado | §1, caso de negocio |
| *«Desarrolla procesos de negocio como Servicios»* | Los cuatro procesos de la primera descomposición son los cuatro servicios: la granularidad ya viene decidida | §1.3 · matriz 2 |
| *«Permite que cada Servicio evolucione independientemente»* | Las tres fases de implantación se entregan servicio por servicio, sin detener lo ya entregado | RE-05 · RE-12 · EAC-07 |
| *«Plantea aplicaciones distribuidas, multi-nivel»* | Siete centros, cinco filiales y suministradores externos acceden a la misma plataforma | RE-11 · RE-03 · EAC-03 |

La razón de fondo es de **integración**: el problema que el caso describe son sistemas de compras distintos en cada centro (pág. 4) y la obligación de convivir con lo existente (`RE-01`, `RE-13`, `RE-14`). SOA expone cada proceso con un contrato estable, detrás del cual puede haber el paquete comprado (`RE-02`) o un sistema de planta.


### 5.3 Estilos complementarios, cada uno con su driver

| Estilo | Dónde se aplica | Driver |
|---|---|---|
| **En capas** | Dentro de cada servicio: presentación, lógica de negocio y datos | EAC-07 |
| **Cliente-servidor (N niveles)** | Navegador, portal y tableta como clientes; servicios y base de datos como niveles | EAC-03 · RE-11 |
| **Llamada y retorno** | Operaciones interactivas: emitir un pedido, aprobar, consultar | EAC-02 · EAC-05 |
| **Basado en eventos** | Entre servicios y hacia los centros: «pedido emitido», «material recibido», «factura conciliada» | EAC-01 · EAC-09 · RE-12 |
| **Tuberías y filtros** | Carga del almacén analítico: extraer, depurar duplicados, consolidar | RF-14 |


### 5.4 Estilos descartados

| Estilo | Por qué no |
|---|---|
| **Monolítico** (un ERP completo) | Lo prohíbe el caso: *«no estaba buscando una solución completa de planificación de recursos empresariales»* (`RE-04`). Además obligaría a implantar todo de una vez, contra `RE-05` |
| **Microservicios** | La granularidad por proceso ya basta; partir más fino multiplica la operación sin un driver que lo pida, y el núcleo es un paquete de mercado (`RE-02`) |
| **Par a par** | Hay un dueño claro de los datos (Compras): no hay pares equivalentes |


### 5.5 Patrones arquitectónicos usados

De la lista de clase, de menor alcance que el estilo y con una regla cada uno: **API Gateway** (una sola puerta de entrada para suministradores y clientes web), **Single Sign-On** y **Access Token** (identidad corporativa y de suministradores), **Load Balance** (reparto entre nodos), **Circuit Breaker** (un sistema de planta caído no arrastra a los servicios), **Store and forward** (el agente de planta y la tableta guardan y reenvían), **Webhook** (aviso al sistema del suministrador) y **Log aggregation** (bitácora única).


### 5.6 Lo que cambia al traer el caso al presente

| En el caso (1998-1999) | Hoy | Driver |
|---|---|---|
| «Red Internet de Suministros»; intercambio electrónico de documentos | Portal web del suministrador y API sobre HTTPS | RE-03 · EAC-04 |
| Un sistema de compras por centro, modificado localmente | Una plataforma única en la nube, configurada y no personalizada | RE-08 · EAC-07 |
| Servidores propios por planta | Contenedores e infraestructura definida como código | EAC-03 · EAC-08 |
| Usuario y contraseña por sistema | Inicio de sesión único con doble factor | EAC-04 |
| Lista de control de funcionalidades y demostraciones | Además, escenarios de atributos de calidad medibles | §3.2 · §6 |
| ISO/IEC 9126 | Familia ISO/IEC 25000 | §6.4 |


### 5.7 Diagrama de bloques: arquitectura basada en eventos

El **diagrama de bloques de alto nivel** es el primer paso antes del detalle: quién produce, quién enruta y quién consume. Toda flecha lleva el nombre del evento que transporta.

![[02-Diagramas/caso-hd/5-estilo-despliegue/bloques-hd.svg]]

*Figura 8. Diagrama de bloques de SiL'K: productores, enrutador y consumidores de eventos.*

**Cómo se integra el bus de eventos.** Es un componente central con una interfaz para publicar y suscribirse; los publicadores no conocen a los suscriptores.

| Evento | Publicador | Suscriptores | Para qué |
|---|---|---|---|
| Solicitud aprobada | Servicio Requisición y Pedido | El mismo servicio (bandeja del comprador) | Que el comprador la convierta en pedido |
| Pedido emitido | Servicio Requisición y Pedido | Suministradores · Recepción y Facturas · MRP/DRP de planta | Avisar al suministrador y esperar la entrega |
| Requisitos publicados | Agente de integración de la planta | Servicio Requisición y Pedido | Generar propuestas de pedido (CU-03) |
| Material recibido | App de recepción | Recepción y Facturas · Suministradores · MRP/DRP de planta | Conciliar y medir el plazo real |
| Factura conciliada | Servicio Recepción y Facturas | Sistema de Cuentas de Acreedores | Pagar |
| Retraso detectado | Servicio Recepción y Facturas | Suministradores · comprador | Reclamar y evaluar (CU-18, CU-10) |

**Beneficios para SiL'K**, los cuatro de clase: comunicación desacoplada (una planta caída no detiene a las demás, `RE-12`), flexibilidad (cada fase agrega suscriptores sin tocar lo entregado, `RE-05`), escalabilidad (`EAC-03`) y reutilización de los eventos (el almacén analítico los recibe todos, `RF-14`).


### 5.8 Perspectiva lógica: capas dentro de cada servicio

| Elemento | Responsabilidad |
|---|---|
| **Capa de presentación** | Recibe la interacción del usuario y le muestra resultados: aplicación web, portal del suministrador y app de recepción |
| **Capa de servicios web** | Expone los servicios para integrar sistemas externos: API Gateway y contratos de cada servicio |
| **Capa de negocio** | Coordina la ejecución de los casos de uso: los cuatro servicios, uno por proceso |
| **Capa de datos** | Almacena los objetos y oculta al resto que es una base relacional |
| **Capa de integración** | Conecta con los sistemas existentes: MRP/DRP de planta, Cuentas de Acreedores, ingeniería |


### 5.9 Diagrama de despliegue

El **diagrama de despliegue** (o de distribución) muestra los nodos físicos y qué componentes ejecuta cada uno. Notación de clase: nodo como cubo; `«device»` para el hardware y `«executionEnvironment»` para el software que aloja componentes; componentes **dentro** del nodo; conexión de línea llena con el protocolo; zonas FrontEnd y BackEnd. La figura 9 da la vista de conjunto y las figuras 10 a 12 amplían cada zona.

![[02-Diagramas/caso-hd/5-estilo-despliegue/despliegue-hd.svg]]

*Figura 9. Diagrama de despliegue de SiL'K, vista de conjunto.*

| Nodo | Componentes | Por qué está ahí |
|---|---|---|
| PC de oficina | Aplicación web SiL'K | Compradores, solicitantes y dirección: sin instalación (EAC-05) |
| Tableta del muelle | App de recepción con cola local | Recibir aunque no haya red (EAC-01) |
| Equipo y servidor del suministrador | Portal del suministrador · cliente de API | Dos formas de acceso: una persona o su sistema (RE-03) |
| Borde de red | API Gateway · proveedor de identidad · pasarela VPN | Única entrada, autenticada y limitada (EAC-04) |
| Clúster de contenedores | Cuatro servicios de negocio · portal · Servicio de Integración | Un servicio por proceso (§5.1); escala por nodos (EAC-03) |
| Clúster de mensajería | Bus de eventos · cola de reintentos | Desacopla servicios y centros (EAC-01, EAC-09) |
| Servidor de base de datos | BD transaccional · bitácora de auditoría | Un registro único (RF-10) y rastro de auditoría (RE-15) |
| Almacén analítico | Almacén de datos · tablero | El gasto consolidado no compite con la operación (EAC-02, RF-14) |
| Región secundaria | Réplica y clúster en espera | Recuperación ante desastre (EAC-01) |
| Servidor de planta (uno por centro) | MRP/DRP · agente de integración · sistema local en retiro | Los sistemas existentes no se mueven (RE-13, RE-14) |
| Servidores corporativos | Cuentas de Acreedores · directorio · sistemas de ingeniería | Sistemas existentes de la sede (RE-13) |

> **Supuestos de dimensionamiento**
>
> El caso no trae ningún dato de hardware. Para 800 usuarios concurrentes (`EAC-02`) con crecimiento a 3.000 (`EAC-03`) se supone: clúster de 3 nodos de 8 vCPU y 32 GB (24 vCPU y 96 GB en total, con capacidad para perder un nodo), base de datos primaria y en espera en zonas distintas, y mensajería de 3 nodos. Son valores de partida para la prueba de carga del paso 5 (§6.1), no un compromiso.

![[02-Diagramas/caso-hd/5-estilo-despliegue/despliegue-hd-detalle-1-usuarios.png]]

*Figura 10. Detalle del despliegue: usuarios y dispositivos.*

![[02-Diagramas/caso-hd/5-estilo-despliegue/despliegue-hd-detalle-2-nube.png]]

*Figura 11. Detalle del despliegue: nube privada virtual y región secundaria.*

![[02-Diagramas/caso-hd/5-estilo-despliegue/despliegue-hd-detalle-3-existentes.png]]

*Figura 12. Detalle del despliegue: sistemas existentes en los centros.*


## 6. Drivers de calidad y de restricción en los pasos, y modelo de calidad (criterio 6, 20 pts)


### 6.1 Los pasos para definir la arquitectura, con sus drivers

Los siete pasos de la lámina *Pasos para la definición de una Arquitectura de software*. En cada uno se indica qué drivers de calidad y de restricción lo condicionan.

| # | Paso | Qué se hizo para SiL'K | Drivers de calidad | Drivers de restricción |
|---|---|---|---|---|
| 1 | Creación del **caso de negocio** | Negocio delimitado, contexto, core y descomposición (§1) | - | RE-04 ámbito · RE-06 valor |
| 2 | **Entendimiento de los requisitos** | Stakeholders, RF, escenarios de calidad y restricciones; matrices (§2-§4) | EAC-01 a EAC-09, escritos como EaC | RE-01 a RE-16, por categoría |
| 3 | **Creación y selección** de la arquitectura | SOA con un servicio por proceso y estilos complementarios (§5) | EAC-06 y EAC-07 deciden SOA; EAC-01 y EAC-09 piden eventos | RE-01, RE-02, RE-13 (integrar) · RE-04 (no monolítico) |
| 4 | **Documentación y comunicación** | Este documento: vista de escenarios (CDU) y vista física (despliegue) | Cada EaC ubicado en un nodo (§6.2) | RE-10: comunicar a 800 personas, como los boletines del caso |
| 5 | **Análisis o evaluación** | Recorrer los EaC sobre el despliegue y medir con el modelo de calidad (§6.4) | Las nueve medidas son el criterio de aprobación | RE-01: revisión del grupo de Integración de Arquitecturas |
| 6 | **Implementación** basada en la arquitectura | Tres fases; cada fase entrega servicios completos | EAC-03: crecer de 800 a 3.000 entre fases | RE-05 fases · RE-12 no parar la línea · RE-14 coexistencia |
| 7 | **Aseguramiento** de que la implementación esté acorde | En cada fase se vuelven a medir los EaC y se revisa la conformidad | Las medidas del §3.2 como pruebas de aceptación | RE-15: rastro de auditoría |

> **El caso ya hacía una parte del paso 5**
>
> El equipo de SiL'K evaluó a los finalistas con *«diez escenarios posibles, basados en los requisitos tecnológicos y del proceso»* (pág. 12) y con una lista de control con umbral del 90 % (pág. 11). Lo que se agrega al traerlo al presente es que los escenarios sean de **atributos de calidad** y tengan **medida**.


### 6.2 Los escenarios de calidad incorporados a la solución

Cada escenario del §3.2 se convierte en una decisión de arquitectura y queda ubicado en el despliegue del §5.9. Es la respuesta al numeral 4 de la tarea.

| EaC | Decisión de arquitectura (táctica) | Patrón | Dónde queda en el despliegue |
|---|---|---|---|
| EAC-01 Disponibilidad | Redundancia en dos zonas, base en espera activa, región secundaria; la recepción trabaja sin conexión | Circuit Breaker · Store and forward | Borde · clúster · BD · región secundaria · tableta · agente de planta |
| EAC-02 Desempeño | Reparto de carga; las consultas analíticas salen de la base transaccional | Load Balance | Borde · almacén analítico |
| EAC-03 Escalabilidad | Servicios sin estado en contenedores; se agregan nodos | Load Balance | Clúster de contenedores |
| EAC-04 Seguridad | Entrada única, doble factor, autorización por suministrador, cifrado en tránsito y en reposo, bitácora | API Gateway · SSO · Access Token | Borde · BD (bitácora) |
| EAC-05 Usabilidad | Una sola aplicación web con catálogo guiado; la interfaz separada de la lógica | - | PC de oficina · portal web |
| EAC-06 Compatibilidad | Adaptadores por sistema, contratos de servicio estables, VPN a los centros | Store and forward · Webhook | Servicio de Integración · agente de planta |
| EAC-07 Modificabilidad | Un servicio por proceso, capas dentro de cada uno, reglas por configuración | Log aggregation | Clúster de contenedores |
| EAC-08 Portabilidad | Contenedores e infraestructura como código; base de datos relacional estándar | - | Clúster · BD |
| EAC-09 Fiabilidad | Mensajes idempotentes, reintentos, transacciones y conciliación a tres bandas | Store and forward | Clúster de mensajería · BD |


### 6.3 Las restricciones incorporadas a la solución

| Restricción | Decisión que impone |
|---|---|
| RE-01 · RE-13 · RE-14 (compatibilidad e integración) | Servicio de Integración y agente en cada planta; los sistemas existentes no se modifican |
| RE-02 (paquete de mercado) | El paquete queda detrás de los contratos de servicio: se configura, no se personaliza |
| RE-03 (acceso por Internet) | Portal y API públicos detrás del API Gateway |
| RE-04 (no es un ERP) | Solo los cuatro servicios del ámbito; lo demás se integra, no se reemplaza |
| RE-05 · RE-12 (fases, sin parar la línea) | Un servicio por fase, desplegado sin interrupción; los eventos aíslan a la planta |
| RE-06 · RE-07 (coste y soporte) | Infraestructura que crece por demanda; un proveedor con hoja de ruta |
| RE-08 (proceso común) | Un solo servicio por proceso para todos los centros, con reglas configurables por división |
| RE-10 (cambio y formación) | Una interfaz única y guiada; entornos de formación por fase |
| RE-11 (centros y filiales) | Acceso web desde cualquier centro; región secundaria |
| RE-15 · RE-16 (control interno y datos personales) | Bitácora de solo inserción, segregación de funciones y cifrado |


### 6.4 Determinación del modelo de calidad

Un **modelo de calidad** descompone la calidad del producto en características y subcaracterísticas que se pueden medir. El pensamiento ISO no es una norma suelta, es una **familia**:

| Norma | Qué aporta | Uso en SiL'K |
|---|---|---|
| **ISO/IEC 9126** (2001) | El modelo clásico: seis características (funcionalidad, fiabilidad, usabilidad, eficiencia, mantenibilidad, portabilidad) y métricas internas, externas y en uso | Es el modelo del programa del curso; sirve de referencia y de puente |
| **ISO/IEC 25000** (SQuaRE) | La familia que la sucede, en cinco divisiones: 2500n gestión, 2501n modelo, 2502n medición, 2503n requisitos, 2504n evaluación | Marco general |
| **ISO/IEC 25010** | El modelo de calidad del producto: ocho características | **Modelo adoptado** |
| **ISO/IEC 25023** | Medidas para cada característica | Origen de las métricas |
| **ISO/IEC 25040** | El proceso de evaluación | Cómo se aplica en los pasos 5 y 7 |

> **Por qué 25010 y no 9126**
>
> La consigna pide métodos actuales, y la 25010 sustituye a la 9126. Además, lo que más pesa en este caso (**seguridad** y **compatibilidad**) en la 9126 eran subcaracterísticas de *funcionalidad*; en la 25010 son características de primer nivel. El caso mismo eliminó a un proveedor por compatibilidad.

**El modelo determinado para SiL'K.** Cada característica se concreta en una subcaracterística, una métrica y un umbral, y se traza al driver del §3. Es el árbol que se mide en los pasos 5 y 7.

| Característica ISO/IEC 25010 | Subcaracterística | Equivalente en ISO/IEC 9126 | Driver | Métrica | Umbral |
|---|---|---|---|---|---|
| Adecuación funcional | Completitud funcional | Funcionalidad › adecuación | RF-01 a RF-18 | % de los criterios de la especificación funcional cubiertos sin personalizar | ≥ 95 % (el caso exigía 90 %) |
| Eficiencia de desempeño | Comportamiento temporal | Eficiencia › comportamiento temporal | EAC-02 | Tiempo de respuesta, percentil 95 | ≤ 2 s con 800 usuarios |
| Eficiencia de desempeño | Capacidad | Eficiencia › utilización de recursos | EAC-03 | Usuarios soportados sin cambio de código | 3.000 |
| Compatibilidad | Interoperabilidad · coexistencia | Funcionalidad › interoperabilidad | EAC-06 · RE-13 · RE-14 | % de interfaces estándar; esfuerzo de integrar un sistema | 100 % · ≤ 10 días-persona |
| Usabilidad | Capacidad de aprendizaje · operabilidad | Usabilidad › facilidad de aprendizaje | EAC-05 | Tiempo y pasos de la primera solicitud; % de éxito | ≤ 3 min · ≤ 5 pasos · 90 % |
| Fiabilidad | Disponibilidad · recuperabilidad | Fiabilidad › recuperabilidad | EAC-01 | % de disponibilidad mensual; tiempo de relevo | 99,9 % · ≤ 15 min |
| Fiabilidad | Tolerancia a fallos | Fiabilidad › tolerancia a fallos | EAC-09 | Registros duplicados ante reintentos | 0 |
| Seguridad | Confidencialidad · autenticidad · responsabilidad | Funcionalidad › seguridad | EAC-04 · RE-15 · RE-16 | Lecturas cruzadas; % de accesos con doble factor; % de operaciones en bitácora | 0 · 100 % · 100 % |
| Mantenibilidad | Modularidad · capacidad de ser modificado | Mantenibilidad › facilidad de cambio | EAC-07 | Tiempo de un cambio de regla; servicios tocados | ≤ 1 día hábil · 1 |
| Portabilidad | Adaptabilidad · capacidad de ser instalado | Portabilidad › adaptabilidad | EAC-08 | Tiempo de levantar la solución en otro entorno | ≤ 5 días hábiles |

**Cómo se usa.** En el paso 5 se evalúa la arquitectura contra los diez umbrales antes de construir; en el paso 7 se vuelve a medir al cerrar cada una de las tres fases. Una característica por debajo de su umbral bloquea el paso a la fase siguiente. Las ocho características de la norma están cubiertas; las tres con más peso para este caso son **compatibilidad, seguridad y fiabilidad**, las mismas que la prioridad del §3.2.


### 7. Supuestos y límites

- Las medidas de calidad, las dos restricciones regulatorias y el dimensionamiento son **supuestos de diseño**; el caso no trae esos datos.
- No se elige proveedor de software: el caso termina sin decidirlo y la rúbrica no lo pide. La arquitectura vale para cualquiera de los tres finalistas, porque el paquete queda detrás de los contratos de servicio.
- No se incluye un diagrama de componentes aparte: los componentes van dentro de sus nodos en el despliegue.
- Las medidas de las descripciones textuales (por ejemplo, dos días hábiles para responder un reclamo) son reglas de negocio propuestas.


### 8. Referencias

- Austin, R. D., Sole, D. y Cotteleer, M. J. (2003). *La selección de software empresarial de Harley Davidson Motor Company* (caso 606-S14). Harvard Business School.
- Bass, L., Clements, P. y Kazman, R. (2021). *Software Architecture in Practice* (4.ª ed.). Addison-Wesley.
- ISO/IEC 9126-1:2001. *Software engineering. Product quality. Part 1: Quality model*. International Organization for Standardization.
- ISO/IEC 25010:2011. *Systems and software engineering. Systems and software Quality Requirements and Evaluation (SQuaRE). System and software quality models*. International Organization for Standardization.
- Montoya-Suárez, Monsalve-Gómez y Sepúlveda-Castaño (2015). Un caso de estudio para la adopción de un modelo de trazabilidad de requisitos en el sector energético. *Lámpsakos*, (13), 88-100. Nota técnica del curso.
- Rojas de Morán, C. (2026). Presentaciones del curso Análisis y Diseño de Sistemas II: *Arquitectura de Software*, *CDU Negocio: modelado de drivers RF* y *Calidad del Software*. ECYS, Universidad de San Carlos de Guatemala.


## Preguntas de repaso

1. ¿Por qué el negocio es la gestión de suministros y no la selección del software?
2. ¿Por qué el comprador aparece en el contexto y no en el core?
3. ¿De qué dos matrices se deriva la de Stakeholders vs. Casos de Uso?
4. ¿Qué escalón de la lámina de SOA fija la granularidad de los servicios?
5. ¿Qué dos características son de primer nivel en ISO/IEC 25010 y no lo eran en la 9126?
