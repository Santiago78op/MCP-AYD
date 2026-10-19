---
tema: Guion de presentación
fuente: "Generado por 06-Proyecto-MCP/generar-presentacion-parq.py desde Guion - Presentación Caso Parquímetros.md"
fecha: 2026-10-19
tarea: Tarea 3 - Caso Parquímetros
---

# Guion de Byron Josué Par Rancho · Equipo de desarrollo

## Tus láminas

| Lámina | Título | Empieza en | Dura |
|---|---|---|---|
| **6** | El negocio: cinco procesos | 5:00 | 1:00 |
| **7** | Cuatro alternativas | 6:00 | 1:15 |
| **8** | La arquitectura: SOA con eventos | 7:15 | 1:15 |
| **9** | Despliegue | 8:30 | 1:00 |

Hablás **4:30** de los 15 minutos. Si dan 10 minutos: se omite la 9 (el despliegue se nombra en la 8); hablás de 4:00 a 6:30.

**Antes de hablar:** quién te pasa la palabra y con qué frase; **al terminar:** a quién se la pasás.

> *Entra después de Jemima (lámina 5).*

## Diapositiva 6 · El negocio: cinco procesos · Byron · 5:00

**Página 6 de 15** de la presentación

> Primero delimitamos el negocio: la gestión del estacionamiento en la vía pública. Los actores son el
> conductor, el comité vecinal, la Delegación, el área de tránsito, el banco y el proveedor del equipo.
> El verificador trabaja adentro, así que no es actor sino trabajador. Y el cuidacarros tampoco es
> actor: no participa en el negocio de forma legal, pero igual tenemos que tomarlo en cuenta.
> *(clic)* De ahí salen cinco procesos: concertar la zona, cobrar por placa, verificar y sancionar,
> rendir cuentas y mantener la red. Cada uno será un servicio.

## Diapositiva 7 · Cuatro alternativas · Byron · 6:00

**Página 7 de 15** de la presentación

> Evaluamos cuatro soluciones contra los seis problemas y los drivers.
> *(clic)* Uno: rediseñar solo la información. Barato, pero no toca la falta de personal.
> *(clic)* Dos: pagar con el número de placa, con monedas, tarjeta o celular, usando el mismo equipo que ya se compró.
> *(clic)* Tres: sensores por cajón y tarifa por demanda, como San Francisco. Caro y vulnerable al vandalismo.
> *(clic)* Cuatro: gobierno comunitario, que no es software pero resuelve consulta y confianza.
> Elegimos la dos como núcleo, con la uno adentro y la cuatro alrededor. La tres queda para después, cuando haya datos.

## Diapositiva 8 · La arquitectura: SOA con eventos · Byron · 7:15

**Página 8 de 15** de la presentación

> El estilo principal es SOA, arquitectura orientada a servicios: cada uno de los cinco procesos es un
> servicio independiente. Es justo lo que dice la lámina de clase: desarrollar los procesos de negocio
> como servicios.
> *(clic)* Y los servicios se avisan con eventos. Cuando alguien paga, el parquímetro avisa «pago
> registrado» y a ese aviso reaccionan la base de datos, las notificaciones y el tablero, sin que el
> parquímetro tenga que conocerlos.
> *(clic)* Cuatro decisiones cambian el día a día: el pago se liga a la placa y desaparece el boleto;
> se encienden el pago con tarjeta y la alarma; la multa solo nace cuando el oficial confirma la
> evidencia; y todo lo cobrado se publica.

## Diapositiva 9 · Despliegue · Byron · 8:30

**Página 9 de 15** de la presentación

> Así se despliega. Arriba, el parquímetro, el teléfono del conductor, el del verificador y la consola
> de la Delegación. El parquímetro se conecta por la red celular y, si se cae la señal, sigue cobrando,
> guarda los pagos y los manda cuando vuelve la conexión. Al centro, la nube con los seis servicios, la mensajería, la base de datos y la analítica;
> abajo, una réplica en otra región; a la derecha, el banco y la autoridad de tránsito.
> Jemima les muestra cómo medimos que esto funciona.

> *Al terminar, le pasa la palabra a Jemima (lámina 10).*


## Preguntas que te tocan

| Pregunta | Respuesta | Dónde está en el PDF |
|---|---|---|
| ¿Por qué SOA y no microservicios? | Byron: el programa no puede sumar personal (RE-07) para operar decenas de servicios | §5.1 |
| ¿Por qué el cuidacarros no es actor? | Byron: no interactúa de forma legítima; es factor externo y genera RE-12 y EAC-11 | Declaraciones, §5.5 |
| ¿Qué pasa si se cae la red? | Byron: el parquímetro guarda y reenvía (EAC-03) | §3.4, §5.1 |
| ¿Por qué no sensores desde el inicio? | Byron: costo, vandalismo y no hay datos; la arquitectura los deja preparados | §4.2 |
