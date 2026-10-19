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
| Documento que se sube | `08-Tareas/Grupo2_CasoParquimetros.pdf` (44 páginas: carátula del molde de Redes, índice paginado, texto vertical y figuras anchas en horizontal) y `.docx` | `python3 06-Proyecto-MCP/generar-entrega-parq.py` (el índice se calcula en dos pasadas) |
| Presentación | `08-Tareas/Grupo2_CasoParquimetros_Presentacion.pptx` (Arial, animada, guion en notas) | `python3 06-Proyecto-MCP/generar-presentacion-parq.py` |
| Guion maestro | [[Guion - Presentación Caso Parquímetros]] | a mano; de él salen notas y guiones individuales |
| Guiones individuales | `08-Tareas/guiones-caso-parquimetros/Guion - Santiago.md`, `- Jemima.md`, `- Byron.md` | los genera el script de la presentación |
| Láminas | `02-Diagramas/caso-parquimetros/` (contexto, core, descomposición, 2 CDU expandidos, bloques, despliegue) | `python3 06-Proyecto-MCP/generar-excalidraw.py caso-parquimetros/<carpeta>` |
| Prototipo | `08-Tareas/prototipo-parquimetros/index.html` (`?paso=1..4` muestra cada pantalla) | a mano |
| Repositorio público del grupo | github.com/Santiago78op/Dise-o-Arquitectonico-los-Parqu-metros (`main`, `develop`, `v1.0.0`) con documento, presentación, diagramas y el **sitio** (`sitio/index.html` + `prototipo.html`) | se copian las salidas de acá; el sitio vive solo allá |

## Qué se sube a UEDI

| Archivo | Para qué |
|---|---|
| `Grupo2_CasoParquimetros.pdf` (43 páginas) | El documento: es lo que se califica |
| `Grupo2_CasoParquimetros_Presentacion.pdf` (15 páginas) | La presentación, si la plataforma pide PDF |
| `Grupo2_CasoParquimetros_Presentacion.pptx` | Para exponer: tiene las animaciones; **sin notas del orador** |

Él movió las copias de entrega a `~/Documents/02-Diagramas/G2-Parquimetros/`; acá quedan las mismas.
El sitio se levanta en local con `python3 -m http.server 8000` en la raíz del repo del grupo
(`http://127.0.0.1:8000/sitio/`); GitHub Pages **no** está activado.

## Verificación hecha

- PDF: `validar-entrega-pdf.py` sin fallas (ocupación mínima 69 %); páginas revisadas a ojo.
- Láminas: cada una mirada; se corrigieron cruces de líneas en la descomposición y un CU sin actor (CU-09).
- Presentación: Keynote la abre y la reproduce; 46 estados estables = 15 láminas + 31 clics.
- Citas de Guatemala verificadas contra las notas de prensa (La Hora, Soy502, Emisoras Unidas, Prensa Libre).

## Lo que falta (lo hace el grupo)

- **Exposición confirmada: lunes 19/10/2026, turno 1, de 17:20 a 18:00** (anuncio de la clase). El
  turno es de 40 minutos; la exposición sigue armada para 15 y el resto queda para preguntas. La
  carátula ya dice 19/10/2026: no hay que regenerar.
- Ensayar con el reloj del guion; cada integrante tiene su archivo.
- Revisar que la portada diga la fecha correcta («octubre de 2026»).

## Bitácora

- **2026-10-19 (noche).** Guion reescrito para el público: cada diapositiva dice qué se ve, qué
  aparece en cada clic, la idea clave y una nota «Por qué lo menciono» con el origen de cada
  referencia (México, Antigua, San Francisco, ISO 9126, PDH); glosario y respuestas listas. Los
  encabezados usan el antetítulo real de la pantalla y el generador aborta si no coinciden. Fotos del
  parquímetro del caso en las diapositivas 2 y 4; PDF de la presentación rehecho desde Keynote.
  Habla medida: unos 14 min de 15. Repo del grupo en `v1.0.3`.

- **2026-10-19 (cierre).** A pedido suyo: fuera del documento GitFlow y las frases que hablaban del
  propio texto («este documento propone», «cómo se leyó la consigna», la tabla de la consigna); el
  .pptx sin notas del orador. Presentación exportada a PDF. Repo del grupo en `v1.0.2`.

- **2026-10-19 (tarde).** Repo del grupo creado con GitFlow (tres `feature/*`, `release/1.0.0`,
  etiqueta `v1.0.0`). Documento: carátula como la de Redes (escudo de Ingeniería, título dorado),
  índice con páginas reales, resumen ejecutivo, equipo, conclusiones y recomendaciones; texto en
  vertical. Presentación: títulos aserción (Alley), barra de avance con Morph (Keynote lo
  reproduce como Movimiento mágico, medido), barrido en flujos; 46 estados verificados. Sitio
  desde la plantilla 39 del segundo cerebro: axe 0 violaciones de 320 a 1440 px.

- **2026-10-19.** Enunciado guardado y decodificado. Investigación de Guatemala. Siete láminas,
  prototipo, entrega (md, docx, pdf), presentación y guiones. A pedido suyo: vocabulario de
  estudiante, «franeleros» definido y reemplazado por «cuidacarros», tabla «Palabras que usamos».
  Hallazgo técnico: Keynote rechaza un .pptx con notas creadas desde la plantilla por defecto de
  python-pptx; se usa `06-Proyecto-MCP/plantillas/base-presentacion-16x9.pptx`.
