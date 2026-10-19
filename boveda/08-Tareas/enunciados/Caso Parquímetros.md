---
tema: Enunciado
fuente: "Instrucciones de la Tarea 3 pegadas por el estudiante el 2026-10-19 + Caso 4 «Repensando los parquímetros» (Morales Zaragoza, UAM Cuajimalpa, 2015), en enunciados/Tarea 3/"
fecha: 2026-10-19
tarea: Tarea 3 - Caso Parquímetros
alias: [enunciado parquimetros, enunciado tarea 3, caso 4 parquimetros, SERVIparq]
---

# Tarea 3: Caso 4, Repensando los parquímetros (enunciado)

> [!info] Qué hay acá
> **§1 es textual**: las instrucciones tal como las publicó la catedrática. **§2 es el texto del
> caso** extraído del PDF. El PDF trae varios párrafos con la fuente codificada (letras corridas un
> lugar); se decodificaron. Las figuras de los anexos (13 partes del dispositivo, tabla de análisis
> funcional, panel de uso, registros de pruebas) solo están en el PDF. Las referencias de la
> bibliografía que salieron ilegibles se dejaron como están.

## 1. Instrucciones (textual)

> Instrucciones:
>
> Estudio y análisis individual del caso.
> Investigación de los tópicos relacionados al caso que consideren oportunos.
> Discusión previa del caso en equipos de trabajo.
> Planteo de posibles soluciones, desde el punto de vista de LA ARQUITECTURA DEL SOFTWARE, CALIDAD EN EL SOFTWARE, ARQUITECTURA EN EL CICLO DE VIDA Y ARQUITECTURA DE LA INFORMACIÓN.
> El grupo que expondrá deberá elaborar un documento completo con la solución y una presentación que incluya como mínimo: análisis del caso, posibles soluciones y la solución seleccionada con respuestas a las cuestiones que presenta el caso.  Debidamente justificado.
> Si consideran necesario desarrollar una parte de algún sistema, pueden hacerlo, teniendo en cuenta la solución de ARQUITECTURA DE SOFTWARE ELEGIDA.

**Grupo 2** (sin Elías Vasquez, que ya no está en el grupo): Santiago Barrera (Scrum Master /
coordinador), Jemima Chavajay (Product Owner), Byron Par (equipo de desarrollo).

**Pedido adicional del estudiante:** enriquecer con cómo funciona el estacionamiento en la vía
pública en Guatemala y los cobros de personas ajenas a las municipalidades (cuidacarros).

## 2. Texto del caso

![[08-Tareas/enunciados/Tarea 3/Caso 4 - Repensando los parquímetros.pdf]]


<!-- página 1 del PDF -->
51
Caso 4: 
Repensando los parquímetros, un acercamiento al diseño de interfaces desde 
la perspectiva del usuario. 
Autor: Nora Morales Zaragoza
Profesora investigadora
Departamento de Teoría y Procesos del Diseño
División de Ciencias de la Comunicación y Diseño
Universidad Autónoma Metropolitana, Unidad Cuajimalpa
Síntesis. (Abstract)
El caso se centra en el estudio del uso de los parquímetros en la vida cotidiana urbana con el objetivo de de-
tectar fallas o adaptaciones en la interfaz, para mejorar su interacción desde una visión sistémica y centrada 
en el usuario. Se exploran técnicas etnográficas de observación y del Diseño de Información, destacando 
Las “Pruebas Desempeño” iterativas y el “Bodystorming” que parte de una recreación física del entorno y la 
actuación de roles en una situación simulada para inspirar conceptos, crear empatía en situaciones parti-
culares y fomentar el uso de prototipos rápidos.
Palabras clave
Diseño de Información, Pruebas de eficiencia y requisitos de desempeño. Prototipos rápidos, Experiencia de uso.
Caso desarrollado con fines didácticos, la situación descrita no debe ser considerada como referente de buenas o malas prácticas de gestión directiva. 
(Los personajes y hechos han sido modificados y adaptados para proteger la confidencialidad)
Elaboración de prototipos, diseño centrado en el usuario, etnografía y urbanismo/Morales/Repensando los parquímetros…/2015

