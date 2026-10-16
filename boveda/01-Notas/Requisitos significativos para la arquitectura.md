---
tema: Arquitectura en el ciclo de vida
fuente: "NOTA TÉCNICA DE CLASE — NT3. «Arquitectura del SW y Metodologías Ágiles» (00-Fuentes/lecturas/), apartados «Los Requisitos de Importancia Arquitectónica» y «Estrategias de captura de RSA». La definición de la NT1 (Meaurio y Schmieder) se cita al lado."
fecha: 2026-10-16
punto_del_programa: "Unidad 3 — Arquitectura en las metodologías: enfoque predictivo y ágil"
alias: [RSA, ASR, Architecturally Significant Requirement, requisitos significantes para la arquitectura, requisito de importancia arquitectónica, requisitos de importancia arquitectónica, requisitos arquitectónicamente significativos]
---

# Requisitos significativos para la arquitectura (RSA)

Un **RSA** (*Architecturally Significant Requirement*, ASR) es un requisito que **cambia la
arquitectura**: si faltara, la arquitectura sería otra. Es el concepto en que se apoya la
[[Arquitectura ágil]].

> [!note] El nombre cambia según la nota técnica
> La NT3 los llama **«Requisitos Significantes para la Arquitectura»** en el resumen y **«Requisitos de
> Importancia Arquitectónica»** en el título del apartado. La NT1 los llama **«requerimientos
> significativos arquitectónicamente»**. Son lo mismo: la sigla **RSA** es la de la NT3.

## 1. La definición

La NT3 da dos, y conviene citar las dos:

> *"Un Requisito de Importancia Arquitectónica es un requisito que tendrá un importante efecto en la
> arquitectura, y que como se dijo, si están ausentes, la arquitectura resultante será totalmente
> diferente."*

> Tomando la definición de Chen, Babar y Nuseibeh (2013), los RSA *"son aquellos requisitos que tienen
> un impacto medible en una arquitectura de sistemas de software"*.

Y la consecuencia: *"no sería posible diseñar una arquitectura adecuada, si no se elicitan
adecuadamente los RSA"*.

| Fuente | Cómo los define |
|---|---|
| **NT1** (Meaurio y Schmieder) | *"aquellos que tienen un impacto **esencial** sobre la arquitectura"* |
| **NT3**, con Chen | *"un impacto **medible**"* |
| **NT3**, prueba de ausencia | si faltan, *"la arquitectura resultante será totalmente diferente"* |

**Regla memorizable:** *un RSA es el que, si lo sacás, cambia el dibujo.*

## 2. Para qué existe

Para no tratar **todos** los requisitos igual. *"Algunos requisitos tienen un efecto mucho más
profundo en la arquitectura que otros"*: los RSA son esos, y son los que hay que encontrar **antes**
de decidir la arquitectura. En ágil, donde se evita el trabajo inicial grande, son **lo mínimo** que
no se puede dejar para después.

> [!important] Es la misma idea que los drivers de clase
> Los [[Drivers arquitectónicos]] son *"los factores críticos que guían el diseño"* y *"determinan su
> estructura fundamental"*. Un RSA es un driver visto desde los requisitos. Y la NT3 confirma lo que
> enseña la clase: **no son solo los no funcionales**. *"Los RSA generalmente toman la forma de
> requisitos no funcionales, pero en algunos casos también toman la forma de requisitos
> funcionales"*: los drivers de tipo **RF** del curso.

## 3. La trampa: los RSA no son «los no funcionales»

La NT3 parte de la división de siempre:

| Tipo | Qué especifica |
|---|---|
| **Funcional** | *"las características deseadas de un sistema"* |
| **No funcional** | *"las propiedades requeridas de un sistema"*: atributos de calidad, seguridad, disponibilidad, restricciones del sistema, metas, características de usabilidad |

El error es igualar RSA con no funcional. **Hay no funcionales que no son RSA y funcionales que
sí lo son.** La pregunta que decide no es *«¿es funcional?»* sino *«¿cambia la arquitectura?»*.

## 4. Por qué cuesta encontrarlos: tres propiedades

| Propiedad | Qué quiere decir, según la NT3 |
|---|---|
| **Subjetivos** | *"pueden ser vistos, interpretados y analizados de manera diferente por diferentes personas y en diferentes contextos"* |
| **Relativos** | *"la importancia de cada RSA se determina a veces a partir de su relación con otros RSA en un contexto dado"* |
| **Interactúan entre ellos** | *"al intentar alcanzar un RSA particular, puede a su vez afectar (en forma favorable o desfavorable) a otros RSA"* |

