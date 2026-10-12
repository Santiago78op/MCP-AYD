---
tema: Plan de tarea
fuente: "Instrucciones y rúbrica de la catedrática (2026-10-12) + caso HBS 606-S14. Ver enunciados/Caso Harley-Davidson.md"
fecha: 2026-10-12
tarea: Caso Harley-Davidson
alias: [Harley, Harley-Davidson, SiLK, SiL'K, CasoHD, caso HD, plan harley]
---

# Plan — Caso Harley-Davidson (proyecto SiL'K)

Aplicación del **paso 1** de [[_Método para resolver una tarea]]: el enunciado desarmado en
entregables, anclado a la teoría de clase, con lo que el material **no cubre** y las decisiones que
hay que tomar antes de escribir una sola línea del entregable.

> [!note] Estado al 2026-10-13: entrega armada
> El entregable está en [[Entrega - Caso Harley-Davidson]] y el estado en
> [[Avance - Caso Harley-Davidson]]. Este archivo queda como el **estudio del enunciado**. Dos de los
> tres huecos del §3 se cerraron después de escribirlo: «EaC» con el material de clase
> ([[Ejemplo resuelto - Sistema de Transporte READM]]) y «modelo de calidad» con la respuesta de la
> catedrática (familia ISO: 9126 y serie 25000).

> [!note] El nombre de la carpeta
> El PDF llegó en `enunciados/Tarea 2/`, pero ya existe una *Tarea 2* (la continuación de FarmaHosp,
> entregada el 18/09). Para no confundirlas, todo lo de este caso se llama **Caso Harley-Davidson**.

---

## 1. Los entregables

| # | Criterio (textual) | Pts | Qué hay que producir | Material |
|---|---|---|---|---|
| 1 | *"Habilidad para identificar el caso de negocio (Diagrama de Constexto, CDU Core y CDU 1era. Descomposición)"* | 15 | tres diagramas en notación de negocio | [[Guía - Caso de negocio]] · [[Ejemplos resueltos de casos de negocio]] |
| 2 | *"Identificación de Stakeholders caso Harley-Davidson"* | 10 | tabla de stakeholders con id | [[Guía - Identificación de stakeholders]] |
| 3 | *"Completitud de drivers RF, Atributos de Calidad y Restricción del caso Harley-Davidson"* | 20 | CDU expandidos · escenarios con número · restricciones por categoría | [[Drivers arquitectónicos]] · [[Guía - Drivers de calidad y restricción]] |
| 4 | *"Acoplamiento de Matrices de trazabilidad a los criterios 1,2 y 3"* — **cuatro** matrices | 15 | STK×Req · Req×CDU · STK×CDU · Req×Req | [[Guía - Matrices de trazabilidad]] · [[Matriz de trazabilidad de requisitos]] |
| 5 | *"Identificación de los estilos arquitectónicos en función de los criterios anteriores. Diagrama de Despliegue de Arquitectura"* | 20 | estilo(s) justificado(s) + despliegue | [[Guía - Selección del estilo arquitectónico]] · [[Diagrama de despliegue]] |
| 6 | *"Adaptación de los drivers Atributos de Calidad y los de Restricción a los pasos para definir la arquitectura de software que se necesita y determinación del modelo de calidad."* | 20 | **nuevo** — ver §3 | [[Proceso de diseño arquitectónico]] · [[Método de diseño centrado en la arquitectura]] · [[Atributos de calidad]] (complemento) |

**Restricciones de forma**: archivo `GrupoN_CasoHD.pdf` · entrega el martes 13 de octubre · una
**presentación en grupo** en la clase de ese día es *"requisito para habilitar la entrega final"*.

**La consigna transversal**: *"Traer el caso al presente y trabajarlo con los métodos y tecnologías
actuales."* El caso es de 1998-1999. Afecta a los criterios 3, 5 y 6.

## 2. Qué cambió respecto de FarmaHosp

| | Tarea 2 FarmaHosp | Caso Harley-Davidson |
|---|---|---|
| Caso | nuevo desde cero: **no se reutiliza nada** | — |
| Matrices | tres | **cuatro**: se suma *Requerimientos vrs. Requerimientos* (la matriz cuadrada de dependencias; es justo la plantilla de la NT1, fig. 1) |
| Diagrama de bloques | pedido (30 pts con despliegue) | **no se pide**: solo despliegue |
| Estilo | *"estilo y justificación"* (10) | *"los estilos"*, en plural, *"en función de los criterios anteriores"* — pide trazarlos a los drivers |
| Criterio 6 | bloques y despliegue | **pasos para definir la arquitectura + modelo de calidad** |
| Datos de hardware | el enunciado los daba (SAN, vCPU, sitio alterno) | **el caso no da ninguno** |
| Números de calidad | 8 acuerdos de calidad escritos | **ninguno** sobre el comportamiento del sistema |

## 3. Lo que el material de clase no cubre

Son tres huecos, y los tres caen en los **20 puntos del criterio 6** y en el numeral 4.

| Hueco | Qué hay en la bóveda | Qué falta |
|---|---|---|
| **«EaC»** — *"Incorporar los drivers atributos de calidad en el software (mediante Eac)"* | **cero menciones** de la sigla en toda la bóveda. Lo más cercano es el **escenario de atributo de calidad** de seis partes ([[Atributos de calidad]] §7), que es complemento del SAIP | saber qué expande la sigla. La lectura más probable es *Escenarios de atributos de Calidad*; no está confirmada |
| **«modelo de calidad»** | la unidad 2 (Calidad del Software) **no tiene presentación de clase**. El programa lista los seis de ISO 9126; la nota los desarrolla como complemento | cuál modelo espera, y qué es *"determinarlo"*: ¿elegir una norma?, ¿armar el árbol característica → subcaracterística → métrica para SiL'K? |
| **«los pasos para definir la arquitectura»** | hay **tres** listas de clase: los **4 pasos** (datos → estructura → alternativas → método), los **7** de la lámina *"Pasos para la definición de una Arquitectura de software"* y las **8 etapas** del método centrado en la arquitectura | cuál de las tres. La de 7 es la que lleva ese título casi literal |

> [!important] Mientras no haya respuesta
> Regla de la bóveda: se **asume y se declara**. Las lecturas por defecto están en §6. Las tres
> preguntas quedaron anotadas como 41, 42 y 43 en [[Preguntas pendientes para clase]].

## 4. Lo que el caso regala, criterio por criterio

Los hechos y las páginas están en la ficha del enunciado (`enunciado("Caso Harley-Davidson")`).

| Criterio | De dónde sale | Lo que hay |
|---|---|---|
| 1 — caso de negocio | anexos 6a y 6b | la cadena de nueve actividades con **seis dentro del ámbito**, y las **tres fases** (transacciones · información sobre suministradores · seguimiento de proyectos) |
| 2 — stakeholders | anexo 4 y págs. 3, 4, 8, 9, 10, 12 | promotores, comité de dirección, equipo, los grupos (PUG, ITC, AI), los 16 proveedores estratégicos, las áreas encuestadas, los 2.000 que generan solicitudes |
| 3 — drivers RF | anexo 10 y anexo 6b | los diez criterios funcionales de la especificación y las doce actividades de las tres fases |
| 3 — calidad | anexo 10 y pág. 6 | el caso **nombra** atributos (facilidad de uso, solidez tecnológica, compatibilidad, portabilidad, Internet) pero **no les pone número** |
| 3 — restricción | págs. 9, 11, 12 | no es un ERP · ámbito delimitado · compatibilidad con la arquitectura existente y las normas del grupo AI · tres fases · producción que no puede parar |
| 5 — despliegue | anexo 2a | siete centros en tres estados, cinco filiales, y los proveedores por Internet |

## 5. Las trampas del caso

1. **El título engaña.** El caso se llama *"La selección de software empresarial"* y catorce de sus
   quince páginas narran un concurso de proveedores. El negocio a modelar **no es la selección**:
   es la gestión de suministros que SiL'K va a soportar.
2. **Dos poblaciones con el mismo nombre.** *"Suministrador"* es a la vez el proveedor de piezas
   (actor del negocio) y el proveedor de software (stakeholder del proyecto, no actor).
3. **Los números del caso son de negocio, no de calidad.** 34 millones, 70 %, 85 %, 55-60 % son
   metas y diagnósticos del negocio. Ninguno es la **medida** de un escenario. Un driver de calidad
   sin número no es un driver: hay que **derivar** la medida y declarar el supuesto.
4. **Los atributos que el caso nombra no están en la lista de siete.** Compatibilidad y
   portabilidad **no** figuran entre los siete drivers de calidad de la diapositiva (rendimiento,
   escalabilidad, disponibilidad, seguridad, mantenibilidad, usabilidad, fiabilidad), pero **sí**
   en las normas ISO. Es el punto de contacto con el *"modelo de calidad"* del criterio 6.
5. **Se compra, no se construye.** El caso descarta el ERP completo y elige un paquete. La
   arquitectura que se pide es la de la **solución**: el paquete, sus integraciones con los
   sistemas existentes y el acceso de los proveedores.
6. **«Al presente» sin fabricar hechos.** Lo que se actualiza es la tecnología (la *"red Internet
   de Suministros"* de 1998); los hechos del caso —organización, ámbito, fases— no se tocan. Todo
   lo que se agregue va como **supuesto declarado**.
7. **El caso no dice quién ganó.** La entrega no tiene por qué elegir proveedor: la rúbrica no lo
   pide.

## 6. Decisiones de fondo — a tomar antes de empezar

| # | Decisión | Lecturas defendibles | Recomendación y razón |
|---|---|---|---|
| D1 | **La frontera del negocio** | A. Harley-Davidson entera · B. la **gestión de suministros y compras** · C. el proyecto de selección | **B.** Es el ámbito que el propio caso dibuja en el anexo 6a, y sigue el criterio ya usado en FarmaHosp (el negocio era el ciclo de vida del MAC, no el hospital). Con A el sistema queda chico frente al negocio; C es la trampa 1 |
| D2 | **Quiénes son actores** bajo B | proveedor de piezas, y las **áreas** que piden y reciben: ingeniería / desarrollo de productos, fabricación, cuentas por pagar, logística | regla de clase: *las áreas son actores, las personas son trabajadores*. Los compradores son **trabajadores**. Los 2.000 que generan solicitudes entran **como área**, no como individuos |
| D3 | **Primera descomposición** | A. las tres fases del anexo 6b · B. las seis actividades del anexo 6a agrupadas | **A.** Son tres, caen en el rango de 3 a 5, las nombra el caso y alinean un proceso con una fase de implantación |
| D4 | **Qué lista de «pasos»** para el criterio 6 | 4 pasos · 7 pasos · 8 etapas | **Los 7**, por el título de la lámina; nombrar las otras dos |
| D5 | **Qué modelo de calidad** | ISO 9126 (el del programa) · ISO/IEC 25010 (su sucesora) | **25010, declarando que sucede a la 9126 del programa**: la consigna pide métodos actuales y es la que trae compatibilidad y portabilidad como características |
| D6 | **«EaC»** | escenarios de atributos de calidad | escribirlos en las **seis partes** con medida numérica, y declarar la lectura de la sigla |
| D7 | **Sin grupo** | — | preguntarle a ella cómo nombrar el archivo y si la presentación individual habilita la entrega (pregunta 44) |

## 7. Cobertura del enunciado

| Frase del enunciado | Dónde se atiende |
|---|---|
| *"presentación en grupo … requisito para habilitar la entrega final"* | pendiente — pregunta 44 |
| *"Traer el caso al presente"* | criterios 3, 5 y 6, con supuestos declarados |
| *"Estudio y análisis individual del caso"* | este archivo y la ficha del enunciado |
| *"Discusión previa del caso en equipos"* | no aplica: trabaja solo |
| *"pasos para definir la arquitectura de software"* (numeral 3) | criterios 1 a 5, ordenados por D4 |
| *"mediante Eac"* (numeral 4) | criterio 6 — pregunta 41 |
| *"determinación del modelo de calidad"* | criterio 6 — pregunta 42 |
| *"GrupoN_CasoHD.pdf"* | paso 6 del método — pregunta 44 |

## Notas relacionadas

- [[_Método para resolver una tarea]] · [[_Protocolo de tutoría]]
- [[Preguntas pendientes para clase]] — las 43 a 46 siguen abiertas; la 41 y la 42 están resueltas
- [[Entrega - Tarea 2 FarmaHosp]] — el antecedente más cercano en forma, no en contenido

## Preguntas de repaso

1. ¿Por qué el negocio a modelar no es la selección del proveedor de software?
2. ¿Qué dos anexos dan casi hecho el criterio 1, y qué aporta cada uno?
3. ¿Cuál es la matriz nueva respecto de FarmaHosp y por qué es cuadrada?
4. ¿Por qué 34 millones de dólares no sirve como medida de un driver de calidad?
5. ¿Qué tres términos de la rúbrica no tienen material de clase?
