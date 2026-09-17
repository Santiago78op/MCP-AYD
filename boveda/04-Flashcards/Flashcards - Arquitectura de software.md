---
tema: Arquitectura de software
fuente: "Arquitectura de Software.pdf / Arquitectura de Software (1).pdf + capturas_U2_F2 (10-13, 29: 4+1 vistas · 27, 28, 31-38: fundamentos) + capturas_U2 (2)"
fecha: 2026-08-19
---

# Flashcards — Arquitectura de software

Compatible con el plugin **Spaced Repetition** de Obsidian: cada tarjeta es una línea con la
pregunta, el separador de dos signos de dos puntos, y la respuesta.

#flashcards/arquitectura

Según IEEE 1471, ¿qué es la arquitectura de software?::La organización fundamental de un sistema descrita en sus componentes, la relación entre ellos y con el ambiente, y los principios que guían su diseño y evolución.

¿Cuál es el criterio de Grady Booch para decidir si algo es arquitectura?::"Toda la arquitectura es diseño, pero no todo el diseño es arquitectura." Lo significativo se mide por el **costo del cambio**: si cambiarlo sale caro, es arquitectura.

¿Qué fórmula explica por qué creció la importancia de la arquitectura?::Escala + Complejidad + Distribución = **Riesgos**.

¿Qué diferencia hay entre una **estructura** y una **vista** arquitectónica?::La estructura es el conjunto de elementos *en sí*, tal como existen en el software o hardware. La vista es la *representación* de esa estructura para las partes interesadas. Los arquitectos diseñan estructuras y documentan vistas.

¿Qué es un **punto de vista arquitectónico**?::Una plantilla que describe la forma de crear y utilizar una perspectiva de la arquitectura; incluye nombre, socios, problemas abordados, y el modelado y las convenciones analíticas.

¿Cuáles son las cinco vistas del modelo 4+1?::Vista lógica, vista de procesos, vista de despliegue (o desarrollo), vista física y la vista "+1" de escenarios.

¿Qué diagramas UML acompañan a cada vista del modelo 4+1?::Lógica → clases y paquetes. Procesos → actividad. Despliegue/desarrollo → componentes y paquetes. Física → deployment. Escenarios (+1) → casos de uso.

¿Por qué la quinta vista del modelo 4+1 se llama "+1"?::Porque no es una vista más al mismo nivel: los casos de uso **unen** las otras cuatro y dan trazabilidad de componentes, clases, equipos y paquetes para la realización de cada caso de uso.

¿En qué vista del modelo 4+1 aparecen los requisitos no funcionales?::En la **vista de procesos**: ejecución, disponibilidad, tolerancia a fallas, integridad, seguridad y confiabilidad, entre otros.

¿Cuáles son las cuatro influencias en la arquitectura?::Stakeholders, organizaciones de desarrollo, ambiente técnico y experiencia del arquitecto. Stakeholders + organizaciones de desarrollo producen los requisitos de calidad.

¿Por qué el ciclo de influencias es un ciclo y no una secuencia?::Porque el **sistema construido retroalimenta a sus propias influencias**: cambia lo que esperan los stakeholders, la organización que lo mantiene, el ambiente técnico y la experiencia del arquitecto.

¿Cuáles son los tres beneficios de una arquitectura de software?::1) Proporciona la comunicación entre stakeholders. 2) Manifiesta las decisiones de diseño tempranamente. 3) Las arquitecturas como modelo reusable y transferible.

¿Cuáles son los cuatro pasos del proceso de diseño arquitectónico?::1) Diseño de los datos. 2) Obtención de las representaciones de la estructura arquitectónica. 3) Análisis de alternativas de estilos o patrones arquitectónicos. 4) Elaboración de la arquitectura con un método de diseño. **Ojo:** son los cuatro del **deck en PDF**; hay otras dos versiones de "los pasos" en el material — la lista de **7 actividades** y las **8 etapas** de la Figura 2-8. No confundirlas.

¿Qué cuatro propiedades se revisan en las comprobaciones de cada etapa del diseño?::Que los productos sean **claros, correctos, completos y consistentes** con los requerimientos y entre sí.

¿De qué tipo de requerimientos es responsable el arquitecto según SUN SL-425?::De integrar los **requerimientos no funcionales (NRFs)** en el sistema. Además visualiza el comportamiento, crea los planos y define cómo trabajan juntos los elementos.

¿Cuáles son las tres restricciones del triángulo del proyecto (van sobre los lados, no en los vértices) y qué frase lo resume?::Cost/Resources, Scope y Time/Schedule. "I can make it for you fast, cheap, or good. Pick any two."

¿Qué mide un diagrama de Kiviat en este contexto y cuáles son sus ejes?::Mide la **flexibilidad** del proyecto —cuánto se puede mover cada dimensión— sobre cinco ejes: features, quality, cost, schedule y staff.

Completá: la arquitectura del software es el resultado de equilibrar ______ y ______.::Requisitos funcionales y calidad.

¿Por qué la arquitectura no es una fase del ciclo de vida?::Porque es un **proceso iterativo** a través de requisitos y calidad: se va y se vuelve entre requisitos, atributos de calidad y decisiones de diseño.

¿Qué significa "menos es más" como beneficio de la arquitectura?::Que un **vocabulario restringido de alternativas de diseño** es bueno: un equipo con pocas formas acordadas de hacer las cosas es más consistente y más rápido que uno donde cada quien inventa.

