---
tema: Herramientas — StarUML
fuente: https://docs.staruml.io/ + repo staruml/staruml-mcp-server
fecha: 2026-08-19
version_documentada: StarUML v7
verificado_en_maquina: 2026-08-20 (StarUML 7.1.0, macOS, Node v26.3.0)
---

# StarUML — referencia de trabajo

Nota de referencia para cuando haya que **crear un diagrama formal en StarUML**. No es material
de la materia: es el manual de la herramienta, condensado a lo que se necesita para operarla
desde un cliente MCP.

> [!important] Consultá esto ANTES de generar Mermaid para StarUML
> El dato que más ahorra tiempo está en la sección "Qué acepta". StarUML importa **solo 7 tipos**
> de Mermaid. Si generás un `graph LR` o un diagrama de casos de uso esperando que entre como
> UML, no va a funcionar como esperás.

Fuente: <https://docs.staruml.io/> · MCP: <https://github.com/staruml/staruml-mcp-server>

---

## Qué acepta: los 7 tipos de Mermaid importables

Verificado en el esquema de entrada de la herramienta `generate_diagram` del MCP y en la página
*Mermaid Support* de la documentación:

| Mermaid | Entra a StarUML | Diagrama resultante |
|---|---|---|
| `classDiagram` | Sí | Class Diagram (UML) |
| `sequenceDiagram` | Sí | Sequence Diagram (UML) |
| `stateDiagram` | Sí | Statechart Diagram (UML) |
| `flowchart` | Sí | **Flowchart** (no UML) |
| `erDiagram` | Sí | Entity-Relationship Diagram |
| `requirementDiagram` | Sí | Requirement Diagram (SysML) |
| `mindmap` | Sí | Mindmap Diagram |

**Todo lo demás no se puede importar por Mermaid**, aunque StarUML sí lo soporte como diagrama
nativo. En particular, y esto importa para esta materia:

| Diagrama de la materia | ¿Existe en StarUML? | ¿Se puede importar por Mermaid? |
|---|---|---|
| Casos de uso | Sí, nativo | **No** |
| Componentes | Sí, nativo | **No** |
| Despliegue (deployment) | Sí, nativo | **No** |
| Actividad | Sí, nativo | **No** |
| Objetos, comunicación, timing | Sí, nativos | **No** |
| DFD (flujo de datos) | Sí, nativo | **No** |
| Paquetes | Sí, nativo | **No** |

> [!warning] La trampa del `flowchart`
> Un `flowchart` de Mermaid **siempre** entra como diagrama de **Flowchart**, nunca como UML.
> Si tenés un `flowchart` que *representa* casos de uso —como los de [[Caso de uso]] o los del
> [[diseño]] del proyecto MCP—, al importarlo obtenés cajas y flechas de flowchart, no actores
> y elipses de casos de uso. El diagrama se crea; lo que no se traduce es la **semántica UML**.
>
> Si necesitás un diagrama de casos de uso formal, hay dos caminos honestos:
> 1. Importar el `flowchart` y después convertir los elementos a mano en StarUML.
> 2. Dibujarlo directo en StarUML desde el diagrama nativo de casos de uso, usando el Mermaid
>    solo como guion de qué actores y qué casos de uso poner.

---

## El MCP de StarUML: las 4 herramientas

Del repositorio `staruml/staruml-mcp-server`:

| Herramienta | Parámetros | Qué hace |
|---|---|---|
| `generate_diagram` | `code` (string, **requerido**) — código Mermaid | Genera el diagrama en StarUML |
| `get_all_diagrams_info` | ninguno | Información de todos los diagramas del proyecto |
| `get_current_diagram_info` | ninguno | Información del diagrama abierto |
| `get_diagram_image_by_id` | `diagramId` (string, requerido) | Devuelve la imagen de un diagrama |

El `diagramId` sale de `get_all_diagrams_info`. Es el mismo patrón que
[[diseño|nuestro DA-06]]: primero listás para conseguir el id, después pedís por id.

**`generate_diagram` acepta Mermaid crudo en el parámetro `code`.** Por eso el flujo cruzado
funciona sin que nadie convierta nada: el texto que devuelve `obtener_diagrama` de nuestro
servidor entra directo acá.

---

## Requisitos para que funcione

