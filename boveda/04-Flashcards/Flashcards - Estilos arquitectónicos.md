---
tema: Arquitectura de software
fuente: "Presentación de clase — capturas_U2 (21, 43-47, 49-52). NÚCLEO (tarjetas finales). + COMPLEMENTO — Reynoso + SAIP 4ª ed. + Guía de estudio (tarjetas iniciales)"
fecha: 2026-09-15
---

# Flashcards — Estilos arquitectónicos (punto 1.9)

Compatible con el plugin **Spaced Repetition** de Obsidian: cada tarjeta es una línea con la
pregunta, el separador de dos signos de dos puntos, y la respuesta.

> [!warning] Dos bloques: complemento primero, clase al final
> Las tarjetas iniciales salen de la **Parte II (complemento)** de [[Estilos arquitectónicos]]:
> Reynoso, SAIP y guía de estudio. Las del bloque **"Lo que dio la clase"**, al final, salen de las
> capturas de la unidad 2 y de [[Arquitectura monolítica]], [[Arquitectura en capas]] y
> [[Arquitectura en la nube]]. **Si chocan, manda la clase.**

#flashcards/estilos

¿Qué es un estilo arquitectónico según Reynoso?::Un **concepto descriptivo** que define una forma de articulación u organización arquitectónica. El conjunto de los estilos cataloga las formas básicas posibles de estructuras de software; las complejas se articulan por **composición**.

¿Cuáles son los cuatro ingredientes con que se describe un estilo?::**Componentes** (elementos), **conectores**, **configuraciones** y **restricciones**.

¿Por qué el concepto de estilo va más allá de lo que cubre UML?::Porque pone los **conectores** como elemento de primera clase, y el modelado orientado a objetos y UML no los cubren satisfactoriamente. De ahí la existencia de los ADLs.

¿Cuántos estilos arquitectónicos hay y cuántos patrones de diseño?::Estilos: **seis o siete clases** fundamentales y unos **veinte ejemplares** como máximo. Patrones de diseño: **centenares**.

¿Por qué "ningún sistema real es de un solo estilo"?::Porque las arquitecturas complejas resultan del **agregado o la composición** de estilos más básicos. Ejemplo: microservicios (cliente-servidor) + bus de eventos (invocación implícita) + capas internas + contenedor (VM) + base de datos (centrado en datos) + pipeline de despliegue (batch secuencial).

¿Cuáles son los componentes y conectores del estilo **tubería y filtro**?::Componentes: **filtros** que transforman un flujo de forma **incremental** (empiezan a producir antes de terminar de consumir), más fuente y sumidero. Conectores: **tuberías**, flujos unidireccionales que preservan el orden y no transforman nada.

¿Cuál es la restricción clave de tubería y filtro?::Los filtros **no comparten estado ni conocen la identidad de sus vecinos**; toda la comunicación pasa por las tuberías. La corrección no debe depender del orden en que procesan.

¿Qué favorece y qué sacrifica tubería y filtro?::Favorece modificabilidad, reutilización, **paralelismo** y testabilidad. Sacrifica **interactividad**, estado compartido, latencia por etapa y el manejo de errores.

¿Qué es el **batch secuencial** y en qué se diferencia de tubería y filtro?::Es el caso **degenerado**: cada etapa espera a que la anterior termine del todo y pasa **archivos completos**, sin concurrencia. Es el estilo de los procesos nocturnos de mainframe y de un pipeline de despliegue.

¿Cuál es la diferencia entre **repositorio** y **pizarra**?::Quién tiene la **iniciativa**. En el repositorio la tienen los accesores (el almacén es pasivo); en la pizarra el propio almacén **notifica** a los agentes suscritos. La pizarra es repositorio + invocación implícita.

¿Cuál es la restricción del estilo centrado en datos?::Los accesores solo interactúan **a través del almacén**, nunca directamente entre sí. El **esquema de datos es el contrato** compartido por todos.

¿Qué sacrifica el estilo centrado en datos?::Performance y disponibilidad (el almacén es **cuello de botella y punto único de falla**), **acoplamiento oculto** por el esquema —cambiarlo impacta a todos los accesores— y dificultad de distribución.

¿Cuál es la restricción que **define** el estilo en capas?::La relación "tiene permitido usar" debe ser **unidireccional y estrictamente ordenada**: nunca usos hacia arriba, y normalmente solo la capa inmediata inferior.

¿Cómo se llama usar una capa no adyacente?::***Layer bridging***. En exceso destruye las metas de portabilidad que justificaban el estilo.

¿Qué favorece y qué sacrifica el estilo en capas?::Favorece modificabilidad, **portabilidad** (la capa baja aísla el SO o la red) y testabilidad de abajo hacia arriba. Sacrifica **performance**: una llamada del tope puede atravesar muchas capas.

¿Cuál es la diferencia entre una **capa** y un **tier**?::La capa es una partición del **código**: vive en la estructura de **módulos** (estática). El tier es una partición del **despliegue**: vive en la estructura de **asignación**. Se pueden tener tres capas en un solo tier.

¿En qué se diferencian **capas** y **microkernel**, siendo los dos jerárquicos?::En capas la jerarquía es de **abstracción** (cada nivel oculta el de abajo); en microkernel es de **extensión** (el centro es mínimo y la funcionalidad se enchufa por interfaces fijas).

¿Qué sacrifica el estilo **microkernel / plug-in**?::**Seguridad y privacidad**: como los plug-ins pueden venir de terceros, es más fácil introducir vulnerabilidades.

¿Cuál es el rasgo definitorio de la **invocación implícita**?::El componente que emite **no invoca a nadie directamente**: anuncia un evento y la infraestructura decide a quién le llega. De ahí que la invocación de los suscriptores sea implícita.

