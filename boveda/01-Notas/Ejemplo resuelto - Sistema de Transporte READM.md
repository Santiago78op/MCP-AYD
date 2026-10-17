---
tema: Calidad del software
fuente: "Presentación de clase «Calidad del Software» (MBA. MSc. Claudia Rojas de Morán) — archivo 00-Fuentes/lecturas/Calidad del SW Parte II.pdf, 23 diapositivas. NÚCLEO. Está en la carpeta de lecturas, pero es material de clase: lleva su encabezado y su pie. + COMPLEMENTO — procedencia probable de las tablas (Cervantes, Velasco y Castro, «Arquitectura de software: conceptos y ciclo de desarrollo») y la lectura de las figuras sin texto, marcadas. La clase la volvió a dar el 16/10: capturas_U3_F1 26-31 = láminas 14-19, 32-33 = 21-22, 34 = 20 (la 23 repite ese diagrama)"
fecha: 2026-10-12
alias: [READM, RedADM, sistema de transporte, EAC, EaC, escenario de atributo de calidad, bus de eventos, ejemplo de calidad]
---

# Ejemplo resuelto — Sistema de Transporte READM

El encadenamiento **completo** que la catedrática resolvió en la presentación *Calidad del Software*:
del diagrama de contexto al diagrama de despliegue, pasando por los drivers y el bus de eventos. Es
el **molde** de una entrega de arquitectura: cada lámina corresponde a un criterio de la rúbrica del
[[Plan - Caso Harley-Davidson]].

> [!important] Lo que este material resuelve
> **«EaC» son los escenarios de atributos de calidad.** La tabla de drivers de calidad usa el
> identificador `EAC-nn`, y el primer escenario está escrito en seis partes rotuladas. Era la duda
> 41 de [[Preguntas pendientes para clase]].

## 1. La cadena, lámina por lámina

| # | Lámina | Qué muestra | Criterio que cubre |
|---|---|---|---|
| 2 | *Sistema de Transporte READM* — Diagrama de contexto | El sistema al centro (círculo), entidades externas (rectángulos) y flujos de datos con nombre | caso de negocio |
| 3 | *CDU ALTO NIVEL. Core del Sistema* | Una elipse, **Reserva y Venta de Boletos ADM**, y cinco actores con barra de negocio | caso de negocio |
| 4 | *CDU ALTO NIVEL. Primera Descomposición* | Cinco procesos y los actores del core, más uno nuevo | caso de negocio |
| 5 | *Stakeholders* | Tabla: Nombre · Descripción · Responsabilidades | stakeholders |
| 6 | *Características del Sistema* / *Alcance del Sistema* | Características `CAR-nn` con prioridad y objetivo de negocio; alcance por entregas | — |
| 7-8 | *CDU EXPANDIDOS. Driver Funcional* | Reservar Boletos y Comprar Boletos, con «include» | drivers RF |
| 9-10 | *CDU EXPANDIDOS. Requisitos / Drivers Funcionales* | Diagrama de CU del sistema y tabla `CU-nn` | drivers RF |
| 11 | *CDU EXPANDIDOS. Requisitos / Drivers de Atributos de Calidad* | Tabla `EAC-nn` | drivers de calidad |
| 12 | *Drivers de Restricción* | Tabla por tipo de restricción | drivers de restricción |
| 13 | *MATRICES DE TRAZABILIDAD* | Interesados contra vistas de la documentación | matrices |
| 14 | *DIAGRAMA DE BLOQUES. Arquitectura basada en Eventos* | Productores, enrutador y consumidores | estilo |
| 15 | *Perspectiva Lógica: CAPAS/SOA* | Cinco capas y su responsabilidad | estilo |
| 16 | *Diagrama de Componentes* | Componentes dentro de cada capa | — |
| 17-18 | *Diagrama de Distribución* / *Diagrama de Despliegue* | Nodos, capas y componentes dentro | despliegue |
| 19-23 | *¿Cómo integramos el bus de eventos?* | El bus como componente con interfaz publicador/suscriptor | estilo |

## 2. El caso de negocio (láminas 2-4)

![[adjuntos/calidad-del-software-parte-ii/01-contexto-readm.png]]

