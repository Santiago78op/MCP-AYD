---
tema: Arquitectura de software
fuente: "Presentación de clase — capturas_U2_F2 (1-8) + capturas_U2 (21). NÚCLEO. Las marcadas (complemento) salen de conocimiento general"
fecha: 2026-09-16
---

# Flashcards — Patrones de diseño y patrones arquitectónicos

Compatible con el plugin **Spaced Repetition** de Obsidian: cada tarjeta es una línea con la
pregunta, el separador de dos signos de dos puntos, y la respuesta.

Salen de [[Patrones de diseño]] y [[Patrones arquitectónicos]]. Las que llevan *(complemento)* no
están en la diapositiva.

#flashcards/patrones

¿Cuáles son los dos tipos de patrón que dio la clase?::**Patrones de diseño** (creacionales, estructurales, comportamiento) y **patrones arquitectónicos** (integración, seguridad, web).

¿Cómo define la clase un patrón de diseño?::Es la **solución a un problema de diseño** que debe haber **comprobado su efectividad** resolviendo problemas similares en el pasado, y tiene que ser **reutilizable** en contextos diferentes.

Si quitás o reemplazás un patrón de diseño, ¿a quién afecta?::Solo a **las clases directamente relacionadas con él**; para el resto de componentes de la arquitectura el impacto es **imperceptible**.

¿Qué hacen los patrones creacionales?::Controlan la forma en que se **crean** los objetos, con mecanismos que **evitan la creación directa** de objetos.

¿Qué hacen los patrones estructurales?::Tienen que ver con **cómo se relacionan las clases** con otras clases; dan orden y hacen los componentes **más flexibles y extensibles**.

¿Qué hacen los patrones de comportamiento?::Se relacionan con **procedimientos y la asignación de responsabilidad** a los objetos; engloban también los **patrones de comunicación** entre ellos.

¿Cuántos patrones de diseño listó la clase y cuáles dos no son del catálogo GoF?::**25**. *(complemento)* Los 23 de GoF más **Object Pool** y **Null Object**.

¿Cómo define la clase un patrón arquitectónico?::Tiene un **gran impacto sobre el componente**: cualquier cambio una vez construido el componente podría tener un **impacto mayor**.

¿Por qué un patrón arquitectónico es "fácil de reconocer"?::Porque tiene **impacto global sobre la aplicación** y **rige la forma de trabajar o comunicarse con otros componentes**; cambiarlo afecta al componente y a los **componentes relacionados**.

¿Qué categorías de patrón arquitectónico cuelgan del árbol de la clase?::**Integración, Seguridad y Web** (conectadas); al costado, sin línea, **SOA, Comunicación y Cloud**.

Nombrá cinco de los 13 patrones arquitectónicos de la clase.::DTO, DAO, Polling, Webhook, Load Balance, Service Registry, Service Discovery, API Gateway, Access Token, SSO, Store and forward, **Circuit Breaker**, Log aggregation (cualquiera cinco).

¿Qué contiene a qué en el dibujo de "Estilos Arquitectónicos"?::El **estilo** contiene **patrones arquitectónicos**, y cada patrón arquitectónico contiene **patrones de diseño**.

El patrón arquitectónico tiene "impacto global" y "menor alcance que el estilo": ¿cómo se concilian?::Son ejes distintos: **alcance** = cuántos aspectos cubre (uno solo, menor que el estilo); **impacto** = hasta dónde se propaga un cambio (al componente y los relacionados, mayor que el patrón de diseño).

¿Singleton, Adapter y Observer a qué familia pertenecen?::*(complemento)* Singleton = **creacional**, Adapter = **estructural**, Observer = **comportamiento**. Su lista está ordenada así: 1-6 creacionales, 7-13 estructurales, 14-25 comportamiento.
