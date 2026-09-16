---
tema: Primer Parcial — respuestas redactadas
fuente: "Primer Parcial. Producción.pdf — Caso SmartPress"
fecha: 2026-08-22
---

# SmartPress — Respuestas redactadas

Primer Parcial, Análisis y Diseño de Sistemas II. Este documento contiene las respuestas escritas; los diagramas y las tablas de drivers y matrices van aparte y se referencian donde corresponde.

## Antes de responder: la frontera que elegí

Lo primero que hice fue decidir qué es «el negocio», porque de eso depende todo lo demás. El caso describe una planta completa —AutoParts Guatemala— pero el proyecto aprobado no es la planta: es SmartPress, el control de calidad en línea de la producción de piezas de precisión. Esa es la frontera que voy a modelar. Quedan fuera ventas, finanzas, recursos humanos, compras y la operación del ERP: existen, pero no son el negocio que estoy analizando.

La consecuencia de esa decisión es la que más se nota en los diagramas: el operario de máquina, el supervisor de turno, el ingeniero de calidad, el director de planta y el equipo de TI están DENTRO del negocio, así que son trabajadores del negocio, no actores. Los actores son las áreas y los sistemas que quedan del otro lado de la frontera: el proveedor de materia prima, el Área de Producción, el PLC, el Área de Mantenimiento, el cliente ensamblador, el ente certificador y los sistemas legacy. Son siete.

Uso una sola convención de identificadores, la de la NT1: RFG-0nn para requerimientos funcionales, CUN-0n para casos de uso de negocio, CU-0nn para casos de uso del sistema, AC-0n para atributos de calidad y RES-x0n para restricciones. Y para clasificar calidad uso las siete categorías de clase, no las seis de ISO 9126, porque acá estoy identificando drivers y no respondiendo teoría.

## Parte I.1 — Core del negocio y primera descomposición

El core es un solo caso de uso de negocio, porque el core es el negocio entero sin abrir: «Gestión del Control de Calidad en Línea de la Producción de Piezas de Precisión (SmartPress)». Alrededor van los siete actores, cada uno con su asociación.

Puse al proveedor de materia prima y al ente certificador aunque el enunciado no los liste en la tabla de stakeholders. El proveedor entra porque la etapa 1 dice que cada lote llega con certificado de calidad, y ese certificado es un insumo del control de calidad. El ente certificador entra porque ISO 9001 e IATF 16949 no son papeles guardados: son auditorías que ocurren, y quien audita interactúa con el negocio. Lo declaro como asunción para que no parezca invento.

La descomposición tiene cinco procesos y no es casualidad: son las cinco etapas que el propio enunciado describe. CUN-01 recepción y calificación de materia prima; CUN-02 preparación y calibración de la máquina; CUN-03 monitoreo y control en línea del ciclo de producción; CUN-04 inspección final y mejora del modelo predictivo; CUN-05 trazabilidad, embarque y auditoría de calidad. Los nombré como sustantivos derivados de verbo, no como «crear», «consultar» o «registrar», porque eso sería descomposición funcional y no procesos de negocio.

El núcleo es CUN-03. Es donde el negocio genera su valor —detectar la desviación ANTES de que la pieza salga mal— y es también donde se concentran los requisitos duros de tiempo. CUN-01 y CUN-02 son de soporte, y CUN-05 es gerencial: control, auditoría y rendición de cuentas.

En la descomposición aparece un actor que no estaba en el core: el sistema de medición láser (CMM). No es un error. Los actores pueden crecer del core a la descomposición cuando afloran contrapartes que estaban implícitas; lo que no puede pasar es que uno desaparezca, y los siete del core siguen estando.

De los cinco procesos expandí dos, que es lo que pide el enunciado: CUN-03 y CUN-05. Los elegí porque son los que más pesan en la arquitectura. CUN-03 impone la latencia y la tolerancia a fallos; CUN-05 impone la inmutabilidad, la retención de siete años y el volumen. Los otros tres son importantes para el negocio, pero no cambian la estructura del sistema.

