---
tema: Guion de presentación
fuente: "Entrega - Caso Parquímetros (Tarea 3, Caso 4 Repensando los parquímetros)"
fecha: 2026-10-19
tarea: Tarea 3 - Caso Parquímetros
alias: [guion parquimetros, guion tarea 3, presentación SERVIparq]
---

# Guion de la presentación · Caso 4: Repensando los parquímetros

Grupo 2 · tres oradores · **15 minutos** (supuesto: si dan 10, ver el recorte al final).
Archivo: `08-Tareas/Grupo2_CasoParquimetros_Presentacion.pptx`, que se arma con
`python3 06-Proyecto-MCP/generar-presentacion-parq.py`. El .pptx no lleva notas del orador: el guion
es este archivo y los individuales. *(clic)* marca dónde se avanza una animación.

| Bloque | Orador | Diapositivas | Reloj |
|---|---|---|---|
| Apertura, caso y Guatemala | **Santiago** (coordinador) | 1 a 3 | 0:00 a 3:00 |
| Problemas y requisitos de desempeño | **Jemima** (Product Owner) | 4 y 5 | 3:00 a 5:00 |
| Negocio, alternativas y arquitectura | **Byron** (equipo de desarrollo) | 6 a 9 | 5:00 a 9:30 |
| Calidad, información y prototipo | **Jemima** | 10 a 12 | 9:30 a 12:30 |
| Ciclo de vida, cobros informales y cierre | **Santiago** | 13 a 15 | 12:30 a 15:00 |

**Las diapositivas de cada uno:**

| Orador | Diapositivas | Lo que dice arriba en cada una | Tiempo |
|---|---|---|---|
| **Santiago** | **1, 2, 3, 13, 14, 15** | 1 PORTADA · 2 EL CASO · 3 INVESTIGACIÓN · 13 ARQUITECTURA EN EL CICLO DE VIDA · 14 FACTORES EXTERNOS · 15 CIERRE | 5:30 |
| **Jemima** | **4, 5, 10, 11, 12** | 4 LOS SEIS PROBLEMAS · 5 REQUISITOS DE DESEMPEÑO · 10 CALIDAD DEL SOFTWARE · 11 ARQUITECTURA DE LA INFORMACIÓN · 12 PARTE DESARROLLADA | 5:00 |
| **Byron** | **6, 7, 8, 9** | 6 CASO DE NEGOCIO · 7 POSIBLES SOLUCIONES · 8 ARQUITECTURA DEL SOFTWARE · 9 DESPLIEGUE | 4:30 |

**Cómo hablar:** con palabras de todos los días. Si sale un término del curso (SOA, driver, evento),
se dice qué significa en la misma frase. El documento trae la tabla «Palabras que usamos».

Regla para los cambios de orador: quien termina nombra al siguiente y su tema en una frase
(*«Jemima les muestra qué problemas encontramos»*). Así no hay silencios.

## Diapositiva 1 · PORTADA · Santiago · 0:00

**Página 1 de 15** · en pantalla: «Repensando los parquímetros»

> Buenos días. Somos el Grupo 2: Jemima Chavajay, Byron Par y Santiago Barrera. Presentamos el caso
> cuatro, *Repensando los parquímetros*. Nuestra propuesta se llama SIEP, Sistema Integrado de
> Estacionamiento en la vía Pública, y la vamos a defender desde las cuatro perspectivas que pide la
> consigna: arquitectura del software, calidad, arquitectura en el ciclo de vida y arquitectura de la
> información.

## Diapositiva 2 · EL CASO · Santiago · 0:30

**Página 2 de 15** · en pantalla: «SERVIparq quiere que el cajón rote, pero el programa tiene seis problemas»

> SERVIparq es el programa del gobierno de la Ciudad de México que opera los parquímetros. Su meta es
> urbana: que un cajón que vale hasta doscientos mil pesos deje de ser de uno solo y rote.
> *(clic)* Lo recaudado se reparte setenta por ciento para operar y treinta para la comunidad.
> *(clic)* En 2012 llega Margarita Patiño, hace un diagnóstico y encuentra seis problemas.
> *(clic)* Contrata a Smartmedia, una empresa de diseño. Le pide a la gente que haga tareas con el
> parquímetro y mide si encuentra y entiende la información. Hasta armaron una calle de mentira en una
> sala para que los participantes actuaran la situación. Nuestra conclusión: Smartmedia arregló la
> pantalla, pero tres de los seis problemas no tienen que ver con la pantalla.

