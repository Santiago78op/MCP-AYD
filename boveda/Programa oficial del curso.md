---
tema: Programa del curso
fuente: "ProgramaClase-AYD2-2-26.pdf — ECYS-USAC, vía DTT-ECYS"
fecha: 2026-09-17
---

# Programa oficial — Análisis y Diseño de Sistemas II (785)

Datos del programa oficial de **mi sección**, para saber contra qué se estudia y qué falta.

| Dato | Valor |
|---|---|
| Curso | Análisis y Diseño de Sistemas II |
| Código | **785** · 5 créditos |
| Escuela | Ciencias y Sistemas · Área de **Software** |
| Pre-requisito | 283 — Análisis y Diseño de Sistemas 1 |
| Post-requisito | 780 — Software Avanzado |
| Semestre | **2do semestre 2026** |
| Docente | MBA. MSc. Ing. Claudia Rojas de Morán |
| Auxiliar | Kevin Josué Hernández Gómez |
| Sección | **A** |
| Curso | Lunes y Martes, 17:20–19:00 (meet) |
| Laboratorio | Jueves, 17:20–19:00 (meet) |

## Descripción y objetivo

> El curso está diseñado para que el estudiante identifique y aplique los distintos estilos
> arquitectónicos, así como los patrones aplicables para el diseño de componentes de una
> aplicación. El uso de dichos estilos y patrones de arquitectura, **técnicas para definir una
> arquitectura que satisfaga los requerimientos funcionales y no funcionales**, comprenden el
> resto del curso.

Objetivo general: aplicar procesos de diseño de software que consideren **los diferentes tipos de
requerimientos** que pueden impactar en la estructura del sistema.

Eso último es la brújula del curso: todo se juzga contra los requerimientos, funcionales y no
funcionales. Es la razón por la que la [[Matriz de trazabilidad de requisitos]] importa acá.

---

## Cronograma y evaluaciones

| Actividad | Fecha |
|---|---|
| Principios de Diseño de Software (1.1 a 1.7) | 13 de julio al 10 de agosto |
| **Primer parcial** | **22 de agosto** |
| Principios de Diseño de Software (1.8 y 1.9) | 17 al 24 de agosto |
| Calidad del Software | 25 de agosto al 7 de septiembre |
| **Segundo parcial** | **19 de septiembre** |
| Arquitectura en el ciclo de vida | 8 de septiembre al 12 de octubre |
| Semana de Congresos Estudiantiles | 28 de septiembre al 2 de octubre |
| **Tercer parcial** | **17 de octubre** |
| Arquitectura y Negocios | 19 al 27 de octubre |
| Último día de clases | 30 de octubre |
| Evaluaciones finales | 31 de octubre al 13 de noviembre |

Ponderación: zona 75 pts (clase: exposición 4 + tareas/cortos 5 + tres parciales 10/13/13;
laboratorio 30 pts equivalentes) y examen final 25 pts. **Se aprueba con 61.** El laboratorio se
aprueba con 61/100 y es **obligatorio ganarlo** para tener derecho al examen final.

---

## Contenido temático y estado de mis notas

Leyenda: ✅ cubierto · 🟡 parcial · ❌ sin nota

### Unidad 1 — Principios de Diseño de Arquitectura de Software

