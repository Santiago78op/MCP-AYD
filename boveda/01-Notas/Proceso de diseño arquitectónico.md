---
tema: Arquitectura de software
fuente: "Arquitectura de Software.pdf / Arquitectura de Software (1).pdf + capturas de clase del 19/08/2026 + Presentación de clase — capturas_U2 (0, 1, 2). Todo NÚCLEO."
fecha: 2026-08-19
actualizada: 2026-09-15
---

# Proceso de diseño arquitectónico

También llamado **arquitecting**: el proceso de la arquitectura del software. La presentación
lo cuenta en cuatro preguntas: *¿cuáles son los pasos?*, *¿cuál es el producto final?*,
*¿cómo me aseguro que lo hice bien?* y *¿qué permite?*

## ¿Cuáles son los pasos?

Cuatro, en este orden:

1. El diseño de la arquitectura comienza con el **diseño de los datos**.
2. Continúa con la obtención de las **representaciones de la estructura arquitectónica** del sistema.
3. Se analizan **alternativas de estilos o patrones arquitectónicos**.
4. Seleccionada la alternativa, se elabora la arquitectura con el empleo de un **método de diseño**.

```mermaid
flowchart TD
    P1["1. Diseño de los datos"] --> P2["2. Representaciones de la<br/>estructura arquitectónica"]
    P2 --> P3["3. Análisis de alternativas:<br/>estilos o patrones arquitectónicos"]
    P3 --> P4["4. Elaboración de la arquitectura<br/>con un método de diseño"]
    P4 --> PF["Producto final:<br/>modelo de arquitectura"]
```

El paso 1 sorprende a muchos: **se arranca por los datos**, no por las pantallas ni por los
módulos. Encaja con lo que dice [[Arquitecto de software]] sobre el diseñador de base de datos
creando la arquitectura de los datos, y con el arquitecto del sistema eligiendo el estilo
arquitectónico a partir de los requerimientos obtenidos durante el análisis de los datos.

![[adjuntos/arquitectura-de-software/arq-p21.png]]

## Los siete pasos, según la diapositiva "Pasos para la definición"

Además de los cuatro de arriba, la clase da una **lista de siete actividades** con el título
*"Pasos para la definición de una Arquitectura de software"*:

| # | Paso | Dónde está en la bóveda |
|---|---|---|
| 1 | **Creación del caso de negocio** para el sistema | [[Guía - Caso de negocio]] |
| 2 | **Entendimiento de los requisitos** | [[Drivers arquitectónicos]], [[Caso de uso del negocio]] |
| 3 | **Creación y selección** de la arquitectura | [[Estilos arquitectónicos]], [[Tácticas y patrones arquitectónicos]] |
| 4 | **Documentación y comunicación** de la arquitectura | [[Estructuras y vistas arquitectónicas]], [[Modelo 4+1 vistas]] |
| 5 | **Análisis o evaluación** de la arquitectura | [[Evaluación de la arquitectura]] |
| 6 | **Implementación** del sistema basado en la arquitectura | [[Arquitectura y proceso de desarrollo]] |
| 7 | **Aseguramiento** de que la implementación esté acorde a la arquitectura | ídem §3 |

![[adjuntos/capturas-clase/pasos-definicion-lista-7.png]]

> [!important] El paso 7 no es un adorno
> *"Aseguramiento de que la implementación esté **acorde** a la arquitectura"* es una actividad
> aparte de implementar. Es la **conformidad**: verificar que lo que se construyó sea lo que se
> diseñó. Sin ese paso, la arquitectura documentada y el sistema real se separan — y ahí empieza la
> deuda arquitectónica (→ [[Tácticas y patrones arquitectónicos]] §7).

### Y es un ciclo, no una lista

La otra diapositiva del mismo título lo dibuja como diagrama de actividad, con **`«precede»`** entre
etapas y una **flecha de retorno** desde implementación hasta requerimientos:

```mermaid
flowchart TD
    R["REQUERIMIENTOS<br/><i>(de la arquitectura)</i>"] -->|"«precede»"| D["DISEÑO<br/><i>(de la arquitectura)</i>"]
    D -->|"«precede»"| DOC["DOCUMENTACIÓN<br/><i>(de la arquitectura)</i>"]
    DOC -->|"«precede»"| E["EVALUACIÓN<br/><i>(de la arquitectura)</i>"]
    E -->|"«precede»"| I["IMPLEMENTACIÓN<br/><i>(de la arquitectura)</i>"]
    I -->|"«precede»<br/>vuelve a empezar"| R
```