| Requisito | Valor |
|---|---|
| StarUML | **v7.0.0 o superior** |
| Node.js | **v22 o superior** |
| API Server de StarUML | **activado** (ver abajo) |
| Puerto por defecto | 58321 |

### Activar el API Server (se olvida y es la causa típica de fallo)

El MCP no habla con StarUML por magia: usa el **API Server** interno de StarUML.

> [!warning] La documentación dice que viene apagado; en la 7.1.0 no
> Verificado el 20/08/2026 en esta máquina: con `settings.json` **sin ninguna de las dos claves**,
> StarUML 7.1.0 ya estaba escuchando en el 58321 (`lsof` lo confirma y `curl http://localhost:58321/`
> devuelve `Hello from StarUML API Server!`). O sea que en la 7.1 viene **encendido por defecto**.
> Igual conviene dejar las claves explícitas, para no depender de un default que puede cambiar.

Se editan en `settings.json`:

| SO | Ruta |
|---|---|
| **macOS** | `/Users/<usuario>/Library/Application Support/StarUML/settings.json` |
| Windows | `C:\Users\<usuario>\AppData\Roaming\StarUML\settings.json` |
| Linux | `~/.config/StarUML/settings.json` |

```json
{
  "apiServer": true,
  "apiServerPort": 58321
}
```

### Conectar el MCP

```json
{
  "mcpServers": {
    "staruml-mcp-server": {
      "command": "npx",
      "args": ["-y", "staruml-mcp-server"]
    }
  }
}
```

Si el puerto del API Server no es el 58321, se pasa `--api-port=<puerto>` en los `args`.

> [!danger] Editá `settings.json` con StarUML **cerrado**
> StarUML mantiene la configuración en memoria y **reescribe el archivo entero** al cerrar (guarda
> ahí el `windowState`). Cualquier clave que agregues con la app abierta se pierde al salir.

---

## Sin MCP: importar Mermaid a mano

También se puede, y conviene saberlo para cuando el MCP no esté conectado:

**Tools → Generate Diagram by Mermaid** → pegar el código → *Generate* → elegir el paquete que
va a contener el diagrama y sus elementos.

---

## Limitaciones de la importación, por tipo

Cosas de Mermaid que StarUML **ignora** al importar. Útil para no perder tiempo escribiendo algo
que no va a sobrevivir el viaje:

| Tipo | Lo que se pierde |
|---|---|
| Class Diagram | Namespaces, estilos y clases CSS, formato Markdown, links, interacciones |
| Sequence Diagram | Group/Box, color de fondo, estilos, menú de actor; mensajes sin punta de flecha, líneas con extremos cruzados, flechas bidireccionales. La activación se muestra en todo el diagrama |
| State Diagram | Estados compuestos, concurrencia, estilos y clases, formato Markdown |
| Flowchart | Algunas formas de nodo, formas expandidas, tipos de flecha no sólidos, animación, **subgraphs** |
| ER Diagram | Formato Markdown, estilos y clases |
| Requirement Diagram | Formato Markdown, estilos y clases |
| Mindmap | Formas de nodo, iconos y clases, formato Markdown |

> [!note] Los `subgraph` no sobreviven
> Varios diagramas de la bóveda usan `subgraph` para marcar el límite del sistema — por ejemplo
> el de [[Caso de uso]] y el de contexto en [[diseño]]. Al importarlos a StarUML **los subgraph
> se pierden**: los nodos entran, la caja que los agrupaba no.

---

## Los diagramas de la materia en StarUML

Mapa de qué diagrama nativo usar para cada tema del curso. Los nativos existen todos; la columna
de la derecha es la que dice si se puede llegar ahí por Mermaid o hay que dibujar.

| Tema | Diagrama en StarUML | Vía |
|---|---|---|
| [[Caso de uso]], [[Modelo de casos de uso del negocio]] | Use Case Diagram | dibujar |
| [[Modelo 4+1 vistas]] — vista lógica | Class Diagram, Package Diagram | Mermaid (clases) / dibujar (paquetes) |
| [[Modelo 4+1 vistas]] — vista de procesos | Activity Diagram | dibujar |
| [[Modelo 4+1 vistas]] — vista de desarrollo | Component Diagram, Package Diagram | dibujar |
| [[Modelo 4+1 vistas]] — vista física | Deployment Diagram | dibujar |
| Modelo entidad-relación | Entity-Relationship Diagram | Mermaid |
| DFD | Data Flow Diagram | dibujar |
| Estados | Statechart Diagram | Mermaid |
| Secuencia | Sequence Diagram | Mermaid |