Al expandirlos cambié de plano: los CDU expandidos ya no son de negocio, son del sistema. Por eso ahí sí aparecen las personas como actores —operario, supervisor, ingeniero de calidad— y los estereotipos de negocio desaparecen. Mezclar los dos planos en un mismo diagrama invalida el artefacto, así que están separados a propósito.

## Parte I.2 — Los atributos de calidad y por qué son arquitectónicos

Inferí ocho atributos de calidad. Todos llevan un número, porque un atributo de calidad sin medida no es un driver: es un deseo, y no se puede probar si se cumplió. Cada uno lo escribí como escenario de seis partes (fuente, estímulo, artefacto, entorno, respuesta y medida) en la tabla anexa; acá explico por qué cada uno es arquitectónico y no un simple requisito de implementación.

**AC-01 — Rendimiento: la inferencia del modelo debe dar resultado en menos de 1 segundo para ciclos de 45 s y menos de 5 para los de 120 s.**

Es arquitectónico porque decide DÓNDE corre el modelo. Si la inferencia se hace en la nube, la latencia de internet es impredecible y no cabe en la ventana del ciclo. Este atributo, solo, obliga a procesamiento en el borde, dentro de la planta.

**AC-02 — Rendimiento del lazo de control: el sistema debe responder al PLC en menos de 200 ms.**

Obliga a separar el canal de control del canal de analítica. Si la orden de ajuste viaja por la misma cola que 12,500 mediciones por segundo, va a esperar detrás de ellas. Son dos caminos de ejecución distintos, con presupuestos de tiempo distintos.

**AC-03 — Disponibilidad: ante una caída de red de 30 segundos, cero mediciones perdidas y trazabilidad reconstruida al 100 %, sin corte visible para el operario.**

El enunciado dice que la red industrial tiene caídas esporádicas. Eso significa que no puedo asumir red confiable: hay que bufferizar en el borde y reconciliar después, con operaciones idempotentes para que reconciliar no duplique registros.

**AC-04 — Escalabilidad: el pico de 10× del turno de noche sin degradar el servicio.**

Obliga a desacoplar la ingesta con una cola y a particionar el almacenamiento por máquina y por tiempo. Descarta escribir sincrónicamente contra una base transaccional, que es exactamente lo que la Parte III propone hacer.

**AC-05 — Seguridad: 100 % de las órdenes de ajuste firmadas y autenticadas, cero aceptadas sin firma válida, nada en texto plano por la red.**

Este es el más serio de todos, porque el riesgo no es de datos: el enunciado dice que una orden incorrecta puede dañar la máquina o causar lesiones. Obliga a un broker de comandos con firma digital y autenticación mutua sobre OPC-UA.

**AC-06 — No repudio y consulta forense: registros inmutables y verificables, retención de 7 años, y responder una consulta forense en menos de 10 minutos sobre 1.3 PB.**

Obliga a almacenamiento por niveles —caliente, tibio y frío— y a un registro tipo WORM con hash encadenado. También obliga a separar el índice de trazabilidad de los datos crudos: si para encontrar un lote hay que recorrer petabytes, los 10 minutos son imposibles.

**AC-07 — Mantenibilidad: el equipo interno de 4 personas debe poder operar el sistema después de que el científico de datos se vaya a los 6 meses, con US$ 20,000 de capacitación.**

Este atributo no agrega funcionalidad: LIMITA. Acota cuántos componentes y cuántas tecnologías distintas puede tener la arquitectura, porque lo que 4 personas no pueden operar, en la práctica no existe. Es el que más tensiona con la prohibición del monolito.

**AC-08 — Usabilidad: un operario debe poder usar el sistema con 3 horas de capacitación o menos.**

Obliga a que la interfaz de piso sea deliberadamente pobre y distinta del tablero del supervisor y de la consola del ingeniero de calidad. Son tres interfaces, no una configurable.

## Parte I.3 — Las restricciones

