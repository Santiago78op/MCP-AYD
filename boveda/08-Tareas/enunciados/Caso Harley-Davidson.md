---
tema: Enunciado
fuente: "Instrucciones y rúbrica publicadas por la catedrática (pegadas por el estudiante el 2026-10-12) + Caso_Seleccionsoftwareempresarial_S12.pdf (HBS 606-S14, Austin, Sole y Cotteleer, rev. 22/01/2003), en enunciados/Tarea 2/"
fecha: 2026-10-12
tarea: Caso Harley-Davidson
---

# Caso Harley-Davidson — proyecto SiL'K (enunciado y ficha del caso)

> [!info] Qué hay acá y qué no
> **§1 y §2 son textuales**: las instrucciones y la rúbrica tal como las publicó la catedrática,
> con sus erratas marcadas *[sic]*. **§3 en adelante es una ficha**: los hechos del caso con su
> página del PDF y las frases que conviene citar entre comillas. No es una transcripción completa
> del caso — para eso está el PDF, `enunciados/Tarea 2/Caso_Seleccionsoftwareempresarial_S12.pdf`
> (28 páginas: 15 de relato y 11 anexos).
>
> Las figuras de los anexos 6a y 9 **no tienen texto extraíble**: están leídas de la imagen. La del
> anexo 5 (gráfico de tiempos) tiene sus rótulos en el texto, pero **cuáles van en negrita no**:
> eso hay que leerlo de la figura antes de citarlo.

---

## 1. Instrucciones (textual)

> Para la clase del martes 13 de octubre, es indispensable realizar una presentación en grupo que
> será requisito para habilitar la entrega final de esta tarea.
>
> Traer el caso al presente y trabajarlo con los métodos y tecnologías actuales.
>
> Debe realizar:
>
> 1. Estudio y análisis individual del caso.
> 2. Discusión previa del caso en equipos de trabajo.
> 3. Trabajar los pasos para definir la arquitectura de software que necesitaría el proyecto SIL´K
> 4. Incorporar los drivers atributos de calidad en el software (mediante Eac) a la solución
>    planteada en el numeral 3.
>
> La tarea se entregará el martes 13 de octubre y deberá incluir los numerales 3 y 4 de acuerdo a
> la siguiente rúbrica de calificación:
>
> NOTA: SOLO TOMEN EN CUENTA A LAS PERSONAS DEL EQUIPO QUE TRABAJEN ACTIVAMENTE EN LA TAREA.
>
> Formato para el nombre del archivo: GrupoN_CasoHD.pdf

## 2. Rúbrica (textual)

| No. | Criterio de evaluación | Excelente | Muy bien | Bueno | Necesita mejorar |
|---|---|---|---|---|---|
| 1 | Habilidad para identificar el caso de negocio (Diagrama de Constexto *[sic]*, CDU Core y CDU 1era. Descomposición) | 15 | 10 | 5 | 2 |
| 2 | Identificación de Stakeholders caso Harley-Davidson | 10 | 8 | 5 | 2 |
| 3 | Completitud de drivers RF, Atributos de Calidad y Restricción del caso Harley-Davidson | 20 | 15 | 10 | 5 |
| 4 | Acoplamiento de Matrices de trazabilidad a los criterios 1, 2 y 3: Stakeholders vrs. Requerimientos · Requerimientos vrs. Casos de Uso · Stakeholders vrs. Casos de Uso · Requerimientos vrs. Requerimientos | 15 | 10 | 5 | 2 |
| 5 | Identificación de los estilos arquitectónicos en función de los criterios anteriores. Diagrama de Despliegue de Arquitectura | 20 | 15 | 10 | 5 |
| 6 | Adaptación de los drivers Atributos de Calidad y los de Restricción a los pasos para definir la arquitectura de software que se necesita y determinación del modelo de calidad. | 20 | 15 | 10 | 5 |

Total: **100 puntos**.

---

## 3. El caso en una página

**Quién**: Harley-Davidson Motor Company, fabricante de motocicletas de gran cilindrada. Sede en
Milwaukee, unos 6.000 empleados, más de 600 concesionarios independientes, filiales en Alemania,
Reino Unido, Benelux, Francia y Japón (pág. 2).