| Punto | Tema | Estado | Nota |
|---|---|---|---|
| 1.1 | Concepto de arquitectura de software | ✅ | [[Arquitectura de software]] |
| 1.2 | ¿Por qué es importante? | ✅ | [[Arquitectura de software]] |
| 1.3 | Beneficios de una arquitectura de SW | ✅ | [[Beneficios de la arquitectura de software]] |
| 1.4 | Pasos para la definición de una arquitectura | ✅ | [[Proceso de diseño arquitectónico]] |
| 1.5 | ¿Qué se tiene en cuenta para el diseño? | ✅ | [[Qué se tiene en cuenta para el diseño]] (clase, capturas_U2) + [[Ciclo de influencias en la arquitectura]], [[Equilibrio de restricciones del proyecto]] |
| 1.6 | **Arquitectura y Requerimientos (CDU de negocio)** | ✅ | Todo el bloque de casos de uso + [[Matriz de trazabilidad de requisitos]] |
| 1.7 | **¿Cómo se modela? Diagramas de Despliegue** | ✅ | **Dado en clase** (capturas_U2, recibidas 2026-09-15). Hub: [[Cómo se modela la arquitectura]] → [[Lenguajes de descripción de arquitectura]], [[Diagramas UML estructurales y de comportamiento]], [[Diagrama de bloques de alto nivel]], [[Diagrama de componentes]], [[Interfaces de componentes]], [[Diagrama de despliegue]], [[Diagrama de paquetes]], [[Diagrama de secuencia]], [[Diagrama de clases]], [[Ejemplo resuelto - Parque de atracciones]] |
| 1.8 | Estructuras y Vistas · Categorías de Estructuras | ✅ | [[Estructuras y vistas arquitectónicas]] + [[Categorías de estructuras]] (capturas de clase del 19/08; la lámina *Estructuras* de capturas_U2_F2 27 llama "de localización" a la de asignación) + [[Modelo 4+1 vistas]] (repetido en clase el 16/09, capturas_U2_F2 10-13 y 29) |
| 1.9 | Géneros y Estilos Arquitectónicos | 🟡 | **Casi completo** (capturas_U2, capturas_U2_F2 y capturas_U2_F3): [[Estilos arquitectónicos]], [[Catálogo de estilos arquitectónicos]], [[Arquitectura de referencia]], [[Patrones arquitectónicos]], [[Patrones de diseño]], [[Arquitectura monolítica]], [[Arquitectura en capas]], [[Arquitectura en la nube]], [[Arquitectura centrada en el flujo de datos]], [[Tuberías y filtros]], [[Arquitectura de llamada y retorno]], [[Llamada a procedimiento remoto]], [[Modelo-Vista-Controlador]], [[Arquitectura orientada a servicios]]. Falta **on premise**, **centrada en datos** y el desarrollo de **eventos** |

El detalle de 1.9 contra lo que dio la clase (capturas_U2, capturas_U2_F2 y capturas_U2_F3):

| Tema del programa | Estado en clase |
|---|---|
| Cliente-servidor | ✅ como *arquitectura de 2 capas* y como *call return: cliente-servidor* (U2_F3 32) → [[Arquitectura en capas]] · [[Arquitectura de llamada y retorno]] |
| En o por capas | ✅ N-Capas + clínica veterinaria + la serie *"en o por capas"* (U2_F3 0-12: definición, anillos, 3 niveles, ventajas/desventajas, 2 ejercicios) → [[Arquitectura en capas]] |
| On premise vs cloud | 🟡 cloud sí ([[Arquitectura en la nube]]); on premise **sin diapositiva** |
| Flujo de datos | ✅ U2_F3 13-28: la familia, tuberías y filtros, secuencial por lotes → [[Arquitectura centrada en el flujo de datos]] · [[Tuberías y filtros]] |
| Llamada y retorno | ✅ U2_F3 29-48: definición, cliente-servidor, SOA, y los patrones RPC, OO y MVC → [[Arquitectura de llamada y retorno]] · [[Arquitectura orientada a servicios]] · [[Llamada a procedimiento remoto]] · [[Modelo-Vista-Controlador]] |
| Centrada en datos | 🟡 **nombrada y clasificada** en dos catálogos (capturas_U2_F2 30 y 30-cc), sin desarrollo → [[Catálogo de estilos arquitectónicos]] |
| Basada en eventos | 🟡 **nombrada** (EDA en la lista de 9; *Event-based* en el árbol C&C), sin desarrollo |
| Arquitectura candidata · arquitectura de referencia | ✅ capturas_U2_F2 23-26 → [[Arquitectura de referencia]]. De candidata solo hay la tabla de cuatro tipos, sin definición textual |
| Estilo vs. patrón · patrones de diseño y arquitectónicos | ✅ capturas_U2_F2 0-8 y 14-22 → [[Estilos arquitectónicos]] §1, [[Patrones arquitectónicos]], [[Patrones de diseño]] |
| *(fuera del programa)* Monolítica | ✅ → [[Arquitectura monolítica]] |

