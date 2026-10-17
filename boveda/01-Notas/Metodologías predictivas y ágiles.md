---
tema: Arquitectura en el ciclo de vida
fuente: "Presentación de clase (capturas_U3_F1 36-41, 2026-10-16): «Metodología Ágil para la Gestión de Proyectos», «Enfoques de Desarrollo de Proyectos», «Predictivo vrs. Ágil», «Tradicional vrs. Ágil», «Scrum». NÚCLEO. + COMPLEMENTO marcado: los nombres en español de los roles de Scrum y la lectura de las figuras sin texto"
fecha: 2026-10-16
punto_del_programa: "Unidad 3 — Arquitectura en las metodologías: enfoque predictivo y ágil (SCRUM)"
alias: [metodología ágil, metodologías ágiles, predictivo, tradicional, cascada, waterfall, agile, Scrum, Product Owner, Scrum Master, Development Team, planning fallacy, cadencia de entrega]
---

# Metodologías predictivas y ágiles

> [!note] Es el punto 1 de la unidad 3, ahora con láminas de clase
> Hasta el 16/10 este punto estaba solo con complemento en [[Arquitectura y proceso de desarrollo]]
> (Garland & Anthony) y con la NT3 en [[Arquitectura ágil]]. Estas láminas mandan sobre aquella.

## 1. Cómo se elige una metodología — los siete factores

La lámina *"Metodología Ágil para la Gestión de Proyectos"* arranca con una frase entre comillas:

> **"Los mejores equipos entregan pronto y frecuentemente"**

y sigue: *"La metodología a seleccionar dependerá de varios factores"*:

| # | Factor | Lo que aclara la lámina |
|---|---|---|
| 1 | **¿Cómo son los requerimientos?** | *certidumbre de los requisitos* |
| 2 | **Estabilidad del alcance** | — |
| 3 | **Cadencia de entrega** | *momento y frecuencia de los entregables: entrega única, múltiples, periódicas* |
| 4 | **Riesgos** | — |
| 5 | **Seguridad** | — |
| 6 | **Proyecto** | — |
| 7 | **Organización** | — |

**Regla memorizable**: *requisitos inciertos, alcance inestable y entregas frecuentes → ágil;
requisitos ciertos, alcance estable y entrega única → predictivo.*

> [!warning] La trampa
> La lámina no dice que ágil sea siempre mejor: dice que **depende de factores**. Responder *"ágil,
> porque es moderno"* contradice su propia lámina.

![[adjuntos/capturas-clase-U3/metodologias/u3f1-36-factores-para-elegir-metodologia.png]]

## 2. El enfoque tradicional (cascada) — por qué falla en software

La cascada de la lámina: **Requisitos → Diseño → Construcción → Pruebas → Entrega**.

*"Pero... ¿por qué no funciona para el desarrollo de software y las TIC?"*

1. Se enfoca el desarrollo de software con un **modelo de producción**.
2. Se presupone que **los clientes saben exactamente lo que quieren**.
3. Se presupone que **los requisitos no cambian** (o cambian poco).
4. Se planifica con **información incompleta**.
5. **La ejecución no se ajusta al plan.**
6. Se planifica de **modo optimista**: *'Planning fallacy'* (**Kahneman & Tversky, 1979**).

Y en rojo, el veredicto: **"Válido en entornos estables y con certidumbre"**.

> [!tip] La *planning fallacy* (falacia de la planificación)
> Es el sesgo de subestimar el tiempo y el costo de una tarea propia aunque se sepa que las parecidas
> se atrasaron *(definición: complemento; la lámina solo da el nombre, los autores y el enlace)*.

![[adjuntos/capturas-clase-U3/metodologias/u3f1-37-cascada-por-que-no-funciona.png]]

## 3. El enfoque ágil — puesta en marcha

La flecha de la lámina: **AGILE — PLANTEAMIENTO → REQUERIMIENTOS PRIORIZADOS → ITERACIÓN**, rotulada
**PUESTA EN MARCHA**.

Debajo, tres ciclos iguales, cada uno: **Req's → Design → (Develop → Test) → Deploy**, con
**"1-4 Semanas"** al centro y **una caja (un entregable)** al final de cada uno. Las cajas crecen: cada
iteración entrega más producto.

Y la tira de la **Mona Lisa en 6 pasos**: del boceto a lápiz a la obra terminada, pintando primero la
cara y extendiendo el color en cada paso.

| Qué enseña la Mona Lisa | Por qué |
|---|---|
| **Incremental** | cada paso agrega una parte pintada |
| **Iterativo** | desde el paso 1 está el cuadro **entero** en boceto, y se refina |
| **Valor temprano** | lo más importante (la cara) se termina primero = *requerimientos priorizados* |

