---
tema: Glosario
fuente: "Arquitectura de Software.pdf / Arquitectura de Software (1).pdf / CDU Negocio - Modelado de Drivers RF.pdf / capturas_U2 + PDF Tema 5 + IS 04 05b (2026-09-15) / capturas_U2_F2 (2026-09-16) / capturas_U2_F3 (2026-09-17)"
fecha: 2026-08-19
---

# Glosario — Análisis y Diseño de Sistemas

Glosario global de la materia, en orden alfabético. Cada término lleva una definición de 1-2
líneas y el enlace a la nota donde se explica a fondo.

---

## A

- **AC-0nn / NEC-0nn / CU-0nn / RFG-0nn** — La convención de identificadores de la NT1: actor, necesidad, caso de uso y requisito funcional general. Tres dígitos, y los CU prefijados por su paquete (`Administración::CU-011`). → [[Guía - Matrices de trazabilidad]]
- **Actor del negocio** — Rol que alguien o algo juega cuando interactúa con el negocio para beneficiarse de sus resultados. Siempre modela algo *fuera* del negocio. → [[Actor del negocio]]
- **Actor del negocio (notación)** — Monigote con una **barra diagonal cruzando la cabeza**; el CUN es una elipse con la diagonal en el borde. Sin la diagonal es un actor/CU **del sistema**. → [[Convenios del diagrama de CUN]]
- **AD (descripción arquitectónica)** — El producto de trabajo que expresa la arquitectura: "una colección de artefactos que documentan una arquitectura" (ISO 42010). → [[El ciclo del architecting]]
- **ADD (Attribute-Driven Design)** — Método del SAIP para diseñar la arquitectura convirtiendo drivers en estructuras, en rondas e iteraciones. → [[Guía - Drivers de calidad y restricción]]
- **ADL (Lenguaje de descripción de arquitectura)** — Lenguaje textual formal ideado para describir una arquitectura software en términos de componentes y conectores. Una de las tres formas de modelarla, con UML y los diagramas de bloque. → [[Lenguajes de descripción de arquitectura]]
- **Ágil (proceso)** — Proceso con cuatro rasgos: entrega rápida y frecuente, respuesta al cambio, arquitecturas que **emergen de equipos autoorganizados** y autoexamen del equipo. → [[Arquitectura y proceso de desarrollo]]
- **Agregación** — Relación es-parte-de con rombo **hueco** en el todo: la parte sobrevive al todo. → [[Relaciones y dependencias en UML]]
- **allocated-to / migrates-to** — Las dos relaciones de la estructura de despliegue: dónde reside un elemento de software, y a dónde puede migrar si la asignación es dinámica. → [[Diagrama de despliegue]]
- **API Gateway** — Patrón arquitectónico de la lista de clase: una única puerta de entrada delante de muchos servicios (la definición es complemento). → [[Patrones arquitectónicos]]
- **API RESTful** — Ver **REST**. → [[Tuberías y filtros]] §4
- **Arco de comunicación** — El nombre formal de la línea que une un actor con un caso de uso; es la misma que en el diagrama de CUN lleva la navegabilidad. → [[Caso de uso]]
- **Arqueología arquitectónica** — Recuperar la arquitectura de un sistema legacy sin documentación confiable (Clements). → [[El ciclo del architecting]]
- **Arquitecting** — El proceso de la arquitectura del software. → [[Proceso de diseño arquitectónico]]
- **Arquitecto de software** — Rol responsable de obtener los requisitos del cliente, generar el diseño de arquitectura, dar soluciones a los desarrolladores e integrar los requerimientos no funcionales. → [[Arquitecto de software]]
- **Arquitecto jefe** — El único rol que la clase marca como **necesario** cuando la arquitectura la diseña un equipo (los otros: arquitecto de aplicaciones, de infraestructuras, de datos). → [[Arquitecto de software]]
- **Arquitectura candidata** — La primera propuesta de arquitectura, todavía por validar: se produce en el **esfuerzo inicial** (guarda `[initial effort]` del flujo de Ambler). **En clase** (capturas_U2_F2, 25) la diapositiva la presenta con una tabla de **tipos**: conceptual, modular, código y ejecución, cada uno con sus elementos y relaciones. → [[Arquitectura de referencia]] · [[Proceso de diseño arquitectónico]]
- **Arquitectura centrada en el flujo de datos** — **En clase**: familia en la que *"la computación/procesamiento es dirigido por el flujo de datos en el sistema"* (capturas_U2_F3, 13); los datos se transforman pasando por filtros conectados por tuberías. *"Enfatiza la reutilización y la modificabilidad"* (15). Miembros: tuberías y filtros, secuencial por lotes. → [[Arquitectura centrada en el flujo de datos]]
- **Arquitectura de 2 capas (cliente-servidor)** — El cliente hace la petición y el servidor responde. Cliente y servidor son **roles**, no máquinas: un smartphone puede ser los dos. → [[Arquitectura en capas]]
- **Arquitectura de la nube** — Los componentes y subcomponentes que se encuentran en una nube, y el diseño que los conecta; "hay mucho más que solo tecnología". → [[Arquitectura en la nube]]
- **Arquitectura de referencia** — **En clase**: *"un modelo de referencia mapeado en elementos de software que cooperativamente implementan la funcionalidad definida en el modelo de referencia y flujos de datos entre ellos"*. Sale de modelo de referencia + patrón arquitectónico, y se adapta para llegar a la arquitectura de un sistema; **en sí no es una arquitectura**. En el flujo de Ambler es la que se reutiliza entre proyectos. → [[Arquitectura de referencia]]
- **Arquitectura de software** — La organización fundamental de un sistema: sus componentes, la relación entre ellos y con el ambiente, y los principios que guían su diseño y evolución. → [[Arquitectura de software]]
- **Arquitectura empresarial** — La arquitectura de **toda la organización**, que cada proyecto refina (*Refine Enterprise Architecture*). → [[Proceso de diseño arquitectónico]]
- **Arquitectura monolítica** — Agrupa toda la funcionalidad y servicios de la aplicación en una **base de código única**; escala verticalmente y se despliega entera. → [[Arquitectura monolítica]]
- **Arquitectura N-Capas (en o por capas)** — Arquitectura multinivel donde a cada nivel se le confía una **misión simple**. **En clase** (capturas_U2_F3, 0): la capa externa sirve a la interfaz de usuario, las intermedias dan utilería y SW de aplicaciones, la interna es la interfaz con el sistema operativo; y es *"especialización de la arquitectura cliente-servidor"* (10). Capa y nivel se usan como sinónimos. → [[Arquitectura en capas]]
- **Arquitectura orientada a servicios (SOA)** — **En clase**: *"la comunicación entre servicios, donde un servicio (cliente) realiza una solicitud (llamada) a otro servicio (proveedor) y espera una respuesta (retorno)"* (capturas_U2_F3, 33). Es de llamada y retorno **y** basada en eventos: *"puede usar motores de orquestación/coreografía e invocar servicios de forma asíncrona"* (34). → [[Arquitectura orientada a servicios]]
- **Artefacto (UML)** — El archivo físico que se despliega (`.jar`, `.ear`, `.dll`); se dibuja como rectángulo con la esquina doblada y se une a su nodo con `«deploy»` (SAIP). **En clase** (PDF Tema 5): *"cualquier producto obtenido durante el desarrollo"* —ejecutable, manual, script de BD, librería—, que **manifiesta** componentes y se dibuja dentro del nodo. → [[Diagrama de despliegue]]
- **Asociación** — Vínculo estructural estable entre elementos, con línea llena. → [[Relaciones y dependencias en UML]]
- **Asociación (en CUN)** — Relación entre un actor del negocio y un CUN que significa que el actor envía y/o recibe mensajes. → [[Modelo de casos de uso del negocio]]
- **Asociación reflexiva** — Asociación de una clase consigo misma; exige **rol** en cada extremo (jefe/empleado). → [[Diagrama de clases]]
- **ASR (requisito arquitectónicamente significativo)** — Requisito de calidad que impacta en la estructura del sistema; es uno de los componentes de los drivers en ADD. → [[Guía - Drivers de calidad y restricción]]
- **ATAM** — *Architecture Tradeoff Analysis Method*: evaluación en 4 fases y 9 pasos que produce riesgos, no-riesgos, sensibilidades y tradeoffs. → [[Evaluación de la arquitectura]]
- **Atributo de calidad (QA)** — Propiedad **medible o testeable** que indica cuán bien un sistema satisface las necesidades de sus stakeholders más allá de la función básica. → [[Atributos de calidad]]
- **Atributos de un buen diseño** — Durabilidad, utilidad y encanto; en software: de confianza y fácil de evolucionar, fácil de implementar, entendible. → [[Arquitectura de software]]

