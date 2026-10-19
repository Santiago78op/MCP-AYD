---
tema: Entrega de tarea
fuente: "Generado por 06-Proyecto-MCP/generar-entrega-parq.py. No editar a mano: cambiar el generador y volver a correrlo"
fecha: 2026-10-19
tarea: Tarea 3 - Caso Parquímetros
alias: [entrega parquimetros, entrega tarea 3, SERVIparq, SIEP]
---

# Caso 4: Repensando los parquímetros · Entrega


## Resumen ejecutivo

**El caso.** SERVIparq, el programa de parquímetros de la Ciudad de México, enfrenta seis problemas: vecinos que no fueron consultados, cuidacarros que siguen cobrando, instrucciones de pago confusas, conductores que no saben cómo reclamar una multa, falta de personal y la sospecha de que el dinero se pierde. Una consultora de diseño, Smartmedia, mejoró la información del parquímetro con pruebas hechas con personas y fijó un nivel de desempeño del 72 %.

**Lo que encontramos.** Tres de los seis problemas no se arreglan con una pantalla mejor: son de gobierno del programa, de funciones del equipo que estaban apagadas y de un cobro informal que compite por el mismo espacio. En Guatemala pasa lo mismo: la capital cobra Q3 por media hora, pero en un solo operativo se retiraron 2,500 objetos con los que se apartaban lugares, y en Antigua la Corte de Constitucionalidad suspendió la base de datos de placas del cobro digital.

**Lo que proponemos.** SIEP, un sistema en el que el pago queda ligado a la placa y no a un boleto. Cada uno de los cinco procesos del negocio es un servicio (arquitectura orientada a servicios) y los servicios se avisan entre sí con eventos. Se reutiliza el parquímetro ya comprado, se encienden el pago con tarjeta y la alarma de vandalismo, la multa solo nace cuando un oficial confirma la evidencia, y todo lo cobrado se publica en un tablero.

| Qué se compromete | Número | Cómo se comprueba |
|---|---|---|
| Conductores que pagan sin ayuda la primera vez | ≥ 72 % | Prueba de desempeño con 12 personas, en la calle |
| Tiempo para saber si una placa pagó | ≤ 2 s | Prueba de carga con 500 verificadores |
| Pagos perdidos si se cae la señal | 0 | Corte de red simulado en el piloto |
| Multas con foto, hora, ubicación y confirmación del oficial | 100 % | Revisión de la bitácora |
| Diferencia entre lo publicado y lo depositado en el banco | Q0 | Conciliación diaria |

**Cómo se construye.** Con un ciclo en espiral, que revisa los riesgos en cada vuelta, y Scrum por dentro, en cuatro fases que empiezan por una colonia piloto. Desarrollamos además un prototipo de la pantalla del parquímetro que mide el 72 % mientras se prueba.


## Equipo de trabajo

| Integrante | Carné | Rol en el equipo | Responsabilidad en este caso |
|---|---|---|---|
| Santiago Julián Barrera Reyes | 201905884 | Scrum Master / coordinador | Análisis del caso, investigación del contexto guatemalteco, arquitectura en el ciclo de vida, integración del documento |
| Jemima Solmaira Chavajay Quiejú | 201801521 | Product Owner | Problemáticas y requisitos de desempeño, calidad del software, arquitectura de la información |
| Byron Josué Par Rancho | 201701078 | Equipo de desarrollo | Alternativas de solución, arquitectura de software (estilos, bloques, despliegue) y prototipo |


### Alcance del análisis

> **El negocio que se modela**
>
> **El negocio** es la **gestión del estacionamiento en la vía pública** en zonas tarifadas: concertar la zona con la comunidad, cobrar, verificar, rendir cuentas y mantener la red. No es la movilidad de la ciudad ni el gobierno completo, y no es el proyecto de diseño de Smartmedia: ese relato es la fuente de los problemas y los requisitos.
>
> **Consecuencia:** el personal de SERVIparq (verificadores, técnicos, operadores de monitoreo, analistas) son **trabajadores del negocio**. Son **actores** las entidades de afuera: el conductor, el comité vecinal, la Delegación, el área de tránsito, el banco y el proveedor de los parquímetros.
>
> Frente al **software**, en cambio, el verificador deja de ser trabajador y pasa a ser una entidad que usa el sistema. Por eso no está en el core (§3.2) y sí en el contexto (§3.1) y en los CDU expandidos (§3.3).
>
> **Los cuidacarros no son actores:** no interactúan con el negocio de forma legítima. Son un **factor externo** que genera restricciones y escenarios de calidad (§3.5, §5.5).

**SIEP** (Sistema Integrado de Estacionamiento en la vía Pública) es el nombre de la solución. El caso ocurre en la Ciudad de México en 2012; en cada decisión se indica cómo se aplicaría en una municipalidad guatemalteca. Los identificadores usados son: `STK-nn` involucrado, `P-nn` problemática, `CDU-nn` proceso de negocio, `CU-nn` caso de uso del sistema, `EAC-nn` escenario de calidad, `RE-nn` restricción y `S-n` alternativa de solución.


### Palabras que usamos

Los términos del caso y del curso que aparecen en el documento, en lenguaje sencillo.

| Palabra | Qué quiere decir aquí |
|---|---|
| **Franelero / cuidacarros** | Persona que, sin ser de la municipalidad, aparta lugares en la calle (con botes, sillas o llantas) y cobra por dejarlos usar. «Franelero» es la palabra mexicana del caso; en Guatemala decimos cuidacarros |
| **Pay and Display** | «Pague y muestre»: el parquímetro cobra con monedas, imprime un boleto y el conductor lo deja visible en el tablero del carro |
| **Pago por placa** | El pago queda registrado al número de placa: no hay boleto y el verificador consulta la placa en su teléfono |
| **Verificador** | Empleado de SERVIparq que revisa en la calle quién pagó. No puede multar: solo un oficial de tránsito puede |
| **Prueba de desempeño** | Se le pide a una persona que haga una tarea con el parquímetro (por ejemplo, pagar una hora) y se mide si la logra, cuánto tarda y dónde se confunde |
| **Bodystorming** | Técnica de diseño: se recrea la calle en una sala y los participantes actúan la situación para descubrir fallas |
| **Driver** | Factor que obliga a diseñar el sistema de cierta forma: una función, una cualidad medible o una restricción |
| **Escenario de calidad (EAC)** | Una cualidad del sistema escrita en seis partes y con un número para comprobarla, por ejemplo «responde en 2 s» |
| **SOA** | Arquitectura orientada a servicios: cada proceso del negocio es un programa independiente que los demás usan por medio de su interfaz |
| **Evento** | Aviso que un componente publica cuando algo pasa («pago registrado») para que otros reaccionen sin conocerse entre sí |
| **Guardar y reenviar** | Si se cae la red, el equipo guarda la operación y la manda cuando vuelve la conexión: no se pierde ningún pago |
| **Arquitectura de la información** | Cómo se ordenan y se nombran los contenidos para que la persona encuentre lo que busca. No es la arquitectura del software |
| **Calidad en uso** | La calidad que percibe el usuario real haciendo su tarea: si la logra (eficacia), con cuánto esfuerzo (productividad), sin riesgo (seguridad) y con gusto (satisfacción) |
| **EMETRA · PMT · PDH** | Empresa Municipal de Tránsito de la capital · Policía Municipal de Tránsito · Procuraduría de los Derechos Humanos |
| **MarbEx** | Marbete digital con el que la Municipalidad de Antigua Guatemala cobra el estacionamiento, por número de placa |


## 1. Análisis del caso


### 1.1 De qué trata

SERVIparq, el programa del gobierno de la Ciudad de México que instala y opera las redes de parquímetros, recibe en octubre de 2012 a una nueva directora, Margarita Patiño. El programa tiene una meta urbana clara: convertir el cajón de estacionamiento, un bien escaso y costoso (hasta 200 mil pesos por cajón en ciertas zonas), en un espacio público ordenado que reduzca la presencia del automóvil. Lo recaudado se reparte en 70 % para inversión, operación y mantenimiento y 30 % para reinversión en la comunidad.

El diagnóstico de Margarita, hecho con investigación secundaria y entrevistas a expertos, encuentra seis problemas. Para resolver los de uso contrata a Smartmedia, una empresa de diseño de interacción que aplica el método de pruebas de desempeño de David Sless: observación participativa, análisis funcional de las 13 partes de información del dispositivo, una sesión con SERVIparq para acordar los requisitos de desempeño (antes, durante y después del uso), un criterio cuantitativo del 72 % y dos rondas de pruebas, la segunda con prototipos en una calle simulada mediante *bodystorming* (recrear la calle en una sala y que los participantes actúen la situación). El caso cierra con la mejora medida y una junta para el plan del año siguiente.

**Nuestra lectura del caso:** Smartmedia resolvió bien la capa de información del dispositivo, pero tres de los seis problemas no son de interfaz. Son de **gobierno del programa** (consulta y rendición de cuentas), de **capacidades del sistema que se apagaron** (pago electrónico y alarma, restringidos a «Pay and Display» por falta de personal) y de **un actor informal que compite por el espacio** (los **franeleros**: así se les dice en México a las personas que apartan lugares en la calle y cobran por dejarlos usar; en Guatemala les decimos **cuidacarros**, y así los llamamos en el resto del documento). Una solución completa necesita las cuatro perspectivas que pide la consigna.


### 1.2 Involucrados (stakeholders)

