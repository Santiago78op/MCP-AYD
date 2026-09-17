---
tema: Arquitectura de software
fuente: "Presentación de clase — capturas_U2_F2 (30, 30-componentes-conectores; cruce con 9), serie «Estilos Arquitectónicos –Catálogo de Estilos–». NÚCLEO. + COMPLEMENTO — procedencia probable de cada diapositiva (Reynoso y Kicillof 2004 · Clements et al., Documenting Software Architectures), marcada, no en disco"
fecha: 2026-09-16
punto_del_programa: "1.9 — Géneros y Estilos Arquitectónicos (catálogo: cliente-servidor, centrada en datos, en capas, flujo de datos, llamada y retorno, basada en eventos)"
alias: "catalogo de estilos, familias de estilos, llamada y retorno, flujo de datos, centrada en datos, peer-to-peer, codigo movil, C&C, componentes y conectores, blackboard, pipes and filters"
---

# Catálogo de estilos arquitectónicos

Cómo se **agrupan** los estilos en familias. Es la parte del punto **1.9** que el programa llama
*"catálogo"* y que hasta hoy solo tenía complemento (Reynoso y el SAIP, en
[[Estilos arquitectónicos]] Parte II).

> [!important] Esta nota es NÚCLEO
> Sale de **dos diapositivas** con el mismo subtítulo en rojo, **"–Catálogo de Estilos–"**: una lista
> textual (captura 30) y un árbol de componentes y conectores (captura *30-componentes-conectores*).
> Además se cruza con la lista de nueve estilos de la captura 9.
>
> **Las dos diapositivas no agrupan igual.** No es un error de transcripción: son dos taxonomías
> distintas en la misma clase. Ver §4.

---

## 1. El catálogo textual (captura 30)

Textual:

> Catalogo de estilos:
> - Arquitectura centrada en datos (arquitecturas de pizarra, Data Warehouse)
> - Arquitectura de flujo de datos (Tuberías y filtros, proceso secuencial en lotes)
> - Arquitecturas de llamada y retorno (llamadas a procedimientos remotos, Modelo Vista Controlador
>   –MVC-, en Capas, Orientadas a Objetos, basadas en Componentes)
> - Arquitecturas Peer-to-peer (basadas en Eventos, orientadas a Servicios, basadas en Recursos)
> - Otras: de Código Móvil (máquinas virtuales), heterogéneos (procesos, atributos)

![[adjuntos/capturas-clase-U2/catalogo-estilos/catalogo-de-estilos-lista.png]]

En tabla, familia → miembros:

| Familia | Miembros que nombra | Qué tienen en común *(paráfrasis propia)* |
|---|---|---|
| **Centrada en datos** | pizarra, *Data Warehouse* | un **almacén central** de datos al que acceden los componentes |
| **Flujo de datos** | tuberías y filtros, proceso secuencial en lotes | los datos **pasan** por una serie de transformaciones |
| **Llamada y retorno** | RPC, **MVC**, **en capas**, orientadas a objetos, basadas en componentes | el que llama **invoca y espera** la respuesta |
| **Peer-to-peer** | basadas en **eventos**, orientadas a **servicios**, basadas en **recursos** | pares que se comunican **sin jerarquía** fija |
| **Otras** | código móvil (máquinas virtuales), heterogéneos (procesos, atributos) | lo que no entra en las cuatro anteriores |

> [!important] Lo que esta diapositiva resuelve
> **Capas va dentro de llamada y retorno.** Hasta ahora era una duda abierta: la diapositiva de
> definición de estilo nombraba *"llamar y regresar"* y *"capas"* por separado, y
> [[Estilos arquitectónicos]] §7 decía *"preguntalo antes de afirmar esa clasificación"*. El catálogo
> de clase lo afirma: **"Arquitecturas de llamada y retorno (… en Capas …)"**. Y MVC también.
>
> **Basada en eventos** —punto del programa que "no aparecía"— **aparece nombrada**, pero **dentro de
> peer-to-peer**, no como familia propia. Ver §4.

> [!note] Procedencia probable (COMPLEMENTO, no verificado en disco)
> Las cinco familias con esos miembros coinciden con la clasificación de **Reynoso y Kicillof**,
> *Estilos y patrones en la estrategia de arquitectura de Microsoft* (2004): flujo de datos · centrados
> en datos · llamada y retorno · código móvil · heterogéneos · peer-to-peer. **Ese documento no está en
> `00-Fuentes/lecturas/`** —el Reynoso que hay es la *Introducción*, que no trae este catálogo—, así
> que no se puede citar textual. Lo que se cita es la diapositiva.

---

## 2. El árbol de componentes y conectores (captura 30-componentes-conectores)