**Qué**: el proyecto **SiL'K** — *Supplier Information Link*, «Acceso a información sobre
proveedores» — busca *"un sistema integrado de compras que proporcionase el soporte necesario a la
nueva Estrategia de Gestión de Suministros"* (pág. 1), descrito también como *"un sistema integral
de gestión de proveedores y de compras para toda la empresa"* (pág. 1).

**Por qué**: las piezas compradas son *"del 55 al 60 por ciento del valor de una motocicleta"*
(pág. 4), y cada centro de producción tiene su propio sistema de compras: *"incluso sistemas
suministrados por el mismo proveedor se habían modificado para responder a necesidades específicas
de los centros de fabricación locales"* (pág. 4).

**En qué momento termina el relato**: enero de 1999. El equipo tiene tres proveedores de software
finalistas y todavía no eligió. El caso **no dice cuál gana**.

> [!warning] El caso es de selección de un paquete, no de construcción
> El texto original es un caso de Harvard sobre **cómo elegir un proveedor de software**. La tarea
> pide otra cosa: **la arquitectura de software que necesitaría el proyecto SiL'K**, traída al
> presente. El relato de la selección sirve como fuente de stakeholders, requisitos y
> restricciones; **no es** el proceso de negocio que hay que modelar.

## 4. La Estrategia de Gestión de Suministros (SMS)

- Objetivo, textual: *"asegurar que Harley-Davidson recibe el producto más adecuado, en el momento
  preciso, con la máxima calidad y el menor coste posible"* (págs. 4-5).
