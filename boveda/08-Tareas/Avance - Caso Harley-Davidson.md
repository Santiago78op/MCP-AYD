---
tema: Avance de tarea
fuente: "Tablero del Caso Harley-Davidson. Si discrepa de la Entrega, manda la Entrega."
fecha: 2026-10-13
tarea: Caso Harley-Davidson
alias: [avance harley, avance HD, tablero harley]
---

# Avance — Caso Harley-Davidson (proyecto SiL'K)

**Entrega y presentación: martes 13 de octubre de 2026.** Se entrega como **Grupo 2** (cuatro
integrantes); el material lo elabora Santiago. Modo: **resolver y explicar**. El entregable es [[Entrega - Caso Harley-Davidson]]; el estudio del enunciado,
[[Plan - Caso Harley-Davidson]]; el molde de clase, [[Ejemplo resuelto - Sistema de Transporte READM]].

## Criterios

| # | Criterio | Pts | Estado | Dónde |
|---|---|---|---|---|
| 1 | Caso de negocio: contexto, core, primera descomposición | 15 | hecho — 3 láminas verificadas | Entrega §1 |
| 2 | Stakeholders | 10 | hecho — 17, con interés propio y fuente | Entrega §2 |
| 3 | Drivers RF, de calidad y de restricción | 20 | hecho — 18 RF, 20 casos de uso en 4 diagramas con sus 20 descripciones textuales, 9 EAC, 16 RE | Entrega §3 |
| 4 | Cuatro matrices acopladas | 15 | hecho — generadas de tres relaciones; la 3 se deriva | Entrega §4 |
| 5 | Estilos, bloques y despliegue | 20 | hecho — SOA + capas + eventos; 2 láminas verificadas | Entrega §5 |
| 6 | Drivers en los pasos y modelo de calidad | 20 | hecho — 7 pasos, EAC a tácticas, ISO/IEC 25010 | Entrega §6 |

## Archivos

| Qué | Dónde | Cómo se rehace |
|---|---|---|
| Documento que se sube | `08-Tareas/Grupo2_CasoHD.pdf` (48 páginas, apaisado) | `python3 06-Proyecto-MCP/generar-entrega-hd.py` |
| Versión editable | `08-Tareas/Entrega - Caso Harley-Davidson.docx` | el mismo comando |
| Las nueve láminas y tres detalles del despliegue | `02-Diagramas/caso-hd/` | `python3 06-Proyecto-MCP/generar-excalidraw.py caso-hd/<carpeta>`; los detalles los recorta el generador de la entrega |
| Presentación de 10 minutos | 13 láminas con animaciones, en claude.ai | se edita en la página |
| Presentación en PowerPoint | `08-Tareas/Grupo2_CasoHD_Presentacion.pptx`: 13 láminas, transiciones, 23 animaciones por clic, el guion en las notas, en Arial | `python3 06-Proyecto-MCP/animar-pptx.py <exportado.pptx> <salida.pptx> <guion.md> Arial` |
| Guion para exponer | `08-Tareas/Guion - Presentación Caso Harley-Davidson.md` | a mano |

## Lo que falta — lo hace el estudiante

- [x] Integrantes y carnés en el encabezado (Grupo 2).
- [x] Nombre del archivo: `Grupo2_CasoHD.pdf`.
- [ ] Ensayar la presentación una vez con reloj: 10 minutos, 23 clics de animación.
- [x] Presentación descargada en PowerPoint y completada (el exportado venía sin animaciones).
- [ ] Abrir `Grupo2_CasoHD_Presentacion.pptx` en PowerPoint o Keynote y pasarla una vez: las animaciones se validaron por estructura, no reproducidas.

> [!warning] La nota de la rúbrica sobre los integrantes
> El enunciado dice: *"SOLO TOMEN EN CUENTA A LAS PERSONAS DEL EQUIPO QUE TRABAJEN ACTIVAMENTE EN LA
> TAREA."* El encabezado lista a los cuatro por decisión del estudiante.

## Supuestos declarados en la entrega

Las medidas de los nueve EAC, las dos restricciones regulatorias (RE-15 y RE-16) y el
dimensionamiento del despliegue: el caso no trae esos datos. También la lectura de «los pasos»
(los siete) y de «traer al presente» (se actualiza la tecnología, no los hechos): dudas 43 y 45.

## Lo que quedó fuera a propósito

| Qué | Por qué |
|---|---|
| Elegir uno de los tres proveedores de software | El caso no lo decide y la rúbrica no lo pide |
| Diagrama de componentes aparte | Los componentes van dentro de los nodos del despliegue |
| Lámina propia de la perspectiva lógica en capas | Va como tabla de responsabilidades (Entrega §5.8) |

## Bitácora

- **2026-10-12** — Enunciado estudiado y desarmado en el Plan. La catedrática respondió sobre el
  modelo de calidad: familia ISO, 9126 y serie 25000. Llegó la presentación *Calidad del Software*
  con el ejemplo READM: confirma `EAC-nn` y da el molde del diagrama de bloques basado en eventos.
- **2026-10-13** — Entrega armada: 9 láminas verificadas mirando la imagen, documento de 36 páginas
  y presentación de 12 láminas.
- **2026-10-13, revisión** — El diagrama de contexto se rehízo con el molde de FarmaHosp (elipse normal al
  centro, entidades alrededor, rótulos horizontales): la primera versión estiraba la elipse y no era la
  figura de la notación. Al documento se le sumaron referencias y se le quitaron las rayas largas. La
  presentación pasó a un estilo sobrio de fondo oscuro, sin tonos crema ni degradados.
- **2026-10-13, validación** — Revisión contra la rúbrica: se corrigieron tres fallas (un caso de uso
  llamado «Consultar…», CU-20 sin actor, y matrices 2 y 3 sin el proceso del criterio 1). El PDF se
  reordenó para no dejar páginas a medio llenar: de 37 a 32, todas por encima del 64 % de ocupación.
- **2026-10-13, cierre** — Descripciones textuales de los veinte casos de uso, agrupadas por proceso junto a
  su diagrama. Letra más grande en bloques y despliegue, y tres figuras de detalle del despliegue. El PDF
  quedó en 48 páginas, ninguna por debajo del 47 % de ocupación. Guion de exposición escrito.
- **2026-10-13, PowerPoint** — El `.pptx` exportado desde la página no trae animaciones ni transiciones y
  depende de una tipografía que no está instalada. `animar-pptx.py` le agrega 13 transiciones, 23
  animaciones de entrada por clic y el guion como notas, y cambia la tipografía a Arial.

## Preguntas de repaso

1. ¿Qué tres cosas tiene que hacer el estudiante antes de subir el PDF?
2. ¿Qué supuestos declara la entrega y por qué hacen falta?