## Diapositiva 3 · INVESTIGACIÓN · Santiago · 1:30

**Página 3 de 15** · en pantalla: «En Guatemala se cobra Q3 por media hora, y también cobran los cuidacarros»

> Trajimos el caso a Guatemala. En la capital, la municipalidad cobra tres quetzales por media hora
> según su acuerdo COM-40-2022, y la banqueta se pinta por colores: blanco se puede, rojo no. EMETRA,
> la empresa municipal de tránsito, anunció que se va a poder pagar con una aplicación.
> *(clic)* Y aquí aparece algo que el sistema no controla: personas que no son de la municipalidad y
> cobran por dejar estacionar, los cuidacarros. En el caso, que pasa en México, les dicen franeleros.
> En un solo operativo se retiraron dos mil quinientos objetos que apartaban lugares. En
> abril, en la zona 13, el Ministerio Público identificó a treinta y tres personas que cobraban hasta
> cincuenta dólares a turistas.
> *(clic)* Y Antigua: su marbete digital, MarbEx, casi duplicó la recaudación, de siete a doce
> millones, pero la Corte de Constitucionalidad suspendió justamente la base de datos de placas y la
> multa de quinientos quetzales. La lección: no basta con cobrar, hay que hacerlo con base legal y que
> la gente confíe. Le doy la palabra a Jemima, que les muestra los problemas.

## Diapositiva 4 · LOS SEIS PROBLEMAS · Jemima · 3:00

**Página 4 de 15** · en pantalla: «Tres de los seis problemas no se arreglan con una pantalla mejor»

> Ordenamos los seis problemas por su causa.
> *(clic)* Los de gobierno: vecinos que no fueron consultados y un sistema que se percibe corrupto
> porque nadie ve a dónde va el dinero.
> *(clic)* Los de información: instrucciones confusas y no saber cómo reclamar una multa.
> *(clic)* Los de capacidad: falta personal, pero el parquímetro ya podía cobrar con tarjeta y avisar
> vandalismo; esas funciones estaban apagadas.
> *(clic)* Y los cuidacarros, que el caso llama franeleros: apartan el lugar y cobran por él, o sea
> que le compiten al parquímetro por el mismo espacio.

## Diapositiva 5 · REQUISITOS DE DESEMPEÑO · Jemima · 4:00

**Página 5 de 15** · en pantalla: «El 72 % es el éxito esperado, pero cada tarea merece su propio número»

> Smartmedia acordó con SERVIparq qué tiene que poder hacer el conductor antes, durante y después de
> usar el parquímetro.
> *(clic)* Y le puso un número. Setenta y dos por ciento: el ochenta por ciento encuentra la
> información, porque la gente va con prisa, por el noventa por ciento que la usa bien.
> *(clic)* Nuestra mejora: el umbral por tarea, según lo que cuesta fallar. Pagar mal termina en una
> multa injusta, así que ahí pedimos ochenta y uno, el máximo del método. Byron les explica cómo lo
> resolvemos.

## Diapositiva 6 · CASO DE NEGOCIO · Byron · 5:00

**Página 6 de 15** · en pantalla: «El negocio son cinco procesos; el cuidacarros queda fuera, pero cuenta»

> Primero delimitamos el negocio: la gestión del estacionamiento en la vía pública. Los actores son el
> conductor, el comité vecinal, la Delegación, el área de tránsito, el banco y el proveedor del equipo.
> El verificador trabaja adentro, así que no es actor sino trabajador. Y el cuidacarros tampoco es
> actor: no participa en el negocio de forma legal, pero igual tenemos que tomarlo en cuenta.
> *(clic)* De ahí salen cinco procesos: concertar la zona, cobrar por placa, verificar y sancionar,
> rendir cuentas y mantener la red. Cada uno será un servicio.

## Diapositiva 7 · POSIBLES SOLUCIONES · Byron · 6:00