## B

- **Batch secuencial (secuencial por lotes)** — **En clase** (capturas_U2_F3, 28): *"los componentes son programas independientes; el supuesto es que cada paso se ejecuta hasta completarse antes que se inicie el siguiente"*. Estilo de la familia flujo de datos. → [[Arquitectura centrada en el flujo de datos]] §5
- **Bus de eventos** — **En clase** (*Calidad del Software*, láminas 19-23): *"componente central que recibe eventos de los publicadores y los distribuye a los suscriptores correspondientes"*, con un modelo de publicación-suscripción. En el diagrama de bloques es el *Event Router*. → [[Ejemplo resuelto - Sistema de Transporte READM]] §10

## C

- **C & C (componentes y conectores)** — La raíz del árbol de estilos que mostró la clase, con cuatro familias: data flow, call-return, event-based y repository. → [[Catálogo de estilos arquitectónicos]]
- **Caja negra / caja blanca** — Ver un componente solo por sus interfaces, o mostrando sus clases o subcomponentes internos. → [[Diagrama de componentes]]
- **Calidad del desarrollo (*developmental quality*)** — Atributo que **no se observa ejecutando** el sistema sino modificándolo: modificabilidad, testabilidad, deployabilidad, integrabilidad. Es la línea del programa "otros atributos de calidad no observables vía ejecución". → [[Atributos de calidad]]
- **Camino** — Conexión entre dos nodos de un diagrama de despliegue: línea llena con el protocolo como estereotipo (`«TCP/IP»`, `«wifi»`). → [[Diagrama de despliegue]]
- **Capa vs tier** — La capa es una partición del código (estructura de módulos); el tier es una partición del despliegue (estructura de asignación). Confundirlos es el error clásico *(complemento, SAIP)*. **En clase se usan como sinónimos** (2 capas = cliente-servidor, three-tier, N-niveles en la nube). → [[Estilos arquitectónicos]] · [[Arquitectura en capas]] §4
- **Cartucho MDA** — En MDA, el paquete que *"contiene las reglas necesarias para realizar una transformación de modelos"* (lectura de Meaurio y Schmieder). → [[Arquitectura dirigida por modelos MDA]] §2
- **Caso de uso (CU)** — Descripción del comportamiento de un sistema en forma de acciones y reacciones, desde el punto de vista del usuario. Propuesto por Ivar Jacobson. → [[Caso de uso]]
- **Caso de uso de apoyo** — CU incluido por **particionamiento** que **no se relaciona con actores**; es la excepción a la regla de "todo CU tiene al menos un actor". → [[Convenios del diagrama de CUN]]
- **Caso de uso del negocio (CUN)** — Secuencia de acciones realizadas en el negocio que producen un resultado de valor observable para ciertos actores del negocio. Representa un proceso de negocio. → [[Caso de uso del negocio]]
- **Catálogo de estilos** — Los estilos agrupados en familias: centrada en datos, flujo de datos, llamada y retorno, peer-to-peer y otras (código móvil, heterogéneos). La clase mostró **dos taxonomías que no coinciden**. → [[Catálogo de estilos arquitectónicos]]
- **Categorías de estructuras** — Las tres en que se agrupan todas las estructuras: **módulos** (unidades de implementación), **componentes y conectores** (tiempo de ejecución) y **asignación** (lo que no es software: CPU, redes, equipos). La lámina *Estructuras* (capturas_U2_F2, 27) llama a la tercera **de localización**. → [[Categorías de estructuras]]
- **Ciclo de influencias en la arquitectura** — Las cuatro influencias (stakeholders, organizaciones de desarrollo, ambiente técnico, experiencia del arquitecto) que moldean la arquitectura y que el sistema resultante retroalimenta. → [[Ciclo de influencias en la arquitectura]]
- **CIM (Computation Independent Model)** — Primer modelo de MDA: *"se centra en los requerimientos y representa el nivel más alto del modelo de negocio. Es un modelo de dominio"*. → [[Arquitectura dirigida por modelos MDA]] §2
- **Circuit Breaker** — Patrón arquitectónico de la lista de clase: deja de llamar a un servicio que falla para no propagar la caída (la definición es complemento). → [[Patrones arquitectónicos]]
- **Clase candidata** — Cada sustantivo del enunciado, en singular y sin repetir, antes de pasarlo por las canastas de descarte. → [[Diagrama de clases]]
- **Clasificación de procesos** — Técnica que separa los procesos del negocio en núcleo, soporte y gerenciales. → [[Identificación de procesos del negocio]]
- **Cliente y proveedor (en una dependencia)** — El cliente es el que depende; el proveedor, el que se depende. La flecha sale del cliente. → [[Relaciones y dependencias en UML]]
- **Cliente-servidor** — **En clase**, miembro de llamada y retorno (capturas_U2_F3, 32): *"Clientes invocan servicios proporcionados por un servidor"* por request/reply; *"el cliente requiere conocer el servidor y el servicio a invocar; los servidores no conocen los clientes"*. También lo dio como 2 capas. → [[Arquitectura de llamada y retorno]] §3 · [[Arquitectura en capas]] §3
- **Componente** — Pieza de software reemplazable que se define por las interfaces que ofrece y requiere; "la personificación en software de una clase" y puede implementar **más de una**. Tres tipos: de distribución, para trabajar en el producto, de ejecución. → [[Diagrama de componentes]]
- **Composición** — Relación es-parte-de con rombo **macizo** en el todo: si muere el todo, mueren las partes. → [[Relaciones y dependencias en UML]]
- **Comprobaciones** — Revisión, en cada etapa, de que los productos del diseño sean claros, correctos, completos y consistentes con los requerimientos y entre sí. → [[Proceso de diseño arquitectónico]]
- **Concern** — El interés que un stakeholder tiene en la entidad de interés: performance, seguridad, mantenibilidad (ISO 42010). → [[Stakeholders]]
- **Conector** — En las estructuras de componentes y conectores, el **vehículo de comunicación** entre los componentes, que son unidades de computación en ejecución. → [[Categorías de estructuras]]
- **Contexto (del diseño)** — Una de las tres entradas del diseño arquitectónico: aspectos del negocio, de la estructura organizacional, tendencias actuales y tecnología disponible. → [[Qué se tiene en cuenta para el diseño]]
- **Core (diagrama)** — El diagrama de CUN de más alto nivel: **una sola elipse** que nombra el negocio o sistema completo, rodeada de todos los actores. → [[Ejemplos resueltos de casos de negocio]]
- **CUN expandidos** — Los CUN con relaciones de inclusión, extensión y generalización-especialización. → [[Caso de uso del negocio]]
- **Curso alterno** — La variante, excepción o desvío del flujo de trabajo, contada en el texto del mismo caso de uso. → [[Descripción textual de casos de uso]]
- **Curso normal de eventos** — El flujo básico de la descripción textual, en **dos columnas** (*acción del actor* / *respuesta del proceso de negocio*) con **una sola numeración** intercalada. → [[Descripción textual de casos de uso]]
- **CWM (Common Warehouse Metamodel)** — Estándar en que se apoya MDA: formato común de intercambio de metadatos en data-warehouse. → [[Arquitectura dirigida por modelos MDA]] §5

