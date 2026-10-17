---
tema: Preguntas pendientes
fuente: "Dudas acumuladas al procesar el material de clase. Cada una cita su captura o su nota."
fecha: 2026-09-17
alias: [preguntas, dudas, preguntas para la catedrática, preguntas pendientes]
---

# Preguntas pendientes para clase

Lo que **no se puede resolver con el material** y hay que preguntarle a la catedrática o al auxiliar.
Regla de la bóveda: si el material es ambiguo, **no se asume en silencio** — se anota acá y, si hay
que entregar igual, se declara la asunción en el entregable.

**Cómo usar este archivo:** llevá las de prioridad alta a la próxima clase. Cuando una se responda,
moverla a *Resueltas* con la fecha y **actualizar la nota que la origina**.

---

## Prioridad alta — afectan qué se estudia o cómo se dibuja en el examen

| # | Pregunta | Por qué importa | Dónde está la evidencia |
|---|---|---|---|
| 1 | **¿Qué entra en el segundo parcial (19/09)?** ¿El material nuevo de "cómo se modela" y estilos, o Calidad del Software (unidad 2 del programa)? | Las capturas nuevas cubren **1.4, 1.5, 1.7 y 1.9**; de **Calidad del Software no hay ninguna presentación**. Si entra Calidad, se estudia solo con complemento | `Programa oficial del curso` · [[Atributos de calidad]] |
| 2 | **La realización de interfaz, ¿se dibuja con línea llena rotulada o punteada con triángulo hueco?** | Sus diagramas de clases usan **línea llena rotulada "Realización"**; su lámina de UML 2.x usa la **punteada con triángulo**. Las dos son de clase | capturas_U2 26-28, 54, 56 vs. 32 · [[Relaciones y dependencias en UML]] |
| 3 | **Dentro de un nodo, ¿van artefactos o componentes?** | El PDF *Tema 5* pone **artefactos** con `«manifest»`; sus capturas ponen **componentes** dentro del nodo | capturas_U2 57-58 vs. PDF págs. 5-6 · [[Diagrama de despliegue]] |
| 4 | **¿Exige las reglas de notación del PDF *Tema 5*** (camelCase, tipos en atributos, `<<Interface>>`) **aunque sus propios ejemplos no las sigan?** | Su diagrama del parque usa mayúscula inicial, sin tipos y `<<Interfaz>>` | capturas_U2 56 vs. PDF pág. 3 · [[Diagrama de clases]] |
| 5 | **En el 4+1, ¿qué nomenclatura quiere?** ¿"Vista de Despliegue" = componentes (unidad 1) o *Implementation / Deployment View* (figura nueva)? | Con el nombre cruzado, una respuesta correcta puede leerse como incorrecta | capturas_U2 2 y 37 · [[Modelo 4+1 vistas]] |
| 23 | **¿Qué definición de estilo arquitectónico espera en el examen?** A: *"establece las restricciones sobre la arquitectura de una familia de diseños arquitectónicos"*. B: *"establece un marco de referencia a partir del cual es posible construir aplicaciones que comparten un conjunto de atributos y características"* | Las dos son de clase y ella no elige. Mientras tanto: citar la A y agregar la B como complemento de la idea | capturas_U2 21 = U2_F2 14 vs. U2_F2 6 · [[Estilos arquitectónicos]] §1 |
| 24 | **¿Qué taxonomía de estilos usa?** Sus dos diapositivas "Catálogo de Estilos" no coinciden: la de texto pone **peer-to-peer como familia**, con eventos y servicios adentro; el árbol C&C pone **Event-based como familia**, y peer to peer y SOA cuelgan de **Call-return**. Además, SOA y pizarra tienen dos padres | Una pregunta del tipo *"¿a qué familia pertenece SOA?"* tiene dos respuestas de clase. **Evidencia nueva (2026-09-17):** para desarrollar usa el **árbol C&C** como portada de cada familia (U2_F3 13, 29-30), y titula siete láminas *"call return: SOA"* con la 34 diciendo *"Es event-based porque…"*. Para SOA la balanza queda 2 a 1 a favor del árbol; P2P y eventos siguen abiertos | capturas_U2_F2 30 vs. 30-componentes-conectores · U2_F3 13, 29-30, 33-39 · [[Catálogo de estilos arquitectónicos]] §4 |