> [!warning] Desfase de numeración
> El estudiante rotuló estas capturas como **unidad 2**, pero su contenido es el de los puntos
> **1.4, 1.5, 1.7 y 1.9** de la unidad 1 del programa. La unidad 2 del programa (**Calidad del
> Software**) recibió su teoría de clase recién el 2026-10-16, en `capturas_U3_F1`. Pregunta abierta para ella: qué entra en el
> segundo parcial (19 de septiembre).

### Unidad 2 — Calidad del Software ✅

**Llegó la teoría de clase el 2026-10-16** (`capturas_U3_F1` 0-25: la carpeta dice U3, el contenido
es esta unidad). Antes solo estaba el ejemplo READM (2026-10-12) y el complemento del SAIP.

| # | Punto | Estado |
|---|---|---|
| 1 | Conceptos generales | ✅ [[Calidad del software]]: definición de clase, Garvin, ISO 9000:2000 |
| 2 | ¿Por qué es importante? | ✅ [[Calidad del software]] §2-§4: los números del problema y las fuentes de errores (56 % requerimientos) |
| 3 | **Normas ISO** | ✅ [[Norma ISO 9126]] (definición, McCall y Boehm, seis características con tablas y rueda) y [[Familia de normas ISO 25000]] (cinco divisiones). La 25010 sigue siendo complemento |
| 4 | **Atributos de calidad**: funcionalidad, fiabilidad, usabilidad, eficiencia, mantenibilidad, portabilidad | ✅ [[Norma ISO 9126]] §4-§5 |
| 4 bis | y otros atributos **no observables vía ejecución** | ✅ [[Atributos observables y no observables vía ejecución]] (Bass 1998: árbol y tabla) |
| — | Escenarios de calidad (EAC) | ✅ [[Escenarios de calidad]] (teoría y tres ejemplos) + [[Ejemplo resuelto - Sistema de Transporte READM]] §5 (tabla `EAC-nn`) |

[[Atributos de calidad]] queda como **complemento** (SAIP): taxonomías comparadas, tradeoffs y
escenarios generales vs concretos.

### Unidad 3 — Arquitectura en el Ciclo de Vida 🟢

**El 2026-10-16 llegaron láminas de clase** (`capturas_U3_F1` 35-45 y `capturas_U3_F3`, 14).

| Tema | Estado |
|---|---|
| Arquitectura en las metodologías: enfoque predictivo y ágil (SCRUM) | ✅ **de clase**: [[Metodologías predictivas y ágiles]] (factores, cascada, ágil, valor, roles) y [[Proceso Scrum en la arquitectura de software]] (sprint, ceremonias, los 14 pasos con la arquitectura base y su refinamiento). + NT1 [[Arquitectura de software en el modelo en espiral]], NT3 [[Arquitectura ágil]] y [[Requisitos significativos para la arquitectura]] |
| Integrando con la arquitectura de la información | ✅ [[Arquitectura de la información]] (NT2 + láminas de inventario, mapa y diagrama funcional) y [[Arquitectura empresarial]] (los cuatro dominios, de clase) |
| Documentando la arquitectura de software | 🟡 — [[Ciclo de desarrollo de la arquitectura]] (la documentación cae en Diseño) + [[Estructuras y vistas arquitectónicas]] + [[El ciclo del architecting]] §4 |
| Implementación y pruebas | 🟡 — [[Ciclo de desarrollo de la arquitectura]] (implementación en Construcción; pruebas sin etapa de arquitectura) y el *modelo del CV guiado por arquitecturas* + [[Arquitectura dirigida por modelos MDA]] (NT1) |
| Evaluación de la arquitectura | 🟡 — de clase solo su lugar en el ciclo ([[Ciclo de desarrollo de la arquitectura]], [[Proceso general de diseño de la arquitectura]]); el método está en [[Evaluación de la arquitectura]] (complemento: ATAM) |


