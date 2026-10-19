---
tema: Guion de exposición
fuente: "Presentación del Caso Harley-Davidson (13 láminas) y Entrega - Caso Harley-Davidson"
fecha: 2026-10-13
tarea: Caso Harley-Davidson
alias: [guion harley, guion presentación, guion HD, exposición harley]
---

# Guion — Presentación del Caso Harley-Davidson (SiL'K)

**Grupo 2 · martes 13 de octubre de 2026 · 10 minutos.**
Presentación para exponer: `08-Tareas/Grupo2_CasoHD_Presentacion_azul.pptx` (PowerPoint o Keynote, sin conexión).
Documento: `08-Tareas/Grupo2_CasoHD.pdf`

## El hilo: seguir un pedido

La exposición no recorre la rúbrica en orden: sigue **un pedido de piezas** desde que alguien lo pide
hasta que se paga. Cada lámina contesta una pregunta sobre ese pedido, y la etiqueta «Criterio N» de
la esquina dice qué parte de la rúbrica cubre. El orden queda: criterio 1, 3, 5, 6, 2 y 4.

Las versiones anteriores quedan de respaldo: `Grupo2_CasoHD_Presentacion.pptx` (orden por criterio,
fondo negro y naranja) y `Grupo2_CasoHD_Presentacion_pedido.pptx` (este orden, colores anteriores).

## Antes de entrar

- Abrí `Grupo2_CasoHD_Presentacion_azul.pptx` y empezá la presentación desde la primera lámina.
- Se avanza con la flecha derecha o la barra espaciadora. **Cada clic hace una sola cosa**: o trae
  una tarjeta, o pasa de lámina. Son 23 clics de tarjetas y 12 cambios de lámina.
- Los diagramas aparecen con la lámina; las tarjetas y las filas entran una por clic.
- Este guion también va en las **notas del orador** de cada lámina, con la marca `[CLIC]`.
- Los títulos van en Georgia y el resto en Arial: las dos están en Windows y en macOS.
- Tené el PDF de la entrega abierto en otra ventana por si piden ver una matriz o un escenario.

## El reloj

| # | Lámina | Clics | Tiempo | Acumulado |
|---|---|---|---|---|
| 1 | Portada | 0 | 0:20 | 0:20 |
| 2 | El caso | 3 | 0:50 | 1:10 |
| 3 | Seis actores, cuatro procesos | 0 | 1:00 | 2:10 |
| 4 | Diagrama de contexto | 0 | 0:45 | 2:55 |
| 5 | Drivers | 3 | 1:10 | 4:05 |
| 6 | SOA | 4 | 1:10 | 5:15 |
| 7 | Diagrama de bloques | 0 | 0:40 | 5:55 |
| 8 | Diagrama de despliegue | 0 | 0:50 | 6:45 |
| 9 | Modelo de calidad | 2 | 1:15 | 8:00 |
| 10 | Stakeholders | 4 | 0:40 | 8:40 |
| 11 | Matrices | 4 | 0:50 | 9:30 |
| 12 | Cierre | 3 | 0:30 | 10:00 |
| 13 | Referencias | 0 | no se expone | — |

Las frases de enganche suman unos cinco segundos por lámina. Si a los cinco minutos todavía no
llegaste al diagrama de bloques, recortá esa lámina a una frase.

---

## 1 · Portada — 0:20

> Buenos días. Somos el Grupo 2. El caso es de Harvard y cuenta cómo Harley-Davidson eligió un
> software de compras en 1998. Nuestra tarea no fue elegir el proveedor: fue definir la arquitectura
> que ese proyecto, SiL'K, necesitaría hoy. En vez de recorrer la rúbrica en orden, vamos a seguir
> un pedido de piezas desde que alguien lo pide hasta que se paga. Arriba de cada lámina está el
> criterio que cubre.

## 2 · El caso — 0:50

Un clic por cada cifra.

