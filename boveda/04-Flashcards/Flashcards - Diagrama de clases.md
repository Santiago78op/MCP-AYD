---
tema: Diagrama de clases
fuente: "Presentación de clase — capturas_U2 (53, 55, 56, 57, 58) + PDF TEMA 5 §3 + PDF IS 04 05b Ejemplos de Diagramas de Clases"
fecha: 2026-09-15
---

# Flashcards — Diagrama de clases

Compatible con el plugin **Spaced Repetition** de Obsidian: cada tarjeta es una línea con la
pregunta, el separador de dos signos de dos puntos, y la respuesta.

#flashcards/diagrama-de-clases

Según el PDF de clase TEMA 5, ¿cuáles son los dos fines del diagrama de clases?::En el **análisis de requisitos**, para generar el esquema de base de datos, y en el **diseño detallado**, para modelar los principales elementos del código antes de implementarlo.

¿Qué deben incluir las asociaciones en cada extremo, según el PDF de clase?::La **multiplicidad** y el **rol**.

¿Qué es una asociación reflexiva? Da el ejemplo de clase.::Una asociación de una clase **consigo misma**. En Persona: *casado-con* (marido 0..1 / mujer 0..1) y *Administra* (jefe 0..1 / empleado *). En el parque: Vagón *Arrastra* Vagón.

¿Cuál es el primer paso del método para obtener clases de un enunciado?::**Subrayar todos los sustantivos**, en singular y sin repetir: son las **clases candidatas**.

Nombrá las nueve canastas de descarte de candidatas.::A redundantes · B irrelevantes · C imprecisas · D nombres de clases (renombrar) · E son atributos · F son operaciones · G interfaces de usuario · H sistema completo · I actores.

¿Cómo se sacan las asociaciones de un enunciado?::Se buscan las frases que unen dos sustantivos ("asientos en un vuelo") y se **reescriben con verbo** ("el vuelo contiene asientos"). El verbo es el nombre de la asociación; después se pone la multiplicidad en los dos sentidos.

¿Por qué el PDF elimina la clase Operario del parque de atracciones?::Porque el operario se relaciona con el sistema **mediante la clase interfaz Dispositivo del operario**: es un actor, y entra por esa clase.

En el diagrama de clases de la catedrática del parque, ¿qué reemplaza a la Central Receptora de Averías del PDF?::La clase **Averías** y las interfaces **RegistroAvería** (realizada por Atracción) y **SolicitarServicio** (realizada por Averías).

En la captura 55 del parque, ¿hacia dónde apuntan los «Extend» de Generar Alerta y en qué punto se enganchan?::Desde Generar Alerta **hacia** Gestión Ficha Noria y Gestión Ficha Montaña Rusa, en el punto de extensión **Detectar Falla**.

¿Cómo se ve en el diagrama de componentes una interfaz que en el de clases realiza una clase?::Como una **piruleta ofrecida** por el componente que contiene esa clase (RegistroAverias en Gestión de Atracciones). Quien la usaba con punteada en clases la usa con punteada en componentes.
