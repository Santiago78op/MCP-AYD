---
tema: Guion de presentación
fuente: "Generado por 06-Proyecto-MCP/generar-presentacion-parq.py desde Guion - Presentación Caso Parquímetros.md"
fecha: 2026-10-19
tarea: Tarea 3 - Caso Parquímetros
---

# Guion de Santiago Julián Barrera Reyes · Scrum Master / coordinador

## Tus diapositivas

| Diapositiva | Arriba dice | Titular en pantalla | Empieza en | Dura |
|---|---|---|---|---|
| **1** | PORTADA | Repensando los parquímetros | 0:00 | 0:30 |
| **2** | EL CASO | SERVIparq quiere que el cajón rote, pero el programa tiene seis problemas | 0:30 | 1:00 |
| **3** | INVESTIGACIÓN | En Guatemala se cobra Q3 por media hora, y también cobran los cuidacarros | 1:30 | 1:30 |
| **6** | CASO DE NEGOCIO | El negocio son cinco procesos; el cuidacarros queda fuera, pero cuenta | 5:00 | 1:00 |
| **7** | POSIBLES SOLUCIONES | Elegimos pagar por placa con el equipo que ya se compró | 6:00 | 1:15 |
| **8** | ARQUITECTURA DEL SOFTWARE | Cada proceso es un servicio, y los servicios se avisan con eventos | 7:15 | 1:15 |
| **9** | DESPLIEGUE | El parquímetro sigue cobrando aunque se caiga la señal | 8:30 | 1:00 |
| **13** | ARQUITECTURA EN EL CICLO DE VIDA | Se construye en espiral por fuera y con Scrum por dentro | 12:30 | 1:00 |
| **14** | FACTORES EXTERNOS | Al cobro informal se le gana con información, datos y acuerdos | 13:30 | 1:00 |
| **15** | CIERRE | Tres ideas para llevarse | 14:30 | 0:30 |

Hablás **10:00** de los 15 minutos. Si dan 10 minutos: se omite la 9 (el despliegue se nombra en la 8) y la 13 se reduce a las cuatro fases; hablás de 0:00 a 2:30, de 4:00 a 6:30 y de 8:00 a 10:00.

**Cómo leerlo:** en cada diapositiva va primero **qué se ve al entrar**, después lo que decís (texto en gris), y en cada *(clic)* qué tarjeta aparece. La **idea clave** es lo único que no se puede olvidar. Arriba de tu primera diapositiva dice quién te pasa la palabra; abajo de la última, a quién se la pasás.

## Diapositiva 1 · PORTADA · Santiago · 0:00

**Página 1 de 15** · en pantalla: «Repensando los parquímetros»

**Qué se ve al entrar:** el título, el nombre de la propuesta (SIEP) y los tres nombres. No hay clics.

> Buenos días. Somos el Grupo 2: Jemima Chavajay, Byron Par, que hoy no pudo acompañarnos, y yo,
> Santiago Barrera.
> El caso cuatro cuenta qué pasó con los parquímetros de la Ciudad de México en 2012. Nos pidieron
> analizarlo y proponer una solución desde cuatro ángulos: arquitectura del software, calidad, ciclo
> de vida y arquitectura de la información. Nuestra propuesta se llama SIEP: Sistema Integrado de
> Estacionamiento en la vía Pública.
> Vamos en cinco partes, que ven en la barra de arriba. Y en cada una lo traemos a Guatemala, porque
> aquí pasa lo mismo.

**Idea clave:** quiénes somos, qué nos pidieron y por dónde vamos a ir.

**Por qué lo menciono:** las cuatro perspectivas no son nuestras: las pide la consigna de la tarea, y
la solución se ordena con ellas. La barra de arriba es el mapa de la exposición.

## Diapositiva 2 · EL CASO · Santiago · 0:30

**Página 2 de 15** · en pantalla: «SERVIparq quiere que el cajón rote, pero el programa tiene seis problemas»

**Qué se ve al entrar:** a la izquierda, la foto del parquímetro con sus partes. Las tres tarjetas de
la derecha aparecen con clic.