| ID | Stakeholder | Interés en el sistema | Papel en el modelo | Influencia |
|---|---|---|---|---|
| STK-01 | SERVIparq: dirección (Margarita Patiño) | Que el programa funcione, se acepte y no requiera más personal | Dueño del negocio | Alta |
| STK-02 | Delegaciones (alcaldías; en Guatemala, la municipalidad) | Ordenar el estacionamiento y recibir el 30 % para su comunidad | Actor de negocio | Alta |
| STK-03 | Vecinos y comités de transparencia | Ser consultados antes y saber a dónde va el dinero | Actor de negocio | Alta |
| STK-04 | Conductor (usuario primario) | Pagar rápido, sin cambio exacto, sin multas injustas | Actor de negocio | Media |
| STK-05 | Verificador de SERVIparq (usuario secundario) | Saber qué vehículo pagó sin discutir con el conductor | Trabajador del negocio | Media |
| STK-06 | Oficiales de tránsito | Levantar multas con evidencia: por norma, solo ellos pueden | Actor de negocio (área de tránsito) | Alta |
| STK-07 | Proveedor del parquímetro (fabricante francés) | Que su equipo se use y se mantenga dentro del contrato | Actor de negocio | Media |
| STK-08 | Bancos e iniciativa privada | Procesar pagos electrónicos con comisión | Actor de negocio | Media |
| STK-09 | Smartmedia (consultora de diseño) | Demostrar que su método alcanza los niveles acordados | Stakeholder, no actor | Media |
| STK-10 | Cuidacarros (en el caso, «franeleros») | Seguir lucrando con el apartado de lugares | Factor externo con interés opuesto | Media en la calle |
| STK-11 | Peatones y personas con discapacidad | Que no se obstruyan accesos, pasos ni rampas | Stakeholder, no actor | Baja |


### 1.3 Las seis problemáticas, con su causa y su perspectiva

El caso agrupa las problemáticas según las preguntas de Margarita (1-2 comunidad, 3-5 uso y desempeño, 6 retroalimentación). Aquí se agregan la **causa raíz** y la **perspectiva** que la resuelve, porque de eso depende qué tipo de driver genera.

| ID | Problemática del diagnóstico | Causa raíz | Perspectiva que la resuelve | Driver que genera |
|---|---|---|---|---|
| P-01 | Inconformidad de vecinos no consultados antes de instalar | El proceso de implementación no tiene un paso de concertación | Ciclo de vida (fase previa) · negocio | CDU-01 · RE-09 |
| P-02 | Cuidacarros que siguen cobrando y alteran la tarifa | El pago legítimo es menos visible y menos cómodo que el informal | Información · arquitectura · gobierno | CU-12 · EAC-11 · RE-12 |
| P-03 | Quejas por las instrucciones de pago y por pagar solo con monedas | Panel con secuencia ilógica; pago electrónico deshabilitado | Información · arquitectura | CU-04 · CU-06 · EAC-01 |
| P-04 | Frustración en el primer uso; no se sabe cómo reclamar una infracción | Falta la etapa «después del uso» en la información | Información · calidad | CU-11 · EAC-02 |
| P-05 | Falta personal para supervisar, mantener y multar | Funciones automáticas apagadas; verificación manual por boleto | Arquitectura · calidad | CU-08 · CU-16 · EAC-04 · EAC-07 · RE-08 |
| P-06 | El sistema se percibe autoritario y corrupto | Nadie ve a dónde va el dinero | Arquitectura · información | CDU-04 · CU-13 · EAC-09 |


### 1.4 Lo que el caso dejó pendiente

- **El diagnóstico fue secundario.** Se basó en literatura y expertos; el usuario apareció recién en la etapa de Smartmedia.
- **Las pruebas no fueron en contexto real.** El permiso para encuestar en la vía pública no se tramitó, y la primera ronda se grabó solo en audio. Seis participantes por ronda sirven para encontrar fallas, no para medir un porcentaje.
- **Se rediseñó la información de una máquina que sigue siendo «Pay and Display».** El boleto en el tablero, origen de la multa injusta citada por un usuario, sigue existiendo.
- **Los problemas 1, 2 y 6 quedaron fuera del alcance de Smartmedia.** El cierre convoca a las Delegaciones a un plan de acción, pero el caso no dice cuál.


## 2. Investigación de los tópicos relacionados


### 2.1 Los tres sistemas que menciona el caso

| Sistema | Cómo funciona | Qué problemas atacaría | Lo que exige |
|---|---|---|---|
| **Pay and Display** (el instalado, de origen francés) | Se paga con monedas, sale un boleto y se coloca visible en el vehículo. El equipo puede pagar con tarjeta por red inalámbrica, cobrar otros servicios y avisar vandalismo, pero esas funciones se restringieron | Ninguno por sí solo; es el punto de partida | Verificadores que lean boletos uno por uno |
| **San Francisco**: sensores por cajón | Sensores avisan si el lugar está ocupado; la tarifa se ajusta a la demanda por hora o por evento | P-05 (supervisión automática) y la meta urbana de rotación | Sensores en cada cajón, datos confiables y una regla de tarifa pública |
| **Seattle**: información en web y app | Muestra en tiempo real cajones libres y tiempo de búsqueda por cuadra | P-03 y P-04 (planear antes del uso), parte de P-06 | Datos de ocupación y una app que la gente use |


### 2.2 El estacionamiento en la vía pública en Guatemala

**Cómo funciona hoy en la capital.** La Municipalidad de Guatemala regula el estacionamiento con el **Acuerdo COM-40-2022**, vigente desde el 12 de febrero de 2024. Fija tarifas por vehículo de **Q3 por cada 30 minutos o fracción**, **Q3.50 desde la segunda hora** y **Q4 desde la cuarta hora**; motocicletas Q2.50 por hora; carga y descarga Q20 por hora. El cobro rige de 7:00 a 20:00 y la banqueta se pinta por color: blanco para estacionar con o sin parquímetro inteligente, rojo para restricción, amarillo para carga y descarga, azul para taxis y fletes autorizados, y verde para horas valle (La Hora, 20/02/2024). EMETRA anunció en marzo de 2024 parquímetros inteligentes con **pago desde una aplicación móvil** y **estaciones de pago** para quien no la tenga, después de pintar las banquetas y retirar los obstáculos (Soy502, 07/03/2024).

**Los cobradores ajenos a la municipalidad.** En la capital, los llamados «cuidadores de carros» ocupan el espacio público con botes, llantas o sillas y cobran por dejar estacionar. En un solo operativo la Policía Municipal de Tránsito retiró **2,500 objetos**; la municipalidad recordó que una persona ajena no puede cobrar por estacionar en la vía pública, que esa conducta podría considerarse **extorsión**, y habilitó la **línea 1551** para denunciar (Emisoras Unidas, 27/02/2023). Los relatos incluyen agresiones a quien no paga (La Hora, 20/02/2024). El 27 de abril de 2026, alrededor del zoológico La Aurora (zona 13), el Ministerio Público identificó a **33 personas** que cobraban entre **Q35 y US$50** a turistas, algunas haciéndose pasar por empleados (Emisoras Unidas, 27/04/2026).

**El caso de Antigua Guatemala.** La municipalidad cobra el estacionamiento con un marbete digital, **MarbEx**, apoyado en una base de datos de placas. Sus ingresos por estacionamiento pasaron de **Q7.07 millones en 2024 a Q12.31 millones en 2025** (La Hora, 21/05/2026). La Corte de Constitucionalidad suspendió provisionalmente el 19 de mayo de 2026 los artículos que definían quién cobra y **la base de datos de placas** (expediente 3595-2026). La municipalidad publicó un reglamento nuevo el 9 de junio de 2026, y en julio la Corte suspendió también su artículo 11, que imponía una **multa de Q500** por no pagar el marbete (expediente 5643-2026; La Hora, 23/07/2026). La gobernación departamental y la municipalidad firmaron además una carta de entendimiento para recuperar el espacio ocupado por cuidadores (entre 30 y 100 según el día), con un protocolo que incluye a la Procuraduría de los Derechos Humanos (Prensa Libre, 12/10/2017).


#### 2.3 Lo que estos hechos le enseñan a la solución

| Hecho | Lección para la arquitectura | Dónde se aplica |
|---|---|---|
| Los cuidadores cobran porque el pago legítimo es invisible o incómodo | El sistema tiene que ganarle al cobro informal en visibilidad y facilidad, no solo prohibirlo | §5.4 · §5.5 · CU-12 |
| La Corte suspendió justamente la base de datos de placas de MarbEx | Una base de placas necesita fundamento legal explícito y protección de datos desde el diseño | RE-04 · EAC-06 |
| La Corte suspendió la multa de Q500 | La sanción tiene que salir de quien la norma faculta y con evidencia verificable | RE-03 · EAC-05 · CU-10 |
| La recaudación de Antigua casi se duplicó en un año | Lo que se cobra se puede medir y publicar: es la respuesta a P-06 | CDU-04 · EAC-09 |
| EMETRA planea app más estaciones de pago | La misma combinación que proponemos: canal digital sin dejar fuera a quien no tiene teléfono | S-2 · §5.1 |


## 3. Caso de negocio y drivers: los insumos de la arquitectura

Antes de proponer una solución se delimita el negocio (el **paso 0** del método de clase) y se identifican los **drivers arquitectónicos**: los factores críticos que guían el diseño, en sus tres tipos de clase: funcionales (casos de uso), de calidad (escenarios con medida) y de restricción (condiciones impuestas desde afuera).


### 3.1 Diagrama de contexto

**El Producto** es el software SIEP. Notación de clase: la **elipse** es El Producto, cada **rectángulo** una entidad o agente externo y cada **flecha** un flujo con nombre, en sustantivo. Son diez entidades y diecinueve flujos.

![[02-Diagramas/caso-parquimetros/1-caso-negocio/contexto-parq.svg]]

*Figura 1. Diagrama de contexto de SIEP: diez entidades y diecinueve flujos.*

| Entidad | Entrega a SIEP | Recibe de SIEP |
|---|---|---|
| Conductor (usuario primario) | Placa, pago y reclamos | Comprobante y aviso de tiempo |
| Comité vecinal de transparencia | Opinión y reportes | Informe de recursos 70/30 |
| Delegación (municipalidad) | Reglamento, zonas y tarifas | Recaudación e indicadores |
| Verificador de SERVIparq | Evidencia de infracción | Placas sin pago vigente |
| Oficial de tránsito | Multa confirmada | Infracción por confirmar |
| Banco y pasarela de pagos | Autorización del cobro | Solicitud de cobro |
| Proveedor de parquímetros | Reparación realizada | Orden de mantenimiento |
| Parquímetro (equipo en la calle) | Pagos y telemetría | Tarifas y configuración |
| Registro vehicular (padrón de placas) | Datos del vehículo | Ninguno: solo se consulta |
| Sistema de multas de tránsito | Estado de la multa | Multa registrada |


### 3.2 CDU de alto nivel (core) y primera descomposición