<!-- página 2 del PDF -->
55
Introducción
Una de las características de la Ciudad de México son los problemas relacionados con la calidad de vida y 
del aire, ocasionada principalmente por el tráfico, la falta de áreas verdes, una red de transporte público 
insuficiente, la sobrepoblación y el uso desmedido del automóvil.  Estos aspectos, entre otros, afectan la 
calidad de vida de las personas por lo que el gobierno de la Ciudad de México ha impulsado una serie de 
medidas como parte de la ley de movilidad urbana que involucra la creación de infraestructura peatonal y 
amigable como ciclo-vías, transporte ecológico o sustentable, rutas peatonales, mejora del espacio público 
y el ordenamiento urbano. 
La red de parquímetros es vista como un instrumento del ordenamiento del estacionamiento en la vía 
pública y una mejora de la movilidad urbana en ciertas zonas de la ciudad, su implementación ha abarcado 
distintas colonias como: Polanco, Hipódromo-Condesa, Roma, Cuauhtémoc, Juárez, Coyoacán y San José 
Insurgentes. (entre otras).
El objetivo de los parquímetros a nivel urbanismo y movilidad es el cambio de incentivo de un cajón 
de estacionamiento de un bien excluyente, limitado y costoso (200 mil pesos por cajón en ciertas zonas) 
–que provoca calles con sobresaturación vehicular– hacia un espacio que ofrece un beneficio más allá del 
particular, dando mayor cobertura y funcionamiento al espacio público, propiciando su ordenamiento y 
reduciendo la presencia del automóvil, haciendo que las personas realicen viajes mucho más eficientes. 
El 15 de octubre del 2012 Margarita Patiño entró como directora del programa SERVIparq, realizado 
por el Gobierno de la Ciudad, que se encarga de la instalación de mobiliario urbano, en particular la ins-
talación de redes de parquímetros y señalamientos para identificar la zona de estacionamiento, así como 
del cuidado y la no obstrucción de accesos vehiculares, pasos peatonales y rampas de acceso para personas 
discapacitadas respetando las normas establecidas. 
Margarita consideró que SERVIparq era un actor clave de mediación entre la Delegación y los representantes 
vecinales para evitar conĀictos y por lo tanto debía funcionar como un gestor de cohesiòn social previo a la insL
talación de las máquinas, no sólo manteniendo informados a la comunidad, sino convocando la formación de 
comités de transparencia y representantes vecinales para que la implementación se lleve a cabo eficientemente; 
Así mismo, el papel de SERVIparq debía ampliarse al mantener a los vecinos y otros actores informados sobre 
el destino de los recursos generados, de los cuales el 70% se destinaba a la inversión, la operación y el manteni-
miento de las unidades y el 30% se reinvertía en la comunidad. Sin embrago, la estrategia de implementación 
había sido muy distinta en cada caso y en ocasiones había suscitado polémica. –ver nota de Peralta, (2014). –
Detección de principales problemáticas.
Una de las primeras acciones que realizò Margarita fue un diagnòstico de las principales problemâticas 
presentadas en Delegaciones de la Ciudad, donde ya se habían instalado los parquímetros. El estudio se 
basó principalmente en investigación secundaria y entrevistas a expertos, como resultado se detectaron seis 
problemáticas principales:
1. La mayoría de los conĀictos generados a partir del programa de parquímetros respondía a la inconL
formidad por los vecinos, al no haber sido consultados antes de la implementación del sistema.
2. El problema de estacionamiento involucraba a un grupo particular de actores, además de la autori-
dad, como el de los “franeleros” -personas que lucran con la asignación y apartado de lugares de esta-
cionamiento por cierta cantidad de dinero- mismo que una vez implementado el sistema, continúan 
ofreciendo dicho “servicio” a los “clientes” afectando la designación de la tarifa original.
[ Repensando los parquímetros, un acercamiento al diseño de interfaces desde la perspectiva del usuario ]

