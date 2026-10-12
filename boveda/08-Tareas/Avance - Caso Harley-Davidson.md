---
tema: Avance de tarea
fuente: "Tablero del Caso Harley-Davidson. Si discrepa de la Entrega, manda la Entrega."
fecha: 2026-10-13
tarea: Caso Harley-Davidson
alias: [avance harley, avance HD, tablero harley]
---

# Avance — Caso Harley-Davidson (proyecto SiL'K)

**Entrega y presentación: martes 13 de octubre de 2026.** Trabajo individual. Modo: **resolver y
explicar**. El entregable es [[Entrega - Caso Harley-Davidson]]; el estudio del enunciado,
[[Plan - Caso Harley-Davidson]]; el molde de clase, [[Ejemplo resuelto - Sistema de Transporte READM]].

## Criterios

| # | Criterio | Pts | Estado | Dónde |
|---|---|---|---|---|
| 1 | Caso de negocio: contexto, core, primera descomposición | 15 | hecho — 3 láminas verificadas | Entrega §1 |
| 2 | Stakeholders | 10 | hecho — 17, con interés propio y fuente | Entrega §2 |
| 3 | Drivers RF, de calidad y de restricción | 20 | hecho — 18 RF, 14 + 6 casos de uso en 4 diagramas, 9 EAC, 16 RE | Entrega §3 |
| 4 | Cuatro matrices acopladas | 15 | hecho — generadas de tres relaciones; la 3 se deriva | Entrega §4 |
| 5 | Estilos, bloques y despliegue | 20 | hecho — SOA + capas + eventos; 2 láminas verificadas | Entrega §5 |
| 6 | Drivers en los pasos y modelo de calidad | 20 | hecho — 7 pasos, EAC a tácticas, ISO/IEC 25010 | Entrega §6 |

## Archivos

| Qué | Dónde | Cómo se rehace |
|---|---|---|
| Documento que se sube | `08-Tareas/GrupoN_CasoHD.pdf` (36 páginas, apaisado) | `python3 06-Proyecto-MCP/generar-entrega-hd.py` |
| Versión editable | `08-Tareas/Entrega - Caso Harley-Davidson.docx` | el mismo comando |
| Las nueve láminas | `02-Diagramas/caso-hd/` | `python3 06-Proyecto-MCP/generar-excalidraw.py caso-hd/<carpeta>` |
| Presentación de 10 minutos | 12 láminas con notas del orador, en claude.ai | se edita en la página |

## Lo que falta — lo hace el estudiante

- [ ] Poner el **carné** en el encabezado del documento (está en blanco).
- [ ] Renombrar el PDF con el **número de grupo** que indique la catedrática.
- [ ] Confirmar con ella que la **presentación individual** habilita la entrega (duda 44).
- [ ] Ensayar la presentación una vez con reloj: 10 minutos.

## Supuestos declarados en la entrega

Las medidas de los nueve EAC, las dos restricciones regulatorias (RE-15 y RE-16) y el
dimensionamiento del despliegue: el caso no trae esos datos. También la lectura de «los pasos»
(los siete) y de «traer al presente» (se actualiza la tecnología, no los hechos): dudas 43 y 45.

## Lo que quedó fuera a propósito

| Qué | Por qué |
|---|---|
| Elegir uno de los tres proveedores de software | El caso no lo decide y la rúbrica no lo pide |
| Diagrama de componentes aparte | Los componentes van dentro de los nodos del despliegue |
| Descripción textual de los 14 casos de uso | Se entrega una (CU-02) como muestra de la plantilla |
| Lámina propia de la perspectiva lógica en capas | Va como tabla de responsabilidades (Entrega §5.7) |

## Bitácora

- **2026-10-12** — Enunciado estudiado y desarmado en el Plan. La catedrática respondió sobre el
  modelo de calidad: familia ISO, 9126 y serie 25000. Llegó la presentación *Calidad del Software*
  con el ejemplo READM: confirma `EAC-nn` y da el molde del diagrama de bloques basado en eventos.
- **2026-10-13** — Entrega armada: 9 láminas verificadas mirando la imagen, documento de 36 páginas
  y presentación de 12 láminas.

## Preguntas de repaso

1. ¿Qué tres cosas tiene que hacer el estudiante antes de subir el PDF?
2. ¿Qué supuestos declara la entrega y por qué hacen falta?