## D

- **Dependencia (UML)** — Relación débil de línea **punteada** y punta abierta, del cliente al proveedor: si cambia el proveedor puede haber que cambiar el cliente. → [[Relaciones y dependencias en UML]]
- **Deployability** — Atributo de calidad que mide la capacidad de despliegue; la estructura de despliegue es la clave para lograrlo. → [[Diagrama de despliegue]]
- **Descripción de la arquitectura** — Conjunto de productos que documentan la arquitectura. → [[Arquitectura de software]]
- **Descripción textual (de un CU)** — Documento con nombre, actores, propósito, resumen, flujo de trabajo (básico y alterno), prioridad y mejoras. → [[Descripción textual de casos de uso]]
- **Deuda arquitectónica** — El deterioro acumulado por muchas decisiones pequeñas: la "muerte por mil cortes". → [[Tácticas y patrones arquitectónicos]]
- **DFD (diagrama de flujo de datos)** — Modela la funcionalidad como transformación de flujos de entrada en flujos de salida; puede mostrar descomposición funcional interna. → [[Casos de uso vs DFD]]
- **Diagrama de alto nivel** — Describe la arquitectura con un **alto nivel de abstracción**; suele ser el primer paso antes de un diseño más detallado. → [[Diagrama de bloques de alto nivel]]
- **Diagrama de bloques** — Representación del funcionamiento de un sistema mediante bloques y sus relaciones, con sus entradas y salidas. → [[Diagrama de bloques de alto nivel]]
- **Diagrama de clases** — Diagrama estructural de la parte estática del sistema; se usa en análisis (esquema de BD) y en diseño detallado (código). **No** es el diagrama de la arquitectura. → [[Diagrama de clases]]
- **Diagrama de componentes** — Describe los elementos físicos del software (fuente, binarios, ejecutables, bibliotecas) y sus dependencias a través de interfaces. → [[Diagrama de componentes]]
- **Diagrama de contexto** — Diagrama que fija el límite del sistema: **elipse** = El Producto, **rectángulo** = entidades o agentes, **flecha** = *streamlines*. Un solo óvalo y todas las flechas con nombre. → [[Diagrama de contexto]]
- **Diagrama de despliegue** — Diagrama UML que muestra cómo el software se asigna a los procesadores y las vías de comunicación del hardware. → [[Diagrama de despliegue]]
- **Diagrama de distribución** — El nombre que usa la clase para el **diagrama de despliegue**: es el mismo diagrama. → [[Diagrama de despliegue]]
- **Diagrama de Kiviat** — Diagrama radar de cinco ejes (features, quality, cost, schedule, staff) usado como "diagrama de flexibilidad" del proyecto. La lámina no define la escala: leído como flexibilidad, un valor alto es un eje más negociable (interpretación). → [[Equilibrio de restricciones del proyecto]]
- **Diagrama de secuencia** — Diagrama de comportamiento que muestra la interacción de objetos a lo largo del tiempo, con mensajes en orden. → [[Diagrama de secuencia]]
- **Diagramas estructurales / de comportamiento (UML)** — Los estructurales muestran lo **estático** (componentes, despliegue, clases, paquetes); los de comportamiento lo **dinámico** (actividad, secuencia, casos de uso). → [[Diagramas UML estructurales y de comportamiento]]
- **Diseño arquitectónico** — Se refiere a la arquitectura de **un sistema concreto**. Es una actividad continua y previa al diseño detallado. → [[Estilos arquitectónicos]]
- **Diseño detallado** — Etapa posterior al diseño de la arquitectura, que modela el detalle de cada pieza (por ejemplo con diagramas de clases). → [[Arquitectura en el ciclo de vida del software]]
- **Dispositivo (`«device»`)** — Nodo que representa **hardware** capaz de ejecutar artefactos. → [[Diagrama de despliegue]]
- **Documento de diseño arquitectónico** — Producto del diseño; se alimenta de requisitos, contexto y experiencia del arquitecto, y suele incluir varias vistas. → [[Qué se tiene en cuenta para el diseño]]
- **Driver arquitectónico** — *(de clase)* Los **factores críticos que guían el diseño** de un sistema; determinan su **estructura fundamental** y actúan como **puente entre los requerimientos del negocio y la implementación técnica**. Hay tres tipos: RF, de calidad y de restricción. → [[Drivers arquitectónicos]]
- **Driver de restricción** — *(de clase)* **Condición impuesta externamente que limita las decisiones arquitectónicas.** Seis categorías: tecnológicas, regulatorias/legales, de negocio/presupuesto, organizacionales, ambientales/físicas y de integración. → [[Drivers arquitectónicos]]
- **Driver RF** — *(de clase)* **Funcionalidad específica que moldea la estructura del sistema.** Se redacta `RFn - Nombre corto: enunciado` y se modela con casos de uso expandidos. → [[Drivers arquitectónicos]]
- **Drivers de calidad** — *(de clase)* Los que **definen cómo debe comportarse el sistema**. Son **siete**: rendimiento, escalabilidad, disponibilidad, seguridad, mantenibilidad, usabilidad y fiabilidad — y todos llevan un **número**. → [[Drivers arquitectónicos]]
- **DTO / DAO** — Patrones arquitectónicos de la lista de clase: un objeto que transporta datos entre capas, y un objeto que encapsula el acceso a la base de datos (las definiciones son complemento). → [[Patrones arquitectónicos]]