El contexto pone **RedADM** al centro, con *Usuarios*, *Administrador*, *Sistemas de terceros* y
*Sistemas de pagos*, y trae su propia leyenda: *Sistema a desarrollar*, *Entidad externa*, *Flujo de
datos*. Los flujos van con nombre: *Datos de viaje*, *Número de tarjeta de crédito*, *Boletos*,
*Información de pagos*, *Confirmación de pagos*, *Reportes*.

![[adjuntos/calidad-del-software-parte-ii/02-cdu-core-reserva-venta-boletos.png]]

**Core:** una sola elipse, *Reserva y Venta de Boletos ADM*, con cinco actores: Usuarios, Marketing,
Pasarela de Pago, VTP y Director de Operación. Actores y caso de uso llevan la barra de negocio.

![[adjuntos/calidad-del-software-parte-ii/03-cdu-primera-descomposicion.png]]

**Primera descomposición:** *Reserva de Boletos*, *Comprar Boletos*, *Cancelaciones*, *Gestión de
Mercadeo y Promoción* y *Reportes y Catálogos*. Aparece un actor que el core no tenía,
*Patrocinador*, y el *Director de Operación* del core figura como *Administrador de Operación*.
Confirma la regla de [[Ejemplos resueltos de casos de negocio]]: los actores pueden **crecer** al
descomponer.

## 3. Stakeholders, características y alcance (láminas 5-6)

![[adjuntos/calidad-del-software-parte-ii/04-stakeholders.png]]

La tabla de stakeholders tiene tres columnas: **Nombre · Descripción · Responsabilidades**. Lista
siete personas con su rol (dueño del sistema, representante de usuarios, representante de terceros,
administrador del sistema, administradora de la base de datos, representante de infraestructura y
líder de proyecto).

![[adjuntos/calidad-del-software-parte-ii/05-caracteristicas-y-alcance.png]]

