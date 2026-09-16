---
tema: Arquitectura de software
fuente: "Presentación de clase — capturas_U2 (5, 6, 7, 8). NÚCLEO. La correspondencia con el ciclo de influencias y con los drivers es lectura propia, marcada."
fecha: 2026-09-15
alias: "que se tiene en cuenta, embudo del diseño, requisitos contexto experiencia, contexto del diseño"
punto_del_programa: "1.5 — ¿Qué se tiene en cuenta para el diseño?"
---

# Qué se tiene en cuenta para el diseño

En corto: **el diseño arquitectónico es un embudo con tres entradas y una salida.** Entran los
**requisitos**, el **contexto** y la **experiencia del arquitecto**; sale el **documento de diseño
arquitectónico**.

Es la respuesta de clase al punto **1.5** del programa, con cuatro diapositivas seguidas: una que da el
embudo y tres que abren cada entrada (los títulos cambian la palabra en **rojo**: *Requisitos*,
*Contexto*, *Arquitecto*).

## 1. El embudo

La diapositiva *"¿Qué se tiene en cuenta para el diseño?"* dibuja un embudo con tres círculos adentro y
una flecha hacia abajo:

| Elemento de la diapositiva | Qué es |
|---|---|
| Círculo **Requisitos** | entrada 1 |
| Círculo **Contexto** | entrada 2 |
| Círculo **Experiencia del arquitecto** | entrada 3 |
| Flecha de salida → **"Documento de diseño arquitectónico (Arquitectura Software)"** | el producto |

![[adjuntos/capturas-clase-U2/diseno-arquitectonico/que-se-tiene-en-cuenta-embudo.png]]

> [!important] La salida tiene nombre
> El producto no es "la arquitectura" en abstracto: es un **documento de diseño arquitectónico**. Es el
> mismo artefacto que RUP le pide al arquitecto (el *documento de descripción de arquitectura*, →
> [[Arquitecto de software]]) y el que "suele incluir varias vistas" (→ [[Proceso de diseño arquitectónico]]
> §"¿Qué información incluye?").

Los tres círculos se **solapan** en el dibujo: no son canastas separadas. Un mismo hecho (por ejemplo,
"hay que mantener la base de datos existente") puede venir de un stakeholder, del contexto
organizacional y de una mala experiencia del arquitecto a la vez.

## 2. Requisitos — lo que piden los stakeholders

La diapositiva *"¿Qué se tiene en cuenta para el diseño? **Requisitos**"* no trae texto propio: trae la
caricatura de los cinco stakeholders, en su versión original en inglés. Leída con zoom:

| Stakeholder (texto de la diapositiva) | Lo que pide (textual) | En español |
|---|---|---|
| *Development organization's management stakeholder* | *"Low cost, keeping people employed, leveraging existing corporate assets!"* | bajo costo, mantener a la gente empleada, **aprovechar los activos existentes** de la empresa |
| *Marketing stakeholder* | *"Neat features, short time to market, low cost, parity with competing products!"* | características vistosas, poco tiempo al mercado, bajo costo, **paridad con la competencia** |
| *End user stakeholder* | *"Behavior, performance, security, reliability!"* | comportamiento, rendimiento, seguridad, fiabilidad |
| *Maintenance organization stakeholder* | *"Modifiability!"* | modificabilidad |
| *Customer stakeholder* | *"Low cost, timely delivery, not changed very often!"* | bajo costo, entrega a tiempo, que no cambie muy seguido |
| *Architect* (abajo, con los brazos en la cabeza) | *"Ohhhhh..."* | — |

![[adjuntos/capturas-clase-U2/diseno-arquitectonico/que-se-tiene-en-cuenta-requisitos-stakeholders.png]]

La lección es la misma que en [[Stakeholders]] y [[Beneficios de la arquitectura de software]]: **los
requisitos llegan en conflicto**. Casi todos piden bajo costo, pero el usuario final pide rendimiento y
seguridad y mantenimiento pide modificabilidad. De ahí sale el trabajo de
[[Equilibrio de restricciones del proyecto]].

> [!warning] Esta versión dice un poco más que la de las notas viejas
> La versión en español de *Arquitectura de Software.pdf* (la que está en [[Stakeholders]]) **no trae**
> *"leveraging existing corporate assets"* ni *"parity with competing products"*, y **agrega**
> *usabilidad* al usuario final. La original en inglés no dice *usability*. Si te lo preguntan, las dos
> son de clase; esta es la más completa en lo que pide la gerencia y marketing.

## 3. Contexto — lo que rodea al proyecto

Es la diapositiva más cargada de las cuatro: cuatro grupos, cada uno con ejemplos. Textual:

- **Aspectos del negocio:**
  - Amortizar la infraestructura.
  - Mantener bajos costes de instalación.
  - Utilizar personal disponible, etc.