El core lleva **una sola elipse** con el nombre del negocio y todos sus actores alrededor; la descomposición, **un solo diagrama** con cinco procesos y **el mismo juego de actores**. Notación de negocio: actor y caso de uso con su barra diagonal. Las asociaciones van sin punta porque la comunicación se inicia en los dos sentidos.

| Proceso de negocio | Problemáticas que atiende | Actores | Resultado de valor |
|---|---|---|---|
| **CDU-01** Concertar e implementar la zona con la comunidad | P-01 · P-02 | Delegación · Comité vecinal | Una zona instalada con acuerdo vecinal, señalizada y con tarifa publicada |
| **CDU-02** Cobrar el estacionamiento por placa | P-03 · P-04 | Conductor · Banco | Un pago registrado a la placa, por el medio que el conductor tenga |
| **CDU-03** Verificar el pago y sancionar | P-04 · P-05 · P-02 | Oficial de tránsito · Conductor | Una infracción justa, con evidencia, y un reclamo que se puede seguir |
| **CDU-04** Rendir cuentas de los recursos a la comunidad | P-06 | Comité vecinal | La comunidad sabe cuánto se recaudó y en qué se invirtió el 30 % |
| **CDU-05** Mantener y monitorear la red de parquímetros | P-05 | Proveedor de parquímetros | Equipos funcionando y vandalismo atendido sin más personal |

![[02-Diagramas/caso-parquimetros/1-caso-negocio/cdu-core-parq.svg]]

*Figura 2. CDU core: el negocio y sus seis actores.*

![[02-Diagramas/caso-parquimetros/1-caso-negocio/cdu-descomposicion-parq.svg]]

*Figura 3. Primera descomposición: cinco procesos de negocio.*

**Trabajadores del negocio** (dentro de la frontera): verificador, técnico de campo, operador de la central de monitoreo, gestor comunitario y analista de transparencia. Siguiendo la regla de clase, **las áreas son actores y las personas son trabajadores**: el oficial de tránsito entra como el área que la norma faculta para multar.


### 3.3 Drivers funcionales (casos de uso del sistema)

Diecinueve casos de uso. Ninguno se llama crear, editar, eliminar o consultar: cada uno deja al actor con un resultado completo. Los de apoyo son los incluidos por particionamiento, que por convenio de clase no llevan actor.

| ID | Caso de uso | Proceso | Actor que lo inicia | Problemática |
|---|---|---|---|---|
| CU-01 | Registrar la consulta vecinal de una zona | CDU-01 | Gestor comunitario | P-01 |
| CU-02 | Configurar zona, cajones, horario y tarifa | CDU-01 | Delegación | P-01 |
| CU-03 | Publicar el mapa y las reglas de la zona | CDU-01 | Conductor (consulta) · Comité vecinal | P-03 · P-04 |
| CU-04 | Pagar el estacionamiento por placa | CDU-02 | Conductor | P-03 |
| CU-05 | Calcular tarifa y tiempo máximo de la zona | CDU-02 | De apoyo («include») | P-03 |
| CU-06 | Autorizar el pago con tarjeta o billetera | CDU-02 | Banco y pasarela | P-03 |
| CU-07 | Avisar el vencimiento y extender el tiempo | CDU-02 | Conductor | P-04 |
| CU-19 | Registrar la sesión de estacionamiento | CDU-02 | De apoyo («include») | P-05 |
| CU-08 | Verificar el pago por placa en la cuadra | CDU-03 | Verificador | P-05 |
| CU-09 | Registrar presunta infracción con evidencia | CDU-03 | Verificador | P-05 |
| CU-10 | Confirmar y emitir la multa | CDU-03 | Oficial de tránsito · Sistema de multas | P-05 |
| CU-11 | Presentar reclamo de infracción | CDU-03 | Conductor | P-04 |
| CU-12 | Reportar un cobro informal (cuidacarros) | CDU-03 | Conductor | P-02 |
| CU-13 | Publicar el tablero de recaudación 70/30 | CDU-04 | Analista de transparencia | P-06 |
| CU-14 | Seguir los proyectos de reinversión | CDU-04 | Comité vecinal | P-06 |
| CU-15 | Recibir y responder la retroalimentación vecinal | CDU-04 | Comité vecinal | P-06 · P-01 |
| CU-16 | Monitorear estado y vandalismo de los parquímetros | CDU-05 | Operador de monitoreo · Parquímetro | P-05 |
| CU-17 | Atender una orden de mantenimiento | CDU-05 | Técnico del proveedor | P-05 |
| CU-18 | Medir el desempeño de la información | CDU-05 | Analista de experiencia de uso | P-03 · P-04 |

**CDU expandidos y descripciones textuales.** Se expanden los dos procesos que concentran los problemas de uso y de personal: CDU-02 y CDU-03. Plantilla de clase: curso normal en dos columnas con una sola numeración y cursos alternos anclados a la línea donde ocurren.


#### CDU-02 Cobrar el estacionamiento por placa

![[02-Diagramas/caso-parquimetros/2-drivers-rf/cdu-expandido-parq-02-cobro.svg]]

*Figura 4. CDU-02 expandido.*


##### CU-04 Pagar el estacionamiento por placa

| Campo | Contenido |
|---|---|
| **Actores** | Conductor (inicia) |
| **Propósito** | Pagar el tiempo de estacionamiento sin boleto, con el medio de pago que tenga a mano. |
| **Resumen** | Se inicia cuando el Conductor llega al parquímetro o abre la app. El sistema calcula la tarifa de la zona, cobra y liga el pago a la placa. Finaliza cuando el Conductor recibe el comprobante. |
| **Prioridad** | Alta |

| Acción del actor | Respuesta del sistema |
|---|---|
| **1.** El Conductor escribe la placa de su vehículo. |  |
|  | **2.** El sistema muestra la tarifa de la zona, el tiempo máximo y el horario de cobro (incluye CU-05). |
| **3.** El Conductor elige el tiempo en bloques de 30 minutos. |  |
|  | **4.** El sistema muestra el total y la hora de vencimiento. |
| **5.** El Conductor paga con monedas. |  |
|  | **6.** El sistema registra la sesión de estacionamiento a la placa (incluye CU-19) y entrega el comprobante con folio, vencimiento y línea de reclamo. |

- **En la línea 1:** la placa tiene un formato inválido. El sistema lo señala con un ejemplo y se vuelve a la línea 1.
- **En la línea 3:** el tiempo excede el máximo de la zona. El sistema lo limita y lo informa; se continúa en la línea 4.
- **En la línea 5:** el Conductor paga con tarjeta o con el QR de la app. Se extiende con CU-06 y, autorizado el pago, se continúa en la línea 6.
- **En la línea 6:** el parquímetro no tiene conexión. Guarda el pago firmado y lo reenvía al reconectarse (EAC-03); el comprobante se entrega igual.


##### CU-05 Calcular tarifa y tiempo máximo de la zona

| Campo | Contenido |
|---|---|
| **Actores** | Ninguno: es de apoyo, incluido por CU-04 |
| **Propósito** | Aplicar la regla de tarifa vigente de la zona sin que el conductor tenga que calcularla. |
| **Resumen** | Se inicia cuando CU-04 necesita el precio. El sistema aplica el tarifario de la zona. Finaliza cuando devuelve el total y el tiempo máximo. |
| **Prioridad** | Alta |

| Acción del actor | Respuesta del sistema |
|---|---|
|  | **1.** El sistema identifica la zona y el horario a partir del parquímetro o de la ubicación de la app. |
|  | **2.** El sistema aplica el tarifario vigente por bloques de 30 minutos y el tiempo máximo de la zona. |
|  | **3.** El sistema devuelve total, hora de vencimiento y tiempo máximo a CU-04. |

- **En la línea 1:** la hora está fuera del horario de cobro. El sistema informa que no se cobra y termina el caso.


##### CU-06 Autorizar el pago con tarjeta o billetera

| Campo | Contenido |
|---|---|
| **Actores** | Banco y pasarela de pagos |
| **Propósito** | Cobrar con tarjeta o billetera digital, la alternativa a las monedas que pidieron los usuarios. |
| **Resumen** | Extiende a CU-04 en su línea 5 cuando el pago es electrónico. Finaliza cuando el Banco autoriza o rechaza. |
| **Prioridad** | Alta |

| Acción del actor | Respuesta del sistema |
|---|---|
|  | **1.** El sistema envía al Banco la solicitud de cobro con el monto y un identificador único de la operación. |
| **2.** El Banco y pasarela de pagos autoriza el cobro. |  |
|  | **3.** El sistema confirma el pago y regresa a CU-04 en la línea 6. |

- **En la línea 2:** el Banco rechaza. El sistema lo informa y ofrece otro medio; se vuelve a la línea 5 de CU-04.
- **En la línea 2:** no hay respuesta en 10 s. El sistema reintenta con el mismo identificador, sin cobrar dos veces.


##### CU-07 Avisar el vencimiento y extender el tiempo

| Campo | Contenido |
|---|---|
| **Actores** | Conductor (recibe el aviso e inicia la extensión) |
| **Propósito** | No volver al parquímetro para saber cuánto tiempo le queda ni para extenderlo. |
| **Resumen** | Se inicia 10 minutos antes del vencimiento. El sistema avisa al Conductor, que puede extender desde la app. Finaliza con la sesión extendida o vencida. |
| **Prioridad** | Media |

| Acción del actor | Respuesta del sistema |
|---|---|
|  | **1.** El sistema detecta que la sesión vence en 10 minutos y avisa al Conductor en la app. |
| **2.** El Conductor elige extender el tiempo. |  |
|  | **3.** El sistema cobra la extensión (CU-06) y actualiza la sesión (incluye CU-19). |

- **En la línea 2:** extender superaría el máximo de la zona. El sistema lo informa y sugiere otra zona cercana.
- **En la línea 2:** el Conductor no responde. La sesión vence y el verificador la verá sin pago vigente.


##### CU-19 Registrar la sesión de estacionamiento

| Campo | Contenido |
|---|---|
| **Actores** | Ninguno: es de apoyo, incluido por CU-04 y CU-07 |
| **Propósito** | Dejar un registro único por placa que el verificador pueda consultar en vez de leer boletos. |
| **Resumen** | Se inicia cuando se confirma un pago o una extensión. Finaliza cuando la sesión queda publicada como evento. |
| **Prioridad** | Alta |

