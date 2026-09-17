---
tema: Arquitectura de software
fuente: "Presentación de clase — capturas_U2_F3 (30, 31, 32, 40, 41, 42, 43). NÚCLEO."
fecha: 2026-09-17
---

# Flashcards — Arquitectura de llamada y retorno y RPC (punto 1.9)

Compatible con el plugin **Spaced Repetition** de Obsidian: cada tarjeta es una línea con la
pregunta, el separador de dos signos de dos puntos, y la respuesta.

Notas: [[Arquitectura de llamada y retorno]] · [[Llamada a procedimiento remoto]]

## Clase — capturas_U2_F3 (2026-09-17)

¿Cómo define la clase, junto al árbol C & C, al estilo Call-return?::"Interacción por invocación síncrona de capacidades proporcionadas por los componentes"
¿Qué significa "síncrono" según la definición en rojo de la clase?::"Proceso o su efecto que se desarrolla en perfecta correspondencia temporal con otro proceso o causa"
¿Cuáles son las tres viñetas de la diapositiva "arquitectura de llamada y retorno"?::Los componentes proporcionan servicios invocados por otros de forma síncrona; se comunican mediante llamadas y respuestas, como funciones o métodos; el componente que invoca permanece en estado de bloqueo mientras el servicio termina
Según la diapositiva "call return: cliente-servidor", ¿quién conoce a quién?::El cliente requiere conocer el servidor y el servicio a invocar; los servidores no conocen a los clientes
¿Con qué esquema de protocolo interactúan cliente y servidor según la clase, y qué ejemplo da?::Un protocolo basado en un esquema request/reply, por ejemplo HTTP
¿Qué ventaja declara la clase para la arquitectura de llamada y retorno?::Se obtiene una estructura de programa relativamente fácil de modificar y cambiar de tamaño
¿Cuáles son los tres patrones arquitectónicos para arquitectura de llamada y retorno que da la clase?::Llamada de procedimiento remoto (RPC), Orientado a objetos y Modelo-Vista-Controlador
¿Cómo describe la clase el patrón orientado a objetos dentro de llamada y retorno?::Los objetos se comunican mediante llamadas a métodos, esperando respuestas
¿Cuál es el objetivo de RPC según la clase?::Extender a los sistemas distribuidos el mecanismo de llamadas a procedimientos y subrutinas de los lenguajes de programación
¿En qué modelo está basado RPC?::En el modelo cliente-servidor
¿Por qué en RPC los parámetros se pasan por valor y no por referencia?::Porque ambos procedimientos se ejecutan en espacios de memoria diferentes
¿Qué condición deben cumplir los parámetros de RPC para viajar por la red?::Ser serializables, es decir, convertibles en una corriente de bytes
¿Cuáles son las cuatro viñetas del modelo de llamada a procedimiento remoto?::Los datos se pasan a través de argumentos; al recibir la llamada se ejecuta la acción codificada en el procedimiento; se notifica la finalización al proceso que invoca; si existe un valor de retorno se envía desde el proceso invocado
En el diagrama de 15 pasos de RPC, ¿qué hacen el Extremo Cliente y el Extremo Servidor?::Empaquetan y envían, y reciben y desempaquetan los parámetros y el resultado; ocultan la comunicación por la red al Cliente y al Servidor
En el diagrama de 15 pasos de RPC, ¿qué pasos cruzan la red y cuál ejecuta el procedimiento?::Cruzan la Red de Comunicaciones el 4 (ida) y el 12 (vuelta); el 8 es el "proceso servicio" que ejecuta suma
