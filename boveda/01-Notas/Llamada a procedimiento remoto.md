---
tema: Arquitectura de software
fuente: "Presentación de clase — capturas_U2_F3 (40, 41, 42, 43), serie «Estilos Arquitectónicos», subtítulo «–Patrones Arquitéctónicos para arquitectura de llamada y retorno–». NÚCLEO. + COMPLEMENTO — stub/skeleton, marshalling y ejemplos de tecnologías (conocimiento general, marcado)"
fecha: 2026-09-17
punto_del_programa: "1.9 — Géneros y Estilos Arquitectónicos (llamada y retorno)"
alias: "RPC, remote procedure call, llamada de procedimiento remoto, llamadas a procedimientos remotos, patron RPC, extremo cliente, extremo servidor, empaquetado, desempaquetado, serializable, paso por valor"
---

# Llamada a procedimiento remoto (RPC)

El primer **patrón arquitectónico** del estilo [[Arquitectura de llamada y retorno]]. Es el único de
sus tres ejemplos (RPC, orientado a objetos, MVC) que la clase **desarrolló** con diapositivas
propias, incluido un diagrama de 15 pasos.

> [!important] Esta nota es NÚCLEO
> Cuatro diapositivas con el mismo subtítulo en rojo, *"–Patrones Arquitéctónicos* [sic] *para
> arquitectura de llamada y retorno–"*:
>
> | Captura | Encabezado en negrita | Qué aporta |
> |---|---|---|
> | 40 | *Llamada de procedimiento remoto (RPC)* | la definición en una línea, como ejemplo del estilo |
> | 41 | *Patrón Arquitectónico de llamada a procedimiento remoto* | el **objetivo**, que se basa en **cliente-servidor**, y el dibujo de dos máquinas |
> | 42 | *Patrón Arquitectónico de llamada a procedimiento remoto* | el **modelo**: argumentos, ejecución, notificación, retorno |
> | 43 | *Arquitectura de llamada a procedimiento remoto* | **paso por valor**, **serialización** y el diagrama de **15 pasos** |

---

## 1. Qué es

Tres definiciones de clase, de la más corta a la más completa.

**En una línea** (captura 40):

> **Llamada de procedimiento remoto (RPC):** Un componente llama a un procedimiento en otro
> componente, que lo ejecuta y devuelve un resultado.

**El objetivo** (captura 41):

> El objetivo de RPC es extender a los sistemas distribuidos el mecanismo de llamadas a procedimientos
> y subrutinas de los lenguajes de programación.
>
> RPC está basado en el modelo cliente - servidor
>
> RPC permite que un proceso localizado en una máquina pueda ejecutar código localizado en otra máquina
> remota, sin preocuparse por la comunicación entre ambas.

**El modelo** (captura 42):

> En el modelo de llamada a procedimiento remoto, un proceso realiza una llamada a procedimiento de
> otro proceso que posiblemente este [sic] localizado remotamente.
>
> - Los datos se pasan a través de argumentos.
> - Cuando un proceso recibe una llamada, se ejecuta la acción codificada en el procedimiento.
> - Se notifica la finalización de la llamada al proceso que lo invoca
> - Si existe un valor de retorno se envía desde el proceso invocado

Las tres ideas que hay que poder decir:

| Idea | Frase de clase | En criollo |
|---|---|---|
| **Qué extiende** | *"extender a los sistemas distribuidos el mecanismo de llamadas a procedimientos y subrutinas"* | llamar a una función **como siempre**, pero la función vive **en otra máquina** |
| **En qué se basa** | *"basado en el modelo cliente - servidor"* | el que llama es **cliente**, el que ejecuta es **servidor** (ver [[Arquitectura de llamada y retorno]] §3) |
| **Qué oculta** | *"sin preocuparse por la comunicación entre ambas"* | el programador no escribe el código de red: lo hacen los **extremos** (§5) |

---

## 2. El dibujo de dos máquinas (captura 41)

![[adjuntos/capturas-clase-U2/llamada-retorno/rpc-objetivo-basado-en-cliente-servidor.png]]

| Lado | Caja verde | Contenido | Qué representa |
|---|---|---|---|
| **Izquierda** (una PC) | **Programa Principal** | `....` · `c=suma(a,b);` · `.....` | el proceso que **llama** a `suma` como si fuera local |
| **Derecha** (otra PC) | **Subrutina** | `....` · `c= a + b;` · `return(c);` | el procedimiento que **se ejecuta en la otra máquina** y devuelve `c` |
| **Abajo** | — | un cable rotulado **Ethernet** que une a las dos PC | la red que el programador **no** ve |