Identifiqué 27 restricciones y las clasifiqué en las tres categorías que pide el enunciado: técnicas, de negocio y de sistema. Aclaro que en clase vimos seis categorías, pero acá uso las tres del enunciado para responder lo que se pregunta y no lo que yo sé.

Las técnicas son once y salen de la infraestructura y de las prohibiciones de la Junta: OPC-UA obligatorio, 25 PLC Siemens, red industrial con caídas, internet de 100 Mbps compartido, un data center de 4 servidores con 20 TB de SAN, nada de datos crudos en la base transaccional, base con particionamiento y retención, prohibición del monolito, cifrado obligatorio, solo agregados a la nube y el stack .NET/SQL Server/Azure del equipo.

Las de negocio son once: US$ 150,000 de infraestructura, US$ 20,000 de capacitación, un equipo de 4 personas sin experiencia en Big Data ni ML, un consultor disponible solo 6 meses, la planta que no para 24/7, ISO 9001, IATF 16949, retención legal de 7 años, la confidencialidad de los datos, el máximo de 3 horas de capacitación para operarios, y la urgencia que dan los US$ 2.5 millones ya pagados en penalizaciones.

Las de sistema son cinco y son las interfaces con lo que ya existe: el ERP legacy en Oracle Forms con REST de 1-2 segundos, el sistema de mantenimiento con la misma limitación, los 25 PLC por OPC-UA en lectura y escritura, el CMM con su inspección destructiva de 3 minutos sobre el 5 % de las piezas, y el código QR como contrato de trazabilidad con el cliente.

Algo importante: las restricciones no se priorizan. Todas son obligatorias y ninguna lleva medida —se cumplen o no se cumplen. Lo que sí hice fue anotar, para cada una, qué decisión de diseño bloquea; eso es lo que las convierte en driver y no en una lista de datos del enunciado.

## Parte II — Los conflictos entre drivers

Identifiqué seis conflictos. Los ordené empezando por el que más compromete el objetivo del proyecto.

### Conflicto 1 — El lazo de control no cabe en el tiempo que tiene

El enunciado pide dos cosas que no caben juntas en el mismo camino. Por un lado, el PLC exige respuesta en menos de 200 ms (AC-02) porque la máquina trabaja en tiempo real. Por otro, la orden de ajuste (RFG-003) nace de una predicción que tarda entre 2 y 5 segundos. Son dos órdenes de magnitud de diferencia. Y encima la Junta prohíbe depender de la nube para el tiempo real, así que ni siquiera puedo comprar velocidad con más hardware remoto. Es un choque entre un requisito funcional y un atributo de calidad, y también entre dos atributos de calidad.

Si no lo resuelvo, pasa lo siguiente: el CU-005 «Ejecutar acción correctiva» se dispara tarde. La máquina sigue inyectando mientras espera la orden y produce justo las piezas defectuosas que el proyecto existe para evitar. En un ciclo de 45 segundos, 5 segundos de inferencia son el 11 % del ciclo y la pieza ya está formada. En la práctica el sistema no evita nada: detecta tarde igual que el muestreo actual, y los US$ 2.5 millones de penalizaciones no se recuperan.

La vista más afectada es la de Procesos, porque el conflicto es de concurrencia y de tiempo: obliga a partir el sistema en dos hilos con presupuestos de tiempo separados, un lazo duro de control por debajo de 200 ms y un lazo blando de predicción que trabaja en segundos. También afecta la vista de Escenarios, porque el escenario CU-001 → CU-003 → «extend» CU-005 deja de ser una secuencia lineal al final del ciclo y hay que reescribirlo como predicción anticipada, con datos parciales, mientras el ciclo todavía corre.

### Conflicto 2 — El volumen no cabe en ningún lado

Se generan 5 TB por día de datos crudos y unos 500 GB por día ya procesados, y hay que guardarlos 7 años: 1.3 PB. El data center tiene 20 TB de SAN. Con datos crudos eso se llena en cuatro días; con datos procesados, en cuarenta. La salida obvia sería la nube, pero la política de seguridad solo deja subir análisis agregados, y los datos crudos no pueden salir de la planta. Y el presupuesto de infraestructura es de US$ 150,000, que además tiene que alcanzar para hardware y licencias. Es un choque entre restricciones, con AC-06 atrapado en medio.

