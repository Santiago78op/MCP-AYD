---
tema: Guion de presentación
fuente: "Generado por 06-Proyecto-MCP/generar-presentacion-parq.py desde Guion - Presentación Caso Parquímetros.md"
fecha: 2026-10-19
tarea: Tarea 3 - Caso Parquímetros
---

# Guion de Byron Josué Par Rancho · Equipo de desarrollo

## Tus diapositivas

| Diapositiva | Arriba dice | Titular en pantalla | Empieza en | Dura |
|---|---|---|---|---|
| **6** | CASO DE NEGOCIO | El negocio son cinco procesos; el cuidacarros queda fuera, pero cuenta | 5:00 | 1:00 |
| **7** | POSIBLES SOLUCIONES | Elegimos pagar por placa con el equipo que ya se compró | 6:00 | 1:15 |
| **8** | ARQUITECTURA DEL SOFTWARE | Cada proceso es un servicio, y los servicios se avisan con eventos | 7:15 | 1:15 |
| **9** | DESPLIEGUE | El parquímetro sigue cobrando aunque se caiga la señal | 8:30 | 1:00 |

Hablás **4:30** de los 15 minutos. Si dan 10 minutos: se omite la 9 (el despliegue se nombra en la 8); hablás de 4:00 a 6:30.

**Cómo leerlo:** en cada diapositiva va primero **qué se ve al entrar**, después lo que decís (texto en gris), y en cada *(clic)* qué tarjeta aparece. La **idea clave** es lo único que no se puede olvidar. Arriba de tu primera diapositiva dice quién te pasa la palabra; abajo de la última, a quién se la pasás.

> *Entra después de Jemima (diapositiva 5).*

## Diapositiva 6 · CASO DE NEGOCIO · Byron · 5:00

**Página 6 de 15** · en pantalla: «El negocio son cinco procesos; el cuidacarros queda fuera, pero cuenta»

**Qué se ve al entrar:** a la izquierda, el texto con el negocio y los actores. El diagrama de la
derecha aparece con clic.

> Antes de diseñar el sistema definimos el negocio: gestionar el estacionamiento en la calle.
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

## Diapositiva 7 · POSIBLES SOLUCIONES · Byron · 6:00

**Página 7 de 15** · en pantalla: «Elegimos pagar por placa con el equipo que ya se compró»

**Qué se ve al entrar:** solo el título. Las cuatro soluciones aparecen una por clic.

> Comparamos cuatro soluciones contra los seis problemas.
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

## Diapositiva 8 · ARQUITECTURA DEL SOFTWARE · Byron · 7:15

**Página 8 de 15** · en pantalla: «Cada proceso es un servicio, y los servicios se avisan con eventos»

**Qué se ve al entrar:** a la izquierda, los cinco procesos. El diagrama de bloques y la fila de
cuatro decisiones aparecen con clic.

> Usamos SOA, que significa arquitectura orientada a servicios: el sistema se arma con piezas
> independientes llamadas servicios, una por cada proceso del negocio. Son los cinco que ven a la
> izquierda. Así lo enseña la clase: los procesos de negocio se desarrollan como servicios. Y como
> cada pieza es independiente, cada Delegación puede ir adoptándolas a su ritmo.
> *(clic)* **→ aparece el diagrama de bloques.** Los servicios se comunican con eventos. Un evento es un
> aviso de que algo pasó. Cuando alguien paga, el parquímetro avisa «pago registrado», y a ese aviso
> reaccionan la base de datos, las notificaciones y el tablero público, sin que el parquímetro tenga
> que conocerlos.
> *(clic)* **→ aparecen las cuatro decisiones.** Esto cambia cuatro cosas en la calle: el pago queda
> ligado a la placa y ya no hay boleto; se encienden el pago con tarjeta y la alarma; una multa solo
> existe si un oficial confirma la evidencia; y todo lo que se cobra se publica.

**Idea clave:** una pieza por proceso, y las piezas se avisan entre sí cuando algo pasa.

## Diapositiva 9 · DESPLIEGUE · Byron · 8:30

**Página 9 de 15** · en pantalla: «El parquímetro sigue cobrando aunque se caiga la señal»

**Qué se ve al entrar:** el diagrama de despliegue completo. No hay clics: se va señalando cada zona.

> El despliegue muestra en qué equipos corre cada parte. Arriba están los aparatos de la gente: el
> parquímetro, el celular del conductor, el del verificador y la computadora de la Delegación.
> El parquímetro se conecta por la red celular. Si se cae la señal, sigue cobrando: guarda los pagos y
> los envía cuando vuelve la conexión. Eso dice el título.
> Al centro está la nube: los seis servicios, que son los cinco procesos más uno que conecta con los
> sistemas de afuera; la mensajería, que lleva los avisos; la base de datos y la analítica. Abajo, una
> copia de todo en otra región por si falla la principal. A la derecha, el banco y la autoridad de
> tránsito.
> Jemima les muestra cómo medimos que esto funciona.

**Idea clave:** si se cae la señal, el parquímetro no pierde ningún pago.

> *Al terminar, le pasa la palabra a Jemima (diapositiva 10).*


## Preguntas que te tocan

| Pregunta | Respuesta | Dónde está en el PDF |
|---|---|---|
| ¿Por qué SOA y no microservicios? | Byron: «Microservicios son decenas de piezas pequeñas y cada una hay que operarla. SERVIparq ya tiene poco personal (RE-07), así que cinco servicios grandes, uno por proceso, es lo que puede sostener.» | §5.1 |
| ¿Por qué el cuidacarros no es actor? | Byron: «Un actor trata con el negocio de forma legítima, y el cuidacarros no. Lo tratamos como factor externo: genera una restricción (RE-12) y un escenario de calidad (EAC-11).» | Declaraciones, §5.5 |
| ¿Qué pasa si se cae la red? | Byron: «El parquímetro guarda los pagos y los manda cuando vuelve la señal. La meta es cero pagos perdidos (EAC-03).» | §3.4, §5.1 |
| ¿Por qué no sensores desde el inicio? | Byron: «Son caros, se pueden dañar y todavía no hay datos para fijar la tarifa por demanda. La arquitectura los deja preparados para la fase tres.» | §4.2 |

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