---

## Prioridad media — contenido que puede caer

| # | Pregunta | Contexto |
|---|---|---|
| 47 | **Las tres notas técnicas de la unidad 3** (NT1 MDA y espiral, NT2 arquitectura de la información, NT3 arquitectura ágil), ¿**entran en el tercer parcial (17/10)**? ¿Y qué más de la unidad 3? ¿Entra también **Calidad del Software** (ISO 9126, escenarios), que llegó el 16/10 en la carpeta `capturas_U3_F1`? | Que la de MDA la repartió ella **ya se sabe**: es la NT1 (ver Resueltas). Siguen sin presentación de clase SCRUM como proceso, documentación, implementación y pruebas | `00-Fuentes/lecturas/` y `presentaciones/` · [[Arquitectura dirigida por modelos MDA]] · [[Arquitectura de la información]] · [[Arquitectura ágil]] |
| 48 | **Las cuatro actividades del modelo en espiral**: la lectura da dos listas (con *evaluación del cliente* en la introducción y con *determinación de objetivos y alternativas* en el apartado III). ¿Cuál espera? | Lectura asumida: la del apartado III, que es la desarrollada y dibujada | [[Arquitectura de software en el modelo en espiral]] §1 |
| 49 | **RSA y drivers, ¿son lo mismo para ella?** La NT1 habla de *requerimientos significativos arquitectónicamente*, la NT3 de *RSA*, y la clase de *drivers arquitectónicos*. ¿Se pueden usar como sinónimos en una respuesta? | Lectura tomada: sí, un RSA es un driver visto desde los requisitos (los dos incluyen funcionales). Prioridad baja | [[Requisitos significativos para la arquitectura]] §2 · [[Drivers arquitectónicos]] |
| 51 | **Usabilidad en ISO 9126: aprendizaje y comprensión** tienen en la lámina la **misma descripción** (*"esfuerzo de los usuarios para reconocer el concepto lógico y sus aplicaciones"*). ¿Cuál es la de aprendizaje? | Lectura tomada: es copia y pega. La descripción vale para comprensión; aprendizaje es el esfuerzo para aprender a usar la aplicación (complemento). Prioridad baja | capturas_U3_F1 10 · [[Norma ISO 9126]] §4.3 |
| 52 | **La tabla titulada «Atributos de Calidad NO observables vía ejecución»** lista disponibilidad, confidencialidad, funcionalidad, desempeño, confiabilidad, *safety* y *security*: los cuatro primeros son **la rama de observables** del árbol. ¿El título está invertido? | Si preguntan *"nombre atributos no observables"* hay dos respuestas de clase. Lectura tomada: el título está mal; se contesta con el árbol (interoperabilidad, portabilidad, escalabilidad, mantenibilidad) | capturas_U3_F1 17 vs. 22 · [[Atributos observables y no observables vía ejecución]] §3 |
| 53 | **Escalabilidad como no observable**: el árbol de Bass la pone en *no observables*, pero la lámina de drivers de calidad la mide corriendo (*10.000 peticiones*). Y la **usabilidad** no aparece en el árbol. ¿Cómo la quiere clasificada? | Lectura tomada: en una pregunta sobre esta clasificación, se responde con el árbol y se declara | capturas_U3_F1 22 · [[Drivers arquitectónicos]] §4 · [[Atributos observables y no observables vía ejecución]] §2 |
| 54 | **Las medidas de sus escenarios no llevan número** (*"Inmediata"*, *"probado en diferentes dispositivos"*, *"en el menor tiempo posible"*). ¿Acepta medidas cualitativas, o vale la regla de drivers de *"sin número es un deseo"* que siguen los `EAC` de READM? | Cambia cómo se escribe un EAC en el examen. Lectura tomada: **poner número siempre**; cumple las dos versiones | capturas_U3_F1 23-24 vs. READM lámina 11 · [[Escenarios de calidad]] §6 |
| 50 | **¿Qué significa «CCV»** en los títulos de la NT1 y la NT2 (*Arquitectura del SW y CCV*, *La Arquitectura de la Información en el CCV*)? | Lectura tomada: **ciclo de vida**, porque la unidad 3 se llama *Arquitectura en el Ciclo de Vida* y los dos artículos tratan del ciclo de desarrollo. Prioridad baja | [[Arquitectura de la información]] · [[Arquitectura de software en el modelo en espiral]] |
| 6 | ¿Va a dar **arquitectura basada en eventos** y **on premise**? *(Candidata y de referencia ya se dieron: ver Resueltas.)* Eventos (EDA) está **nombrada** en tres diapositivas pero no se desarrolló; on premise sigue sin ninguna | capturas_U2_F2 9, 30, 30-cc · [[Estilos arquitectónicos]] §3 |
| 7 | Los estilos que **solo nombró** (centrada en datos, microkernel, microservicios, P2P), ¿se evalúan? *(Flujo de datos, llamada y retorno y SOA ya se desarrollaron: ver Resueltas. **REST** tiene una sola diapositiva, ver la 31.)* | La lista de 9 (capturas_U2_F2 9) nombra microkernel, microservicios y P2P sin ninguna diapositiva que los desarrolle |
| 8 | ¿Espera que se distinga **capa** (lógica) de **nivel/tier** (físico), o se usan como sinónimos? | En clase se usan como sinónimos: "2 capas" = cliente-servidor, "N-niveles en la nube" |
| 9 | ¿Hay que **leer o escribir** sintaxis de ADL (Acme), o alcanza con la definición? | [[Lenguajes de descripción de arquitectura]] |
| 10 | ¿Los **paquetes** se evalúan dentro del 1.7 o como diagrama aparte? | capturas_U2 39-41 · [[Diagrama de paquetes]] |
| 11 | El título dice **"2.- Diagrama de Distribución"**: ¿el "1." es el de componentes? ¿Cuál es la serie completa? | capturas_U2 22 y 34 |
| 12 | ¿Los ejemplos de control industrial (**SCADA**, PlantPAx) se evalúan en detalle o solo ilustran qué es un diagrama de bloques? | capturas_U2 14-17 · [[Diagrama de bloques de alto nivel]] |
| 13 | ¿Adopta las convenciones **no estándar** del PDF para secuencia (flechas azules de *Forward*, rojas en `break`, condiciones sin corchetes)? | PDF *Tema 5* págs. 7-8 · [[Diagrama de secuencia]] |
| 14 | La **importación de paquetes**, ¿se evalúa como UML 1.x (no transitiva) o UML 2.x (`«import»` público reexporta, `«access»` no)? | [[Diagrama de paquetes]] §3 |
| 15 | La **dependencia**, ¿incluye el uso por **atributo** (PDF) o solo el uso **temporal** (su tabla de la vista lógica)? | capturas_U2 25 vs. PDF pág. 4 |
| 25 | ¿Cómo define **arquitectura candidata**? La diapositiva se titula *"Definición de una arquitectura candidata"* pero solo muestra la tabla conceptual / modular / código / ejecución, sin ninguna frase de definición | capturas_U2_F2 25 · [[Arquitectura de referencia]] §4 — por ahora se define con el flujo de Ambler (unidad 1) |
| 26 | **La tercera categoría de estructuras, ¿"asignación" o "de localización"?** Mismo concepto con dos nombres en dos láminas suyas (y la segunda dice *"Componentes-y-Conector"*) | captura del 19/08 vs. capturas_U2_F2 27 · [[Categorías de estructuras]]. Mientras tanto: *"asignación (o de localización)"* |
| 27 | **¿El diagrama de paquetes va en la vista lógica, en la de desarrollo o en las dos?** Sus diapositivas del 4+1 lo ponen en las dos; el PDF *Tema 5*, solo en la de desarrollo | capturas_U2_F2 11-12 vs. PDF pág. 1 · [[Modelo 4+1 vistas]] |
| 30 | **Tuberías y filtros, ¿estilo o patrón?** La 21 dice *"Este **estilo** se podría usar cuando"*; la 26 se titula *"Un ejemplo de uso del **patrón** Filtros y Tuberías"* | Mientras tanto: **estilo** de la familia flujo de datos (lo dicen la 21, el catálogo textual y el árbol C&C); la 26 usa "patrón" porque su figura viene de la literatura de patrones · capturas_U2_F3 21 vs. 26 · [[Tuberías y filtros]] |
| 31 | **¿REST entra en flujo de datos?** La única diapositiva de *API RESTful* está bajo el subtítulo *"–arquitectura centrada en el flujo de datos–"*; el catálogo textual pone *basadas en Recursos* bajo peer-to-peer y la lista de 9 lo trae como estilo propio | Tres ubicaciones de clase para lo mismo · capturas_U2_F3 20 · [[Tuberías y filtros]] §4 |
| 32 | **En tuberías y filtros, ¿los datos pasan completos o por partes?** La 27 pone como desventaja *"los datos se transmiten de forma completa"* y como ventajas, juntas, *"Fuerza un procesamiento secuencial"* y *"Ejecución concurrente"*. El complemento dice "incremental" | ¿La transmisión completa describe tuberías y filtros o el secuencial por lotes (28)? · capturas_U2_F3 27-28 · [[Tuberías y filtros]] §8 |
| 33 | **En capas, ¿dónde va el servidor web?** La 2: *"El primer nivel consiste en la capa de presentación que incluye el navegador y el servidor web"*; la 6: *Capa 1 Navegador · Capa 2 Servidor Web*; la 10 separa *Capa Cliente* de *Capa Web/Servicios* | Si pide dibujar capas, cambia el corte · capturas_U2_F3 2, 6, 10 · [[Arquitectura en capas]] §7 |
| 34 | **¿Las capas son estrictas o relajadas?** La 10 dice *"Una capa solamente tiene relación con la siguiente"* y, en la misma lámina, *"la mayoría de la interacción ocurre solamente entre capas vecinas"* | ¿Se permite saltarse una capa? · capturas_U2_F3 10 · [[Arquitectura en capas]] §10 |
| 35 | **RPC, orientado a objetos y MVC, ¿estilos o patrones arquitectónicos?** El catálogo textual los lista como *"Arquitecturas de llamada y retorno (…)"*; la U2_F3 40 los llama *"Patrones Arquitéctónicos [sic] para arquitectura de llamada y retorno"*, 41-42 y 44-48 dicen *"Patrón Arquitectónico"*, pero la 44 abre con *"Un estilo de arquitectura de software que utilice MVC…"* | Mientras tanto: **patrón arquitectónico** (lo dice la mayoría y encaja con estilo ⊃ patrón). Prioridad baja · capturas_U2_F2 30 vs. U2_F3 40-44 · [[Modelo-Vista-Controlador]] §5 · [[Llamada a procedimiento remoto]] §6 |
| 36 | **En MVC, ¿la base de datos es parte del Modelo?** La 44 le da al modelo *"sus mecanismos de persistencia"* y el recuadro del Modelo en la 48 encierra la Oracle Database; la 45 dice *"Lo ideal es que el modelo sea independiente del sistema de almacenamiento"* | Lectura tomada: la persistencia es del modelo; el almacenamiento, algo que el modelo usa · capturas_U2_F3 44, 45, 48 · [[Modelo-Vista-Controlador]] |
| 37 | **Los dos ejercicios de la captura 12** (partida multijugador; tienda online en o por capas), ¿se entregan o se evalúan? El 1 no nombra estilo; el 2 dice *"en o por capas"* | Si caen en el parcial, hay que practicarlos · capturas_U2_F3 12 · [[Arquitectura en capas]] §12 |