- Distinción central: **vendedor** (*"aquella persona que uno puede encontrar en cualquier
  esquina"*) frente a **suministrador** (*"una extensión de nosotros mismos"*) (pág. 5).
- Cambio que pide: pasar de *"una mentalidad de realización de transacciones a corto plazo a tener
  una visión a largo plazo de las relaciones con los suministradores"* (pág. 5).
- Meta de tiempo: que el personal de compras dedique **al menos el 70 %** a gestión de
  proveedores. La encuesta mostró que **el 85 %** se iba en *"actividades no estratégicas como, por
  ejemplo, la revisión de las existencias, la aceleración de los procesos y la recogida de datos"*
  (pág. 8).
- Propuesta de valor (octubre de 1997): reducción de costes de compra de **34 millones de dólares
  en cinco años** (pág. 7).

## 5. La organización

| Elemento | Qué es | Pág. |
|---|---|---|
| Tres círculos | Creación de la Demanda (CDC), Grupo de Fabricación (PPG), Actividades de Soporte (PSC) | 3 |
| Consejo de Dirección y Estrategia | supervisa los tres círculos | 3 |
| Oficina de dirección general de Informática | tres directores, uno por círculo, en vez de un único director | 3 |
| Círculo de Tecnologías de la Información (ITC) | uno por círculo. El del Grupo de Fabricación *"contaba con todas las facultades necesarias para poder tomar las decisiones relacionadas con la inversión en nuevas tecnologías"* | 3 |
| Grupo de Unidad de Compras (PUG) | dirige el área de Compras, con directivos de cada centro de producción y de las cuatro divisiones | 4 |
| Cuatro divisiones de compras | MRO (consumibles de fabricación), OE (piezas de la moto), P&A (posventa), GM (ropa y artículos de marca) | 4, nota 3 |
| Grupo de Integración de Arquitecturas (AI) | *"establece las normas aplicables a la configuración del hardware y del software"* y debe *"garantizar que las soluciones técnicas definidas por el equipo del proyecto SiL'K fueran compatibles con la arquitectura de los sistemas de información existentes"* | 9, nota 12 |
| Consejo Asesor de Suministradores | **16** proveedores estratégicos, se reúne cada tres meses | 10, nota 13 |

**Centros** (anexo 2a, pág. 17): Milwaukee (sede, P&A, artículos varios, ventas, I+D), Wauwatosa
(centro de desarrollo de productos, motores XL), Menomonee Falls (motores FL), Franklin
(distribución de P&A), Tomahawk (fibra de vidrio), York (ensamblaje final), Kansas City
(ensamblaje final).

**Volumen de usuarios** (págs. 8 y 10): unas **200** personas en la organización de compras, más de
**2.000** empleados que generan solicitudes de pedido, y un público objetivo de **800** (200 de
abastecimientos y 600 de departamentos asociados).

## 6. Las personas con nombre (anexo 4, págs. 20-21)

| Grupo | Quién |
|---|---|
| **Promotores** | Garry Berryman (vicepresidente de Gestión de Materiales) · Dave Storm (vicepresidente de Planificación y Servicios de Información) |
| **Comité de Dirección** | los dos promotores · Tom Cullen (director de Sistemas, Grupo de Fabricación) · Pat Davidson (directora de Planificación y Control de Compras) · Cory Mason (dirección general de Informática del Grupo de Fabricación) |
| **Equipo del proyecto** | Dave Cotteleer (director del proyecto) · Julie Anding (Gestión del Cambio) · Chuck Braunschweig (Innovación de Procesos) · Blaine Webster (analista de sistemas) · y los representantes de Compras: Chuck Carter y Eileen Jarosz (Centro de Desarrollo de Productos), Glenn Christianson (Tomahawk), Eric Doman (Artículos Varios), Maxine Peissig (Tren de Fuerza), Rick Pues (Kansas City), Kerry Sarder (Piezas y Accesorios), Bob Walker (York) |
| **Fuera del anexo 4** | Karen Kaminski, directora de Integración de Arquitecturas (pág. 12) |

Partes consultadas en la segunda encuesta: *"los departamentos de Cuentas de Acreedores
Comerciales, de Recursos Humanos y de Logística, que mantenían relaciones continuas con el área de
Compras"* (pág. 8).

## 7. El ámbito del proyecto

**Anexo 6a** (pág. 23, leído de la figura). La cadena completa tiene nueve actividades; la leyenda
distingue las que SiL'K cubre (borde grueso) de las que *"no entra[n] dentro del ámbito"*:

| # | Actividad | Rótulo al pie | ¿En el ámbito? |
|---|---|---|---|
| 1 | Desarrollo | Del Concepto a la Actividad de Producción | **sí** |
| 2 | Pedido / Programación | Pedidos de los Clientes y Plan de Productos | no |
| 3 | Requisitos | MRP/DRP | **sí** |
| 4 | Realización de Pedidos importantes | Requisitos para el envío a Suministradores | **sí** |
| 5 | Logística de Entrada | Del Almacén del Suministrador al Almacén de Harley | **sí** |
| 6 | Recepción | — | **sí** |
| 7 | Movimiento Interno de Materiales | Recepción para Punto de Utilización | no |
| 8 | Uso de Materiales / Consumo | De Componentes a Puntos acabados | **sí** |
| 9 | Distribución | Productos Acabados al Cliente | no |

**Anexo 6b** (pág. 23) — las tres fases de puesta en funcionamiento:

| Fase | Nombre | Incluye |
|---|---|---|
| 1 | Procesos y sistemas de **transacciones** | requisitos / requisiciones / plazos · creación de documentos de compra · recibos / seguimiento · procesado de facturas |
| 2 | Procesos y sistemas de **información sobre suministradores** — *"a través de la red Internet de Suministros"* | información sobre resultados de los suministradores · comunicación e integración · gestión de los contactos |
| 3 | Procesos y sistemas de **seguimiento de proyectos** | metodología de productos coincidentes · planificación de productos · asignación de recursos · costes objetivo · preparación para la creación y el lanzamiento |

**Las reglas básicas** que el equipo dio a los proveedores (pág. 11): *"no estaba buscando una
solución completa de planificación de recursos empresariales (ERP)"*, *"su ámbito estaba muy bien
delimitado"* y *"los proveedores no deberían perder el tiempo buscando funcionalidades
adicionales"*.

## 8. De dónde salen los requisitos

**Los diez criterios funcionales** de la especificación (anexo 10, pág. 26): 1. diseños y bases de
apoyo · 2. definición de peticiones · 3. documentación · 4. recepción · 5. gestión de suministros ·
6. seguimiento del proyecto · 7. asuntos diversos · 8. interfaces · 9. formación · 10. otras
cuestiones.

**Lo que el caso nombra como calidad** (anexo 10): *"la solidez tecnológica y la facilidad de uso de
los sistemas"*, y entre los criterios cualitativos: **compatibilidad de las arquitecturas**,
**portabilidad de plataformas**, **funcionalidad Internet inmediata**, ofertas de soporte técnico,
método de formación.

**Beneficios esperados** (anexo 3, págs. 18-19), por los tres ejes del modelo de Integración de
Negocios — **personal, procesos y nuevas tecnologías** —: eliminación de registros duplicados,
proceso uniforme de abastecimiento en todos los centros, reducción del ciclo temporal de las
compras, reducción de las actividades manuales, consolidación de datos para la toma de decisiones,
agrupación empresarial de la demanda, *"mejora del acceso de los proveedores a la calidad, los
costes y los plazos y a los datos de demanda"*.

**Los dos obstáculos** que anticipa Cory Mason (pág. 6): el temor a afectar la producción —
*"Tenemos empleados que lo que más les importa es que las líneas de producción no dejen de
funcionar"*— y la *"proclividad natural de la compañía a realizar mejoras continuas, en lugar de
transformar las áreas de negocios"*.

## 9. Los tres finalistas (págs. 13-14 y anexo 10)

| | Proveedor 1 | Proveedor 2 | Proveedor 3 |
|---|---|---|---|
| Adecuación a la especificación | 93,44 % | **98,69 %** | 96,83 % |
| Perfil | afinidad cultural, fuerte en gestión del cambio | gran proveedor de ERP, el más caro, formal | gran proveedor de ERP, **ya contratado por Harley** en otra área |
| Internet | no lo ofrece directo: *"integrar una solución complementaria"* | *"interface avanzado que capacitaba para trabajar en Internet"* | calificación M-B |
| Compatibilidad de arquitecturas | A | M-A | A |
| Portabilidad de plataformas | A | M | A |
| Coste | A (mejor) | B (peor) | M |
| Gestión del cambio | A | M-A | M |

Dos descartes anteriores que valen como evidencia de restricción (pág. 12): uno con *"gran
funcionalidad"* eliminado *"debido a su incompatibilidad arquitectónica con las normas actuales y
previstas de infraestructura de Harley-Davidson"*, y otro eliminado por *"su pequeño tamaño y de su
capacidad potencial para satisfacer las necesidades futuras de soporte"*.

## 10. Cronología (anexo 7, pág. 24)

Enero de 1997, lanzamiento de la SMS · julio de 1997, primera reunión de SiL'K · octubre de 1997,
propuesta de valor · noviembre de 1997 a marzo de 1998, proceso «real» · abril a septiembre de 1998,
procesos «futuros» · 30 de septiembre de 1998, especificación funcional · 16 de octubre, solicitud
de ofertas · 5 de noviembre, reunión general de suministradores de software · 11 de diciembre, tres
preseleccionados · 10 al 22 de enero de 1999, demostraciones · **30 de enero de 1999, selección**.

## 11. Erratas e inconsistencias del texto

Para no arrastrarlas a la entrega:

| En el caso | Qué pasa |
|---|---|
| *"Check Carter"* (pág. 11) y *"Chuck Carter"* (anexo 4) | la misma persona |
| *"Barryman"* (pág. 4) | es Berryman |
| *"Grupo de Dirección de Compras"* (anexo 7) | es el Grupo de Unidad de Compras (PUG) |
| SMS como *"Estrategia"* y como *"Sistema de Gestión de Suministros"* (pág. 7) | es la **estrategia**; el sistema es SiL'K |
| *"suministrador"* | la traducción usa la misma palabra para los **proveedores de piezas** de Harley y para los **proveedores de software** que concursan. Son dos poblaciones distintas |
| ocho proveedores responden, siete presentan | la nota 15 lo explica con retiros, pero las cuentas no cierran limpias: no citar el número sin la nota |