<!-- página 3 del PDF -->
56
| Casos de estudio |
3. Los usuarios directos se quejaban del funcionamiento de los parquímetros, en particular de las ins-
trucciones de pago y al hecho de que no existieran otras alternativas de pago. 
4. Las personas se sentían frustradas al interactuar con la información del sistema, sobre todo si era la 
primera vez. En caso de recibir una infracción los usuarios no conocían el proceso de reclamo ni a quién 
pudieran acudir para aclarar la situación o alguna falla.
5. Falta de recursos humanos para la supervisión y mantenimiento de los dispositivos y la ejecución de mul-
tas, ya que de acuerdo a la normatividad, solamente los oficiales de tránsito pueden levantar la multa. 
6. Los ciudadanos percibían el sistema como autoritario y corrupto al no estar informados sobre el des-
tino de los recursos. 
A partir de este diagnóstico Margarita se hizo distintas preguntas:
¿Cómo diseñar una estrategia de implementación de parquímetros que se adaptara a las necesidades de 
cada zona e informara eficientemente propiciando la integración de distintos actores en etapas previas a la 
implementación del programa?
Esta pregunta respondía a la problemáticas 1 y 2 y apuntaban hacia una estrategia de integración de la 
comunidad por colonia para la toma de decisiones.
¿Cómo mejorar la información del sistema para facilitar la experiencia de uso?
¿Qué indicadores de desempeño de la tecnología permitirían mejorar el sistema haciéndolo más ami-
gable y eficiente?
¿Cómo cubrir la carencia de recursos humanos con los recursos tecnológicos sin que afectara la expe-
riencia de uso?
Estas tres preguntas respondían a las problemáticas 3, 4 y 5, se enfocaban hacia la funcionabilidad y usabili-
dad del dispositivo en relación con el usuario y la construcción de indicadores de desempeño de la tecnología.
¿Cómo mantener retroalimentación con las personas una vez instalada la red de parquímetros?
Esta última problemática demandaba un sistema de comunicación y retroalimentación del programa 
que mantuviera a los distintos actores, en particular a los vecinos, informados sobre los recursos generados 
y el seguimiento de acciones por parte de la autoridad.
Aspectos tecnológicos
El diseño del dispositivo de parquímetros, de origen francés, se eligió al iniciar el programa, unos años an-
tes de que Margarita se incorporara a SERVIparq. Era uno de los más populares en Europa, aunque existían 
otros sistemas más avanzados como el de San Francisco que cuenta con sensores que avisan al proveedor 
de servicio si los lugares han sido ocupados y permite adaptar la tarifa a la demanda de estacionamiento en 
distintos momentos del día o eventos particulares en la zona. 
Otro sistema que se consideró fue el que se utilizaba en la ciudad de Seattle que se conectaba a una pá-
gina web o a aplicaciones móviles proporcionando al usuario con información en tiempo real sobre cajones 
libres de estacionamiento y tiempo mínimo de búsqueda por cuadra, permitiéndole así planear su visita, 
tomar decisiones respecto a su movilidad y hacer más eficientes sus viajes.
A pesar de que los parquímetros adquiridos por SERVIparq tenían la capacidad de ofrecer una gran va-
riedad de acciones, como por ejemplo: 

<!-- página 4 del PDF -->
57
a) La ejecución del pago electrónico o de tarjeta a través de conexión inalámbrica 
b) El pago de servicios de otra índole como luz y agua. 
c) La capacidad de aviso en tiempo real a la central de monitoreo, si es que el dispositivo estaba siendo 
vandalizado. 
Los directivos del programa en ese entonces, restringieron ciertas características de su funcionamiento a 
una base sencilla de tareas denominada “Pay and Display” ya que no existían suficientes recursos humanos 
por parte de la autoridad para reaccionar a acciones de vandalismo o el hacerlo implicaba integrar al fun-
cionamiento del sistema a otros socios clave como bancos o la iniciativa privada.  
Margarita pensó que era un momento adecuado para probar la eficacia del sistema y validar la habi-
litación de ciertas funciones propias dispositivo o rediseñar uno nuevo sin tener que aumentar el capital 
humano. Por lo que decidió buscar a una empresa de diseño de interacción a partir de un artículo que leyó 
en una revista de diseño de interacción.
A la semana siguiente Javier Medina y Marco Ortiz, fundadores de la empresa Smartmedia se presenta-
ron en las oficinas de SERVIParq. A Margarita le entusiasmó la presentación de Smartmedia, en particular le 
llamó la atención que utilizaran técnicas del diseño de información, para presentar la información de manera 
clara y eficiente al usuario, y un enfoque interdisciplinario, en su equipo había gente que venía de disciplinas 
como la antropología, comunicación, diseño gráfico, tecnología y psicología. 
Javier le explicó que en Smartmedia su principal enfoque era en el diseño de interacción1 y se basaban en el 
análisis crítico de la tecnología existente y la exploración de nuevas formas de mejorarla para el bien común. Su 
metodología de investigación en diseño2 utilizaba tanto técnicas etnográficas para la inmersión y recopilación 
de datos de una situación única como un método desarrollado por el profesor David Sless del Communica-
tion Research Institue de Australia, (CRI) quien ha desarrollado estudios de desempeño de documentos 
informativos como: instructivos de medicamentos, contratos, facturas, pólizas de seguros y sitios web, entre 
otros midiendo la calidad de comunicación entre el público y las instituciones gubernamentales en el sec-
tor público en Australia y otras partes del mundo. Smartmedia había incorporado esta metodología en el 
desarrollo y diseño de interfaces gráficas. 
Proceso de trabajo
El proceso de Smartmedia se basaba en diseñar, analizar y perfeccionar los diseños existentes en el mer-
cado para detectar fallas en el desplegado informativo y en definir los requisitos de desempeño de los 
mismos, de acuerdo a las tareas que se espera que las personas realicen al utilizar la información en cierto 
contexto. “La primera etapa de nuestro proceso es el diagnóstico y nos ayuda a establecer los criterios de eficiencia posibles 
que nuestro cliente quiere lograr y buscamos empatarlos con lo que el usuario espera lograr con la pieza de comunicación”. 
Aseveró Joaquín. “Una vez definido el diagnóstico, procedemos a desarrollar conceptos que permiten ser validados por 
los usuarios en el propio contexto y hacemos modificaciones sobre prototipos o modelos tangibles, agilizando y optimizan-
do las propuestas hacia una solución pertinente y equilibrada para todos los involucrados” continuó. “Nuestro método 
funciona del mismo modo en que un médico busca síntomas de alguna enfermedad y aplica el tratamiento y luego com-
prueba si los síntomas han desaparecido o no”.
A partir de esta reunión Margarita y el equipo de Smartmedia definieron el objetivo del proyecto:
“Identificar cuáles son las tareas principales que el usuario común espera de un parquímetro, así como las barreras 
1  El estudio de la relación de las tecnologías de información en el contexto de la practica humana (Kaptelinin, 2006).
2 Se refiere al estudio de las personas como usuarios de productos, servicios y entornos en términos de la industria y la práctica, tendencia que 
se ha incrementado enormemente en las dos últimas décadas. Ese tipo de investigación informa e inspira al propio proceso de desarrollo y 
diseño de un producto o servicio y cuenta con sus propios métodos y herramientas. (Sanders, 2012. p.18)
[ Repensando los parquímetros, un acercamiento al diseño de interfaces desde la perspectiva del usuario ]

