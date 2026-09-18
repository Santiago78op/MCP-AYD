# -*- coding: utf-8 -*-
"""Emite la Entrega de la Tarea 2 (FarmaHosp) como .docx.

Se corre desde boveda/06-Proyecto-MCP, igual que los otros generadores:

    python3 generar-entrega-docx.py

Lee las laminas de ../02-Diagramas/ y las convierte a PNG 2x con fondo blanco
(hace falta `rsvg-convert`, de librsvg: `brew install librsvg`). El .docx sale
en ../08-Tareas/.

Criterios de forma, decididos con el estudiante el 2026-09-18:
  · SIN caratula: solo un encabezado compacto con la identificacion.
  · SIN checklists de rigor ni comentarios sobre la rubrica: son aparato de
    trabajo. Lo que si queda son las DECLARACIONES que se califican (frontera,
    convencion de ids, taxonomia, supuestos), como notas.
  · Monocromo: las notas se distinguen por negrita, cuerpo menor y sangria,
    nunca por color ni recuadro.
  · Salto de pagina solo antes de las secciones de nivel 1.
"""
import os
import re
import shutil
import subprocess
import tempfile

from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.section import WD_SECTION, WD_ORIENT
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

AQUI = os.path.dirname(os.path.abspath(__file__))
DIAGRAMAS = os.path.join(AQUI, "..", "02-Diagramas")
OUT = os.path.join(AQUI, "..", "08-Tareas", "Entrega - Tarea 2 FarmaHosp.docx")

LAMINAS = {
    "contexto-farmahosp": "2-caso-negocio",
    "cdu-core-farmahosp": "2-caso-negocio",
    "cdu-descomposicion-farmahosp": "2-caso-negocio",
    "cdu-expandido-prescripcion": "3.1-drivers-rf",
    "bloques-farmahosp": "6-bloques-despliegue",
    "componentes-farmahosp": "6-bloques-despliegue",
    "despliegue-farmahosp": "6-bloques-despliegue",
}


def _preparar_imagenes():
    """SVG -> PNG 2x con fondo blanco explicito (estilo-diagramas.md 6)."""
    if shutil.which("rsvg-convert") is None:
        raise SystemExit("Falta rsvg-convert. Instalalo con: brew install librsvg")
    tmp = tempfile.mkdtemp(prefix="entrega-docx-")
    for nombre, carpeta in LAMINAS.items():
        svg = os.path.join(DIAGRAMAS, carpeta, nombre + ".svg")
        if not os.path.exists(svg):
            raise SystemExit("Falta la lamina %s — generala con generar-excalidraw.py" % svg)
        subprocess.run(["rsvg-convert", "-z", "2", "-b", "white", svg,
                        "-o", os.path.join(tmp, nombre + ".png")], check=True)
    return tmp


IMG = _preparar_imagenes()
CTX = os.path.join(IMG, "contexto-farmahosp.png")

AZUL = RGBColor(0x00, 0x00, 0x00)
GRIS = "EDEFF2"
AMAR = "FFF6E0"

doc = Document()

# ---------- estilos base ----------
st = doc.styles["Normal"]
st.font.name = "Calibri"
st.font.size = Pt(10.5)
st.paragraph_format.space_after = Pt(6)
st.paragraph_format.line_spacing = 1.15
rpr = st.element.get_or_add_rPr()
rf = rpr.find(qn('w:rFonts'))
if rf is None:
    rf = OxmlElement('w:rFonts'); rpr.append(rf)
rf.set(qn('w:eastAsia'), "Calibri")

for name, size, color, before, after in [
    ("Heading 1", 17, AZUL, 18, 8),
    ("Heading 2", 13.5, AZUL, 14, 6),
    ("Heading 3", 11.5, AZUL, 11, 4),
    ("Heading 4", 10.5, AZUL, 9, 3),
]:
    s = doc.styles[name]
    s.font.name = "Calibri"; s.font.size = Pt(size); s.font.color.rgb = color
    s.font.bold = True
    s.paragraph_format.space_before = Pt(before)
    s.paragraph_format.space_after = Pt(after)
    s.paragraph_format.keep_with_next = True

# ---------- página carta ----------
def carta(sec, landscape=False):
    if landscape:
        sec.orientation = WD_ORIENT.LANDSCAPE
        sec.page_width, sec.page_height = Inches(11), Inches(8.5)
        sec.left_margin = sec.right_margin = Inches(0.8)
        sec.top_margin = sec.bottom_margin = Inches(0.7)
    else:
        sec.orientation = WD_ORIENT.PORTRAIT
        sec.page_width, sec.page_height = Inches(8.5), Inches(11)
        sec.left_margin = sec.right_margin = Inches(1.0)
        sec.top_margin = sec.bottom_margin = Inches(1.0)

carta(doc.sections[0])

def pie(sec, texto="FarmaHosp — Tarea 2 · Santiago Barrera"):
    p = sec.footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(texto + "   ·   ")
    r.font.size = Pt(8); r.font.color.rgb = RGBColor(0x77, 0x77, 0x77)
    fld = OxmlElement('w:fldSimple'); fld.set(qn('w:instr'), 'PAGE')
    rr = OxmlElement('w:r'); rpr2 = OxmlElement('w:rPr')
    sz = OxmlElement('w:sz'); sz.set(qn('w:val'), '16'); rpr2.append(sz)
    rr.append(rpr2); t = OxmlElement('w:t'); t.text = "1"; rr.append(t); fld.append(rr)
    p._p.append(fld)

# ---------- helpers ----------
def runs(par, text, size=None, bold_all=False):
    """Parsea **negrita** y `codigo`."""
    text = text.replace("`", "")
    for i, chunk in enumerate(re.split(r"\*\*", text)):
        if not chunk:
            continue
        r = par.add_run(chunk)
        r.bold = bold_all or (i % 2 == 1)
        if size:
            r.font.size = Pt(size)
    return par

def H(text, level=1, brk=False):
    """brk usa page_break_before sobre el propio titulo.

    El parrafo vacio con salto que habia antes dejaba una linea en blanco
    colgando arriba de cada seccion.
    """
    p = doc.add_heading(level=level)
    p.text = ""
    runs(p, text, bold_all=True)
    for r in p.runs:
        r.font.color.rgb = AZUL
    if brk:
        p.paragraph_format.page_break_before = True
    return p

def P(text, size=10.5, align=None, space_after=6, italic=False):
    p = doc.add_paragraph()
    runs(p, text, size=size)
    if italic:
        for r in p.runs:
            r.italic = True
    if align:
        p.alignment = align
    p.paragraph_format.space_after = Pt(space_after)
    return p

def BUL(items, size=10):
    for it in items:
        p = doc.add_paragraph(style="List Bullet")
        runs(p, it, size=size)
        p.paragraph_format.space_after = Pt(2)