> [!note] La captura está cortada abajo
> Debajo del cable Ethernet salen dos líneas más hacia el borde inferior; la diapositiva sigue fuera
> de la captura. Lo que se ve alcanza para la idea: **la llamada está de un lado, el código del
> otro, y los une una red**.

Es la frase del objetivo dibujada: *"un proceso localizado en una máquina"* (Programa Principal)
*"pueda ejecutar código localizado en otra máquina remota"* (Subrutina).

---

## 3. Cómo transcurre una llamada (captura 42)

Las cuatro viñetas son **una secuencia**:

| # | Viñeta textual | Quién actúa |
|---|---|---|
| 1 | *"Los datos se pasan a través de argumentos."* | el **proceso que invoca** |
| 2 | *"Cuando un proceso recibe una llamada, se ejecuta la acción codificada en el procedimiento."* | el **proceso invocado** |
| 3 | *"Se notifica la finalización de la llamada al proceso que lo invoca"* | el **invocado** avisa al **invocante** |
| 4 | *"Si existe un valor de retorno se envía desde el proceso invocado"* | el **invocado** devuelve el resultado |

![[adjuntos/capturas-clase-U2/llamada-retorno/rpc-modelo-argumentos-y-retorno.png]]

Fijate en el **"Si existe"** de la 4: la llamada **siempre** notifica que terminó (3), pero **no
siempre** devuelve un valor. Un procedimiento que solo *hace* algo (registrar, borrar) termina sin
retorno, y el que llamó igual se desbloquea.

---

## 4. Paso por valor y serialización (captura 43)

Textual, con el encabezado *"Arquitectura de llamada a procedimiento remoto"*:

> En RPC, todos los parámetros que se utilicen en las llamadas han de ser pasados por valor; y no por
> referencia, ya que ambos procedimientos se ejecutan en espacios de memoria diferentes.
>
> Para que estos parámetros puedan ser enviados a través de la red, es necesario que sean
> serializables, es decir, convertibles en una corriente de bytes.

Las dos reglas, con su porqué:

| Regla | Por qué, según la diapositiva | Qué pasaría si no |
|---|---|---|
| **Por valor, no por referencia** | *"ambos procedimientos se ejecutan en espacios de memoria diferentes"* | una referencia es una **dirección de memoria del cliente**: en el servidor esa dirección **no apunta a nada** *(lectura propia)* |
| **Serializables** | para *"ser enviados a través de la red"*, deben ser *"convertibles en una corriente de bytes"* | un dato que no se puede convertir en bytes (una conexión abierta, un archivo abierto) **no viaja** *(lectura propia)* |

| | Paso por **valor** | Paso por **referencia** |
|---|---|---|
| Qué viaja | **una copia** del dato | la **dirección** donde está el dato |
| ¿Sirve en RPC? | **sí**, obligatorio | **no** |
| Si el servidor lo modifica | cambia su copia; el cliente **no** se entera salvo por el valor de retorno | — |

---

## 5. El diagrama de los 15 pasos (captura 43)

![[adjuntos/capturas-clase-U2/llamada-retorno/rpc-parametros-por-valor-diagrama-15-pasos.png]]

### Los elementos

Leídos a resolución completa, de izquierda a derecha:

| Recuadro | Contiene | Color |
|---|---|---|
| **Máquina del Cliente** | **Cliente** (`⋮` · `a=suma()` · flecha doble vertical rotulada **bloqueado** · `a<- resultado` · `⋮`) y **Extremo Cliente** (`suma {` · *envío* · *empaquetado* · *desempaquetado* · *recepción* · `}`). Entre los dos, las cajas *parámetros* (arriba) y *resultado* (abajo) | blanco; el Extremo Cliente sobre **amarillo** |
| **Red de Comunicaciones** | solo el rótulo; la cruzan dos flechas gruesas | **amarillo** |
| **Máquina del Servidor** | **Extremo Servidor** (*recepción* · *desempaquetado* · *empaquetado* · *envío*) y **Servidor** (`suma {` · flecha doble vertical rotulada **proceso servicio** · `}`). Entre los dos, las cajas *parámetros* (arriba) y *resultado* (abajo) | blanco; el Extremo Servidor sobre **amarillo** |

La franja **amarilla** cubre **Extremo Cliente + Red + Extremo Servidor**: marca todo lo que hace RPC
por su cuenta. Lo que queda **fuera** del amarillo —Cliente y Servidor— es el código que escribe el
programador. Es el *"sin preocuparse por la comunicación"* de la captura 41, pintado.