> Empiezo por el caso, porque todo lo que vamos a proponer responde a él.
> El caso pasa en la Ciudad de México, en 2012. SERVIparq es el programa del gobierno que instala y
> opera los parquímetros. Este es su parquímetro: arriba, el panel con las instrucciones; abajo, la
> ranura de monedas, el teclado para escribir la placa y una ranura para tarjeta que no se usaba.
> La meta es que un lugar de estacionamiento, que ahí vale hasta doscientos mil pesos, lo usen muchos
> conductores durante el día y no uno solo.
> *(clic)* **→ aparece «70/30».** Lo que se cobra se reparte así: setenta por ciento para operar los
> equipos y treinta por ciento se invierte en la misma colonia.
> *(clic)* **→ aparece «6 problemas».** En 2012 llega una nueva directora, Margarita Patiño. Hace un
> diagnóstico y encuentra seis problemas.
> *(clic)* **→ aparece «Pruebas con personas».** Para mejorar el parquímetro contrata a Smartmedia, una
> empresa de diseño, que pone a personas reales a usarlo y mide si entienden la información.

**Idea clave:** el parquímetro existe para que el lugar rote, y tiene seis problemas.

**Por qué lo menciono:**
- **Ciudad de México, 2012:** es donde y cuando pasa el caso que nos dieron; no lo elegimos nosotros.
- **Los 200 mil pesos:** explican por qué importa que el lugar rote: es un espacio caro y escaso.
- **Margarita Patiño y Smartmedia:** son los protagonistas del caso. Lo que hizo Smartmedia es el
  punto de partida que nosotros completamos.
- **La foto:** es del propio caso; sirve para que el público vea el aparato del que hablamos.

## Diapositiva 3 · INVESTIGACIÓN · Santiago · 1:30

**Página 3 de 15** · en pantalla: «En Guatemala se cobra Q3 por media hora, y también cobran los cuidacarros»

**Qué se ve al entrar:** la tarjeta «Q3». Las otras dos aparecen con clic.

> ¿Por qué hablamos de Guatemala si el caso es de México? Porque la consigna pide investigar los temas
> del caso, y aquí estamos viviendo lo mismo.
> En la capital, la Municipalidad cobra tres quetzales por cada media
> hora. La banqueta pintada de blanco indica que se puede estacionar, y la roja que no. EMETRA, la
> empresa municipal de tránsito, anunció que se va a poder pagar con el celular.
> *(clic)* **→ aparece «2,500».** Igual que en México, hay personas que no son de la municipalidad y
> cobran por dejar estacionar: los cuidacarros. En el caso les dicen «franeleros», que es la palabra
> mexicana. En un solo operativo de la Policía Municipal de Tránsito se retiraron dos mil quinientos
> objetos que apartaban lugares. Y este año, en la zona 13, el
> Ministerio Público identificó a treinta y tres personas que cobraban hasta cincuenta dólares a
> turistas.
> *(clic)* **→ aparece «Q12 M».** En Antigua, el marbete digital MarbEx, que es un pago ligado a la
> placa, subió lo recaudado de siete a doce millones de quetzales. Pero la Corte de
> Constitucionalidad suspendió la base de datos de placas y la multa de quinientos quetzales.
> La lección: no alcanza con cobrar bien; hay que tener base legal y que la gente confíe.
> Le doy la palabra a Jemima, que nos muestra los seis problemas.

**Idea clave:** en Guatemala pasa lo mismo, y Antigua muestra que sin confianza ni base legal el
sistema se cae.

**Por qué lo menciono:**
- **La capital y EMETRA:** muestran que en Guatemala ya se cobra por parquímetro y que se viene el
  pago por celular, lo mismo que proponemos.
- **El operativo de la PMT y la zona 13:** prueban que los cuidacarros no son una anécdota: es un
  problema grande y puede ser delito.
- **Antigua y MarbEx:** es el ejemplo guatemalteco más parecido a nuestra propuesta, porque también
  cobra por placa. Muestra que funciona (subió lo recaudado) y su riesgo (la Corte frenó la base de
  datos de placas). Por eso nuestra solución cuida esos datos.
- Todo esto sale de noticias de 2023 a 2026, citadas en el §2.2 del documento.

**Ojo con el reloj:** las diapositivas 1 a 3 suman unos 3:14 dichos a ritmo normal, y tenés 3:00.
Ensayalas una vez con cronómetro. Si vas pasado, acortá la parte de la zona 13 a una frase
(*«y en la zona 13 el Ministerio Público identificó a treinta y tres cuidacarros»*). Lo que no se puede
saltar es la lección de Antigua. Tenés que pasarle la palabra a Jemima en el **minuto 3:00**.

> *Al terminar, le pasa la palabra a Jemima (diapositiva 4).*

> *Entra después de Jemima (diapositiva 5).*

## Diapositiva 6 · CASO DE NEGOCIO · Santiago · 5:00

