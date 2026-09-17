---
tema: Arquitectura de software
fuente: "Presentación de clase — capturas_U2_F3 (0, 1, 2, 4, 5, 6, 7, 10, 11, 12), serie «Estilos Arquitectónicos –arquitectura en o por capas–». NÚCLEO."
fecha: 2026-09-17
---

# Flashcards — Arquitectura en o por capas (punto 1.9)

Compatible con el plugin **Spaced Repetition** de Obsidian: cada tarjeta es una línea con la
pregunta, el separador de dos signos de dos puntos, y la respuesta.

Notas: [[Arquitectura en capas]]

## Clase — capturas_U2_F3 (2026-09-17)

Según la definición de clase de la arquitectura en o por capas, ¿a qué se acercan progresivamente las operaciones de cada capa?::Al conjunto de instrucciones de la máquina
En la arquitectura en o por capas, ¿para qué sirven los componentes de la capa externa?::Sirven a las operaciones de interfaz del usuario
En la arquitectura en o por capas, ¿qué proporcionan las capas intermedias?::Servicios de utilería y de SW de aplicaciones
En la arquitectura en o por capas, ¿para qué sirven los componentes de la capa interna?::Sirven como interfaz con el sistema operativo
¿Cuáles son los cuatro anillos del diagrama de capas concéntricas, de afuera hacia adentro?::Capa de la interfaz de usuario, Capa de la Aplicación, Capa de Utilerías y Capa Central; los rectángulos dentro de los anillos son módulos
Según la infografía de clase, ¿de qué arquitectura es especialización la arquitectura por capas?::De la arquitectura cliente-servidor
¿Cuáles son las 4 capas más comunes de un sistema de información y su otro nombre?::Presentación (capa UI), aplicación (capa de servicio), lógica de negocios (capa de dominio) y acceso a datos (capa de persistencia)
¿Cómo describe la infografía el modelo en capas usando una figura?::Como una "pirámide invertida de re-uso" donde cada capa agrega responsabilidad y abstracción a la capa directamente sobre ella
Según la infografía, ¿dónde pueden residir las capas de una aplicación?::En la misma máquina física (misma capa) o distribuidas sobre diferentes computadores (n-capas)
¿Cómo se comunican los componentes de una capa con los de otras capas, según la infografía?::A través de interfaces muy bien definidas
En el diagrama de tres niveles web, ¿qué abarca cada nivel?::1er nivel la capa de presentación, del navegador al servidor web; 2º nivel el programa o script en su entorno de ejecución; 3er nivel los datos que necesita el segundo
¿Cuáles son las tres ventajas de la arquitectura en o por capas según la clase?::Facilita la descomposición del problema en varios niveles de abstracción; soporta fácilmente la evolución (los cambios solo afectan a las capas vecinas); se pueden cambiar las implementaciones respetando las interfaces con las capas adyacentes
¿Cuáles son las dos desventajas de la arquitectura en o por capas según la clase?::No todos los sistemas pueden estructurarse en capas, y a menudo es difícil encontrar la separación en capas adecuadas
¿Cuáles son los tres tiers del diagrama three-tier de clase?::Tier 1 Presentation (Clients), Tier 2 Business Logic (Application Servers) y Tier 3 Data/Resource (Existing Enterprise Information Systems, con Resource Manager y Resources)
¿Qué artefacto piden los dos ejercicios de la serie de capas?::Un diagrama de bloques: el de la partida multijugador por Internet y el de la tienda en línea con catálogo, inventario y confirmaciones por correo aplicando el estilo en o por capas