---

## Sobre láminas concretas — posibles erratas

| # | Pregunta | Qué se ve |
|---|---|---|
| 16 | **Captura 51 (Prime Video)**: ¿el diagrama es el **monolito** o la arquitectura **distribuida previa**? | Se titula "Monolítica en AWS", pero muestra Step Functions, Lambdas y buckets intermedios — que es lo que Amazon **abandonó** al pasar al monolito |
| 17 | **Captura 49 (clínica veterinaria)**: ¿las flechas de BBDD y Servicios hacia Lógica de negocio apuntan así a propósito? | Según la convención de dependencia, diría que **la base usa la lógica** |
| 18 | **Captura 55 (CDU del parque)**: el actor lleva la **barra diagonal de negocio** en una lámina rotulada "CDU EXPANDIDOS", y *Gestión Ficha Montaña Rusa* y *Generar Alerta* **no tienen actor** | Choca con el convenio "un CU sin actor es un error" y mezcla planos |
| 19 | **Captura 56 (clases del parque)**: ¿por qué eliminó la clase **CRA** del PDF y la reemplazó por **Averías** más dos interfaces? ¿Es el criterio que espera al pasar de clases a componentes? | También renombra *Torniquete* a *Molinete* y `-NúmSerieVagón()` es un atributo con paréntesis |
| 20 | **Captura 31**: ¿cuál de los dos dibujos es la forma **icónica** y cuál la **expandida**? ¿Qué significa el estereotipo `«Annotation»`? | La diapositiva no los rotula |
| 21 | **Captura 58**: ¿*Gestión de Atracciones* es FrontEnd o BackEnd? | La zona naranja casi no la cubre |
| 28 | **capturas_U2_F2 1 (árbol de patrones)**: *SOA*, *Comunicación* y *Cloud* están en cajas naranjas **sin línea** que las una a la rama de patrones arquitectónicos. ¿Son más categorías o se refieren a otra cosa? | Solo Integración, Seguridad y Web están conectadas. **Evidencia nueva:** la U2_F3 38 dice *"El estilo de arquitectura SOA"*, así que la caja SOA probablemente agrupa patrones de ese estilo | [[Patrones arquitectónicos]] §3 |
| 29 | **capturas_U2_F2 36 (Kiviat)**: ¿un valor alto significa **más flexible** o **más prioritario**? | La lámina no define la escala; la nota lo lee como flexibilidad, y eso es interpretación |
| 38 | **capturas_U2_F3 34 (SOA)**: en los dos diagramas, **una** de las respuestas es punteada y el resto llenas. ¿La punteada es la respuesta asíncrona? | La lámina no lo explica; la nota lo deja como lectura propia · [[Arquitectura orientada a servicios]] §3 |
| 39 | **capturas_U2_F3 26 (Secure Pipes and Filters)**: Role1 tiene *Right i (op1, op2)* y op3 es de *Right j*/Role2, pero en el `sd Sistema` es `:Role1` quien pide `op3` y termina ejecutándose. ¿La decisión no debería ser denegar? | [[Tuberías y filtros]] §7 |
| 40 | **capturas_U2_F3 5 (Apache/MySQL)**: el paso 4 va del PHP en ejecución hacia el ícono de Python en la carpeta privado, y no dice qué se pide | Prioridad baja · [[Arquitectura en capas]] §3 |