Si no lo resuelvo tengo que elegir entre dos malas opciones. Si boto los datos crudos, el ingeniero de calidad se queda sin con qué reentrenar el modelo, y esa es la necesidad oculta que sostiene todo el valor del sistema: sin reentrenamiento, el modelo se degrada solo. Si no boto nada, incumplo la retención de 7 años y la trazabilidad que exige IATF 16949, con riesgo de perder la certificación y con ella a los clientes ensambladores.

Afecta la vista Lógica, porque obliga a partir el modelo de datos en dos repositorios distintos: uno de series de tiempo comprimido para lo crudo y uno relacional para el maestro de trazabilidad, con una relación explícita entre ambos. Y afecta la vista de Procesos, porque la agregación y la compresión dejan de ser un proceso nocturno y pasan a ser procesamiento en streaming, con su propia ventana de tiempo y su propio consumo de CPU compitiendo con la inferencia.

### Conflicto 3 — Parar la máquina contra no parar la máquina

El enunciado ordena detener la máquina inmediatamente cuando la predicción diga «pieza defectuosa». Pero el operario cobra un bono por producción y cada parada se lo baja; y la Junta directamente prohíbe parar la producción. Cada falso positivo del modelo es una parada injustificada, y el propio ingeniero de calidad dice que su prioridad es reducir falsos positivos. Lo grave de este conflicto es que la persona que debe obedecer la alerta tiene un incentivo económico para desobedecerla.

Si no lo resuelvo, el operario aprende a ignorar o a silenciar el sistema, o la planta lo desactiva por presión de producción, y SmartPress queda como un tablero decorativo: el control de calidad vuelve al muestreo de 1 de cada 100 al final de la línea y los reclamos siguen. Y si en cambio la política es agresiva y para todo, la planta pierde disponibilidad productiva sin que la tasa real de defectos baje.

Afecta la vista de Escenarios, porque el «extend [predicción = defectuosa]» no puede ser una condición de sí o no: hay que modelar umbral, nivel de confianza, confirmación humana (que es el CU-009) y el escenario del falso positivo, que hoy no está documentado. También afecta la vista de Procesos, porque la política de decidir entre ajustar parámetros o detener pasa a ser un componente con estado propio dentro del camino de control, y necesita poder correr en modo shadow para medirse sin parar nada.

### Conflicto 4 — La inmutabilidad frena la ingesta

Sellar cada registro de forma inmutable y verificable —hash, firma, encadenamiento, WORM— cuesta tiempo por cada escritura. Con 12,500 mediciones por segundo en régimen normal y 125,000 en el pico de la noche, ese costo se multiplica hasta que la ingesta ya no le sigue el ritmo al proceso físico. Es un choque entre dos atributos de calidad: seguridad y no repudio contra rendimiento y escalabilidad.

Si no lo resuelvo, la cola de ingesta crece hasta desbordarse justo en el turno de mayor carga y se pierden mediciones. Eso rompe RFG-004: quedan piezas sin expediente completo. Y cuando llegue un reclamo del cliente no voy a poder reconstruir el lote, que es exactamente la pérdida de trazabilidad que originó el proyecto, además de incumplir IATF 16949.

Afecta la vista Lógica, porque obliga a distinguir qué se sella y qué no: se sella el expediente de la pieza, que son millones de registros al día, no cada medición cruda, que son mil millones. Y afecta la vista de Procesos, porque el sellado tiene que salirse del camino crítico de ingesta y pasar a un proceso asincrónico por lotes, con su propia garantía de que no se saltó nada.

### Conflicto 5 — Un sistema distribuido para un equipo que no puede operarlo