## E

- **EAC (escenario de atributo de calidad)** — El identificador `EAC-nn` de los drivers de calidad en el ejemplo de clase. Tabla de cuatro columnas: ID, Categoría, Escenario (fuente de estímulo, estímulo, artefacto, entorno, respuesta, medida de la respuesta) y Prioridad como par, por ejemplo (A, A). Es lo que la rúbrica llama «EaC». → [[Ejemplo resuelto - Sistema de Transporte READM]] §5
- **EDA (Event Driven Architecture)** — Estilo 7 de la lista de nueve de la clase: la arquitectura basada en eventos. Está nombrada, pero no se desarrolló. → [[Estilos arquitectónicos]] · [[Catálogo de estilos arquitectónicos]]
- **Elementos, Forma y Razón** — La afirmación con que la clase define la **arquitectura** (no el estilo): elementos de procesamiento, datos y conexión; la forma, que son sus propiedades y relaciones; y la razón, que es la motivación de la elección. → [[Estilos arquitectónicos]]
- **Empaquetado / desempaquetado** — En RPC, convertir los parámetros o el resultado en bytes para cruzar la red y reconstruirlos del otro lado (pasos del diagrama de la captura 43 de U2_F3). → [[Llamada a procedimiento remoto]]
- **Entorno de ejecución (`«executionEnvironment»`)** — Nodo que representa **software** capaz de ejecutar artefactos (JRE, máquina virtual); siempre va dentro de un dispositivo. → [[Diagrama de despliegue]]
- **ESB (Enterprise Service Bus, bus empresarial)** — Intermediario al que se conectan clientes y proveedores de servicios en lugar de invocarse directamente (capturas_U2_F3, 34 y 39). → [[Arquitectura orientada a servicios]] §8
- **Escenario de atributo de calidad** — La especificación de un requisito de calidad en seis partes: fuente, estímulo, artefacto, entorno, respuesta y **medida**. → [[Atributos de calidad]]
- **Escenarios (vista de)** — La vista "+1" del modelo 4+1: los casos de uso que amarran las otras cuatro vistas y dan trazabilidad. → [[Modelo 4+1 vistas]]
- **Estereotipo** — Extensión de UML que define un tipo especializado; se escribe entre `«»` y se aplica tanto a clases como a **relaciones**. En el modelo de CUN los dos estereotipos base son *actor del negocio* y *caso de uso del negocio*. → [[Relaciones y dependencias en UML]], [[Modelo de casos de uso del negocio]]
- **Estilo arquitectónico** — **En clase hay dos definiciones, sin que ella elija**: *"establece las restricciones sobre la arquitectura de una familia de diseños arquitectónicos"* (capturas_U2 21) y *"establece un marco de referencia a partir del cual es posible construir aplicaciones que comparten un conjunto de atributos y características"* (capturas_U2_F2 6). También lo define como una **transformación impuesta** al diseño de todo un sistema, que se compone de uno o más patrones arquitectónicos. En Reynoso (complemento) conjuga componentes, conectores, configuraciones y restricciones. → [[Estilos arquitectónicos]]
- **Estructura arquitectónica** — El conjunto de elementos en sí, tal como existen en el software o el hardware. Se representa mediante vistas. → [[Estructuras y vistas arquitectónicas]]
- **Estructura de despliegue** — Muestra cómo el software se asigna a los elementos de procesamiento y comunicación del hardware; permite razonar sobre rendimiento, integridad, seguridad y disponibilidad. → [[Diagrama de despliegue]]
- **Estructuras de asignación** — Las que mapean software sobre lo que NO es software: despliegue, implementación y asignación de trabajo. → [[Diagrama de despliegue]]
- **Estructuras de localización** — El nombre que la lámina *Estructuras* da a las de **asignación**: relación entre los elementos de software y los ambientes externos donde el software es creado o ejecutado. → [[Categorías de estructuras]]
- **Etapas del método de diseño** — Las **ocho** de la Figura 2-8, en cuatro fases: requerimientos (drivers, alcance), diseño/refinamiento, experimentación (decisión, experimentar) y producción (planear, implementar). → [[Método de diseño centrado en la arquitectura]]
- **Extend (relación de extensión)** — Relación que agrega a un CU base una conducta opcional u optativa, que no siempre ocurre. → [[Relación de extensión extend]]
- **Extremo cliente / extremo servidor** — En el diagrama de RPC de clase, las piezas que empaquetan, envían, reciben y desempaquetan, y ocultan la red al cliente y al servidor (fuera de clase: *stub* y *skeleton*). → [[Llamada a procedimiento remoto]]

## F

- **Filtro** — Componente de tuberías y filtros. **En clase**: *"no necesariamente realizan únicamente tareas de filtrado sino que ejecutan formas variables de transformación"*, y no necesita conocer el funcionamiento de los filtros vecinos (capturas_U2_F3, 19). → [[Tuberías y filtros]]
- **Forma icónica / expandida (interfaces)** — La interfaz dibujada como símbolo (círculo o semicírculo) o como caja `«interface»` con sus operaciones. → [[Interfaces de componentes]]
- **Fragmento combinado (alt/opt/break/loop)** — Marco con condición en un diagrama de secuencia: alterna, hace opcional, corta o repite parte del flujo. → [[Diagrama de secuencia]]
- **FrontEnd / BackEnd** — Agrupación que atraviesa los nodos del despliegue: lo que usa el usuario frente a lo que procesa y guarda. → [[Ejemplo resuelto - Parque de atracciones]]
- **Función** — Grupo funcional que responde a un objetivo de la organización y que puede involucrar a varias áreas. Agrupa varios procesos de negocio; no es un CUN. → [[Identificación de procesos del negocio]]
- **FURPS** — Taxonomía de calidad de la Tabla 1 de la NT1: **F**uncionalidad, facilidad de uso (*usability*), confiabilidad (*reliability*), rendimiento (*performance*) y capacidad de soporte (*supportability*). Es **otra** clasificación de clase, distinta de los seis del programa. → [[Atributos de calidad]]