![[adjuntos/capturas-clase/pasos-definicion-ciclo-precede.png]]

> [!warning] Corrección 2026-09-15 — la flecha de retorno es LLENA
> Leída a resolución completa (capturas_U2, 1), la flecha que vuelve de IMPLEMENTACIÓN a REQUERIMIENTOS
> es una línea **llena**, igual que las demás, con su propio **`<<precede>>`** al costado. Antes este
> esquema la dibujaba punteada: no lo es. Además el diagrama original tiene **nodo inicial** (arriba) y
> **nodo final** (abajo, después de IMPLEMENTACIÓN): el lazo no es infinito, se vuelve a empezar o se
> termina. El Mermaid de arriba es un esquema; **manda la imagen**.

**Cinco etapas y un lazo.** Eso confirma con fuente de clase lo que
[[Arquitectura en el ciclo de vida del software]] dice en palabras: *"es un proceso iterativo"*. Y se
corresponde casi uno a uno con el ciclo del SAIP que está en [[El ciclo del architecting]]:

| Clase (5 etapas) | SAIP (6 pasos) |
|---|---|
| **Requerimientos** | 1. entender el contexto + 2. elicitar los ASRs |
| **Diseño** | 3. diseñar (ADD) |
| **Documentación** | 4. documentar |
| **Evaluación** | 5. evaluar (ATAM) |
| **Implementación** | 6. realizar y sostener |

> [!tip] Ojo con el estereotipo
> Usó **`«precede»`**, no `«include»` ni `«extend»`. Es un estereotipo de **precedencia
> temporal**: "esto va antes que aquello". No confundirlo con las relaciones de casos de uso
> (→ [[Relaciones y dependencias en UML]]).

#### La misma figura, otra vez: "La etapa de diseño en la Arquitectura de Software"

En la presentación de la unidad 2 el diagrama reaparece **idéntico**, pero con otro título y otro
énfasis. Leída con zoom:

| Elemento | Qué cambia respecto de la versión anterior |
|---|---|
| Título | *"La etapa de diseño en la Arquitectura de Software"* (antes: *"Pasos para la definición de una Arquitectura de software"*) |
| Caja resaltada (relleno azul) | **DISEÑO** (antes estaba resaltada **REQUERIMIENTOS**) |
| Flecha grande a la derecha | apunta a DISEÑO con el texto **"En este capítulo"** |
| Pie de figura | *"La etapa de diseño en el ciclo de desarrollo de la arquitectura."* |
| Todo lo demás | igual: cinco cajas *(de la arquitectura)*, cinco `<<precede>>`, nodo inicial, nodo final y retorno |

![[adjuntos/capturas-clase-U2/diseno-arquitectonico/etapa-de-diseno-ciclo-precede.png]]

La lectura (propia, no la dijo así): **la unidad 1 se paró en REQUERIMIENTOS** (drivers, casos de uso del negocio, trazabilidad) y
**la unidad 2 se para en DISEÑO**. La figura funciona como mapa del curso: te dice en qué caja estás.

## El flujo de definición: las actividades son CONCURRENTES

La diapositiva *"Arquitectura del Software — Flujo de Definición"* (diagrama de actividad de
**Scott W. Ambler**, 2004-2005) muestra algo distinto y complementario: un **fork/join** — las
barras gruesas — con cuatro ramas **en paralelo**.

```mermaid
flowchart TD
    INI(("inicio")) --> F[" "]
    F --> A1["Define Architectural<br/>Requirements"]
    F --> DEC{"[initial effort]"}
    F --> A3["Define Reference<br/>Architecture"]
    F --> A4["Support Project<br/>Teams"]
    DEC -->|"sí"| A2["Define Candidate<br/>Architecture"]
    A2 --> A5["Refine Enterprise<br/>Architecture"]
    DEC -->|"no"| A5
    A1 --> J[" "]
    A5 --> J
    A3 --> J
    A4 --> J
    J --> FIN(("fin"))
```

![[adjuntos/capturas-clase/arq-flujo-de-definicion-ambler.png]]

Tres lecturas que importan:

**1. Las actividades no son una fila.** Definir requisitos, definir la arquitectura de referencia y
**dar soporte a los equipos de proyecto** ocurren **al mismo tiempo**. El arquitecto no "termina" de
diseñar y después acompaña: hace las dos cosas en paralelo.

