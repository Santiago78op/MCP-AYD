---
tema: Índice
fuente: —
fecha: 2026-08-19
---

# Índice — Análisis y Diseño de Sistemas

Nota de entrada de la bóveda. Desde acá navego todo.

> [!note] Última sesión: 2026-09-17 — dónde retomar
> Se procesaron las **49 capturas nuevas de `capturas_U2_F3/`** con 5 agentes en paralelo: 6 notas
> nuevas (flujo de datos, tuberías y filtros, llamada y retorno, RPC, SOA, MVC),
> [[Arquitectura en capas]] ampliada con la serie *"en o por capas"*, 75 flashcards y 17 términos de glosario nuevos
> (6 ampliados). 47 capturas quedaron recortadas; la 3 ya estaba y la 29 es la 30 sin el texto rojo.
> Los estilos **flujo de datos**, **llamada y retorno** y **SOA** pasaron de *nombrados* a
> *desarrollados*. El mapa está en *Capturas de clase, tercera tanda*.
>
> **Lo que sigue, por orden:**
> 1. **Parcial del 19/09.** Repaso de lo nuevo: llamada y retorno (*invocación síncrona*, bloqueo),
>    RPC/OO/MVC como **patrones arquitectónicos** de ese estilo, SOA en **dos familias**, ventajas y
>    desventajas de capas y de tuberías y filtros, y las responsabilidades de modelo, vista y controlador.
> 2. Llevar a clase [[Preguntas pendientes para clase]]: la 1 (**qué entra en el parcial**), la 24
>    (taxonomía de estilos, ahora con más evidencia) y las nuevas 30-37.
> 3. **Calidad del Software** (unidad 2 del programa) sigue **sin material de clase**.

> [!important] Antes que nada
> [[Programa oficial del curso]] — el contenido temático oficial de la sección A, el cronograma
> con las fechas de los parciales, y qué puntos del programa **todavía no tienen nota**.

## Mapa de carpetas

| Carpeta | Qué guarda |
|---|---|
| `00-Fuentes/presentaciones/` | Las presentaciones originales. **No se modifican nunca.** |
| `adjuntos/` | Imágenes extraídas de cada presentación (una subcarpeta por presentación). |
| `01-Notas/` | Notas atómicas: una por concepto. |
| `02-Diagramas/` | Diagramas exportados (`.excalidraw`, `.svg`, imágenes). |
| [[03-Glosario]] | Glosario global de términos. |
| `04-Flashcards/` | Tarjetas de repaso por tema, para el plugin Spaced Repetition. |
| `00-Fuentes/lecturas/` | Lecturas complementarias en PDF (Reynoso). |
| `05-Quizzes/` | Quizzes generados y mis resultados, con fecha. |
| `06-Proyecto-MCP/` | El proyecto práctico: diseño del servidor MCP `tutor-ayds`. |
| `08-Tareas/` | Método de trabajo, guías paso a paso por entregable, planes de tarea y enunciados. |
| `07-Referencias/` | Manual de las herramientas de dibujo (StarUML, Excalidraw) y el puente de la teoría al diagrama. No es materia de examen. |

## Notas por tema

### Arquitectura de software

- [[Arquitectura de software]] — definiciones (IEEE 1471, Kazman, Arlow & Neustadt, Booch), terminología y atributos
- [[Arquitecto de software]] — el rol según RUP y según SUN SL-425
- [[Beneficios de la arquitectura de software]] — los tres beneficios y qué permite la arquitectura
- [[Ciclo de influencias en la arquitectura]] — las cuatro influencias y la retroalimentación del sistema
- [[Estructuras y vistas arquitectónicas]] — estructura ≠ vista
- [[Modelo 4+1 vistas]] — las cinco vistas y sus diagramas UML
- [[Proceso de diseño arquitectónico]] — las **tres versiones** de "los pasos" reconciliadas (4 del deck, 7 de la lista, 8 etapas), el producto final y las comprobaciones
- [[Equilibrio de restricciones del proyecto]] — triángulo, diagrama de Kiviat y cubo de dimensiones
- [[Arquitectura en el ciclo de vida del software]] — por qué es iterativa y no una fase
- [[Diagrama de despliegue]] — punto 1.7, **ahora de clase** (= *diagrama de distribución*): nodo, dispositivo, entorno de ejecución, artefacto, camino
- [[Estilos arquitectónicos]] — punto 1.9, **de clase**: qué es un estilo (Elementos, Forma y Razón), estilo vs. patrón, la lista de 9 estilos + el catálogo de complemento
- [[Relaciones y dependencias en UML]] — qué significa cada flecha, hacia dónde apunta, y el puente con la matriz de dependencias
- [[Stakeholders]] — los cinco de la clase, ISO 42010, PALM, y la diferencia con actor y trabajador
- [[Tácticas y patrones arquitectónicos]] — el eslabón entre un atributo de calidad y una decisión

