---
tema: Arquitectura de software
fuente: "Presentación de clase — capturas_U2 (50, 51, 52). NÚCLEO. + COMPLEMENTO — conocimiento general de AWS/Azure y on premise vs cloud (marcado)"
fecha: 2026-09-15
punto_del_programa: "1.9 — Diseño Arquitectónico: on premise, cloud"
---

# Arquitectura en la nube

Cubre la parte **cloud** del punto 1.9 del programa (*"Diseño Arquitectónico: on premise, cloud"*).
La clase la dio con tres diapositivas: una definición con un diagrama de AWS, el caso de Amazon Prime
Video y una arquitectura de N-niveles en Azure. Ver [[Estilos arquitectónicos]].

---

## 1. Qué es: la definición de clase

Diapositiva *"Cloud Computing"*, textual:

> La **arquitectura de la nube** se compone de los **componentes y subcomponentes que se encuentran en
> una nube**. Si bien es una descripción muy general, en la arquitectura de la nube hay **mucho más
> que solo tecnología**.

> Se refiere al **diseño** y **conecta todos los componentes y tecnologías necesarios para la
> computación en la nube**.

![[adjuntos/capturas-clase-U2/estilos/cloud-computing-definicion.png]]

Las dos frases, desarmadas:

| Frase | Qué quiere decir |
|---|---|
| *"componentes y subcomponentes que se encuentran en una nube"* | la arquitectura en la nube sigue siendo **componentes y relaciones**, igual que cualquier arquitectura; lo que cambia es **dónde** viven |
| *"hay mucho más que solo tecnología"* | no alcanza con listar servicios del proveedor: hay decisiones de diseño detrás (cómo se conectan, cómo se reparten, cómo escalan) |
| *"se refiere al diseño y conecta todos los componentes"* | es un **diseño**: decide la conexión entre las piezas |

**Regla para el examen:** *arquitectura de la nube = los componentes y subcomponentes que están en una
nube, más el diseño que los conecta; es más que tecnología.*

### El diagrama de la diapositiva: un portal bancario en AWS

Sin texto que lo explique en la diapositiva. Leído con zoom (no se redibuja; varios rótulos son muy
chicos y se marcan como dudosos):

| Zona | Elementos |
|---|---|
| **Usuario** | *Socio*, que entra por *Canal Web* y por *Canal Móvil* |
| **Recuadro "Portal Bancario"** (cuenta de AWS), parte superior | *CloudFront* → *Frontend estático* (bucket S3) · *API Gateway* → *Lambda Authorizer* → *DynamoDB* |
| **VPC** dentro del portal | *VPC Endpoint* → *Network Load Balancer* → *Kubernetes Nodes* en **tres Availability zones** (subredes privadas) con *Auto Scaling* |
| **Datos**, en cada zona | *Amazon Aurora* (un *Writer* en la zona 2 y *Readers* en las zonas 1 y 3, unidos por línea punteada) · *ElastiCache* en las tres |
| **Servicios de soporte** | *Amazon EKS* · *Amazon ECR* |
| **Conexión hacia afuera** | *VPC Attachment* → *Transit Gateway Network Account* → ícono de VPN (rótulo ilegible) |
| **Recuadro "Cooperativa"** | *Service Bus* → *Servicios SOAP* → *Mainframe*; los Kubernetes Nodes llegan al *Service Bus*. Es el mismo bus empresarial con SOAP que la clase dio en SOA → [[Arquitectura orientada a servicios]] §8 |

> [!tip] Lo que se puede leer en el dibujo sin agregar nada
> - **Tres zonas de disponibilidad** con la misma estructura: la aplicación está **replicada**.
> - La **base de datos** tiene un solo escritor y varios lectores.
> - El recuadro **"Cooperativa"** está **fuera** del portal de AWS y tiene un **Mainframe**: el
>   diagrama mezcla nube con un sistema propio de la organización. Es un buen ejemplo para el
>   contraste *on premise* vs *cloud* (§4).

---

## 2. El caso Prime Video

La diapositiva *"Monolítica en AWS: La Arquitectura de Amazon Prime Video"* se estudia en
[[Arquitectura monolítica]] §3, con su tabla de elementos y la advertencia sobre qué muestra
realmente el diagrama.

Lo que aporta a esta nota: **nube y monolito no se excluyen**. El estilo (monolítico, en capas…)
es una decisión; que corra en la nube es **otra** decisión, de despliegue.

---

## 3. N-niveles en la nube (Azure)

Diapositiva *"N-niveles en la nube"*. Es un diagrama sin texto explicativo, con íconos de Azure.

![[adjuntos/capturas-clase-U2/estilos/n-niveles-en-la-nube-azure.png]]

Leído a resolución completa (no se redibuja):

