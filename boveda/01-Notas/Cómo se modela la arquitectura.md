---
tema: Modelado de la arquitectura
fuente: "Presentación de clase — capturas_U2 (10). NÚCLEO. + PDF de clase «TEMA 5: Modelado de arquitectura software», pág. 3 (diagrama de clases en el diseño detallado). NÚCLEO. La comparación entre las tres formas (eje formal/informal, cuándo conviene cada una) es COMPLEMENTO, marcado."
fecha: 2026-09-15
alias: "como se modela, modelar la arquitectura, formas de modelar, adl uml bloques"
punto_del_programa: "1.7 — ¿Cómo se modela?"
---

# Cómo se modela la arquitectura

Nota **hub**: responde la pregunta de la diapositiva y manda a la nota de cada forma.

## 1. Lo que dice la clase

Diapositiva *"¿Cómo se modela?"*, textual:

> La arquitectura de un sistema software puede modelarse mediante:
> - **Lenguajes de Descripción de Arquitectura (ADLs)**
> - **Diagramas UML**
> - **Diagramas de bloque de alto nivel**

![[adjuntos/capturas-clase-U2/diseno-arquitectonico/como-se-modela-tres-formas.png]]

Son **tres formas**, en ese orden, y cada una tiene después su propia diapositiva:

| # | Forma | Qué es, en una línea | Nota |
|---|---|---|---|
| 1 | **ADLs** | lenguajes **textuales formales** que describen la arquitectura en términos de **componentes y conectores** | [[Lenguajes de descripción de arquitectura]] |
| 2 | **Diagramas UML** | lenguaje **gráfico estándar**, en dos familias: **estructurales** (componentes, despliegue…) y de **comportamiento** (actividad, secuencia…) | [[Diagramas UML estructurales y de comportamiento]] |
| 3 | **Diagramas de bloque de alto nivel** | dibujos de cajas y líneas, **sin notación estándar**, para dar la visión general | [[Diagrama de bloques de alto nivel]] |

Los diagramas UML concretos que usa la clase para la arquitectura:

- [[Diagrama de componentes]] — cómo se divide el software en piezas reemplazables.
- [[Diagrama de despliegue]] — sobre qué nodos físicos corre cada pieza.
- [[Diagrama de secuencia]] — cómo se comunican las piezas en el tiempo.

> [!important] La conexión con "qué incluye el diseño"
> La clase dijo antes que el diseño de la arquitectura incluye **estructura** (*"subsistemas como
> composición de componentes"*) y **comportamiento** (*"comunicación entre componentes"*) — ver
> [[Proceso de diseño arquitectónico]]. Las dos familias de UML son justamente eso: los **estructurales**
> modelan la estructura, los de **comportamiento** modelan el comportamiento.

## 2. Las tres formas comparadas — COMPLEMENTO

*(La diapositiva solo las enumera. La comparación es conocimiento general, para entender por qué
existen las tres.)*

Las tres están sobre un mismo eje: **cuánta precisión** tienen contra **quién las entiende**.

| | ADL | UML | Bloques de alto nivel |
|---|---|---|---|
| **Formato** | texto | gráfico | gráfico |
| **Formalidad** | alta: sintaxis y semántica precisas | media: notación estándar, semántica a veces laxa | baja: sin notación fija |
| **Analizable por herramienta** | sí | parcialmente | no |
| **Lo entiende un stakeholder no técnico** | no | con ayuda | sí |
| **Riesgo típico** | nadie lo lee | se usa mal la notación | cada lector entiende otra cosa |
| **Uso típico** | verificación, investigación, sistemas críticos | documentar vistas para el equipo | presentar la idea general, primeras discusiones |

```mermaid
flowchart LR
    B["Bloques de alto nivel<br/>informal, para todos"] --> U["UML<br/>semiformal, estándar"] --> A["ADL<br/>formal, analizable"]
```

*(Esquema propio: de izquierda a derecha crece la precisión y se achica el público que lo lee.)*

**No se excluyen.** Un documento de diseño arquitectónico normalmente arranca con un diagrama de bloques
para dar la idea, y después baja a UML por vista (→ [[Modelo 4+1 vistas]]). El ADL aparece solo si hace
falta verificar formalmente.

## 3. La trampa

Creer que "modelar la arquitectura" es **hacer un diagrama de clases**. El diagrama de clases es del
**diseño detallado** (el PDF de clase lo pone *"durante el diseño detallado para modelar los principales
elementos del código"*), y la clase ya marcó que la arquitectura se diseña **antes** del diseño detallado
(→ [[Arquitectura en el ciclo de vida del software]]). Los ejemplos que la diapositiva de UML da para la
arquitectura son otros: **componentes** y **despliegue** (estructurales), **actividad** y **secuencia**
(comportamiento).

## Notas relacionadas

- [[Lenguajes de descripción de arquitectura]]
- [[Diagramas UML estructurales y de comportamiento]]
- [[Diagrama de bloques de alto nivel]]
- [[Diagrama de componentes]] · [[Diagrama de despliegue]] · [[Diagrama de secuencia]]
- [[Modelo 4+1 vistas]] — qué diagrama va en cada vista
- [[Proceso de diseño arquitectónico]] — qué información tiene que quedar modelada

## Preguntas de repaso

1. ¿Cuáles son las tres formas de modelar una arquitectura según la clase?
2. ¿Cuál de las tres es textual y cuál no tiene notación estándar?
3. ¿Qué familia de diagramas UML modela la *estructura* y cuál el *comportamiento*? Dá dos ejemplos de cada una.
4. ¿Por qué el diagrama de clases no es el diagrama típico para modelar la arquitectura?
5. ¿En qué situación preferirías un diagrama de bloques de alto nivel antes que UML?