- [[Drivers arquitectónicos]] — **de clase**: la definición y los tres tipos (RF, calidad, restricción) con sus ejemplos
- [[Diagrama de contexto]] — **de clase**: la notación (producto, entidades, streamlines) y dos ejemplos resueltos
- [[Categorías de estructuras]] — **de clase**: módulos, componentes y conectores, asignación
- [[Método de diseño centrado en la arquitectura]] — **de clase**: las 8 etapas en 4 fases, con el caso de negocio como **paso 0**

#### Cómo se diseña y cómo se modela — capturas_U2 (**de clase**, 2026-09-15)

- [[Qué se tiene en cuenta para el diseño]] — punto 1.5: requisitos + contexto + experiencia del arquitecto → documento de diseño
- [[Cómo se modela la arquitectura]] — **hub** del 1.7: ADL, diagramas UML, diagramas de bloque de alto nivel
- [[Lenguajes de descripción de arquitectura]] — ADL: componentes y conectores en texto formal
- [[Diagramas UML estructurales y de comportamiento]] — estático vs dinámico, y qué diagrama va en qué vista
- [[Diagrama de bloques de alto nivel]] — primer paso antes del diseño detallado; SCADA, facturación, Multi-AZ
- [[Diagrama de componentes]] — tipos de componentes, componente vs clase, de clases a componentes
- [[Interfaces de componentes]] — provista/requerida, forma icónica/expandida
- [[Diagrama de paquetes]] — contenido, importar/exportar
- [[Diagrama de secuencia]] — mensajes síncronos/asíncronos, fragmentos alt/opt/break/loop
- [[Diagrama de clases]] — dos fines, notación, y el **método** para sacar clases de un enunciado
- [[Ejemplo resuelto - Parque de atracciones]] — **su encadenamiento completo**: enunciado → CDU expandidos → clases → componentes → despliegue
- [[Arquitectura monolítica]] — base de código única, la tabla de 7 características, Prime Video
- [[Arquitectura en capas]] — N-capas y 2 capas (cliente-servidor); en clase capa = nivel. Desde U2_F3: definición por capa, 3 niveles web, ventajas/desventajas y 2 ejercicios
- [[Arquitectura en la nube]] — cloud computing, N-niveles en la nube

#### Patrones, estilos y referencia — capturas_U2_F2 (**de clase**, 2026-09-16)

- [[Patrones de diseño]] — impacto relativo, las tres familias, la lista de 25
- [[Patrones arquitectónicos]] — gran impacto sobre el componente, la lista de 13, estilo ⊃ patrón arquitectónico ⊃ patrón de diseño, **alcance ≠ impacto**
- [[Arquitectura de referencia]] — modelo de referencia + patrón → arquitectura de referencia; la tabla de tipos de la **arquitectura candidata**
- [[Catálogo de estilos arquitectónicos]] — las familias (llamada y retorno incluye capas y MVC) y el árbol C&C; **sus dos taxonomías no coinciden**

#### Las familias desarrolladas — capturas_U2_F3 (**de clase**, 2026-09-17)

- [[Arquitectura centrada en el flujo de datos]] — *"la computación es dirigida por el flujo de datos"*, la analogía textil y el estilo **secuencial por lotes**
- [[Tuberías y filtros]] — filtros que transforman, pipes que conectan, cuándo usarlo, ventajas/desventajas y el ejemplo de seguridad
- [[Arquitectura de llamada y retorno]] — *invocación síncrona*, bloqueo, cliente-servidor, y sus **patrones arquitectónicos** RPC, OO y MVC
- [[Llamada a procedimiento remoto]] — RPC: parámetros por valor y serializables, los 15 pasos cliente-red-servidor
- [[Arquitectura orientada a servicios]] — SOA: antes/después, invocación directa o por **ESB**, y por qué es también *event-based*
- [[Modelo-Vista-Controlador]] — patrón arquitectónico: responsabilidades de modelo, vista y controlador, modelo activo, y por qué **no** es 3 capas
- [[Convenios del diagrama de CUN]] — **de clase**: cuántos actores, navegabilidad, y los dos usos de `«include»`

### Calidad del software

- [[Atributos de calidad]] — unidad 2: definición, los seis del programa, escenarios de 6 partes, tradeoffs e ISO

### Arquitectura en el ciclo de vida

- [[El ciclo del architecting]] — los seis pasos, los cinco rasgos, y qué es la descripción arquitectónica
- [[Evaluación de la arquitectura]] — ATAM: fases, nueve pasos, riesgos, sensibilidades y tradeoffs
- [[Arquitectura y proceso de desarrollo]] — predictivo (RUP) vs ágil (SCRUM), el rol del arquitecto en cada flujo, implementación y pruebas

### Requisitos

