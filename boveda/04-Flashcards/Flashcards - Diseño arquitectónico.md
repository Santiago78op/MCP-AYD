---
tema: Diseño arquitectónico
fuente: "Presentación de clase — capturas_U2 (0 a 11). NÚCLEO."
fecha: 2026-09-15
---

# Flashcards — Diseño arquitectónico

Compatible con el plugin **Spaced Repetition** de Obsidian: cada tarjeta es una línea con la
pregunta, el separador de dos signos de dos puntos, y la respuesta.

#flashcards/diseno-arquitectonico

Según la clase, ¿qué incluye el diseño de la arquitectura?::**Estructura** (subsistemas como composición de componentes), **comportamiento** (comunicación entre componentes), cualquier otra información relevante (protocolos de comunicación, sincronización y acceso a datos · distribución física · puntos de variabilidad y extensión) y **aspectos de seguridad**.

¿Cuándo se diseña la arquitectura?::Es el **primer paso en el diseño**, previo al diseño detallado (analizar el problema → diseño arquitectura → diseño detallado), y además es una **actividad continua**: evoluciona durante el desarrollo y todo el tiempo de vida de la aplicación.

¿Cuáles son las tres cosas que se tienen en cuenta para el diseño y qué producen?::**Requisitos**, **contexto** y **experiencia del arquitecto**. Producen el **documento de diseño arquitectónico**.

¿Cuáles son los cuatro grupos de aspectos del contexto?::Aspectos del **negocio** (amortizar infraestructura, bajos costes de instalación, personal disponible) · de la **estructura organizacional** (intereses creados, ej. mantener una BD existente · método estándar de hacer negocio) · **tendencias actuales** (nube, apps móviles) · **tecnología disponible** (centralizado vs distribuido, desde cero vs servicios externos).

¿Qué hace el arquitecto con sus experiencias anteriores?::Las **buenas** dan lugar a **replicar** esos diseños; las **malas** se **evitan** en el nuevo diseño.

Según la clase, ¿qué incluye el documento de diseño arquitectónico y qué es una vista?::Suele incluir **varias vistas**. Una vista representa un **aspecto parcial** de una arquitectura software, y cada participante en el desarrollo estará interesado en una o varias.

En la figura 4+1 de la unidad 2, ¿qué participante corresponde a cada vista?::Logical View → analista y usuario final · Implementation View → programador · Process View → integrador de sistemas · Deployment View → administrador de sistemas · Use Case View al centro.

¿Qué rol del equipo de arquitectura es necesario y qué otros roles son posibles?::El **arquitecto jefe** es necesario. Posibles: arquitecto de aplicaciones, de infraestructuras, de datos.

¿Cuáles son las tres formas de modelar una arquitectura según la clase?::**Lenguajes de descripción de arquitectura (ADLs)**, **diagramas UML** y **diagramas de bloque de alto nivel**.

¿Qué es un ADL según la clase?::Lenguajes **textuales formales** ideados para describir una arquitectura software en términos de **componentes y conectores**.