**Página 7 de 15** · en pantalla: «Elegimos pagar por placa con el equipo que ya se compró»

> Evaluamos cuatro soluciones contra los seis problemas y los drivers.
> *(clic)* Uno: rediseñar solo la información. Barato, pero no toca la falta de personal.
> *(clic)* Dos: pagar con el número de placa, con monedas, tarjeta o celular, usando el mismo equipo que ya se compró.
> *(clic)* Tres: sensores por cajón y tarifa por demanda, como San Francisco. Caro y vulnerable al vandalismo.
> *(clic)* Cuatro: gobierno comunitario, que no es software pero resuelve consulta y confianza.
> Elegimos la dos como núcleo, con la uno adentro y la cuatro alrededor. La tres queda para después, cuando haya datos.

## Diapositiva 8 · ARQUITECTURA DEL SOFTWARE · Byron · 7:15

**Página 8 de 15** · en pantalla: «Cada proceso es un servicio, y los servicios se avisan con eventos»

> El estilo principal es SOA, arquitectura orientada a servicios: cada uno de los cinco procesos es un
> servicio independiente. Es justo lo que dice la lámina de clase: desarrollar los procesos de negocio
> como servicios.
> *(clic)* Y los servicios se avisan con eventos. Cuando alguien paga, el parquímetro avisa «pago
> registrado» y a ese aviso reaccionan la base de datos, las notificaciones y el tablero, sin que el
> parquímetro tenga que conocerlos.
> *(clic)* Cuatro decisiones cambian el día a día: el pago se liga a la placa y desaparece el boleto;
> se encienden el pago con tarjeta y la alarma; la multa solo nace cuando el oficial confirma la
> evidencia; y todo lo cobrado se publica.

## Diapositiva 9 · DESPLIEGUE · Byron · 8:30

**Página 9 de 15** · en pantalla: «El parquímetro sigue cobrando aunque se caiga la señal»

> Así se despliega. Arriba, el parquímetro, el teléfono del conductor, el del verificador y la consola
> de la Delegación. El parquímetro se conecta por la red celular y, si se cae la señal, sigue cobrando,
> guarda los pagos y los manda cuando vuelve la conexión. Al centro, la nube con los seis servicios, la mensajería, la base de datos y la analítica;
> abajo, una réplica en otra región; a la derecha, el banco y la autoridad de tránsito.
> Jemima les muestra cómo medimos que esto funciona.

## Diapositiva 10 · CALIDAD DEL SOFTWARE · Jemima · 9:30

**Página 10 de 15** · en pantalla: «Nos comprometemos con cuatro números que se pueden medir»

> Usamos los dos modelos de ISO 9126 del programa: calidad del producto y calidad en uso.
> *(clic)* Eficacia: setenta y dos por ciento completa el pago sin ayuda.
> *(clic)* Rendimiento: el verificador sabe si una placa pagó en dos segundos.
> *(clic)* Disponibilidad: cero pagos perdidos aunque se caiga la red.
> *(clic)* Seguridad: el cien por ciento de las multas con foto, hora, ubicación y la firma del oficial.
> Cada entrega se acepta con una prueba de desempeño, ahora en la calle y con doce personas.

## Diapositiva 11 · ARQUITECTURA DE LA INFORMACIÓN · Jemima · 10:45

**Página 11 de 15** · en pantalla: «La información se ordena por lo que el conductor hace en cada momento»

> La arquitectura de la información organiza los contenidos para que la gente los encuentre. La
> organizamos por momento de uso.
> *(clic)* Antes: la señal con el color de la banqueta y el mapa en la app.
> *(clic)* Durante: tres pasos, placa, tiempo y pago, con la tarifa siempre arriba.
> *(clic)* Después: comprobante con folio, aviso antes de vencer y cómo reclamar.

## Diapositiva 12 · PARTE DESARROLLADA · Jemima · 11:30

**Página 12 de 15** · en pantalla: «El prototipo mide si llegamos al 72 % mientras se prueba»

> Desarrollamos una parte del sistema: la pantalla del parquímetro. Usa el tarifario real de la
> capital y trae un modo de prueba que cronometra cada intento y calcula si llegamos al setenta y dos
> por ciento. Y en el paso de pago dice lo que el cuidacarros no quiere que se sepa: este es el único
> cobro. Santiago cierra con cómo se construye.