## G
- **Generalización entre actores** — El actor **padre** se queda con el CUN **compartido** y cada **hijo** con el suyo. Ejemplo de clase: *Cliente* despacha medicamentos; solo Consulta Externa asigna citas y solo Hospitalización asigna camas. → [[Ejemplos resueltos de casos de negocio]]

- **Generalización-especialización** — Relación que muestra workflows que comparten estructura, propósito y comportamiento: un CU padre y uno o más CU hijos. → [[Generalización y especialización en casos de uso]]
- **Gold plating** — Funcionalidad construida que ningún requisito pidió; la detecta la trazabilidad hacia atrás. → [[Matriz de trazabilidad de requisitos]]
- **Grano grueso / grano fino** — Los elementos arquitectónicos son de grano grueso y los de diseño de grano fino; hay que conservar la traza entre ambos para que la arquitectura gobierne el resto del proceso. → [[Arquitectura de software en el modelo en espiral]] §2

## I
- **IaaS / PaaS / SaaS** — Modelos de nube: infraestructura (el dispositivo), plataforma (el entorno de ejecución), software listo para usar (el artefacto). → [[Diagrama de despliegue]]
- **Importancia y urgencia (de un CU)** — Dos campos de escala **cerrada** de la plantilla textual: importancia {vital, importante, quedaría bien} y urgencia {inmediatamente, hay presión, puede esperar}. → [[Descripción textual de casos de uso]]

- **Importar / exportar (paquetes)** — `«import»` es una dependencia punteada del paquete que usa al usado, y solo da acceso a lo **público** (lo exportado). → [[Diagrama de paquetes]]
- **Inception** — Primera fase de RUP: se define la **visión**, el **caso de negocio** y el **alcance**; los requisitos de alto nivel suelen estar incompletos, así que hay que **asumir supuestos** y refinarlos después. → [[Arquitectura y proceso de desarrollo]]
- **Include (relación de inclusión)** — Relación en que el comportamiento de un CU se inserta explícitamente dentro del CU base; siempre ocurre. → [[Relación de inclusión include]]
- **Inclusión por particionamiento** — `«include»` usado por **un solo** CU base, para partir un flujo largo. El incluido suele ser un **CU de apoyo sin actores**. La clase la marca **PARTICIONAR**. → [[Convenios del diagrama de CUN]]
- **Inclusión por reutilización** — `«include»` usado por **dos o más** CU base que comparten comportamiento. La clase la marca **REUTILIZAR**. → [[Convenios del diagrama de CUN]]
- **Infraestructura de software** — Frameworks y clases utilitarias compartidas (logging, wrappers de COTS, arranque/apagado); debe empezar antes del diseño de subsistemas, aunque sus requisitos salgan del propio desarrollo. → [[Arquitectura y proceso de desarrollo]]
- **Integridad conceptual** — *"La clave para el diseño de sistemas con éxito"*: la tiene *"un pequeño número de mentes llegando juntos a diseñar la arquitectura"*. Es la meta de la interacción del arquitecto con el dominio y la planeación. → [[Arquitectura de software en el modelo en espiral]] §2
- **Interfaz provista (proporcionada)** — Servicio que un componente **ofrece**; se dibuja como círculo (*lollipop*). → [[Interfaces de componentes]]
- **Interfaz requerida** — Servicio que un componente **necesita** de otro; se dibuja como semicírculo (*socket*). → [[Interfaces de componentes]]
- **Invariantes del estilo** — Las restricciones de interconexión o composición entre componentes que un estilo impone, y que lo identifican. → [[Estilos arquitectónicos]]
- **Invocación implícita** — Estilo basado en eventos: el emisor anuncia un evento y la infraestructura decide a quién le llega; los suscriptores se invocan implícitamente. → [[Estilos arquitectónicos]]
- **ISM (Implementation Specific Model)** — Último modelo de MDA: el código, que *"se realiza automáticamente a partir de cada PSM"*. → [[Arquitectura dirigida por modelos MDA]] §2
- **ISO 9126** — Norma de calidad de producto con seis características: funcionalidad, fiabilidad, usabilidad, eficiencia, mantenibilidad y portabilidad. Es la lista del programa. → [[Atributos de calidad]]
- **ISO/IEC 25010** — Sucesora de ISO 9126; asciende la seguridad y la compatibilidad a características de primer nivel, llegando a ocho. → [[Atributos de calidad]]
- **Iteración controlada** — En proyectos grandes la iteración es inevitable (requisitos incompletos, cambios, ciclo de vida largo); “la única decisión es tomar el control de las iteraciones o no”. → [[Arquitectura y proceso de desarrollo]]

## L

- **Layer bridging** — Usar una capa no adyacente, violando la restricción del estilo en capas; en exceso destruye la portabilidad que justificaba el estilo. → [[Estilos arquitectónicos]]
- **Llamada a procedimiento remoto (RPC)** — **Patrón arquitectónico** de llamada y retorno, basado en cliente-servidor: *"extender a los sistemas distribuidos el mecanismo de llamadas a procedimientos y subrutinas"* (capturas_U2_F3, 41). Parámetros **por valor** y **serializables**, porque los procedimientos corren en espacios de memoria diferentes (43). → [[Llamada a procedimiento remoto]]
- **Llamada y retorno** — **En clase**: *"Interacción por invocación síncrona de capacidades proporcionadas por los componentes"* (capturas_U2_F3, 30); el que invoca *"permanece en estado de bloqueo"* hasta que el servicio termina (31). Miembros: cliente-servidor, capas, SOA; sus patrones arquitectónicos: RPC, orientado a objetos y MVC (40). → [[Arquitectura de llamada y retorno]] · [[Catálogo de estilos arquitectónicos]]

## M