- **Aspectos de la estructura organizacional:**
  - Promoción de los intereses creados, ej. mantener una BD existente.
  - Mantener el método estándar de hacer negocio, etc.
- **Tendencias actuales:**
  - Desplegar la aplicación en la nube.
  - Interfaz para aplicaciones móviles, etc.
- **Tecnología disponible:** sistema centralizado vs distribuido, desarrollo desde cero vs. uso de
  servicios externos, etc.

![[adjuntos/capturas-clase-U2/diseno-arquitectonico/que-se-tiene-en-cuenta-contexto.png]]

Para memorizarlo: **N-O-T-T** — **N**egocio, **O**rganización, **T**endencias, **T**ecnología.

> [!tip] "Intereses creados" no es un insulto
> *Promoción de los intereses creados* quiere decir que dentro de la organización hay gente o áreas que
> **ya invirtieron** en algo y lo van a defender. El ejemplo de ella es *mantener una BD existente*: aunque
> técnicamente convenga otra, la arquitectura tiene que convivir con esa. En FarmaHosp es exactamente el
> choque Java/Oracle interno vs. Python/PostgreSQL de la consultora.

### Lectura propia: el contexto son drivers de restricción

*(Esto no está en la diapositiva: es un puente con [[Drivers arquitectónicos]], que sí es de clase.)*

Casi todo lo que la diapositiva llama "contexto" es, en el vocabulario de drivers, una **restricción**:
una condición impuesta desde afuera que limita las decisiones.

| Ejemplo de la diapositiva "Contexto" | Categoría de restricción (drivers) |
|---|---|
| Amortizar la infraestructura · bajos costes de instalación | de negocio / presupuesto |
| Utilizar personal disponible | organizacional |
| Mantener una BD existente | organizacional, y a menudo de integración |
| Mantener el método estándar de hacer negocio | organizacional |
| Desplegar en la nube · interfaz para móviles | tecnológica (si es impuesta) — o una opción de diseño (si no lo es) |
| Centralizado vs. distribuido · desde cero vs. servicios externos | **no es restricción**: es una **decisión** que el arquitecto toma |

La última fila es la trampa: *"tecnología disponible"* no te impone nada, **te abre opciones** entre las
que elegir.

## 4. Experiencia del arquitecto

La diapositiva *"¿Qué se tiene en cuenta para el diseño? **Arquitecto**"* es una foto de alguien
dibujando un diagrama en un vidrio, con este texto:

> Los arquitectos desarrollan su modo de pensar a partir de experiencias anteriores.
> - Experiencias anteriores buenas darán lugar a replicar esos diseños.
> - Las experiencias anteriores malas se evitarán en el nuevo diseño.

![[adjuntos/capturas-clase-U2/diseno-arquitectonico/que-se-tiene-en-cuenta-experiencia-arquitecto.png]]

Consecuencia directa: **dos arquitectos con los mismos requisitos y el mismo contexto pueden producir
arquitecturas distintas**, y las dos pueden ser defendibles. Es la misma idea que cierra el
[[Ciclo de influencias en la arquitectura]].

## 5. Cómo encaja con las otras dos diapositivas parecidas

*(Correspondencia propia; las tres fuentes son de clase.)*

La clase dijo esto mismo **tres veces**, con distinto nombre. No se contradicen:

| Embudo (esta nota) | [[Ciclo de influencias en la arquitectura]] | [[Arquitectura en el ciclo de vida del software]], punto 7 |
|---|---|---|
| **Requisitos** | Stakeholders | *(puntos 1 y 3: requisitos, stakeholders)* |
| **Contexto** | Organizaciones de desarrollo + Ambiente técnico | Organización + Entorno |
| **Experiencia del arquitecto** | Experiencia del arquitecto | Experiencia |

Lo que agrega el embudo: la **salida con nombre** (documento de diseño arquitectónico) y el detalle del
contexto con **ejemplos concretos**. Lo que agrega el ciclo: que **el sistema construido retroalimenta**
a las entradas.

## Notas relacionadas

- [[Ciclo de influencias en la arquitectura]] — la misma idea como ciclo
- [[Stakeholders]] — de dónde salen los requisitos
- [[Drivers arquitectónicos]] — requisitos y contexto convertidos en drivers
- [[Arquitecto de software]] — quién pone la experiencia
- [[Proceso de diseño arquitectónico]] — qué contiene el documento que sale del embudo
- [[Equilibrio de restricciones del proyecto]]

## Preguntas de repaso

1. ¿Cuáles son las tres entradas del embudo y cuál es su salida?
2. Nombrá los cuatro grupos de aspectos del **contexto** y un ejemplo de cada uno.
3. ¿Qué quiere decir "promoción de los intereses creados" y qué ejemplo dio la clase?
4. Según la diapositiva, ¿qué hace un arquitecto con sus experiencias anteriores buenas y con las malas?
5. ¿Por qué "centralizado vs. distribuido" no es una restricción sino una decisión?