| Acción del actor | Respuesta del sistema |
|---|---|
|  | **1.** El sistema crea o actualiza la sesión con placa, zona, cajón, inicio, vencimiento y medio de pago. |
|  | **2.** El sistema publica el evento «pago registrado» en el bus de eventos. |

- **En la línea 1:** ya existe una sesión vigente para la placa en la zona. El sistema suma el tiempo, sin duplicar.


#### CDU-03 Verificar el pago y sancionar

![[02-Diagramas/caso-parquimetros/2-drivers-rf/cdu-expandido-parq-03-verificacion.svg]]

*Figura 5. CDU-03 expandido.*


##### CU-08 Verificar el pago por placa en la cuadra

| Campo | Contenido |
|---|---|
| **Actores** | Verificador (inicia) |
| **Propósito** | Saber qué vehículos de la cuadra no tienen pago vigente, sin depender de un boleto visible. |
| **Resumen** | Se inicia cuando el Verificador recorre una cuadra. El sistema le muestra las placas con y sin pago. Finaliza cuando termina la cuadra. |
| **Prioridad** | Alta |

| Acción del actor | Respuesta del sistema |
|---|---|
| **1.** El Verificador abre la cuadra en la app de verificación. |  |
|  | **2.** El sistema muestra la lista de placas con sesión vigente en esa cuadra, actualizada. |
| **3.** El Verificador captura o escribe la placa de cada vehículo estacionado. |  |
|  | **4.** El sistema indica si la placa tiene pago vigente. |

- **En la línea 2:** no hay conexión. La app usa la lista local, que no tiene más de 5 minutos de antigüedad (EAC-04).
- **En la línea 4:** la placa no tiene pago vigente. Se extiende con CU-09.


##### CU-09 Registrar presunta infracción con evidencia

| Campo | Contenido |
|---|---|
| **Actores** | Verificador |
| **Propósito** | Dejar una presunta infracción con evidencia suficiente para que el oficial la confirme. |
| **Resumen** | Extiende a CU-08 en su línea 4 cuando la placa no tiene pago vigente. Finaliza cuando la presunta infracción queda enviada. |
| **Prioridad** | Alta |

| Acción del actor | Respuesta del sistema |
|---|---|
| **1.** El Verificador toma la fotografía del vehículo y de la placa. |  |
|  | **2.** El sistema agrega hora, ubicación y firma digital del dispositivo, y espera 10 minutos de tolerancia. |
|  | **3.** Pasada la tolerancia sin pago, el sistema publica la presunta infracción para el oficial de tránsito. |

- **En la línea 2:** el conductor paga durante la tolerancia. El sistema cancela la presunta infracción y lo registra.


##### CU-10 Confirmar y emitir la multa

| Campo | Contenido |
|---|---|
| **Actores** | Oficial de tránsito (inicia) · Sistema de multas de tránsito |
| **Propósito** | Cumplir la norma: solo el oficial levanta la multa, y lo hace con evidencia. |
| **Resumen** | Se inicia cuando el Oficial de tránsito revisa sus presuntas infracciones. Finaliza con la multa registrada o la presunta infracción descartada. |
| **Prioridad** | Alta |

| Acción del actor | Respuesta del sistema |
|---|---|
| **1.** El Oficial de tránsito revisa la evidencia de la presunta infracción. |  |
|  | **2.** El sistema muestra fotografías, hora, ubicación y el historial de pagos de esa placa en la zona. |
| **3.** El Oficial de tránsito confirma la multa. |  |
|  | **4.** El sistema la envía al Sistema de multas de tránsito, que devuelve su número; el sistema avisa al conductor. |

- **En la línea 3:** la evidencia es insuficiente. El Oficial la descarta con un motivo y el caso termina.


##### CU-11 Presentar reclamo de infracción

| Campo | Contenido |
|---|---|
| **Actores** | Conductor (inicia) |
| **Propósito** | Aclarar una infracción sabiendo a quién acudir y en cuánto tiempo responde. |
| **Resumen** | Se inicia cuando el Conductor recibe una multa que considera injusta. Finaliza cuando recibe la resolución. |
| **Prioridad** | Alta |

| Acción del actor | Respuesta del sistema |
|---|---|
| **1.** El Conductor ingresa el número de multa o su placa en la app, la web o la línea de atención. |  |
|  | **2.** El sistema muestra la evidencia y los pagos de esa placa en la fecha. |
| **3.** El Conductor describe el motivo y adjunta su prueba. |  |
|  | **4.** El sistema registra el reclamo con un folio, informa el plazo de respuesta (5 días hábiles) y lo asigna. |

- **En la línea 2:** el sistema encuentra un pago vigente para esa placa a la hora de la multa. Propone la anulación automática al oficial.


##### CU-12 Reportar un cobro informal (cuidacarros)

| Campo | Contenido |
|---|---|
| **Actores** | Conductor (inicia) |
| **Propósito** | Denunciar un cobro informal sin exponerse, para que la autoridad sepa dónde actuar. |
| **Resumen** | Se inicia cuando alguien le pide dinero al Conductor por estacionar. Finaliza cuando el reporte llega a la autoridad. |
| **Prioridad** | Media |

| Acción del actor | Respuesta del sistema |
|---|---|
| **1.** El Conductor elige «Reportar cobro informal» en el comprobante o en la app. |  |
|  | **2.** El sistema toma la ubicación de la cuadra y la hora, sin pedir datos personales. |
| **3.** El Conductor agrega, si quiere, el monto pedido y una descripción. |  |
|  | **4.** El sistema envía el reporte a la Policía Municipal de Tránsito y lo suma al mapa de cobros informales. |

- **En la línea 1:** hay amenaza o agresión. El sistema muestra la línea de emergencia antes de continuar.


### 3.4 Drivers de calidad: escenarios de atributos de calidad (EAC)

Cada escenario indica su categoría de calidad (la lista de drivers de calidad vista en clase) y la subcaracterística de ISO/IEC 9126 que afecta. La prioridad es el par (importancia para el negocio, dificultad técnica), en A alta, M media o B baja. El 72 % es el criterio que acordaron SERVIparq y Smartmedia; las demás medidas son metas que propone el grupo.

| ID | Categoría | Escenario de seis partes | Atributo afectado | Prioridad |
|---|---|---|---|---|
| EAC-01 | Usabilidad | **Fuente de estímulo:** Conductor que usa el parquímetro por primera vez y lleva prisa. **Estímulo:** necesita pagar una hora para su placa. **Artefacto:** interfaz del parquímetro. **Entorno:** en la calle, de día, con lluvia o con poca luz. **Respuesta:** completa el pago sin ayuda y sin colocar boleto. **Medida de la respuesta:** ≥ 72 % de los participantes de la prueba de desempeño completan la tarea (80 % encuentra × 90 % usa bien), en ≤ 90 s. | Calidad en uso › eficacia · usabilidad › operabilidad | (A, A) |
| EAC-02 | Usabilidad | **Fuente de estímulo:** Conductor frente al parquímetro o en la app. **Estímulo:** busca la tarifa, el tiempo máximo y cómo reclamar. **Artefacto:** pantalla y comprobante. **Entorno:** operación normal. **Respuesta:** encuentra los tres datos en la pantalla o el comprobante. **Medida de la respuesta:** ≥ 80 % de los participantes encuentra cada dato en ≤ 10 s. | Usabilidad › comprensibilidad | (A, M) |
| EAC-03 | Disponibilidad | **Fuente de estímulo:** Red celular de la zona. **Estímulo:** se cae la conexión del parquímetro. **Artefacto:** terminal de pago por placa. **Entorno:** horario de cobro. **Respuesta:** sigue cobrando, guarda los pagos firmados y los reenvía al reconectar. **Medida de la respuesta:** 0 pagos perdidos · sincronización ≤ 5 min después de la reconexión · cobro disponible ≥ 99,5 % mensual por equipo. | Fiabilidad › tolerancia a fallos · recuperabilidad | (A, M) |
| EAC-04 | Rendimiento | **Fuente de estímulo:** Verificador en la cuadra. **Estímulo:** consulta una placa. **Artefacto:** servicio de verificación y app del verificador. **Entorno:** hora pico, 500 verificadores conectados. **Respuesta:** indica si la placa tiene pago vigente. **Medida de la respuesta:** ≤ 2 s en 95 de cada 100 consultas en línea · sin conexión, lista local con antigüedad ≤ 5 min. | Eficiencia › comportamiento temporal | (A, M) |
| EAC-05 | Seguridad | **Fuente de estímulo:** Verificador. **Estímulo:** registra una presunta infracción. **Artefacto:** servicio de verificación y sanción. **Entorno:** operación normal. **Respuesta:** la infracción solo se vuelve multa si un oficial de tránsito la confirma con evidencia. **Medida de la respuesta:** 100 % de las multas con fotografía, hora, ubicación y firma del dispositivo · 0 multas sin confirmación del oficial. | Funcionalidad › seguridad · conformidad | (A, A) |
| EAC-06 | Seguridad | **Fuente de estímulo:** Usuario interno o atacante. **Estímulo:** intenta consultar los movimientos de una placa. **Artefacto:** base de sesiones y bitácora. **Entorno:** operación normal. **Respuesta:** permite el acceso solo con rol autorizado y lo registra; la analítica usa placas seudonimizadas (reemplazadas por un código que no identifica al dueño). **Medida de la respuesta:** 0 consultas sin bitácora · 100 % de accesos internos con doble factor · datos de placa borrados a los 90 días si no hay multa ni reclamo. | Funcionalidad › seguridad | (A, A) |
| EAC-07 | Fiabilidad | **Fuente de estímulo:** Persona que fuerza o golpea un parquímetro. **Estímulo:** abre la caja o daña el equipo. **Artefacto:** sensor de vandalismo y servicio de red y mantenimiento. **Entorno:** cualquier hora. **Respuesta:** avisa a la central y genera la orden para el proveedor y el aviso a la policía municipal. **Medida de la respuesta:** alarma en la central en ≤ 60 s en el 95 % de los casos · orden de mantenimiento en ≤ 5 min. | Fiabilidad › madurez · recuperabilidad | (M, M) |
| EAC-08 | Mantenibilidad | **Fuente de estímulo:** Delegación. **Estímulo:** cambia la tarifa, el horario o activa tarifa por demanda en una zona. **Artefacto:** servicio de zonas y tarifario. **Entorno:** operación normal. **Respuesta:** el cambio se configura y llega a todos los parquímetros de la zona. **Medida de la respuesta:** ≤ 1 día hábil · 0 líneas de código modificadas. | Mantenibilidad › facilidad de cambio | (A, B) |
| EAC-09 | Fiabilidad | **Fuente de estímulo:** Fin del día de cobro. **Estímulo:** cierra la recaudación. **Artefacto:** servicio de transparencia y conciliación bancaria. **Entorno:** operación normal. **Respuesta:** publica lo recaudado por zona y el reparto 70/30, conciliado con el banco. **Medida de la respuesta:** publicado en ≤ 24 h · diferencia con el banco = Q0. | Funcionalidad › exactitud | (A, M) |
| EAC-10 | Escalabilidad | **Fuente de estímulo:** Delegación. **Estímulo:** incorpora una colonia nueva de 300 parquímetros. **Artefacto:** plataforma completa. **Entorno:** crecimiento planificado. **Respuesta:** la incorpora con configuración, sin rediseñar. **Medida de la respuesta:** EAC-04 se mantiene con el doble de equipos · alta de la colonia en ≤ 5 días hábiles. | Eficiencia › utilización de recursos | (M, M) |
| EAC-11 | Seguridad | **Fuente de estímulo:** Conductor al que le piden dinero por estacionar. **Estímulo:** reporta el cobro informal. **Artefacto:** servicio de verificación y sanción. **Entorno:** operación normal. **Respuesta:** el reporte llega a la policía municipal y aparece en el mapa de cobros informales. **Medida de la respuesta:** reporte entregado en ≤ 5 min · 0 datos personales del denunciante almacenados. | Funcionalidad › seguridad (protección del usuario) | (A, M) |