- [[Matriz de trazabilidad de requisitos]] — trazabilidad pre-RS y post-RS, la RTM y la cadena de arquitectura. **De clase**: sale de `NT1. Trazabilidad de Requerimientos.pdf`, que además trae la **plantilla obligatoria** de la matriz

### Casos de uso

- [[Caso de uso]] — definición de Jacobson, para qué sirven y en qué momento se usan
- [[Casos de uso vs DFD]] — la comparación, en dos diferencias
- [[Modelo de casos de uso del negocio]] — el modelo, sus estereotipos y cómo se construye
- [[Actor del negocio]] — rol, candidatos, consideraciones y generalización entre actores
- [[Caso de uso del negocio]] — definición de CUN y sus consideraciones
- [[Proceso de negocio]] — la definición desarmada, y por qué no es una función
- [[Identificación de procesos del negocio]] — clasificación, agrupamiento y objetivos
- [[Relación de inclusión include]] — `<include>`
- [[Relación de extensión extend]] — `<extend>`
- [[Generalización y especialización en casos de uso]] — padre e hijos, y las tres relaciones comparadas
- [[Realizaciones de casos de uso del negocio]] — el adentro del negocio
- [[Descripción textual de casos de uso]] — la plantilla y el ejemplo *Atender pedido*

## Flashcards

- [[Flashcards - Arquitectura de software]] (42 tarjetas) — 20 de clase (capturas_U2_F2: 4+1 vistas y fundamentos)
- [[Flashcards - Casos de uso del negocio]] (27 tarjetas)
- [[Flashcards - Trazabilidad de requisitos]] (25 tarjetas)
- [[Flashcards - Diagrama de despliegue]] (34 tarjetas) — 11 de clase (capturas_U2)
- [[Flashcards - Estilos arquitectónicos]] (58 tarjetas) — 31 de clase (capturas_U2 y capturas_U2_F2)
- [[Flashcards - Patrones de diseño y arquitectónicos]] (14 tarjetas) — de clase (capturas_U2_F2)
- [[Flashcards - Arquitectura de referencia y catálogo]] (15 tarjetas) — de clase (capturas_U2_F2)
- [[Flashcards - Arquitectura en capas]] (15 tarjetas) — de clase (capturas_U2_F3)
- [[Flashcards - Flujo de datos]] (15 tarjetas) — de clase (capturas_U2_F3)
- [[Flashcards - Llamada y retorno]] (15 tarjetas) — de clase (capturas_U2_F3)
- [[Flashcards - Arquitectura orientada a servicios]] (15 tarjetas) — de clase (capturas_U2_F3)
- [[Flashcards - Modelo-Vista-Controlador]] (15 tarjetas) — de clase (capturas_U2_F3)
- [[Flashcards - Relaciones y dependencias en UML]] (30 tarjetas) — 8 de clase (capturas_U2)
- [[Flashcards - Diseño arquitectónico]] (10 tarjetas) — de clase (capturas_U2)
- [[Flashcards - Diagramas de alto nivel y secuencia]] (10 tarjetas) — de clase (capturas_U2 + PDF Tema 5)
- [[Flashcards - Diagrama de componentes]] (10 tarjetas) — de clase (capturas_U2 + PDF Tema 5)
- [[Flashcards - Diagrama de paquetes]] (9 tarjetas) — de clase (capturas_U2)
- [[Flashcards - Diagrama de clases]] (10 tarjetas) — de clase (capturas_U2 + PDF IS 04 05b)
- [[Flashcards - Atributos de calidad]] (24 tarjetas)
- [[Flashcards - Stakeholders, tácticas y evaluación]] (30 tarjetas)
- [[Flashcards - Arquitectura y proceso de desarrollo]] (28 tarjetas)
- [[Flashcards - Drivers arquitectónicos y contexto]] (39 tarjetas) — de diapositivas de clase
- [[Flashcards - CUN, convenios y método]] (34 tarjetas) — de diapositivas de clase
- [[Flashcards - Ejemplos resueltos y descripción textual]] (25 tarjetas) — de diapositivas de clase

> [!note] Sobre las tres últimas
> Salen de **diapositivas de clase**, pero unas pocas respuestas llevan el marcador
> **«(lectura nuestra)»**: derivan de lo que ella dijo y son correctas, pero **no son su texto**.
> Sirve para saber qué se puede citar como suyo y qué no.

## Tareas