---

## Del Caso 1 (FarmaHosp), sigue abierta

| # | Pregunta | Estado |
|---|---|---|
| 22 | ¿Qué espera con *"priorizar los 5 drivers más críticos según el **contexto guatemalteco**"*? | **No hay material de clase** sobre cómo priorizar, y "contexto guatemalteco" no está definido en ninguna fuente. Se entregó con un criterio declarado; conviene validarlo |

---

## Del Caso Harley-Davidson (entrega 13/10)

| # | Pregunta | Por qué importa | Dónde está la evidencia |
|---|---|---|---|
| 43 | **¿Cuáles son «los pasos para definir la arquitectura»** del criterio 6: los 4 pasos, los 7 de la lámina *"Pasos para la definición de una Arquitectura de software"* o las 8 etapas del método centrado en la arquitectura? | Hay tres listas de clase. Lectura asumida: **los 7**, por el título | [[Proceso de diseño arquitectónico]] · [[Método de diseño centrado en la arquitectura]] |
| 46 | **«Diagrama de Distribución» y «Diagrama de Despliegue», ¿son dos diagramas?** En *Calidad del Software* hay una lámina con cada título: la de distribución reparte capas en nodos; la de despliegue baja al componente y rotula el protocolo | En las capturas anteriores decía *Diagrama de Distribución* por el de despliegue. Lectura asumida: es el mismo diagrama a dos niveles de detalle | láminas 17-18 · [[Ejemplo resuelto - Sistema de Transporte READM]] §9 · [[Diagrama de despliegue]] |
| 45 | **«Traer el caso al presente»**: ¿se actualiza solo la tecnología, o también los hechos del caso (cifras, organización, normativa vigente)? | El caso es de 1998-1999 y no trae ni hardware ni números de calidad. Lectura asumida: se actualiza la tecnología, los hechos no se tocan, y lo agregado va como supuesto declarado | instrucciones del caso · [[Plan - Caso Harley-Davidson]] §5 |