| Zona (de izquierda a derecha) | Elementos | Qué pasa |
|---|---|---|
| **Internet** | — | el tráfico entra a un **Load balancer** |
| **DMZ** | dos VM **NVA** | el load balancer reparte entre las dos NVA, que pasan el tráfico al siguiente load balancer |
| **Web tier** | **Load balancer** + tres **VM** | reparte entre las tres VM web |
| **Business tier** | **Load balancer** + tres **VM** | recibe desde el web tier y reparte entre las tres VM de negocio |
| **Data tier** | **Load balancer** + **SQL Server (primary)** y **SQL Server (secondary)** | recibe desde el business tier y reparte hacia los dos SQL Server |
| **Acceso de administración** | **DevOps** → *Azure Portal* → VM **Bastion** en la *AzureBastionSubnet* | entrada separada, solo para operar |
| **Contenedor** | un recuadro punteado, **Virtual network**, encierra la DMZ, los tres tiers y el Bastion; Internet, el primer load balancer, DevOps y Azure Portal quedan afuera | — |

Cómo se relaciona con lo que dio la clase:

| En [[Arquitectura en capas]] (N-Capas) | En N-niveles en la nube |
|---|---|
| Presentación | **Web tier** |
| Negocio | **Business tier** |
| Datos (SGBD) | **Data tier** |
| Servidor aplicativo = **tres** servidores | cada tier con **tres VM** detrás de un **load balancer** |
| (el ícono chico sin rótulo entre cliente y servidores — correspondencia probable, no confirmada) | **DMZ** con las NVA |

Es **el mismo estilo** que N-Capas, **desplegado en la nube**. Lo nuevo que agrega el dibujo:

| Elemento | Para qué está (en el dibujo) |
|---|---|
| **Load balancer delante de cada tier** | cada nivel escala solo: se agregan VM sin tocar los otros niveles — la *"arquitectura escalable"* de la definición de N-Capas |
| **SQL Server primary / secondary** | la base tiene respaldo |
| **DMZ** | una zona intermedia entre Internet y los tiers de la aplicación |
| **Bastion** separado | los administradores no entran por el mismo camino que los usuarios |

> [!note] COMPLEMENTO — siglas que la diapositiva no explica
> - **DMZ** (*zona desmilitarizada*): subred intermedia entre Internet y la red interna, donde se
>   ponen los elementos expuestos.
> - **NVA** (*Network Virtual Appliance*): una VM que cumple función de red, típicamente firewall.
> - **Bastion**: máquina de salto para administrar las VM sin exponerlas directamente a Internet.
> - **Load balancer**: reparte las peticiones entre varias instancias iguales.
> - El dibujo corresponde a la arquitectura de referencia de N-tier que publica Microsoft para Azure.
>
> Y fijate en el vocabulario: la diapositiva dice *"N-**niveles**"* y el dibujo *"**tier**"*; en
> N-Capas decía *"capas"*. La clase los usa como sinónimos — ver [[Arquitectura en capas]] §4.

**Regla para el examen:** *N-niveles en la nube = presentación (web), negocio y datos en tiers
separados, cada uno detrás de un load balancer, dentro de una red virtual, con DMZ a la entrada y
bastion para administrar.*

---

## 4. On premise vs cloud

> [!warning] COMPLEMENTO — no hay diapositiva de on premise
> El programa pide *"Diseño Arquitectónico: on premise, cloud"*. La clase dio **cloud**; el
> contraste con **on premise** no tiene diapositiva. Lo que sigue es conocimiento general.

| | **On premise** | **Cloud** |
|---|---|---|
| Dónde está la infraestructura | en instalaciones **propias** de la organización | en un **proveedor** (AWS, Azure…) |
| Quién la compra y la opera | la organización | el proveedor; la organización paga por uso |
| Cómo se escala | comprando hardware | agregando instancias (como las VM detrás de cada load balancer) |
| Control | total | compartido con el proveedor |

La idea que une esto con el resto de la unidad: **on premise vs cloud es una decisión de despliegue,
no de estilo.** El mismo estilo en capas puede correr en servidores propios (el diagrama de N-Capas)
o en la nube (el de Azure). Lo que cambia son los atributos de calidad alcanzables y los costos. Y
las dos cosas pueden convivir: el portal bancario de §1 está en AWS pero se conecta al **Mainframe**
de la **Cooperativa**. Ver [[Diagrama de despliegue]].

---

## Notas relacionadas

- [[Estilos arquitectónicos]] — el catálogo y el punto 1.9
- [[Arquitectura en capas]] — N-Capas, el estilo que la nube despliega por tiers
- [[Arquitectura monolítica]] — el caso Prime Video en AWS
- [[Diagrama de despliegue]] — dónde se modela la decisión on premise vs cloud
- [[Atributos de calidad]] — escalabilidad, disponibilidad, seguridad
- [[Arquitectura orientada a servicios]] — el *Enterprise Service Bus* del recuadro Cooperativa

## Preguntas de repaso

1. Citá la definición de arquitectura de la nube de la clase. ¿Por qué dice que es "más que solo tecnología"?
2. En el diagrama de N-niveles en Azure, ¿cuáles son los tres tiers y qué hay delante de cada uno?
3. ¿Para qué están la DMZ y el Bastion en ese diagrama?
4. ¿Qué relación hay entre N-Capas y N-niveles en la nube?
5. ¿Por qué on premise vs cloud es una decisión de despliegue y no de estilo? Dá un ejemplo con los diagramas de clase.