**2. La guarda `[initial effort]` es la clave del diagrama.** Solo en el **esfuerzo inicial** se
define una **arquitectura candidata**; en las vueltas siguientes se va directo a **refinar la
arquitectura empresarial**. O sea: la arquitectura candidata es un artefacto **de arranque**, no de
cada iteración.

**3. Aparecen dos términos del punto 1.9 del programa**, y por fin con fuente:

| Término de la diapositiva | Qué es |
|---|---|
| **Define Candidate Architecture** — *arquitectura candidata* | la primera propuesta, la que se produce en el esfuerzo inicial y todavía hay que validar |
| **Define Reference Architecture** — *arquitectura de referencia* | la que sirve de patrón para varios proyectos, más estable y transversal |
| **Refine Enterprise Architecture** | la arquitectura de **toda la organización**, que cada proyecto refina |
| **Support Project Teams** | el arquitecto **acompaña** a los equipos, en paralelo con todo lo demás |

Eso da tres niveles de alcance: **candidata** (este proyecto, primera vuelta) → **de referencia**
(reutilizable entre proyectos) → **empresarial** (la organización entera).

## ¿Qué incluye el diseño de la arquitectura?

Con el mismo título *"Pasos para la definición de una Arquitectura de software"*, la unidad 2 abre con
**qué tiene que contener** el diseño. Textual:

> El diseño de la arquitectura incluye:
> - **Estructura:** descripción de subsistemas como composición de componentes.
> - **Comportamiento:** descripción de la comunicación entre componentes.
> - **Cualquier otra información que el arquitecto considere relevante:**
>   - Protocolos de comunicación, sincronización y acceso a datos.
>   - Distribución física.
>   - Puntos de variabilidad y extensión.
> - **Aspectos de seguridad.**
> - …

![[adjuntos/capturas-clase-U2/diseno-arquitectonico/que-incluye-el-diseno-arquitectura.png]]

| Contenido | Qué responde | Con qué se modela *(correspondencia propia → [[Cómo se modela la arquitectura]])* |
|---|---|---|
| **Estructura** | ¿de qué piezas está hecho? | diagramas UML **estructurales**: [[Diagrama de componentes]] |
| **Comportamiento** | ¿cómo se hablan esas piezas? | diagramas UML **de comportamiento**: [[Diagrama de secuencia]], actividad |
| Protocolos | ¿con qué reglas se comunican, sincronizan y leen datos? | notas sobre los conectores, interfaces |
| **Distribución física** | ¿en qué máquinas corre cada pieza? | [[Diagrama de despliegue]] |
| Puntos de variabilidad y extensión | ¿dónde se puede cambiar o agregar sin romper? | — (conecta con modificabilidad, → [[Atributos de calidad]]) |
| **Aspectos de seguridad** | ¿cómo se protege? | — (atributo de calidad) |

Dos cosas para marcar:

- **Estructura y comportamiento son obligatorios**; lo demás es *"cualquier otra información que el
  arquitecto considere relevante"*. O sea: el mínimo de un diseño arquitectónico son las piezas **y** cómo
  se comunican. Solo las piezas no alcanza.
- La lista termina en **"…"**: es abierta. Seguridad aparece suelta, en el primer nivel, no dentro de "otra
  información" — la diapositiva la destaca.

Y compará con el **producto final** de abajo (datos, estructura, propiedades y relaciones): dicen lo
mismo con otras palabras — *relaciones (interacciones) entre componentes* es el **comportamiento**.

## ¿Qué información incluye el diseño arquitectónico? — Las vistas

La diapositiva siguiente pone planos de una casa (plantas, fachadas, elevaciones) al lado de la figura
del **modelo 4+1**, con este texto:

> El documento de diseño arquitectónico suele incluir varias vistas. Una vista representa un aspecto
> parcial de una arquitectura software. Cada participante en el desarrollo estará interesado en una o
> varias vistas.

![[adjuntos/capturas-clase-U2/diseno-arquitectonico/informacion-diseno-vistas-4mas1.png]]

La analogía de los planos es el punto: **una casa no se documenta con un solo plano** (planta, fachada,
instalación eléctrica), y cada gremio mira el suyo. La figura, leída con zoom:

| Vista (texto de la figura) | Participante unido con una línea | Nombre en [[Modelo 4+1 vistas]] |
|---|---|---|
| **Logical View** | *Analyst; End user* | Vista Lógica |
| **Implementation View** | *Programmer* | Vista de Despliegue *(o de Desarrollo)* |
| **Process View** | *System Integrator* | Vista de Procesos |
| **Deployment View** | *System Administrator* | Vista **Física** |
| **Use Case View** (óvalo al centro, encima de las cuatro) | — | +1 Escenarios |

> [!warning] Ojo con "Deployment View"
> En esta figura **Deployment View** es la de la **distribución física** (la del administrador de sistemas),
> y la de componentes se llama **Implementation View**. La presentación de la unidad 1 llamaba *"Vista de
> Despliegue o Vista de Desarrollo"* a la de **componentes**. Son la misma estructura con nombres cruzados:
> el diagrama de **despliegue** va en la vista del **administrador de sistemas**, sea que se llame
> *Deployment View* o *Vista Física* (→ [[Modelo 4+1 vistas]], [[Diagrama de despliegue]]).

Lo nuevo que aporta esta figura respecto de la unidad 1: **a quién le sirve cada vista**. Es la idea de
[[Estructuras y vistas arquitectónicas]] (cada stakeholder necesita ver el sistema de una manera) con
nombres propios.

## ¿Cuál es el producto final?

Un **modelo de arquitectura** que incluye:

- Los **datos** y la **estructura** del software.
- Las **propiedades** y **relaciones** (interacciones) que hay entre los componentes.

Fijate que es exactamente lo que piden las definiciones de [[Arquitectura de software]]:
componentes + propiedades externamente visibles + relaciones.

![[adjuntos/arquitectura-de-software/arq-p22.png]]

## ¿Cómo me aseguro que lo hice bien? — Comprobaciones

> En cada etapa se revisan los productos del trabajo del diseño del software para que sean
> **claros, correctos, completos y consistentes** con los requerimientos y entre sí.

Cuatro criterios, y ojo con el último: consistentes **con los requerimientos** *y* **entre sí**.
No basta que cada documento sea correcto por separado; tienen que no contradecirse. Esto es
verificación y validación aplicada al diseño.

![[adjuntos/arquitectura-de-software/arq-p23.png]]

## ¿Qué permite?

1. **Analizar la efectividad** del diseño para cumplir los requerimientos establecidos.
2. **Considerar alternativas arquitectónicas** en una etapa en la que hacer cambios al diseño
   todavía es relativamente fácil.
3. **Reducir los riesgos** asociados con la construcción del software.

El punto 2 es el argumento económico de todo el tema: el costo de cambiar crece con el tiempo,
así que el momento de probar alternativas es *ahora*, en el diseño, no en la construcción.
Es la misma idea del criterio de Booch — arquitectura es lo que sale caro cambiar.

![[adjuntos/arquitectura-de-software-v1/arqv1-p20.png]]

## Un ejemplo real

La presentación muestra un diagrama de una solución sobre **Amazon Web Services**, con el
modelo de datos aparte. Sirve para ver que el producto final no es un texto: es un conjunto de
diagramas de componentes y servicios con sus interacciones.

![[adjuntos/arquitectura-de-software-v1/arqv1-p18.png]]

## Notas relacionadas

- [[Arquitectura de software]]
- [[Arquitecto de software]]
- [[Beneficios de la arquitectura de software]]
- [[Modelo 4+1 vistas]]
- [[Arquitectura en el ciclo de vida del software]]
- [[Equilibrio de restricciones del proyecto]]
- [[Qué se tiene en cuenta para el diseño]] — las entradas del documento de diseño
- [[Cómo se modela la arquitectura]] — con qué se representa lo que el diseño incluye

## Preguntas de repaso

1. Enumerá los cuatro pasos del diseño arquitectónico en orden.
2. ¿Por qué el proceso comienza con el diseño de los datos?
3. ¿Qué cuatro propiedades se revisan en las comprobaciones de cada etapa?
4. ¿Qué incluye el modelo de arquitectura que es el producto final?
5. ¿Por qué conviene considerar alternativas arquitectónicas temprano?
6. Según la clase, ¿qué incluye el diseño de la arquitectura? ¿Cuáles dos contenidos son el mínimo?
7. En la figura 4+1 de la unidad 2, ¿qué participante corresponde a cada vista, y en cuál va el diagrama de despliegue?