Lo que sí es **de clase** es [[Arquitectura en el ciclo de vida del software]], que corresponde a la
diapositiva "¿Dónde debe colocarse la arquitectura en el ciclo de vida?" — es una parte, no la
unidad completa. Todo lo demás de esta unidad es **complemento** y hay que validarlo contra la
presentación cuando llegue.

> [!note] La arquitectura de la información ya tiene fuente
> Era el único punto del programa sin ninguna fuente. El 2026-10-16 llegó la **NT2**, *La
> Arquitectura de la Información en el CCV*, y lo cubre entero: [[Arquitectura de la información]].
> Las tres notas técnicas de la unidad 3 son **material de clase**: NT1 (MDA y espiral), NT2 (AI)
> y NT3 (arquitectura ágil).

### Unidad 4 — Arquitectura y Negocios ❌

"Aplicaciones con casos". Sin material todavía.

---

## Lo que falta pedir

Las presentaciones y capturas que tengo cubren **1.1–1.8** y 1.9 casi entero (actualizado 2026-09-17). Para el resto necesito material:

| Prioridad | Qué falta | Para cuándo |
|---|---|---|
| Media | **1.9 lo que faltó**: centrada en datos y basada en eventos desarrolladas, on premise, y una definición textual de arquitectura candidata | cuando se dé |
| Media | Unidad 2 completa — Calidad del Software | 25 de agosto al 7 de septiembre |
| Baja | Unidades 3 y 4 | septiembre y octubre |

---

## Bibliografía oficial

- *Essential Software Architecture* — Ian Gorton
- *Just Enough Software Architecture* — George Fairbanks
- *Head First Design Patterns* — Freeman, Freeman, Bates, Sierra
- *Software Systems Architecture: working with stakeholders using viewpoints and perspectives* — Rozanski, Woods
- *Software Performance and Scalability: a quantitative approach* — Henry H. Liu
- *Software Architecture Patterns*, 2ª ed. — Mark Richards
- *Software Quality Engineering* — Jeff Tian
- *Software Architecture in Practice* — Bass, Clements, **Kazman**

### Qué nota se apoya en qué libro

Revisión honesta de si el complemento de la bóveda cae **dentro** de la bibliografía oficial:

| Fuente usada | ¿Está en la bibliografía? | Qué sostiene |
|---|---|---|
| *Software Architecture in Practice* 4ª ed. | ✅ **sí** (n° 8) | [[Atributos de calidad]], [[Tácticas y patrones arquitectónicos]], [[Evaluación de la arquitectura]], [[El ciclo del architecting]], [[Stakeholders]], [[Guía - Drivers de calidad y restricción]] |
| Reynoso, *Introducción a la Arquitectura de Software* | ❌ no | [[Estilos arquitectónicos]], parte de [[Arquitectura y proceso de desarrollo]] §7 |
| Garland & Anthony, *Large-Scale Software Architecture* | ❌ no | [[Arquitectura y proceso de desarrollo]] §1–6, [[Modelo 4+1 vistas]] |
| ISO/IEC/IEEE 42010, 29148 | ❌ no (son normas, no libros) | [[Estructuras y vistas arquitectónicas]], [[Matriz de trazabilidad de requisitos]] |

> [!tip] Lo que esto cambia al escribir una entrega
> Cuando haya que justificar una clasificación, **citá primero el SAIP**: es el único complemento que
> está en la bibliografía oficial, así que es el más defendible. Reynoso y Garland son buenos para
> entender, pero no son autoridad en este curso.

