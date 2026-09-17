---
tema: Preguntas pendientes
fuente: "Dudas acumuladas al procesar el material de clase. Cada una cita su captura o su nota."
fecha: 2026-09-16
alias: [preguntas, dudas, preguntas para la catedrática, preguntas pendientes]
---

# Preguntas pendientes para clase

Lo que **no se puede resolver con el material** y hay que preguntarle a la catedrática o al auxiliar.
Regla de la bóveda: si el material es ambiguo, **no se asume en silencio** — se anota acá y, si hay
que entregar igual, se declara la asunción en el entregable.

**Cómo usar este archivo:** llevá las de prioridad alta a la próxima clase. Cuando una se responda,
moverla a *Resueltas* con la fecha y **actualizar la nota que la origina**.

---

## Prioridad alta — afectan qué se estudia o cómo se dibuja en el examen

| # | Pregunta | Por qué importa | Dónde está la evidencia |
|---|---|---|---|
| 1 | **¿Qué entra en el segundo parcial (19/09)?** ¿El material nuevo de "cómo se modela" y estilos, o Calidad del Software (unidad 2 del programa)? | Las capturas nuevas cubren **1.4, 1.5, 1.7 y 1.9**; de **Calidad del Software no hay ninguna presentación**. Si entra Calidad, se estudia solo con complemento | `Programa oficial del curso` · [[Atributos de calidad]] |
| 2 | **La realización de interfaz, ¿se dibuja con línea llena rotulada o punteada con triángulo hueco?** | Sus diagramas de clases usan **línea llena rotulada "Realización"**; su lámina de UML 2.x usa la **punteada con triángulo**. Las dos son de clase | capturas_U2 26-28, 54, 56 vs. 32 · [[Relaciones y dependencias en UML]] |
| 3 | **Dentro de un nodo, ¿van artefactos o componentes?** | El PDF *Tema 5* pone **artefactos** con `«manifest»`; sus capturas ponen **componentes** dentro del nodo | capturas_U2 57-58 vs. PDF págs. 5-6 · [[Diagrama de despliegue]] |
| 4 | **¿Exige las reglas de notación del PDF *Tema 5*** (camelCase, tipos en atributos, `<<Interface>>`) **aunque sus propios ejemplos no las sigan?** | Su diagrama del parque usa mayúscula inicial, sin tipos y `<<Interfaz>>` | capturas_U2 56 vs. PDF pág. 3 · [[Diagrama de clases]] |
| 5 | **En el 4+1, ¿qué nomenclatura quiere?** ¿"Vista de Despliegue" = componentes (unidad 1) o *Implementation / Deployment View* (figura nueva)? | Con el nombre cruzado, una respuesta correcta puede leerse como incorrecta | capturas_U2 2 y 37 · [[Modelo 4+1 vistas]] |
| 23 | **¿Qué definición de estilo arquitectónico espera en el examen?** A: *"establece las restricciones sobre la arquitectura de una familia de diseños arquitectónicos"*. B: *"establece un marco de referencia a partir del cual es posible construir aplicaciones que comparten un conjunto de atributos y características"* | Las dos son de clase y ella no elige. Mientras tanto: citar la A y agregar la B como complemento de la idea | capturas_U2 21 = U2_F2 14 vs. U2_F2 6 · [[Estilos arquitectónicos]] §1 |
| 24 | **¿Qué taxonomía de estilos usa?** Sus dos diapositivas "Catálogo de Estilos" no coinciden: la de texto pone **peer-to-peer como familia**, con eventos y servicios adentro; el árbol C&C pone **Event-based como familia**, y peer to peer y SOA cuelgan de **Call-return**. Además, SOA y pizarra tienen dos padres | Una pregunta del tipo *"¿a qué familia pertenece SOA?"* tiene dos respuestas de clase | capturas_U2_F2 30 vs. 30-componentes-conectores · [[Catálogo de estilos arquitectónicos]] §4 |

---

## Prioridad media — contenido que puede caer