<!-- página 5 del PDF -->
58
| Casos de estudio |
y adaptaciones que realizan al interactuar con mismos, con el propósito de mejorar la experiencia de uso y su funciona-
miento a nivel sistémico”.
Etapa de diagnóstico
El primer acercamiento que propuso Javier fue la observación participativa, donde se registraron varias 
acciones de personas utilizando los parquímetros, en ciertas ocasiones se platicó con los participantes quie-
nes enunciaron situaciones particulares como las que se muestran a continuación.
Estrategia de un usuario
“El hecho de traer cambio se ha vuelto algo muy importante para mí, así que guardo un frasco en la guantera del coche para 
no tener ningún problema, la cosa es que me lo pueden robar”.
Comentario de un usuario
“Coloqué el boleto en la ventanilla del copiloto de manera visible, sin embrago el verificador de SERVIparq me infraccionó a 
pesar de que en el seguimiento de la queja llevaba como prueba fotos del tablero de carro”.
Una vez entendiendo el funcionamiento bâsico del parquímetro, las expectativas y estrategias de las 
personas se procedió a un análisis riguroso de la información.
Análisis funcional 
El análisis funcional se refiere a la identificación de todas las partes de información del documento in-
formativo y que tienen contacto con el usuario en el momento de la interacción, enunciando su función y 
priorizando su organización de acuerdo al nivel de relevancia de los distintos usuarios. “El usuario primario 
es aquel que realiza las tareas principales al interactuar con el dispositivo y mientras que el usuario secundario no está 
tan relacionado con la información del dispositivo, pero mantiene cierta relación con el sistema. Por ejemplo, el verifica-
dor del sistema, quién recolecta los pagos”, comentó Mario (ver tabla. 1.0 en Anexos).
Smartmedia identificó 13 partes de información relevante de acuerdo a la experiencia del uso de los par-
químetros y la presentaron a manera de tabla (ver Fig. 1.0 en Anexos)  en la siguiente reunión que tuvieron 
con SERVIparq. 
Sesión de definición de Requisitos de desempeño 
“Los Requisitos de desempeño son aquellas tareas que se requiere que el usuario realice con la pieza de información 
en el contexto de uso” explicó Javier a los participantes en dicha reunión y agregó: “Nosotros consideramos suma-
mente importante establecer estos requisitos con ustedes, ya que estos definen la base para evaluar las nuevas propuestas de 
diseño y se hacen a partir de la secuencia lógica de acciones que las personas enunciaron en la observación participativa y 
lo que ustedes como SERVIparq esperan que el usuario haga o comprenda al momento de interactuar con los dispositivos”.
r destacò tres momentos principales de la experiencia del uso de los parquímetros: Una etapa 
previa al uso: “Antes del uso”, (es decir antes de llegar a la zona de estacionamiento); una segunda etapa: 
“Durante el uso” (al momento de estar frente a la máquina) y una última etapa “Después del uso” (al alejarse 
de la zona). Ahora era momento para que SERVIparq identificara las principales tareas que esperaba que el 
usuario realizara con la información proporcionada. 
Javier tomó como ejemplo el panel de información detectado como “Panel de uso” en el análisis funcional 
(ver fig. 2.0 Anexos) cuya función principal es comunicar la secuencia de acciones que el usuario debe 
ejecutar para efectuar el pago en el parquímetro. De acuerdo a la información en el desplegado, los parti-
cipantes identificaron las siguientes tareas y sub-tareas que el usuario debe de poder realizar:

<!-- página 6 del PDF -->
59
1.- Introducir únicamente los números de la placa del automóvil. 
  - Presionar el botón verde
  - Presionar botón con letra “C” en caso de haberse equivocado
2.- Depositar monedas, únicamente de ciertos valores
3.- Oprimir botón verde
4.- Colocar el boleto (comprobante de pago) en una posición específica dentro del automóvil.
  - Cancelar la acción de pago, en caso de necesario
En ese mismo desplegado se presentaba otro tipo de información bajo el rubro de “Mapa de proximidad” 
y los participantes distinguieron las siguientes tareas:
1.-  Ubicar espacialmente al parquímetro que se estâ utilizando.
2.-  Identificar el número del parquímetro.
3.- Identificar la forma de contacto con el proveedor y duración servicio del servicio en caso de tener 
una queja o aclaración.
Javier señaló que la secuencia de acciones o tareas que se describían en el “Panel de Uso” no necesariamente 
empataba con la secuencia lógica que una persona debe llevar a cabo cuando usa un parquímetro. Así que pro-
puso una dinámica donde todos los participantes debían enunciar las acciones que una persona que busca 
estacionamiento realiza comúnmente en base a los tres momentos de uso. El “Antes”, “Durante” y “Después” 
del uso, mientras los participantes enunciaban las acciones, él iba escribiendo en un pizarrón. Al terminar esa 
parte de la sesión, Javier pasó al frente a cada uno de los participantes para que argumentaran el por qué habían 
colocado cada acción en las distintas etapas y pidió que entre todos, simplificaran la lista y organizaran las tareas 
de acuerdo a las prioridades de uso en una estructura coherente. Es así como obtuvieron la siguiente tabla. 
Antes del uso En el momento de uso Después del uso
1. Localizar la zona de parquí-
metros
2. Ubicar un cajòn libre
 - Realizar la maniobra 
de estacionarse
3. Ubicar el parquímetro que le 
corresponde
1.  Comparar el costo por tiempo de servicio
2.  Identificar el máximo de tiempo que puede 
usar el servicio
3.  Identificar el cómo pagar
 ?- Tipo de moneda
 - Dónde introducir el pago 
4. Entender el proceso para realizar el pago
- Saber la placa del automóvil e introducir la in-
formación
 - Depositar monedas
 - Recibir el boleto e identificar sus partes
 - Colocar el boleto en la zona adecuada 
del automóvil
5.- En caso de tener dudas
- Contactar al proveedor de servicio.
1. Llevar la cuenta del tiempo del 
servicio
2. Conocer el tiempo de con-
clusión del servicio
  - Realizar el proceso 
de pago nuevamente si es ne-
cesario
3. En caso de tener aclaración 
o dudas
 - Contactar con el-
proveedor de servicio
- Localizar en dónde y cómo 
pagar la multa
Tabla de Requisitos de desempeño acordados en la sesiòn de grupo.
[ Repensando los parquímetros, un acercamiento al diseño de interfaces desde la perspectiva del usuario ]