### Los 15 pasos

Cada número está en un círculo junto a una flecha curva. Dirección leída con zoom en cada punta:

| Paso | Dónde | Flecha: de → a | Qué pasa |
|---|---|---|---|
| **1** | Máquina del Cliente | `a=suma()` (Cliente) → *parámetros* | el cliente llama a `suma` como si fuera local y entrega los parámetros |
| **2** | Máquina del Cliente | *parámetros* → *empaquetado* (dentro de `suma {` del Extremo Cliente) | el extremo cliente recibe los parámetros |
| **3** | Extremo Cliente | *empaquetado* → *envío* | los parámetros se empaquetan (se serializan, §4) y pasan a envío |
| **4** | Red de Comunicaciones | *envío* (Extremo Cliente) → *recepción* (Extremo Servidor), flecha gruesa → | el paquete viaja por la red |
| **5** | Extremo Servidor | *recepción* → *desempaquetado* | se reciben y desempaquetan los bytes |
| **6** | Máquina del Servidor | *desempaquetado* → *parámetros* | se reconstruyen los parámetros |
| **7** | Máquina del Servidor | *parámetros* → `suma` (Servidor) | se llama al procedimiento real, ahora sí local |
| **8** | Servidor | flecha doble entre `{` y `}`, rotulada **proceso servicio** | se ejecuta `suma` |
| **9** | Máquina del Servidor | fin de `suma` (Servidor) → *resultado* | el servidor devuelve el resultado |
| **10** | Máquina del Servidor | *resultado* → *empaquetado* (Extremo Servidor) | el extremo servidor toma el resultado |
| **11** | Extremo Servidor | *empaquetado* → *envío* | el resultado se empaqueta y pasa a envío |
| **12** | Red de Comunicaciones | *envío* (Extremo Servidor) → *recepción* (Extremo Cliente), flecha gruesa ← | la respuesta viaja por la red |
| **13** | Extremo Cliente | *recepción* → *desempaquetado* | se recibe y desempaqueta la respuesta |
| **14** | Máquina del Cliente | *desempaquetado* → *resultado* | se reconstruye el resultado |
| **15** | Máquina del Cliente | *resultado* → `a<- resultado` (Cliente) | el cliente recibe el valor y **sigue** |

### Cómo se lee de un vistazo

| Tramo | Pasos | Simétrico de |
|---|---|---|
| Cliente → red: llamar, empaquetar, enviar | 1-3 | 13-15 (recibir, desempaquetar, devolver al cliente) |
| Cruce de ida | 4 | 12 (cruce de vuelta) |
| Red → servidor: recibir, desempaquetar, llamar | 5-7 | 9-11 (resultado, empaquetar, enviar) |
| Ejecución | **8** | — es el único paso que **hace el trabajo** |

**De 15 pasos, uno solo es la suma.** Los otros 14 son el costo de que el procedimiento esté en otra
máquina.

> [!important] El "bloqueado" une esta diapositiva con la definición del estilo
> En el Cliente, la flecha doble **bloqueado** va desde `a=suma()` (paso 1) hasta `a<- resultado`
> (paso 15). Es exactamente la tercera viñeta de [[Arquitectura de llamada y retorno]] §2: *"Un
> componente que invoca un servicio permanece en estado de bloqueo mientras el servicio termina"*.
> Por eso RPC es un patrón **de llamada y retorno**: el cliente no hace nada entre 1 y 15.

---

## 6. Dónde encaja

| Pregunta | Respuesta de clase | Fuente |
|---|---|---|
| ¿Qué es RPC? | un **patrón arquitectónico** | 41 y 42: *"Patrón Arquitectónico de llamada a procedimiento remoto"* |
| ¿De qué estilo? | **llamada y retorno** | subtítulo de 40-43 |
| ¿Sobre qué modelo? | **cliente-servidor** | 41 |
| ¿Qué otros patrones comparten el estilo? | orientado a objetos y [[Modelo-Vista-Controlador]] | 40 |