En el material hay **tres** versiones de "los pasos para definir una arquitectura". Nombralas y decí qué aporta cada una.::**1)** Los **4 pasos** del deck en PDF (datos → representaciones → alternativas de estilos → método de diseño). **2)** La lista de **7 actividades** (caso de negocio, requisitos, creación y selección, documentación, evaluación, implementación, aseguramiento) — es la más citable porque está en viñetas. **3)** Las **8 etapas** de la Figura 2-8 en 4 fases, con el **paso 0** (caso de negocio) y los lazos de refinamiento — la única que trae **experimentación** y una **decisión de ir/no ir**. Se reconcilian en [[Proceso de diseño arquitectónico]].

Si en un parcial preguntan "¿cuáles son los pasos?" sin más contexto, ¿qué conviene responder?::La **lista de 7**: es la que ella dio en viñetas y la más reconocible. Y agregar una línea diciendo que el método completo (Figura 2-8) las organiza en **8 etapas y 4 fases** con el caso de negocio como **paso 0**. Eso demuestra que conocés las tres sin contradecirte.

## Clase — capturas_U2_F2 (2026-09-16) — 4+1 vistas

Según la clase, ¿por qué es frecuente separar una arquitectura en vistas?::Porque las arquitecturas del sistema son usadas por **diversos conjuntos de personas en tiempos diferentes** del ciclo de desarrollo.

¿Qué proceso identifica el conjunto estándar de vistas llamado "4+1 Vistas de Arquitectura", según la clase?::El **RUP** (Proceso Unificado Racional). El autor original del modelo es Kruchten, pero ella lo atribuye al RUP.

¿Qué tres cosas permite el enfoque 4+1 a los grupos de participantes?::1) **Comunicar las necesidades** (es decir, requisitos). 2) **Resolver los conflictos**. 3) **Realizar los documentos de decisiones**.

¿Con qué diagramas UML se complementa la vista lógica?::Diagrama de **clases** y diagrama de **paquetes**.

¿Con qué diagrama UML se complementa la vista de procesos, según sus diapositivas?::Solo con el diagrama de **actividad** (no secuencia). Lo confirma también el PDF TEMA 5.

¿Con qué diagramas UML se complementa la "Vista de Despliegue o Vista de Desarrollo"?::Diagrama de **componentes** y diagrama de **paquetes**. Ojo: pese al nombre, NO lleva el diagrama de despliegue.

¿Con qué diagrama UML se complementa la vista física?::Con el **diagrama de deployment** (= despliegue = distribución). Los elementos de la vista lógica se mapean a componentes de software o de hardware.

¿Qué diagrama aparece en dos vistas del 4+1 y por qué no es un error?::El de **paquetes**: en la **lógica** (agrupa clases) y en la de **despliegue/desarrollo** (agrupa componentes). El paquete es un mecanismo de agrupación que sirve para cualquier elemento UML.

¿Qué participante le corresponde a cada vista en la figura en inglés de la clase?::Logical View → Analyst y End user · Implementation View → Programmer · Process View → System Integrator · Deployment View → System Administrator · Use Case View al centro, sin participante.

Regla para no confundir los nombres de vistas del 4+1::**Componentes y paquetes → vista de desarrollo/implementación** (sus diapositivas la llaman "de Despliegue o de Desarrollo"). **Nodos y hardware → vista física** (la figura en inglés la llama "Deployment View"). La palabra "despliegue" cambia de lado; el contenido no.

## Clase — capturas_U2_F2 (2026-09-16) — fundamentos

En la lámina *"Estructuras"*, ¿con qué tres nombres aparecen las categorías de estructuras?::**Módulos**, **Componentes-y-Conector** y **De Localización**. Son las mismas tres de la lámina "Categorías de Estructuras" con otros nombres.

¿A qué categoría corresponden las estructuras **"De Localización"**?::A las de **asignación**. Las dos muestran la relación del software con lo que no es software: donde es **ejecutado** (CPU, redes) y donde es **creado** (equipos de desarrollo). En el examen escribí "asignación (o de localización)".

Según la lámina *"Estructuras"*, ¿qué son los elementos de una estructura de módulos?::Módulos, que son **unidades de implementación**.

Según la lámina *"Estructuras"*, ¿qué son los componentes y qué son los conectores?::Los componentes son **componentes de ejecución** (principalmente **unidades de computación**); los conectores son el **vehículo de comunicación** entre los componentes.

¿Qué muestran las estructuras **De Localización**?::La relación entre los elementos de software y los elementos en **uno o más ambientes externos** en los cuales el software es **creado o ejecutado**.

Definición básica de Arlow y Neustadt (2005)::La arquitectura de software de un programa o sistema de computación es **la estructura o estructuras del sistema**, las cuales comprometen **elementos de software**, las **propiedades externamente visibles** de esos elementos y las **relaciones** entre ellos.

¿Con qué compara la clase a la arquitectura de software y qué atributos dice que garantiza?::Con los **planos de una casa** (bases, distribución, pasillos de interacción). Idea y construye los planos de aplicaciones y canales digitales, y garantiza que funcionen de manera óptima entregando **calidad, disponibilidad y seguridad**, entre otros atributos.

¿Cuántos términos define la terminología de clase y cuáles son?::**Siete**, en dos láminas. Arquitectura, arquitecto y arquitecting · sistema, descripción de la arquitectura, perspectiva de la arquitectura y punto de vista arquitectónico.

¿Qué cuatro cosas incluye un **punto de vista arquitectónico**?::Un **nombre**, **socios**, los **problemas más abordados** por el punto de vista, y el **modelado y las convenciones analíticas**.

En el Kiviat de ejemplo, ¿qué ejes quedan casi en 0 y qué significa si "alto = más flexible"?::**Schedule** y **Staff**: la fecha y el personal **no se pueden mover**. *Features* (~8) es lo más negociable. Ojo: la lámina no define la escala, declarala antes de interpretar.