- [[_Método para resolver una tarea]] — el método general: punto de inicio y 6 pasos
- [[Plan - Caso 1 FarmaHosp]] — la rúbrica desarmada: 4 criterios, 100 puntos, y las ambigüedades a preguntar
- [[Guía - Caso de negocio]] — la secuencia canónica: contexto → core → primera descomposición → CDU expandidos → matriz
- [[Guía - Diagrama de casos de uso del negocio]] — paso a paso con ejemplo visual incremental
- [[Guía - Identificación de stakeholders]] — criterio 2 (25 pts): las tres checklists, la necesidad oculta y los conflictos
- [[Guía - Drivers de calidad y restricción]] — criterio 3 (30 pts): escenarios, restricciones y la priorización de los 5
- [[Guía - Matrices de trazabilidad]] — las tres matrices que pide la rúbrica (20 pts)
- [[Guía - Selección del estilo arquitectónico]] — el molde de respuesta con SOA por defecto, sus complementarios, los descartes y **cuándo NO contestar SOA**
- [[Ejemplos resueltos de casos de negocio]] — **de clase**: los **cuatro** encadenamientos completos (Tienda Electrónica, Fábrica, Restaurante, **Hospital**) y la checklist para compararte

Los artefactos vivos de cada tarea (el estado real se lee **ahí**, no acá):

- [[Preguntas pendientes para clase]] — **las dudas abiertas** (las 43-46 son del Caso Harley-Davidson), con su evidencia; llevá las de prioridad alta a la próxima clase
- [[Avance - Tarea 2 FarmaHosp]] — **Tarea 2 (entrega 18/09)**: criterios 1-4 reutilizados, 5 estilo y 6 bloques y despliegue
- [[Entrega - Tarea 2 FarmaHosp]] — descripciones textuales de CDU-01..07, estilo SOA justificado, bloques y despliegue
- [[Plan - Caso Harley-Davidson]] — **Caso Harley-Davidson, proyecto SiL'K (entrega 13/10)**: la rúbrica desarmada en 6 criterios, lo que el material no cubre (EaC, modelo de calidad) y las decisiones de fondo
- [[Avance - Caso Harley-Davidson]] — el tablero: los 6 criterios hechos y lo que falta que haga el estudiante antes de subir
- [[Guion - Presentación Caso Harley-Davidson]] — el guion de los 10 minutos: qué decir en cada lámina, cuándo hacer clic, el reloj y las preguntas probables
- [[Entrega - Caso Harley-Davidson]] — el entregable completo: caso de negocio, 17 stakeholders, drivers, cuatro matrices, SOA con bloques y despliegue, y el modelo de calidad ISO/IEC 25010
- [[Ejemplo resuelto - Sistema de Transporte READM]] — **el ejemplo completo de la presentación Calidad del Software**: de contexto a despliegue, la tabla de EAC y el bus de eventos · tarjetas en [[Flashcards - Ejemplo READM y bus de eventos]]
- [[Avance - Caso 1 FarmaHosp]] — el tablero: criterios, ruta de pasos y bitácora
- [[Entrega - Caso 1 FarmaHosp]] — el entregable numerado según la rúbrica (**manda sobre el Avance**)
- [[Entrega - Parcial 1 SmartPress]] — lo entregado en el primer parcial (22/08), con sus láminas en `02-Diagramas/examen/`
- [[SmartPress - Respuestas redactadas]] — las respuestas en prosa de ese parcial

## Referencias de herramientas

No es materia de examen: es el manual de las herramientas del ecosistema.

- [[StarUML]] — los 7 tipos de Mermaid importables y qué se pierde en el camino
- [[Excalidraw]] — los 5 tipos nativos y el fallback a imagen SVG
- [[De la teoría al diagrama]] — el puente: qué sintaxis usar para cada diagrama de la materia

## Preparación del primer parcial — 22 de agosto

> [!warning] El parcial cae DENTRO del bloque 1.8 / 1.9
> El cronograma pone *"Principios de Diseño de Software (1.8 y 1.9): **17 al 24 de agosto**"* y el
> parcial es el **22**. **No se puede asumir que solo entra hasta 1.7.**
>
> **Pregunta para el auxiliar, antes del sábado:** *¿el parcial cubre 1.8 y 1.9, o solo hasta 1.7?*

Estado real de preparación, punto por punto:

| Punto | Estado | Con qué contás |
|---|---|---|
| 1.1 – 1.3 Concepto, importancia, beneficios | ✅ **núcleo sólido** | [[Arquitectura de software]], [[Beneficios de la arquitectura de software]] |
| 1.4 Pasos para la definición | ✅ **núcleo** | [[Proceso de diseño arquitectónico]] — con las **tres** versiones reconciliadas |
| 1.5 Qué se tiene en cuenta | ✅ **núcleo** | [[Método de diseño centrado en la arquitectura]] (8 etapas + paso 0), [[Ciclo de influencias en la arquitectura]] |
| 1.6 Arquitectura y Requerimientos (CDU de negocio) | ✅ **núcleo fuerte** | el bloque de 12 notas de casos de uso + [[Convenios del diagrama de CUN]] + [[Drivers arquitectónicos]] |
| 1.7 Diagramas de Despliegue | ✅ **núcleo** | [[Diagrama de despliegue]] |
| 1.8 Estructuras y Vistas · Categorías | ✅ **núcleo** | [[Categorías de estructuras]], [[Estructuras y vistas arquitectónicas]], [[Modelo 4+1 vistas]] |
| **1.9 Géneros y Estilos** | ⚠️ **el punto débil** | [[Estilos arquitectónicos]] es **complemento entero** (Reynoso + SAIP, sin presentación) |