> Empecemos por qué importa ese pedido.
>
> Tres datos explican por qué existe SiL'K.
> *(clic)* Entre el 55 y el 60 por ciento del valor de una motocicleta son piezas compradas.
> *(clic)* El personal de Compras pasa el 85 por ciento de su tiempo en tareas no estratégicas,
> cuando la meta era dedicar el 70 por ciento a los proveedores.
> *(clic)* Y son siete centros, cada uno con su propio sistema de compras.
>
> La trampa del caso es el título: casi todo el relato narra un concurso de proveedores de software,
> pero ese no es el negocio. El negocio es la gestión de suministros y compras. Esa frontera decide
> todo lo demás: los compradores son trabajadores del negocio, y los actores son el proveedor y las
> áreas que piden, reciben y pagan.

## 3 · Seis actores, cuatro procesos — 1:00

> ¿Por dónde pasa el pedido? Este es el negocio. Criterio uno.
>
> El core es una sola elipse, la gestión de suministros y compras, con seis actores: el proveedor y
> cinco áreas. Aplicamos la regla de clase: las áreas son actores, las personas son trabajadores.
>
> La primera descomposición tiene cuatro procesos: requisición y pedido, recepción y pago, relación
> con suministradores, y compras en proyectos de nuevos productos. Salen de las tres fases del anexo
> 6b del caso; la primera la partimos en dos porque quien pide no es quien recibe ni quien paga.
>
> Quédense con esto: estos cuatro procesos van a ser después los cuatro servicios de la arquitectura.

## 4 · Diagrama de contexto — 0:45

> Mientras el pedido viaja, el software intercambia información con todos estos.
>
> Sigue siendo el criterio uno. El Producto es el software SiL'K, la elipse del centro; los rectángulos son las
> entidades externas. Arriba y a la izquierda están las personas y las áreas; a la derecha, el
> suministrador y la recepción; abajo, los sistemas que ya existen. Son diez entidades y diecinueve
> flujos, y cada flecha lleva nombre en sustantivo.
>
> Un detalle: el comprador aparece aquí como entidad externa al software, aunque dentro del negocio
> es un trabajador. Cambia la lente, no la persona.

## 5 · Drivers — 1:10

Un clic por tarjeta.

> ¿Qué le exige ese pedido al sistema?
>
> Criterio tres: los tres tipos de driver.
> *(clic)* Dieciocho funcionales, entregados como casos de uso expandidos: veinte casos en cuatro
> diagramas, y ninguno es un «crear, editar o consultar».
> *(clic)* Nueve de calidad, escritos como escenarios de atributos de calidad, los EaC, con sus seis
> partes: fuente de estímulo, estímulo, artefacto, entorno, respuesta y medida. Sin medida no es un
> driver. Los tres de prioridad alta y alta son disponibilidad del 99,9 por ciento, seguridad y
> compatibilidad.
> *(clic)* Y dieciséis de restricción: no es un ERP, va en tres fases, tiene que ser compatible con
> lo existente y no puede parar la línea de producción. Las restricciones no se priorizan.
>
> Una aclaración honesta: el caso da cifras de negocio, no de comportamiento del sistema. Las medidas
> las derivamos de sus volúmenes y lo declaramos como supuesto.

## 6 · SOA — 1:10

Un clic por escalón; la escalera sube de izquierda a derecha.

> ¿Cómo lo atendemos?
>
> Criterio cinco. El estilo principal es SOA, con un servicio por proceso de negocio. Lo justificamos
> con la escalera de la lámina de clase.
> *(clic)* Define las necesidades del negocio. *(clic)* Desarrolla los procesos como servicios: son
> los cuatro de la descomposición, así que la granularidad ya venía decidida. *(clic)* Cada servicio
> evoluciona por separado, una fase a la vez. *(clic)* Y se distribuye en varios niveles: centros,
> filiales y suministradores.
>
> La razón de fondo es de integración: hay que convivir con los sistemas de cada planta. Lo
> complementamos con capas dentro de cada servicio y eventos entre servicios. Y descartamos el
> monolítico porque el propio equipo dijo que no buscaba un ERP completo.