StarUML v7 además trae C4, BPMN, wireframes y arquitectura AWS/GCP como diagramas adicionales, y
SysML (requisitos, bloques, paramétrico).

---

## Prueba real de `generate_diagram` (20/08/2026)

Se corrió la herramienta contra StarUML 7.1.0 abierto, con un **diagrama de contexto** de ejemplo
(una biblioteca, deliberadamente ajena al Caso 1). Qué se aprendió, más allá de lo que dice la doc:

**1. El diagrama de contexto SÍ entra; el core y la primera descomposición NO.**
Es consecuencia directa de los 7 tipos. El contexto es un `flowchart` —elipse del Producto,
rectángulos de entidades, flechas con nombre—, así que viaja entero. Las otras dos etapas de
[[Ejemplos resueltos de casos de negocio|la secuencia canónica]] son diagramas de casos de uso.

| Etapa del caso de negocio | Mermaid | ¿Entra por MCP? |
|---|---|---|
| Contexto | `flowchart` | **Sí** |
| Core | casos de uso | No — hay que dibujarlo |
| Primera descomposición | casos de uso | No — hay que dibujarlo |

**2. El MCP no levanta ninguna restricción: es el mismo importador.**
La descripción del parámetro `code` en el esquema de la herramienta lista **los mismos 7 tipos**
que el menú *Generate Diagram by Mermaid*. `generate_diagram` es ese importador expuesto por HTTP,
no una vía distinta con más capacidad.

**3. El acomodo del dibujo queda como trabajo manual.**
StarUML coloca los nodos pero **no reacomoda las etiquetas de las flechas**: se encimaron unas con
otras hasta quedar ilegibles. La herramienta ahorra tipear nodos y relaciones; no ahorra diagramar.

![[adjuntos/staruml-mcp/prueba-generate-diagram-contexto.png]]

**4. El diagrama se crea en el proyecto abierto, y el MCP no puede borrarlo.**
Aparece como `FCFlowchartDiagram` con el nombre *"Flowchart Diagram by Mermaid"*. Si sale mal, se
borra a mano desde el Model Explorer: no hay herramienta de borrado entre las 4.

**5. `get_diagram_image_by_id` devuelve PNG con marca de agua `UNREGISTERED`.**
Es la licencia de StarUML, no el MCP. Para una entrega, exportar desde una instalación licenciada.

---

## Cómo quedó conectado en esta máquina

No hay **Claude Desktop** instalado: el servidor está registrado en **Claude Code**, ámbito `user`
(`~/.claude.json`), o sea disponible desde cualquier carpeta.

```bash
claude mcp add staruml -s user -- npx -y staruml-mcp-server
claude mcp list      # staruml: npx -y staruml-mcp-server - Connected
```

Para que las herramientas aparezcan hay que **reiniciar la sesión** del cliente: los servidores MCP
se cargan al arrancar. Y **StarUML tiene que estar abierto** cuando se las use — el servidor es solo
un puente HTTP hacia la app.

---

## Notas relacionadas

- [[Excalidraw]] — la otra herramienta de dibujo del ecosistema
- [[diseño]] — el diseño del servidor MCP y el flujo cruzado
- [[Modelo 4+1 vistas]] — qué diagrama UML pide cada vista
- [[Caso de uso]]

## Preguntas de repaso

1. ¿Cuáles son los 7 tipos de Mermaid que StarUML puede importar?
2. Tenés un `flowchart` que modela casos de uso. ¿Qué obtenés al importarlo y qué NO?
3. ¿Qué parámetro recibe `generate_diagram` y de qué tipo?
4. ¿Qué hay que activar en StarUML para que el MCP pueda hablarle, y dónde?
5. ¿Qué le pasa a un `subgraph` de Mermaid al importarlo?
6. De las tres etapas del caso de negocio, ¿cuál se puede generar por MCP y por qué las otras dos no?
7. ¿Por qué hay que cerrar StarUML antes de editar su `settings.json`?
