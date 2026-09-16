---
tema: Modelado de arquitectura — diagramas UML
fuente: "Presentación de clase — capturas_U2 (23, 24, 29, 30, 31, 32, 33, 54). NÚCLEO. + PDF TEMA 5, págs. 2-3."
fecha: 2026-09-15
---

# Flashcards — Diagrama de componentes

Compatible con el plugin **Spaced Repetition** de Obsidian: cada tarjeta es una línea con la
pregunta, el separador de dos signos de dos puntos, y la respuesta.

Salen de [[Diagrama de componentes]] y [[Interfaces de componentes]].

#flashcards/componentes

Según la diapositiva, ¿qué describen los diagramas de componentes?::Los **elementos físicos y sus realizaciones** en el entorno. Muestran las opciones de realización incluyendo código fuente, binario y ejecutable.

¿Cuál es la relación entre un componente y una clase?::El componente es la **personificación en software de una clase**. La clase es una abstracción de atributos y operaciones, y **un componente puede ser la implementación de más de una clase**.

¿Cuáles son los tres tipos de componentes?::**De distribución** (DLL, ejecutables, controles ActiveX, Java, Webservices), **para trabajar en el producto** (archivos de base de datos y de código a partir de los cuales se crean los de distribución) y **de ejecución** (creados como resultado de un sistema en ejecución).

¿Qué dos tipos de interfaz tiene un componente y cómo se dibujan?::**Provista** (provides): círculo completo, el componente ofrece el servicio. **Requerida** (required): semicírculo, el componente necesita el servicio.

¿Por qué las interfaces son importantes para un componente?::Porque permiten que el componente sea **reusable y reemplazable**: quien lo usa solo conoce la interfaz.

En el PDF del TEMA 5, ¿qué es una interfaz "de entrada" y una "de salida"?::De **entrada** = **requerida** (servicios que el componente necesita). De **salida** = **proporcionada** (servicios que el componente ofrece).

¿Qué diferencia hay entre la forma icónica y la expandida de una interfaz?::**Icónica**: la interfaz es un símbolo (círculo o semicírculo). **Expandida**: la interfaz es una caja con el estereotipo «interface» y sus operaciones.

En forma expandida, ¿cómo se relacionan con la interfaz el componente que la implementa y el que la usa?::El que la **implementa**: línea punteada con **triángulo hueco**. El que la **usa**: línea punteada con **punta abierta** y «use».

¿Qué operaciones de una clase pasan a la interfaz de su componente?::Solo las **públicas (+)**. En el ejemplo Dictionary, `Spell_check` y `Synoyms` pasan a la interfaz, y `Add Words` (privada) queda adentro.

¿Qué diferencia hay entre ver un componente como caja negra y como caja blanca?::**Caja negra**: los detalles de implementación quedan ocultos, solo se ven sus interfaces. **Caja blanca**: se muestran los detalles internos, normalmente con un diagrama de clases o de otros componentes.