## 7 · Diagrama de bloques — 0:40

> Así viaja el pedido por dentro.
>
> Este es el diagrama de bloques, con el molde del ejemplo de clase: a la izquierda los productores
> de eventos, al centro el enrutador y a la derecha los consumidores. Cada flecha lleva el evento que
> transporta. Quien produce un evento no conoce a quien lo consume: si el sistema de una planta se
> cae, los demás siguen. Eso responde a la restricción de no parar la producción.

## 8 · Diagrama de despliegue — 0:50

> Y aquí es donde ocurre.
>
> El despliegue tiene cuatro zonas. Arriba, en verde, los dispositivos: la PC, la tableta del muelle
> y el suministrador por Internet. Al centro, en naranja, la nube: una sola entrada, el clúster con un
> servicio por proceso, el bus de eventos y la base de datos con su réplica. A la derecha, en
> amarillo, lo que ya existe: el MRP de cada planta y Cuentas de Acreedores.
>
> Lo existente no se mueve: se conecta. El caso no trae hardware, así que el dimensionamiento es un
> supuesto declarado.

## 9 · Modelo de calidad — 1:15

Un clic para la tabla y otro para la frase de abajo.

> ¿Cómo sabemos que el pedido llegó bien?
>
> Criterio seis, que tiene dos partes. La primera: los siete pasos para definir la arquitectura. En
> el documento indicamos, paso por paso, qué drivers de calidad y de restricción lo condicionan; por
> ejemplo, las tres fases y no parar la línea condicionan la implementación.
>
> *(clic)* La segunda: el modelo de calidad. Seguimos el pensamiento ISO como familia de normas. La
> 9126 tiene seis características; la serie 25000 la sucede, y adoptamos la 25010 porque ahí
> seguridad y compatibilidad son características de primer nivel, y son las que más pesan en este
> caso. Cada característica queda con su escenario, su decisión de arquitectura y su umbral.
> *(clic)* Y se mide dos veces: antes de construir y al cerrar cada fase.

## 10 · Stakeholders — 0:40

Un clic por tarjeta.

> ¿A quién le importa que ese pedido salga bien?
>
> Criterio dos: diecisiete interesados. Entra a la lista quien aporta un interés que ningún otro trae.
> *(clic)* Cinco patrocinan y deciden. *(clic)* Seis usan el sistema: unos 200 compradores, más de
> 2.000 solicitantes y cuatro áreas vecinas. *(clic)* Cuatro regulan y acompañan, entre ellos el
> grupo que fija las normas de arquitectura. *(clic)* Y dos son externos.
>
> Ojo: el caso llama «suministrador» tanto al proveedor de piezas como al de software. El primero es
> actor del negocio; el segundo solo es stakeholder del proyecto.

## 11 · Matrices — 0:50

Un clic por fila.

> Y la prueba de que nada quedó suelto.
>
> Criterio cuatro: las cuatro matrices que pide la rúbrica.
> *(clic)* Stakeholders contra requerimientos: ningún requerimiento queda sin dueño.
> *(clic)* Requerimientos contra casos de uso: todo requerimiento se realiza.
> *(clic)* Stakeholders contra casos de uso: no la llenamos a mano, sale de cruzar las dos anteriores,
> así que no puede contradecirlas.
> *(clic)* Y requerimientos contra requerimientos, que es de dependencias: muestra que el registro
> único de suministradores sostiene a otros seis requerimientos. Eso nos dice qué construir primero.

## 12 · Cierre — 0:30

Un clic por idea.

