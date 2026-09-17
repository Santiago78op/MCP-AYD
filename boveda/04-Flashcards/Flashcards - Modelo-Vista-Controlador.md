---
tema: Arquitectura de software
fuente: "Presentación de clase — capturas_U2_F3 (44, 45, 46, 47, 48), serie «Estilos Arquitectónicos». NÚCLEO."
fecha: 2026-09-17
---

# Flashcards — Modelo-Vista-Controlador (punto 1.9)

Compatible con el plugin **Spaced Repetition** de Obsidian: cada tarjeta es una línea con la
pregunta, el separador de dos signos de dos puntos, y la respuesta.

Notas: [[Modelo-Vista-Controlador]]

## Clase — capturas_U2_F3 (2026-09-17)

¿Qué tres cosas separa MVC según la diapositiva de clase?::"Los datos de una aplicación, la interfaz de usuario, y la lógica de control en tres componentes distintos"
¿Qué contiene el Modelo en MVC?::"Una representación de los datos que maneja el sistema, su lógica de negocio, y sus mecanismos de persistencia"
¿Qué es la Vista en MVC?::La interfaz de usuario, "que compone la información que se envía al cliente" y los mecanismos de interacción con éste
¿Qué hace el Controlador en MVC según la definición?::"Actúa como intermediario entre el Modelo y la Vista, gestionando el flujo de información entre ellos y las transformaciones para adaptar los datos a las necesidades de cada uno"
¿Cuáles son las cuatro responsabilidades del modelo?::Acceder a la capa de almacenamiento de datos (idealmente independiente de ella), definir las reglas de negocio, llevar un registro de las vistas y controladores, y si es activo notificar a las vistas los cambios producidos por un agente externo
¿Qué ejemplo de regla de negocio del modelo da la diapositiva?::"Si la mercancía pedida no está en el almacén, consultar el tiempo de entrega estándar del proveedor"
¿Qué es un modelo activo en MVC?::El que notifica a las vistas los cambios que en los datos pueda producir un agente externo, por ejemplo un fichero por lotes que actualiza los datos o un temporizador que desencadena una inserción
¿De qué son responsables las vistas en MVC?::Recibir datos del modelo y mostrarlos al usuario, tener un registro de su controlador asociado (normalmente porque lo instancian) y dar el servicio "Actualización()"
¿Quién puede invocar el servicio "Actualización()" de la vista?::El controlador, o el modelo cuando es un modelo activo que informa de cambios producidos por otros agentes
¿De qué es responsable el controlador en MVC?::Recibe los eventos de entrada (un clic, un cambio en un campo de texto) y contiene reglas de gestión de eventos del tipo "SI Evento Z, entonces Acción W", que suponen peticiones al modelo o a las vistas
¿Qué ejemplos de petición del controlador da la diapositiva?::A las vistas, una llamada al método "Actualizar()". Al modelo, "Obtener_tiempo_de_entrega ( nueva_orden_de_venta )"
En MVC, ¿las reglas de negocio van en el controlador?::No. Las define el Modelo. El controlador tiene reglas de gestión de eventos y le pide al modelo lo que necesita
En el diagrama del sistema de ventas, ¿qué encierra cada recuadro rojo?::Izquierda, el Modelo (Oracle Database y los discos). Centro, las terminales Ventas, Cajero y Administrador (la Vista, sin rótulo propio). Derecha, el Controlador (los tres servidores)
¿MVC es estilo o patrón para la clase?::Patrón arquitectónico (título de las diapositivas). Un estilo lo utiliza, y el catálogo lo ubica en la familia llamada y retorno
¿Por qué MVC no equivale a tres capas?::Porque la lógica de negocio está en el Modelo junto con los datos, el Controlador solo gestiona eventos, y el modelo activo habla directo con la vista sin pasar por el controlador
