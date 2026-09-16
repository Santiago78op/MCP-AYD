---
tema: Arquitectura de software
fuente: "Presentación de clase — capturas_U2 (39, 40, 41, 57). NÚCLEO. + UML de Booch, Rumbaugh y Jacobson (complemento)"
fecha: 2026-09-15
---

# Flashcards — Diagrama de paquetes

Compatible con el plugin **Spaced Repetition** de Obsidian: cada tarjeta es una línea con la
pregunta, el separador de dos signos de dos puntos, y la respuesta.

Salen de [[Diagrama de paquetes]]. Las que llevan *(complemento)* no están en la diapositiva.

#flashcards/paquetes

¿Cuáles son las dos funciones de los paquetes según la clase?::**Organizar** los elementos en los modelos para comprenderlos más fácilmente, y **controlar el acceso** a sus contenidos para controlar las líneas de separación de un sistema.

¿Qué elementos puede contener un paquete (recuadro rojo de la clase)?::Clases, interfaces, componentes, nodos, colaboraciones, casos de uso, diagramas **e incluso otros paquetes**.

¿Qué significa que "la posesión es una relación compuesta" en un paquete?::Que el elemento **se declara en el paquete**: le pertenece a ese paquete.

¿Cómo se dibuja un paquete en UML y dónde va su nombre?::Como una **carpeta**: rectángulo con pestaña. El nombre va en el cuerpo si está vacío, y **en la pestaña** si el cuerpo muestra su contenido (lista o elementos dibujados).

¿Qué hay que hacer para usar los elementos de otro paquete?::**Importar** el paquete que interesa, con una dependencia punteada estereotipada «import» que va **del que importa al importado**.

Cuando un paquete importa a otro, ¿a qué elementos puede acceder?::Solo a los **públicos** (marcados con +). Esos elementos se dice que son **exportados** por el paquete que los contiene.

En la figura de clase, Cliente importa Políticas y Políticas importa GUI. ¿Puede Cliente usar Ventana de GUI?::*(complemento)* **No en UML 1.x**: la importación no es transitiva y Cliente tendría que importar GUI directamente. En UML 2.x un «import» público sí reexporta, y «access» no.

¿Qué indican los símbolos +, - y # delante de un elemento de un paquete?::*(complemento)* Visibilidad **pública** (exportada), **privada** y **protegida**. Solo lo público es accesible para quien importa.

¿En qué vistas del 4+1 de la presentación se usa el diagrama de paquetes?::En la **Vista Lógica** (con el de clases) y en la **Vista de Despliegue o de Desarrollo** (con el de componentes).