> [!important] Si el parcial cubre 1.9, ahí está el riesgo
> Tres subpuntos, tres estados distintos:
>
> | Subpunto | Fuente |
> |---|---|
> | **Arquitectura candidata** y **de referencia** | ✅ ya tienen fuente de clase: el *Flujo de Definición* de Ambler, en [[Proceso de diseño arquitectónico]] |
> | **Catálogo de estilos** (cliente-servidor, capas, centrada en datos, flujo de datos, llamada y retorno, eventos) | ⚠️ complemento: los seis están cubiertos, pero de Reynoso y el SAIP |
> | **Diseño arquitectónico: on premise vs cloud** | ❌ **sin fuente alguna** — ni clase, ni libros locales |
>
> Prioridad de repaso si el tiempo es corto: **1.6 y 1.9**. El 1.6 porque es el más pesado y el que
> alimenta el Caso 1; el 1.9 porque es el que menos respaldo tiene.

> [!note] Actualizado el 2026-09-16 — esta tabla es del primer parcial y quedó superada
> Candidata, de referencia y el catálogo de estilos **ya tienen diapositivas de clase**
> (capturas_U2_F2): [[Arquitectura de referencia]] y [[Catálogo de estilos arquitectónicos]]. On premise
> sigue sin fuente. El estado vigente está en *Contenido del curso — estado real*, más abajo.

---

## Contenido del curso — estado real

Alineado con el **programa oficial** de la sección A (4 unidades), no con una lista genérica.
El detalle punto por punto está en [[Programa oficial del curso]].

### Unidad 1 — Principios de Diseño de Arquitectura de Software

- [x] 1.1 Concepto — [[Arquitectura de software]]
- [x] 1.2 ¿Por qué es importante? — [[Arquitectura de software]]
- [x] 1.3 Beneficios — [[Beneficios de la arquitectura de software]]
- [x] 1.4 Pasos para la definición — [[Proceso de diseño arquitectónico]]
- [x] **1.5 ¿Qué se tiene en cuenta para el diseño?** — [[Qué se tiene en cuenta para el diseño]] (**de clase**, capturas_U2) + [[Proceso de diseño arquitectónico]] con los **7 pasos**, el ciclo `«precede»` y el flujo de definición de Ambler (**de clase**); más: [[Ciclo de influencias en la arquitectura]], [[Equilibrio de restricciones del proyecto]]
- [x] 1.6 Arquitectura y Requerimientos (CDU de negocio) — bloque de casos de uso + [[Matriz de trazabilidad de requisitos]]
- [x] **1.7 ¿Cómo se modela? Diagramas de Despliegue** — **de clase** desde capturas_U2: hub [[Cómo se modela la arquitectura]] → [[Diagrama de componentes]], [[Diagrama de despliegue]], [[Diagrama de paquetes]], [[Diagrama de clases]], [[Diagrama de secuencia]], [[Diagrama de bloques de alto nivel]]
- [x] **1.8 Estructuras y Vistas · Categorías de Estructuras** — [[Estructuras y vistas arquitectónicas]] + [[Categorías de estructuras]] (**de clase**) ~~; las tres categorías** están en [[Diagrama de despliegue]] §3
- [~] **1.9 Géneros y Estilos Arquitectónicos** — **de clase casi entero** (capturas_U2, U2_F2 y U2_F3): [[Estilos arquitectónicos]], [[Catálogo de estilos arquitectónicos]], [[Arquitectura de referencia]], [[Patrones arquitectónicos]], [[Patrones de diseño]], [[Arquitectura monolítica]], [[Arquitectura en capas]], [[Arquitectura en la nube]], [[Arquitectura centrada en el flujo de datos]], [[Tuberías y filtros]], [[Arquitectura de llamada y retorno]], [[Llamada a procedimiento remoto]], [[Arquitectura orientada a servicios]], [[Modelo-Vista-Controlador]]. Falta: centrada en datos y basada en eventos desarrolladas, on premise

### Unidad 2 — Calidad del Software

- [x] Conceptos generales · ¿Por qué es importante? — [[Atributos de calidad]] (**complemento**: falta la presentación)
- [x] **Normas ISO** — ISO 9126 y 25010 en [[Atributos de calidad]] (**complemento**)
- [x] **Atributos de calidad**: los seis del programa, con escenarios de 6 partes — [[Atributos de calidad]] (**complemento**)

### Unidad 3 — Arquitectura en el Ciclo de Vida