def shade(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr()
    sh = OxmlElement('w:shd')
    sh.set(qn('w:val'), 'clear'); sh.set(qn('w:color'), 'auto'); sh.set(qn('w:fill'), hexcolor)
    tcPr.append(sh)

def header_repeat(row):
    trPr = row._tr.get_or_add_trPr()
    th = OxmlElement('w:tblHeader'); th.set(qn('w:val'), "true")
    trPr.append(th)

def fijar_anchos(t, widths):
    """Word obedece el tblGrid, no solo el tcW: hay que escribir los dos."""
    for i, w in enumerate(widths):
        t.columns[i].width = w
    total = sum(int(w) for w in widths)
    tblPr = t._tbl.tblPr
    for old in tblPr.findall(qn('w:tblW')):
        tblPr.remove(old)
    tw = OxmlElement('w:tblW')
    tw.set(qn('w:type'), 'dxa')
    tw.set(qn('w:w'), str(int(total / 635)))   # EMU -> twips
    tblPr.append(tw)

def NOTE(text, fill=None, size=10, usable=6.5):
    """Nota monocroma: la entrada en negrita, el cuerpo a 9.5 y con sangria.

    Se distingue del cuerpo por el tamano y el desnivel, no por color ni por
    recuadro: la entrega va en blanco y negro.
    """
    lineas = [l for l in text.splitlines() if l.strip()]
    for i, line in enumerate(lineas):
        par = doc.add_paragraph()
        runs(par, line, size=10 if i == 0 else 9.5)
        if i == 0:
            for r in par.runs:
                r.bold = True
        par.paragraph_format.left_indent = Inches(0.3)
        par.paragraph_format.space_after = Pt(3 if i < len(lineas) - 1 else 10)
    return None

def TBL(headers, rows, fracs=None, size=8.5, usable=6.5, align_center_from=None):
    n = len(headers)
    if fracs is None:
        fracs = [1.0 / n] * n
    widths = [Inches(usable * f) for f in fracs]
    t = doc.add_table(rows=1, cols=n)
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    hdr = t.rows[0]
    header_repeat(hdr)
    for i, h in enumerate(headers):
        c = hdr.cells[i]
        p = c.paragraphs[0]
        runs(p, h, size=size, bold_all=True)
        p.paragraph_format.space_after = Pt(1)
        p.paragraph_format.keep_with_next = False
        shade(c, GRIS)
        c.width = widths[i]
    for row in rows:
        cells = t.add_row().cells
        for i, val in enumerate(row):
            c = cells[i]
            p = c.paragraphs[0]
            runs(p, str(val), size=size)
            p.paragraph_format.space_after = Pt(1)
            if align_center_from is not None and i >= align_center_from:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            c.width = widths[i]
    fijar_anchos(t, widths)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return t

def IMGP(path, width=6.5, caption=None):
    doc.add_picture(path, width=Inches(width))
    doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
    if caption:
        p = doc.add_paragraph()
        runs(p, caption, size=9)
        for r in p.runs:
            r.italic = True; r.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER

def CHK(title, items):
    """Las checklists de rigor son aparato de trabajo, no van en la entrega."""
    return None

def newsec(landscape=False):
    s = doc.add_section(WD_SECTION.NEW_PAGE)
    carta(s, landscape)
    return s

# =====================================================================
# ENCABEZADO COMPACTO (sin caratula: solo la identificacion que se pide)
# =====================================================================
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("Caso FarmaHosp \u2014 Tarea 2 (continuaci\u00f3n)")
r.bold = True; r.font.size = Pt(19); r.font.color.rgb = AZUL
for line in ["An\u00e1lisis y Dise\u00f1o de Sistemas II (785) \u00b7 ECYS, USAC \u00b7 MBA. MSc. Claudia Rojas de Mor\u00e1n",
             "Santiago Barrera \u00b7 Carn\u00e9: ____________________ \u00b7 18 de septiembre de 2026"]:
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(line); r.font.size = Pt(10)
    p.paragraph_format.space_after = Pt(2)
doc.add_paragraph().paragraph_format.space_after = Pt(6)

# =====================================================================
# ÍNDICE / CORRESPONDENCIA
# =====================================================================
H("Índice y correspondencia con la rúbrica", 2)
TBL(["#", "Criterio de la rúbrica", "Pts", "Sección"],
    [["1", "Caso de negocio: contexto, core y primera descomposición, con descripciones textuales", "20", "§2"],
     ["2", "Identificación de stakeholders", "10", "§1"],
     ["3", "Drivers RF, de calidad, de restricción y los 5 más críticos", "20", "§3"],
     ["4", "Matrices de trazabilidad", "10", "§4"],
     ["5", "Selección del estilo arquitectónico y su justificación", "10", "§5"],
     ["6", "Diagrama de bloques y diagrama de despliegue", "30", "§6"],
     ["", "**Total**", "**100**", ""]],
    fracs=[0.06, 0.64, 0.10, 0.20], size=10, align_center_from=2)


# =====================================================================
# §0 FRONTERA
# =====================================================================
H("0. Frontera del negocio (declaración de alcance)", 1, brk=True)
NOTE("**Esta declaración condiciona todo el resto del documento**\n"
     "**Entidad de interés (el negocio):** la **gestión del ciclo de vida del medicamento de alto costo (MAC)** "
     "del Hospital Universitario «Dr. Juan José Ortega».\n"
     "**Razón de ser:** garantizar que el MAC correcto llegue al paciente correcto, en condiciones de conservación "
     "válidas, con trazabilidad completa y auditable desde la compra hasta la farmacovigilancia.\n"
     "**Qué queda adentro:** las 6 etapas del ciclo de vida — adquisición, almacenamiento, prescripción, "
     "dispensación, administración, seguimiento y farmacovigilancia.\n"
     "**Qué queda afuera:** el resto de la operación hospitalaria (consulta externa, hospitalización, cirugía, "
     "laboratorio), que solo se relaciona con este negocio por sus interfaces.\n"
     "**Consecuencia sobre los actores:** el personal clínico y administrativo que **ejecuta** esas 6 etapas "
     "—médico tratante, farmacéutico clínico, enfermero de piso, almacenista, jefe de farmacovigilancia y director "
     "administrativo— son **trabajadores del negocio**, no actores, porque están dentro de la frontera. Son "
     "**actores del negocio** únicamente las entidades que interactúan con él desde afuera: paciente, proveedor de "
     "MAC, MSPAS, Contraloría General de Cuentas y sistema legacy de admisiones. **Son cinco**, y son exactamente "
     "los cinco del core (§2.2).\n"
     "Criterio aplicado: «cada actor modela algo fuera del negocio» — Jacobson, modelado de negocio.", fill="E8F0FA")

# =====================================================================
# §1 STAKEHOLDERS
# =====================================================================
H("1. Identificación de stakeholders · criterio 2 — 10 pts", 1, brk=True)
H("1.1 Cómo se identificaron", 2)
P("Se partió de los **8 stakeholders nombrados en el enunciado** y se completó con tres barridos: los cinco roles "
  "genéricos de clase, las categorías de metas de negocio de **PALM**, y los internos que no son usuarios "
  "(Garland & Anthony). De ahí salieron **5 stakeholders que el enunciado usa en sus escenarios pero no lista en su tabla**.")
TBL(["Agregado", "Barrido que lo encontró", "Requisito propio que ningún otro trae"],
    [["**Junta Directiva del hospital**", "cliente / crecimiento y continuidad",
      "Aprobó y financia el proyecto: plazo de 12 meses y evidencia de que las pérdidas se detuvieron"],
     ["**Contraloría General de Cuentas**", "responsabilidad hacia el estado (auditor)",
      "Informe forense de un lote y **registros inmutables**. El MSPAS pide reportar; la Contraloría pide **probar**"],
     ["**Consultora externa (desarrolladores)**", "organización de desarrollo",
      "Venía fusionada con el equipo interno en la tabla del enunciado, y el propio enunciado los enfrenta después: "
      "Python/PostgreSQL vs. Java/Oracle. **Dos intereses opuestos no pueden ser un mismo stakeholder**"],
     ["**Proveedor de MAC**", "etapa 1 del ciclo de vida",
      "La trazabilidad **arranca en él**: lote, vencimiento y factura entran al sistema desde su entrega"],
     ["**Operaciones de TI / data center**", "operaciones y gestión del sistema",
      "Techo fijo de 32 vCPU / 128 GB / SAN 10 TB **sin autoescalado**, y 500,000 registros de sensores diarios. "
      "Nadie más responde por eso"]],
    fracs=[0.22, 0.24, 0.54], size=9)

NOTE("**Criterio usado para incluir a alguien**\n"
     "Un stakeholder entra a la lista solo si se le puede nombrar **un concern propio** que ningún otro de la lista "
     "aporte. Roles como INCAP, RRHH o el personal de admisiones tienen exigencias reales, pero no aportan un concern "
     "distinto de uno ya listado (cumplimiento normativo, capacitación, confidencialidad): se tratan como "
     "**drivers de restricción** en el criterio 3, no como stakeholders separados.")

H("1.2 Tabla de stakeholders", 2)
P("Tipo de interés: **usa · paga · mantiene · opera · regula · construye** — cada tipo anticipa la clase de driver "
  "que ese stakeholder va a aportar en el criterio 3.")

STK = [
 ["STK-01", "Médico tratante (oncólogo)", "usa", "dentro — trabajador",
  "«Quiero prescribir rápidamente, en menos de 5 minutos, sin andar buscando papel.»",
  "Que el sistema le **sugiera** el MAC según protocolo, le **alerte** interacciones y contraindicaciones, "
  "**valide contra inventario en tiempo real** y —si no hay stock— le permita pedir compra urgente o reemplazo "
  "terapéutico desde la misma pantalla. Y que **recuerde su patrón de prescripción**.",
  "Usabilidad y eficiencia, sobre integridad de datos clínicos"],
 ["STK-02", "Farmacéutico/a clínico/a", "usa", "dentro — trabajador",
  "«Quiero un sistema que no se caiga, porque si no puedo dispensar, los pacientes no reciben su quimioterapia.»",
  "Operación **< 2 s** y que **funcione aunque falle la red** (la farmacia está en el sótano, con Wi-Fi inestable). "
  "Y un **inventario predictivo** que anticipe faltantes con 7 días de vista, según las prescripciones programadas.",
  "Disponibilidad (operación degradada) y performance"],
 ["STK-03", "Enfermero/a de piso", "usa", "dentro — trabajador",
  "«Quiero que el escáner funcione rápido y no se trabe.»",
  "Validación paciente-medicamento **< 1 s**; poder **administrar offline** si cae la conexión, con trazabilidad que "
  "se resuelve al reconectar **sin duplicar registros**; y registrar reacciones adversas por **voz a texto**.",
  "Performance y disponibilidad, con usabilidad bajo presión"],
 ["STK-04", "Director Administrativo", "paga · usa", "dentro — trabajador",
  "«Quiero ahorrar dinero y evitar pérdidas por caducidad.»",
  "**Tablero financiero**: costo por paciente, por servicio y % de desperdicio. Y **auditar quién autorizó cada "
  "compra y quién dio de baja un vencido**, de forma transparente para la Contraloría.",
  "Auditabilidad y observabilidad del negocio"],
 ["STK-05", "Jefe de Farmacovigilancia", "regula (interno) · usa", "dentro — trabajador",
  "«Quiero cumplir con la ley y reportar efectos adversos.»",
  "**Detección automática de patrones** de efectos adversos (ej. 5 pacientes del mismo lote con náuseas → alerta "
  "temprana) y que los reportes al sistema nacional se **generen automáticamente**, sin transcripción manual.",
  "Cumplimiento normativo e integrabilidad"],
 ["STK-06", "Paciente", "usa (indirecto)", "**fuera — actor**",
  "«Quiero que me den mi medicamento rápido y no me equivoquen.»",
  "**Trazabilidad verificable por él mismo** (escanear el QR y confirmar medicamento y dosis), **notificación de la "
  "próxima dosis** por SMS/WhatsApp en tratamiento ambulatorio, y **confidencialidad total** de su diagnóstico.",
  "Confidencialidad, y trazabilidad de cara al paciente"],
 ["STK-07", "Ministerio de Salud (MSPAS)", "regula", "**fuera — actor**",
  "«Queremos estandarizar la trazabilidad a nivel nacional.»",
  "Exportación en **HL7 FHIR** para interoperar con otros hospitales y **APIs seguras** para que el sistema nacional "
  "consulte efectos adversos en tiempo real. Reporte obligatorio **≤ 24 h** en XML con la DTD del MSPAS.",
  "Interoperabilidad y cumplimiento"],
 ["STK-08", "Equipo interno de TI del hospital (3 personas: Java 8, Spring Boot, Oracle PL/SQL, Angular)",
  "mantiene", "dentro — trabajador",
  "«Queremos usar tecnologías modernas y entregar rápido.»",
  "Que el stack sea **mantenible por 3 personas con su experiencia real** después de que la consultora se vaya; "
  "**evolución incremental**; y **documentación viva**, porque la rotación de personal es alta.",
  "**Mantenibilidad y modificabilidad**"],
 ["STK-09", "Consultora externa — 5 desarrolladores (Python/Django, React, MongoDB, Kafka)", "construye",
  "fuera — solo interés", "«Queremos usar tecnologías modernas y entregar rápido.»",
  "Un stack **negociado** que su equipo pueda construir y el interno pueda heredar, y **módulos con límites claros** "
  "para entregar por incrementos dentro de los 12 meses de contrato.",
  "Constructibilidad y velocidad de entrega"],
 ["STK-10", "Junta Directiva del hospital", "paga", "fuera — solo interés",
  "«Aprobamos la transformación digital: queremos resultados.»",
  "**Hitos visibles dentro de los 12 meses** y evidencia medible de que las pérdidas (Q. 2.5 M por caducidades) y los "
  "errores de medicación se detuvieron, sin exponer al hospital a sanciones legales.",
  "Costo, plazo y continuidad institucional"],
 ["STK-11", "Contraloría General de Cuentas", "regula (audita)", "**fuera — actor**",
  "«Exigimos trazabilidad completa desde la compra hasta la administración.»",
  "**Informe forense de un lote en < 10 minutos** —compra, proveedor, factura, temperaturas, pacientes, enfermero, "
  "médico, bajas y ajustes— sobre registros **inmutables que nadie pueda alterar, ni el administrador del sistema**.",
  "**Auditabilidad e inmutabilidad**"],
 ["STK-12", "Proveedor de MAC", "provee", "**fuera — actor**",
  "«Queremos recibir órdenes de compra y que se nos reciba el producto.»",
  "Que el número de lote, el vencimiento y la factura entren al sistema **exactos y sin transcripción manual** (los 3 "
  "errores por etiqueta mal transcrita nacen acá), y una vía para **notificar retiros de lote**.",
  "Integridad del dato de origen"],
 ["STK-13", "Operaciones de TI / data center (VMware, SAN, red)", "opera", "dentro — trabajador",
  "«Que el servidor no se caiga.»",
  "Que la solución **quepa en 32 vCPU / 128 GB / SAN 10 TB sin autoescalado**, absorba el **pico de 10x los lunes "
  "8:30 AM**, sobreviva a **500,000 registros de sensores/día** y priorice el tráfico de dispensación.",
  "**Escalabilidad con recursos fijos** y observabilidad"],
]
TBL(["ID", "Stakeholder", "Tipo", "Posición", "Lo que dice que quiere", "Necesidad oculta", "Concern dominante"],
    STK, fracs=[0.055, 0.155, 0.075, 0.09, 0.19, 0.29, 0.145], size=7.5)

NOTE("**Por qué STK-08 y STK-13 son stakeholders distintos**\n"
     "Son las mismas personas —el hospital tiene 3 en TI—, pero el criterio de identidad de un stakeholder es "
     "**el concern, no la persona**: como mantenimiento piden un stack que puedan heredar (Java/Oracle); como "
     "operaciones piden que la solución quepa en una capacidad fija. Son dos requisitos independientes y uno puede "
     "cumplirse sin el otro.")

H("1.3 Conflictos entre stakeholders", 2)
P("Cada tensión es un **tradeoff que la arquitectura tendrá que resolver**, no una falla del análisis.")
TBL(["Stakeholder A", "pide", "Stakeholder B", "pide", "Tensión", "Cómo se resuelve"],
    [["STK-08 Equipo interno de TI", "Java + Oracle: es lo que sabe mantener", "STK-09 Consultora externa",
      "Python + PostgreSQL + MongoDB: es lo que sabe construir",
      "**Constructibilidad vs. mantenibilidad**, agravada porque el hospital exige que el interno lo mantenga solo tras 12 meses",
      "Decide **quién se queda**: manda la mantenibilidad del equipo interno. La consultora aporta velocidad dentro de ese stack"],
     ["STK-06 Paciente", "Confidencialidad máxima: nadie no autorizado ve su diagnóstico", "STK-04 Director Administrativo",
      "Auditar todo lo que ocurre en el sistema", "**Confidencialidad vs. auditabilidad**",
      "El enunciado ya la resuelve: se audita **el acceso y la transacción**, no el diagnóstico. Ni el director lo ve sin orden judicial"],
     ["STK-03 Enfermero", "Poder administrar **offline** cuando cae la red", "STK-11 Contraloría",
      "Registro inmutable, sin duplicados ni huecos", "**Disponibilidad vs. consistencia e integridad**",
      "Escritura local con **resolución idempotente** al reconectar (acuerdo de calidad #2)"],
     ["STK-01 Médico", "Prescribir en < 5 min con validación en tiempo real", "STK-13 Operaciones de TI",
      "Presupuesto de infraestructura fijo, sin autoescalado", "**Performance vs. costo de infraestructura**",
      "Mitigación arquitectónica (caché, réplicas de lectura, colas) en vez de más hardware (acuerdo de calidad #5)"],
     ["STK-05 Jefe de Farmacovigilancia", "Reportar el efecto adverso **≤ 24 h** por ley", "STK-07 MSPAS",
      "Solo recibe de 8:00 a 16:00, batch diario, XML con DTD", "**Cumplimiento vs. disponibilidad del sistema externo**",
      "Desacople asincrónico: se persiste y se reintenta en ventana hábil. El plazo legal lo cumple el registro local"],
     ["STK-10 Junta Directiva", "Resultados visibles dentro de 12 meses", "STK-08 Equipo interno de TI",
      "Documentación viva y un stack que pueda heredar", "**Plazo vs. calidad interna**",
      "Entrega incremental por módulos: dispensación y almacén primero"]],
    fracs=[0.13, 0.17, 0.13, 0.17, 0.20, 0.20], size=8)

CHK("Checklist del criterio 2", [
    "La frontera está declarada antes de hablar de actores",
    "Cada stakeholder tiene ID (STK-nn)",
    "Cada uno tiene un concern propio que ningún otro aporta",
    "Se distingue «lo que dice que quiere» de «la necesidad oculta»",
    "Los conflictos están con su resolución, no solo enunciados",
    "Se declara quién quedó fuera y por qué (INCAP, RRHH, admisiones → drivers de restricción)",
])

# =====================================================================
# §2 CASO DE NEGOCIO
# =====================================================================
H("2. Caso de negocio · criterio 1 — 20 pts", 1, brk=True)
H("2.1 Diagrama de contexto", 2)
P("**El Producto (único óvalo):** Sistema Integral de Gestión de Medicamentos de Alto Costo — FarmaHosp")
NOTE("**Este diagrama es del sistema, no del negocio**\n"
     "Frente al **negocio** (§0), el médico, el farmacéutico y el enfermero son trabajadores. Frente al **software** "
     "son entidades externas: le entregan y reciben información, pero no viven dentro del producto. Es el mismo "
     "criterio del ejemplo de clase, donde el Bibliotecario figura como entidad externa aunque trabaje en la biblioteca.")
H("Entidades y agentes (rectángulos) con sus streamlines", 3)
TBL(["#", "Entidad o agente", "Origen", "Entra al sistema", "Sale del sistema"],
    [["1", "**Médico tratante**", "STK-01", "Prescripción médica · Solicitud de compra urgente o reemplazo terapéutico · Ajuste de dosis",
      "Alerta de interacción y contraindicación · Disponibilidad de inventario en tiempo real · Notificación de efecto adverso de su paciente"],
     ["2", "**Farmacéutico clínico**", "STK-02", "Confirmación de dispensación con lote asignado · Dictamen sobre lote afectado",
      "Cola de órdenes de dispensación · Etiqueta con código de barras/QR · Proyección de faltantes a 7 días · Alerta de ruptura de cadena de frío"],
     ["3", "**Enfermero de piso**", "STK-03", "Registro de administración (pulsera, código de lote, credencial biométrica) · Reporte de reacción adversa",
      "Validación paciente-medicamento · Alerta de discrepancia paciente/lote"],
     ["4", "**Director Administrativo**", "STK-04", "Autorización de orden de compra",
      "Tablero de costo por paciente y % de desperdicio · Reporte de pérdida estimada"],
     ["5", "**Jefe de Farmacovigilancia**", "STK-05", "Seguimiento farmacoterapéutico · Dictamen de causalidad",
      "Alerta temprana de patrón de efectos adversos por lote"],
     ["6", "**Paciente**", "STK-06", "Consulta de trazabilidad por QR", "Confirmación de medicamento y dosis · Recordatorio de próxima dosis"],
     ["7", "**Proveedor de MAC**", "STK-12", "Datos de lote, fecha de vencimiento y factura", "Orden de compra"],
     ["8", "**Contraloría General de Cuentas**", "STK-11", "Solicitud de auditoría de lote", "Informe forense de trazabilidad"],
     ["9", "**Operaciones de TI / data center**", "STK-13", "Parámetros de operación", "Métricas de capacidad y alertas de operación"],
     ["10", "**Sistema legacy de admisiones** (COBOL/SOAP, 7:00-17:00)", "sistema externo", "Datos demográficos del paciente", "Consulta de identificación de paciente"],
     ["11", "**Sistema nacional de farmacovigilancia** (MSPAS, XML/DTD, 8:00-16:00)", "sistema externo",
      "Alerta nacional de retiro de lote · Consulta de efectos adversos vía API", "Reporte de efecto adverso en formato XML/DTD"],
     ["12", "**Directorio activo / LDAP**", "sistema externo", "Credenciales validadas", "Solicitud de autenticación"],
     ["13", "**Sensores IoT de cámaras** (2-8 °C, -20 °C, ambiente)", "agente", "Lecturas de temperatura y humedad cada 5 minutos", "—"],
     ["14", "**Pasarela de SMS / WhatsApp**", "sistema externo", "Acuse de entrega del mensaje", "Mensaje de notificación (alerta de guardia, recordatorio de dosis, OTP)"]],
    fracs=[0.04, 0.22, 0.10, 0.32, 0.32], size=8)

NOTE("**Quién quedó fuera del contexto y por qué**\n"
     "STK-09 **Consultora externa** y STK-10 **Junta Directiva** son stakeholders con requisitos fuertes, pero "
     "**no intercambian información con el sistema en operación**. Confirma la regla: todo actor es stakeholder, "
     "pero no todo stakeholder es actor.")
IMGP(CTX, 6.4, "Diagrama de contexto — 14 entidades, 27 streamlines. Un óvalo (El Producto), rectángulos para "
                "entidades y agentes, y una flecha con nombre por sentido.")
P("**14 entidades · 27 streamlines.** Distribución por canasta: 4 usuarios directos, 4 del negocio "
  "(decide / insumo / audita), 6 dispositivos y sistemas externos.")
TBL(["Canasta", "Entidades"],
    [["**Usa**", "Médico tratante, Farmacéutico clínico, Enfermero de piso, Paciente"],
     ["**Decide y controla**", "Director Administrativo, Jefe de Farmacovigilancia"],
     ["**Insumo**", "Proveedor de MAC"],
     ["**Audita**", "Contraloría General de Cuentas"],
     ["**Agente**", "Sensores IoT de cámaras (cada 5 min)"],
     ["**Sistemas externos**", "Legacy de admisiones (COBOL/SOAP, 7-17 h), Directorio activo LDAP, Sistema nacional de farmacovigilancia (XML/DTD, 8-16 h), Pasarela SMS/WhatsApp"],
     ["**Opera**", "Operaciones de TI / data center"]],
    fracs=[0.25, 0.75], size=9)
CHK("Checklist del diagrama de contexto", [
    "Un solo óvalo, y nombra un sistema, no el hospital",
    "Todas las entidades en rectángulos",
    "Todas las flechas con nombre, en sustantivo y no en verbo",
    "Flujos bidireccionales como dos flechas separadas",
    "Ninguna entidad es parte del producto",
    "Los tres sistemas externos presentes (admisiones, farmacovigilancia nacional, LDAP) y los sensores IoT como agente",
])

H("2.2 Diagrama de CDU de alto nivel (core del negocio)", 2)
P("**La única elipse:** Gestión del Ciclo de Vida del Medicamento de Alto Costo (MAC) — el negocio completo, con el "
  "nombre de la frontera declarada en §0. El core **no lista procesos**: es el negocio visto como una sola cosa; "
  "abrirlo en procesos es trabajo de la primera descomposición (§2.3).")
H("Quién es actor y quién no — la decisión, defendida", 3)
TBL(["Actor del core", "Por qué está fuera del campo de acción"],
    [["**Paciente**", "Recibe el resultado de valor del negocio; no ejecuta ninguna etapa"],
     ["**Proveedor de MAC**", "Entrega los lotes desde afuera; con él arranca la trazabilidad"],
     ["**MSPAS**", "Regulador externo; recibe los reportes de farmacovigilancia (su sistema nacional es su canal)"],
     ["**Contraloría General de Cuentas**", "Auditor externo; exige el informe forense"],
     ["**Sistema legacy de admisiones**", "Sistema externo al ciclo del MAC; provee la identidad del paciente"]],
    fracs=[0.30, 0.70], size=9)
P("**Quién NO se dibuja, y por qué** (esto vale tantos puntos como el dibujo):")
TBL(["Excluido", "Razón"],
    [["Médico, farmacéutico, enfermero, director, jefe de farmacovigilancia",
      "**Trabajadores del negocio**: ejecutan las 6 etapas desde adentro de la frontera (§0). Van en las realizaciones, no como actores"],
     ["Sensores IoT", "Equipamiento **del proceso de almacenamiento**: herramienta interna del negocio, no un tercero que interactúe con él"],
     ["LDAP y pasarela SMS/WhatsApp", "Infraestructura **del software**, no del negocio: aparecen en el contexto (plano del sistema), no acá"],
     ["Junta Directiva y consultora externa", "Stakeholders que no interactúan con el negocio en operación"]],
    fracs=[0.33, 0.67], size=9)
NOTE("**El contraste con el diagrama de contexto (§2.1) es deliberado**\n"
     "En el contexto el enfermero y los sensores **sí** aparecen, porque el límite ahí es el software. Acá el límite "
     "es el negocio, y quienes lo ejecutan por dentro desaparecen del dibujo. Son dos planos distintos con dos "
     "fronteras distintas.")
IMGP(os.path.join(IMG, "cdu-core-farmahosp.png"), 6.0,
     "Core del negocio — una sola elipse, los cinco actores alrededor, notación de negocio (barras diagonales) y líneas sin punta.")
CHK("Checklist del core", [
    "Una sola elipse, y nombra el negocio completo",
    "Estereotipos de negocio en todos los elementos (diagonales + «actor de negocio» / «caso de uso de negocio»)",
    "CUN al centro, actores en círculo",
    "Líneas sin punta (comunicación en los dos sentidos, como los 4 cores de la cátedra)",
    "Ningún trabajador dibujado como actor; ningún actor suelto sin línea",
    "Consistente con la frontera de §0 y con la tabla de stakeholders de §1.2",
])

H("2.3 Primera descomposición — los procesos del negocio", 2)
P("La única elipse del core (§2.2) se abre en **los procesos que la realizan**: **un solo diagrama**, los CUN en "
  "columna al centro y **el mismo juego de actores del core** a los lados — el molde de la Tienda Electrónica y la "
  "Fábrica de Materiales.")
H("Los procesos, con su clasificación (criterio de la nota técnica)", 3)
P("Los seis primeros son **las 6 etapas del ciclo de vida que el enunciado fija textualmente** — por eso son seis y "
  "no los 3-5 del patrón observado en clase: el número lo dicta el enunciado, no el patrón. El séptimo cubre la "
  "categoría **gerencial** de la NT, que las etapas no traen y el enunciado exige a gritos (el tablero del Director, "
  "la auditoría de la Contraloría).")
TBL(["ID", "Proceso de negocio", "Categoría", "¿Por qué esa categoría?"],
    [["CDU-01", "Adquisición de MAC", "**soporte**", "No beneficia al paciente directamente: abastece al núcleo"],
     ["CDU-02", "Almacenamiento y conservación de MAC", "**soporte**", "Sostiene al núcleo (cadena de frío, inventario); el paciente no lo ve"],
     ["CDU-03", "Prescripción del tratamiento", "**núcleo**", "Servicio que el cliente (paciente) recibe del negocio"],
     ["CDU-04", "Dispensación del MAC", "**núcleo**", "Ídem: el lote se asigna nominalmente al paciente"],
     ["CDU-05", "Administración del MAC al paciente", "**núcleo**", "El acto de valor central del ciclo"],
     ["CDU-06", "Seguimiento y farmacovigilancia", "**núcleo**", "El paciente recibe el monitoreo posterior; cierra el ciclo"],
     ["CDU-07", "Control y auditoría de la gestión de MAC", "**gerencial**", "Manejo del negocio en su conjunto: transparencia ante la Contraloría y tablero del Director"]],
    fracs=[0.09, 0.30, 0.13, 0.48], size=9)
P("Nombres según la regla de la NT: **sustantivo derivado de verbo + complemento** (Adquisición de MAC → adquirir "
  "MAC ✓), la misma forma que Procesamiento de Pedidos y Gestión de Inventario en los ejemplos de clase.", size=9.5, italic=True)
H("Las asociaciones, una por una", 3)
TBL(["Proceso", "Actor(es)", "Razón"],
    [["CDU-01 Adquisición", "Proveedor de MAC", "De él entran lotes, vencimientos y facturas"],
     ["CDU-02 Almacenamiento", "**ninguno**",
      "Es la **excepción de CU de apoyo** de los convenios de clase: «es posible que un caso de uso de apoyo no "
      "interactúe con ningún actor». Ningún externo participa en conservar la cadena de frío; los sensores son "
      "equipamiento del proceso, no actores"],
     ["CDU-03 Prescripción", "Paciente · Sistema legacy de admisiones",
      "El paciente es examinado y recibe la prescripción; el legacy provee su identidad y datos demográficos"],
     ["CDU-04 Dispensación", "Paciente", "El lote se asigna a su nombre y él puede verificarlo por QR"],
     ["CDU-05 Administración", "Paciente", "Recibe el medicamento — el acto de valor"],
     ["CDU-06 Seguimiento", "Paciente · MSPAS", "El paciente reporta reacciones; al MSPAS va el reporte obligatorio de farmacovigilancia"],
     ["CDU-07 Control y auditoría", "Contraloría General de Cuentas", "Exige el informe forense y la trazabilidad completa"]],
    fracs=[0.22, 0.24, 0.54], size=9)
P("**Verificación de consistencia con el core** (la regla: pueden aparecer actores nuevos, no puede desaparecer "
  "ninguno): Paciente ✓ (4 procesos — el actor principal toca varios, como en el molde), Proveedor ✓, MSPAS ✓, "
  "Contraloría ✓, Legacy de admisiones ✓. **Los cinco del core están; no se agregó ninguno nuevo.**")
P("**Sin include ni extend**: la cátedra no los usa en la primera descomposición — aparecen recién en los CDU "
  "expandidos (§3.1), y solo con criterio explícito.")
IMGP(os.path.join(IMG, "cdu-descomposicion-farmahosp.png"), 5.4,
     "Primera descomposición — un solo diagrama, 7 procesos en columna, el mismo juego de actores del core.")
CHK("Checklist de la primera descomposición", [
    "Un solo diagrama, no uno por proceso",
    "Estereotipos de negocio en todos los elementos",
    "Nombres en sustantivo-de-verbo + complemento (la prueba: todos se convierten en verbo)",
    "Ningún proceso llamado crear / editar / eliminar / consultar",
    "Las 6 etapas del enunciado cubiertas, una por proceso; las 3 categorías de la NT presentes y justificadas",
    "El mismo juego de actores del core: ninguno desapareció",
    "El único CU sin actor (CDU-02) está amparado en la excepción de apoyo, declarada",
    "IDs CDU-nn asignados — son los que van a las matrices del criterio 4",
])

# =====================================================================
# §2.4 DESCRIPCIONES TEXTUALES
# =====================================================================
H("2.4 Descripciones textuales de los procesos de negocio", 2)
P("**Plantilla usada:** la de *Atender pedido* — la que coincide con la lista de campos que dictó la catedrática y la "
  "única que mostró resuelta: Nombre, Actores, Propósito, Resumen, **curso normal en dos columnas con una sola "
  "numeración intercalada**, Cursos alternos anclados con «En la línea N», Prioridad, Mejoras y Otras secciones.")
NOTE("**Plano de negocio: la columna derecha es «Respuesta del proceso de negocio»**\n"
     "Quienes actúan en la columna derecha son **trabajadores del negocio** (médico tratante, farmacéutico clínico, "
     "enfermero de piso, almacenista, jefe de farmacovigilancia, director administrativo): están **dentro** de la "
     "frontera declarada en §0. En la columna izquierda solo aparecen los **cinco actores** del core: PACIENTE, "
     "PROVEEDOR DE MAC, MSPAS, CONTRALORÍA GENERAL DE CUENTAS y SISTEMA LEGACY DE ADMISIONES.")

def cdu(idn, nombre, actores, proposito, resumen, curso, alternos, prioridad, mejoras, secciones=None):
    H("%s · %s" % (idn, nombre), 3)
    TBL(["Campo", "Contenido"],
        [["**Nombre**", nombre], ["**Actores**", actores], ["**Propósito**", proposito], ["**Resumen**", resumen]],
        fracs=[0.16, 0.84], size=9)
    TBL(["Acción del actor", "Respuesta del proceso de negocio"], curso, fracs=[0.42, 0.58], size=9)
    H("Cursos alternos", 4)
    BUL(alternos, size=9)
    P("**Prioridad:** %s" % prioridad, size=9.5)
    H("Mejoras", 4)
    BUL(mejoras, size=9)
    if secciones:
        for titulo, pasos in secciones:
            H("Sección: %s" % titulo, 4)
            for i, paso in enumerate(pasos, 1):
                p = doc.add_paragraph()
                runs(p, "%d. %s" % (i, paso), size=9)
                p.paragraph_format.left_indent = Inches(0.25)
                p.paragraph_format.space_after = Pt(1)

cdu("CDU-01", "Adquisición de MAC", "PROVEEDOR DE MAC",
    "Abastecer al hospital de medicamentos de alto costo con número de lote, fecha de vencimiento y factura exactos, "
    "verificando su calidad desde la recepción.",
    "El caso de uso se inicia cuando se detecta la necesidad de comprar un MAC (por la proyección de faltantes o por "
    "una solicitud urgente del médico). El proceso autoriza y emite la orden de compra, recibe los lotes y controla "
    "su calidad. El caso de uso finaliza cuando los lotes conformes quedan ingresados al almacén y el proveedor "
    "recibe la conformidad de la recepción.",
    [["", "**1.** El Farmacéutico clínico identifica la necesidad de compra a partir de la proyección de faltantes a 7 días."],
     ["", "**2.** El Director Administrativo autoriza la orden de compra; queda registrado quién la autorizó."],
     ["", "**3.** El Almacenista emite la orden de compra al Proveedor de MAC."],
     ["**4.** El Proveedor de MAC recibe la orden de compra y entrega los lotes con su factura.", ""],
     ["", "**5.** El Almacenista recibe los lotes y registra número de lote, fecha de vencimiento y factura, leyéndolos de la etiqueta del proveedor, sin transcripción manual."],
     ["", "**6.** El Farmacéutico clínico realiza el control de calidad de recepción (temperatura y humedad). *Si el lote es conforme, pasar a 7. Si no es conforme, ver curso alterno de la línea 6.*"],
     ["", "**7.** El Almacenista ubica cada lote en la cámara que le corresponde (2-8 °C, -20 °C o ambiente) y lo deja disponible para su conservación."],
     ["**8.** El Proveedor de MAC recibe la conformidad de la recepción.", ""]],
    ["**En la línea 1:** el Médico tratante solicita una **compra urgente o un reemplazo terapéutico** porque no hay stock para su prescripción. La orden se marca como urgente y se continúa en la línea 2.",
     "**En la línea 6:** el lote **no es conforme**. El Farmacéutico clínico lo rechaza registrando el motivo, el Almacenista lo devuelve y el Proveedor de MAC recibe la notificación de rechazo. Fin del caso de uso para ese lote."],
    "Alta.",
    ["Recibir del proveedor el lote, el vencimiento y la factura en formato electrónico: elimina la transcripción manual que originó los 3 errores de medicación del enunciado.",
     "Que el proveedor pueda notificar **retiros de lote** por la misma vía."])

cdu("CDU-02", "Almacenamiento y conservación de MAC",
    "*Ninguno* — caso de uso **de apoyo** (excepción de los convenios de clase; declarada en §2.3)",
    "Conservar cada lote en condiciones válidas y mantener un inventario confiable, rotado y auditable.",
    "El caso de uso se inicia cuando un lote ingresa a una cámara desde la Adquisición. El proceso vigila la "
    "temperatura y la humedad de la cámara, rota el inventario y anticipa faltantes. El caso de uso finaliza cuando "
    "el lote sale del almacén hacia la Dispensación o se da de baja por vencimiento o por ruptura de la cadena de frío.",
    [["*(sin actor: proceso de apoyo)*", "**1.** El Almacenista registra la ubicación del lote en su cámara."],
     ["", "**2.** Los sensores de la cámara registran temperatura y humedad cada 5 minutos, y el proceso conserva esas lecturas como evidencia inalterable. *Si la temperatura sale del rango, ver curso alterno de la línea 2.*"],
     ["", "**3.** El Farmacéutico clínico revisa la proyección de faltantes a 7 días según las prescripciones programadas. *Si se anticipa un faltante, se origina una Adquisición (CDU-01).*"],
     ["", "**4.** El Almacenista rota el inventario: despacha primero los lotes válidos más próximos a vencer."],
     ["", "**5.** El Almacenista da de baja los lotes vencidos; queda registrado quién dio de baja cada uno."],
     ["", "**6.** El lote queda disponible para la Dispensación (CDU-04)."]],
    ["**En la línea 2:** **ruptura de la cadena de frío** (escenario del enunciado: de 2 °C a 10 °C durante 15 minutos). El proceso registra el incidente con timestamp exacto, determina qué lotes estaban en la cámara, alerta al Farmacéutico de guardia por SMS y correo, bloquea esos lotes para la dispensación y entrega al Director Administrativo el reporte de pérdida estimada en quetzales."],
    "Alta.",
    ["Evidencia criptográfica de que las lecturas de temperatura no fueron manipuladas (acuerdo de calidad #8)."],
    [("Decidir sobre un lote fuera de temperatura",
      ["El Farmacéutico de guardia evalúa físicamente los lotes bloqueados.",
       "La política del hospital indica descartarlos.",
       "Si el fabricante soporta la exposición (por ejemplo, hasta 30 minutos), el Farmacéutico jefe puede sobrescribir la regla con justificación y firma; la decisión queda auditada.",
       "Los lotes se desbloquean o se dan de baja, según la decisión registrada."])])

cdu("CDU-03", "Prescripción del tratamiento", "PACIENTE · SISTEMA LEGACY DE ADMISIONES",
    "Indicar al paciente el MAC adecuado, validado contra protocolo, interacciones, contraindicaciones y disponibilidad real en el inventario del hospital.",
    "El caso de uso se inicia cuando el paciente es evaluado por el médico tratante. El proceso identifica al "
    "paciente, selecciona el medicamento y lo valida clínicamente y contra el inventario. El caso de uso finaliza "
    "cuando la prescripción validada queda enviada a la farmacia y el paciente recibe la indicación de su tratamiento.",
    [["**1.** El Paciente se presenta a su consulta o está hospitalizado y es evaluado.", ""],
     ["", "**2.** El Médico tratante solicita la identificación y los datos demográficos del paciente."],
     ["**3.** El Sistema legacy de admisiones provee la identidad y los datos demográficos del paciente.", ""],
     ["", "**4.** El Médico tratante selecciona el MAC (dosis, vía de administración y frecuencia) con la sugerencia según el protocolo y su patrón de prescripción."],
     ["", "**5.** La prescripción se valida contra protocolos clínicos, interacciones medicamentosas y contraindicaciones o alergias. *Si no hay alertas, pasar a 6. Si hay alertas, ver curso alterno de la línea 5.*"],
     ["", "**6.** Se verifica la disponibilidad del MAC en el inventario del hospital. *Si hay stock, pasar a 7. Si no hay, ver curso alterno de la línea 6.*"],
     ["", "**7.** El Médico tratante emite la prescripción, que queda enviada a la Dispensación (CDU-04)."],
     ["**8.** El Paciente recibe la indicación de su tratamiento.", ""]],
    ["**En la línea 3:** el sistema legacy **no está disponible** (fuera de 7:00-17:00 o lento). Se usa la identidad ya registrada del paciente y la verificación queda pendiente hasta que el legacy responda. Continúa en la línea 4.",
     "**En la línea 5:** hay alerta de protocolo, interacción o contraindicación. El Médico tratante ajusta la prescripción (volver a 4) o la mantiene con justificación registrada (pasar a 6).",
     "**En la línea 6:** **no hay stock**. El Médico tratante solicita, desde la misma prescripción, una compra urgente (origina CDU-01) o un reemplazo terapéutico (volver a 4)."],
    "Alta.",
    ["Que el proceso recuerde las preferencias de marca de cada médico, para prescribir en menos de 5 minutos."],
    [("Acceso de urgencia a diagnóstico sensible",
      ["El Médico de urgencias necesita ver un diagnóstico de confidencialidad máxima (VIH, cáncer) de un paciente que no es suyo.",
       "Registra la justificación de la emergencia.",
       "Accede al diagnóstico; el acceso queda registrado con quién, cuándo y por qué."])])

cdu("CDU-04", "Dispensación del MAC", "PACIENTE",
    "Asignar nominalmente al paciente un lote válido del inventario del hospital y entregarlo etiquetado para su administración.",
    "El caso de uso se inicia cuando llega a la farmacia una prescripción validada. El proceso verifica "
    "disponibilidad, asigna un lote específico, genera su etiqueta y registra la dispensación. El caso de uso "
    "finaliza cuando el lote etiquetado queda entregado para su administración y el paciente puede verificar por QR qué se le asignó.",
    [["", "**1.** El Farmacéutico clínico recibe la orden de dispensación. *Si no puede dispensar a tiempo en una urgencia, ver curso alterno de la línea 1.*"],
     ["", "**2.** El Farmacéutico clínico verifica la disponibilidad en el inventario del hospital (no en farmacia externa)."],
     ["", "**3.** El Farmacéutico clínico asigna un lote específico al paciente."],
     ["", "**4.** El Farmacéutico clínico genera la etiqueta con código de barras/QR del lote asignado."],
     ["", "**5.** Para oncológicos y opioides, el Farmacéutico clínico registra su parte del doble registro, que deberá coincidir con el del Enfermero de piso."],
     ["", "**6.** El Farmacéutico clínico entrega el medicamento etiquetado a enfermería."],
     ["**7.** El Paciente puede escanear el código QR y verificar que el medicamento y la dosis asignados son los correctos.", ""]],
    ["**En la línea 1:** urgencia con el farmacéutico ocupado (escenario del sábado 6:00 PM). Ver sección *Dispensación de urgencia*.",
     "**En la línea 2:** **la farmacia pierde la conexión** (Wi-Fi inestable del sótano). La dispensación continúa con el inventario local de la farmacia y se concilia automáticamente cuando la conexión regresa, sin duplicar registros. Continúa en la línea 3."],
    "Alta.",
    ["Proyección de faltantes visible en la misma pantalla de dispensación."],
    [("Dispensación de urgencia",
      ["**Opción A:** el Enfermero de piso toma el medicamento de la gaveta de *dispensación inmediata* y lo escanea; queda registrado quién lo tomó y por qué.",
       "**Opción B:** se autoriza el préstamo del medicamento de otro paciente que lo tiene prescrito para el día siguiente, y se genera la notificación para reponerlo antes de que ese paciente lo necesite.",
       "**Opción C:** se reserva el lote (dispensación virtual) sin retiro físico inmediato; el Farmacéutico clínico valida la entrega física dentro de las 12 horas siguientes."])])

cdu("CDU-05", "Administración del MAC al paciente", "PACIENTE",
    "Aplicar el medicamento correcto al paciente correcto, con registro completo y trazable del acto.",
    "El caso de uso se inicia cuando el enfermero va a aplicar una dosis dispensada. El proceso identifica al "
    "paciente, al medicamento y al enfermero, valida que coincidan y registra la aplicación. El caso de uso finaliza "
    "cuando el paciente recibió el medicamento y la administración quedó registrada.",
    [["", "**1.** El Enfermero de piso escanea la pulsera del paciente."],
     ["", "**2.** El Enfermero de piso escanea el código de barras del medicamento dispensado."],
     ["", "**3.** El Enfermero de piso se autentica con su credencial biométrica en la tablet."],
     ["", "**4.** Se valida que paciente y medicamento coinciden, en menos de 500 ms. *Si coinciden, pasar a 5. Si no, ver curso alterno de la línea 4.*"],
     ["", "**5.** Para oncológicos y opioides, el registro del Enfermero de piso se compara con el del Farmacéutico clínico. *Si la discrepancia supera los 5 minutos, se activa una alerta de seguridad.*"],
     ["", "**6.** El Enfermero de piso aplica el medicamento."],
     ["**7.** El Paciente recibe el medicamento.", ""],
     ["", "**8.** El Enfermero de piso registra hora, fecha, sitio de aplicación y reacciones adversas inmediatas, por dictado de voz si es necesario. *Si hay reacción adversa, se origina el Seguimiento (CDU-06).*"]],
    ["**En la línea 1 o 2:** **el escáner falla** (5 % de lecturas). El Enfermero de piso ingresa el código manualmente. Continúa en la línea siguiente.",
     "**En la línea 4:** paciente y medicamento **no coinciden** (escenario del metotrexato, cama 302 vs. 304). El proceso muestra la alerta de ALTO y el Enfermero de piso detiene la administración. Fin del caso de uso.",
     "**En la línea 6:** **no hay conexión**. La administración se registra offline y la trazabilidad se concilia automáticamente al volver la conexión, sin duplicar registros. Continúa en la línea 7."],
    "Alta.",
    ["Registro de reacciones adversas por voz a texto: escribir en la tablet con el paciente en shock es inviable."])

cdu("CDU-06", "Seguimiento y farmacovigilancia", "PACIENTE · MSPAS",
    "Vigilar la respuesta del paciente al tratamiento, ajustar la dosis y cumplir con el reporte obligatorio de efectos adversos.",
    "El caso de uso se inicia cuando se registra un efecto adverso o llega un control de seguimiento del paciente. "
    "El proceso notifica al médico, analiza el caso, cruza reportes del mismo lote y genera el reporte oficial. El "
    "caso de uso finaliza cuando el MSPAS recibe el reporte y el paciente tiene su tratamiento ajustado.",
    [["**1.** El Paciente presenta o reporta un efecto adverso en los días posteriores a la administración.", ""],
     ["", "**2.** El Enfermero de piso o el Médico tratante registra el efecto adverso."],
     ["", "**3.** El Médico tratante es notificado, evalúa al paciente y ajusta la dosis según la respuesta."],
     ["", "**4.** El Jefe de Farmacovigilancia analiza el caso y lo cruza con otros reportes del mismo lote. *Si detecta un patrón, ver curso alterno de la línea 4.*"],
     ["", "**5.** El Jefe de Farmacovigilancia genera el reporte en el formato XML con la DTD definida por el MSPAS, dentro de las 24 horas."],
     ["**6.** El MSPAS recibe el reporte en su sistema nacional de farmacovigilancia.", ""],
     ["**7.** El Paciente recibe el aviso de su próxima dosis por SMS o WhatsApp.", ""]],
    ["**En la línea 4:** **patrón de efectos adversos** (por ejemplo, 5 pacientes del mismo lote con náuseas) o **alerta nacional** del MSPAS. Se genera una alerta temprana y el lote se bloquea en el almacén (CDU-02).",
     "**En la línea 6:** el sistema nacional **no está recibiendo** (solo recibe de 8:00 a 16:00; el incidente fue a las 19:30). El reporte queda registrado con su fecha y hora, lo que cumple el plazo legal, y se entrega al abrirse la ventana. Continúa en la línea 7."],
    "Alta.",
    ["Exportación en HL7 FHIR para compartir con otros hospitales."])

cdu("CDU-07", "Control y auditoría de la gestión de MAC", "CONTRALORÍA GENERAL DE CUENTAS",
    "Dar transparencia financiera y trazabilidad forense completa de cada lote, sobre registros que nadie puede alterar.",
    "El caso de uso se inicia cuando la Contraloría General de Cuentas solicita, sin previo aviso, la trazabilidad de "
    "un lote. El proceso reúne el historial inmutable del lote desde la compra hasta la administración. El caso de "
    "uso finaliza cuando la Contraloría recibe el informe forense, en menos de 10 minutos.",
    [["**1.** La Contraloría General de Cuentas solicita la trazabilidad completa de un lote.", ""],
     ["", "**2.** El Director Administrativo solicita el informe forense del lote."],
     ["", "**3.** El proceso reúne del historial inmutable: fecha de compra, proveedor y factura; ingreso al almacén y temperaturas; pacientes a los que se administró; hora, fecha, enfermero y médico; devoluciones, caducidades y ajustes. *Si algún registro no pasa la verificación de integridad, ver curso alterno de la línea 3.*"],
     ["", "**4.** El Director Administrativo revisa y entrega el informe forense, en menos de 10 minutos."],
     ["**5.** La Contraloría General de Cuentas recibe el informe forense.", ""]],
    ["**En la línea 3:** un registro **no coincide** con su huella de integridad. El informe lo marca como evidencia de manipulación y se entrega igual, con la anomalía declarada."],
    "Alta.",
    ["Tablero de control del Director Administrativo: costo por paciente, por servicio y % de desperdicio, con quién autorizó cada compra y quién dio de baja cada lote vencido."])

# =====================================================================
# §3 DRIVERS
# =====================================================================
H("3. Drivers arquitectónicos · criterio 3 — 20 pts", 1, brk=True)
H("3.1 Drivers RF (CDU expandidos)", 2)
P("**Acá cambia el plano: del negocio al SISTEMA.** Los estereotipos de negocio desaparecen, el recuadro ahora es el "
  "software, y el personal clínico —que en los diagramas del negocio era trabajador— **reaparece como actor**, porque "
  "frente al software está afuera. Cada proceso de la primera descomposición (§2.3) se expande en los casos de uso "
  "del sistema que lo realizan, y **cada caso de uso expandido es un driver RF**. Lo que este entregable demuestra es "
  "**completitud**: que ningún requisito funcional del enunciado quede sin caso de uso.")
NOTE("**Convención de identificadores, declarada**\n"
     "El material de clase trae dos convenciones (CU_0n de la diapositiva; CU-0nn/RFG-0nn de la NT1). Este documento "
     "usa **una sola en todo el trabajo**: prefijo + guion medio + dos dígitos (STK-nn, CDU-nn, RF-nn, AC-nn, RE-nn), "
     "porque son los ids que anclan las matrices del criterio 4 y no se renumeran nunca.")
H("La tabla de drivers RF — completitud contra el enunciado", 3)
RF = [
 ["**CDU-01 Adquisición**", "", ""],
 ["RF-01", "Gestionar órdenes de compra", "etapa 1"],
 ["RF-02", "Registrar recepción de lotes (lote, vencimiento, factura)", "etapa 1; los 3 errores de transcripción"],
 ["RF-03", "Registrar control de calidad de recepción (temperatura, humedad)", "etapa 1"],
 ["RF-04", "Tramitar compra urgente o reemplazo terapéutico", "necesidad oculta del médico"],
 ["**CDU-02 Almacenamiento**", "", ""],
 ["RF-05", "Monitorear temperatura y humedad de cámaras (sensores cada 5 min)", "etapa 2"],
 ["RF-06", "Registrar incidente de cadena de frío y bloquear lotes afectados", "escenario 1"],
 ["RF-07", "Alertar al farmacéutico de guardia (SMS y correo)", "escenario 1"],
 ["RF-08", "Sobrescribir la regla de descarte con justificación y firma del farmacéutico jefe, auditada", "pregunta emergente del escenario 1"],
 ["RF-09", "Proyectar faltantes a 7 días según prescripciones programadas", "necesidad oculta del farmacéutico"],
 ["**CDU-03 Prescripción**", "", ""],
 ["RF-10", "Prescribir MAC (dosis, vía, frecuencia)", "etapa 3"],
 ["RF-11", "Validar contra protocolos clínicos «include»", "etapa 3"],
 ["RF-12", "Verificar interacciones medicamentosas «include»", "etapa 3"],
 ["RF-13", "Verificar contraindicaciones y alergias «include»", "etapa 3"],
 ["RF-14", "Consultar inventario en tiempo real «include»", "necesidad oculta del médico"],
 ["RF-15", "Sugerir MAC según protocolo y patrón de prescripción del médico", "necesidad oculta del médico"],
 ["RF-16", "Acceder a diagnóstico sensible con justificación auditada (médico de urgencias)", "acuerdo de calidad 4"],
 ["**CDU-04 Dispensación**", "", ""],
 ["RF-17", "Dispensar MAC (verificar orden, disponibilidad y asignar lote)", "etapa 4"],
 ["RF-18", "Generar etiqueta con código de barras/QR", "etapa 4"],
 ["RF-19", "Dispensación inmediata de urgencia con registro de quién y por qué (opción A)", "escenario 2"],
 ["RF-20", "Préstamo entre pacientes con notificación de reposición (opción B)", "escenario 2"],
 ["RF-21", "Dispensación virtual con validación física en 12 h (opción C)", "escenario 2"],
 ["RF-22", "Doble registro farmacéutico-enfermero con alerta si discrepancia > 5 min", "regulación INCAP"],
 ["**CDU-05 Administración**", "", ""],
 ["RF-23", "Administrar MAC (escaneo de pulsera, medicamento y credencial biométrica)", "etapa 5"],
 ["RF-24", "Validar paciente-medicamento con alerta de discrepancia", "escenario 3"],
 ["RF-25", "Ingresar código manualmente como respaldo del escáner", "entorno técnico (5 % de fallo)"],
 ["RF-26", "Operar offline y reconciliar al reconectar sin duplicar", "acuerdo de calidad 2"],
 ["RF-27", "Registrar reacción adversa inmediata con voz a texto", "necesidad oculta del enfermero"],
 ["**CDU-06 Seguimiento y farmacovigilancia**", "", ""],
 ["RF-28", "Registrar seguimiento farmacoterapéutico y ajuste de dosis", "etapa 6"],
 ["RF-29", "Generar y reenviar el reporte al sistema nacional (XML/DTD, ≤ 24 h, ventana 8-16 h)", "etapa 6 + escenario 6"],
 ["RF-30", "Detectar patrones de efectos adversos por lote y generar alerta temprana", "necesidad oculta del jefe de farmacovigilancia"],
 ["RF-31", "Notificar la próxima dosis al paciente (SMS/WhatsApp)", "necesidad oculta del paciente"],
 ["RF-32", "Verificar trazabilidad del medicamento por QR (paciente)", "necesidad oculta del paciente"],
 ["**CDU-07 Control y auditoría**", "", ""],
 ["RF-33", "Generar informe forense de lote en < 10 min sobre registros inmutables", "escenario 4"],
 ["RF-34", "Presentar tablero de costo por paciente, por servicio y % de desperdicio", "necesidad oculta del director"],
 ["RF-35", "Auditar autorizaciones de compra y bajas de inventario", "necesidad oculta del director"],
 ["RF-36", "Responder solicitudes de información pública con datos anonimizados", "Ley de Acceso a la Información"],
 ["RF-37", "Exportar datos en HL7 FHIR y exponer API para el sistema nacional", "necesidad del MSPAS"],
]
TBL(["ID", "Driver RF (caso de uso del sistema)", "Origen en el enunciado"], RF, fracs=[0.10, 0.58, 0.32], size=8.5)
P("**37 drivers RF**, cada uno trazable a su proceso (CDU-nn) y a su origen en el enunciado. Esa doble columna **es** "
  "la prueba de completitud que pide el criterio.")

H("Expandido de CDU-03 Prescripción — el diagrama profundo", 3)
P("El más rico del caso: junta las **dos justificaciones de include**, un extend condicionado y la "
  "**generalización de actores** del molde del Hospital de la cátedra.")
IMGP(os.path.join(IMG, "cdu-expandido-prescripcion.png"), 6.2,
     "CDU-03 expandido — plano del sistema: sin estereotipos de negocio, include punteado base→incluido, extend punteado extensión→base con su condición, y generalización de actores.")
TBL(["Relación", "Tipo", "Justificación (el criterio, no la sintaxis)"],
    [["Prescribir → Validar protocolo / interacciones / contraindicaciones", "include por **particionamiento**",
      "El enunciado exige las tres validaciones **siempre**: el base no funciona sin ellas. Partirlas hace legible el CU y son casos de apoyo sin actor (excepción de los convenios)"],
     ["Prescribir → Consultar inventario", "include por **reutilización**",
      "También lo necesita Dispensar (RF-17): comportamiento compartido entre dos CU"],
     ["Solicitar compra urgente → Prescribir", "extend con condición [sin stock]",
      "Prescribir **funciona perfectamente sin él**; solo se dispara en la excepción"],
     ["Médico tratante / de urgencias → Médico", "**generalización**",
      "El CU compartido (Prescribir) queda en el **padre**; cada hijo se queda con el suyo — el patrón exacto del Hospital de la cátedra"],
     ["Médico de urgencias — Acceder a diagnóstico", "asociación propia del hijo",
      "Solo urgencias tiene ese derecho (ABAC, acuerdo de calidad 4)"]],
    fracs=[0.30, 0.20, 0.50], size=8.5)
P("Nota de reutilización entre procesos: *Consultar inventario* lo incluyen **Prescribir y Dispensar**; *Doble "
  "registro INCAP* lo incluyen **Dispensar y Administrar** (la regulación exige que ambos extremos coincidan). Esa es "
  "la inclusión por reutilización operando **entre** expandidos, no solo adentro de uno.")
CHK("Checklist de los CDU expandidos", [
    "Plano del sistema: sin estereotipos de negocio; el recuadro es el software",
    "El personal clínico reaparece como actor (y está dicho por qué)",
    "Cada include y cada extend tiene su criterio escrito (reutilización / particionamiento / condición)",
    "Dirección correcta: include base→incluido; extend extensión→base con su condición",
    "Los CU sin actor son incluidos de apoyo (excepción de los convenios)",
    "Generalización con el padre arriba y el CU compartido en el padre",
    "37 drivers RF con ID, cada uno trazable a su CDU-nn y a su origen en el enunciado",
    "Los 6 escenarios críticos del enunciado aparecen en algún RF",
])

# ---- 3.2 calidad
H("3.2 Drivers de atributos de calidad", 2)
P("**Un atributo de calidad NO es un caso de uso, y un nombre de atributo NO es un driver.** Los 8 «acuerdos de "
  "calidad esperados» del enunciado —que él mismo ordena «clasificar bajo el nombre que corresponda y tratar como "
  "drivers arquitectónicos»— van acá como **escenarios de seis partes**: fuente, estímulo, artefacto, entorno, "
  "respuesta y **medida de respuesta**. La medida es la parte que convierte el deseo en driver: sin número no se "
  "puede diseñar ni verificar.")
NOTE("**Taxonomía usada, declarada**\n"
     "Se clasifica con **los seis atributos del programa** (ISO 9126): funcionalidad, fiabilidad, usabilidad, "
     "eficiencia, mantenibilidad, portabilidad. En esa taxonomía la **seguridad** y la **interoperabilidad** son "
     "subcaracterísticas de **funcionalidad** — en su sucesora ISO 25010 serían características de primer nivel. Los "
     "acuerdos 3, 4, 6 y 8 caen ahí, y se dice explícitamente en cada ficha. Cuando un escenario toca dos atributos, "
     "se declara **cuál domina**: un driver con dos categorías sin decidir no orienta ninguna decisión.")
TBL(["ID", "Acuerdo", "Atributo dominante", "Otros", "Stakeholder detrás"],
    [["AC-01", "Validación paciente-medicamento < 500 ms / < 2 s", "**eficiencia**", "fiabilidad", "STK-03 enfermero"],
     ["AC-02", "Operación offline ≥ 4 h con reconciliación", "**fiabilidad**", "funcionalidad", "STK-02 / STK-03"],
     ["AC-03", "Registros inmutables y trazables sin degradar", "**funcionalidad** (seguridad: no repudio)", "eficiencia", "STK-11 Contraloría"],
     ["AC-04", "Autorización contextual ABAC con excepción auditada", "**funcionalidad** (seguridad: confidencialidad)", "eficiencia", "STK-06 paciente"],
     ["AC-05", "Pico de 10x con presupuesto fijo", "**eficiencia**", "fiabilidad", "STK-13 operaciones"],
     ["AC-06", "Integración legacy SOAP + nacional XML/DTD", "**funcionalidad** (interoperabilidad)", "fiabilidad, eficiencia", "STK-07 MSPAS"],
     ["AC-07", "Mantenible por el equipo interno tras la consultora", "**mantenibilidad**", "—", "STK-08 equipo interno"],
     ["AC-08", "Temperaturas inalterables y verificables criptográficamente", "**funcionalidad** (seguridad: integridad)", "—", "STK-11 Contraloría"]],
    fracs=[0.08, 0.34, 0.26, 0.15, 0.17], size=8.5)

H("Las fichas — los 8 escenarios en seis partes", 3)
FICHAS = [
 ("AC-01 — Eficiencia (comportamiento temporal) · secundario: fiabilidad · acuerdo 1 + escenario crítico 3",
  [["Fuente", "El enfermero de piso, desde la Toughpad junto a la cama"],
   ["Estímulo", "Escanea la pulsera del paciente y el código del medicamento para validar"],
   ["Artefacto", "El módulo de administración (validación paciente-medicamento)"],
   ["Entorno", "Operación normal de red; y **condición degradada** (Wi-Fi inestable del piso)"],
   ["Respuesta", "Confirma la correspondencia o dispara la alerta roja de discrepancia"],
   ["**Medida**", "**< 500 ms** (p95) en red normal y **< 2 s** en degradada, con 15,000 pacientes y 800 SKUs en base — la alerta de 4 s del escenario 3 es el contraejemplo"]]),
 ("AC-02 — Fiabilidad (tolerancia a fallos y recuperabilidad) · secundario: funcionalidad · acuerdo 2 + escenario crítico 5",
  [["Fuente", "La caída del servidor central (o del enlace)"],
   ["Estímulo", "Los puestos de farmacia y las tablets pierden conectividad"],
   ["Artefacto", "Los módulos de dispensación y administración"],
   ["Entorno", "Hora pico — lunes 8:30, el peor momento posible"],
   ["Respuesta", "Siguen operando con registro local; al reconectar, la trazabilidad se reconcilia automáticamente"],
   ["**Medida**", "Operación offline **≥ 4 horas**; **100 %** de los registros reconciliados, **0 duplicados**"]]),
 ("AC-03 — Funcionalidad → seguridad: no repudio · secundario: eficiencia · acuerdo 3 + escenario crítico 4",
  [["Fuente", "Cualquier usuario — **incluido el administrador del sistema**"],
   ["Estímulo", "Intenta modificar o eliminar un registro histórico (inventario, prescripción, dispensación, administración)"],
   ["Artefacto", "El almacén de registros del sistema"],
   ["Entorno", "Operación normal"],
   ["Respuesta", "La modificación se rechaza; todo cambio entra como **evento nuevo** trazado a su usuario"],
   ["**Medida**", "**0** modificaciones históricas posibles; **100 %** de eventos con usuario; el rendimiento de operación no se degrada por el historial (escrituras dentro de AC-01)"]]),
 ("AC-04 — Funcionalidad → seguridad: confidencialidad · secundario: eficiencia · acuerdo 4 + política de datos del hospital",
  [["Fuente", "Un médico de urgencias que **no** es el tratante (y, en el caso negativo, personal de admisión)"],
   ["Estímulo", "Solicita el diagnóstico sensible (VIH, cáncer) de un paciente"],
   ["Artefacto", "El módulo de expedientes y su motor de autorización (ABAC)"],
   ["Entorno", "Emergencia, fuera del horario del tratante"],
   ["Respuesta", "A urgencias: concede **con justificación obligatoria** y registro en el log. A admisión: **niega siempre** — ni el director accede sin orden judicial"],
   ["**Medida**", "**100 %** de accesos de excepción con justificación registrada; **0** accesos de personal no autorizado; decisión de autorización **< 200 ms**"]]),
 ("AC-05 — Eficiencia (utilización de recursos bajo sobrecarga) · secundario: fiabilidad · acuerdo 5 + escenario crítico 5",
  [["Fuente", "Los usuarios concurrentes de todo el hospital"],
   ["Estímulo", "Un pico de **10× el tráfico normal**"],
   ["Artefacto", "El sistema completo, sobre el data center fijo (32 vCPU / 128 GB / SAN 10 TB, **sin autoescalado**)"],
   ["Entorno", "Lunes 8:30 — sobrecarga"],
   ["Respuesta", "Sigue atendiendo priorizando el tráfico crítico (dispensaciones); degrada lo no crítico"],
   ["**Medida**", "**0 colapsos**; las dispensaciones se mantienen dentro de la medida de AC-01; **sin hardware adicional** (mitigación arquitectónica: caché, colas, réplicas de lectura)"]]),
 ("AC-06 — Funcionalidad → interoperabilidad · secundarios: fiabilidad, eficiencia · acuerdo 6 + escenario crítico 6",
  [["Fuente", "El sistema legacy de admisiones (COBOL/SOAP, 3-5 s, 7:00-17:00) y el sistema nacional de farmacovigilancia (XML/DTD, 8:00-16:00)"],
   ["Estímulo", "El sistema necesita identidad del paciente; debe entregar un reporte de efecto adverso"],
   ["Artefacto", "Los adaptadores de integración"],
   ["Entorno", "El incidente ocurre **fuera de la ventana** del sistema externo (la anafilaxia de las 19:30)"],
   ["Respuesta", "Los datos de admisiones se **replican/cachean** para no bloquear la operación; los reportes se **encolan y reintentan** en ventana hábil — el plazo legal lo cumple el registro local"],
   ["**Medida**", "La respuesta al farmacéutico **no espera al legacy** (dentro de AC-01); **100 %** de reportes entregados **≤ 24 h**"]]),
 ("AC-07 — Mantenibilidad (cambiabilidad y analizabilidad) · acuerdo 7 + restricciones del equipo",
  [["Fuente", "El equipo interno de TI: 3 personas, Java 8 / Spring Boot / Oracle PL/SQL / Angular"],
   ["Estímulo", "Un cambio normativo del MSPAS o una corrección, **después de que la consultora se fue**"],
   ["Artefacto", "El código del sistema y su documentación viva"],
   ["Entorno", "Mantenimiento post-entrega, sin apoyo externo, con rotación de personal alta"],
   ["Respuesta", "El equipo implementa el cambio solo con su experiencia real y la documentación"],
   ["**Medida**", "El cambio afecta **un solo módulo** (cambiar farmacovigilancia sin tocar inventario); resuelto **sin intervención externa**; evolución incremental por módulos posible"]]),
 ("AC-08 — Funcionalidad → seguridad: integridad · acuerdo 8 + escenario crítico 1",
  [["Fuente", "Un auditor de la Contraloría (o el farmacéutico jefe que evalúa un lote)"],
   ["Estímulo", "Verifica que las lecturas de temperatura que justificaron descartar un lote **no fueron manipuladas**"],
   ["Artefacto", "El registro de lecturas de los sensores IoT"],
   ["Entorno", "Auditoría posterior al descarte (el informe forense del escenario 4)"],
   ["Respuesta", "El sistema **demuestra criptográficamente** la integridad de la serie (hash encadenado o firma de sensores)"],
   ["**Medida**", "**100 %** de las lecturas verificables; **cualquier** alteración posterior es detectable"]]),
]
for titulo, filas in FICHAS:
    H(titulo, 4)
    TBL(["Parte", "Contenido"], filas, fracs=[0.15, 0.85], size=8.5)
CHK("Checklist de los drivers de calidad", [
    "Ninguno dibujado como caso de uso",
    "Los 8 acuerdos del enunciado convertidos, cada uno con las 6 partes completas",
    "Toda medida es un número, no un adjetivo",
    "El entorno declara normal / degradado / sobrecarga — la parte que más se olvida",
    "Taxonomía declarada: los 6 atributos del programa; seguridad e interoperabilidad bajo funcionalidad (ISO 9126), con la nota de ISO 25010",
    "Cada escenario con atributo dominante decidido y stakeholder identificable detrás",
    "IDs AC-01…AC-08 — van a las matrices sin renumerarse",
])

# ---- 3.3 restricciones
H("3.3 Drivers de restricción", 2)
P("Una restricción es **una decisión de diseño que ya está tomada** y que el arquitecto no negocia. Se reconoce "
  "porque se escribe con «debe» o «no se puede», y porque **no tiene medida**: se cumple o no se cumple. Por eso "
  "**no se priorizan**: todas son obligatorias — la diferencia tajante con los atributos de calidad de §3.2.")
P("La columna **«qué decisión bloquea»** es la que convierte la cita en driver: una restricción sirve para "
  "**descartar alternativas**, y eso se hace visible.")
H("Las 8 explícitas del enunciado (textuales, sin parafrasear)", 3)
TBL(["ID", "Restricción (textual)", "Tipo", "Qué decisión bloquea"],
    [["RE-01", "«No se puede usar una base de datos que no soporte transacciones ACID para el módulo de inventario»", "técnica", "Descarta NoSQL sin ACID para inventario — el MongoDB de la consultora incluido"],
     ["RE-02", "«No se puede depender de la nube pública para el almacenamiento de datos sensibles… solo… análisis estadístico agregado (datos anonimizados)»", "técnica", "Descarta bases y SaaS en la nube para lo clínico; todo en el data center local"],
     ["RE-03", "«No se puede usar una tecnología que requiera licencias de pago anuales… (ej. Oracle Enterprise, SQL Server Enterprise). Se prefiere software open-source»", "negocio", "Descarta las bases comerciales — **incluida la Oracle que el equipo interno prefiere**"],
     ["RE-04", "«No se puede obligar a los enfermeros a usar dispositivos personales (BYOD)… el hospital provee los Toughpads»", "negocio", "El cliente de enfermería se diseña para las Toughpad, no para «cualquier teléfono»"],
     ["RE-05", "«No se puede diseñar un sistema monolítico, porque el módulo de farmacovigilancia tiene ciclos de entrega diferentes…»", "técnica", "Obliga módulos desplegables por separado; descarta el despliegue único"],
     ["RE-06", "«No se pueden almacenar contraseñas ni credenciales en texto plano en ninguna capa»", "técnica", "Descarta configuraciones y logs con secretos; obliga hashing y gestión de secretos"],
     ["RE-07", "«No se puede implementar una solución que requiera entrenamiento de más de 2 horas para los enfermeros»", "negocio", "Acota la complejidad de la interfaz de enfermería; descarta flujos que exijan curso"],
     ["RE-08", "«No se puede generar un único punto de falla en la autenticación; si… (LDAP) cae, el hospital debe seguir operando con… respaldo (ej. OTP por SMS)»", "técnica", "Descarta autenticar solo contra LDAP; obliga el mecanismo de respaldo"]],
    fracs=[0.08, 0.46, 0.10, 0.36], size=8.5)
H("Las implícitas — regulatorias, del entorno y organizativas", 3)
P("Repartidas por el enunciado fuera de la sección de restricciones; se barren por origen:")
TBL(["ID", "Restricción", "Origen", "Qué decisión bloquea / dónde se realiza"],
    [["RE-09", "Reporte de efectos adversos **≤ 24 h** en **XML con la DTD del MSPAS**", "regulatoria — Norma Técnica de Farmacovigilancia", "El formato y el plazo no se negocian; se realiza en RF-29 y AC-06"],
     ["RE-10", "**Doble registro** farmacéutico-enfermero para oncológicos y opioides; alerta si discrepancia **> 5 min**", "regulatoria — INCAP", "Obliga la coincidencia en tiempo real; se realiza en RF-22"],
     ["RE-11", "Responder solicitudes ciudadanas de datos estadísticos (no personales) en **10 días hábiles**", "regulatoria — Ley de Acceso a la Información Pública", "Obliga la vía de datos anonimizados; se realiza en RF-36"],
     ["RE-12", "Diagnósticos sensibles visibles **solo** para tratante, farmacéutico y enfermero asignado; el director **solo con orden judicial**", "regulatoria — Política de Datos del Hospital", "Fija el modelo de autorización; se realiza en AC-04 y RF-16"],
     ["RE-13", "Data center fijo: **32 vCPU / 128 GB / SAN 10 TB, sin autoescalado**", "técnica del entorno", "Descarta resolver el pico con hardware; obliga la mitigación arquitectónica de AC-05"],
     ["RE-14", "Tablets **Panasonic Toughpad, Android 9, 3 GB RAM** ya compradas", "técnica del entorno", "El cliente móvil debe correr ahí: descarta frameworks pesados y versiones de Android nuevas"],
     ["RE-15", "Escáneres Bluetooth con **5 % de fallo**: la entrada manual del código es obligatoria", "técnica del entorno", "Obliga el respaldo manual de RF-25; descarta flujos solo-escáner"],
     ["RE-16", "**Wi-Fi inestable** en el sótano de farmacia; internet de 50 Mbps compartido con priorización de tráfico crítico", "técnica del entorno", "Descarta diseños que asuman red confiable; empuja AC-01 degradado y AC-02"],
     ["RE-17", "El sistema debe poder ser **mantenido exclusivamente por el equipo interno** (3 personas) tras los 12 meses", "organizativa", "Acota el stack a lo que el interno pueda heredar; es el origen de AC-07"],
     ["RE-18", "**Entrega en 12 meses**, con evolución **incremental**: dispensación y almacén → prescripción → farmacovigilancia", "organizativa", "Fija el orden de construcción y refuerza RE-05 (módulos separados)"]],
    fracs=[0.07, 0.38, 0.22, 0.33], size=8.5)
NOTE("**La tensión que estas restricciones resuelven juntas**\n"
     "RE-03 (sin licencias: descarta Oracle Enterprise) **choca** con la preferencia del equipo interno (Oracle), y "
     "RE-17 exige que ese mismo equipo mantenga el sistema. Leídas juntas, acotan el stack por las dos puntas: "
     "**el lenguaje que el interno domina + una base open source con ACID** (RE-01). El conflicto de stacks de la "
     "tabla de §1.3 no se resuelve por gusto: lo resuelven las restricciones.")
NOTE("**Los stakeholders recortados en §1.1, saldados acá**\n"
     "INCAP reaparece como RE-10; el personal de admisiones como la cara negativa de RE-12; la capacitación limitada "
     "(RRHH) es RE-07. Ninguno se perdió: pagan sus puntos en este criterio, como se declaró al recortarlos.")
CHK("Checklist de las restricciones", [
    "Las 8 explícitas del enunciado, textuales (parafrasear es donde se pierde el requisito)",
    "Barridos los cuatro orígenes: explícitas, regulatorias, técnicas del entorno, organizativas",
    "Ninguna tiene prioridad: todas se cumplen",
    "Ninguna tiene medida: se cumplen o no (lo que tiene medida es un atributo de calidad)",
    "Cada una con su columna «qué decisión bloquea»",
    "Las que se realizan en un RF o AC llevan la referencia cruzada",
    "IDs RE-01…RE-18 — a las matrices sin renumerar",
])

# ---- 3.4 priorizacion
H("3.4 Los 5 drivers más críticos (contexto guatemalteco)", 2)
P("**El método (ADD): dos ejes, no una nota única.** La **importancia para el negocio** la asignan los stakeholders; "
  "la **dificultad o riesgo técnico**, el arquitecto. Cada driver recibe un par (importancia, dificultad) en "
  "alto/medio/bajo, y lo que se ataca primero es la intersección **(A, A)**: alto valor y alta dificultad, donde una "
  "decisión equivocada cuesta más deshacerla.")
P("**Qué se prioriza y qué no:** compiten los drivers de **atributos de calidad** (AC-nn) — las **restricciones no se "
  "priorizan** (todas se cumplen, §3.3) y la funcionalidad tiene su completitud en §3.1.")
NOTE("**«Según el contexto guatemalteco» — interpretación declarada**\n"
     "La rúbrica lo exige y **no lo define** en ningún material de clase. Se declara por tanto la "
     "interpretación aplicada: los **ejes del contexto nacional que el propio "
     "enunciado pone sobre la mesa** — marco regulatorio local (MSPAS, Contraloría, Ley de Acceso, INCAP), presupuesto "
     "público fijo sin autoescalado ni licencias renovables, infraestructura real (50 Mbps compartidos, Wi-Fi "
     "inestable), capital humano (3 personas de TI, alta rotación) y criticidad social (referencia nacional, 1,200 "
     "pacientes diarios).")
H("La matriz de los dos ejes — los 8 candidatos", 3)
TBL(["ID", "Driver", "Importancia (quién la sostiene)", "Dificultad (por qué)", "Par"],
    [["AC-01", "Validación < 500 ms / < 2 s", "**A** — STK-03: evita el error fatal del escenario 3", "**A** — el número con red degradada y equipo mixto", "**(A, A)**"],
     ["AC-02", "Offline ≥ 4 h con reconciliación", "**A** — STK-02/STK-03: sin esto la quimioterapia se detiene", "**A** — reconciliar sin duplicar es un problema de consistencia distribuida", "**(A, A)**"],
     ["AC-03", "Inmutabilidad y trazabilidad total", "**A** — STK-11: el proyecto nace de auditorías fallidas", "**M** — bitácora inmutable es patrón conocido; el reto es no degradar", "(A, M)"],
     ["AC-04", "Confidencialidad ABAC con excepción", "**A** — STK-06: ley + estigma de VIH/cáncer", "**M** — ABAC es patrón establecido", "(A, M)"],
     ["AC-05", "Pico de 10x con presupuesto fijo", "**A** — STK-13: el lunes 8:30 ya colapsó una vez", "**A** — sin autoescalado ni hardware nuevo: solo arquitectura", "**(A, A)**"],
     ["AC-06", "Interoperabilidad legacy + nacional", "**A** — STK-07: plazo legal de 24 h", "**M** — cola local con reintento en ventana es patrón estándar", "(A, M)"],
     ["AC-07", "Mantenibilidad por el equipo interno", "**A** — STK-08: sin esto el sistema muere a los 12 meses", "**M** — la decisión dura es temprana (stack, módulos)", "(A, M)"],
     ["AC-08", "Integridad criptográfica de sensores", "**M** — STK-11: parcialmente subsumido por AC-03", "**M** — hash encadenado es técnica conocida", "(M, M)"]],
    fracs=[0.07, 0.22, 0.30, 0.31, 0.10], size=8.5)
P("Tres quedan en **(A, A)** y cuatro en **(A, M)**: para los dos lugares restantes se desempata **con el contexto "
  "guatemalteco**, que es exactamente lo que la rúbrica pide.")
H("Los 5 seleccionados", 3)
TBL(["#", "ID", "Driver", "Justificación en el contexto guatemalteco"],
    [["1", "AC-02", "Operación offline ≥ 4 h con reconciliación", "**Conectividad**: el enunciado da Wi-Fi inestable en el sótano y 50 Mbps compartidos — en el contexto local la intermitencia no es un caso raro, es **el estado normal de la red**. Diseñar asumiendo conexión confiable haría el sistema inútil justo donde opera la farmacia"],
     ["2", "AC-01", "Validación paciente-medicamento < 500 ms / < 2 s", "**Dispositivos y red reales**: el número hay que lograrlo en Toughpads Android 9 de 3 GB (gama baja, ya compradas — RE-14) y sobre la red degradada. En otro contexto se resuelve con mejor hardware; acá el hardware es un dato, no una variable"],
     ["3", "AC-05", "Pico de 10x con presupuesto fijo", "**Presupuesto público**: no hay autoescalado, no hay nube para lo sensible (RE-02, RE-13) y el presupuesto de un hospital nacional no crece con la demanda. El pico se absorbe **con arquitectura o no se absorbe**"],
     ["4", "AC-07", "Mantenibilidad por el equipo interno", "**Capital humano**: 3 personas de TI, rotación alta por contratos de 12 meses, y sin dinero para consultoras permanentes ni licencias (RE-03, RE-17). En este contexto, un sistema que solo su constructor puede mantener es un sistema **muerto a mediano plazo** — y condiciona la decisión más temprana de todas: el stack"],
     ["5", "AC-03", "Inmutabilidad y trazabilidad total", "**Marco regulatorio local**: la Contraloría audita sin previo aviso y el proyecto **nace** de auditorías fallidas (Q 2.5 M perdidos, registros en papel). En la gestión pública guatemalteca la trazabilidad ante la Contraloría no es un plus: es la supervivencia institucional del proyecto"]],
    fracs=[0.04, 0.08, 0.24, 0.64], size=8.5)
P("**Por qué quedaron fuera los otros (A, M)** — el desempate, dicho: AC-04 (ABAC) y AC-06 (interoperabilidad) son de "
  "importancia alta pero su dificultad es media **porque se resuelven con patrones establecidos** que condicionan "
  "menos la estructura temprana que el stack (AC-07) o la inmutabilidad transversal (AC-03). Y AC-08 queda "
  "parcialmente cubierto por la decisión que se tome para AC-03. **Quedar fuera del top 5 no los vuelve opcionales**: "
  "siguen siendo drivers y entran a las matrices.")
CHK("Checklist de la priorización", [
    "Exactamente 5, como pide la rúbrica",
    "Cada uno con su par (importancia, dificultad) — no una nota única",
    "La importancia sostenida por un stakeholder identificado; la dificultad argumentada",
    "Las restricciones no compitieron — todas se cumplen",
    "La interpretación de «contexto guatemalteco» declarada y marcada como pregunta pendiente",
    "Cada justificación cita datos del enunciado, no generalidades",
    "El desempate entre pares iguales está explicado, y los no seleccionados no desaparecen",
])

# =====================================================================
# §4 MATRICES  (seccion apaisada)
# =====================================================================
newsec(landscape=True)
U = 9.4
H("4. Matrices de trazabilidad · criterio 4 — 10 pts", 1)
P("**No son diagramas: son tablas**, y su regla común es una sola — *una matriz solo sirve si se lee en los dos "
  "sentidos*. Las celdas marcadas son el inventario; **el hallazgo son los huecos**, y todo hueco queda comentado. "
  "Los ids son los mismos de las secciones anteriores, sin renumerar: STK-01..13, CDU-01..07, RF-01..37.")

H("4.1 Stakeholders vs. CDU", 2)
P("**Celda:** X = participa directamente en el proceso · i = tiene interés en su resultado sin participar.")
M1 = [
 ["STK-01 Médico tratante", "", "", "X", "i", "i", "X", ""],
 ["STK-02 Farmacéutico", "i", "X", "", "X", "i", "", ""],
 ["STK-03 Enfermero", "", "", "", "X", "X", "i", ""],
 ["STK-04 Director Admin.", "X", "i", "", "", "", "", "X"],
 ["STK-05 Jefe Farmacovig.", "", "", "", "", "i", "X", "i"],
 ["STK-06 Paciente", "", "", "X", "i", "X", "X", ""],
 ["STK-07 MSPAS", "", "", "", "", "", "X", "X"],
 ["STK-08 Equipo interno TI", "i", "i", "i", "i", "i", "i", "i"],
 ["STK-09 Consultora", "i", "i", "i", "i", "i", "i", "i"],
 ["STK-10 Junta Directiva", "i", "", "", "", "", "", "X"],
 ["STK-11 Contraloría", "i", "i", "", "", "", "", "X"],
 ["STK-12 Proveedor de MAC", "X", "i", "", "", "", "", ""],
 ["STK-13 Operaciones TI", "i", "i", "i", "i", "i", "i", "i"],
]
TBL(["", "CDU-01 Adquis.", "CDU-02 Almac.", "CDU-03 Prescr.", "CDU-04 Dispen.", "CDU-05 Admin.", "CDU-06 Seguim.", "CDU-07 Control"],
    M1, fracs=[0.23] + [0.11] * 7, size=9, usable=U, align_center_from=1)
P("**Lectura por columna** — *¿para quién es cada proceso?* **Ninguna columna vacía**: todo proceso tiene al menos un "
  "stakeholder con X. El más poblado es CDU-05 (administración), coherente con que sea el acto de valor central.")
P("**Lectura por fila** — *¿dónde aparece cada stakeholder?* **Ninguna fila vacía.** Tres filas son enteramente i "
  "(STK-08, STK-09, STK-13): **no es un hueco, es su naturaleza** — quien construye, mantiene y opera tiene interés "
  "transversal en todos los procesos sin participar en ninguno. Es la demostración en matriz de que *no todo "
  "stakeholder es actor*.")

H("4.2 Drivers RF vs. Drivers RF — dependencias", 2)
P("**Se lee: «la fila depende de la columna».** Es **asimétrica** y la **diagonal queda excluida** (NT1 de la "
  "cátedra). Con 37 RF la matriz completa es 37×37 y casi vacía, así que se presenta en dos vistas — decisión "
  "declarada: primero la **tabla de dependencias completa**, después la **matriz del tronco**.")
DEP = [
 ["RF-02 recepción de lotes", "RF-01", "no se recibe sin orden de compra"],
 ["RF-06 incidente y bloqueo", "RF-05", "sin monitoreo no hay incidente que registrar"],
 ["RF-07 alerta de guardia", "RF-06", "alerta lo que el incidente detectó"],
 ["RF-08 sobrescribir descarte", "RF-06", "se sobrescribe la decisión que el incidente disparó"],
 ["RF-09 proyección de faltantes", "RF-02, RF-10", "proyecta sobre inventario y prescripciones programadas"],
 ["RF-10 prescribir", "RF-11, RF-12, RF-13, RF-14", "los cuatro include obligatorios"],
 ["RF-14 consultar inventario", "RF-02", "consulta los lotes registrados"],
 ["RF-15 sugerir MAC", "RF-10, RF-11", "sugiere sobre protocolo e historial de prescripción"],
 ["RF-17 dispensar", "RF-10, RF-14, RF-02", "dispensa una prescripción, contra inventario real"],
 ["RF-18 etiqueta QR", "RF-17", "etiqueta el lote asignado"],
 ["RF-19/RF-20/RF-21 opciones A/B/C", "RF-17", "las tres extienden la dispensación"],
 ["RF-22 doble registro INCAP", "RF-17, RF-23", "exige coincidencia entre ambos extremos"],
 ["RF-23 administrar", "RF-17, RF-24", "administra lo dispensado, tras validar"],
 ["RF-24 validar paciente-medicamento", "RF-18", "valida contra la etiqueta generada"],
 ["RF-25 entrada manual", "RF-24", "es su respaldo"],
 ["RF-26 operar offline", "RF-17, RF-23", "continúa esas operaciones sin red"],
 ["RF-27 reacción por voz", "RF-23", "registra sobre una administración"],
 ["RF-28 seguimiento", "RF-23", "sigue lo administrado"],
 ["RF-29 reporte nacional", "RF-27, RF-28", "reporta lo registrado"],
 ["RF-30 patrones por lote", "RF-27, RF-02", "cruza reacciones contra lotes"],
 ["RF-31 notificar dosis", "RF-10", "notifica la frecuencia prescrita"],
 ["RF-32 trazabilidad QR", "RF-18, RF-23", "muestra la cadena etiqueta→administración"],
 ["RF-33 informe forense", "RF-02, RF-05, RF-17, RF-23", "recorre la cadena completa del lote"],
 ["RF-34 tablero financiero", "RF-02, RF-17", "agrega costos y desperdicio"],
 ["RF-35 auditar autorizaciones", "RF-01, RF-08", "audita compras y sobrescrituras"],
 ["RF-36 información pública", "RF-34", "publica los agregados anonimizados"],
 ["RF-37 HL7 / API nacional", "RF-28, RF-29", "expone lo que farmacovigilancia registra"],
]
TBL(["RF que depende", "Depende de", "Razón"], DEP, fracs=[0.28, 0.22, 0.50], size=8.5, usable=U)
P("**La matriz del tronco** (fila depende de columna; — = diagonal excluida):")
TR = [
 ["RF-01", "—", "", "", "", "", "", "", "", "", "", "", ""],
 ["RF-02", "X", "—", "", "", "", "", "", "", "", "", "", ""],
 ["RF-05", "", "", "—", "", "", "", "", "", "", "", "", ""],
 ["RF-10", "", "", "", "—", "X", "", "", "", "", "", "", ""],
 ["RF-14", "", "X", "", "", "—", "", "", "", "", "", "", ""],
 ["RF-17", "", "X", "", "X", "X", "—", "", "", "", "", "", ""],
 ["RF-18", "", "", "", "", "", "X", "—", "", "", "", "", ""],
 ["RF-23", "", "", "", "", "", "X", "", "—", "X", "", "", ""],
 ["RF-24", "", "", "", "", "", "", "X", "", "—", "", "", ""],
 ["RF-28", "", "", "", "", "", "", "", "X", "", "—", "", ""],
 ["RF-29", "", "", "", "", "", "", "", "", "", "X", "—", ""],
 ["RF-33", "", "X", "X", "", "", "X", "", "X", "", "", "", "—"],
]
TBL(["dep. ↓ / de →", "01", "02", "05", "10", "14", "17", "18", "23", "24", "28", "29", "33"],
    TR, fracs=[0.16] + [0.07] * 12, size=9, usable=U, align_center_from=1)
P("**Lectura por fila** — *¿qué necesito antes de construir esto?* Filas vacías (autónomos, candidatos a construirse "
  "primero): RF-01, RF-05, RF-11/12/13 (los catálogos de validación). Coincide con la restricción RE-18: "
  "**dispensación y almacén primero**.")
P("**Lectura por columna** — *¿si cambio esto, qué se rompe?* Las columnas más pobladas son RF-02 (4 dependientes), "
  "RF-17 (6) y RF-23 (5): **el registro de lotes, la dispensación y la administración son los RF críticos del "
  "sistema**. Hallazgo: la criticidad estructural coincide con el orden del ciclo de vida, lo que valida la "
  "descomposición. **Sin ciclos**: ningún par depende mutuamente.")

H("4.3 CDU vs. Drivers RF — cobertura", 2)
P("**Celda:** X = ese proceso cubre ese driver. Partida en dos por legibilidad (37 columnas):")
CV1 = [
 ["CDU-01", "X", "X", "X", "X", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
 ["CDU-02", "", "", "", "", "X", "X", "X", "X", "X", "", "", "", "", "", "", "", "", "", ""],
 ["CDU-03", "", "", "", "", "", "", "", "", "", "X", "X", "X", "X", "X", "X", "X", "", "", ""],
 ["CDU-04", "", "", "", "", "", "", "", "", "", "", "", "", "", "X", "", "", "X", "X", "X"],
 ["CDU-05", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
 ["CDU-06", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
 ["CDU-07", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
]
TBL([""] + ["%02d" % i for i in range(1, 20)], CV1, fracs=[0.10] + [0.0474] * 19, size=8, usable=U, align_center_from=1)
CV2 = [
 ["CDU-01", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
 ["CDU-02", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
 ["CDU-03", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
 ["CDU-04", "X", "X", "X", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
 ["CDU-05", "", "", "X", "X", "X", "X", "X", "X", "", "", "", "", "", "", "", "", "", ""],
 ["CDU-06", "", "", "", "", "", "", "", "", "X", "X", "X", "X", "X", "", "", "", "", ""],
 ["CDU-07", "", "", "", "", "", "", "", "", "", "", "", "", "", "X", "X", "X", "X", "X"],
]
TBL([""] + ["%02d" % i for i in range(20, 38)], CV2, fracs=[0.10] + [0.05] * 18, size=8, usable=U, align_center_from=1)
P("**Lectura por columna** — *¿todo RF tiene quién lo cubra?* **Ninguna columna vacía: los 37 RF están cubiertos.** "
  "Esa es la prueba de completitud del criterio 3, ahora demostrada en matriz.")
P("**Lectura por fila** — *¿todo proceso justifica su existencia?* **Ninguna fila vacía**, y el reparto es parejo "
  "(4-7 RF por proceso): ningún CDU está sobrecargado ni sobra.")
P("**El hallazgo fino**: RF-14 aparece en **dos filas** (CDU-03 y CDU-04) y RF-22 también (CDU-04 y CDU-05). No es "
  "un error de la matriz: **es la inclusión por reutilización de §3.1 hecha visible** — consultar inventario lo "
  "comparten prescribir y dispensar; el doble registro INCAP exige que dispensación y administración coincidan.")

H("4.4 La cadena completa — la prueba de las tres juntas", 2)
P("Las tres matrices se verifican encadenándolas. Un recorrido de ida:")
NOTE("**STK-11 Contraloría** → (matriz 1) participa en **CDU-07** → (matriz 3) que cubre **RF-33** informe forense → "
     "(matriz 2) que depende de **RF-02, RF-05, RF-17, RF-23** — la cadena completa del lote.", fill="E8F0FA", usable=U)
P("Y la vuelta — *¿si cambia RF-17 (dispensar), a qué stakeholders les afecta?*: por la matriz 2, caen RF-18, "
  "RF-19/20/21, RF-22, RF-23, RF-26, RF-33, RF-34; por la matriz 3 eso toca CDU-04, CDU-05 y CDU-07; por la matriz 1, "
  "los afectados son **farmacéutico, enfermero, paciente, director y Contraloría**. Ese recorrido es el análisis de "
  "impacto que la NT1 promete.")
CHK("Checklist del criterio 4", [
    "Los ids son los mismos de §1–§3, sin renumerar",
    "Cada matriz declara qué significa su celda",
    "Las tres leídas por fila y por columna, con los huecos comentados",
    "La de RF vs. RF es de dependencias, asimétrica, diagonal excluida, sin ciclos",
    "Ningún CDU sin stakeholder; ningún RF sin CDU que lo cubra",
    "Los «huecos» legítimos justificados (filas i transversales; RF compartidos por reutilización)",
    "La cadena STK → CDU → RF → RF recorrida en los dos sentidos",
])

# =====================================================================
# §5 ESTILO  (vuelve a vertical)
# =====================================================================
newsec(landscape=False)
H("5. Selección del estilo arquitectónico y su justificación · criterio 5 — 10 pts", 1)
H("5.1 La decisión, en una línea", 2)
NOTE("**Arquitectura orientada a servicios (SOA)** con **un servicio de negocio por proceso** (CDU-01 a CDU-07), "
     "**cada servicio organizado en capas**, comunicación de **llamada y retorno** para lo que exige respuesta "
     "inmediata y **basada en eventos** (bus) para lo asíncrono, clientes **cliente-servidor offline-first**, y un "
     "**pipeline de tuberías y filtros** para la telemetría de las cámaras.", fill="E8F0FA")
P("Un sistema real no es de un solo estilo: el estilo **principal** fija la estructura (SOA) y los "
  "**complementarios** resuelven drivers concretos donde el principal no alcanza. Taxonomía usada: la **lista de 9 "
  "estilos** y las **familias** de clase (árbol C&C).")

H("5.2 Por qué SOA — la definición de clase aplicada al caso", 2)
P("La lámina «Funcionamiento de la Arquitectura (SOA)» describe **cuatro escalones**, y FarmaHosp los cumple uno por uno:")
TBL(["Escalón de la clase", "Texto de la lámina", "En FarmaHosp", "Driver que lo exige"],
    [["1. Definición", "«Define las necesidades del negocio»", "Los 7 procesos del caso de negocio (CDU-01..07) y los 37 RF", "criterio 1 y 3"],
     ["2. Desarrollo", "«Desarrolla procesos de negocio como Servicios»", "**Un servicio por proceso**: Adquisición, Almacenamiento e Inventario, Prescripción, Dispensación, Administración, Farmacovigilancia, Auditoría y Tablero", "RE-05"],
     ["3. Evolución", "«Permite que cada Servicio evolucione independientemente»", "Farmacovigilancia tiene **otro ciclo de entregas** que inventario; se entrega por incrementos", "RE-05 · RE-18 · AC-07"],
     ["4. Distribución", "«Plantea aplicaciones distribuidas, multi-nivel»", "Clientes (Toughpad, farmacia, portal) → acceso → servicios → datos, repartidos en nodos", "AC-05 · AC-02"]],
    fracs=[0.14, 0.26, 0.42, 0.18], size=8.5)
P("Y la definición conceptual: «un servicio (cliente) realiza una solicitud (llamada) a otro servicio (proveedor) y "
  "espera una respuesta (retorno)». SOA además es **de dos familias**: «Es event-based porque puede usar motores de "
  "orquestación/coreografía e invocar servicios de forma asíncrona». Esa doble pertenencia es exactamente lo que "
  "FarmaHosp necesita: validar al paciente **ya** (síncrono) y reportar al MSPAS **cuando abra la ventana** (asíncrono).")

H("5.3 Los estilos complementarios — cada uno con su driver", 2)
TBL(["Estilo (familia de clase)", "Dónde se aplica", "Driver que resuelve", "Por qué este y no otro"],
    [["**En capas** (llamada y retorno)", "**Dentro de cada servicio**: capa de API (controlador REST), capa de lógica de negocio, capa de acceso a datos", "AC-07 mantenibilidad", "Es la estructura que el equipo interno ya conoce (Spring Boot); la clase: «Soporta fácilmente la evolución del sistema, los cambios sólo afectan a las capas vecinas»"],
     ["**Llamada y retorno** (REST síncrono)", "Validación paciente-medicamento, consulta de inventario, autenticación", "AC-01 < 500 ms · RF-14 · RF-24", "Hace falta la respuesta **antes** de seguir: «Interacción por invocación síncrona»"],
     ["**Basada en eventos** (bus de eventos)", "Reportes al MSPAS, notificaciones, sincronización offline, ruptura de cadena de frío, absorción del pico", "AC-05 pico 10x · AC-06 · RF-07 · RF-29", "El emisor **no espera**: la cola absorbe el pico y guarda lo que no puede entregarse (MSPAS solo recibe de 8 a 16)"],
     ["**Cliente-servidor offline-first**", "App de enfermería en la Toughpad y app de farmacia, con base local y bandeja de sincronización", "AC-02 offline ≥ 4 h · RE-16 · RF-26", "El cliente guarda y opera solo; al volver la red **reconcilia con identificador único** y el servidor descarta duplicados"],
     ["**Tuberías y filtros** (flujo de datos)", "Telemetría de cámaras: recibir → validar → sellar con hash encadenado → detectar ruptura → publicar evento", "AC-08 integridad · RF-05 · RF-06", "«Adecuada para sistemas con transformaciones de datos en pasos sucesivos»; cada filtro se cambia sin tocar los demás"]],
    fracs=[0.19, 0.26, 0.19, 0.36], size=8.5)

H("5.4 Los estilos descartados — tan importante como el elegido", 2)
TBL(["Estilo de la lista de clase", "¿Por qué no?", "Evidencia"],
    [["**Monolítico**", "**Prohibido**", "RE-05: «No se puede diseñar un sistema monolítico, porque el módulo de farmacovigilancia tiene ciclos de entrega diferentes…»"],
     ["**Microservicios**", "Demasiada granularidad para **3 personas** de TI y **32 vCPU sin autoescalado**: cada microservicio suma despliegue, monitoreo y base propia", "AC-07 · RE-13 · RE-17 · STK-08"],
     ["**Peer to peer**", "Sin un centro no hay **una sola verdad auditable** ni inventario con consistencia fuerte", "AC-03 · RE-01 (ACID en inventario)"],
     ["**Microkernel**", "No hay un núcleo estable con extensiones enchufables: hay siete procesos con el mismo peso", "—"],
     ["**Monolito en capas puro**", "Capas sin servicios sigue siendo un despliegue único", "RE-05"],
     ["**REST como estilo único**", "Se usa REST como **protocolo** de la llamada y retorno, pero no resuelve la asincronía", "AC-06 · RF-29"]],
    fracs=[0.22, 0.48, 0.30], size=8.5)

H("5.5 Cómo atiende la arquitectura a los 5 drivers más críticos", 2)
TBL(["#", "Driver (top 5 de §3.4)", "Táctica arquitectónica", "Dónde se ve en §6"],
    [["1", "AC-02 offline ≥ 4 h sin duplicar", "Base local cifrada en la Toughpad y en la farmacia + **bandeja de salida** con **identificador único generado en el cliente**; el Servicio de Sincronización reconcilia de forma **idempotente**", "Bloques: Sincronización offline. Despliegue: BD local en Toughpad y estación de farmacia"],
     ["2", "AC-01 validación < 500 ms / < 2 s", "La Toughpad descarga al inicio del turno las **administraciones programadas** de sus pacientes: la validación se hace **localmente**, sin viajar por la red; en línea se confirma contra la **caché**", "Despliegue: Validación local en Toughpad y Caché en el data center"],
     ["3", "AC-05 pico 10x con presupuesto fijo", "**Dos instancias** de cada servicio tras un **balanceador**, **caché** de lecturas, **bus** que absorbe las escrituras no críticas, **prioridad de tráfico** para dispensación y administración, y la **réplica del sitio alterno** para informes y tablero", "Bloques: Acceso y Bus. Despliegue: VM-03/04, VM-09"],
     ["4", "AC-07 mantenible por el equipo interno", "Stack que el interno ya domina: **Java + Spring Boot + Angular**; **PostgreSQL** en lugar de Oracle; la **misma plantilla de capas** en los 7 servicios; contratos **OpenAPI** como documentación viva", "§5.6"],
     ["5", "AC-03 inmutabilidad y trazabilidad total", "**Bitácora de eventos de solo inserción** (sin UPDATE ni DELETE, ni para el administrador) con **hash encadenado**; el informe forense se arma sobre la **réplica** para no degradar la operación", "Bloques: Bitácora inmutable. Despliegue: VM-10 y sitio alterno"]],
    fracs=[0.04, 0.18, 0.48, 0.30], size=8.5)
P("Los que no entraron al top 5 también se atienden: **AC-04** ABAC en el Servicio de Identidad y Acceso con caché de "
  "decisiones; **AC-06** adaptadores de integración con cola (guardar y reenviar) y copia nocturna de pacientes del "
  "legacy; **AC-08** filtro *Sellar* del pipeline de telemetría.")

H("5.6 Stack tecnológico — lo decide el conflicto STK-08 vs STK-09", 2)
TBL(["Pieza", "Elección", "Restricción o driver", "Descartado y por qué"],
    [["Lenguaje y framework de servicios", "**Java 17 + Spring Boot 3**", "RE-17 · AC-07", "Python/Django: el interno no lo puede mantener solo"],
     ["Base de datos", "**PostgreSQL 16** (primaria + réplica en sitio alterno)", "RE-01 ACID · RE-03 sin licencias", "Oracle Enterprise: RE-03 · MongoDB: sin ACID multi-documento para inventario (RE-01)"],
     ["Web", "**Angular**", "AC-07", "React: el interno no lo conoce"],
     ["App de enfermería", "**Android nativa** (Java/Kotlin) con **SQLite cifrado**", "RE-14 Android 9, 3 GB · RE-04 · RE-07", "Frameworks multiplataforma pesados: 3 GB de RAM"],
     ["Bus de eventos", "**RabbitMQ**", "AC-05 · AC-06 · RE-03", "Kafka: lo conoce la consultora, pero su operación es excesiva para 3 personas"],
     ["Caché", "**Redis**", "AC-01 · AC-05", "—"],
     ["Identidad", "**Keycloak** (federado con LDAP + OTP por SMS de respaldo)", "RE-08 · RE-06 · AC-04", "Autenticar solo contra LDAP: RE-08"],
     ["Balanceo y prioridad de tráfico", "**Nginx**", "AC-05 · 50 Mbps compartidos", "—"],
     ["Observabilidad", "**Prometheus + Grafana**", "STK-13", "—"]],
    fracs=[0.20, 0.26, 0.22, 0.32], size=8.5)
P("**Todo es open source** (RE-03) y **todo lo sensible reside en el data center local** (RE-02); a la nube pública "
  "solo sale el **análisis estadístico con datos anonimizados**.")
CHK("Checklist del criterio 5", [
    "La definición de estilo es textual de clase, con su fuente",
    "Cada estilo elegido cita el AC-nn o RE-nn que lo obliga",
    "Están los descartados con su evidencia",
    "Se atienden los 5 drivers del top 5 del criterio 3, y se dice qué pasa con los otros tres",
    "El stack sale de las restricciones, no del gusto",
])

# =====================================================================
# §6 BLOQUES Y DESPLIEGUE
# =====================================================================
H("6. Diagrama de bloques y de despliegue · criterio 6 — 30 pts", 1, brk=True)
P("Tres láminas, en el orden de la clase: **primero el alto nivel, después el detalle** — «Suele ser el primer paso "
  "antes de un diseño más detallado (ej. con diagramas de componentes)».")
TBL(["#", "Lámina", "Qué responde"],
    [["6.1", "**Diagrama de bloques**", "¿Cuáles son las partes grandes, cómo se conectan y qué fluye entre ellas?"],
     ["6.2", "**Diagrama de componentes**", "¿De qué piezas de software está hecho y qué interfaces ofrece cada una?"],
     ["6.3", "**Diagrama de despliegue**", "¿En qué hardware corre cada pieza y por qué red se hablan?"]],
    fracs=[0.08, 0.27, 0.65], size=9)

H("6.1 Diagrama de bloques de alto nivel", 2)
P("**Definición de clase aplicada:** «representación del funcionamiento de un sistema, que se hace mediante bloques y "
  "sus relaciones, y que, además, definen la organización de todo el proceso interno, sus entradas y sus salidas». "
  "Por eso la lámina se lee de **izquierda (entradas) a derecha (salidas)** y **todas las flechas llevan nombre** con "
  "lo que fluye.")
TBL(["Banda", "Bloque", "Responsabilidad", "Traza"],
    [["**Entradas**", "Enfermería (Toughpad + escáner Bluetooth)", "Administrar y validar offline", "RF-23..27 · RE-04 · RE-14 · RE-15"],
     ["", "Farmacia (estación offline, sótano)", "Dispensar aunque falle el Wi-Fi", "RF-17..22 · RE-16"],
     ["", "Portal clínico y administrativo", "Prescribir, farmacovigilancia, tablero", "RF-10..16 · RF-28..35"],
     ["", "Paciente (consulta QR)", "Verificar su medicamento", "RF-32"],
     ["", "Sensores IoT de cámaras (vía gateway)", "Lecturas cada 5 min", "RF-05"],
     ["**Acceso**", "Balanceador y API Gateway", "Reparte carga, prioriza dispensación y administración", "AC-05"],
     ["", "Identidad y acceso", "LDAP + OTP de respaldo, ABAC", "RE-08 · AC-04 · RE-12"],
     ["**Servicios de negocio (SOA)**", "Adquisición · Almacenamiento e Inventario · Prescripción · Dispensación · Administración · Farmacovigilancia · Auditoría y Tablero", "Un servicio por proceso CDU-01..07, cada uno en capas", "RE-05 · AC-07"],
     ["**Servicios de soporte**", "Sincronización offline", "Reconciliación idempotente", "AC-02 · RF-26"],
     ["", "Pipeline de telemetría (tuberías y filtros)", "Recibir → validar → sellar → detectar → publicar", "AC-08 · RF-05 · RF-06"],
     ["", "Integración", "Adaptadores legacy SOAP, MSPAS XML/DTD, HL7 FHIR", "AC-06 · RF-29 · RF-37"],
     ["", "Notificaciones", "SMS, WhatsApp, correo", "RF-07 · RF-31"],
     ["**Bus de eventos**", "—", "Desacopla y absorbe picos", "AC-05 · AC-06"],
     ["**Datos**", "Base transaccional PostgreSQL", "Inventario ACID", "RE-01"],
     ["", "Bitácora inmutable", "Solo inserción + hash encadenado", "AC-03 · AC-08"],
     ["", "Caché", "Lecturas rápidas", "AC-01 · AC-05"],
     ["", "Réplica en sitio alterno", "Respaldo y lecturas de informes", "escenario de caída · RF-33"],
     ["**Salidas (externos)**", "Legacy de admisiones · Sistema nacional MSPAS · LDAP · Pasarela SMS/WhatsApp · Nube (solo anonimizado)", "—", "AC-06 · RE-02 · RE-08"]],
    fracs=[0.17, 0.34, 0.28, 0.21], size=8)

newsec(landscape=True)
IMGP(os.path.join(IMG, "bloques-farmahosp.png"), 9.3,
     "§6.1 Diagrama de bloques de alto nivel — bandas por nivel, entradas a la izquierda, salidas a la derecha, toda flecha con lo que fluye y el driver entre paréntesis en cada bloque.")

newsec(landscape=False)
H("6.2 Diagrama de componentes", 2)
P("**Definición de clase aplicada:** un componente es «una unidad software que puede ser reemplazada y actualizada de "
  "forma independiente» y se define «en términos de los servicios que ofrecen (interfaces de salida) y los servicios "
  "que requieren». Notación de la clase: interfaz **provista = círculo**, dependencia **punteada** del que usa hacia "
  "la interfaz.")
TBL(["Componente", "Interfaz provista", "La usan", "Traza"],
    [["SvcAdquisicion", "IOrdenCompra", "SvcInventario (faltantes), SvcPrescripcion (compra urgente)", "RF-01..04"],
     ["SvcInventario", "IInventario", "SvcPrescripcion, SvcDispensacion", "RF-05..09 · RF-14 · RE-01"],
     ["SvcPrescripcion", "IPrescripcion", "SvcDispensacion", "RF-10..16"],
     ["SvcDispensacion", "IDispensacion", "SvcAdministracion (doble registro)", "RF-17..22"],
     ["SvcAdministracion", "IAdministracion", "AppEnfermeria", "RF-23..27"],
     ["SvcFarmacovigilancia", "IFarmacovigilancia", "SvcAdministracion (reacción adversa)", "RF-28..32"],
     ["SvcAuditoria", "IAuditoria", "PortalWeb", "RF-33..37"],
     ["SvcSincronizacion", "ISincronizacion", "AppEnfermeria, AppFarmacia", "AC-02 · RF-26"],
     ["SvcIdentidad", "IAutenticacion · IAutorizacion", "todos los clientes y servicios", "RE-08 · AC-04"],
     ["SvcIntegracion", "IAdmisiones · IReporteMSPAS", "SvcPrescripcion, SvcFarmacovigilancia", "AC-06 · RF-29 · RF-37"],
     ["SvcNotificacion", "INotificacion", "SvcInventario, SvcFarmacovigilancia", "RF-07 · RF-31"],
     ["PipelineTelemetria", "ILectura", "GatewayIoT", "RF-05 · AC-08"],
     ["BitacoraInmutable", "IRegistroEvento", "todos los servicios de negocio", "AC-03"]],
    fracs=[0.22, 0.24, 0.32, 0.22], size=8.5)
P("En la lámina, las cuatro interfaces transversales (SvcIntegracion, SvcNotificacion, SvcIdentidad y "
  "BitacoraInmutable) se dibujan como dependencias del **grupo** de servicios de negocio, para no repetir siete "
  "flechas iguales por cada una.")

newsec(landscape=True)
IMGP(os.path.join(IMG, "componentes-farmahosp.png"), 9.3,
     "§6.2 Diagrama de componentes — el nombre de la interfaz arriba del símbolo, la bola unida a su componente con línea llena, y el semicírculo del lado del consumidor abrazando la bola.")

newsec(landscape=False)
H("6.3 Diagrama de despliegue", 2)
P("**Definición de clase aplicada:** «Se utilizará para representar la arquitectura física sobre la que un sistema "
  "software es desplegado. Por tanto, describe tanto dispositivos hardware como software». Notación: **nodo = cubo**, "
  "«device» para hardware, «executionEnvironment» para software **siempre dentro de un dispositivo** — una **máquina "
  "virtual** es el ejemplo del propio PDF —, componentes dentro del nodo, **conexión = línea llena** con el protocolo "
  "como estereotipo, y las zonas **FrontEnd / BackEnd** marcadas.")
TBL(["Nodo", "Tipo", "Contiene", "Conexión", "Traza"],
    [["**Toughpad Panasonic** (Android 9, 3 GB, 32 GB)", "«device» → «executionEnvironment» Android 9", "App de Enfermería · Validación local · BD local cifrada (SQLite) · Bandeja de sincronización", "«wifi / HTTPS» al data center · «Bluetooth» al escáner", "RE-04 · RE-14 · AC-01 · AC-02"],
     ["**Escáner de código de barras**", "«device»", "— (entrada manual de respaldo en la app)", "«Bluetooth»", "RE-15 · RF-25"],
     ["**Estación de farmacia** (PC del sótano)", "«device» → «executionEnvironment» Navegador", "App de Farmacia offline · BD local (IndexedDB) · Bandeja de sincronización", "«wifi inestable / HTTPS» · «USB» a impresora", "RE-16 · AC-02"],
     ["**Impresora de etiquetas**", "«device»", "—", "«USB»", "RF-18"],
     ["**PC clínica y administrativa**", "«device» → «executionEnvironment» Navegador", "Portal web (Angular)", "«Ethernet 1 Gbps / HTTPS»", "RF-10..16 · RF-28..35"],
     ["**Smartphone del paciente**", "«device» → «executionEnvironment» Navegador", "Consulta QR", "«Internet / HTTPS»", "RF-32"],
     ["**Sensores IoT** (cada cámara)", "«device»", "—", "«MQTT» al gateway", "RF-05"],
     ["**Gateway IoT**", "«device»", "Buffer local (guardar y reenviar)", "«MQTT / TLS» al data center", "AC-08 · escenario de caída"],
     ["**Servidor de virtualización VMware** — data center principal (32 vCPU / 128 GB / SAN 10 TB)", "«device» con 11 «executionEnvironment» (VM-01 a VM-11)", "ver tabla de VMs", "—", "RE-13"],
     ["**Servidor de respaldo** — sitio alterno", "«device» → VM", "PostgreSQL réplica (lectura para informes y tablero) · Servicios en espera", "«replicación en streaming / TCP»", "escenario de caída · RF-33"],
     ["**Servidor legacy de admisiones**", "«device» externo", "COBOL con interfaz SOAP", "«SOAP / HTTPS»", "AC-06"],
     ["**Sistema nacional de farmacovigilancia** (MSPAS)", "«device» externo", "Recepción XML/DTD, 8:00-16:00", "«Internet / HTTPS»", "RE-09 · RF-29"],
     ["**Directorio activo (LDAP)**", "«device»", "—", "«LDAPS»", "RE-08"],
     ["**Pasarela SMS / WhatsApp**", "«device» externo", "—", "«Internet / HTTPS»", "RF-07 · RF-31"],
     ["**Nube pública**", "«device» externo", "Analítica estadística **anonimizada**", "«Internet / HTTPS»", "RE-02 · RF-36"]],
    fracs=[0.24, 0.20, 0.26, 0.16, 0.14], size=7.5)

H("Las máquinas virtuales del data center — la prueba de que cabe en el hardware fijo (RE-13)", 3)
TBL(["VM", "Qué corre", "vCPU", "RAM", "Por qué"],
    [["VM-01, VM-02", "Balanceador y API Gateway (Nginx)", "1 + 1", "2 + 2 GB", "AC-05 · sin punto único de falla"],
     ["VM-03, VM-04", "Servidor de aplicaciones (JRE 17): los **7 servicios de negocio + Sincronización**", "5 + 5", "14 + 14 GB", "AC-05: dos instancias de cada servicio"],
     ["VM-05, VM-06", "Identidad y acceso (Keycloak + ABAC)", "1 + 1", "4 + 4 GB", "RE-08: sin punto único de falla"],
     ["VM-07, VM-08", "Integración y eventos: RabbitMQ, Integración, Notificaciones, Pipeline de telemetría", "2 + 2", "8 + 8 GB", "AC-06 · AC-05"],
     ["VM-09", "Caché (Redis)", "1", "8 GB", "AC-01 · AC-05"],
     ["VM-10", "PostgreSQL primaria + Bitácora inmutable", "8", "48 GB", "RE-01 · AC-03"],
     ["VM-11", "Observabilidad (Prometheus + Grafana)", "1", "4 GB", "STK-13"],
     ["**Total**", "", "**28 de 32**", "**116 de 128 GB**", "queda margen para el hipervisor"]],
    fracs=[0.14, 0.44, 0.11, 0.13, 0.18], size=8.5, align_center_from=2)
NOTE("**Por qué la réplica de lectura NO está en el data center principal**\n"
     "La SAN tiene **10 TB** y el enunciado estima **5 TB de datos + 2 TB de logs + 100 GB de imágenes** el primer "
     "año: **7.1 TB**. Una réplica completa en la misma SAN sumaría otros 5 TB — **no cabe**. Por eso las lecturas "
     "pesadas (informe forense RF-33, tablero RF-34) van contra la **réplica del sitio alterno**, que el enunciado ya "
     "da por existente. El pico del lunes no depende de esa réplica: lo absorben la caché, el bus y las dos instancias.")
NOTE("**Supuestos declarados (el enunciado no los da)**\n"
     "• Existe un enlace de red entre el data center principal y el sitio alterno.\n"
     "• Los PCs de la farmacia, del personal clínico y administrativo, y la impresora de etiquetas ya existen.\n"
     "• El gateway IoT es parte del equipamiento de las cámaras con sensores.")

newsec(landscape=True)
IMGP(os.path.join(IMG, "despliegue-farmahosp.png"), 9.3,
     "§6.3 Diagrama de despliegue — nodos como cubos, «device» y «executionEnvironment», componentes dentro del nodo, toda conexión con su protocolo como estereotipo y las zonas FrontEnd / BackEnd.")

newsec(landscape=False)
H("6.4 Cómo se comporta en los escenarios críticos del enunciado", 2)
P("La prueba de que la arquitectura **no es decorativa**: cada escenario, recorrido sobre los nodos.")
TBL(["Escenario del enunciado", "Qué pasa en la arquitectura"],
    [["**La cadena de frío se rompe** (3:00 AM)", "Sensores → Gateway IoT → Pipeline de telemetría: *sellar* guarda la lectura con hash, *detectar* ve la ruptura y *publica* el evento → Inventario bloquea los lotes, Notificaciones envía SMS y correo, Auditoría calcula la pérdida"],
     ["**Urgencia oncológica** (sábado 6:00 PM)", "Dispensación ofrece las opciones A/B/C; cada una se registra en la Bitácora inmutable con quién y por qué"],
     ["**Error de medicación** (cama 302/304)", "La validación ocurre **en la Toughpad** contra las administraciones programadas del turno: < 500 ms sin depender de la red"],
     ["**Auditoría de la Contraloría**", "Auditoría consulta la Bitácora inmutable sobre la réplica del sitio alterno: informe < 10 min sin frenar la operación"],
     ["**Caída del servidor central** (lunes 8:30)", "Toughpads y farmacia **siguen operando offline**; el gateway guarda las lecturas; al volver, Sincronización concilia sin duplicar. El balanceador reparte entre VM-03 y VM-04"],
     ["**Farmacovigilancia** (19:30, MSPAS cerrado)", "El reporte se registra con fecha y hora y queda en la cola del bus; Integración lo entrega a las 8:00"]],
    fracs=[0.30, 0.70], size=9)
CHK("Checklist del criterio 6", [
    "Diagrama de bloques: entradas a la izquierda, salidas a la derecha, todas las flechas con nombre",
    "Componentes: interfaz provista como círculo, dependencias punteadas del que usa hacia la interfaz",
    "Despliegue: cubos, «device» / «executionEnvironment» dentro de un dispositivo, componentes adentro del nodo",
    "Toda conexión con protocolo como estereotipo",
    "FrontEnd y BackEnd marcados, y los sistemas externos aparte",
    "Cada nodo y cada componente trazan a un RF, AC o RE",
    "Las cuentas de hardware cierran: 28/32 vCPU, 116/128 GB, 7.1/10 TB",
    "Los tres diagramas y las tablas usan los mismos nombres",
])

# pie de pagina y guardado
for s in doc.sections:
    try:
        s.footer.is_linked_to_previous = False
    except Exception:
        pass
    pie(s)

doc.save(OUT)
print("OK ->", OUT)
