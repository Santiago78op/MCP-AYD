---
tema: Arquitectura de software
fuente: "Presentación de clase — capturas_U2_F3 (33, 34, 35, 36, 37, 38, 39), serie «Estilos Arquitectónicos», subtítulo «–call return: SOA–». NÚCLEO."
fecha: 2026-09-17
---

# Flashcards — Arquitectura orientada a servicios (punto 1.9)

Compatible con el plugin **Spaced Repetition** de Obsidian: cada tarjeta es una línea con la
pregunta, el separador de dos signos de dos puntos, y la respuesta.

Notas: [[Arquitectura orientada a servicios]]

## Clase — capturas_U2_F3 (2026-09-17)

¿Cómo define la clase SOA "conceptualmente hablando"?::"Se refiere a la comunicación entre servicios, donde un servicio (cliente) realiza una solicitud (llamada) a otro servicio (proveedor) y espera una respuesta (retorno)"
¿A qué familia de estilos asigna la clase a SOA en el subtítulo de sus láminas?::A llamada y retorno: "Estilos Arquitectónicos –call return: SOA"
¿Por qué dice la clase que SOA también es event-based?::"Porque puede usar motores de orquestación/coreografía e invocar servicios de forma asíncrona"
¿De qué dos formas se hace la interacción en SOA, según la clase?::Mediante invocación directa o mediante el uso de un bus empresarial (ESB)
¿Qué dice la infografía que NO debe ser un servicio SOA?::"Un servicio SOA no debe ser tratado como un servicio proveído por un componente": provee interfaces con alcance de aplicación, no del nivel de componente u objeto
¿Cuáles son los cuatro escalones del "Funcionamiento de la Arquitectura (SOA)"?::Definición (define las necesidades del negocio), Desarrollo (desarrolla procesos de negocio como servicios), Evolución (permite que cada servicio evolucione independientemente) y Distribución (plantea aplicaciones distribuidas, multi-nivel)
¿Cuáles son los tres beneficios de SOA de la infografía de clase?::Alineación con el Dominio, Abstracción y Capacidad de Descubrimiento
En el beneficio "Abstracción" de SOA, ¿qué provee el desacople?::Que los servicios son autónomos y se accede a ellos a través de un contrato formal
¿Qué rótulos tienen el "Antes de SOA" y el "Después de SOA" en la figura de clase?::Antes: Silos aislados - Cerrados - Monolíticos. Después: Compartidos - Colaborativos - Interoperables - Integrado
Según la clase, ¿qué hay que determinar para diseñar la orquestación empresarial en SOA?::Recopilar la información, datos, objetivos y recursos, y determinar el traslape funcional y el potencial reúso (además de definir objetivos empresariales, maximizar reusabilidad e interoperabilidad y adaptarse a soluciones comerciales y no propias)
¿Qué cuatro hijos tiene SOA en el árbol de la infografía, y cuáles tiene Service?::SOA: Application frontend, Service, Service repository, Service bus. Service: Contract, Implementation, Interface (Implementation se divide en Business logic y Data)
¿Qué capas muestra la figura de clase de una solución SOA bancaria?::Acceso Multiplataforma, Componentes de Negocio Reutilizables, Servicios Reutilizables y Fuentes de Información (CRM, Bancos, Finanzas, DWH)
¿Qué se conecta al Enterprise Service Bus en la figura de clase?::Portal, SOAP (J2EE, .NET), Transacciones B2B, Flujo de Servicios, Datos, Aplicaciones Existentes y Nueva Lógica de Servicios
¿Qué ejemplos de aplicaciones orientadas a servicios da la infografía?::Sistemas que comparten información médica (Harvard Medical School), sistemas de reservas (Starwood Hotels and Resorts) y sistemas de WorkFlow (State Children's Health Insurance Program)
¿Qué taxonomía de clase choca con ubicar SOA bajo llamada y retorno?::El catálogo textual, que pone las arquitecturas orientadas a servicios bajo peer-to-peer. El árbol C&C sí coincide: SOA bajo Call-return y Event-based
