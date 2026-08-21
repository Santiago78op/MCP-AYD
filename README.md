# Tutor AYDS

Tutor personal de **Análisis y Diseño de Sistemas II** (curso 785, Escuela de Ciencias y Sistemas,
USAC): una bóveda de Obsidian con los apuntes del curso, más un servidor MCP que la expone como
herramientas para Claude.

```
tutor-ayds/
├── boveda/      Los apuntes: notas, glosario, flashcards, guías de tareas
└── ayds-mcp/    El servidor MCP que sirve esa bóveda (12 herramientas)
```

---

## Instalación en macOS

```bash
git clone <la-url-de-tu-repo> ~/tutor-ayds
cd ~/tutor-ayds
bash instalar.sh
```

Eso es todo. El script detecta qué tenés, instala solo lo que falta, compila, corre las tres
auditorías y registra el servidor en Claude Code.

Para ver qué haría sin que toque nada:

```bash
bash instalar.sh --verificar
```

> [!NOTE]
> **El script no instala runtimes por su cuenta.** Si falta Node o es viejo, te dice el comando y se
> detiene. Es a propósito: elegir entre `brew` y `nvm` es tu decisión, y así no terminás con dos
> versiones de Node instaladas.

### Lo imprescindible

**Node.js ≥ 20** para el servidor (dependencias JavaScript puro, sin compilador de C ni base de
datos) y **Python 3** para las herramientas de la bóveda (`sincronizar.py` y los generadores de
diagramas — solo biblioteca estándar, sin pip).

```bash
node -v                 # >= 20
node -p process.arch    # arm64 en un Mac con Apple Silicon
```

Si falta: `brew install node` (o `nvm install 22`, si ya usás nvm).

### Lo opcional

| | Para qué | Si falta |
|---|---|---|
| **Obsidian** | Leer y editar la bóveda cómodamente | El servidor funciona igual: lee los `.md` directo |
| **Claude Code** (CLI) | Usar el tutor desde la terminal | Se puede usar solo con Claude Desktop |
| **Claude Desktop** | Usar el tutor en la app | Se puede usar solo con Claude Code |
| **StarUML v7+** | Modelar y validar la semántica UML | Ojo, medido: **sin licencia marca TODA exportación, SVG incluido** — la lámina final sale del generador |
| **Google Chrome** + MCP `chrome-devtools` | La verificación visual de los diagramas (paso 4 del checklist) | El instalador registra el MCP; sin Chrome no hay verificación |

> [!IMPORTANT]
> **No copies `node_modules` de otra máquina.** TypeScript 7 instala un binario del compilador **por
> plataforma**: el árbol de dependencias de una máquina Windows no sirve en el Mac. Si lo trajiste,
> `rm -rf ayds-mcp/node_modules ayds-mcp/dist` y volvé a correr el script.

---

## Las herramientas de la bóveda

Tres scripts Python (biblioteca estándar, sin pip), documentados en
`boveda/06-Proyecto-MCP/estilo-diagramas.md`:

| Script | Qué hace | Comando |
|---|---|---|
| `boveda/sincronizar.py` | Valida (y repara con `--aplicar`) que este repo y el vault de trabajo `SO2_MT` queden **idénticos** | `python3 boveda/sincronizar.py` |
| `boveda/06-Proyecto-MCP/generar-excalidraw.py` | De coordenadas explícitas emite la lámina: `.excalidraw` editable **y** `.svg` vectorial sin marca de agua. Determinista: mismos bytes en cualquier máquina | `python3 …/generar-excalidraw.py <nombre>` |
| `boveda/06-Proyecto-MCP/generar-mdj.py` | Escribe el proyecto **nativo `.mdj` de StarUML** con el layout ya resuelto (el MCP de StarUML no posiciona elementos) | `python3 …/generar-mdj.py <nombre>` |

Las láminas generadas viven versionadas en `boveda/02-Diagramas/` — tras `git pull`, las dos
máquinas ya comparten exactamente los mismos archivos.

## El espejo con el repo de trabajo

`boveda/` es un **espejo** del vault del repo `SO2_MT` (`~/Desktop/SO2/AYD_2/Ayd`): se estudia en
dos máquinas y cada cambio se espeja y commitea **en los dos repos en el mismo movimiento**. La
validación no es a ojo: `python3 boveda/sincronizar.py` compara archivo por archivo y sale con
código 1 si hay desfase. El instalador corre esta validación en su sección 8. Las únicas
diferencias legítimas son `.claude/` y `CLAUDE.md`.

## Probarlo

```bash
claude
```

Y algunas cosas que se le pueden pedir:

```
¿Qué notas tengo sobre arquitectura de software?

Tomame un quiz de 5 preguntas de casos de uso del negocio y corregime.

¿Por dónde empiezo el Caso 1 de FarmaHosp?

Tomá el diagrama de secuencia de la nota "diseño" y creálo en StarUML.
```

El último cruza tres sistemas: el cliente pide la fuente a este servidor y se la pasa al MCP de
StarUML. Los servidores MCP no se hablan entre sí — el cliente es el único integrador.

---

## Qué hace y qué no

**Hace:** sirve el contenido de la bóveda (notas, glosario, diagramas, flashcards), el manual de las
herramientas de dibujo, el método para resolver tareas, y registra el progreso de los quizzes.

