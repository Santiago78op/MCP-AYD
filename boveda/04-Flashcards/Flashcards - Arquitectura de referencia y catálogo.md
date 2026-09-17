---
tema: Arquitectura de software
fuente: "Presentación de clase — capturas_U2_F2 (23, 24, 25, 26, 30, 30-componentes-conectores). NÚCLEO."
fecha: 2026-09-16
---

# Flashcards — Arquitectura de referencia y catálogo de estilos (punto 1.9)

Compatible con el plugin **Spaced Repetition** de Obsidian: cada tarjeta es una línea con la
pregunta, el separador de dos signos de dos puntos, y la respuesta.

Notas: [[Arquitectura de referencia]] · [[Catálogo de estilos arquitectónicos]]

## Clase — capturas_U2_F2 (2026-09-16)

¿Qué dos conceptos entran, según la diapositiva, para formar una arquitectura de referencia?::El modelo de referencia y el patrón arquitectónico; de la arquitectura de referencia sale el "Software de Arquitectura" (la arquitectura del sistema)
¿Qué dice la diapositiva sobre modelo de referencia, patrón arquitectónico y arquitectura de referencia?::"Estos son conceptos útiles que capturan elementos de una arquitectura, pero en sí ellos no son arquitecturas"
¿Qué es un modelo de referencia?::Una división de funcionalidad junto con el flujo de datos entre las piezas; un estándar de descomposición de un problema conocido en partes que cooperativamente lo resuelven
¿Qué es una arquitectura de referencia?::Un modelo de referencia mapeado en elementos de software que cooperativamente implementan la funcionalidad definida en el modelo de referencia y flujos de datos entre ellos
¿Cuál es la palabra que separa modelo de referencia de arquitectura de referencia?::"Mapeado": el modelo divide funcionalidad; la arquitectura la mapea en elementos de software
¿Cuáles son los cuatro tipos de arquitectura de la tabla "Definición de una arquitectura candidata"?::Conceptual, Modular, Código y Ejecución
En la tabla de arquitectura candidata, ¿qué elementos y relaciones tiene el tipo Modular?::Elementos: subsistemas, módulos. Relaciones: exportaciones, importaciones
En la tabla de arquitectura candidata, ¿qué elementos y relaciones tienen los tipos Código y Ejecución?::Código: archivos, directorios, bibliotecas / incluye, contiene. Ejecución: tareas, líneas, interacciones de objetos / usos, llamadas
¿Cuáles son las familias del catálogo de estilos textual de clase?::Centrada en datos, flujo de datos, llamada y retorno, peer-to-peer, y otras (código móvil y heterogéneos)
Según el catálogo de clase, ¿a qué familia pertenece la arquitectura en capas?::A las arquitecturas de llamada y retorno, junto con RPC, MVC, orientadas a objetos y basadas en componentes
¿Qué miembros tiene la familia peer-to-peer en el catálogo textual?::Basadas en eventos, orientadas a servicios y basadas en recursos
¿Cuáles son las cuatro familias del árbol "C & C" del catálogo de estilos?::Data flow, Call-return, Event-based y Repository
En el árbol C&C, ¿qué dos estilos cuelgan de dos familias a la vez?::SOA (Call-return y Event-based) y Blackboard (Event-based y Repository)
En el árbol C&C, ¿de qué estilo es hijo Multi-tier?::De Client-server, que a su vez cuelga de Call-return
¿En qué se contradicen el catálogo textual y el árbol C&C?::En el textual, peer-to-peer es familia y eventos es miembro; en el árbol, Event-based es familia y peer to peer es miembro de Call-return