**Características del sistema** — columnas *ID · Descripción · Prioridad · Objetivo de negocio
asociado*. Son doce, de `CAR-01` a `CAR-12`, con prioridad Alta, Media o Baja y un objetivo `ON-n`.
Mezclan funciones (*"permitir realizar la compra de boletos desde un navegador web"*) con calidad
(*"soportar de manera simultánea por lo menos cien interacciones"*, *"estar disponible 24 horas al
día y, en caso de falla, retomar actividad en, máximo, cinco minutos"*).

**Alcance del sistema** — por entregas:

| Número de entrega | Tema principal | Características a incluir |
|---|---|---|
| 1.0 | Funcionalidad básica | CAR-01, CAR-02, CAR-03, CAR-04, CAR-07, CAR-08, CAR-11, CAR-12 |
| 2.0 | Estabilidad del sistema e integración con terceros | CAR-05, CAR-09, CAR-06 |
| 3.0 | Visibilidad | CAR-10 |

## 4. Drivers funcionales (láminas 7-10)

![[adjuntos/calidad-del-software-parte-ii/06-cdu-expandido-reservar-boletos.png]]

![[adjuntos/calidad-del-software-parte-ii/07-cdu-expandido-comprar-boletos.png]]

![[adjuntos/calidad-del-software-parte-ii/08-drivers-funcionales-diagrama.png]]

![[adjuntos/calidad-del-software-parte-ii/09-drivers-funcionales-tabla.png]]

La tabla tiene tres columnas: **ID · Descripción · Característica asociada**. Ocho casos de uso,
de `CU-01` a `CU-08`, cada uno trazado a su `CAR`. El diagrama muestra dos actores, *Usuario* y
*Administrador*, con generalización entre ellos.

> [!warning] Dos cosas de estas láminas que chocan con otras reglas de clase
> - `CU-08` es *"Administrar Catálogos"*, y la propia tabla anota: *"en realidad este caso
>   representa a múltiples casos de uso"*. La regla de no nombrar casos «crear / editar / consultar»
>   sigue en pie: esa nota lo reconoce.
> - En la lámina 8, *Checkout* incluye *Seleccionar Dirección de Envío* en un sistema de boletos de
>   autobús: es el ejemplo genérico de la herramienta, no del caso.

## 5. Drivers de atributos de calidad — los EAC (lámina 11)

![[adjuntos/calidad-del-software-parte-ii/10-drivers-atributos-calidad-eac.png]]

Columnas: **ID · Categoría · Escenario · Prioridad**.

| ID | Categoría | Escenario | Prioridad |
|---|---|---|---|
| EAC-01 | Desempeño | **Fuente de estímulo:** un usuario. **Estímulo:** selecciona la opción "buscar" una vez que ha elegido las ciudades de salida y destino, así como las fechas de su viaje. **Artefacto:** en la pantalla de consulta (CU-01). **Entorno:** en un momento normal de operación y hay cien usuarios conectados al sistema. **Respuesta:** el sistema procesa la petición y muestra la lista de corridas. **Medida de la respuesta:** en un tiempo no mayor a dos segundos. | (A, A) |
| EAC-02 | Disponibilidad del sistema | Ocurre una falla interna del sistema que detiene su operación en un momento en que él estaba funcionando de manera normal. El sistema vuelve a operar normalmente en un periodo no mayor a cinco minutos. | (M, A) |
| EAC-03 | Seguridad | Un atacante intercepta la comunicación entre la PC de un usuario y el sistema mientras tal cliente realiza la compra de un boleto (CU-02) en un momento normal de operación. El atacante no obtiene ninguna información en claro (no cifrada). | (A, B) |
| EAC-04 | Usabilidad | Un usuario captura con errores los campos de un formato en el navegador mientras hace la compra de un boleto (CU-02), en un momento normal de operación. El sistema resalta los campos llenados erróneamente y describe instrucciones de llenado. | (M, A) |
| EAC-05 | Facilidad de prueba | Un probador realiza examinaciones unitarias de los componentes del sistema encargados de la lógica de negocio y la persistencia de datos en tiempo de desarrollo. El total de los componentes pueden ser probados de forma unitaria sin modificaciones en el código de estos componentes. | (B, B) |
| EAC-06 | Modificabilidad | Un desarrollador cambia el idioma de la interfaz de usuario del sistema en tiempo de desarrollo/mantenimiento. El nuevo idioma se agrega de manera exitosa sin requerir el cambio y la recompilación del código. | (M, B) |

Lo que se aprende de la tabla:

- **Las seis partes** van rotuladas solo en el primero; los demás las traen en prosa, pero están
  todas. Coinciden con [[Atributos de calidad]] §7, con dos nombres propios: *fuente de estímulo* y
  *medida de la respuesta*.
- **Cada escenario se ancla a un caso de uso** (`CU-01`, `CU-02`) cuando el artefacto es una
  función.
- **La prioridad es un par** de letras entre A, M y B.
- **Las categorías** son desempeño, disponibilidad, seguridad, usabilidad, facilidad de prueba y
  modificabilidad.

> [!note] COMPLEMENTO — qué significa el par de la prioridad
> La lámina no lo define. En el libro del que parece salir la tabla (Cervantes, Velasco y Castro),
> el primer valor es la **importancia para el negocio** y el segundo la **dificultad técnica** de
> lograrlo. Es la misma lectura de dos ejes de [[Guía - Drivers de calidad y restricción]]. Si se
> usa en una entrega, **declarar** la lectura.

> [!warning] Otra lista de categorías
> Esta tabla usa *desempeño*, *facilidad de prueba* y *modificabilidad*, que no están con ese nombre
> en la lista de siete de [[Drivers arquitectónicos]] (rendimiento, escalabilidad, disponibilidad,
> seguridad, mantenibilidad, usabilidad, fiabilidad). Las dos son de clase: elegir una y declararla.

## 6. Drivers de restricción (lámina 12)

![[adjuntos/calidad-del-software-parte-ii/11-drivers-restriccion.png]]

| Tipo de restricción | Descripción |
|---|---|
| **Del cliente** | Tiempos de entrega y presupuestos establecidos. Véase la sección 5.3 del documento de visión y alcance. |
| **De la organización de desarrollo** | Los ingenieros de los que se dispone están familiarizados con los siguientes *frameworks* de Java: Java Server Faces (JSF), *Spring* e *Hibernate*. |

Son **dos tipos**, no las seis categorías de [[Drivers arquitectónicos]]. No se contradicen: las
seis sirven de lista de control para encontrarlas; estos dos, para decir **quién** la impone.

## 7. La matriz de la lámina 13

![[adjuntos/calidad-del-software-parte-ii/12-matriz-interesados-vistas.png]]

Bajo el título *MATRICES DE TRAZABILIDAD* hay una sola matriz, y **no cruza requisitos**: cruza
**interesados** (líder del proyecto, equipo de desarrollo, equipo de pruebas, representante de
infraestructura, arquitecto, representante de usuarios, director de operación) contra las **vistas**
de la documentación, agrupadas en *vistas de módulos*, *vistas de componentes y conectores*, *vistas
de localización* y *otra documentación*. Cada celda dice cuánto detalle necesita ese interesado:
`d` muy detallada, `m` considerable detalle, `p` poco detalle.

Los tres grupos de vistas son las tres [[Categorías de estructuras]] — y acá la tercera se llama
**de localización**.

## 8. El estilo: bloques basados en eventos y capas/SOA (láminas 14-15)

![[adjuntos/calidad-del-software-parte-ii/13-bloques-basado-en-eventos.png]]

El [[Diagrama de bloques de alto nivel]] se titula *Arquitectura basada en Eventos* y tiene tres
zonas:

| Zona | Bloques | Texto de la lámina |
|---|---|---|
| **Event Producer** | Website · Mobile app · Point-of-Sale | *"Un cliente reserva, cancela o pone una nueva orden de compra de boletos a través del sitio web"* |
| **Event Router** | el bus | *"El bus de eventos recibe, filtra y empuja los eventos a los clientes apropiados"* |
| **Event Consumer** | Admor. de BDD · Plataforma de Pagos · VTP | *"Los eventos desencadenan cambios en la disponibilidad de boletos en la BDD"* |

Cada flecha lleva el evento que transporta: *reserva / compra / cancelación*, *reserva / nueva
orden*, *cancelaciones*, *consultas de las corridas*, *consultas VTP*. Cada bloque tiene un **ícono**,
su nombre y una línea que dice qué hace.

![[adjuntos/calidad-del-software-parte-ii/14-perspectiva-logica-capas-soa.png]]

**Perspectiva lógica: CAPAS/SOA** — cinco paquetes con el estereotipo `«capa»` y dependencias
punteadas: Presentación y Servicios web dependen de Negocio; Negocio depende de Datos e Integración.

| Elemento | Responsabilidad |
|---|---|
| **Capa de presentación** | Engloba todos los componentes encargados de recibir interacción por parte del usuario y de mostrarle resultados. |
| **Capa de servicios web** | Expone servicios web para soportar la integración de sistemas externos. |
| **Capa de negocio** | Engloba componentes de coordinación que se encargan de llevar a cabo la ejecución de los casos de uso del sistema. |
| **Capa de datos** | Engloba componentes encargados de almacenar objetos en una base de datos, ocultando del resto de la aplicación el hecho de que se trata de una base de datos relacional. |
| **Capa de integración** | Permite la integración con sistemas externos (por ejemplo, sistema de cobros). |

> [!important] El ejemplo combina tres estilos, y no lo oculta
> El mismo sistema es **en capas** por dentro, **SOA** hacia afuera (la capa de servicios web) y
> **basado en eventos** entre sus partes. Es evidencia de clase de que una entrega puede —y suele—
> declarar un estilo principal y sus complementarios. Encaja con
> [[Guía - Selección del estilo arquitectónico]].

## 9. Componentes, distribución y despliegue (láminas 16-18)

![[adjuntos/calidad-del-software-parte-ii/15-diagrama-componentes.png]]

![[adjuntos/calidad-del-software-parte-ii/16-diagrama-distribucion.png]]

![[adjuntos/calidad-del-software-parte-ii/17-diagrama-despliegue.png]]

- **Componentes:** van **dentro del paquete de su capa**, con el estereotipo `«Domain Object»`, y
  la capa de negocio provee las interfaces *ServicioConsultaCorridas* y *ServicioCompraBoletos*.
- **Distribución:** los nodos (Dispositivo móvil, PC usuario, Sistema externo, Servidor web,
  Servidor aplicativo, Servidor BD, Sistema de pagos) con **las capas dentro**.
- **Despliegue:** *PC Usuario* (Navegador) — `«HTTP»` — *Servidor Web* (capa Presentación) —
  `«RMI»` — *Servidor Aplicativo* (capas Negocio y Datos) — `«JDBC»` — *Servidor BD*.

> [!warning] «Distribución» y «despliegue» aparecen como dos láminas distintas
> En [[Diagrama de despliegue]] quedó anotado que ella dice *"Diagrama de Distribución"* por el de
> despliegue. Acá hay una lámina con cada título: la de distribución reparte **capas** en nodos; la
> de despliegue baja al **componente** y rotula el protocolo de cada conexión. Es una diferencia de
> **nivel de detalle**, no de notación. Queda como duda 46.

## 10. ¿Cómo integramos el bus de eventos? (láminas 19-23)

![[adjuntos/calidad-del-software-parte-ii/18-bus-eventos-microservicios.png]]

Texto de la lámina 21:

> En diagramas de componentes, un bus de eventos se representa como un componente central que
> facilita la comunicación asíncrona entre otros componentes, utilizando un modelo de
> publicación-suscripción.

| Parte | Qué es |
|---|---|
| **Publicadores** | *"Componentes que generan y envían eventos al bus."* |
| **Suscriptores** | *"Componentes que se registran para recibir eventos específicos del bus."* |
| **Bus de eventos** | *"Componente central que recibe eventos de los publicadores y los distribuye a los suscriptores correspondientes."* |
| **Publicación** | los publicadores *"envían"* eventos al bus |
| **Suscripción** | los suscriptores *"reciben"* eventos del bus |

Cómo se dibuja: el bus como un componente **con una interfaz para publicar y suscribirse**; los
eventos como **objetos o mensajes**; y una interfaz que permita interactuar con él
*"independientemente de la implementación subyacente"*.

**Para el ejercicio** (lámina 22): *ServicioDeReservas/Compra* es el publicador,
*ServicioDeNotificaciones* el suscriptor y *BusDeEventos* el componente central. El primero envía
*ReservaRealizada*; el bus lo recibe, *"lo transforma en NotificacionDeReserva"* y lo envía al
segundo.

![[adjuntos/calidad-del-software-parte-ii/19-bus-eventos-componentes.png]]

**Los cuatro beneficios**, textuales:

| Beneficio | Texto |
|---|---|
| **Comunicación desacoplada** | *"Los componentes no necesitan conocerse directamente, reduciendo la complejidad y los acoplamientos."* |
| **Flexibilidad** | *"Se pueden agregar o quitar componentes sin afectar a otros, siempre y cuando se suscriban o publiquen a los eventos adecuados."* |
| **Escalabilidad** | *"El bus de eventos puede ser escalable para manejar un gran volumen de eventos y suscriptores."* |
| **Facilita la reutilización** | *"Los eventos pueden ser reutilizados por diferentes componentes."* |

Con esto, la **arquitectura basada en eventos** deja de estar solo nombrada (era la duda 6): tiene
diagrama de bloques, diagrama de componentes y beneficios.

## 11. Lo que la presentación no trae

Se titula *Calidad del Software*, pero **no desarrolla** los puntos de la unidad 2 del programa:
conceptos generales, normas ISO ni la lista de atributos. De calidad trae la tabla de EAC y nada
más.

**Actualización 2026-10-16:** la teoría llegó en otra tanda de capturas (`capturas_U3_F1` 0-25), que
además **repite** las láminas 14-23 de esta presentación (capturas 26-34, señal de que pesan en el
examen). Ver [[Calidad del software]], [[Norma ISO 9126]], [[Familia de normas ISO 25000]],
[[Atributos observables y no observables vía ejecución]] y [[Escenarios de calidad]].

## Notas relacionadas

- [[Ejemplos resueltos de casos de negocio]] — los cuatro encadenamientos anteriores
- [[Ejemplo resuelto - Parque de atracciones]] — el otro ejemplo que llega hasta el despliegue
- [[Drivers arquitectónicos]] · [[Atributos de calidad]] · [[Guía - Drivers de calidad y restricción]]
- [[Diagrama de bloques de alto nivel]] · [[Diagrama de componentes]] · [[Diagrama de despliegue]]
- [[Arquitectura en capas]] · [[Arquitectura orientada a servicios]] · [[Estilos arquitectónicos]]

## Preguntas de repaso

1. ¿Qué significa `EAC` y qué cuatro columnas tiene su tabla?
2. ¿Cuáles son las seis partes del escenario `EAC-01`, con los nombres que usa la lámina?
3. ¿Qué tres zonas tiene el diagrama de bloques basado en eventos y qué lleva cada flecha?
4. ¿Qué responsabilidad tiene la capa de servicios web y cuál la de integración?
5. ¿Cómo se representa un bus de eventos en un diagrama de componentes y cuáles son sus cuatro beneficios?