### 3.5 Drivers de restricción

Ordenados por las seis categorías de clase. Las restricciones no se priorizan: todas son obligatorias.

| ID | Categoría | Restricción | Fuente |
|---|---|---|---|
| RE-01 | Tecnológica | Reutilizar los parquímetros de origen francés ya adquiridos; sus funciones de pago inalámbrico y alarma existen pero están deshabilitadas | Caso, «Aspectos tecnológicos» |
| RE-02 | Tecnológica | El equipo trabaja a la intemperie: pantalla legible con sol, lluvia, neblina y de noche | Caso, comentario de Marco |
| RE-03 | Regulatoria | Solo los oficiales de tránsito pueden levantar la multa (en Guatemala, la Policía Municipal de Tránsito) | Caso, P-05 · COM-40-2022 |
| RE-04 | Regulatoria | La base de datos de placas y la sanción necesitan fundamento expreso en el reglamento, y protección de datos personales | Supuesto, a partir de la CC, exp. 3595-2026 y 5643-2026 |
| RE-05 | Regulatoria | Información pública de oficio sobre los recursos (en Guatemala, Ley de Acceso a la Información Pública, Decreto 57-2008) | Caso, P-06 · supuesto de traslado |
| RE-06 | De negocio | Reparto fijo de lo recaudado: 70 % inversión, operación y mantenimiento; 30 % reinversión en la comunidad | Caso, Introducción |
| RE-07 | De negocio | Mejorar sin aumentar el capital humano | Caso, decisión de Margarita |
| RE-08 | Organizacional | Cada Delegación implementa distinto: la solución se configura por zona, no se impone igual a todas | Caso, Introducción |
| RE-09 | Organizacional | La implementación pasa por comités vecinales de transparencia antes de instalar | Caso, visión de Margarita |
| RE-10 | Organizacional | Probar en la vía pública exige un permiso especial de la ciudad | Caso, pruebas de evaluación |
| RE-11 | Ambiental o física | Riesgo de vandalismo de los equipos y del dinero en la caja | Caso, capacidad de aviso |
| RE-12 | Ambiental o física | Cuidacarros que ocupan los cajones con objetos y cobran: el sistema convive con ellos en la calle | Caso, P-02 · §2.2 |
| RE-13 | De integración | Bancos e iniciativa privada como socios para el pago electrónico | Caso, «Aspectos tecnológicos» |
| RE-14 | De integración | Sistema de multas de tránsito y padrón vehicular, que pertenecen a otra autoridad | Supuesto de diseño |


### 3.6 Priorización: los cinco drivers que más pesan

| # | Driver | Por qué pesa | Decisión de arquitectura que fuerza |
|---|---|---|---|
| 1 | EAC-05 Infracción solo con evidencia y oficial | Sin esto la multa es ilegal (RE-03) y el sistema pierde legitimidad | Servicio de sanción separado; evidencia firmada en el dispositivo |
| 2 | EAC-06 Protección de la base de placas | Es lo que la Corte suspendió en Antigua | Placas reemplazadas por un código en la analítica, bitácora de solo inserción, retención limitada |
| 3 | EAC-01 Eficacia del 72 % | Es el criterio que el propio caso acordó | Pago por placa en tres pasos y prueba de desempeño en cada iteración |
| 4 | EAC-03 Cobro sin conexión | Un parquímetro que no cobra es un cajón regalado al cuidacarros | Cliente-servidor con guardar y reenviar en el equipo |
| 5 | EAC-04 Verificación en 2 s | Es lo que permite cubrir la falta de personal (P-05, RE-07) | Lista local en la app y consulta por evento, no por lectura de boletos |


## 4. Posibles soluciones

Se plantean cuatro alternativas. Las tres primeras son excluyentes en su núcleo técnico; la cuarta es de gobierno y se combina con cualquiera. Cada una se mira desde las cuatro perspectivas de la consigna.

| Alternativa | Arquitectura del software | Calidad del software | Arquitectura en el ciclo de vida | Arquitectura de la información |
|---|---|---|---|---|
| **S-1** Rediseñar la información sobre el mismo «Pay and Display» (lo que entregó Smartmedia) | Ningún cambio: equipo aislado, boleto en el tablero, verificación visual | Mejora la eficacia de uso hasta el 72 %, pero no toca disponibilidad ni seguridad de la multa | Un ciclo corto de diseño y pruebas; sin construcción de software | Panel reorganizado por pasos; sigue sin la etapa «después del uso» |
| **S-2** Pago por placa, con varios medios de pago y conectado: se habilitan las funciones apagadas del equipo y se suma una plataforma de servicios | SOA por proceso con eventos; el parquímetro y la app del verificador trabajan sin conexión | Once escenarios medibles; el 72 % se vuelve criterio de aceptación de cada entrega | Iterativo e incremental: piloto en una colonia, luego por zonas | Tres momentos de uso cubiertos: señal y app antes, tres pasos durante, comprobante y aviso después |
| **S-3** Red sensorizada con tarifa por demanda (modelo San Francisco) | Sensores por cajón, gateway IoT y motor de tarifas en tiempo real | Exige alta disponibilidad de sensores y datos confiables; riesgo de vandalismo | Proyecto largo y caro, con riesgo alto al inicio | Ocupación en tiempo real; la tarifa cambiante es difícil de comunicar |
| **S-4** Gobierno comunitario y respuesta al cobro informal: consulta previa, comité, tablero público y protocolo con la policía municipal y la PDH | Requiere servicios de transparencia y reportes; no exige una plataforma particular | Se mide con la satisfacción y la confianza (calidad en uso) | Agrega una fase previa de concertación a cada zona | Publica cuentas claras y avisa que el único cobro es el del parquímetro |


### 4.1 Evaluación contra las problemáticas y los drivers

**Sí** resuelve · **Parcial** resuelve en parte · **No** no resuelve. Una alternativa que no toca un driver de los cinco priorizados (§3.6) queda descartada como solución única.

| Criterio | S-1 | S-2 | S-3 | S-4 |
|---|---|---|---|---|
| P-01 Vecinos no consultados | No | No | No | Sí |
| P-02 Cuidacarros | Parcial | Parcial | Parcial | Sí |
| P-03 Instrucciones y medios de pago | Parcial | Sí | Sí | No |
| P-04 Primer uso y reclamos | Parcial | Sí | Parcial | Parcial |
| P-05 Falta de personal | No | Sí | Sí | No |
| P-06 Percepción de corrupción | No | Parcial | Parcial | Sí |
| EAC-05 Multa con evidencia (prioridad 1) | No | Sí | Sí | No |
| EAC-06 Protección de placas (prioridad 2) | no aplica | Sí | Sí | no aplica |
| EAC-01 Eficacia del 72 % (prioridad 3) | Sí | Sí | Parcial | No |
| RE-01 Reutilizar el equipo comprado | Sí | Sí | No (sensores nuevos) | Sí |
| RE-07 Sin más personal | Sí | Sí | Sí | Parcial |
| Costo y riesgo de implementación | Bajo | Medio | Alto | Bajo |


### 4.2 La decisión

> **Solución seleccionada: S-2 como núcleo, con S-1 dentro y S-4 alrededor; S-3 queda como evolución**
>
> **S-2** es la única que ataca la falta de personal (P-05) y los tres drivers de mayor prioridad, y lo hace con el equipo ya comprado (RE-01): las funciones de pago electrónico y de alarma existen y estaban apagadas.
>
> **S-1 queda incluida:** el método de Smartmedia (pruebas de desempeño y prototipos) se adopta como la forma de diseñar y aceptar cada pantalla. No se descarta su trabajo: se lleva a un equipo que ya no necesita boleto.
>
> **S-4 se suma** porque los problemas 1, 2 y 6 son de gobierno: ningún software los resuelve solo.
>
> **S-3 no se descarta, se aplaza:** la arquitectura deja preparados el tarifario configurable (EAC-08) y el evento de ocupación. Se activa cuando haya datos que justifiquen la inversión en sensores.


## 5. Solución seleccionada: SIEP


### 5.1 Arquitectura del software

**Estilo principal: arquitectura orientada a servicios (SOA), un servicio por proceso de negocio.** Los cinco procesos de la primera descomposición se convierten en cinco servicios, más uno de integración. Se justifica con la escalera de la lámina de SOA de clase: el negocio **define** sus procesos, **desarrolla los procesos de negocio como servicios**, **cada servicio evoluciona independientemente** y el resultado es una solución **distribuida multinivel**. El tamaño de cada servicio ya está decidido por la descomposición del §3.2, y cada Delegación puede adoptar los servicios a su ritmo (RE-08).