<!-- página 7 del PDF -->
60
| Casos de estudio |
Finalmente Javier agradeció la participación de todos y comentó que aún con la tabla de tareas definida, 
había que designar ciertos valores cuantitativos a las acciones basándose en investigaciones previas que 
parten de la siguiente premisa:
“Los usuarios que saben leer, generalmente pueden encontrar la información que se les pide en un desplegado informativo un 
90% de la veces y a su vez pueden utilizar apropiadamente esta información un 90%”.
“En ese sentido, cualquier desplegado informativo puede tener un nivel de eficiencia del 81% y no mayor, pues siem-
pre existirá una posibilidad de error o desatención de la información de un 19 %. “Así mismo hay que considerar que 
los dispositivos de los parquímetros se encuentran a la intemperie por lo que ciertas causas ambientales (lluvia, neblina, 
iluminación etc.) también pueden ser un factor que impida la lectura de la información.” continuó Marco.
Como consecuencia del comentario de Marco y al concomimiento empírico de que muchas personas 
llevan prisa cuando utilizan un parquímetro, Margarita decidió disminuir a un 80% -en vez de 90% sugeri-
do por Smartmedia– la capacidad de encontrar la información en el desplegado informativo, y se mantuvo 
en el porcentaje del 90% de instancias en las que el lector promedio utilizar dicha información apropiada-
mente, estableciendo el criterio del 72% como un nivel óptimo de desempeño en el uso de los dispositivos. 
Pruebas de Evaluación de desempeño.
Una vez identiÿcada la lista de tareas principales en la interacciòn con los parquímetros, y la secuencia de 
acciones basadas en la expectativa de uso de los dispositivos así como la definición de los niveles óptimos de 
desempeño. Se realizó un “protocolo de entrevista” a manera de cuestionario que guiará las primeras pruebas 
con los usuarios. 
La primera parte de las pruebas consistió en preguntar a seis personas que localizaran cierto tipo de 
información en los dispositivos, pidiéndoles que enunciaran como actuarían en base a la información 
proporcionada por los dispositivos (no en base a su conocimiento previo). El registro se realizó de manera 
cuantitativa y cualitativa enfocándose principalmente en tres aspectos:
 Lo que las personas decían
 Si encontraban la informaciòn que se les pedía y
 Si mostraban diÿcultad en localizar o entender la informaciòn
Smartmedia generalmente documentaba las sesiones en video y aunque la metodología sugería que las 
pruebas se realizaran en el contexto real, no se pudo realizar dicha acción ya que las encuestas tenían que 
realizarse en el espacio público y había que pedir un permiso especial a la ciudad, por lo que Javier decidió 
registrarlas en audio únicamente. Durante el análisis de dichas pruebas, Javier y Marco se encontraron con el 
equipo de diseñadores y antropólogos de Smartmedia que realizaron las encuestas, y se enfocaron en cuanti-
ficar tanto el número de fallas del diseño como la medición en cuanto a qué tan alejados quedaban de los 
niveles de eficiencia establecidos. Así mismo, trataron de detectar aquellas instancias en donde el usuario 
había tenido cierta dificultad en entender la información. Javier comentó: “Es importante recalcar que estas 
pruebas están diseñadas para encontrar las fallas en los desplegados informativos y no en el desempeño de las personas” 
escuchen las grabaciones e identifiquen por los comentarios y en base a lo que recuerdan si las personas se sintieron frus-
tradas o confundidas al no encontrar la información que les pedían”. Dicha sesión de análisis dio como resultado 
un panorama de donde se encontraba el diseño de los dispositivos actuales y cuanto se debe perfeccionar 
el nuevo diseño para cumplir con los criterios acordados.