Además:

- son **más difíciles de comprender** que los funcionales, así que *"pasan desapercibidos o no
  obtienen suficiente atención por adelantado"*, y eso se acentúa en ágil;
- son **difíciles de validar** cuando el proyecto ya terminó;
- identificarlos *"lleva mucho trabajo y es poco clara para los que no son expertos en
  arquitecturas"*.

**Quiénes intervienen** en identificarlos y especificarlos: *"las principales partes interesadas del
sistema, como los usuarios finales, los desarrolladores, los administradores y los mantenedores"*
(→ [[Stakeholders]]).

> [!note] «Interactúan entre ellos» es el tradeoff
> Que alcanzar un RSA afecte a otro es lo que en [[Evaluación de la arquitectura]] se llama
> **tradeoff**, y lo que la NT1 de trazabilidad (unidad 1) llama **requisitos en conflicto**.

## 5. Cómo se capturan

**Las estrategias de Chen**, sacadas de un estudio empírico con expertos:

| Estrategia | Cómo funciona |
|---|---|
| **Categorizar las decisiones de diseño** | se arman tablas resumidas con las decisiones que el arquitecto tiene que tomar, y se recorre la lista de requisitos buscando cuál afecta a cada tipo de decisión. *"Si un requisito afecta a alguna decisión de diseño, es por definición un RSA"* |
| **Entrevistas a interesados** | preguntar a los stakeholders |
| **Comprensión de objetivos de negocios** | los objetivos del negocio señalan qué requisitos pesan |

**La de Babar y otros, y la de Bass, Clements y Kazman:** usar **escenarios** para caracterizar los
atributos, *"en particular los de calidad"*, y aproximaciones basadas en *frameworks* de evidencias.

> [!important] Los escenarios ya los sabés hacer
> Es el escenario de **seis partes** del curso: fuente de estímulo, estímulo, artefacto, entorno,
> respuesta y medida de la respuesta (→ [[Ejemplo resuelto - Sistema de Transporte READM]]). Y la
> estrategia de Chen es, en la práctica, la prueba que ya usás: si el requisito no mueve ninguna
> decisión de diseño, no es driver.

**El límite:** *"las consideraciones sobre requisitos RSA no alcanzan a especificar la totalidad
sobre las arquitecturas"*. Los RSA dicen **qué** guía el diseño; diseñar sigue siendo otro trabajo.

## 6. El método, corrido sobre un ejemplo

Ejemplo propio, no de la NT3. Para un sistema de citas médicas, tres requisitos:

| Requisito | ¿Mueve una decisión de diseño? | ¿RSA? |
|---|---|---|
| *El paciente reserva una cita desde el celular* | sí: obliga a una capa de presentación móvil y a un servicio expuesto | **sí**, y es **funcional** |
| *La reserva responde en menos de 2 s con 5.000 usuarios simultáneos* | sí: caché, escalado horizontal | **sí**, no funcional |
| *El botón de confirmar es verde* | no: ninguna estructura cambia | **no**, aunque sea no funcional (usabilidad) |

Fijate en la tercera fila: es **no funcional y no es RSA**. Y la primera es **funcional y sí lo es**.

## Checklist

- [ ] ¿Cada RSA pasa la prueba de ausencia (sin él, la arquitectura sería otra)?
- [ ] ¿Revisé también los **funcionales**, no solo los no funcionales?
- [ ] ¿Los de calidad están escritos como **escenario con medida**?
- [ ] ¿Anoté qué RSA se afectan entre sí (tradeoffs)?
- [ ] ¿Salieron de los stakeholders y de los objetivos del negocio, no de mi cabeza?

## Notas relacionadas

- [[Arquitectura ágil]] — donde los RSA son el concepto central
- [[Drivers arquitectónicos]] — la versión de clase
- [[Arquitectura de software en el modelo en espiral]] — la NT1, que los ubica en la vuelta del plan de desarrollo
- [[Atributos de calidad]] — los no funcionales que suelen ser RSA
- [[Stakeholders]] — quiénes los identifican

## Preguntas de repaso

1. ¿Qué es un RSA? Dá la definición de Chen y la prueba de ausencia.
2. ¿Un RSA es siempre un requisito no funcional? Justificá con la NT3.
3. ¿Qué significa que los RSA sean subjetivos, relativos y que interactúen entre ellos?
4. Explicá la estrategia de Chen de categorizar las decisiones de diseño.
5. ¿Qué relación hay entre los RSA y los drivers arquitectónicos de clase?