Mismo subtítulo, otra organización. Es un árbol cuya raíz es **"C & C"** —*componentes y
conectores*, la categoría de estructuras de tiempo de ejecución de [[Categorías de estructuras]]—.
Está **en inglés**. Transcrito leyendo cada línea con zoom:

| Nivel | Padre | Hijos |
|---|---|---|
| 1 | **C & C** | Data flow · Call-return · Event-based · Repository |
| 2 | **Data flow** | Batch sequential · Pipes and filters |
| 3 | **Pipes and filters** | Pipeline · UNIX pipe-and-filter |
| 2 | **Call-return** | Client-server · Peer to peer · SOA |
| 3 | **Client-server** | Multi-tier |
| 2 | **Event-based** | SOA · Point to point messaging · Publish-suscribe *[sic]* · Blackboard |
| 2 | **Repository** | Blackboard · Shared data |

![[adjuntos/capturas-clase-U2/catalogo-estilos/catalogo-estilos-arbol-componentes-conectores.png]]

> [!warning] Dos hojas con DOS padres — no es un error de lectura
> Se verificó a resolución completa: **SOA** cuelga de **Call-return y de Event-based** a la vez, y
> **Blackboard** cuelga de **Event-based y de Repository** a la vez. El árbol no es un árbol estricto:
> es una jerarquía donde un estilo puede heredar de dos familias.
>
> | Estilo | Por qué tiene dos padres *(lectura propia)* |
> |---|---|
> | **SOA** | un servicio se puede consumir **por llamada** (petición-respuesta) o **por mensajes/eventos** |
> | **Blackboard** (pizarra) | es un **repositorio** que además **avisa** a los agentes cuando cambia (invocación implícita) |

**Tres detalles que valen puntos:**

1. **Multi-tier es hijo de client-server.** O sea: **N-capas/multinivel es una especialización de
   cliente-servidor**, que a su vez es de llamada y retorno. Consistente con lo que dio la clase en
   [[Arquitectura en capas]]: *2 capas = modelo cliente-servidor*.
2. **Peer to peer está bajo Call-return.** En el catálogo textual es al revés: P2P es una familia que
   **contiene** a eventos y servicios. Ver §4.
3. La diapositiva escribe **"Publish-suscribe"**, sin la *b* de *subscribe*. Citalo como
   *publish-subscribe* y, si lo copiás de la lámina, con *[sic]*.

> [!note] Procedencia probable (COMPLEMENTO, no verificado en disco)
> Es la figura de estilos C&C de **Clements et al.**, *Documenting Software Architectures: Views and
> Beyond* (SEI) — de la misma escuela que el SAIP. No está en `00-Fuentes/`.

---

## 3. Qué estilo aparece en qué lista

Hay **cinco** listas de estilos en el material de clase y el programa. Ninguna coincide con otra.

| Estilo | Programa 1.9 | Definición de estilo (capturas_U2 21) | Lista de 9 (captura 9) | Catálogo textual (30) | Árbol C&C (30-cc) | Desarrollado en |
|---|---|---|---|---|---|---|
| **Monolítico** | — | — | ✅ 1 | — | — | [[Arquitectura monolítica]] |
| **Cliente-servidor** | ✅ | — | ✅ 2 | — | ✅ bajo Call-return | [[Arquitectura en capas]] §3 |
| **En capas / multi-tier** | ✅ | ✅ *capas* | ✅ 3 | ✅ bajo llamada y retorno | ✅ *Multi-tier*, bajo Client-server | [[Arquitectura en capas]] |
| **Microkernel** | — | — | ✅ 4 | — | — | — |
| **SOA** (orientada a servicios) | — | — | ✅ 5 | ✅ bajo peer-to-peer | ✅ bajo Call-return **y** Event-based | — |
| **Microservicios** | — | — | ✅ 6 | — | — | — |
| **Basada en eventos** (EDA) | ✅ | — | ✅ 7 *"Event Drive Architecture"* [sic] | ✅ bajo peer-to-peer | ✅ **familia** *Event-based* | — |
| **REST** / basadas en recursos | — | — | ✅ 8 | ✅ *basadas en Recursos*, bajo peer-to-peer | — | — |
| **Peer-to-peer** | — | — | ✅ 9 | ✅ **familia** | ✅ bajo Call-return | — |
| **Centrada en datos** / repository | ✅ | ✅ *centrado en datos* | — | ✅ **familia** | ✅ **familia** *Repository* | Parte II de [[Estilos arquitectónicos]] |
| Pizarra / blackboard | — | — | — | ✅ bajo centrada en datos | ✅ bajo Event-based **y** Repository | Parte II |
| *Data Warehouse* · *Shared data* | — | — | — | ✅ *Data Warehouse* | ✅ *Shared data* | — |
| **Flujo de datos** | ✅ | ✅ | — | ✅ **familia** | ✅ **familia** *Data flow* | Parte II |
| Tuberías y filtros · lotes | — | — | — | ✅ los dos | ✅ Pipes and filters · Batch sequential (+ Pipeline, UNIX) | Parte II |
| **Llamada y retorno** | ✅ | ✅ *"llamar y regresar"* | — | ✅ **familia** | ✅ **familia** *Call-return* | — |
| RPC · MVC · OO · componentes | — | — | — | ✅ los cuatro | — | — |
| Point to point messaging · publish-subscribe | — | — | — | — | ✅ bajo Event-based | Parte II (publish-subscribe) |
| Código móvil (máquinas virtuales) | — | — | — | ✅ en *Otras* | — | Parte II (*intérprete / MV*) |
| Heterogéneos (procesos, atributos) | — | — | — | ✅ en *Otras* | — | — |
| **Nube** | *on premise / cloud* | — | — | — | — | [[Arquitectura en la nube]] |

