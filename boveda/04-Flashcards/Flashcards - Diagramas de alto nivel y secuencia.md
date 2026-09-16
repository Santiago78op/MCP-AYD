---
tema: Modelado de la arquitectura
fuente: "Presentación de clase — capturas_U2 (12-20) + PDF de clase «TEMA 5: Modelado de arquitectura software», págs. 1 y 6-8. NÚCLEO."
fecha: 2026-09-15
---

# Flashcards — Diagramas de alto nivel y secuencia

Compatible con el plugin **Spaced Repetition** de Obsidian: cada tarjeta es una línea con la
pregunta, el separador de dos signos de dos puntos, y la respuesta.

Salen de [[Diagramas UML estructurales y de comportamiento]], [[Diagrama de bloques de alto nivel]]
y [[Diagrama de secuencia]].

#flashcards/modelado

¿En qué dos familias divide la clase los diagramas UML?::**Estructurales** (estático: componentes, despliegue, clases, paquetes, objetos) y de **comportamiento** (dinámico: actividad, secuencia, casos de uso).

Según la clase, ¿qué son los diagramas de alto nivel?::Describen la arquitectura con un **alto nivel de abstracción**. Suelen ser el **primer paso antes de un diseño más detallado** (ej. con diagramas de componentes).

¿Qué es un diagrama de bloques, según la diapositiva?::La representación del funcionamiento de un sistema mediante **bloques y sus relaciones**, que definen la organización de todo el proceso interno, **sus entradas y sus salidas**.

¿Qué es SCADA?::Un sistema de **control y adquisición de datos** para supervisar y controlar **procesos industriales en tiempo real**: red de dispositivos y software que recopila datos de sensores y equipos de campo, los transmite a un sistema central y permite a los operadores ajustar a distancia.

¿Qué atributo de calidad ilustra el ejemplo Multi-AZ de AWS y con qué mecanismos?::**Disponibilidad** (tolerancia a fallos para bases de datos en producción): recuperación de fallo automática, replicación síncrona, habilitado con un solo clic.

¿Para qué integrar SCADA con la nube, según la diapositiva?::Para mejorar la **escalabilidad**, la **accesibilidad** y la **rentabilidad**.

¿Qué muestra un diagrama de secuencia, según el TEMA 5?::La **interacción de un conjunto de objetos** a través del **tiempo**: objetos y clases usados, mensajes intercambiados e invocaciones a métodos. Muestra qué se hace y en qué orden.

¿Cómo se distingue en un diagrama de secuencia un mensaje síncrono de uno asíncrono?::Síncrono: **cabeza llena**, el emisor queda bloqueado y la respuesta va en **línea discontinua**. Asíncrono: **cabeza abierta**, termina inmediatamente.

¿Qué diferencia hay entre los fragmentos alt, opt, break y loop?::**alt** = un flujo u otro según condición · **opt** = solo si se cumple la condición · **break** = detiene la ejecución, para casos de error · **loop** = se repite mientras se cumpla la condición.

¿Qué es un diagrama de secuencia de alto nivel?::Uno que describe la **comunicación entre las aplicaciones integradas** (ej. MyApplication con GoogleMaps, Tripadvisor y Accuweather API), no entre objetos internos.