**Página 6 de 15** · en pantalla: «El negocio son cinco procesos; el cuidacarros queda fuera, pero cuenta»

**Qué se ve al entrar:** a la izquierda, el texto con el negocio y los actores. El diagrama de la
derecha aparece con clic.

> Gracias, Jemima. Ahora pasamos a la solución. Antes de diseñar software, en el curso aprendimos a
> delimitar primero el negocio, porque así sabemos qué tiene que hacer el sistema y para quién.
> Definimos el negocio así: gestionar el estacionamiento en la calle.
> Los actores son quienes tratan con ese negocio desde afuera: el conductor, el comité de vecinos, la
> Delegación, que es como una municipalidad dentro de la Ciudad de México, el área de tránsito, el
> banco y el proveedor del parquímetro.
> El verificador, que revisa si los carros pagaron, trabaja para SERVIparq; por eso no es actor sino
> trabajador. Y el cuidacarros tampoco es actor, porque no participa de forma legal. Pero el diseño
> igual lo toma en cuenta.
> *(clic)* **→ aparece el diagrama de procesos.** De ahí salen cinco procesos: acordar la zona con los
> vecinos, cobrar por placa, verificar y multar, rendir cuentas y mantener los equipos. Cada proceso va
> a ser una pieza del sistema.

**Idea clave:** cinco procesos, y el cuidacarros no es actor pero sí cuenta.

**Por qué lo menciono:** delimitar el negocio antes de diseñar es el primer paso del método que vimos
en el curso; los cinco procesos son los que después se vuelven servicios.

## Diapositiva 7 · POSIBLES SOLUCIONES · Santiago · 6:00

**Página 7 de 15** · en pantalla: «Elegimos pagar por placa con el equipo que ya se compró»

**Qué se ve al entrar:** solo el título. Las cuatro soluciones aparecen una por clic.

> Con los problemas y el negocio claros, vimos qué caminos había. Comparamos cuatro soluciones contra
> los seis problemas.
> *(clic)* **→ aparece «S-1».** Rediseñar solo la información. Es barata y rápida, pero no resuelve la
> falta de personal ni la desconfianza.
> *(clic)* **→ aparece «S-2», marcada como núcleo.** Pagar con el número de placa: con monedas, tarjeta
> o celular, usando el mismo parquímetro que ya se compró. Ataca cinco de los seis problemas.
> *(clic)* **→ aparece «S-3».** Sensores en cada lugar y tarifa según la demanda, como en San
> Francisco. Es cara, los sensores se pueden dañar y todavía no hay datos para ajustarla.
> *(clic)* **→ aparece «S-4».** Gobierno comunitario: consultar a los vecinos, publicar lo cobrado y
> acordar con los cuidacarros. No es software, pero devuelve la confianza.
> Elegimos la dos como centro, con la uno adentro y la cuatro alrededor. La tres queda para después,
> cuando haya datos.

**Idea clave:** pago por placa con el equipo que ya existe.

**Por qué lo menciono:** **San Francisco** aparece en el propio caso como ejemplo de un sistema más
avanzado, con sensores por lugar; por eso lo usamos como la opción más ambiciosa. Comparar cuatro
caminos es lo que pide la consigna: «posibles soluciones y la solución seleccionada».

## Diapositiva 8 · ARQUITECTURA DEL SOFTWARE · Santiago · 7:15

**Página 8 de 15** · en pantalla: «Cada proceso es un servicio, y los servicios se avisan con eventos»

**Qué se ve al entrar:** a la izquierda, los cinco procesos. El diagrama de bloques y la fila de
cuatro decisiones aparecen con clic.

> Ya elegimos qué hacer; ahora, cómo se arma el software por dentro.
> Usamos SOA, que significa arquitectura orientada a servicios: el sistema se arma con piezas
> independientes llamadas servicios, una por cada proceso del negocio. Son los cinco que ven a la
> izquierda. Es uno de los estilos que vimos en el curso, y su regla es justo esa: cada proceso del
> negocio se vuelve un servicio.
> *(clic)* **→ aparece el diagrama de bloques.** Los servicios se comunican con eventos. Un evento es un
> aviso de que algo pasó. Cuando alguien paga, el parquímetro avisa «pago registrado», y a ese aviso
> reaccionan la base de datos, las notificaciones y el tablero público, sin que el parquímetro tenga
> que conocerlos.
> *(clic)* **→ aparecen las cuatro decisiones.** Esto cambia cuatro cosas en la calle: el pago queda
> ligado a la placa y ya no hay boleto; se encienden el pago con tarjeta y la alarma; una multa solo
> existe si un oficial confirma la evidencia; y todo lo que se cobra se publica.