> [!warning] Tres rótulos para lo mismo en el material de clase
> - 41 y 42: ***"Patrón Arquitectónico** de llamada a procedimiento remoto"*.
> - 43: ***"Arquitectura** de llamada a procedimiento remoto"*.
> - Catálogo textual (capturas_U2_F2, 30): *"Arquitecturas de llamada y retorno (**llamadas a
>   procedimientos remotos**, …)"*, como miembro de la familia.
>
> La doctrina de clase es *estilo ⊃ patrón arquitectónico ⊃ patrón de diseño* y dos de las tres
> diapositivas de RPC dicen **patrón arquitectónico**. En un examen: **"RPC es un patrón
> arquitectónico del estilo llamada y retorno, basado en el modelo cliente-servidor"**.
>
> Ojo también: RPC **no está** en la lista de 13 patrones arquitectónicos de
> [[Patrones arquitectónicos]] §5. Esa lista no es exhaustiva.

---

## 7. COMPLEMENTO — los nombres que vas a encontrar afuera

> [!note] COMPLEMENTO (conocimiento general; no es de la clase)
> | Término de la clase | Nombre habitual en la literatura |
> |---|---|
> | **Extremo Cliente** | *stub* del cliente (o *proxy*) |
> | **Extremo Servidor** | *skeleton* o *stub* del servidor |
> | **empaquetado / desempaquetado** | *marshalling / unmarshalling* |
> | convertir en *"corriente de bytes"* | serialización |
>
> - **Tecnologías que implementan el patrón:** Sun RPC (ONC), Java RMI (la versión orientada a
>   objetos), XML-RPC, gRPC.
> - **La trampa de la transparencia.** *"Sin preocuparse por la comunicación"* no quiere decir que la
>   red no exista: una llamada remota es **miles de veces más lenta** que una local y **puede fallar**
>   aunque el procedimiento esté bien (el servidor está caído, se perdió el paquete). Por eso los
>   sistemas reales agregan tiempos de espera y reintentos, y patrones como **Circuit Breaker** (de
>   la lista de 13).

> [!tip] La clase ya había usado RPC, sin nombrarlo como patrón
> En el ejemplo de ADL (capturas_U2), el sistema `simple_cs` une `client` y `server` con
> `Connector rpc = { Roels { caller, callee}}` [sic]: un **conector RPC** con los roles *caller*
> (quien llama) y *callee* (quien es llamado). Es el mismo cliente-servidor de la captura 41, escrito
> en un ADL. Ver [[Lenguajes de descripción de arquitectura]] §2.

---

## 8. La trampa

> [!warning] Tres errores con RPC
> 1. **Pasar parámetros por referencia.** La clase lo dice explícito: **por valor**, porque los dos
>    procedimientos están en **espacios de memoria diferentes**.
> 2. **Olvidar la serialización.** Que se pase por valor no alcanza: el valor tiene que poder
>    convertirse en **una corriente de bytes** para cruzar la red.
> 3. **Creer que el cliente sigue trabajando mientras espera.** Queda **bloqueado** del paso 1 al 15:
>    RPC es síncrono, por eso es de llamada y retorno y no basado en eventos.

**Regla memorizable:** *RPC = llamar a una subrutina que vive en otra máquina, sobre cliente-servidor.
Parámetros por valor y serializables. Los extremos empaquetan, envían, reciben y desempaquetan. De 15
pasos, solo el 8 hace el trabajo, y el cliente está bloqueado del 1 al 15.*

---

## Notas relacionadas

- [[Arquitectura de llamada y retorno]] — el estilo al que pertenece este patrón y su definición de bloqueo
- [[Modelo-Vista-Controlador]] — el otro patrón arquitectónico del estilo con diapositiva propia
- [[Arquitectura en capas]] — cliente-servidor como 2 capas, el modelo en que se basa RPC
- [[Patrones arquitectónicos]] — qué es un patrón arquitectónico y la lista de 13
- [[Catálogo de estilos arquitectónicos]] — RPC como miembro de la familia en el catálogo textual
- [[Lenguajes de descripción de arquitectura]] — el conector `rpc` del ejemplo `simple_cs`
- [[Diagrama de secuencia]] — la comunicación síncrona, con el emisor bloqueado

## Preguntas de repaso

1. ¿Cuál es el objetivo de RPC según la clase y en qué modelo se basa?
2. ¿Por qué en RPC los parámetros se pasan por valor y no por referencia? ¿Qué otra condición deben
   cumplir para viajar por la red?
3. Enumerá las cuatro viñetas del modelo de llamada a procedimiento remoto. ¿Qué indica el *"Si
   existe"* de la última?
4. En el diagrama de 15 pasos, ¿qué hacen el Extremo Cliente y el Extremo Servidor? ¿Qué pasos cruzan
   la red y cuál es el único que ejecuta el procedimiento?
5. ¿Qué marca la flecha *bloqueado* del lado del Cliente y con qué viñeta de la definición de llamada y
   retorno se corresponde?