| Estilo | Dónde se aplica | Driver que lo justifica |
|---|---|---|
| **SOA** (principal) | Cinco servicios de negocio y uno de integración | RE-08 · RE-14 · EAC-08 |
| **Basada en eventos** | Pagos, infracciones, alarmas y fallas se publican en un bus; notificaciones, sanción y tablero se suscriben | EAC-07 · EAC-09 · EAC-03 |
| **Capas** | Dentro de cada servicio: presentación, negocio, datos e integración | EAC-08 · mantenibilidad |
| **Cliente-servidor con guardar y reenviar** | El parquímetro y la app del verificador trabajan sin conexión y sincronizan después | EAC-03 · EAC-04 · RE-02 |
| **Tuberías y filtros** | Analítica: eventos, limpieza, ocultar la placa, agrupar por zona, indicadores | EAC-06 · EAC-09 |

> **Lo que se descartó, y por qué**
>
> **Microservicios:** dividir cada servicio en decenas de piezas exige un equipo de operación que el programa no tiene y no puede contratar (RE-07).
>
> **Monolito:** obligaría a todas las Delegaciones a cambiar al mismo tiempo (RE-08) y una falla del cobro tumbaría también la verificación.

**Las cuatro decisiones que cambian el día a día:**

- **El pago se liga a la placa, no a un boleto.** Desaparece el boleto mal colocado que originó la multa injusta citada en el caso, y el verificador consulta la placa en vez de leer tableros (P-03, P-04, P-05).
- **Se habilitan las funciones apagadas del equipo:** pago con tarjeta por la red inalámbrica y aviso de vandalismo. La alarma ya no necesita a una persona mirando una pantalla: genera sola la orden al proveedor y el aviso a la policía municipal (EAC-07, RE-07).
- **La sanción queda separada del cobro.** El verificador solo registra evidencia; la multa nace cuando el oficial de tránsito la confirma (EAC-05, RE-03). En Guatemala, ese oficial es la Policía Municipal de Tránsito.
- **Todo lo que se cobra se publica.** El tablero de transparencia muestra la recaudación por zona y el reparto 70/30 conciliado con el banco (EAC-09, P-06).

![[02-Diagramas/caso-parquimetros/3-arquitectura/bloques-parq.svg]]

*Figura 6. Diagrama de bloques: productores, enrutador y consumidores de eventos.*

![[02-Diagramas/caso-parquimetros/3-arquitectura/despliegue-parq.svg]]

*Figura 7. Diagrama de despliegue de SIEP.*

**El despliegue.** Arriba, los cuatro dispositivos de los usuarios; al centro, la nube del gobierno de la ciudad con el borde de red, el clúster de los seis servicios, la mensajería, la analítica y la base de datos; abajo, la réplica en una segunda región; a la derecha, los sistemas externos del banco y de la autoridad de tránsito. El tamaño de los servidores es una estimación. Las figuras 7a a 7c muestran cada zona con más detalle.

![[02-Diagramas/caso-parquimetros/3-arquitectura/despliegue-parq-detalle-1-usuarios.png]]

*Figura 7a. Despliegue, detalle: dispositivos de los usuarios.*

![[02-Diagramas/caso-parquimetros/3-arquitectura/despliegue-parq-detalle-2-nube.png]]

*Figura 7b. Despliegue, detalle: nube del gobierno de la ciudad y región secundaria.*

![[02-Diagramas/caso-parquimetros/3-arquitectura/despliegue-parq-detalle-3-externos.png]]

*Figura 7c. Despliegue, detalle: sistemas externos.*


### 5.2 Calidad del software

**Modelo de calidad.** Se usan los dos modelos de ISO/IEC 9126 que da el programa: el de **calidad del producto** (seis características) para la arquitectura, y el de **calidad en uso** (eficacia, productividad, seguridad y satisfacción, en un contexto específico de uso) para lo que el caso mide con personas. ISO/IEC 25010, sucesora de la 9126 dentro de la familia ISO 25000, se menciona como referencia para el traslado; la estructura no cambia.

| Modelo | Característica | Métrica | Umbral | Driver |
|---|---|---|---|---|
| Calidad en uso | Eficacia | % de participantes que completan la tarea | ≥ 72 % | EAC-01 |
| Calidad en uso | Productividad | Tiempo para completar el pago | ≤ 90 s | EAC-01 |
| Calidad en uso | Seguridad | Multas anuladas por error del sistema | ≤ 1 por cada 1.000 | EAC-05 |
| Calidad en uso | Satisfacción | Encuesta de cierre de la prueba, escala de 1 a 5 | ≥ 4 de promedio | P-06 |
| Producto | Funcionalidad › seguridad | Consultas a placas sin bitácora | 0 | EAC-05 · EAC-06 · EAC-11 |
| Producto | Fiabilidad | Pagos perdidos sin conexión · disponibilidad del cobro | 0 · ≥ 99,5 % | EAC-03 · EAC-07 |
| Producto | Usabilidad › comprensibilidad | % que encuentra tarifa, máximo y reclamo | ≥ 80 % en ≤ 10 s | EAC-02 |
| Producto | Eficiencia | Respuesta de verificación (95 de cada 100 consultas) | ≤ 2 s | EAC-04 · EAC-10 |
| Producto | Mantenibilidad | Tiempo de cambiar una tarifa de zona | ≤ 1 día hábil | EAC-08 |
| Producto | Portabilidad | Días para instalar SIEP en otra municipalidad | ≤ 20 días hábiles (supuesto) | RE-08 |


#### El 72 %, y cómo se mejora la forma de fijarlo

El 72 % sale de multiplicar dos probabilidades: que la persona **encuentre** la información (Smartmedia proponía 90 %; Margarita la bajó a **80 %** porque la gente usa el parquímetro con prisa) y que, encontrada, la **use bien** (se mantuvo en **90 %**): 0,80 × 0,90 = 0,72. Es un buen punto de partida, pero aplica el mismo número a todas las tareas. Proponemos **fijar el umbral por tarea, según su consecuencia**:

| Tarea | Consecuencia de fallar | Umbral propuesto |
|---|---|---|
| Pagar por placa | Una multa injusta | ≥ 81 % (el máximo teórico del método) |
| Entender la tarifa y el tiempo máximo | Pagar de más o de menos | ≥ 72 % |
| Saber cómo reclamar | Frustración y percepción de abuso | ≥ 72 % |
| Ubicar el número del parquímetro | Molestia menor | ≥ 64 % (0,80 × 0,80) |

**Cómo se evalúa.** Cada entrega se acepta con una **prueba de desempeño** (Sless): tareas, participantes que no conocen el diseño, protocolo de entrevista, registro cuantitativo y cualitativo, comparación contra el umbral, corrección y nueva ronda. Se agregan tres mejoras: hacerla **en la calle** con el permiso tramitado desde la fase previa (RE-10), subir a **12 participantes** por ronda para que el porcentaje signifique algo, y **grabar en video**. La arquitectura se evalúa además contra los once EAC antes de construir (paso de evaluación del ciclo, §5.3).


### 5.3 Arquitectura en el ciclo de vida

**Qué metodología.** La lámina de clase dice que la elección depende de siete factores. Aplicados al caso:

| Factor | En este caso | Empuja hacia |
|---|---|---|
| Certidumbre de los requisitos | Baja en la interfaz (se descubre probando con personas); alta en la norma de multas | Ágil en la interfaz |
| Estabilidad del alcance | Cambia por zona y por Delegación | Ágil |
| Cadencia de entrega | Entregas frecuentes: una colonia piloto, luego otras | Ágil |
| Riesgos | Altos al inicio: legal (placas), vandalismo, aceptación vecinal | Iterativo guiado por riesgo |
| Seguridad | Datos personales y dinero público | Controles formales en cada entrega |
| Proyecto | Hardware ya comprado, software nuevo e integraciones con otras autoridades | Mixto |
| Organización | Gobierno con procesos de compra y aprobación formales | Fases con hitos |

> **Decisión: un ciclo híbrido**
>
> **Por fuera, el modelo en espiral** (NT1 de la unidad 3, Meaurio y Schmieder): cada vuelta define objetivos y alternativas, analiza riesgos, hace ingeniería y planifica la siguiente. Es lo que el caso ya hizo sin nombrarlo: diagnóstico, concepto, prototipo, prueba y vuelta a la mesa de trabajo.
>
> **Por dentro, Scrum con arquitectura** (lámina de clase *Proceso Scrum en la arquitectura de software*): los pasos resaltados son 1, especificación de CDU (§3.3); 2, priorización de CDU (§3.6); 4, arquitectura base en el primer sprint (§5.1); y 9, refinamiento de la arquitectura del sprint 1 al n.
>
> **Los requisitos significativos para la arquitectura** (NT3): EAC-05, EAC-06 y EAC-03. Si cambian, la arquitectura sería otra.

| Etapa del ciclo de la arquitectura | Qué se hace en SIEP | Etapa del proyecto |
|---|---|---|
| Requerimientos | Diagnóstico con usuarios, requisitos de desempeño, drivers del §3 | Fase 0 |
| Diseño, documentación y evaluación | Documento de arquitectura; evaluación contra los EAC; prueba de desempeño de los prototipos | Fase 0 y sprint 1 |
| Implementación de la arquitectura | Arquitectura base: cobro por placa, verificación, bus de eventos | Construcción, sprints 1-4 |
| Pruebas | Pruebas de desempeño con personas en la calle y pruebas de carga contra EAC-04 | Cada sprint |
| Implantación | Colonia piloto, luego por zona con su comité | Fases 1-3 |

| Fase | Duración (supuesto) | Qué entrega | Problemáticas que cierra |
|---|---|---|---|
| **0** Concertación y diagnóstico | 2 meses | Consulta en la colonia piloto, comité, censo de cobros informales con la PDH, permiso para probar en la calle, base legal de placas | P-01 · P-02 |
| **1** Pago por placa y verificación | 4 sprints de 2 semanas | Equipo reconfigurado, cobro con monedas y tarjeta, app del verificador, sanción con evidencia, tablero mínimo | P-03 · P-04 · P-05 |
| **2** App del conductor y red monitoreada | 4 sprints | Pago y extensión por app, avisos, alarma de vandalismo, reportes de cobro informal | P-02 · P-05 · P-06 |
| **3** Información de ocupación y tarifa por demanda | Según datos de las fases 1-2 | Sensores en las zonas de mayor demanda; tarifa configurable por hora | Meta urbana |


