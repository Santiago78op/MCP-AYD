---
tema: Arquitectura de software
fuente: "Presentación de clase — capturas_U2 (43, 44, 51). NÚCLEO. + COMPLEMENTO — caso Prime Video 2023 (conocimiento general, marcado)"
fecha: 2026-09-15
punto_del_programa: "1.9 — Géneros y Estilos Arquitectónicos"
---

# Arquitectura monolítica

Uno de los estilos que la catedrática desarrolló con diapositivas propias. No figura en el catálogo
del punto 1.9 del programa, pero sí en clase. Ver [[Estilos arquitectónicos]].

## 1. Qué es

Textual de la diapositiva:

> Este tipo de arquitecturas tienen la principal característica de **agrupar toda la funcionalidad y
> servicios de la aplicación en una base de código única**.

El dibujo que la acompaña muestra **tres círculos superpuestos** —**Interfaz usuario (UI)**,
**Lógica del negocio** y **Capa de acceso a los datos**— unidos por una sola línea a una única
**Base de datos**. La superposición es el mensaje: las tres partes **no están separadas**, forman un
solo bloque.

![[adjuntos/capturas-clase-U2/estilos/monolitica-definicion.png]]

| Elemento del dibujo | Qué representa |
|---|---|
| Interfaz usuario (UI) | la presentación |
| Lógica del negocio | las reglas del negocio |
| Capa de acceso a los datos | la comunicación con la base |
| Los tres círculos **superpuestos** | una sola aplicación, una base de código |
| Base de datos (una sola) | el almacenamiento, compartido por todo |

> [!note] Monolítico no quiere decir "sin capas"
> Las tres partes del dibujo son las mismas capas de [[Arquitectura en capas]]. Lo que hace
> monolítica a una arquitectura no es la falta de capas: es que **todo está en una base de código
> y se despliega junto**.

## 2. Sus siete características

La segunda diapositiva es una tabla. Textual:

| | Arquitectura Monolítica |
|---|---|
| **Estructura** | Aplicación única y monolítica |
| **Comunicación** | Interna, dentro de la aplicación monolítica |
| **Escalabilidad** | Escalado vertical, toda la aplicación a la vez |
| **Despliegue** | Requiere desplegar toda la aplicación |
| **Mantenibilidad** | Compleja, cambios pueden afectar toda la aplicación |
| **Tecnología** | Uso de una única tecnología/lenguaje de programación |
| **Acoplamiento** | Fuerte acoplamiento entre componentes |

![[adjuntos/capturas-clase-U2/estilos/monolitica-tabla-caracteristicas.png]]

> [!tip] Cómo leer la tabla
> La tabla tiene **una sola columna**, pero su forma (filas de criterios) es la de una
> **comparación**: son exactamente los ejes con que se contrasta un monolito con microservicios.
> La columna de microservicios **no está en la diapositiva**; si te la piden, es complemento.

Tres de las filas se traducen directo a [[Atributos de calidad]]:

| Fila | Atributo que toca | Lectura |
|---|---|---|
| Escalabilidad — *vertical, toda la aplicación a la vez* | escalabilidad | para crecer se agranda **la máquina**, y se escala **todo** aunque solo una parte esté cargada |
| Mantenibilidad — *cambios pueden afectar toda la aplicación* | mantenibilidad | un cambio chico obliga a probar y **redesplegar** todo |
| Acoplamiento — *fuerte entre componentes* | modificabilidad | es la causa de las dos filas anteriores |

**Regla para el examen:** *monolito = una base de código, un despliegue, una tecnología, escalado
vertical, acoplamiento fuerte.*

## 3. El caso de la clase: Amazon Prime Video en AWS

La tercera diapositiva se titula ***"Monolítica en AWS: La Arquitectura de Amazon Prime Video"*** y
muestra un diagrama de servicios de AWS (sin texto explicativo en la diapositiva).

![[adjuntos/capturas-clase-U2/estilos/monolitica-aws-prime-video.png]]

Elementos del diagrama, leídos a resolución completa (no se redibuja):