La Junta prohíbe el monolito, y el caso exige un pipeline de streaming, un almacén de series de tiempo, un motor de ML con despliegue canary y un archivo histórico de petabytes. Nada de eso está en el stack del equipo, que son 4 personas de .NET, SQL Server, Azure y Angular. El único que domina esas tecnologías es el consultor, y se va a los 6 meses. Es un choque entre una restricción técnica y el atributo de mantenibilidad: la arquitectura correcta en el papel es inoperable por la organización que la va a recibir.

Si no lo resuelvo, al mes 7 nadie puede reentrenar el modelo ni diagnosticar por qué se cayó un componente. El modelo se degrada en silencio con el desgaste de moldes y sensores, los falsos negativos suben y los reclamos regresan, ahora con un sistema caro que la planta ya no entiende. Para mí este es el riesgo más probable de todo el caso, porque no falla el día uno: falla cuando ya nadie está mirando.

Afecta la vista Lógica, porque acota cuántos componentes y cuántas tecnologías distintas puede haber: empuja a un particionamiento mínimo de tres servicios y no de quince, y a usar servicios gestionados sobre el stack conocido en vez de plataformas nuevas. Y afecta la vista de Escenarios, porque el escenario de actualizar el modelo sin parar la producción (RFG-014) tiene que ser ejecutable por el equipo interno, no por el consultor, y eso cambia por completo cómo se diseña el pipeline de despliegue.

### Conflicto 6 — Firmar cuesta tiempo

Autenticar y firmar cada orden de ajuste agrega handshake, verificación de certificado y validación criptográfica a un camino que ya tiene apenas 200 ms de presupuesto. Y no puedo cambiar OPC-UA por un protocolo más liviano, porque cambiar las máquinas sería prohibitivamente caro. Es un choque entre dos atributos de calidad con una restricción técnica que tapa la salida fácil.

Si sacrifico la seguridad, una orden falsificada o mal formada puede dañar una máquina o causar lesiones —el enunciado lo advierte explícitamente— y ahí la responsabilidad ya no es de calidad, es civil y penal. Si sacrifico la latencia, caigo en el conflicto 1 y la retroalimentación llega tarde.

Afecta la vista de Procesos, porque hay que decidir dónde vive la verificación: conviene una sesión OPC-UA persistente con autenticación mutua establecida una sola vez, en lugar de verificar mensaje por mensaje, y hay que repartir el presupuesto de 200 ms por etapa. Y afecta la vista de Escenarios, porque hay que documentar dos escenarios que hoy no existen: el de la orden ilegítima rechazada y el de degradación segura, es decir, qué hace la máquina si no puede verificar la firma. Mi criterio es que no ejecuta.

## Parte III.1 — ¿Estoy de acuerdo con la tabla única SensorReadings?

No, no estoy de acuerdo. Y la primera razón no es técnica sino de cumplimiento: la Junta Directiva dice textualmente que no se pueden almacenar todos los datos crudos de sensores en la base transaccional. Eso es una restricción, y las restricciones no se discuten ni se priorizan: se cumplen. La decisión del equipo viola RES-T06 de frente. También viola RES-T07, que exige una base con particionamiento y retención, y una tabla plana sin estrategia de partición no lo cumple.

Aparte de eso, los números no dan. Son 25 máquinas por 500 mediciones por segundo por 86,400 segundos: 1,080 millones de filas por día, unos 5 TB diarios en crudo y 1.3 PB a 7 años, contra los 20 TB de SAN que hay y los US$ 150,000 de presupuesto. La tabla se llena en cuatro días.

El argumento del equipo sobre los índices está invertido. A 12,500 inserciones por segundo —y 125,000 en el pico de la noche— mantener un índice B-tree sobre Timestamp y MachineID no ayuda a la escritura: la degrada, y además produce fragmentación y contención de página. Los índices sirven para leer, y este es un problema de escritura sostenida.

El formato también está mal elegido. Con columnas SensorName y Value se está usando un modelo entidad-atributo-valor: una fila por medición, con el nombre del sensor repetido mil millones de veces al día, sin tipado fuerte y sin posibilidad de compresión columnar. Es el peor factor de expansión posible para este volumen.