### 5.4 Arquitectura de la información

La **arquitectura de la información** organiza los **contenidos** para que el usuario los encuentre y los use: categorías, etiquetas y navegación (NT2 de la unidad 3, Moyares y Bretones). No es la arquitectura del software. El caso es, en el fondo, un problema de arquitectura de la información, y el trabajo de Smartmedia recorre sus tres etapas: **investigación** (observación participativa), **organización** (las 13 partes de información y la tabla de antes, durante y después) y **diseño** (prototipos validados).

**Inventario de la información, reorganizado por momento de uso.** El criterio de organización deja de ser «lo que cabe en el panel» y pasa a ser la **tarea** del conductor en cada momento.

| Momento | Contenido | Dónde aparece | Etiqueta única |
|---|---|---|---|
| Antes del uso | Zona con cobro, horario, tarifa, cajones libres | Señal vertical con el color de la banqueta · mapa en la app | «Zona con parquímetro» |
| Antes del uso | Ubicación del parquímetro que corresponde | Número grande en el equipo y en la señal de la cuadra | «Parquímetro 0412» |
| Durante el uso | Tarifa por 30 min y tiempo máximo | Franja fija arriba de la pantalla, siempre visible | «Q3 por 30 min · máximo 4 h» |
| Durante el uso | Los tres pasos: placa, tiempo, pago | Una pantalla por paso, con la barra de progreso | «1 · Placa» «2 · Tiempo» «3 · Pago» |
| Durante el uso | Medios de pago aceptados | Paso 3, con monedas válidas | «Monedas · Tarjeta · QR» |
| Durante el uso | Aviso de que no hay otro cobro | Paso 3 | «Este es el único cobro» |
| Después del uso | Hora de vencimiento y folio | Comprobante en pantalla, impreso opcional y en la app | «Vence 11:00 · folio 0412-0001» |
| Después del uso | Aviso antes de vencer y extensión | Notificación en la app | «Le quedan 10 min» |
| Después del uso | Cómo reclamar una multa y cómo reportar un cobro informal | Comprobante, app y línea de atención | «Reclamos» · «Reportar cobro informal» |

**Mapa y navegación.** La pantalla del parquímetro es **lineal** (tres pasos, sin menús): en la calle y con prisa no se navega, se avanza. La app tiene **cuatro secciones** que repiten los momentos de uso: *Encontrar lugar* (antes), *Pagar* (durante), *Mis sesiones* (después) y *Ayuda y reclamos*. El tablero de transparencia se organiza por **zona**, porque así piensa el vecino: *¿cuánto se recaudó en mi colonia y en qué se invirtió?*

**La información también es un dominio de la arquitectura empresarial.** En la lámina de clase de arquitectura empresarial, la arquitectura de la información es el **modelo de datos**. Las entidades de SIEP son: Zona, Cuadra, Cajón, Parquímetro, Tarifa, Sesión de estacionamiento, Placa (con un código en lugar del número para la analítica), Pago, Presunta infracción, Multa, Reclamo, Reporte de cobro informal, Orden de mantenimiento y Movimiento de recursos (70/30). Las dos lecturas conviven y se declaran: contenidos para el usuario (NT2) y datos de la organización (lámina).


### 5.5 Factores externos: los cobros de personas ajenas a la municipalidad

El cuidacarros compite con el parquímetro por el mismo cajón. Gana cuando el pago legítimo es invisible, incómodo o se percibe injusto, y cuando el conductor teme un daño al vehículo. La respuesta combina las cuatro perspectivas, sin criminalizar a priori a quien hoy vive de eso.

| Perspectiva | Respuesta |
|---|---|
| Arquitectura de la información | La señal y la pantalla dicen que el único cobro es el del parquímetro; la tarifa está siempre visible, así el conductor sabe cuánto es lo correcto |
| Arquitectura del software | CU-12 envía el reporte con ubicación y hora, sin datos del denunciante (EAC-11). La analítica cruza la ocupación observada por el verificador con los pagos registrados: una cuadra llena y sin pagos es una cuadra capturada |
| Calidad del software | Seguridad en uso: el conductor no debe exponerse. El reporte es anónimo y la app muestra la línea de emergencia si hay amenaza |
| Arquitectura en el ciclo de vida | La fase 0 incluye un censo de cuidadores y un protocolo con la policía municipal y la Procuraduría de los Derechos Humanos, como en Antigua Guatemala; la implantación por zona se coordina con ese protocolo |
| Negocio (opción a decidir por la Delegación) | Ofrecer a quienes se registren un trabajo formal de orientación al usuario en la zona, pagado con parte del 30 % de reinversión comunitaria. Requiere base legal y no reemplaza la verificación |


## 6. Respuestas a las cuestiones del caso


#### Pregunta 1. ¿Qué otro tipo de estudio podría haber hecho Margarita para un diagnóstico inicial del problema?

Un estudio con **datos primarios** antes de contratar el diseño: (a) **observación de campo cuantitativa** por cuadra (ocupación, rotación, vehículos sin pago, presencia de cuidacarros); (b) **análisis de los datos que ya tenía**: recaudación por parquímetro, multas, reclamos y fallas, que muestran dónde falla el sistema; (c) **encuestas y grupos focales con vecinos** de colonias con y sin parquímetros, para medir la inconformidad (P-01, P-06); y (d) un **mapa de actores** con sus intereses, que habría puesto a los cuidacarros al centro desde el inicio. Su diagnóstico se basó en investigación secundaria y expertos, que sirven para formular hipótesis, no para medirlas.


#### Pregunta 2. ¿Qué problema del diagnóstico resuelve mejor la metodología expuesta, y cuál pudo abordar SERVIparq más a fondo?

Resuelve mejor el **P-03** (instrucciones de pago) y, en parte, el **P-04** (frustración del primer uso): la metodología mide si la persona encuentra y usa la información, que es exactamente esa falla. El que SERVIparq pudo abordar más a fondo es el **P-05** (falta de personal): el propio dispositivo tenía pago electrónico y alarma apagados, y verificar por placa habría multiplicado lo que cubre cada verificador. También quedaron fuera el P-02 y el P-06, que no son de interfaz sino de gobierno.


#### Pregunta 3. ¿De qué otra manera se podía clasificar la problemática para abordar soluciones pertinentes?

Por **causa raíz y perspectiva** (§1.3): gobierno y comunidad (P-01, P-06), actores informales (P-02), información (P-03, P-04) y capacidades del sistema (P-05). Otra forma útil es por **momento de uso** (antes, durante, después) y por **actor afectado** (vecino, conductor, verificador, autoridad). Y, desde la arquitectura, por **tipo de driver**: lo que exige una función nueva, lo que exige una cualidad medible y lo que viene impuesto desde afuera. Esta última clasificación dice directamente qué parte del sistema hay que diseñar.


#### Pregunta 4. ¿Qué otros sistemas se mencionan y cuáles habrían resuelto mejor las problemáticas?

El caso menciona el de **San Francisco** (sensores que avisan si el cajón está ocupado y tarifa ajustable a la demanda) y el de **Seattle** (página web y app con cajones libres y tiempo de búsqueda por cuadra), además del **Pay and Display** instalado. Seattle habría resuelto mejor P-03 y P-04, porque cubre el momento «antes del uso» que el panel no tiene. San Francisco habría atacado P-05 con supervisión automática, pero con costo alto, sensores expuestos al vandalismo y una tarifa variable difícil de explicar. La mejor relación costo-beneficio era **habilitar las funciones que ya tenía el equipo** y sumar la información de Seattle: es la solución S-2 (§4).


#### Pregunta 5. ¿Qué otras tareas o acciones podrían incluirse en los requisitos de desempeño?

**Antes:** saber si se puede pagar con tarjeta o app antes de llegar; identificar los colores de la banqueta. **Durante:** verificar que la placa escrita es la correcta antes de pagar; elegir el medio de pago; reconocer que no hay que pagarle a nadie más. **Después:** extender el tiempo sin volver al equipo; recibir aviso antes de vencer; consultar la sesión vigente; reportar una falla del equipo o un cobro informal; saber a dónde va el dinero. Se incluyen porque cada una corresponde a una queja del diagnóstico que la tabla acordada no cubre.


#### Pregunta 6. ¿Cuáles son los componentes principales del diseño de una prueba de desempeño?

(1) Las **tareas** y la secuencia esperada, que salen de los requisitos de desempeño; (2) los **criterios** de aceptación cuantitativos (encontrar y usar, y su producto: el 72 %); (3) los **participantes**, que no conocen el diseño; (4) el **protocolo de entrevista**, que pide actuar según lo que el dispositivo dice y no según lo que la persona ya sabe; (5) el **contexto**, idealmente el real; (6) el **registro** cuantitativo y cualitativo (lo que dicen, si encuentran, si dudan); (7) el **análisis**, que cuenta fallas del diseño y no de las personas; y (8) la **iteración** hasta cumplir el criterio.


#### Pregunta 7. ¿De qué otra manera pueden representarse los requisitos de desempeño?

Como **historias de usuario con criterios de aceptación** (*como conductor con prisa quiero pagar por placa para no colocar boleto; aceptado si 72 % lo logra en 90 s*); como **escenarios de atributos de calidad** de seis partes (EAC-01 y EAC-02); como **mapa del recorrido del usuario** (*customer journey*) por momento de uso; como **diagramas de actividad** del flujo de pago; o como **casos de uso con su descripción textual** (§3.3). Los EAC tienen la ventaja de que la medida queda escrita junto al requisito.


#### Pregunta 8. ¿Por qué el 72 % como nivel óptimo, y qué alternativa hay para definir los criterios?

Porque es el producto de dos probabilidades: **80 % encuentra** la información (Margarita bajó el 90 % sugerido porque la gente usa el parquímetro con prisa y a la intemperie) por **90 % la usa bien**. La premisa de la investigación previa dice que ningún desplegado supera el 81 %. **Alternativa:** fijar un umbral **por tarea, según la consecuencia de fallar** (§5.2), medir también el **tiempo en la tarea** y la **satisfacción**, y tomar como línea base la primera ronda con el equipo actual, exigiendo una mejora relativa medible.


