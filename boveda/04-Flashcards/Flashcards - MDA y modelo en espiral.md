---
tema: Arquitectura en el ciclo de vida
fuente: "NOTA TÉCNICA DE CLASE NT1 (unidad 3) — Meaurio y Schmieder (2013), Revista Latinoamericana de Ingeniería de Software 1(4): 142-146"
fecha: 2026-10-13
---

# Flashcards — MDA y modelo en espiral

Compatible con el plugin **Spaced Repetition** de Obsidian: cada tarjeta es una línea con la
pregunta, el separador de dos signos de dos puntos, y la respuesta. Salen de
[[Arquitectura dirigida por modelos MDA]] y [[Arquitectura de software en el modelo en espiral]].

> [!note] Es la NT1 de la unidad 3
> Nota técnica de clase (*Arquitectura del SW y CCV*), no una diapositiva. No confundir con la NT1
> de trazabilidad de la unidad 1.

¿Qué es MDA y quién lo promueve? :: Model Driven Architecture, de la OMG: construir software como transformación sucesiva de modelos en UML, desde alto nivel de abstracción hasta una plataforma concreta.
¿Cuáles son los cuatro modelos de MDA, en orden? :: CIM, PIM, PSM e ISM: negocio, sistema sin tecnología, sistema con tecnología, y código.
¿Qué es el PIM en MDA? :: El modelo de alto nivel del sistema, independiente de cualquier tecnología o plataforma. Equivale casi por entero a la fase de análisis.
¿Qué contiene un cartucho MDA? :: Las reglas necesarias para realizar una transformación de modelos.
¿Cuáles son las cuatro ventajas de MDA según la lectura? :: Separación de responsabilidades, productividad, portabilidad, y mantenimiento y documentación.
¿En qué cuatro estándares se apoya MDA? :: UML, MOF, XMI y CWM.
¿Qué elemento nuevo incorpora el modelo en espiral de Boehm? :: El análisis de riesgo, que se hace en cada vuelta.
En la espiral, ¿qué representan el avance angular y el desplazamiento radial? :: El avance angular es el progreso del desarrollo, y el desplazamiento radial, el incremento acumulado de los costes.
¿Cuáles son las cuatro actividades del modelo en espiral según el apartado III de la lectura? :: Determinación de objetivos y alternativas, análisis de riesgo, ingeniería y planificación.
¿Qué doble función tiene la arquitectura en el ciclo de análisis de riesgos? :: Se la analiza para comprobar que soporta los requerimientos de calidad, y se la usa como prototipo para estudiar el comportamiento del sistema antes de diseñarlo.
¿Qué son los requerimientos significativos arquitectónicamente? :: Los que tienen un impacto esencial sobre la arquitectura.
¿Qué deficiencia de los ciclos de vida tradicionales resuelve MDA? :: La pérdida de trazabilidad entre los artefactos de las distintas etapas: con la doble transformación automática, al regenerar, la trazabilidad queda garantizada.
¿Qué tres actores interactúan en el ciclo de requerimientos según la figura 5? :: La arquitectura de software como experto de la solución, la administración del negocio como experto del dominio, y la administración del proyecto como experto de la planeación.