- **MAC (medicamento de alto costo)** — Medicamento cuyo valor mensual por paciente supera los Q. 50,000; el objeto del sistema FarmaHosp. → [[Plan - Caso 1 FarmaHosp]]
- **Matriz de dependencias** — Matriz cuadrada de requisito contra requisito: las **columnas (X)** son los que **originan** la dependencia y las **filas (Y)** los que **dependen**. Se lee "fila depende de columna" y sirve para analizar el impacto de los cambios. Es la plantilla oficial del Caso 1. → [[Guía - Matrices de trazabilidad]]
- **Matriz de trazabilidad (RTM)** — Tabla que cruza cada requisito con su origen, su diseño, su código y sus pruebas. → [[Matriz de trazabilidad de requisitos]]
- **MDA (Model Driven Architecture)** — Propuesta de la OMG: construir software como transformación sucesiva de modelos en UML, de CIM y PIM a PSM y a código. → [[Arquitectura dirigida por modelos MDA]]
- **Mensaje síncrono / asíncrono** — El síncrono bloquea al emisor hasta la respuesta (cabeza llena, respuesta punteada); el asíncrono no espera (cabeza abierta). → [[Diagrama de secuencia]]
- **Microkernel / plug-in** — Forma del estilo jerárquico: un núcleo con mecanismos mínimos y plug-ins que aportan la funcionalidad por interfaces fijas. → [[Estilos arquitectónicos]]
- **Modelo 4+1 vistas** — Las vistas lógica, de procesos, de despliegue/desarrollo y física, más la de escenarios. Según la clase las identifica el **RUP**, y existen porque la arquitectura la usan **distintos grupos de personas en distintos momentos**. → [[Modelo 4+1 vistas]]
- **Modelo activo** — En MVC, el modelo que *"notificará a las vistas los cambios que en los datos pueda producir un agente externo"* (capturas_U2_F3, 45), sin pasar por el controlador. → [[Modelo-Vista-Controlador]]
- **Modelo de casos de uso del negocio** — Modelo que describe los procesos de un negocio y cómo se benefician e interactúan socios y clientes en esos procesos. → [[Modelo de casos de uso del negocio]]
- **Modelo de referencia** — **En clase**: *"una división de funcionalidad junto con el flujo de datos entre las piezas"*; *"un estándar de descomposición de un problema conocido"*. No es una arquitectura. → [[Arquitectura de referencia]]
- **Modelo en espiral** — Modelo evolutivo e iterativo de Boehm (1986), guiado por el **análisis de riesgo**. El avance angular es el progreso y el desplazamiento radial, el coste acumulado. Cuatro actividades: objetivos y alternativas, análisis de riesgo, ingeniería, planificación. → [[Arquitectura de software en el modelo en espiral]] §1
- **Modelo-Vista-Controlador (MVC)** — **Patrón arquitectónico** (título de capturas_U2_F3, 44-48) que *"separa los datos de una aplicación, la interfaz de usuario, y la lógica de control en tres componentes distintos"*. El modelo tiene datos, reglas de negocio y persistencia; la vista muestra; el controlador recibe los eventos de entrada. Cae en llamada y retorno. → [[Modelo-Vista-Controlador]]
- **Modelos semánticos (de un estilo)** — La parte de un estilo que permite entender las propiedades generales del sistema analizando las propiedades conocidas de sus partes. → [[Estilos arquitectónicos]]
- **Moderación cautelosa** — La postura del libro frente a ágil: se produce menos documentación, pero incluso un equipo ágil grande necesita un número razonable de vistas. → [[Arquitectura y proceso de desarrollo]]
- **MOF (Meta Object Facility)** — Estándar de la OMG con el que *"puede definirse cualquier lenguaje de modelado incluyendo UML"*; provee un repositorio de modelos y metamodelos. → [[Arquitectura dirigida por modelos MDA]] §5
- **Muerte por mil cortes** — El deterioro de una arquitectura por la acción bienintencionada de quienes la modifican. → [[Tácticas y patrones arquitectónicos]]
- **Multiplicidad** — Cuántas instancias de una clase participan en un extremo de la asociación (1, 0..1, *, 1..*). → [[Diagrama de clases]]

## N
- **N-niveles en la nube** — Tiers web, de negocio y de datos, cada uno detrás de un balanceador, en una red virtual con DMZ y bastion. → [[Arquitectura en la nube]]
- **Navegabilidad** — En el diagrama de CUN, **quién inicia** la comunicación: flecha al CUN = inicia el actor; flecha al actor = inicia el CUN; **sin saetas** = los dos sentidos. **No** son flujos de datos. → [[Convenios del diagrama de CUN]]

- **Necesidad oculta** — Lo que el stakeholder realmente necesita, distinto de lo que dice querer; es donde está el requisito medible. En el Caso 1 es una columna explícita de la tabla de stakeholders. → [[Guía - Identificación de stakeholders]]
- **No-riesgo** — Una decisión que sí satisface un escenario; documentarla es evidencia. → [[Evaluación de la arquitectura]]
- **Nodo (UML)** — Un equipo, servidor o dispositivo en un diagrama de despliegue; se dibuja como caja 3D y puede contener otros nodos. Dos clases: **dispositivo** (hardware) y **entorno de ejecución** (software). → [[Diagrama de despliegue]]
- **NRFs (requerimientos no funcionales)** — Rendimiento, seguridad, disponibilidad, modificabilidad y similares; el arquitecto es responsable de integrarlos en el sistema. → [[Arquitecto de software]]
- **NT (nota técnica)** — Los documentos que reparte la catedrática además de las diapositivas: `NT Identificación de CDU de Negocio` y `NT1. Trazabilidad de Requerimientos`. Son **material de clase**, no complemento. → [[Programa oficial del curso]]
- **Núcleo, soporte y gerenciales** — Los tres tipos de procesos de negocio en la técnica de clasificación. → [[Identificación de procesos del negocio]]

## O

- **Orquestación / coreografía** — Los motores que, según la clase, hacen que SOA sea *event-based* (capturas_U2_F3, 34). Orquestación: un coordinador central; coreografía: cada servicio reacciona a los otros (definición: complemento). → [[Arquitectura orientada a servicios]]

## P