**Cómo se lee la tabla:**

- **Los seis del programa tienen, todos, al menos una diapositiva de clase** que los nombra. El que
  faltaba —*basada en eventos*— está en la lista de 9, en el catálogo textual y en el árbol.
- **Nombrado no es desarrollado.** De los seis, solo **capas** y **cliente-servidor** tienen
  diapositivas de desarrollo. Los demás siguen explicándose con complemento.
- La **lista de 9** (captura 9) es de **estilos concretos** y de moda (monolito, microservicios,
  REST); el **catálogo** y el **árbol** son de **familias**. Por eso casi no se solapan: la lista de 9
  no nombra ni una familia clásica (centrada en datos, flujo de datos, llamada y retorno).

---

## 4. Las dos taxonomías de clase no coinciden

| Punto | Catálogo textual (30) | Árbol C&C (30-cc) |
|---|---|---|
| ¿Peer-to-peer es familia o miembro? | **familia** (contiene eventos, servicios, recursos) | **miembro** de Call-return |
| ¿Eventos es familia o miembro? | **miembro** de peer-to-peer | **familia** (*Event-based*) |
| ¿Dónde va SOA? | bajo peer-to-peer | bajo Call-return **y** Event-based |
| ¿Dónde va la pizarra? | bajo centrada en datos | bajo Repository **y** Event-based |
| ¿Cliente-servidor? | **no aparece** | bajo Call-return, con multi-tier debajo |
| ¿Capas? | bajo llamada y retorno | *Multi-tier*, bajo client-server (→ call-return) |
| Idioma y origen probable | español · Reynoso y Kicillof | inglés · Clements et al. (SEI) |

**En lo que las dos coinciden** —y eso sí se puede afirmar sin dudar—:

- **Flujo de datos** es familia, con **tuberías y filtros** y **secuencial en lotes** adentro.
- **Centrada en datos / repository** es familia, con la **pizarra** adentro.
- **Llamada y retorno** es familia, y **capas** (multinivel) cae dentro.

> [!warning] La trampa
> Contestar *"¿a qué familia pertenece peer-to-peer?"* o *"¿basada en eventos es una familia?"* con
> una sola respuesta como si fuera la única. **Depende de cuál de sus dos diapositivas se use.** En un
> examen: declarar la taxonomía en una línea (*"según el catálogo de estilos de clase…"*) y responder
> con esa. Es pregunta para clase cuál prefiere.

**Regla memorizable:** *datos que se guardan (centrada en datos), datos que pasan (flujo de datos),
control que vuelve (llamada y retorno), pares que se avisan (peer-to-peer / eventos).*

---

## Notas relacionadas

- [[Estilos arquitectónicos]] — definiciones de estilo y patrón, y el complemento que explica cada familia
- [[Arquitectura de referencia]] — las diapositivas anteriores de la misma serie
- [[Patrones arquitectónicos]] — el nivel de menor alcance que el estilo
- [[Arquitectura en capas]] — capas y cliente-servidor, los dos desarrollados en clase
- [[Arquitectura monolítica]] — el primero de la lista de 9, fuera de los dos catálogos
- [[Arquitectura en la nube]] — el *cloud* del programa
- [[Categorías de estructuras]] — de dónde sale el "C & C" de la raíz del árbol

## Preguntas de repaso

1. Nombrá las cinco entradas del catálogo textual de estilos y dos miembros de cada una.
2. Según el catálogo de clase, ¿la arquitectura en capas pertenece a alguna familia? ¿A cuál?
3. En el árbol de componentes y conectores, ¿qué dos estilos tienen dos padres y cuáles son?
4. ¿En qué dos puntos se contradicen el catálogo textual y el árbol C&C? ¿Cómo lo manejarías en un
   examen?
5. ¿Qué relación hay, en el árbol, entre *multi-tier* y *client-server*, y cómo encaja con lo que dio
   la clase sobre la arquitectura de 2 capas?