- [x] Arquitectura en las metodologías: predictivo y ágil (SCRUM) — [[Arquitectura y proceso de desarrollo]] §2–5 (**complemento**)
- [ ] Integrando con la arquitectura de la información — **cero material en las fuentes locales**, hay que pedirlo en clase
- [x] Documentando la arquitectura de software — [[El ciclo del architecting]] §4 (**complemento**)
- [x] Implementación y pruebas — [[Arquitectura y proceso de desarrollo]] §3, el rol del arquitecto por flujo (**complemento**)
- [x] **Evaluación de la arquitectura** — [[Evaluación de la arquitectura]] (**complemento**: ATAM completo)
- [x] Dónde se coloca en el ciclo de vida — [[Arquitectura en el ciclo de vida del software]]

### Unidad 4 — Arquitectura y Negocios

- [ ] Aplicaciones con casos

## Huecos detectados

Lo que **falta material** para poder escribir la nota, ordenado por urgencia:

| Prioridad | Qué falta | Por qué urge |
|---|---|---|
| Media | ~~Presentación de **1.9**~~ — **RESUELTO EN PARTE** con capturas_U2 (monolítica, capas, nube, diseño/estilo/patrón). Faltan **basada en eventos**, **on premise** y los estilos solo nombrados (centrado en datos, flujo de datos, llamada y retorno) | Parte de 1.9 |
| Media | ~~**Arquitectura candidata** y **de referencia**~~ — **RESUELTO**: primero con el *Flujo de Definición* de Ambler ([[Proceso de diseño arquitectónico]]) y desde el 2026-09-16 con diapositivas propias → [[Arquitectura de referencia]]. Sigue faltando **on premise vs cloud** | Parte de 1.9 |
| **Alta** | Presentación de la **unidad 2** para validar [[Atributos de calidad]], que hoy es todo complemento | Se da del 25 de agosto al 7 de septiembre |
| **Alta** | **"Integrando con la arquitectura de la información"** (unidad 3): lo busqué en la guía de estudio, en Reynoso y en Garland — **cero menciones** en todas | Es el único punto del programa sin **ninguna** fuente |
| Baja | Unidad 3 (validar contra la presentación) y unidad 4 completa | Septiembre y octubre |
| Baja | **Unidad 4**: hay una captura sin procesar — *"Sistema de entrega de valor"* (`adjuntos/capturas-clase/sistema-de-entrega-de-valor.png`), con el modelo entorno externo / interno / portafolio → programa → proyecto → producto → operaciones. Encaja en "Arquitectura y Negocios" | Se da del 19 al 27 de octubre |

Y lo que falta por otras razones:

- **Casos de uso del sistema.** El deck dice "del Negocio **y del Sistema**" pero solo desarrolla los del negocio.
- **DFD.** Aparece solo como término de comparación en [[Casos de uso vs DFD]].
- ~~**Diagramas UML individuales.**~~ — **RESUELTO** con capturas_U2 y el PDF Tema 5: componentes, despliegue, paquetes, clases y secuencia tienen nota. Sigue sin nota el **diagrama de actividad**.
- ~~**Trazabilidad de requisitos** de fuente externa~~ — **RESUELTO**: apareció `NT1. Trazabilidad de Requerimientos.pdf`, nota técnica de clase, que es **la fuente de la plantilla** (su fig. 1, p. 91). El tema es núcleo, no complemento. Ver [[Matriz de trazabilidad de requisitos]].

## Presentaciones procesadas

| Presentación | Páginas | Fecha de proceso | Notas generadas |
|---|---|---|---|
| Arquitectura de Software.pdf | 29 | 2026-08-19 | 9 (bloque de arquitectura) |
| Arquitectura de Software (1).pdf | 20 | 2026-08-19 | aporta a las mismas 9 |
| CDU Negocio - Modelado de Drivers RF.pdf | 27 | 2026-08-19 | 12 (bloque de casos de uso) |
| NT Identificación de CDU de Negocio.pdf | 6 | 2026-08-19 | artículo fuente del deck (Hernández, 2005) |
| **NT1. Trazabilidad de Requerimientos.pdf** | 13 | 2026-08-19 | [[Matriz de trazabilidad de requisitos]] + [[Guía - Matrices de trazabilidad]]; **fuente de la plantilla** |
| ProgramaClase-AYD2-2-26.pdf | 5 | 2026-08-19 | [[Programa oficial del curso]] |
| Caso FarmaHosp.pdf | 8 | 2026-08-19 | [[Plan - Caso 1 FarmaHosp]] + las 5 guías de `08-Tareas/` |
| Large-Scale Software Architecture.pdf | 281 | 2026-08-19 | [[Arquitectura y proceso de desarrollo]] (complemento) |
| **Bass, Clements, Kazman — SAIP 4ª ed.** | 620 | 2026-08-19 | el **único libro de la bibliografía oficial** en la bóveda; sostiene [[Atributos de calidad]], [[Tácticas y patrones arquitectónicos]], [[Evaluación de la arquitectura]], [[El ciclo del architecting]], [[Stakeholders]] y [[Guía - Drivers de calidad y restricción]] |
| **capturas de clase** (68 imágenes) | — | 2026-08-19 | [[Ejemplos resueltos de casos de negocio]], [[Drivers arquitectónicos]], [[Diagrama de contexto]], [[Categorías de estructuras]], [[Método de diseño centrado en la arquitectura]], [[Convenios del diagrama de CUN]] + aportan a 6 notas y 2 guías más |