> [!warning] Tres libros de la bibliografía que faltan en disco y conviene tener
> - **Rozanski & Woods**, *Software Systems Architecture: working with stakeholders using viewpoints
>   and perspectives* — es **el** libro de stakeholders y de *perspectivas*. Ataca directo el
>   criterio 2 del Caso 1 (25 pts) y aporta las clases de stakeholder que hoy salen del SAIP.
> - **Fairbanks**, *Just Enough Software Architecture* — diseño guiado por riesgo; es el origen de
>   "cuánta arquitectura es suficiente".
> - **Mark Richards**, *Software Architecture Patterns* 2ª ed. — catálogo de estilos, para validar
>   [[Estilos arquitectónicos]] contra una fuente oficial en vez de Reynoso.

> [!note] Dos de estos ya aparecen en clase
> **Bass/Clements/Kazman** es la fuente de la definición de arquitectura que está en
> [[Arquitectura de software]] ("la estructura de estructuras..."), y el PDF
> el libro está **en la bóveda**, en
> `00-Fuentes/lecturas/Bass, Clements, Kazman - Software Architecture in Practice 4a ed.pdf`.
> Es el único libro de la bibliografía oficial que viaja con el repo, justamente porque es el que
> las notas citan.
> Rozanski y Woods es de donde sale el vocabulario de **vistas y perspectivas** de
> [[Estructuras y vistas arquitectónicas]].

---

## El laboratorio

El programa de laboratorio de AYD2 (785) cubre, además: administración de la configuración
(control de versiones, integración continua), entrega continua, **pruebas** (unitarias, de
integración, de sistema, de aceptación de requerimientos funcionales y no funcionales),
arquitectura de software (**por capas, 4+1 vistas, MVC**), arquitecturas orientadas al servicio
(SOA, web services, cloud) y **patrones de diseño** (creación, estructura, comportamiento).

Dos cosas que conectan con lo que ya tengo:

- **4+1 vistas** aparece explícitamente en el laboratorio → [[Modelo 4+1 vistas]].
- **Pruebas de aceptación de requerimientos funcionales y no funcionales** es el otro extremo de
  la [[Matriz de trazabilidad de requisitos]]: son la columna "cómo se verifica".

Y en el disco ya hay una presentación de patrones (Factory, State, Strategy) en
`Unidad_1/presentacion-patrones/`, que corresponde a la unidad de patrones del laboratorio.

> [!note] Qué material del curso **no** viaja en el repo
> Estos quedaron fuera a propósito, en `AYD_2/Unidad_1/` del disco local:
>
> | Archivo | Por qué no viaja |
> |---|---|
> | `articulo.pdf` (18 MB) | contenido no identificado; nada lo cita |
> | `Guia_Arquitectura_Software.pdf` (2,7 MB) | ya está destilado en las notas; es una guía derivada, no fuente oficial |
> | `Introduccion.PDF`, `Practica 1.pdf`, `presentacion_patrones.pdf` | material de laboratorio, fuera del contenido teórico |
>
> Si alguno hace falta en la Mac, hay que copiarlo a mano o agregarlo a `00-Fuentes/lecturas/`.

---

## Notas relacionadas

- [[Índice]] — el mapa de la bóveda
- [[Matriz de trazabilidad de requisitos]] — el tema que conecta 1.6 con las unidades 2 y 3
- [[Arquitectura de software]] · [[Estructuras y vistas arquitectónicas]] · [[Modelo 4+1 vistas]]

## Preguntas de repaso

1. ¿Cuáles son las cuatro unidades del curso y cuál es la fecha de cada parcial?
2. ¿Qué punto del programa cubre "Arquitectura y Requerimientos" y por qué dice "(CDU de negocio)"?
3. ¿Cuáles son los seis estilos del catálogo del punto 1.9?
4. ¿Cuáles son los seis atributos de calidad de la unidad 2?
5. ¿Qué hace falta para tener derecho al examen final?