- **PALM** — Taller que elicita las metas de negocio como escenarios de siete partes y les asocia atributos de calidad. → [[Stakeholders]]
- **Paquete** — Agrupa elementos del modelo para organizarlo y controlar el acceso. Puede contener clases, interfaces, componentes, nodos, colaboraciones, casos de uso, diagramas y otros paquetes. → [[Diagrama de paquetes]]
- **Paso 0 (caso de negocio)** — La creación del caso de negocio, que la clase marca **fuera** de las ocho etapas: no es una etapa del método, es lo que existe **antes** de que arranque. → [[Método de diseño centrado en la arquitectura]]
- **Patrón arquitectónico** — **En clase**: *"solución general a un problema común del diseño arquitectónico"*, de **menor alcance que un estilo**, pero de **gran impacto sobre el componente**: rige cómo trabaja o se comunica con otros, y cambiarlo afecta a los componentes relacionados. Dio 13 ejemplos (DTO, DAO, API Gateway, Circuit Breaker…). En el SAIP (complemento) **empaqueta tácticas**. → [[Patrones arquitectónicos]] · [[Tácticas y patrones arquitectónicos]]
- **Patrón de diseño** — Solución a un problema de diseño con efectividad comprobada y reutilizable en contextos diferentes. Su impacto es **relativo**: quitarlo solo afecta a las clases relacionadas. La clase dio una lista de 25. → [[Patrones de diseño]]
- **Patrones creacionales / estructurales / de comportamiento** — Las tres familias de patrones de diseño: cómo se **crean** los objetos, cómo se **relacionan** las clases, y cómo se asignan **responsabilidades** y se comunican los objetos. → [[Patrones de diseño]]
- **Perspectiva de la arquitectura** — Representación desde una perspectiva específica de un determinado sistema o de una parte del mismo. → [[Arquitectura de software]]
- **PIM (Platform Independent Model)** — Modelo de MDA de alto nivel, *"independiente de cualquier tecnología o plataforma"*. Equivale casi por entero a la fase de análisis; en él se hacen los cambios. → [[Arquitectura dirigida por modelos MDA]] §2
- **Pipeline** — La arquitectura completa de filtros conectados por pipes (conectores que transmiten los datos de un filtro al siguiente). → [[Tuberías y filtros]]
- **Pirámide invertida de re-uso** — Como describe la clase el modelo en capas: cada capa agrega responsabilidad y abstracción a la capa directamente sobre ella (capturas_U2_F3, 10). → [[Arquitectura en capas]] §6
- **Pizarra (blackboard)** — Variante activa del estilo centrado en datos: el almacén notifica a los agentes suscritos (repositorio + invocación implícita). **En clase** el catálogo textual la pone en *centrada en datos*, y el árbol C&C la cuelga de **Repository y Event-based a la vez**. → [[Catálogo de estilos arquitectónicos]] · [[Estilos arquitectónicos]]
- **Plantilla obligatoria (matriz)** — La **Fig. 1, página 91** de la NT1 de trazabilidad: matriz de dependencias requisitos X vs. requisitos Y. No es sugerida, es la que hay que usar. → [[Guía - Matrices de trazabilidad]]
- **Post-RS (trazabilidad)** — Enlaza el requisito con lo que se construyó: diseño, código y pruebas. → [[Matriz de trazabilidad de requisitos]]
- **Pre-RS (trazabilidad)** — Enlaza el requisito con su origen: stakeholders, reglas de negocio, documentos previos. → [[Matriz de trazabilidad de requisitos]]
- **Precede (estereotipo `«precede»`)** — Estereotipo de **precedencia temporal** que usa la clase entre las cinco etapas del ciclo de definición (requerimientos → diseño → documentación → evaluación → implementación). No confundir con `«include»` ni `«extend»`. → [[Proceso de diseño arquitectónico]]
- **Primera descomposición** — **Un solo** diagrama de CUN que abre la única elipse del *core* en N procesos, conservando **el mismo juego de actores**. → [[Guía - Caso de negocio]]
- **Prioridad y mejoras** — Dos campos de cierre de la descripción textual: la prioridad (un valor simple, p. ej. *Alta*) y las oportunidades de mejora detectadas en el proceso. → [[Descripción textual de casos de uso]]
- **Proceso de negocio** — Grupo de tareas lógicamente relacionadas, en cierta secuencia y manera, que emplean recursos de la organización para dar resultados en apoyo a sus objetivos. → [[Proceso de negocio]]
- **PSM (Platform Specific Model)** — Modelo de MDA que *"describe el sistema de acuerdo con una tecnología de implementación determinada"*. Se genera del PIM por transformación. → [[Arquitectura dirigida por modelos MDA]] §2
- **Puerto** — Punto del borde de un componente que agrupa interfaces relacionadas; habitual en caja blanca. → [[Diagrama de componentes]]
- **Punto de extensión** — Lugar que el caso de uso **base declara** y que el caso extendido es el único autorizado a alterar. Es lo que hace a `«extend»` "más controlada" que la generalización. → [[Relación de extensión extend]]
- **Punto de sensibilidad** — Decisión con efecto marcado sobre una respuesta de un atributo de calidad. → [[Evaluación de la arquitectura]]
- **Punto de tradeoff** — Decisión a la que dos o más respuestas son sensibles, una mejorando y otra empeorando (ej.: la frecuencia del heartbeat). → [[Evaluación de la arquitectura]]
- **Punto de vista arquitectónico** — Plantilla que describe la forma de crear y utilizar una perspectiva de la arquitectura. → [[Arquitectura de software]]
- **Punto focal (de la comunicación)** — Sin él una buena arquitectura no emerge: los equipos reinventan infraestructura, usan estándares distintos y persiguen metas locales. → [[Arquitectura y proceso de desarrollo]]

## Q

- **QAW (Quality Attribute Workshop)** — Método facilitado de siete pasos para generar, priorizar y refinar escenarios de calidad con los stakeholders. → [[Guía - Drivers de calidad y restricción]]

## R

- **Rationale** — La justificación de las decisiones arquitectónicas, ligándolas a los concerns de los stakeholders (ISO 42010). → [[El ciclo del architecting]]
- **Realización** — El elemento (clase o componente) implementa una interfaz. En UML 2.x: punteada con triángulo hueco. **Ojo**: en sus diagramas de clases (capturas_U2 26-28, 54, 56) ella la dibuja con **línea llena rotulada «Realización»**. → [[Relaciones y dependencias en UML]]
- **Realizaciones de CUN** — Muestran cómo colaboran los trabajadores y entidades de negocio para ejecutar el proceso; se documentan con diagramas de actividad, clases y secuencia, y descripción textual. → [[Realizaciones de casos de uso del negocio]]
- **Repositorio** — Variante pasiva del estilo centrado en datos: los accesores tienen la iniciativa y el esquema de datos es el contrato común. → [[Estilos arquitectónicos]]
- **Requerimientos significativos arquitectónicamente** — *"Aquellos que tienen un impacto esencial sobre la arquitectura"* (lectura de Meaurio y Schmieder). Es la misma idea que los drivers arquitectónicos de clase. → [[Arquitectura de software en el modelo en espiral]] §2 · [[Drivers arquitectónicos]]
- **Requisito huérfano** — Requisito sin diseño o sin caso de prueba asociado; hueco de cobertura. → [[Matriz de trazabilidad de requisitos]]
- **Requisitos en conflicto** — Dos requisitos están en conflicto "si no pueden implementarse juntos, es decir, si la solución a un requisito **impide** la implementación de otro" (NT1). Es el tradeoff visto desde los requisitos. → [[Matriz de trazabilidad de requisitos]]
- **REST** — Estilo 8 de la lista de nueve de la clase. La única diapositiva es la de *API RESTful* (capturas_U2_F3, 20), puesta **dentro de la serie de flujo de datos**: *"interfaz que dos sistemas de computación utilizan para intercambiar información de manera segura a través de Internet"*. → [[Tuberías y filtros]] §4
- **Rol (asociación)** — Nombre del papel que juega una clase en un extremo de una asociación. → [[Diagrama de clases]]
- **RUP** — *Rational Unified Process*: fases (inception, elaboration, construction, transition) y flujos de trabajo donde el arquitecto tiene un rol definido en cada uno. Según la clase, es el que **identifica las 4+1 vistas de arquitectura**. → [[Arquitectura y proceso de desarrollo]] · [[Modelo 4+1 vistas]]