**Idea clave:** una pieza por proceso, y las piezas se avisan entre sí cuando algo pasa.

**Por qué lo menciono:** SOA es un estilo de arquitectura del curso. Lo elegimos porque los cinco
procesos ya nos dan las piezas, y porque cada Delegación puede adoptarlas por separado. Los eventos
resuelven que el pago avise a varias partes sin depender de ellas.

## Diapositiva 9 · DESPLIEGUE · Santiago · 8:30

**Página 9 de 15** · en pantalla: «El parquímetro sigue cobrando aunque se caiga la señal»

**Qué se ve al entrar:** el diagrama de despliegue completo. No hay clics: se va señalando cada zona.

> Esto no se queda en papel: el despliegue muestra en qué equipos corre cada parte. Arriba están los aparatos de la gente: el
> parquímetro, el celular del conductor, el del verificador y la computadora de la Delegación.
> El parquímetro se conecta por la red celular. Si se cae la señal, sigue cobrando: guarda los pagos y
> los envía cuando vuelve la conexión. Eso dice el título.
> Al centro está la nube: los seis servicios, que son los cinco procesos más uno que conecta con los
> sistemas de afuera; la mensajería, que lleva los avisos; la base de datos y la analítica. Abajo, una
> copia de todo en otra región por si falla la principal. A la derecha, el banco y la autoridad de
> tránsito.
> Jemima les muestra cómo medimos que esto funciona.

**Idea clave:** si se cae la señal, el parquímetro no pierde ningún pago.

**Por qué lo menciono:** el despliegue demuestra que la solución se puede montar con equipo real, y
responde el riesgo más obvio en la calle: que se caiga la red celular.

> *Al terminar, le pasa la palabra a Jemima (diapositiva 10).*

> *Entra después de Jemima (diapositiva 12).*

## Diapositiva 13 · ARQUITECTURA EN EL CICLO DE VIDA · Santiago · 12:30

**Página 13 de 15** · en pantalla: «Se construye en espiral por fuera y con Scrum por dentro»

**Qué se ve al entrar:** el título y una línea con los factores. Los dos cuadros de método y las
cuatro fases aparecen con clic.

> Gracias, Jemima. La última perspectiva es el ciclo de vida: cómo se construye todo esto en el
> tiempo. Para elegir cómo trabajar usamos los siete factores que vimos en el curso. Aquí pesan tres: la pantalla
> correcta solo se descubre probando con gente, cada Delegación quiere algo distinto y hay riesgos
> fuertes al inicio. Por eso mezclamos dos métodos.
> *(clic)* **→ aparecen «Espiral» y «Scrum con arquitectura».** Por fuera, el modelo en espiral: el
> proyecto avanza en vueltas y cada vuelta empieza revisando los riesgos, como hizo Smartmedia al
> probar y corregir. Por dentro, Scrum, que trabaja en sprints, que son periodos cortos de una a cuatro
> semanas. La arquitectura se arma en el primer sprint y se mejora en cada sprint siguiente.
> *(clic)* **→ aparecen las cuatro fases.** Fase cero: consulta en la colonia piloto y contar a los
> cuidacarros. Fase uno: pago por placa y multa con evidencia. Fase dos: la app, la alarma y los
> reportes. Fase tres, cuando ya haya datos: los sensores.

**Idea clave:** espiral para controlar riesgos, Scrum para avanzar, y cuatro fases.

**Por qué lo menciono:** los siete factores para elegir metodología y los pasos de arquitectura
dentro de Scrum son material del curso. Smartmedia aparece porque su forma de trabajar, probar y
corregir, es justo una vuelta de espiral.

## Diapositiva 14 · FACTORES EXTERNOS · Santiago · 13:30

**Página 14 de 15** · en pantalla: «Al cobro informal se le gana con información, datos y acuerdos»

**Qué se ve al entrar:** solo el título. Las cuatro tarjetas aparecen una por clic.