---

## Resueltas

Al responder una, moverla acá con la fecha y actualizar la nota que la originó.

| Era | Pregunta | Respuesta | Cómo se resolvió |
|---|---|---|---|
| 47 (en parte) | ¿La lectura de MDA y el modelo en espiral la repartió ella? | **Sí: es la NT1 de la unidad 3**, *Arquitectura del SW y CCV*. Mismo texto que el PDF del 12/10 (99,6 % igual). Pasa de *lectura* a **nota técnica de clase** | Llegó como nota técnica el 2026-10-16 · [[Arquitectura dirigida por modelos MDA]] · [[Arquitectura de software en el modelo en espiral]] |
| 44 | Trabajo sin grupo: ¿habilita la entrega la presentación individual? ¿cómo se nombra el archivo? | **Dejó de aplicar: se entrega como Grupo 2**, con cuatro integrantes; el archivo es `Grupo2_CasoHD.pdf` | Decisión del estudiante, 2026-10-13 |
| 41 | ¿Qué significa «EaC» en *"Incorporar los drivers atributos de calidad en el software (mediante Eac)"*? | **Escenarios de atributos de calidad.** La tabla de drivers de calidad del ejemplo READM usa el id `EAC-nn`, con el escenario en seis partes y la prioridad como par | Con material de clase, presentación *Calidad del Software* lámina 11, el 2026-10-12 · [[Ejemplo resuelto - Sistema de Transporte READM]] §5 |
| 42 | ¿Qué modelo de calidad espera? | **El pensamiento ISO como familia de normas, con normas concretas como la 9126 o la serie 25000.** Qué significa *determinarlo* no lo precisó: se entregó como árbol característica, subcaracterística, métrica y umbral | Respuesta de la catedrática, transmitida por el estudiante el 2026-10-12. **Desde el 2026-10-16 **sí hay láminas**: ISO 9126 y la familia 25000 son de clase → [[Norma ISO 9126]] · [[Familia de normas ISO 25000]] |
| 6 (en parte) | ¿Va a dar arquitectura **basada en eventos**? | **Sí, con un ejemplo:** diagrama de bloques *Arquitectura basada en Eventos* y el bus de eventos como componente publicador/suscriptor | Con material de clase, *Calidad del Software* láminas 14 y 19-23, el 2026-10-12 · [[Ejemplo resuelto - Sistema de Transporte READM]] §8 y §10 |
| 6 (en parte) | ¿Va a dar arquitectura **candidata** y **de referencia**? | **Sí, se dieron.** Referencia: *"un modelo de referencia mapeado en elementos de software…"*; candidata: la tabla de cuatro tipos | Con material de clase, capturas_U2_F2 23-26, el 2026-09-16 · [[Arquitectura de referencia]] |
| 7 (en parte) | ¿"Llamada y retorno" **incluye** capas? | **Sí.** *"Arquitecturas de llamada y retorno (llamadas a procedimientos remotos, Modelo Vista Controlador –MVC–, en Capas, Orientadas a Objetos, basadas en Componentes)"*. En el árbol C&C, client-server y multi-tier también cuelgan de call-return | Con material de clase, capturas_U2_F2 30 y 30-cc, el 2026-09-16 · [[Catálogo de estilos arquitectónicos]] |
| 7 (en parte) | ¿Va a desarrollar **flujo de datos**, **llamada y retorno** y **SOA**, o solo los nombra? | **Los desarrolló.** Flujo de datos con tuberías y filtros y secuencial por lotes; llamada y retorno con cliente-servidor, RPC y MVC; SOA con siete láminas | Con material de clase, capturas_U2_F3 13-48, el 2026-09-17 · [[Arquitectura centrada en el flujo de datos]] · [[Arquitectura de llamada y retorno]] · [[Arquitectura orientada a servicios]] |