## Diapositiva 13 · ARQUITECTURA EN EL CICLO DE VIDA · Santiago · 12:30

**Página 13 de 15** · en pantalla: «Se construye en espiral por fuera y con Scrum por dentro»

> Para elegir cómo trabajar usamos los siete factores de la clase. La pantalla no se sabe cómo debe
> quedar hasta probarla con gente, cada Delegación quiere algo distinto y hay riesgos fuertes al
> inicio. Por eso combinamos dos métodos.
> *(clic)* Por fuera, el modelo en espiral: en cada vuelta se revisan primero los riesgos, igual que
> hizo Smartmedia probando y corrigiendo. Por dentro,
> Scrum con los cuatro pasos de arquitectura de la lámina: especificar y priorizar casos de uso,
> arquitectura base en el primer sprint y refinamiento en cada sprint.
> *(clic)* Cuatro fases: concertación con la colonia piloto; pago por placa y verificación; app y red
> monitoreada; y, con datos, sensores.

## Diapositiva 14 · FACTORES EXTERNOS · Santiago · 13:30

**Página 14 de 15** · en pantalla: «Al cobro informal se le gana con información, datos y acuerdos»

> Volvemos al cuidacarros, porque es el problema que más se parece a Guatemala.
> *(clic)* Información: la pantalla dice que es el único cobro.
> *(clic)* Software: el conductor puede reportar un cobro sin dar su nombre, y el sistema marca las
> cuadras que están llenas pero donde casi nadie paga: ahí hay alguien cobrando.
> *(clic)* Ciclo de vida: antes de instalar, contar cuántos cuidacarros hay y acordar con la
> Procuraduría de los Derechos Humanos cómo se actúa, como se hizo en Antigua.
> *(clic)* Y una opción para la Delegación: ofrecer trabajo formal de orientación, pagado con el treinta por ciento comunitario.

## Diapositiva 15 · CIERRE · Santiago · 14:30

**Página 15 de 15** · en pantalla: «Tres ideas para llevarse»

> Tres ideas para llevarse. La pantalla era la mitad del problema. Las funciones que faltaban ya
> estaban en el equipo. Y lo que se cobra se publica, porque sin confianza no hay sistema. Gracias;
> con gusto respondemos sus preguntas.

## Preguntas probables y quién responde

| Pregunta | Responde | Dónde está en el PDF |
|---|---|---|
| ¿Por qué SOA y no microservicios? | Byron: el programa no puede sumar personal (RE-07) para operar decenas de servicios | §5.1 |
| ¿De dónde sale el 72 %? | Jemima: 80 % encuentra × 90 % usa bien | §5.2 |
| ¿Por qué el cuidacarros no es actor? | Byron: no interactúa de forma legítima; es factor externo y genera RE-12 y EAC-11 | Declaraciones, §5.5 |
| ¿Qué pasa si se cae la red? | Byron: el parquímetro guarda y reenvía (EAC-03) | §3.4, §5.1 |
| ¿Qué modelo de calidad usaron? | Jemima: ISO 9126, producto y calidad en uso; 25010 como sucesora | §5.2 |
| ¿Cómo protegen la base de placas? | Santiago: en los reportes la placa se cambia por un código, todo acceso queda registrado y los datos se borran a los 90 días (EAC-06). Lo aprendimos de lo que pasó en Antigua | §2.3, §3.4 |
| ¿Por qué no sensores desde el inicio? | Byron: costo, vandalismo y no hay datos; la arquitectura los deja preparados | §4.2 |
| ¿Qué metodología y por qué? | Santiago: híbrido espiral más Scrum, por los siete factores | §5.3 |

## Si dan 10 minutos

Se omiten las diapositivas 9 (despliegue: se nombra en la 8) y 12 (prototipo: se menciona en la 11), y la
13 se reduce a las cuatro fases. Reloj: Santiago 0:00-2:30, Jemima 2:30-4:00, Byron 4:00-6:30,
Jemima 6:30-8:00, Santiago 8:00-10:00.
