---
tema: Arquitectura de software
fuente: "Presentación de clase — capturas_U2_F3 (13-28), serie «Estilos Arquitectónicos –arquitectura centrada en el flujo de datos–» y «–estilo Secuencial por Lotes–». NÚCLEO."
fecha: 2026-09-17
---

# Flashcards — Arquitectura centrada en el flujo de datos y tuberías y filtros (punto 1.9)

Compatible con el plugin **Spaced Repetition** de Obsidian: cada tarjeta es una línea con la
pregunta, el separador de dos signos de dos puntos, y la respuesta.

Notas: [[Arquitectura centrada en el flujo de datos]] · [[Tuberías y filtros]]

## Clase — capturas_U2_F3 (2026-09-17)

¿Qué frase agregó la clase al árbol C & C, junto a Data flow resaltado?::"La computación/procesamiento es dirigido por el flujo de datos en el sistema"
¿En qué se enfoca la arquitectura centrada en el flujo de datos?::En la transformación de datos a través de una serie de componentes o filtros conectados por tuberías, donde cada filtro realiza una operación específica y los datos fluyen de forma independiente entre ellos
¿Qué dos atributos enfatiza la arquitectura de flujo de datos y para qué sistemas es adecuada?::Enfatiza la reutilización y la modificabilidad; es adecuada para sistemas con transformaciones de datos en pasos sucesivos
¿Cuáles son los dos ejemplos de arquitectura de flujo de datos que da la clase?::Las arquitecturas de tuberías y filtros y las de proceso secuencial en lotes
¿Qué caracteriza al estilo secuencial por lotes (batch sequential)?::Los componentes son programas independientes, y el supuesto es que cada paso se ejecuta hasta completarse antes que se inicie el paso siguiente
Según la diapositiva, ¿qué es una tubería (pipeline)?::Una arquitectura que conecta componentes computacionales (filtros) a través de los conectores (pipes), y las comunicaciones se ejecutan como un flujo
En la figura de la clase, ¿qué señalan Pipe, Operation y Pipeline?::Pipe es un tramo de tubo (el conector), Operation es la pieza entre tubos (el filtro) y Pipeline es el conjunto completo
¿Un filtro solo filtra datos?::No: los filtros no necesariamente realizan únicamente tareas de filtrado sino que ejecutan formas variables de transformación
¿Qué necesita saber un filtro de sus vecinos?::Nada de su funcionamiento: espera la entrada con cierta forma y produce su salida de una forma específica
¿Cuándo se podría usar tuberías y filtros? (tres condiciones)::Cuando se puede especificar la secuencia de un número conocido de pasos, no se requiere esperar la respuesta asincrónica de cada paso, y los componentes de abajo inspeccionan y actúan sobre los datos que vienen de arriba (no viceversa)
¿Cuál es la aplicación típica de tuberías y filtros según la clase?::Un procesamiento clásico de datos: el cliente hace un requerimiento, se valida, un web service toma el objeto de la base de datos, se convierte en html y se representa en pantalla
¿Qué muestran las figuras de módulo monolítico vs. pipelines?::Que en módulos monolíticos Task A y Task B se programan dos veces, mientras que con tuberías y filtros los mismos componentes se reutilizan en distintos pipelines
¿Cuáles son las cinco ventajas de tuberías y filtros?::Simple de entender e implementar, facilidad de mantenimiento y mejora, facilidad de diagnóstico, fuerza un procesamiento secuencial y ejecución concurrente
¿Cuáles son las cuatro desventajas de tuberías y filtros?::Demasiado simplista, no maneja condicionales, bucles y otras lógicas de control de flujo, no apto para situaciones interactivas, y problemas de rendimiento porque los datos se transmiten de forma completa
¿Qué elementos agrega el ejemplo de Secure Pipes and Filters alrededor de cada filtro?::Un ReferenceMonitor que consulta los derechos (Right) del rol antes de invocar la operación, un Authenticator y un Log por filtro, y derechos de configure sobre las pipelines