| Elemento | Qué hace en el diagrama |
|---|---|
| **Customer** | envía el *Audio/video stream* al Media Conversion Service (flecha punteada) e inicia el flujo en la AWS Lambda *Entry point* |
| **AWS Step Functions workflow** | el recuadro que contiene la orquestación |
| **AWS Lambda — Entry point** | manda *Start conversion* al Media Conversion Service y lanza la *Parallel execution* |
| **Media Conversion Service** | convierte el stream y deja *audio/video buffers* en un bucket S3 |
| **Amazon S3 — audio/video buffers bucket** (izquierda) | almacena los fragmentos convertidos; le llega también una flecha punteada desde el bloque *Parallel execution* |
| **Parallel execution**: *AWS Step Functions Detector 1* y *Detector 2*, cada uno con su *Compute unit* | analizan en paralelo |
| **AWS Lambda — Result aggregation** | junta los resultados y manda *Aggregated detection results* (punteada) a un segundo bucket, rotulado también *Amazon S3 audio/video buffers bucket* |
| **Amazon SNS — Customer's real-time notification topic** | recibe los *real-time detection results* desde el Detector 2 |

> [!warning] COMPLEMENTO — lo que la diapositiva no dice, y un posible desfase
> Esto **no está en la diapositiva**; es conocimiento general del caso, y no se pudo verificar
> contra la fuente original durante la toma de esta nota (el artículo ya no está en su URL).
>
> - El caso es un artículo del blog técnico de Prime Video (marzo de 2023) sobre su **servicio de
>   monitoreo de calidad de audio/video**. Contaba que pasaron de una arquitectura **distribuida**
>   (serverless, orquestada con Step Functions y Lambda, con buckets S3 intermedios) a un
>   **monolito** que corre en un solo proceso, y que eso **redujo el costo de infraestructura en más
>   de 90 %** y mejoró la escalabilidad. Tuvo mucha repercusión porque iba contra la moda de los
>   microservicios.
> - **El diagrama de la diapositiva parece ser el de la arquitectura INICIAL, la distribuida** —
>   la que abandonaron—, no el del monolito final: tiene Step Functions, Lambdas separadas,
>   detectores en paralelo y buckets S3 intermedios, que es justo lo que el monolito eliminó (el
>   paso de datos entre componentes por S3 era el costo principal).
> - El artículo trata **un componente** de Prime Video, no toda la plataforma.
>
> Lectura prudente para el examen: el caso sirve como ejemplo de que **un monolito puede ser la
> decisión correcta** (costo, latencia entre componentes). Si hay que describir el diagrama,
> describí lo que se ve y **no afirmes que ese dibujo es "el monolito"** sin preguntarle.

**Lo que enseña el caso (complemento):** elegir estilo es elegir qué sacrificar. Distribuir
componentes que se hablan muchísimo entre sí agrega costo y latencia por cada frontera; juntar todo
en un monolito sacrifica escalado independiente, pero gana en costo y rendimiento. Ver la tabla de
canjes en [[Estilos arquitectónicos]] §9.

---

## Notas relacionadas

- [[Estilos arquitectónicos]] — diseño vs estilo vs patrón, y el catálogo
- [[Arquitectura en capas]] — las mismas tres capas, separadas
- [[Arquitectura en la nube]] — dónde se despliega (el caso Prime Video corre en AWS)
- [[Atributos de calidad]] — escalabilidad, mantenibilidad, rendimiento
- [[Diagrama de despliegue]] — "requiere desplegar toda la aplicación"

## Preguntas de repaso

1. ¿Cuál es, según la clase, la **principal característica** de una arquitectura monolítica?
2. Nombrá las siete filas de la tabla de características y qué dice cada una.
3. ¿Qué significa que la escalabilidad del monolito sea **vertical** y "toda la aplicación a la vez"?
4. ¿Por qué un monolito puede tener capas y seguir siendo monolito?
5. ¿Qué enseña el caso de Prime Video sobre elegir un estilo? ¿Qué muestra realmente el diagrama de la diapositiva?
