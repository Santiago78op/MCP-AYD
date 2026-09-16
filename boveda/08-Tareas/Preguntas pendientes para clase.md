---
tema: Preguntas pendientes
fuente: "Dudas acumuladas al procesar el material de clase. Cada una cita su captura o su nota."
fecha: 2026-09-15
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

---

## Prioridad media — contenido que puede caer

| # | Pregunta | Contexto |
|---|---|---|
| 6 | ¿Va a dar **arquitectura basada en eventos**, **candidata**, **de referencia** y **on premise**? Son del punto 1.9 y no aparecieron | [[Estilos arquitectónicos]] §3 |
| 7 | Los estilos que **solo nombró** (centrada en datos, flujo de datos, llamar y regresar), ¿se evalúan? ¿"Llamar y regresar" **incluye** capas y cliente-servidor, o son estilos separados? | La diapositiva los lista **aparte** |
| 8 | ¿Espera que se distinga **capa** (lógica) de **nivel/tier** (físico), o se usan como sinónimos? | En clase se usan como sinónimos: "2 capas" = cliente-servidor, "N-niveles en la nube" |
| 9 | ¿Hay que **leer o escribir** sintaxis de ADL (Acme), o alcanza con la definición? | [[Lenguajes de descripción de arquitectura]] |
| 10 | ¿Los **paquetes** se evalúan dentro del 1.7 o como diagrama aparte? | capturas_U2 39-41 · [[Diagrama de paquetes]] |
| 11 | El título dice **"2.- Diagrama de Distribución"**: ¿el "1." es el de componentes? ¿Cuál es la serie completa? | capturas_U2 22 y 34 |
| 12 | ¿Los ejemplos de control industrial (**SCADA**, PlantPAx) se evalúan en detalle o solo ilustran qué es un diagrama de bloques? | capturas_U2 14-17 · [[Diagrama de bloques de alto nivel]] |
| 13 | ¿Adopta las convenciones **no estándar** del PDF para secuencia (flechas azules de *Forward*, rojas en `break`, condiciones sin corchetes)? | PDF *Tema 5* págs. 7-8 · [[Diagrama de secuencia]] |
| 14 | La **importación de paquetes**, ¿se evalúa como UML 1.x (no transitiva) o UML 2.x (`«import»` público reexporta, `«access»` no)? | [[Diagrama de paquetes]] §3 |
| 15 | La **dependencia**, ¿incluye el uso por **atributo** (PDF) o solo el uso **temporal** (su tabla de la vista lógica)? | capturas_U2 25 vs. PDF pág. 4 |

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

---

## Del Caso 1 (FarmaHosp), sigue abierta

| # | Pregunta | Estado |
|---|---|---|
| 22 | ¿Qué espera con *"priorizar los 5 drivers más críticos según el **contexto guatemalteco**"*? | **No hay material de clase** sobre cómo priorizar, y "contexto guatemalteco" no está definido en ninguna fuente. Se entregó con un criterio declarado; conviene validarlo |

---

## Resueltas

*(Vacío. Al responder una, moverla acá con la fecha y actualizar la nota que la originó.)*