**No hace, a propósito:** no razona, no dibuja, no convierte formatos y no llama a otros servidores
MCP. Armar un quiz o decidir a qué diagrama UML corresponde un `flowchart` es trabajo del modelo.
Dibujar es de StarUML y Excalidraw, cada uno por su propio MCP.

Y una regla que está escrita en el código: **guía, no resuelve las tareas.** Las guías tienen bloques
"tu turno" donde el estudiante para y trabaja, y los ejemplos son de otro dominio para que no se
copien.

### Las 12 herramientas

| Herramienta | Qué devuelve | Escribe |
|---|---|---|
| `listar_temas()` | Las notas con su tema, fuente y fecha | No |
| `leer_nota(nombre)` | El contenido completo de una nota | No |
| `buscar(consulta)` | Fragmentos con archivo y número de línea | No |
| `glosario(termino?)` | Definición breve, o el glosario completo | No |
| `listar_diagramas()` | Archivos de `02-Diagramas/` más los bloques mermaid de las notas | No |
| `obtener_diagrama(nombre)` | La fuente cruda del diagrama, con su tipo | No |
| `obtener_flashcards(tema, cantidad?)` | Tarjetas de repaso, ya separadas en P / R | No |
| `registrar_resultado(tema, puntaje, comentarios?)` | Agrega una línea a `05-Quizzes/progreso.md` | **Sí** |
| `progreso()` | Temas evaluados, puntajes y pendientes | No |
| `referencia(herramienta?)` | Manual de StarUML/Excalidraw y sus límites | No |
| `metodo_tarea(entregable?)` | El método de trabajo y las guías paso a paso | No |
| `enunciado(nombre?)` | El enunciado de una tarea, para citarlo textual | No |

**Once de doce son de solo lectura.** La única escritura toca un solo archivo, y su ruta sale de una
constante: no hay parámetro por donde pasarle otra.

---

## Mantenimiento

```bash
cd ayds-mcp
npm run build            # compilar
npm run verificar        # 33 pruebas de lógica (usa una bóveda temporal)
npm run auditoria        # las 12 herramientas por el protocolo MCP real
npm run auditar-boveda   # integridad de la bóveda y de la documentación
npm run cobertura        # 39 consultas reales: ¿el MCP encuentra el contenido?
npm run atlas            # genera el Atlas de Diagramas de la bóveda
npm run comprobar        # diagnóstico del entorno
```

Las cuatro primeras responden preguntas distintas:

| Prueba | Qué verifica | Falla cuando… |
|---|---|---|
| `verificar` | la **lógica**, contra una bóveda temporal | se rompe una función de `src/` |
| `auditoria` | las **12 herramientas** por el protocolo MCP real | una herramienta deja de responder o de rechazar basura |
| `auditar-boveda` | el **contenido** y la coherencia de la documentación | hay un wikilink roto, frontmatter faltante o un conteo desactualizado |
| `cobertura` | que cada consulta real **encuentre su nota** | se agrega una nota y nadie le pone alias: existe pero es inalcanzable |

### El atlas de diagramas

`npm run atlas` no es una prueba: recorre la bóveda y arma **una sola página** con los **106**
bloques `mermaid` renderizados, agrupados por tema, con filtro por texto y por procedencia
(de clase / complemento / propio). Sirve para repasar antes de un parcial y para ver de un vistazo
si algún diagrama quedó mal.

Cada hoja lleva su identificador `Nota#mermaid-N`, el mismo que acepta `obtener_diagrama`, así que
de la página se puede volver al código fuente sin buscar.

> **Cómo verlo.** Emite los diagramas como `<pre class="mermaid">` **sin cargar ninguna librería**,
> porque el visor de artifacts de Claude renderiza mermaid nativo. Si la abrís con `file://` no se
> dibuja nada: el navegador bloquea el CDN desde el sistema de archivos. O la publicás como
> artifact, o la servís por HTTP agregando el script a mano.

La salida (`atlas-de-diagramas.html`) está en `.gitignore`: se regenera de la bóveda, y versionarla
sería tener dos fuentes de verdad para los mismos diagramas.

Si tocás `src/`, hay que compilar para que el servidor registrado use el código nuevo.

Corré `auditar-boveda` cada vez que agregues una herramienta o un lote de notas: detecta wikilinks
rotos, imágenes que faltan, glosario desordenado y documentación desactualizada.

---

## Documentación

| Documento | Qué contiene |
|---|---|
| `CLAUDE.md` | Cómo debe usar todo esto Claude Code (se lee solo al abrir el repo) |
| `ayds-mcp/README.md` | Detalle del servidor: configuración, problemas comunes, decisiones |
| `boveda/Índice.md` | Punto de entrada de los apuntes |
| `boveda/Programa oficial del curso.md` | Contenido temático, cronograma y fechas de parciales |
| `boveda/06-Proyecto-MCP/diseño.md` | El diseño del servidor: actores, RF, RNF, 13 decisiones de arquitectura |

Ese último documento es, además, el proyecto práctico de la materia: usa la teoría del curso
(casos de uso, vistas, trazabilidad) para diseñar el servidor que sirve los apuntes de esa teoría.