### Capturas de clase: inventario verificado

68 capturas de la **unidad 1** en `00-Fuentes/capturas_U1/` (hasta el 15/09/2026 estaban en `00-Fuentes/capturas/`; el estudiante las separó por unidad). Así están repartidas:

| Estado | Cuántas | Detalle |
|---|---|---|
| **Recortadas, nombradas y citadas** en una nota | **45** | están en `adjuntos/capturas-clase/` con nombre descriptivo |
| **Contenido cubierto** por notas hechas desde el PDF | **21** | son las mismas diapositivas del deck de 27 páginas, ya embebidas desde `adjuntos/cdu-negocio-modelado-drivers-rf/` |
| **Pendiente a propósito** | **1** | *"Sistema de entrega de valor"* — material de **unidad 4**, que se da del 19 al 27 de octubre |
| Descartada | 1 | la portada del deck: sin valor informativo |

> [!important] Cómo se verificó que las 21 no dejan huecos
> No por suposición: se listó el contenido concreto de cada una y se buscó en el corpus de notas.
> Ese chequeo encontró **4 detalles que faltaban de verdad**, y se agregaron:
>
> | Lo que faltaba | Dónde quedó |
> |---|---|
> | **Puntos de extensión** — el mecanismo formal de `«extend»` | [[Relación de extensión extend]] |
> | *"en el lugar especificado en el caso base"* — el de `«include»` | [[Relación de inclusión include]] |
> | *"añadir **o redefinir**"* — lo que hace fuerte a la generalización | [[Generalización y especialización en casos de uso]] |
> | ***Arco de comunicación*** y "formato estructurado de prosa" | [[Caso de uso]] |
>
> Y encontró **dos secciones duplicadas** que se habían creado al cablear las capturas
> (*"¿En qué momento se usan?"* y *"El ejemplo: vendedores ambulantes"*): fusionadas.

### Capturas de clase de la unidad 2: inventario (`00-Fuentes/capturas_U2/`, 59)

Recibidas el 2026-09-15. **Las 59 están recortadas, nombradas y citadas** en
`adjuntos/capturas-clase-U2/<tema>/` — ninguna descartada.

| Capturas | Subcarpeta | Notas |
|---|---|---|
| 0–11 | `diseno-arquitectonico/` | [[Proceso de diseño arquitectónico]], [[Arquitectura en el ciclo de vida del software]], [[Qué se tiene en cuenta para el diseño]], [[Arquitecto de software]], [[Cómo se modela la arquitectura]], [[Lenguajes de descripción de arquitectura]] |
| 12–20 | `diagramas-alto-nivel/` | [[Diagramas UML estructurales y de comportamiento]], [[Diagrama de bloques de alto nivel]] |
| 21, 43–47, 49–52 | `estilos/` | [[Estilos arquitectónicos]], [[Arquitectura monolítica]], [[Arquitectura en capas]], [[Arquitectura en la nube]] |
| 22–33, 54 | `componentes/` | [[Diagrama de componentes]], [[Interfaces de componentes]], [[Relaciones y dependencias en UML]] |
| 34–42, 48 | `despliegue/` | [[Diagrama de despliegue]], [[Diagrama de paquetes]] |
| 53, 55–58 | `ejemplo-parque/` | [[Diagrama de clases]], [[Ejemplo resuelto - Parque de atracciones]] |
| `capturas_U2_F2/` 0 | `estilos/` | [[Estilos arquitectónicos]] §1 — tipos de patrón (el resto de esa carpeta, en la tabla siguiente) |

Y dos PDF que llegaron con ellas:

| PDF | Págs. | Adjuntos | Notas |
|---|---|---|---|
| *modelado-de-arquitectura-software. Diagrmas UML completo* ("TEMA 5") | 8 | `adjuntos/modelado-arquitectura-tema5/` | UML y vistas (p.1), componentes (2–3), clases (3–4), despliegue y nube (4–6), secuencia (6–8) |
| *IS 04 05b Ejemplos de Diagramas de Clases* (Studocu; la captura 56 lo cita como su material) | 9 | `adjuntos/ejemplos-diagramas-clases/` | [[Diagrama de clases]] (método), [[Ejemplo resuelto - Parque de atracciones]] (ejercicio 2) |