> Para cerrar, tres ideas. *(clic)* Los cuatro procesos son los cuatro servicios. *(clic)* Lo
> existente se integra por eventos, no se reemplaza. *(clic)* Y cada escenario de calidad tiene
> medida y umbral.
>
> No elegimos proveedor porque el caso no lo decide y la rúbrica no lo pide: la arquitectura sirve
> con cualquiera de los tres finalistas. Gracias. ¿Preguntas?

## 13 · Referencias

No se expone. Queda de respaldo si preguntan de dónde sale algo.

---

## Preguntas que pueden hacer

| Pregunta | Respuesta corta |
|---|---|
| ¿Por qué el negocio no es Harley-Davidson entera? | Porque el caso delimita el ámbito de SiL'K en su anexo 6a: seis actividades dentro y tres fuera. Modelar toda la empresa dejaría el sistema chico frente al negocio |
| ¿Por qué el comprador no es actor? | Está dentro de la frontera: ejecuta el negocio. Los actores son los de afuera. Frente al software sí es entidad externa, y por eso está en el contexto |
| ¿De dónde salen el 99,9 % y los 2 segundos? | Son supuestos de diseño. El caso solo trae cifras de negocio; las derivamos de sus volúmenes (800 usuarios objetivo) y lo declaramos en el documento |
| ¿Por qué SOA y no microservicios? | La granularidad por proceso ya alcanza, y el núcleo es un paquete de mercado. Partir más fino multiplica la operación sin un driver que lo pida |
| ¿Por qué no un ERP? | El caso lo prohíbe: el equipo dijo que no buscaba una solución completa de planificación de recursos empresariales |
| ¿Por qué ISO/IEC 25010 y no 9126? | La consigna pide métodos actuales y la 25010 sustituye a la 9126. Además, seguridad y compatibilidad eran subcaracterísticas de funcionalidad en la 9126 |
| ¿Por qué no siguieron el orden de la rúbrica? | Están los seis criterios, cada lámina dice cuál cubre. Los ordenamos como ocurre un pedido porque así se ve que cada artefacto sale del anterior |
| ¿Qué proveedor eligieron? | Ninguno: el caso no lo decide y la rúbrica no lo pide. El paquete queda detrás de los contratos de servicio |
| ¿Qué es un EaC? | Un escenario de atributo de calidad: fuente de estímulo, estímulo, artefacto, entorno, respuesta y medida de la respuesta |
| ¿Cómo «trajeron el caso al presente»? | Se actualizó la tecnología: portal web y API en lugar de la «red Internet de Suministros», nube, inicio de sesión único. Los hechos del caso no se tocaron |
| ¿Qué pasa si se cae la nube? | Dos zonas de disponibilidad, base en espera y región secundaria. La tableta del muelle sigue registrando sin conexión y sincroniza después |

## Dónde está cada cosa en el PDF

| Si piden ver… | Sección |
|---|---|
| Contexto, core, descomposición | §1, figuras 1 a 3 |
| Tabla de stakeholders | §2 |
| Casos de uso y sus descripciones textuales | §3.1, figuras 4 a 7 |
| Tabla de EAC | §3.2 |
| Restricciones | §3.3 |
| Las cuatro matrices | §4 |
| Justificación de SOA y estilos descartados | §5.1 a §5.4 |
| Bloques y eventos | §5.7, figura 8 |
| Despliegue y sus detalles | §5.9, figuras 9 a 12 |
| Los siete pasos | §6.1 |
| Modelo de calidad | §6.4 |

## Notas relacionadas

- [[Entrega - Caso Harley-Davidson]] · [[Avance - Caso Harley-Davidson]] · [[Plan - Caso Harley-Davidson]]
- [[Ejemplo resuelto - Sistema de Transporte READM]]

## Preguntas de repaso

1. ¿Cuántos clics lleva la presentación y qué hace cada uno?
2. ¿Qué frase une el criterio 1 con el criterio 5?
3. ¿Qué supuestos hay que reconocer si preguntan por los números?