*(La lectura de la tira es propia: la lámina no trae texto.)*

![[adjuntos/capturas-clase-U3/metodologias/u3f1-38-agil-puesta-en-marcha-mona-lisa.png]]

## 4. Predictivo vs. ágil — diferencias y similitudes

La lámina compara dos líneas de tiempo (*TIME*), con tres paradas cada una, y una leyenda de tres
íconos: **caja de cartón** = *Deliverable Product* (producto entregable), **caja azul** = *Chance of
Failure* (probabilidad de fallar) y **dado rosa** = *Project Run Rate* (ritmo de gasto del proyecto).
Contado con zoom:

| Parada | **Waterfall** | **Agile** |
|---|---|---|
| 1.ª | caja azul + 2 dados | caja de cartón + caja azul + montón de dados |
| 2.ª | caja azul + más dados | caja de cartón **más grande** + caja azul + dados |
| 3.ª | caja azul + **muchos** dados + **recién ahí** las cajas de cartón | caja de cartón **más grande todavía** + caja azul + dados |

**La lectura** *(propia: la lámina solo dice «Diferencias y Similitudes»)*:

- **Diferencia**: en cascada **el producto aparece solo al final** y el gasto (dados) se va
  **acumulando** hasta ahí; en ágil hay **producto en cada parada** y crece de a poco.
- **Similitud**: la **caja azul está en las seis paradas**: los dos enfoques corren riesgo de fallar
  en todo momento. Lo que cambia es que en ágil, si falla, ya hay producto entregado.

![[adjuntos/capturas-clase-U3/metodologias/u3f1-39-predictivo-vs-agil-diferencias.png]]

### Tradicional vs. ágil: dónde aparece el VALOR

| | Tradicional | Ágil |
|---|---|---|
| Ciclo | cascada Requisitos → … → Entrega | ciclos de **1-4 semanas** |
| Flecha verde **VALOR** | **una sola**, al final, en la *Entrega* | **una por iteración**, después de cada *Deploy* |
| Eje | TIEMPO | TIEMPO |

**La idea que hay que llevarse**: en la cascada el cliente recibe valor **una vez**, al final; en ágil
lo recibe **en cada iteración**.

![[adjuntos/capturas-clase-U3/metodologias/u3f1-40-tradicional-vs-agil-valor.png]]

## 5. Scrum — los tres roles del Scrum Team

| Rol (lámina) | Lo que dice la lámina | En español *(complemento)* |
|---|---|---|
| **Product Owner** | *Manages the Product Backlog. Optimizes value of the Product* | dueño del producto: gestiona la pila del producto y maximiza su valor |
| **Scrum Master** | *Manages the Scrum process. Removes Impediments* | facilitador: cuida el proceso y quita impedimentos |
| **Development Team** | *Manages itself. Creates "Done" Increments* | equipo autoorganizado que produce incrementos *terminados* |

Los tres se superponen dentro de un recuadro rotulado **Scrum Team**: el equipo Scrum son los tres
roles, no solo los desarrolladores.

> [!warning] La trampa
> El **Scrum Master no es el jefe** del equipo: *maneja el proceso*, no a las personas. El equipo de
> desarrollo **se gestiona a sí mismo**. Y quien prioriza qué se hace es el **Product Owner**, a
> través del backlog.

![[adjuntos/capturas-clase-U3/metodologias/u3f1-41-scrum-roles.png]]

El sprint, las ceremonias, las responsabilidades de cada rol y **los 14 pasos de Scrum en la
arquitectura** están en [[Proceso Scrum en la arquitectura de software]].

## 6. Y la arquitectura, ¿dónde entra?

Las láminas no lo dicen en esta serie, pero el mismo bloque de clase sigue con
[[Proceso general de diseño de la arquitectura]] y [[Ciclo de desarrollo de la arquitectura]]: el ciclo
de la arquitectura (requerimientos, diseño, documentación, evaluación, implementación) **se mapea** sobre
las actividades técnicas del desarrollo, sea cual sea la metodología. Para el cruce con ágil, la NT3
propone los **RSA** → [[Arquitectura ágil]] y [[Requisitos significativos para la arquitectura]].

## Preguntas de repaso

1. ¿Qué frase abre la lámina de metodología ágil, y de qué siete factores depende la elección?
2. Nombrá cuatro razones por las que la cascada no funciona en software. ¿Qué es la *planning fallacy*?
3. ¿En qué entornos sí es válida la cascada, según la lámina?
4. ¿Qué muestra la tira de la Mona Lisa sobre iterativo e incremental?
5. ¿Cuántas veces aparece la flecha VALOR en el enfoque tradicional y cuántas en el ágil?
6. ¿Cuáles son los tres roles de Scrum y qué hace cada uno según la lámina?