> [!warning] "U2" es el nombre de la carpeta, no el punto del programa
> El contenido corresponde a **1.4, 1.5, 1.7 y 1.9** de la unidad 1 del programa oficial. La unidad 2
> del programa (**Calidad del Software**) sigue sin presentación de clase.

### Capturas de clase, segunda tanda: inventario (`00-Fuentes/capturas_U2_F2/`, 40)

Recibidas el 2026-09-16. Las 40 tienen destino y **ninguna quedó descartada**: 25 son nuevas y
quedaron recortadas en `adjuntos/capturas-clase-U2/<tema>/`, la 0 ya estaba procesada, y **14 eran
diapositivas que ya estaban**,
así que no se copiaron y se sumaron a la `fuente` de la nota como *"la clase la volvió a dar"*.

| Capturas | Subcarpeta | Notas | Repetidas (sin copia) |
|---|---|---|---|
| 0–8 | `patrones/` (0 en `estilos/`) | [[Patrones de diseño]], [[Patrones arquitectónicos]], [[Tácticas y patrones arquitectónicos]] | — |
| 9, 14–22 | `estilos/` | [[Estilos arquitectónicos]] §1.1, §1.2, §2 | 14 = capturas_U2 21 |
| 23–26 | `arquitectura-referencia/` | [[Arquitectura de referencia]] | — |
| 30, 30-componentes-conectores | `catalogo-estilos/` | [[Catálogo de estilos arquitectónicos]] | — |
| 10–13, 29 | `vistas-4mas1/` (solo la 29) | [[Modelo 4+1 vistas]] | 10–13 = PDF *Arquitectura de Software* págs. 25, 27, 28, 29 |
| 27, 28, 31–38 | `fundamentos-arquitectura/` (solo la 27) | [[Categorías de estructuras]], [[Arquitectura de software]], [[Equilibrio de restricciones del proyecto]], [[Beneficios de la arquitectura de software]] | 28, 31–38 = páginas de los dos PDF *Arquitectura de Software* |

> [!note] Dos correcciones que trajo esta tanda
> - **La vista de procesos se complementa con el diagrama de actividad, no con el de secuencia.**
>   [[Categorías de estructuras]] y [[Diagrama de secuencia]] decían otra cosa.
> - **Capas y MVC son de llamada y retorno** (captura 30). [[Estilos arquitectónicos]] §7 lo dejaba
>   como duda.

### Capturas de clase, tercera tanda: inventario (`00-Fuentes/capturas_U2_F3/`, 49)

Recibidas el 2026-09-17, todas de la serie *"Estilos Arquitectónicos"*. Las 49 tienen destino:
**47 nuevas** recortadas en `adjuntos/capturas-clase-U2/<tema>/`, la **3** ya estaba (el ejemplo
smartphone/smartwatch) y la **29** es la 30 sin la definición de síncrono en rojo.

| Capturas | Subcarpeta | Notas | Sin copia |
|---|---|---|---|
| 0–12 | `capas/` | [[Arquitectura en capas]] §3, §5-§12 | 3 = `estilos/dos-capas-smartphone-smartwatch.png` |
| 13–17, 28 | `flujo-datos/` | [[Arquitectura centrada en el flujo de datos]] | — |
| 18–27 | `flujo-datos/` | [[Tuberías y filtros]] | — |
| 29–32, 40 | `llamada-retorno/` | [[Arquitectura de llamada y retorno]] | 29 = variante de la 30 |
| 41–43 | `llamada-retorno/` | [[Llamada a procedimiento remoto]] | — |
| 33–39 | `soa/` | [[Arquitectura orientada a servicios]] | — |
| 44–48 | `mvc/` | [[Modelo-Vista-Controlador]] | — |

> [!note] Lo que cambió en la doctrina con esta tanda
> - **RPC, orientado a objetos y MVC son patrones arquitectónicos** del estilo llamada y retorno
>   (captura 40), **fuera** de la lista de 13 de [[Patrones arquitectónicos]].
> - **SOA es de llamada y retorno y basada en eventos** (33-39): coincide con el árbol C&C.
> - La clase usa el **árbol C&C como portada** de cada familia (13, 29-30).
> - La ficha de complemento de tubería y filtro decía "incremental"; la clase dice que **los datos se
>   transmiten de forma completa** (27). Manda la clase.
> - REST dejó de estar "sin material": hay una diapositiva de *API RESTful* dentro de flujo de datos (20).

> [!info] Sobre los dos PDF de arquitectura
> No son el mismo archivo ni uno es subconjunto del otro. El de **29 páginas** trae las
> definiciones formales y el **modelo 4+1 vistas** completo; el de **20 páginas** trae el
> **ciclo de influencias**, el **diagrama de Kiviat**, el cubo de dimensiones, los **beneficios
> 2 y 3** y el ejemplo de AWS. Las notas están hechas con la **unión** de ambos y cada nota
> declara en el frontmatter de cuál viene.