Y hay dos consecuencias que rompen requisitos ya identificados. Primero, la consulta forense: reconstruir un lote de hace 7 años exigiría recorrer miles de millones de filas EAV, y no hay manera de cumplir los 10 minutos que pide el cliente (AC-06). Segundo, el tiempo real: si la ingesta escribe sincrónicamente contra la misma instancia que sirve las consultas de trazabilidad, la contención de escritura se propaga al lazo de control y compromete AC-01 y AC-02.

Quiero ser justo con el equipo en un punto: su intención —usar lo que ya sabemos— es legítima y tiene respaldo en AC-07, la mantenibilidad. El problema es dónde la aplicaron. SQL Server sí debe usarse, pero para el maestro de trazabilidad: la pieza, el lote, la máquina, el turno, el operario, los parámetros nominales y el resultado. Eso son millones de filas al día, no miles de millones, y ahí el equipo trabaja con lo que domina.

Mi propuesta, en resumen: la ingesta se desacopla con una cola en el borde de la planta, separada del lazo de control; los datos crudos van a un almacén de series de tiempo columnar comprimido, particionado por máquina y por ventana de tiempo, con retención corta de 7 a 30 días; los agregados por ciclo y por pieza —los 500 GB diarios— quedan en una capa tibia con retención media, y son lo único que puede subir agregado a la nube; el maestro de trazabilidad va en SQL Server; y el histórico va a un archivo WORM particionado por año, con hash encadenado y un índice de trazabilidad que permita llegar al lote sin recorrer los datos crudos.

## Parte III.2 — Cómo se lee la matriz de trazabilidad

Hice dos matrices con el formato de la NT1, figura 1, página 91. La primera cruza los drivers funcionales contra los casos de uso: marca con ● el caso de uso dueño de cada requerimiento y con X los que participan en su realización. Ninguna fila queda vacía, o sea que todo requerimiento tiene dónde realizarse; y ninguna columna queda vacía, o sea que no inventé casos de uso sin un requerimiento que los origine. La columna más poblada es CU-004, registrar la trazabilidad del ciclo, lo cual es coherente con que la pérdida de trazabilidad sea el problema que originó el proyecto.

La segunda matriz es la que responde de verdad a la pregunta. Cruza los drivers de calidad y de restricción contra los casos de uso implicados en el almacenamiento, y marca con un triángulo los que ejercen control directo sobre la decisión cuestionada. Ahí se ve el punto: RES-T06 cruza CU-002 y CU-004, que son justamente los dos casos de uso que la tabla única pretendía servir. Si el equipo hubiera consultado esa matriz, la restricción habría bloqueado la decisión antes de escribir la primera línea de SQL. Esa es la utilidad de la trazabilidad: no documentar lo que ya se hizo, sino impedir a tiempo lo que no se debía hacer.

Dos lecturas más que salen de esa matriz. La columna CU-004 concentra nueve drivers de control: un caso de uso con esa densidad de restricciones no admite que su almacenamiento se decida «porque ya lo sabemos hacer»; es un punto de arquitectura, no de implementación. Y AC-07 aparece a favor y en contra a la vez, lo cual no es una inconsistencia: trazado por caso de uso se ve exactamente dónde la mantenibilidad justifica usar SQL Server y dónde no, y así el argumento del equipo se salva a medias en lugar de perderse entero.

## Lo que dejé fuera, y por qué

No expandí CUN-01, CUN-02 ni CUN-04 porque el enunciado pide solamente dos CUN. No hice descripciones textuales de los casos de uso porque el enunciado las excluye explícitamente. No analicé las vistas de Desarrollo ni Física porque la Parte II acota el análisis a Lógica, Procesos y Escenarios. No prioricé los drivers de calidad porque en este parcial no se pide, y las restricciones por definición no se priorizan. Y no diseñé la arquitectura —componentes, capas, despliegue— porque lo que se pide es identificar los drivers, que son el insumo del diseño y no el diseño; lo único que propuse fue lo mínimo necesario para defender la respuesta de la Parte III.