## S

- **SCADA** — Sistema de supervisión, control y adquisición de datos para procesos industriales en tiempo real; ejemplo de clase de diagrama de bloques. → [[Diagrama de bloques de alto nivel]]
- **Scrum** — Proceso ágil iterativo; el libro relata un proyecto tipo Scrum de ~250 desarrolladores que arrancó **sin arquitecto** y tuvo que nombrar uno tarde. → [[Arquitectura y proceso de desarrollo]]
- **Serializable** — *"Convertible en una corriente de bytes"*: condición para que un parámetro de RPC viaje por la red (capturas_U2_F3, 43). → [[Llamada a procedimiento remoto]]
- **Síncrono** — **En clase**: *"Proceso o su efecto que se desarrolla en perfecta correspondencia temporal con otro proceso o causa"* (capturas_U2_F3, 30). Es lo que define a llamada y retorno. → [[Arquitectura de llamada y retorno]] · ver **Mensaje síncrono / asíncrono**
- **Sistema** — Conjunto de componentes que cumplen una función o un conjunto de funciones específicas. → [[Arquitectura de software]]
- **Stakeholder** — Individuo, equipo u organización con un interés en la entidad de interés (ISO 42010). Todo actor es stakeholder; no todo stakeholder es actor. → [[Stakeholders]]
- **Stakeholders** — Participantes del proyecto; cada uno le exige al sistema atributos distintos y a menudo incompatibles. → [[Beneficios de la arquitectura de software]]
- **Straw man (diseño)** — Empezar el diseño en cuanto exista cualquier descripción del sistema, marcándolo **claramente como preliminar**, para tener algo concreto que criticar. → [[Arquitectura y proceso de desarrollo]]
- **Streamline** — El **flujo de información** entre el producto y una entidad externa en el diagrama de contexto. Se dibuja como flecha y **siempre lleva nombre**, en sustantivo. → [[Diagrama de contexto]]
- **Súper-táctica** — Táctica tan fundamental que reaparece en casi todos los patrones: encapsular, restringir dependencias, usar un intermediario, abstraer servicios comunes. → [[Tácticas y patrones arquitectónicos]]

## T

- **Táctica arquitectónica** — Decisión de diseño que influye en el logro de **una** respuesta de **un** atributo de calidad. → [[Tácticas y patrones arquitectónicos]]
- **Thin client / rich client** — Los dos extremos de la capa de presentación en una figura de clase (capturas_U2_F3, 6). La clase no los define; complemento: el thin deja el procesamiento en el servidor, el rich ejecuta parte de la lógica. → [[Arquitectura en capas]] §7
- **Trabajador del negocio** — Quien ejecuta el proceso desde *adentro* del negocio; aparece en las realizaciones de CUN y **no** es un actor. → [[Realizaciones de casos de uso del negocio]]
- **Tradeoff (de atributos)** — Ningún atributo de calidad se logra en aislamiento: lograr uno afecta a los otros, y casi todos afectan negativamente a la performance. → [[Atributos de calidad]]
- **Traslape funcional** — La misma función implementada en varios sistemas; SOA pide determinarlo junto con el potencial reúso (capturas_U2_F3, 36). → [[Arquitectura orientada a servicios]] §5
- **Trazabilidad bidireccional** — Hacia adelante y hacia atrás a la vez; la única completa y la que exigen los estándares. → [[Matriz de trazabilidad de requisitos]]
- **Trazabilidad de requisitos** — Capacidad de describir y seguir la vida de un requisito en ambas direcciones, desde su origen hasta su despliegue (Gotel y Finkelstein). → [[Matriz de trazabilidad de requisitos]]
- **Triángulo del proyecto** — Las tres restricciones alcance / costo / tiempo: se pueden fijar dos, la tercera queda como consecuencia. → [[Equilibrio de restricciones del proyecto]]
- **Tubería y filtro (tuberías y filtros, pipes and filters)** — **En clase** (capturas_U2_F3, 18): *"una tubería (pipeline) es una arquitectura que conecta componentes computacionales (filtros) a través de los conectores (pipes) y las comunicaciones se ejecutan como un flujo"*. Estilo de la familia flujo de datos. → [[Tuberías y filtros]]

## U

- **Utility tree** — Árbol que organiza los escenarios de calidad por atributo, con su importancia de negocio y su riesgo técnico. → [[Evaluación de la arquitectura]]

## V

- **Vía de comunicación** — La línea simple que une dos nodos en un diagrama de despliegue; lleva el protocolo como estereotipo y admite multiplicidad. → [[Diagrama de despliegue]]
- **Vista arquitectónica** — Representación de un conjunto coherente de elementos arquitectónicos, escrita y leída por las partes interesadas. Es la representación de una estructura. → [[Estructuras y vistas arquitectónicas]]
- **Vista de despliegue (o de desarrollo)** — Muestra cómo está dividido el software en componentes y las dependencias entre ellos. Diagramas de componentes y de paquetes. → [[Modelo 4+1 vistas]]
- **Vista de procesos** — Muestra los flujos de trabajo paso a paso y varios requisitos no funcionales. Diagrama de actividad. → [[Modelo 4+1 vistas]]
- **Vista física** — Muestra cómo se distribuyen los componentes entre los equipos que conforman la solución. Diagrama de deployment. → [[Modelo 4+1 vistas]]
- **Vista lógica** — Muestra los requisitos funcionales: el dominio de la aplicación, las clases y objetos del *core*. Diagramas de clases y de paquetes. → [[Modelo 4+1 vistas]]
- **VoI (value of information)** — Técnica para decidir cuánto conviene gastar en experimentar antes de tomar una decisión arquitectónica. → [[El ciclo del architecting]]

## X

- **XMI (XML Metadata Interchange)** — Estándar que permite pasar un modelo UML a XML para que otras aplicaciones lo procesen. → [[Arquitectura dirigida por modelos MDA]] §5