#### Pregunta 9. ¿Qué tipo de propuesta entregó Smartmedia?

Un **rediseño de la información del dispositivo**: nueva secuencia de instrucciones, organización del panel y de los contenidos, validada con prototipos físicos a escala 1:1, más las **tablas comparativas de desempeño** entre el parquímetro actual y los prototipos. Es una propuesta de diseño de información con evidencia, no un sistema nuevo.


#### Pregunta 10. ¿Cómo ayudó el *bodystorming* al equipo de Smartmedia?

Le devolvió el **contexto** que el permiso faltante le había quitado: prisa, distancia entre el auto y el equipo, dónde poner el boleto, falta de cambio. Generó **empatía** en los diseñadores y en SERVIparq, que actuaron los roles; hizo creíble la prueba para los participantes; y produjo **ideas nuevas** a partir de las improvisaciones. Así aparecieron fallas que una entrevista no muestra, como colocar mal la placa o el boleto aunque se dijera haber entendido.


#### Pregunta 11. ¿Qué acción llevó a cabo SERVIparq a partir de esta experiencia?

El caso cierra con una junta de directivos y Delegaciones para el **plan de acción del año siguiente**, sobre estrategias de implementación y monitoreo. Lo razonable es que haya adoptado el rediseño de la interfaz en los equipos, incorporado las pruebas de desempeño como criterio de aceptación de futuros diseños y revisado la estrategia de implementación por colonia. Nuestra propuesta es que ese plan siga la hoja de ruta del §5.3.


#### Pregunta 12. ¿Cómo pueden complementarse o mejorarse las técnicas del caso?

Probar **en el contexto real**, con el permiso tramitado desde el inicio; grabar en **video**; subir el número de participantes; sumar **evaluación heurística** por expertos y **analítica de uso** (abandonos en cada paso del parquímetro y de la app); hacer **pruebas A/B** en cuadras distintas; incluir a **verificadores, oficiales y vecinos** como participantes, no solo conductores; y medir **satisfacción** con un cuestionario estándar al cierre.


#### Pregunta 13. ¿En qué otros contextos puede usarse esta metodología?

En todo desplegado informativo que alguien debe entender sin ayuda: **cajeros automáticos y quioscos de pago**, máquinas de boletos del transporte (en Guatemala, las recargas de la Tarjeta Ciudadana del Transmetro), **formularios de gobierno** (SAT, RENAP, licencias), señalización de hospitales y aeropuertos, **instructivos de medicamentos** (el origen del método de Sless), facturas, contratos y aplicaciones móviles de servicios públicos.


#### Pregunta 14. ¿Es apropiado rediseñar la información constantemente?

**Sí, pero con método, no por moda.** Cambian las tarifas, los medios de pago, la tecnología y los usuarios, y la calidad en uso solo vale en su contexto. Se rediseña cuando la medición cae debajo del umbral o cambia el contexto; no cada vez que alguien opina, porque cambiar sin necesidad obliga a la gente a reaprender. Por eso la arquitectura deja la tarifa y los textos como **configuración** (EAC-08) y mide el desempeño en producción (CU-18): el rediseño se vuelve un ciclo con evidencia.


## 7. Parte desarrollada: prototipo del parquímetro con pago por placa

Siguiendo la arquitectura elegida, desarrollamos el **cliente del parquímetro** del CDU-02 (CU-04 con CU-05 y la extensión CU-06), que es donde se juegan EAC-01 y EAC-02. Es una página web que corre en cualquier navegador: `08-Tareas/prototipo-parquimetros/index.html`.

![[02-Diagramas/caso-parquimetros/4-prototipo/prototipo-cuatro-pantallas.png]]

*Figura 8. Las cuatro pantallas del prototipo: placa, tiempo, pago y comprobante.*

| Qué implementa | Decisión que materializa |
|---|---|
| Tres pasos lineales con barra de progreso y la tarifa fija arriba | Arquitectura de la información (§5.4): organización por momento de uso |
| El pago se liga a la placa y el comprobante dice que no hace falta boleto | Decisión 1 de la arquitectura (§5.1) |
| Tarifario del Acuerdo COM-40-2022: Q3 por 30 min la primera hora, Q3.50 desde la segunda y Q4 desde la cuarta | CU-05 · traslado a Guatemala (§2.2) |
| Monedas, tarjeta y QR | CU-06 · P-03 |
| Aviso de que es el único cobro y botón «Reportar cobro informal» | CU-12 · EAC-11 · §5.5 |
| Folio, número del parquímetro y línea de reclamos en el comprobante | CU-11 · P-04 |
| **Modo de prueba de desempeño:** cronometra cada intento, marca lograda o fallida, calcula la eficacia contra el 72 % y exporta CSV | EAC-01 · §5.2: el prototipo trae su propia herramienta de medición |


## 8. Conclusiones y recomendaciones


### 8.1 Conclusiones

- **La pantalla era la mitad del problema.** El método de Smartmedia resolvió bien la información del parquímetro, pero los problemas de consulta vecinal, cobro informal y desconfianza son de gobierno y de arquitectura del sistema.
- **Lo que faltaba ya estaba en el equipo.** El parquímetro comprado podía cobrar con tarjeta y avisar vandalismo; habilitarlo, y ligar el pago a la placa, cubre la falta de personal sin contratar a nadie.
- **Un servicio por proceso** deja que cada Delegación adopte el sistema a su ritmo y que la tarifa cambie sin tocar código.
- **El 72 % es un buen punto de partida**, pero vale más un umbral por tarea, según lo que cuesta fallar.
- **El cobro informal se combate ganándole**: con información visible, reportes sin riesgo para el conductor y un acuerdo previo con la comunidad, como mostró Antigua Guatemala.
- **Lo que se cobra se publica.** Sin transparencia sobre el 70/30, cualquier mejora técnica se percibe como otro cobro.


### 8.2 Recomendaciones

- Empezar por **una colonia piloto** con su comité vecinal y medir los once escenarios de calidad antes de crecer.
- Tramitar desde el inicio el **permiso para probar en la calle** y la **base legal de la base de datos de placas**.
- Hacer de la **prueba de desempeño** el criterio de aceptación de cada pantalla nueva, con al menos 12 personas.
- Dejar los **sensores y la tarifa por demanda** para cuando haya datos de ocupación que justifiquen la inversión.
- Para Guatemala: coordinar con la Policía Municipal de Tránsito y la Procuraduría de los Derechos Humanos el protocolo para los cuidacarros **antes** de instalar.


## 9. Supuestos y límites

- Las medidas de calidad, salvo el 72 % del caso, y el dimensionamiento del despliegue son **supuestos de diseño**.
- La solución se diseña para SERVIparq (Ciudad de México, 2012); el traslado a Guatemala usa hechos públicos de 2023 a 2026 citados en el §2.2. El estado legal de MarbEx en Antigua puede haber cambiado después de julio de 2026.
- La opción de formalizar a los cuidadores es una propuesta para que la decida cada Delegación; requiere base legal.
- El prototipo es de interfaz: simula el cobro y no se conecta a un banco ni a una base de datos.


## 10. Referencias

- Morales Zaragoza, N. (2015). *Repensando los parquímetros, un acercamiento al diseño de interfaces desde la perspectiva del usuario* (Caso 4). Universidad Autónoma Metropolitana, Unidad Cuajimalpa.
- Bass, L., Clements, P. y Kazman, R. (2021). *Software Architecture in Practice* (4.ª ed.). Addison-Wesley.
- Covella, G. y Olsina, L. *Calidad en uso: especificación y evaluación*. Lectura del curso.
- ISO/IEC 9126-1:2001. *Software engineering. Product quality. Part 1: Quality model*. ISO.
- ISO/IEC 25010:2011. *Systems and software Quality Requirements and Evaluation (SQuaRE). System and software quality models*. ISO.
- Meaurio, V. y Schmieder, E. *Arquitectura del software y el ciclo de vida*. Nota técnica 1 de la unidad 3 del curso.
- Moyares, Y. y Bretones, A. (2010). *La arquitectura de la información en el ciclo de vida del software*. Nota técnica 2 de la unidad 3 del curso.
- Navarro, M. y otros. *Arquitectura del software y metodologías ágiles*. Nota técnica 3 de la unidad 3 del curso.
- Rojas de Morán, C. (2026). Presentaciones del curso Análisis y Diseño de Sistemas II: *Arquitectura de Software*, *Calidad del Software*, *Metodologías* y *Proceso Scrum en la arquitectura de software*. ECYS, USAC.
- Sless, D. y Wiseman, R. (1998). *Writing about medicines for people: usability guidelines for consumer medicine information* (2.ª ed.). Communication Research Institute.
- Emisoras Unidas (27 de febrero de 2023). Retiran objetos que obstaculizan espacios públicos para estacionar.
- Emisoras Unidas (27 de abril de 2026). Investigación sobre «aparta parqueos» y cobros irregulares.
- La Hora (20 de febrero de 2024). Las tarifas por estacionarse en la vía pública.
- La Hora (20 y 21 de mayo de 2026). La CC frena el cobro por estacionarse en la vía pública en Antigua Guatemala · Los millones que dejará de recibir la Muni de Antigua por el cobro del MarbEx tras el fallo de la CC.
- La Hora (23 de julio de 2026). CC suspende infracciones establecidas por la Muni de Antigua en el reglamento de parqueo municipal.
- Soy502 (7 de marzo de 2024). ¿Parquímetros inteligentes? La PMT explica cómo funcionarán.
- Prensa Libre (12 de octubre de 2017). Cuidadores de carros serán retirados de calles de Antigua Guatemala.


## Preguntas de repaso

1. ¿Por qué los cuidacarros no son actores del negocio?
2. ¿De dónde sale el 72 % y por qué conviene fijar el umbral por tarea?
3. ¿Qué tres problemáticas no se resuelven con diseño de interfaz?
4. ¿Qué escalón de la lámina de SOA fija el tamaño de los servicios?
5. ¿Qué le enseña a la arquitectura la suspensión de MarbEx por la Corte de Constitucionalidad?