¿Qué se gana y qué se pierde con publish-subscribe?::Se gana modificabilidad máxima e integrabilidad: agregar un suscriptor es registrarse en un evento, **cero cambios en el publicador**. Se pierde **determinismo y trazabilidad**: nadie sabe cuánto tarda el mensaje ni en qué orden se invocan los suscriptores.

¿Cuáles son las restricciones de **cliente-servidor**?::La comunicación la **inicia siempre el cliente**; los clientes **no se comunican entre sí**. Si el servidor guarda estado del cliente, cada petición debe identificarlo y hace falta fin de sesión o timeout.

¿Qué distingue **microservicios** de **SOA** según el SAIP?::SOA: servicios **heterogéneos y de organizaciones distintas**, reutilizables y con SLA. Microservicios: **un solo sistema de una sola organización**, equipos pequeños, dependencias acíclicas y **solo comunicación por mensajes** (sin enlace directo, sin leer el almacén de otro, sin memoria compartida).

¿Qué es **peer-to-peer** y qué sacrifica?::Estilo simétrico donde cada par actúa como cliente y servidor, sin coordinador central y con churn. Favorece escalabilidad sin centro y resiliencia; sacrifica consistencia, seguridad y administrabilidad.

¿Cuáles son los cuatro elementos del estilo **intérprete / máquina virtual**?::El **motor de interpretación**, la **representación del programa** (bytecode o AST), el **estado del programa** y el **estado del propio intérprete**.

¿Se puede decir que un estilo es mejor que otro?::No. Cada estilo **canjea** un atributo de calidad por otro. Elegir estilo es elegir **qué sacrificar**, y eso solo se decide contra requerimientos concretos.

¿Qué significa "instanciar" una arquitectura de referencia?::Realizar una **customización**: agregar o quitar elementos de la estructura que la arquitectura de referencia define. Ejemplo del SAIP: agregar un componente de integración de pagos junto a los tiers de presentación, negocio y datos.

*(sin fuente en el material)* ¿Qué es una **arquitectura candidata**?::La primera versión de la arquitectura, todavía **no validada**, que se somete a evaluación y de la que puede haber varias en competencia. **Este término no está en el material local ni apareció en las capturas de la unidad 2: confirmar con ella.**

## Lo que dio la clase (NÚCLEO — capturas_U2)

¿Qué es un **diseño arquitectónico** según la clase?::Se refiere a la arquitectura de **un sistema concreto**.

¿Qué es un **estilo arquitectónico** según la clase?::Establece las **restricciones** sobre la arquitectura de una **familia de diseños arquitectónicos**. Ejemplos: centrado en datos, flujo de datos, llamar y regresar, capas.

¿Qué es un **patrón arquitectónico** según la clase, y cómo se compara su alcance con el del estilo?::Una **solución general a un problema común** del diseño arquitectónico. Tiene **menor alcance** que los estilos arquitectónicos.

¿Cuál es la principal característica de la **arquitectura monolítica**?::**Agrupar toda la funcionalidad y servicios de la aplicación en una base de código única.**

¿Cómo describe la tabla de clase la escalabilidad, el despliegue y el acoplamiento del monolito?::Escalabilidad: **escalado vertical, toda la aplicación a la vez**. Despliegue: **requiere desplegar toda la aplicación**. Acoplamiento: **fuerte entre componentes**.

¿Cuáles son las siete filas de la tabla de la arquitectura monolítica?::Estructura, comunicación, escalabilidad, despliegue, mantenibilidad, tecnología y acoplamiento.

¿Cómo define la clase la arquitectura **N-Capas**?::Arquitecturas **multinivel o programación por capas** donde **a cada nivel se le confía una misión simple**, lo que permite diseñar **arquitecturas escalables** (que se amplían con facilidad si las necesidades aumentan).

¿A qué llama la clase **arquitectura de 2 capas**?::Al **modelo cliente-servidor**: el cliente hace la **petición [1]** y el servidor devuelve la **respuesta [2]**.

¿Qué enseña el ejemplo smartphone/smartwatch?::Que **cliente y servidor son roles, no máquinas**: el smartphone es cliente del servidor físico [1-2] y después **cambia de rol** y es servidor del smartwatch [3-4].

¿Qué muestra el diagrama de componentes de la clínica veterinaria?::Un diseño en **cuatro capas** como paquetes: 1 Presentación (interfaz usuarios y administrador), 2 Lógica de negocio (facturas, animales, empleados, avisos, workflow, gestor documental), 3 BBDD y 4 Servicios.

¿Cómo define la clase la **arquitectura de la nube**?::Se compone de los **componentes y subcomponentes que se encuentran en una nube**; hay **mucho más que solo tecnología**: se refiere al **diseño** y conecta todos los componentes y tecnologías necesarios para la computación en la nube.

¿Cuáles son las zonas del diagrama **N-niveles en la nube** de Azure?::**DMZ** (NVA), **Web tier**, **Business tier** y **Data tier** (SQL Server primario y secundario), cada una detrás de un **load balancer**, dentro de una **virtual network**, más un **Bastion** para DevOps.

¿La clase distingue entre **capa** y **nivel (tier)**?::**No**: los usa como sinónimos (N-Capas = multinivel, 2 capas = cliente-servidor, N-niveles = tiers). El complemento sí los distingue: capa = partición del código, tier = partición del despliegue.
¿Qué dos tipos de patrón distingue la diapositiva "Patrones / Estilos Arquitectónicos"?::Patrones de diseño y patrones arquitectónicos; después vienen los estilos arquitectónicos. En su dibujo, los de diseño (Singleton, Composite, Factory Method) son subcomponentes dentro de un componente.
