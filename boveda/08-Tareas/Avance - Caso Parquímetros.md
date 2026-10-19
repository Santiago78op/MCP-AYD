---
tema: Avance de tarea
fuente: "Tablero de la Tarea 3 (Caso 4, Repensando los parquímetros). Si discrepa de la Entrega, manda la Entrega."
fecha: 2026-10-19
tarea: Tarea 3 - Caso Parquímetros
alias: [avance parquimetros, avance tarea 3, tablero parquimetros]
---

# Avance: Tarea 3, Caso 4 Repensando los parquímetros

Llegó el **2026-10-19**. Se entrega y expone como **Grupo 2**, ahora de **tres** integrantes (Elías
Vasquez salió del grupo); Santiago coordina. Modo: **resolver y explicar** («crea todo»). La fecha
de entrega y la duración de la exposición **no** están en el enunciado: se supusieron 15 minutos.
El entregable es [[Entrega - Caso Parquímetros]]; el enunciado, [[enunciados/Caso Parquímetros|Caso Parquímetros]].

## Lo que pide la consigna

| Pide | Estado | Dónde |
|---|---|---|
| Análisis del caso | hecho: resumen, 11 stakeholders, 6 problemáticas con causa raíz | Entrega §1 |
| Investigación de tópicos | hecho: San Francisco, Seattle, Pay and Display; Guatemala (COM-40-2022, cuidacarros, MarbEx y la CC) | Entrega §2 |
| Posibles soluciones en las 4 perspectivas | hecho: 4 alternativas evaluadas contra problemas y drivers | Entrega §3-§4 |
| Solución seleccionada, justificada | hecho: SOA + eventos + capas + guardar y reenviar; calidad ISO 9126; espiral + Scrum; AI por momento de uso; respuesta a los cuidacarros | Entrega §5 |
| Respuestas a las 14 preguntas del caso | hecho | Entrega §6 |
| Parte desarrollada (opcional) | hecho: prototipo del parquímetro con modo de prueba de desempeño | Entrega §7 |
| Presentación | hecho: 15 láminas, 31 clics, verificada en Keynote (46 estados) | ver Archivos |
| Guion por integrante | hecho | ver Archivos |

## Archivos

| Qué | Dónde | Cómo se rehace |
|---|---|---|
| Documento que se sube | `08-Tareas/Grupo2_CasoParquimetros.pdf` (35 páginas, apaisado) y `.docx` | `python3 06-Proyecto-MCP/generar-entrega-parq.py` |
| Presentación | `08-Tareas/Grupo2_CasoParquimetros_Presentacion.pptx` (Arial, animada, guion en notas) | `python3 06-Proyecto-MCP/generar-presentacion-parq.py` |
| Guion maestro | [[Guion - Presentación Caso Parquímetros]] | a mano; de él salen notas y guiones individuales |
| Guiones individuales | `08-Tareas/guiones-caso-parquimetros/Guion - Santiago.md`, `- Jemima.md`, `- Byron.md` | los genera el script de la presentación |
| Láminas | `02-Diagramas/caso-parquimetros/` (contexto, core, descomposición, 2 CDU expandidos, bloques, despliegue) | `python3 06-Proyecto-MCP/generar-excalidraw.py caso-parquimetros/<carpeta>` |
| Prototipo | `08-Tareas/prototipo-parquimetros/index.html` (`?paso=1..4` muestra cada pantalla) | a mano |

## Verificación hecha

- PDF: `validar-entrega-pdf.py` sin fallas (ocupación mínima 69 %); páginas revisadas a ojo.
- Láminas: cada una mirada; se corrigieron cruces de líneas en la descomposición y un CU sin actor (CU-09).
- Presentación: Keynote la abre y la reproduce; 46 estados estables = 15 láminas + 31 clics.
- Citas de Guatemala verificadas contra las notas de prensa (La Hora, Soy502, Emisoras Unidas, Prensa Libre).

## Lo que falta (lo hace el grupo)

- Confirmar fecha de entrega y minutos de exposición; si son 10, el guion trae el recorte.
- Ensayar con el reloj del guion; cada integrante tiene su archivo.
- Revisar que la portada diga la fecha correcta («octubre de 2026»).

## Bitácora

- **2026-10-19.** Enunciado guardado y decodificado. Investigación de Guatemala. Siete láminas,
  prototipo, entrega (md, docx, pdf), presentación y guiones. A pedido suyo: vocabulario de
  estudiante, «franeleros» definido y reemplazado por «cuidacarros», tabla «Palabras que usamos».
  Hallazgo técnico: Keynote rechaza un .pptx con notas creadas desde la plantilla por defecto de
  python-pptx; se usa `06-Proyecto-MCP/plantillas/base-presentacion-16x9.pptx`.