<!-- página 8 del PDF -->
61
[ Repensando los parquímetros, un acercamiento al diseño de interfaces desde la perspectiva del usuario ]
Validación de los prototipos
Después del análisis de las pruebas de desempeño de la etapa previa se volvió a realizar una segunda ron-
da de pruebas con el mismo protocolo pero con seis participantes distintos aunque esta vez ya incluía las 
nuevas propuestas del equipo de diseño de Smartmedia. Javier les pidió que trabajaran las interfaces gráficas 
impresas sobre modelos tangibles a escala uno a uno. Los modelos no necesitaban demasiada calidad para 
su elaboración, podían estar impresos y pegados encima de cajas que simularan las dimensiones de los 
dispositivos reales.
La idea de Javier estaba enfocada a aplicar una técnica que había aprendido en un taller de interacción, 
pues le preocupaba que las pruebas no tuvieran la credibilidad con los participantes y el hecho de que no 
podían ser realizadas en el espacio.
“Bodystorming” (Lluvia corpórea)
La técnica a la que se refería Javier era la de Bodystorming, cuyos objetivos eran los de facilitar la experiencia 
de uso de cierta tecnología o concepto a las personas, a través de la recreación de un escenario improvisado de 
un espacio real, como una cafetería, un hospital, un centro comercial o en ese caso, la vía púbica. Constaba 
de asignar distintos roles a los participantes para que actuaran físicamente la experiencia e improvisaran 
con los objetos que tuvieran a la mano. Por lo que, Javier pidió al equipo de Smartmedia que adaptaran la 
sala de juntas, recreando con materiales muy sencillos una calle de cierta zona de la ciudad. El equipo co-
locó cinta adherible simulando las marcas de pintura para los cajones de estacionamiento, utilizaron mesas 
simulando los vehículos y cartulinas marcadas a manera de placas y papel para el comprobante de pago. 
Colocaron los prototipos impresos encima de las cajas por distintos puntos de la sala, hasta hubo el detalle 
de traer algunas plantas a la sala, que simulaban áreas verdes o jardineras de las banquetas.
Una vez preparada la sala para las sesiones con los participantes, Javier invitò al equipo de rdquh?
para que observaran y participaran en la dinámica. Margarita incluso actuó de una mujer que paseaba a su 
mascota. Se le pidió a cada participante que jugara el rol de una persona que buscaba estacionar su coche 
en cierta zona calle, a algunos participantes se les hizo hincapié en que llevaban mucha prisa porque tenían 
una junta. En un principio, ellos se notaban tensos, pero al entrar a la sala entendieron de lo que se trataba 
y hubo muy buenas improvisaciones de la experiencia, mismas que alimentaron de información valiosa al 
equipo. El equipo de Smartmedia moderaba la sesión y al mismo tiempo, registraba los datos de acuerdo 
con el protocolo de la prueba. 
“ Al actuar su rol, el participante naturalmente explora las posibilidades de la experiencia y señala fallas y supuestos que dan pie 
a nuevas ideas sobre el cómo podemos mejorar la información. Es importante que los diseñadores estén presentes ya que 
el ver como las personas usan sus propios diseños, se convierte en un momento de profunda revelación”., comentó Mario.
Una vez terminada la dinâmica de a?????K????Ā???
pruebas utilizando los mismos criterios que la vez anterior. Se pudieron notar bastantes mejoras, pero aún 
existían ciertas dificultades para realizar ciertas tareas.
Por ejemplo: 
Algunos participantes decían haber entendido el instructivo, pero cuando se trataba de colocar el nú-
mero de placa o el boleto en el lugar correcto del vehículo seguían teniendo dificultad. O cuando había  
que realizar el pago no contaban con el cambio de moneda suficiente lo que apunta una situación común.
“Aunque este tipo de problemas son más circunstanciales y subjetivos, el equipo regresó a la mesa de trabajo a realizar ajustes 
para realizar nuevos prototipos. El proceso puede parecer que no tiene terminación, sin embargo, se debe de hacer hasta 
que las propuestas de rediseño de dispositivos cumplan los niveles de eficiencia acordados con SERVIparq, demostrando así 
que cumplimos con lo acordado y demostrar al cliente que pusimos atención en lo que les es relevante”. Comentó Javier.

<!-- página 9 del PDF -->
62
| Casos de estudio |
Alicia una diseñadora integrante del equipo de Smartmedia comentó: “Gracias a las pruebas tenemos una 
idea mucho más clara de cómo debe funcionar la interfaz gráfica de los parquímetros y en que secuencia deben organi-
zarse los contenidos de las instrucciones”. 
Cierre del caso
En la siguiente sesión Javier entregó tablas comparativas con los niveles de desempeño de la primera prue-
bas – hechas con los parquímetros existentes– y las segundas pruebas hechas con los modelos en la sesión 
de Bodystorming.
Margarita convocó a los directivos de SERVIparq y a las Distintas Delegaciones involucradas en la red de 
parquímetros a una junta a la que asistió con Javier para realizar el plan de acción que se abordaría el año si-
guiente en cuanto a estrategias de implementación y monitoreo del programa de parquímetros de la ciudad. 
Preguntas:
1. ¿Qué otro tipo de estudio podría haber hecho Margarita para un diagnóstico inicial del problema?
2. ¿Qué problema enunciado dentro del diagnóstico inicial crees que resuelve mejor con la metodolo-
gía expuesta?, y ¿Cuál crees SERVIparq pudo haber abordado de manera más profunda?
3. ¿De qué otra manera crees que se podía dar la clasificación de la problemática para abordar solucio-
nes pertinentes?
4. ¿Qué otros sistemas que se mencionan en la lectura fueron considerados en el caso?, y ¿Cuales crees 
que podrían haber resuelto de mejor manera las problemáticas definidas en el diagnóstico inicial? 
Explica porque.
5. ¿Qué otras tareas o acciones se podrían incluir en los requisitos de desempeño de los parquímetros? 
Discute con tu equipo ¿Por qué?
6. ¿Cuales son los componentes principales del diseño de una prueba de desempeño?
7. ¿De que otra manera se te ocurre que los requisitos de desempeño pueden ser representados?
8. ¿Cuál es la razón por la que el equipo define los criterios de eficiencia de la información en un nivel 
òptimo de desempeño del 72%?  ReĀexionen sobre una alternativa para deÿnir dichos criterios.
9. ¿Qué tipo de propuesta crees que el equipo de Smartmedia entregó como resultado de la aplicación 
de esta metodología? 
10. ¿Cómo crees que la dinámica de BodyStorming ayudó al equipo de diseño de Smartmedia?
11. ¿Qué acción crees que se llevó a cabo por parte de SERVIparq a partir de esta experiencia?   
12. ¿Cómo crees que se pueda complementar o mejorar las técnicas propuestas en el caso?
13. ¿ En qué otros contextos crees que se puede utilizar esta metodología?
14. ¿Crees apropiado que se deba rediseñar la información constantemente? ¿Por qué?