| # | Pregunta | Contexto |
|---|---|---|
| 6 | ¿Va a dar **arquitectura basada en eventos** y **on premise**? *(Candidata y de referencia ya se dieron: ver Resueltas.)* Eventos (EDA) está **nombrada** en tres diapositivas pero no se desarrolló; on premise sigue sin ninguna | capturas_U2_F2 9, 30, 30-cc · [[Estilos arquitectónicos]] §3 |
| 7 | Los estilos que **solo nombró** (centrada en datos, flujo de datos, llamada y retorno, **REST**, microkernel), ¿se evalúan? *(Si "llamada y retorno" incluye capas ya está resuelto: ver Resueltas.)* | La lista de 9 (capturas_U2_F2 9) nombra REST y microkernel sin ninguna diapositiva que los desarrolle |
| 8 | ¿Espera que se distinga **capa** (lógica) de **nivel/tier** (físico), o se usan como sinónimos? | En clase se usan como sinónimos: "2 capas" = cliente-servidor, "N-niveles en la nube" |
| 9 | ¿Hay que **leer o escribir** sintaxis de ADL (Acme), o alcanza con la definición? | [[Lenguajes de descripción de arquitectura]] |
| 10 | ¿Los **paquetes** se evalúan dentro del 1.7 o como diagrama aparte? | capturas_U2 39-41 · [[Diagrama de paquetes]] |
| 11 | El título dice **"2.- Diagrama de Distribución"**: ¿el "1." es el de componentes? ¿Cuál es la serie completa? | capturas_U2 22 y 34 |
| 12 | ¿Los ejemplos de control industrial (**SCADA**, PlantPAx) se evalúan en detalle o solo ilustran qué es un diagrama de bloques? | capturas_U2 14-17 · [[Diagrama de bloques de alto nivel]] |
| 13 | ¿Adopta las convenciones **no estándar** del PDF para secuencia (flechas azules de *Forward*, rojas en `break`, condiciones sin corchetes)? | PDF *Tema 5* págs. 7-8 · [[Diagrama de secuencia]] |
| 14 | La **importación de paquetes**, ¿se evalúa como UML 1.x (no transitiva) o UML 2.x (`«import»` público reexporta, `«access»` no)? | [[Diagrama de paquetes]] §3 |
| 15 | La **dependencia**, ¿incluye el uso por **atributo** (PDF) o solo el uso **temporal** (su tabla de la vista lógica)? | capturas_U2 25 vs. PDF pág. 4 |
| 25 | ¿Cómo define **arquitectura candidata**? La diapositiva se titula *"Definición de una arquitectura candidata"* pero solo muestra la tabla conceptual / modular / código / ejecución, sin ninguna frase de definición | capturas_U2_F2 25 · [[Arquitectura de referencia]] §4 — por ahora se define con el flujo de Ambler (unidad 1) |
| 26 | **La tercera categoría de estructuras, ¿"asignación" o "de localización"?** Mismo concepto con dos nombres en dos láminas suyas (y la segunda dice *"Componentes-y-Conector"*) | captura del 19/08 vs. capturas_U2_F2 27 · [[Categorías de estructuras]]. Mientras tanto: *"asignación (o de localización)"* |
| 27 | **¿El diagrama de paquetes va en la vista lógica, en la de desarrollo o en las dos?** Sus diapositivas del 4+1 lo ponen en las dos; el PDF *Tema 5*, solo en la de desarrollo | capturas_U2_F2 11-12 vs. PDF pág. 1 · [[Modelo 4+1 vistas]] |

---

## Sobre láminas concretas — posibles erratas

| # | Pregunta | Qué se ve |
|---|---|---|
| 16 | **Captura 51 (Prime Video)**: ¿el diagrama es el **monolito** o la arquitectura **distribuida previa**? | Se titula "Monolítica en AWS", pero muestra Step Functions, Lambdas y buckets intermedios — que es lo que Amazon **abandonó** al pasar al monolito |
| 17 | **Captura 49 (clínica veterinaria)**: ¿las flechas de BBDD y Servicios hacia Lógica de negocio apuntan así a propósito? | Según la convención de dependencia, diría que **la base usa la lógica** |
| 18 | **Captura 55 (CDU del parque)**: el actor lleva la **barra diagonal de negocio** en una lámina rotulada "CDU EXPANDIDOS", y *Gestión Ficha Montaña Rusa* y *Generar Alerta* **no tienen actor** | Choca con el convenio "un CU sin actor es un error" y mezcla planos |
| 19 | **Captura 56 (clases del parque)**: ¿por qué eliminó la clase **CRA** del PDF y la reemplazó por **Averías** más dos interfaces? ¿Es el criterio que espera al pasar de clases a componentes? | También renombra *Torniquete* a *Molinete* y `-NúmSerieVagón()` es un atributo con paréntesis |
| 20 | **Captura 31**: ¿cuál de los dos dibujos es la forma **icónica** y cuál la **expandida**? ¿Qué significa el estereotipo `«Annotation»`? | La diapositiva no los rotula |
| 21 | **Captura 58**: ¿*Gestión de Atracciones* es FrontEnd o BackEnd? | La zona naranja casi no la cubre |
| 28 | **capturas_U2_F2 1 (árbol de patrones)**: *SOA*, *Comunicación* y *Cloud* están en cajas naranjas **sin línea** que las una a la rama de patrones arquitectónicos. ¿Son más categorías o se refieren a otra cosa? | Solo Integración, Seguridad y Web están conectadas | [[Patrones arquitectónicos]] |
| 29 | **capturas_U2_F2 36 (Kiviat)**: ¿un valor alto significa **más flexible** o **más prioritario**? | La lámina no define la escala; la nota lo lee como flexibilidad, y eso es interpretación |

---

## Del Caso 1 (FarmaHosp), sigue abierta

| # | Pregunta | Estado |
|---|---|---|
| 22 | ¿Qué espera con *"priorizar los 5 drivers más críticos según el **contexto guatemalteco**"*? | **No hay material de clase** sobre cómo priorizar, y "contexto guatemalteco" no está definido en ninguna fuente. Se entregó con un criterio declarado; conviene validarlo |

---

## Resueltas

Al responder una, moverla acá con la fecha y actualizar la nota que la originó.

| Era | Pregunta | Respuesta | Cómo se resolvió |
|---|---|---|---|
| 6 (en parte) | ¿Va a dar arquitectura **candidata** y **de referencia**? | **Sí, se dieron.** Referencia: *"un modelo de referencia mapeado en elementos de software…"*; candidata: la tabla de cuatro tipos | Con material de clase, capturas_U2_F2 23-26, el 2026-09-16 · [[Arquitectura de referencia]] |
| 7 (en parte) | ¿"Llamada y retorno" **incluye** capas? | **Sí.** *"Arquitecturas de llamada y retorno (llamadas a procedimientos remotos, Modelo Vista Controlador –MVC–, en Capas, Orientadas a Objetos, basadas en Componentes)"*. En el árbol C&C, client-server y multi-tier también cuelgan de call-return | Con material de clase, capturas_U2_F2 30 y 30-cc, el 2026-09-16 · [[Catálogo de estilos arquitectónicos]] |