> Antes de cerrar volvemos al cuidacarros, porque es el problema que más se parece a Guatemala y el
> que más nos preguntan. Lo atacamos desde cuatro lados.
> *(clic)* **→ aparece «Información».** La pantalla y la señal dicen que el único cobro es el del
> parquímetro, y cuánto es.
> *(clic)* **→ aparece «Software».** El conductor puede reportar un cobro sin dar su nombre. Y el
> sistema marca las cuadras que están llenas pero donde casi nadie paga: ahí hay alguien cobrando.
> *(clic)* **→ aparece «Ciclo de vida».** Antes de instalar se cuenta cuántos cuidacarros hay y se
> acuerda con la Procuraduría de los Derechos Humanos cómo actuar, como se hizo en Antigua.
> *(clic)* **→ aparece «Opción para la Delegación».** Ofrecerles un trabajo formal orientando a los
> conductores, pagado con el treinta por ciento que va a la comunidad.

**Idea clave:** al cuidacarros no se le gana solo con multas: se le gana con información, datos y
acuerdos.

**Por qué lo menciono:** **la PDH en Antigua**: allí la gobernación y la municipalidad firmaron un
acuerdo para recuperar los espacios ocupados por cuidadores, con un protocolo que incluye a la
Procuraduría de los Derechos Humanos (2017). Lo tomamos como modelo porque ya se probó en Guatemala.

## Diapositiva 15 · CIERRE · Santiago · 14:30

**Página 15 de 15** · en pantalla: «Tres ideas para llevarse»

**Qué se ve al entrar:** las tres ideas numeradas y «Gracias. ¿Preguntas?». No hay clics.

> Para cerrar, tres ideas que resumen todo lo que vieron. Uno: la pantalla era solo la mitad del problema. Dos: lo que faltaba ya
> estaba en el equipo. Tres: lo que se cobra se publica, porque sin confianza no hay sistema.
> Muchas gracias. Con gusto respondemos sus preguntas.

**Idea clave:** leer las tres ideas despacio, mirando al público.


## Preguntas que te tocan

| Pregunta | Respuesta | Dónde está en el PDF |
|---|---|---|
| ¿Por qué SOA y no microservicios? | Santiago: «Microservicios son decenas de piezas pequeñas y cada una hay que operarla. SERVIparq ya tiene poco personal (RE-07), así que cinco servicios grandes, uno por proceso, es lo que puede sostener.» | §5.1 |
| ¿Por qué el cuidacarros no es actor? | Santiago: «Un actor trata con el negocio de forma legítima, y el cuidacarros no. Lo tratamos como factor externo: genera una restricción (RE-12) y un escenario de calidad (EAC-11).» | Declaraciones, §5.5 |
| ¿Qué pasa si se cae la red? | Santiago: «El parquímetro guarda los pagos y los manda cuando vuelve la señal. La meta es cero pagos perdidos (EAC-03).» | §3.4, §5.1 |
| ¿Cómo protegen la base de placas? | Santiago: «En los reportes la placa se cambia por un código, cada acceso queda registrado y los datos se borran a los 90 días (EAC-06). Lo aprendimos de lo que le pasó a Antigua.» | §2.2, §3.4 |
| ¿Por qué no sensores desde el inicio? | Santiago: «Son caros, se pueden dañar y todavía no hay datos para fijar la tarifa por demanda. La arquitectura los deja preparados para la fase tres.» | §4.2 |
| ¿Qué metodología y por qué? | Santiago: «Una mezcla: espiral por fuera para controlar los riesgos y Scrum por dentro para avanzar rápido. La elegimos con los siete factores de clase.» | §5.3 |

## Palabras que hay que saber explicar

| Palabra | Cómo decirla en una frase |
|---|---|
| **SERVIparq** | El programa del gobierno de la Ciudad de México que opera los parquímetros |
| **Delegación** | Una división de la Ciudad de México, parecida a una municipalidad |
| **Cuidacarros** (en el caso, «franelero») | Persona que, sin ser de la municipalidad, aparta lugares y cobra por dejarlos usar |
| **Actor / trabajador** | El actor trata con el negocio desde afuera; el trabajador trabaja adentro |
| **SOA** | Arquitectura orientada a servicios: el sistema se arma con piezas independientes, una por proceso |
| **Evento** | Un aviso de que algo pasó («pago registrado») al que otras piezas reaccionan |
| **Despliegue** | En qué equipos y en qué lugar corre cada parte del sistema |
| **Réplica** | Una copia de todo en otra región, por si falla la principal |
| **ISO 9126** | La norma de calidad del programa: calidad del producto y calidad en uso |
| **Arquitectura de la información** | Cómo se ordena lo que la gente lee para que lo encuentre |
| **Espiral** | Un método que avanza en vueltas y empieza cada vuelta revisando riesgos |
| **Scrum / sprint** | Método ágil que trabaja en periodos cortos (sprints) de una a cuatro semanas |