<!-- página 10 del PDF -->
63
[ Repensando los parquímetros, un acercamiento al diseño de interfaces desde la perspectiva del usuario ]
Anexos:
Fig. 1.0 - Diagrama de identificación de las partes del dispositivo. 
[ Repensando los parquímetros, un acercamiento al diseño de interfaces desde la perspectiva del usuario ]

<!-- página 11 del PDF -->
64
| Casos de estudio |
Fig. 2.0  Dos segmentos de una Tabla de Anâlisis funcional de los parquímetros. Las columnas muestran la parte de informaciòn a la que se reÿere, 
el propósito o función de dicha información y a que tipo de usuario va dirigida principalmente
Fig. 3.0 – Imagen del instructivo visual “Panel de uso” que muestra las instrucciones de pago, mapa de ubicación e identificación del parquímetro 
con los horarios de servicio.


<!-- página 12 del PDF -->
65
[ Repensando los parquímetros, un acercamiento al diseño de interfaces desde la perspectiva del usuario ]
Fig. 4.0 – Ejemplos de registros de “Pruebas de desempeño” en otros contextos, utilizando un programa de hoja de cálculo, se destacan las celdas 
marcadas con amarillo, como aquellas situaciones en las que el participante tuvo dificultad de localizar o entender la información o expresó alguna 
recomendación al respecto.
Bibliografía y referencias
aM?aM?GQOOVH?r?t?dY?f??c?q???q?c. Interactive TechnoL
logies. San Francisco, CA: Morgan Kauffman, Focal Press.
Ecoparq (2014) ¿Qué es y cómo funciona? Portal del Gobierno Federal del DF. México D.F.: GDF. recuperado 
el 12 de julio de http://www.ecoparq.df.gob.mx/index.php/que-es-y-como-funciona
Gray, D., Brown, S., y Macanufo, J. (2010) Gamestorming: A Playbook for Innovators, Rulerbreakers and Changemakers. 
Sebastopol, CA: O’Reilly Media. (p. 59-60.)
Kaptelinin, V., y Nardi A. B. (2006) Acting with Technology: Activity Theory and Interaction Design. Cambridge, 
MA: MIT Press.
Peralta, E. (2014)“Parquímetros: Éxito o Fracaso” publicado en Circula México. México D.F.: CMC. recupera-
do en julio 2014 de http://circulamexico.com/espacio-publico/?p=1468# Parquímetros: Éxito o Fracaso
Sanders, E.B.-N., y Strappers, P. J. (2012). Convival Toolbox, Generative Research for the Front end of Design. 
Amsterdam: BIS Publishers.
rK?jM?`M?GPXXVHM?c???M (T. Hudson, Ed.
 New York, U.S.A.: Jhon Wiley & Sons.
rK?cM?GQOOUHM?d?Đ??ĒY?N~??M TPG TipoGrâÿca, Revista de Diseño No.71 junio-
julio Buenos Aires.
Sless, D., y Wiseman, R. (1998). Writing about medicines for people: usability guidelines for consumer medicine 
information. 2nda edicion. Asutralia: Communication Reserach Institute.
tK?qM?GQOOXH?`?o?f??tw?cY?e??????N~????. Voices 
That Matter. Berkeley, CA: New Riders.
u?n’fK?jM??iM?GQOOWHM?s?h?c?g. Cincinnati, OH: F.+W Media, How Books.

