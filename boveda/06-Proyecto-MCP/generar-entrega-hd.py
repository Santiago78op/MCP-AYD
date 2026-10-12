# -*- coding: utf-8 -*-
"""Emite la Entrega del Caso Harley-Davidson (proyecto SiL'K).

    python3 generar-entrega-hd.py

Una sola fuente de contenido, tres salidas:
  · ../08-Tareas/Entrega - Caso Harley-Davidson.md    (el artefacto vivo de la boveda)
  · ../08-Tareas/Entrega - Caso Harley-Davidson.docx  (editable)
  · ../08-Tareas/GrupoN_CasoHD.pdf                    (lo que se sube; hace falta `soffice`)

Las matrices NO se escriben a mano: salen de las tablas STK_RF, RF_CU y DEP_RF
de este archivo, y la matriz Stakeholders x Casos de Uso se DERIVA de las otras
dos. El script aborta si queda un requisito sin stakeholder, un caso de uso sin
requisito o un stakeholder sin ningun driver.

Forma: los parametros del paso 6 de `_Metodo para resolver una tarea`
(sin caratula, monocromo, notas por negrita y sangria, salto solo en nivel 1).
"""
import os
import re
import shutil
import subprocess
import tempfile

from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_SECTION, WD_ORIENT
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

AQUI = os.path.dirname(os.path.abspath(__file__))
DIAGRAMAS = os.path.join(AQUI, "..", "02-Diagramas")
TAREAS = os.path.join(AQUI, "..", "08-Tareas")
BASE = "Entrega - Caso Harley-Davidson"
PDF = "GrupoN_CasoHD.pdf"

LAMINAS = {
    "contexto-hd": "caso-hd/1-caso-negocio",
    "cdu-core-hd": "caso-hd/1-caso-negocio",
    "cdu-descomposicion-hd": "caso-hd/1-caso-negocio",
    "cdu-expandido-hd-01-requisicion": "caso-hd/3-drivers-rf",
    "cdu-expandido-hd-02-recepcion": "caso-hd/3-drivers-rf",
    "cdu-expandido-hd-03-suministradores": "caso-hd/3-drivers-rf",
    "cdu-expandido-hd-04-proyectos": "caso-hd/3-drivers-rf",
    "bloques-hd": "caso-hd/5-estilo-despliegue",
    "despliegue-hd": "caso-hd/5-estilo-despliegue",
}


def _preparar_imagenes():
    """SVG -> PNG 2x con fondo blanco explicito (estilo-diagramas.md 6)."""
    if shutil.which("rsvg-convert") is None:
        raise SystemExit("Falta rsvg-convert. Instalalo con: brew install librsvg")
    tmp = tempfile.mkdtemp(prefix="entrega-hd-")
    for nombre, carpeta in LAMINAS.items():
        svg = os.path.join(DIAGRAMAS, carpeta, nombre + ".svg")
        if not os.path.exists(svg):
            raise SystemExit("Falta la lamina %s — generala con generar-excalidraw.py" % svg)
        subprocess.run(["rsvg-convert", "-z", "2", "-b", "white", svg,
                        "-o", os.path.join(tmp, nombre + ".png")], check=True)
    return tmp


IMG = _preparar_imagenes()
NEGRO = RGBColor(0, 0, 0)
GRIS = "EDEFF2"
doc = Document()
MD = []          # la misma entrega, en markdown para la boveda

st = doc.styles["Normal"]
st.font.name = "Calibri"
st.font.size = Pt(10.5)
st.paragraph_format.space_after = Pt(6)
st.paragraph_format.line_spacing = 1.15
for name, size, before, after in [("Heading 1", 17, 18, 8), ("Heading 2", 13.5, 14, 6),
                                  ("Heading 3", 11.5, 11, 4), ("Heading 4", 10.5, 9, 3)]:
    s = doc.styles[name]
    s.font.name = "Calibri"; s.font.size = Pt(size); s.font.color.rgb = NEGRO; s.font.bold = True
    s.paragraph_format.space_before = Pt(before)
    s.paragraph_format.space_after = Pt(after)
    s.paragraph_format.keep_with_next = True


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


carta(doc.sections[0], True)


def pie(sec, texto="Caso Harley-Davidson — proyecto SiL'K · Santiago Barrera"):
    if sec is None:
        return
    p = sec.footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(texto + "   ·   ")
    r.font.size = Pt(8); r.font.color.rgb = RGBColor(0x77, 0x77, 0x77)
    fld = OxmlElement('w:fldSimple'); fld.set(qn('w:instr'), 'PAGE')
    rr = OxmlElement('w:r'); t = OxmlElement('w:t'); t.text = "1"; rr.append(t); fld.append(rr)
    p._p.append(fld)


pie(doc.sections[0])


def runs(par, text, size=None, bold_all=False):
    text = text.replace("`", "")
    for i, chunk in enumerate(re.split(r"\*\*", text)):
        if not chunk:
            continue
        # *cursiva* de markdown: se respeta en el .docx en vez de dejar el asterisco
        for j, trozo in enumerate(chunk.split("*")):
            if not trozo:
                continue
            r = par.add_run(trozo)
            r.bold = bold_all or (i % 2 == 1)
            r.italic = (j % 2 == 1)
            if size:
                r.font.size = Pt(size)
        continue
        r = par.add_run(chunk)
        r.bold = bold_all or (i % 2 == 1)
        if size:
            r.font.size = Pt(size)
    return par


def H(text, level=1, brk=False):
    p = doc.add_heading(level=level)
    p.text = ""
    runs(p, text, bold_all=True)
    for r in p.runs:
        r.font.color.rgb = NEGRO
    if brk:
        p.paragraph_format.page_break_before = True
    MD.append("\n%s %s\n" % ("#" * (level + 1), text))


def P(text, size=10.5):
    p = doc.add_paragraph()
    runs(p, text, size=size)
    MD.append(text + "\n")


def BUL(items, size=10):
    for it in items:
        p = doc.add_paragraph(style="List Bullet")
        runs(p, it, size=size)
        p.paragraph_format.space_after = Pt(2)
        MD.append("- " + it)
    MD.append("")


def NOTE(text):
    """Nota monocroma: entrada en negrita, cuerpo a 9.5 y con sangria."""
    lineas = [l for l in text.splitlines() if l.strip()]
    for i, line in enumerate(lineas):
        par = doc.add_paragraph()
        runs(par, line, size=10 if i == 0 else 9.5)
        if i == 0:
            for r in par.runs:
                r.bold = True
        par.paragraph_format.left_indent = Inches(0.3)
        par.paragraph_format.space_after = Pt(3 if i < len(lineas) - 1 else 10)
        MD.append("> " + line + ("" if i else "") )
        MD.append(">")
    MD[-1] = ""


def _shade(cell):
    tcPr = cell._tc.get_or_add_tcPr()
    sh = OxmlElement('w:shd')
    sh.set(qn('w:val'), 'clear'); sh.set(qn('w:color'), 'auto'); sh.set(qn('w:fill'), GRIS)
    tcPr.append(sh)


def TBL(headers, rows, fracs=None, size=9, usable=9.4, centro_desde=None):
    usable = 9.4
    size = max(size, 8)
    n = len(headers)
    if fracs is None:
        fracs = [1.0 / n] * n
    widths = [Inches(usable * f) for f in fracs]
    t = doc.add_table(rows=1, cols=n)
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    hdr = t.rows[0]
    trPr = hdr._tr.get_or_add_trPr()
    th = OxmlElement('w:tblHeader'); th.set(qn('w:val'), "true"); trPr.append(th)
    for i, h in enumerate(headers):
        c = hdr.cells[i]
        p = c.paragraphs[0]
        runs(p, h, size=size, bold_all=True)
        p.paragraph_format.space_after = Pt(1)
        p.paragraph_format.keep_with_next = True
        if centro_desde is not None and i >= centro_desde:
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        _shade(c)
        c.width = widths[i]
    for nf, row in enumerate(rows):
        fila = t.add_row()
        cs = OxmlElement('w:cantSplit'); fila._tr.get_or_add_trPr().append(cs)
        cells = fila.cells
        for i, val in enumerate(row):
            p = cells[i].paragraphs[0]
            runs(p, str(val), size=size)
            p.paragraph_format.space_after = Pt(1)
            p.paragraph_format.keep_with_next = nf < 2 and len(rows) > 3
            if centro_desde is not None and i >= centro_desde:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            cells[i].width = widths[i]
    for i, w in enumerate(widths):
        t.columns[i].width = w
    tblPr = t._tbl.tblPr
    for old in tblPr.findall(qn('w:tblW')):
        tblPr.remove(old)
    tw = OxmlElement('w:tblW'); tw.set(qn('w:type'), 'dxa')
    tw.set(qn('w:w'), str(int(sum(int(w) for w in widths) / 635)))
    tblPr.append(tw)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    MD.append("| " + " | ".join(headers) + " |")
    MD.append("|" + "---|" * n)
    for row in rows:
        MD.append("| " + " | ".join(str(v).replace("\n", "<br>").replace("|", "/") for v in row) + " |")
    MD.append("")


ANCHO_IMG = {"contexto-hd": 9.3, "cdu-core-hd": 8.2, "cdu-descomposicion-hd": 7.6, "bloques-hd": 9.0,
             "despliegue-hd": 9.4}


def IMGP(nombre, width=6.5, caption=None):
    doc.add_picture(os.path.join(IMG, nombre + ".png"), width=Inches(ANCHO_IMG.get(nombre, 9.0)))
    doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.paragraphs[-1].paragraph_format.keep_with_next = True
    MD.append("![[02-Diagramas/%s/%s.svg]]\n" % (LAMINAS[nombre], nombre))
    if caption:
        p = doc.add_paragraph()
        runs(p, caption, size=9)
        for r in p.runs:
            r.italic = True
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        MD.append("*%s*\n" % caption)


def SEC(landscape=False):
    """Todo el documento va apaisado: las laminas y las matrices necesitan el
    ancho, y alternar orientaciones dejaba paginas a medio llenar."""
    return None


# =====================================================================
# DATOS
# =====================================================================
STK = [
 ["STK-01", "Garry Berryman — vicepresidente de Gestión de Materiales (promotor)", "paga · patrocina", "interno",
  "Que la Estrategia de Gestión de Suministros se cumpla: el personal de compras al 70 % en gestión de proveedores y 34 M USD de ahorro en cinco años", "págs. 4-7, anexo 4"],
 ["STK-02", "Dave Storm — vicepresidente de Planificación y Servicios de Información (promotor)", "paga · patrocina", "interno",
  "Que SiL'K encaje en la estrategia de sistemas de toda la compañía y dé una visión consolidada", "pág. 3, anexo 4"],
 ["STK-03", "Grupo de Unidad de Compras (PUG)", "decide · usa", "interno",
  "Un proceso de compras común a los centros y divisiones, y los recursos que cede al proyecto", "págs. 4, 7"],
 ["STK-04", "Pat Davidson — directora de Planificación y Control de Compras", "usa · dueña del proceso", "interno",
  "Planificar y controlar las compras de toda la empresa con datos únicos", "pág. 1, anexo 4"],
 ["STK-05", "Dave Cotteleer — director del proyecto SiL'K", "dirige el proyecto", "interno",
  "Una implantación sin riesgos, dentro del ámbito y en tres fases", "págs. 9-11"],
 ["STK-06", "Compradores de los centros y divisiones (unas 200 personas: MRO, OE, P&A, Artículos Varios)", "usa", "interno — trabajador",
  "Dejar de gastar el 85 % del tiempo en tareas no estratégicas: revisar existencias, acelerar pedidos, registrar datos", "pág. 8, anexo 5"],
 ["STK-07", "Empleados solicitantes (más de 2.000 generan solicitudes de pedido)", "usa (ocasional)", "interno",
  "Pedir lo que necesitan sin formación previa y saber en qué estado está", "pág. 8"],
 ["STK-08", "Suministradores estratégicos — Consejo Asesor de Suministradores (16)", "usa (externo)", "externo — actor",
  "Acceso a sus datos de calidad, costes y plazos y a la demanda prevista; ser tratados como socios, no como vendedores", "págs. 5, 10, anexo 3"],
 ["STK-09", "Grupo de Integración de Arquitecturas — Karen Kaminski", "regula (técnico)", "interno",
  "Que la solución cumpla las normas de hardware y software y sea compatible con la arquitectura existente", "págs. 9, 12"],
 ["STK-10", "Dirección de Sistemas del Grupo de Fabricación (Cory Mason, Tom Cullen) y su Círculo de Tecnologías de la Información", "decide la inversión · opera", "interno",
  "Aprobar la inversión y operar la solución sin afectar a la producción", "págs. 3, 6, 12"],
 ["STK-11", "Gestión del Cambio — Julie Anding", "acompaña la adopción", "interno",
  "Que las 800 personas del público objetivo adopten el nuevo proceso: formación y comunicación", "págs. 10, 14"],
 ["STK-12", "Innovación de Procesos — Chuck Braunschweig", "diseña el proceso", "interno",
  "Un flujo de proceso común, construido sobre las similitudes entre centros", "pág. 8"],
 ["STK-13", "Cuentas de Acreedores Comerciales (Finanzas)", "usa · paga a proveedores", "externo — actor",
  "Pagar solo facturas conciliadas con pedido y recepción", "pág. 8, anexo 6b"],
 ["STK-14", "Logística y recepción", "usa", "externo — actor",
  "Saber qué llega y cuándo, y registrar la recepción en el muelle", "pág. 8, anexo 6a"],
 ["STK-15", "Fabricación — centros de producción", "usa · depende del resultado", "externo — actor",
  "Que las líneas de producción no dejen de funcionar", "pág. 6"],
 ["STK-16", "Ingeniería — Centro de Desarrollo de Productos y equipos de plataforma", "usa", "externo — actor",
  "Integrar a Compras y a los suministradores en el desarrollo de nuevos productos", "págs. 4-5, anexo 6b"],
 ["STK-17", "Proveedor del software (el finalista elegido)", "construye · da soporte", "externo",
  "Implantar su paquete sin personalizaciones que no pueda mantener; relación a largo plazo", "págs. 11-14, anexo 10"],
]

RF = [
 ["RF-01", "Registrar una solicitud de pedido por cualquier empleado autorizado", "CDU-01", "anexo 6b, fase 1a"],
 ["RF-02", "Importar los requisitos de material planificados (MRP/DRP) de cada centro", "CDU-01", "anexo 6a «Requisitos»"],
 ["RF-03", "Aprobar la solicitud según las reglas de autorización", "CDU-01", "anexo 6b, fase 1a"],
 ["RF-04", "Crear el pedido de compra y enviarlo al suministrador", "CDU-01", "anexo 6b, fase 1b"],
 ["RF-05", "Agrupar la demanda de centros y divisiones contra los contratos vigentes", "CDU-01", "anexo 3"],
 ["RF-06", "Registrar la recepción de material contra el pedido", "CDU-02", "anexo 6b, fase 1c"],
 ["RF-07", "Seguir el estado y los plazos de cada pedido", "CDU-02", "anexo 6b, fase 1c"],
 ["RF-08", "Conciliar factura, pedido y recepción, y resolver discrepancias", "CDU-02", "anexo 6b, fase 1d · anexo 5"],
 ["RF-09", "Enviar la factura conciliada a Cuentas de Acreedores para su pago", "CDU-02", "anexo 6b, fase 1d"],
 ["RF-10", "Mantener un registro único de suministradores y sus contactos", "CDU-03", "anexo 6b, fase 2c · anexo 3"],
 ["RF-11", "Publicar al suministrador sus resultados y la demanda prevista", "CDU-03", "anexo 3"],
 ["RF-12", "Evaluar los resultados del suministrador en calidad, costes y plazos", "CDU-03", "anexo 6b, fase 2a"],
 ["RF-13", "Intercambiar documentos de compra con el suministrador por Internet", "CDU-03", "anexo 6b, fase 2b"],
 ["RF-14", "Consolidar los datos de compras de toda la empresa para decidir", "CDU-03", "anexo 3"],
 ["RF-15", "Planificar la participación de Compras y de suministradores en cada proyecto", "CDU-04", "anexo 6b, fase 3b-c"],
 ["RF-16", "Gestionar el coste objetivo de las piezas compradas de un proyecto", "CDU-04", "anexo 6b, fase 3d"],
 ["RF-17", "Controlar la preparación para la creación y el lanzamiento", "CDU-04", "anexo 6b, fase 3e"],
 ["RF-18", "Intercambiar datos con los sistemas existentes de Harley-Davidson", "todos", "anexo 10, criterio 8 · pág. 12"],
]

CU = [
 ["CU-01", "Solicitar material o servicio", "CDU-01", "Empleado solicitante"],
 ["CU-02", "Emitir pedido de compra", "CDU-01", "Comprador · Suministrador"],
 ["CU-03", "Generar propuestas de pedido desde MRP/DRP", "CDU-01", "Sistema MRP/DRP de planta"],
 ["CU-04", "Aprobar solicitud de pedido", "CDU-01", "Responsable de área"],
 ["CU-05", "Recibir material contra pedido", "CDU-02", "Recepcionista de almacén"],
 ["CU-06", "Seguir el estado del pedido", "CDU-02", "Comprador"],
 ["CU-07", "Conciliar factura, pedido y recepción", "CDU-02", "Suministrador · Sistema de Cuentas de Acreedores"],
 ["CU-08", "Incorporar suministrador a la base de aprovisionamiento", "CDU-03", "Comprador"],
 ["CU-09", "Consultar desempeño y demanda prevista", "CDU-03", "Suministrador"],
 ["CU-10", "Evaluar resultados del suministrador", "CDU-03", "Comprador"],
 ["CU-11", "Analizar el gasto consolidado de la empresa", "CDU-03", "Director de Compras"],
 ["CU-12", "Planificar la participación de Compras en el proyecto", "CDU-04", "Comprador de desarrollo · Ingeniero"],
 ["CU-13", "Acordar el coste objetivo de una pieza", "CDU-04", "Comprador de desarrollo · Ingeniero · Suministrador"],
 ["CU-14", "Controlar la preparación para el lanzamiento", "CDU-04", "Comprador de desarrollo"],
]
CU_APOYO = [
 ["CU-15", "Agrupar demanda contra contrato vigente", "«include» de CU-02 y CU-03", "reutilizar: dos casos base lo comparten"],
 ["CU-16", "Solicitar cotización a suministradores", "«extend» de CU-02", "[no hay contrato vigente]"],
 ["CU-17", "Resolver discrepancia de factura", "«extend» de CU-07", "[factura, pedido y recepción no coinciden]"],
 ["CU-18", "Reclamar retraso al suministrador", "«extend» de CU-06", "[plazo de entrega vencido]"],
 ["CU-19", "Calcular indicadores de calidad, coste y plazo", "«include» de CU-09, CU-10 y CU-11", "reutilizar: tres casos base lo comparten"],
 ["CU-20", "Escalar riesgo de lanzamiento", "«extend» de CU-14", "[hito de preparación incumplido]"],
]

AC = [
 ["EAC-01", "Disponibilidad", "Fiabilidad › disponibilidad",
  "La compra no puede parar la producción",
  "99,9 % mensual; conmutación en ≤ 15 min; la recepción sigue sin conexión y sincroniza sin pérdida", "Alta", "Alta", "STK-15, STK-10, STK-14", "pág. 6"],
 ["EAC-02", "Desempeño", "Eficiencia de desempeño › comportamiento temporal",
  "Operación interactiva del comprador y del solicitante",
  "≤ 2 s en el percentil 95 con 800 usuarios concurrentes", "Alta", "Media", "STK-06, STK-07", "pág. 10 (800 usuarios)"],
 ["EAC-03", "Escalabilidad", "Eficiencia de desempeño › capacidad",
  "De 200 compradores a toda la empresa y sus suministradores",
  "De 800 a 3.000 usuarios agregando nodos, con 0 cambios de código y sin salir de EAC-02", "Media", "Media", "STK-02, STK-10", "pág. 8 · Plan 2003"],
 ["EAC-04", "Seguridad", "Seguridad › confidencialidad, autenticidad, responsabilidad",
  "Suministradores externos entran por Internet",
  "100 % de accesos externos con doble factor; TLS 1.3; AES-256 en reposo; 0 lecturas de datos de otro suministrador", "Alta", "Alta", "STK-08, STK-09, STK-13", "anexo 6b, fase 2"],
 ["EAC-05", "Usabilidad", "Usabilidad › capacidad de aprendizaje, operabilidad",
  "2.000 solicitantes ocasionales; el caso evalúa «facilidad de uso»",
  "Primera solicitud sin formación en ≤ 3 min y ≤ 5 pasos, lograda por el 90 % de los solicitantes", "Alta", "Media", "STK-07, STK-11, STK-06", "anexo 10"],
 ["EAC-06", "Compatibilidad", "Compatibilidad › interoperabilidad, coexistencia",
  "Un proveedor fue eliminado por «incompatibilidad arquitectónica»",
  "100 % de las interfaces por API o mensajería estándar; un sistema de planta más se integra en ≤ 10 días-persona sin tocar los servicios de negocio", "Alta", "Alta", "STK-09, STK-10, STK-05", "págs. 9, 12 · anexo 10"],
 ["EAC-07", "Modificabilidad", "Mantenibilidad › modularidad, capacidad de ser modificado",
  "«Reducción del mantenimiento del sistema y de los costes de obsolescencia»",
  "Un cambio de regla de aprobación llega a producción en ≤ 1 día hábil tocando 1 servicio; ≥ 80 % de cobertura de pruebas en los adaptadores", "Media", "Media", "STK-10, STK-17, STK-02", "anexo 3"],
 ["EAC-08", "Portabilidad", "Portabilidad › adaptabilidad, capacidad de ser instalado",
  "El caso califica la «portabilidad de plataformas»",
  "El mismo paquete de despliegue se levanta en otra nube o centro de datos en ≤ 5 días hábiles con 0 cambios de código", "Baja", "Media", "STK-09", "anexo 10"],
 ["EAC-09", "Fiabilidad", "Fiabilidad › tolerancia a fallos · Seguridad › integridad",
  "«Eliminación de registros duplicados» y «corrección de errores»",
  "0 pedidos o facturas duplicados ante reintentos; 100 % de las facturas conciliadas a tres bandas antes del pago", "Alta", "Media", "STK-13, STK-06, STK-12", "anexo 3"],
]

EAC = [
 ["EAC-01", "La infraestructura de la plataforma", "Falla un nodo de aplicación o la base de datos primaria", "Clúster de contenedores y servidor de base de datos",
  "Operación normal, turno de planta con recepciones en curso",
  "El tráfico pasa a los nodos sanos y la base en espera toma el relevo; la tableta de recepción sigue registrando en su cola local",
  "99,9 % mensual · relevo en ≤ 15 min · 0 recepciones perdidas"],
 ["EAC-02", "Comprador", "Emite un pedido de compra con 20 líneas", "Servicio Requisición y Pedido",
  "Carga pico: 800 usuarios concurrentes", "El pedido queda registrado y enviado al suministrador", "≤ 2 s en el percentil 95"],
 ["EAC-03", "Dirección de Sistemas", "Se incorporan los 2.000 solicitantes y los suministradores de la fase 2", "Plataforma completa",
  "Crecimiento planificado entre fases", "Se agregan nodos al clúster; los servicios no cambian", "De 800 a 3.000 usuarios · 0 cambios de código · EAC-02 se mantiene"],
 ["EAC-04", "Usuario de un suministrador, autenticado", "Intenta consultar pedidos de otro suministrador", "API Gateway y Servicio Suministradores",
  "Acceso por Internet", "La petición se rechaza y queda en la bitácora de auditoría", "0 lecturas cruzadas · rechazo y registro en ≤ 1 s · 100 % de accesos externos con doble factor"],
 ["EAC-05", "Empleado solicitante sin formación", "Necesita pedir un artículo por primera vez", "Aplicación web SiL'K",
  "Uso ocasional, desde su PC de oficina", "Completa la solicitud guiado por el catálogo y ve a quién le toca aprobarla", "≤ 3 min · ≤ 5 pasos · 90 % lo logra al primer intento"],
 ["EAC-06", "Equipo de Sistemas", "Hay que conectar el MRP/DRP de un centro más", "Servicio de Integración (adaptadores)",
  "Mantenimiento, con la solución en producción", "Se agrega un adaptador; los servicios de negocio no se modifican", "≤ 10 días-persona · 0 servicios de negocio modificados"],
 ["EAC-07", "Dirección de Compras", "Cambia el límite de aprobación de un tipo de compra", "Servicio Requisición y Pedido",
  "Mantenimiento", "La regla se cambia por configuración, se prueba y se despliega", "≤ 1 día hábil · 1 servicio tocado"],
 ["EAC-08", "Grupo de Integración de Arquitecturas", "Cambia la norma de infraestructura y hay que mover la plataforma", "Paquete de despliegue",
  "Cambio planificado", "La misma definición de infraestructura levanta la solución en el nuevo entorno", "≤ 5 días hábiles · 0 cambios de código"],
 ["EAC-09", "Sistema del suministrador", "Reenvía la misma factura tras un corte de red", "Servicio Recepción y Facturas y cola de reintentos",
  "Red inestable", "El segundo envío se reconoce como repetido y no genera otro registro", "0 duplicados · 100 % de facturas conciliadas antes del pago"],
]

RE = [
 ["RE-01", "Tecnológica", "Compatible con la arquitectura de sistemas existente y con las normas de hardware y software del grupo de Integración de Arquitecturas", "pág. 9, nota 12 · pág. 12", "STK-09"],
 ["RE-02", "Tecnológica", "La solución parte de un paquete de mercado: el proyecto selecciona software, no lo desarrolla desde cero", "págs. 1, 10", "STK-05, STK-17"],
 ["RE-03", "Tecnológica", "Los suministradores acceden por Internet (la «red Internet de Suministros»)", "anexo 6b, fase 2", "STK-08, STK-01"],
 ["RE-04", "De negocio", "No es un ERP completo: el ámbito está delimitado y no se aceptan funcionalidades adicionales", "pág. 11 · anexo 6a", "STK-05, STK-03"],
 ["RE-05", "De negocio", "Implantación en tres fases: transacciones, información sobre suministradores, seguimiento de proyectos", "anexo 6b", "STK-05, STK-03"],
 ["RE-06", "De negocio", "El coste total tiene que caber en la propuesta de valor de 34 M USD en cinco años", "pág. 7 · anexo 10", "STK-01, STK-03, STK-10"],
 ["RE-07", "De negocio", "El proveedor debe poder dar soporte a largo plazo (uno fue eliminado por su pequeño tamaño)", "pág. 12", "STK-17, STK-01"],
 ["RE-08", "Organizacional", "Un único proceso común para todos los centros y las cuatro divisiones de compras", "págs. 4, 8 · anexo 3", "STK-12, STK-04, STK-03"],
 ["RE-09", "Organizacional", "La inversión la aprueba el Círculo de Tecnologías de la Información del Grupo de Fabricación", "pág. 3", "STK-10, STK-05"],
 ["RE-10", "Organizacional", "La formación y la gestión del cambio son parte de la implantación (800 personas; el cambio lo dirigen las personas en un 50-75 % y la tecnología solo en un 5-10 %)", "pág. 10 · anexo 9", "STK-11, STK-04"],
 ["RE-11", "Ambiental / física", "Usuarios repartidos en siete centros de tres estados y filiales en cinco países", "pág. 2 · anexo 2a", "STK-06, STK-02"],
 ["RE-12", "Ambiental / física", "La implantación no puede interrumpir las líneas de producción", "pág. 6", "STK-15, STK-10"],
 ["RE-13", "De integración", "Interconexión con los sistemas en funcionamiento (MRP/DRP de planta, cuentas de acreedores, ingeniería) y con las iniciativas de tecnología en marcha", "pág. 12", "STK-09, STK-10"],
 ["RE-14", "De integración", "Coexistencia con los sistemas de compras locales de cada centro mientras dura la migración por fases", "pág. 4 · anexo 6b", "STK-06, STK-15"],
 ["RE-15", "Regulatoria (supuesto)", "Control interno financiero de una empresa cotizada: segregación de funciones y rastro de auditoría en aprobaciones y pagos", "supuesto «al presente» — pág. 2 (cotiza desde 1986)", "STK-13, STK-02"],
 ["RE-16", "Regulatoria (supuesto)", "Protección de los datos personales de los contactos de suministradores en las filiales europeas", "supuesto «al presente» — pág. 2 (filiales en Europa)", "STK-08, STK-02"],
]

# --- las tres relaciones de las que salen las cuatro matrices
STK_RF = {
 "STK-01": [5, 11, 12, 14, 15], "STK-02": [14, 18], "STK-03": [5, 12, 14], "STK-04": [2, 4, 5, 7, 14],
 "STK-05": [13, 18], "STK-06": [2, 3, 4, 5, 6, 7, 8, 10, 12, 13], "STK-07": [1, 3, 7],
 "STK-08": [4, 9, 10, 11, 13, 16], "STK-09": [13, 18], "STK-10": [2, 18], "STK-11": [],
 "STK-12": [1, 4, 6, 8], "STK-13": [8, 9], "STK-14": [6, 7], "STK-15": [2, 6, 7],
 "STK-16": [15, 16, 17], "STK-17": [18],
}
RF_CU = {1: [1], 2: [3], 3: [4], 4: [2, 3], 5: [2, 3], 6: [5], 7: [6], 8: [7], 9: [7], 10: [8],
         11: [9], 12: [9, 10], 13: [2, 6, 7, 9], 14: [11], 15: [12], 16: [13], 17: [14],
         18: [3, 5, 7, 12]}
# fila DEPENDE de columna
DEP_RF = {2: [18], 3: [1], 4: [2, 3, 5, 10], 5: [10], 6: [4], 7: [4, 13], 8: [4, 6], 9: [8, 18],
          11: [10, 12, 13], 12: [6, 7, 8, 10], 13: [10], 14: [4, 8, 12], 15: [10, 18], 16: [15],
          17: [12, 15]}

# --- verificaciones de acoplamiento: si alguna falla, no hay entrega
ids_stk = [s[0] for s in STK]
assert set(STK_RF) == set(ids_stk)
for n in range(1, 19):
    assert any(n in v for v in STK_RF.values()), "RF-%02d sin stakeholder" % n
    assert RF_CU.get(n), "RF-%02d sin caso de uso" % n
for c in range(1, 15):
    assert any(c in v for v in RF_CU.values()), "CU-%02d sin requisito" % c
STK_DRV = {s: [] for s in ids_stk}
for fila in AC:
    for s in fila[7].split(", "):
        STK_DRV[s].append(fila[0])
for fila in RE:
    for s in fila[4].split(", "):
        STK_DRV[s].append(fila[0])
for s in ids_stk:
    assert STK_RF[s] or STK_DRV[s], "%s sin ningun driver" % s
for f, cols in DEP_RF.items():
    assert f not in cols
STK_CU = {s: sorted({c for r in STK_RF[s] for c in RF_CU[r]}) for s in ids_stk}

RF_CORTO = {1: "Solicitud de pedido", 2: "Requisitos MRP/DRP", 3: "Aprobación", 4: "Pedido de compra",
            5: "Agrupar demanda", 6: "Recepción", 7: "Seguimiento de plazos", 8: "Conciliar factura",
            9: "Envío a pago", 10: "Registro de suministradores", 11: "Publicar resultados y demanda",
            12: "Evaluar suministrador", 13: "Documentos por Internet", 14: "Consolidar datos",
            15: "Planificar proyecto", 16: "Coste objetivo", 17: "Preparación de lanzamiento",
            18: "Integración con existentes"}
STK_CORTO = {"STK-01": "VP Gestión de Materiales", "STK-02": "VP Servicios de Información",
             "STK-03": "Grupo de Unidad de Compras", "STK-04": "Dir. Planif. y Control de Compras",
             "STK-05": "Director del proyecto", "STK-06": "Compradores", "STK-07": "Empleados solicitantes",
             "STK-08": "Suministradores", "STK-09": "Integración de Arquitecturas",
             "STK-10": "Sistemas del Grupo de Fabricación", "STK-11": "Gestión del Cambio",
             "STK-12": "Innovación de Procesos", "STK-13": "Cuentas de Acreedores", "STK-14": "Logística",
             "STK-15": "Fabricación", "STK-16": "Ingeniería", "STK-17": "Proveedor del software"}

# =====================================================================
# ENCABEZADO
# =====================================================================
MD.append("---\ntema: Entrega de tarea\nfuente: \"Generado por 06-Proyecto-MCP/generar-entrega-hd.py — no editar a mano: "
          "cambiar el generador y volver a correrlo\"\nfecha: 2026-10-13\ntarea: Caso Harley-Davidson\n"
          "alias: [entrega harley, entrega HD, CasoHD]\n---\n")
MD.append("# Caso Harley-Davidson — proyecto SiL'K · Entrega\n")
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("Caso Harley-Davidson — arquitectura del proyecto SiL'K")
r.bold = True; r.font.size = Pt(19)
for line in ["Análisis y Diseño de Sistemas II (785) · ECYS, USAC · MBA. MSc. Claudia Rojas de Morán",
             "Santiago Barrera · Carné: ____________________ · 13 de octubre de 2026"]:
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run(line); r.font.size = Pt(10)
    p.paragraph_format.space_after = Pt(2)
    MD.append(line + "\n")

H("Índice y correspondencia con la rúbrica", 2)
TBL(["#", "Criterio de la rúbrica", "Pts", "Sección"],
    [["1", "Caso de negocio: diagrama de contexto, CDU core y CDU primera descomposición", "15", "§1"],
     ["2", "Identificación de stakeholders", "10", "§2"],
     ["3", "Drivers RF, de atributos de calidad y de restricción", "20", "§3"],
     ["4", "Matrices de trazabilidad acopladas a los criterios 1, 2 y 3 (cuatro)", "15", "§4"],
     ["5", "Estilos arquitectónicos, diagrama de bloques y diagrama de despliegue", "20", "§5"],
     ["6", "Drivers de calidad y de restricción en los pasos para definir la arquitectura, y modelo de calidad", "20", "§6"],
     ["", "**Total**", "**100**", ""]],
    fracs=[0.06, 0.70, 0.08, 0.16], size=10, centro_desde=2)

H("Declaraciones que condicionan todo el documento", 2)
NOTE("**Frontera del negocio**\n"
     "**El negocio** es la **gestión de suministros y compras de Harley-Davidson**: el ámbito que el propio caso "
     "dibuja en su anexo 6a. No es la empresa entera, y **no es el concurso de proveedores de software** que da "
     "título al caso: ese relato es la fuente de los stakeholders, los requisitos y las restricciones.\n"
     "**Consecuencia:** quienes ejecutan las compras —compradores, dirección de compras, recepcionistas— son "
     "**trabajadores del negocio**. Son **actores** las entidades de afuera: el proveedor y las **áreas** que piden, "
     "reciben y pagan. Regla de clase aplicada: las áreas son actores, las personas son trabajadores.\n"
     "**Cambio de lente:** frente al **software** SiL'K, esos mismos trabajadores pasan a ser entidades externas. "
     "Por eso el comprador no aparece en el core (§1.2) y sí en el diagrama de contexto (§1.1) y en los CDU expandidos (§3.1).")
NOTE("**Cómo se leyó la consigna**\n"
     "**«Traer el caso al presente»:** se actualiza la **tecnología** (la «red Internet de Suministros» de 1998 pasa a "
     "ser portal web, API y nube). Los **hechos** del caso —organización, ámbito, fases, cifras— no se tocan. Lo que "
     "el caso no dice y hace falta va rotulado como **supuesto**.\n"
     "**«Los pasos para definir la arquitectura»:** los siete de la lámina de clase *Pasos para la definición de una "
     "Arquitectura de software* (§6.1).\n"
     "**«EaC»:** los **escenarios de atributos de calidad**, con identificador `EAC-nn`, seis partes y prioridad en "
     "pares, tal como en el ejemplo de clase del Sistema de Transporte (§3.2).\n"
     "**«Modelo de calidad»:** según la indicación de la catedrática, el pensamiento ISO como **familia de normas**, "
     "con ISO/IEC 9126 y la serie ISO/IEC 25000 como normas concretas (§6.4).\n"
     "**Identificadores:** `STK-nn` stakeholder · `CDU-nn` proceso de negocio · `CU-nn` caso de uso del sistema · "
     "`RF-nn` driver funcional · `EAC-nn` escenario de atributo de calidad (driver de calidad) · `RE-nn` driver de restricción.\n"
     "**Trabajo individual:** el documento lo elaboró una sola persona. El nombre del archivo conserva el formato pedido.")

# =====================================================================
# §1 CASO DE NEGOCIO
# =====================================================================
H("1. Caso de negocio · criterio 1 — 15 pts", 1, brk=True)
P("Es el **paso 0** del método de clase: antes de diseñar, delimitar el negocio y lo que el producto intercambia con "
  "su entorno. Tres diagramas, de afuera hacia adentro.")
H("1.1 Diagrama de contexto", 2)
P("**El Producto** es el software SiL'K. Las entidades son todo lo que intercambia información con él: personas, "
  "áreas y sistemas. Cada flecha es un *streamline* con nombre, en sustantivo: son **19**.")
sec = SEC(True); pie(sec)
IMGP("contexto-hd", 9.3, "Figura 1 — Diagrama de contexto de SiL'K: diez entidades y diecinueve streamlines.")
sec = SEC(False); pie(sec)
TBL(["Entidad", "Entrega a SiL'K", "Recibe de SiL'K"],
    [["Empleado solicitante", "Solicitud de pedido", "Estado de la solicitud"],
     ["Responsable de área (aprobador)", "Decisión de aprobación", "Solicitud pendiente de aprobación"],
     ["Comprador", "Pedido de compra y evaluación", "Propuestas de pedido y alertas de plazo"],
     ["Dirección de Compras", "Contratos y reglas de compra", "Gasto consolidado e indicadores"],
     ["Ingeniería (Centro de Desarrollo de Productos)", "Plan del proyecto y coste objetivo", "Estado de preparación de las piezas"],
     ["Suministrador", "Confirmación, aviso de envío y factura", "Pedido, demanda prevista y resultados"],
     ["Sistema MRP/DRP de planta", "Requisitos de material", "Pedidos en firme y fechas de entrega"],
     ["Recepción y Logística", "Recepción de material", "Entregas previstas"],
     ["Sistema de Cuentas de Acreedores", "Estado del pago", "Factura conciliada para pago"],
     ["Sistemas de compras locales (en retiro)", "Histórico de pedidos y suministradores", "— (solo emiten: se migran y se apagan)"]],
    fracs=[0.30, 0.35, 0.35], size=9)

H("1.2 CDU de alto nivel (core)", 2)
P("Una sola elipse con el nombre del negocio completo y todos sus actores alrededor. Las asociaciones van **sin "
  "punta**: la comunicación se inicia en los dos sentidos.")
IMGP("cdu-core-hd", 6.3, "Figura 2 — CDU core: el negocio y sus seis actores.")
TBL(["Actor del negocio", "Por qué está afuera", "Qué obtiene del negocio"],
    [["Proveedor (suministrador)", "Otra empresa. El caso lo llama «una extensión de nosotros mismos», pero no pertenece a Harley-Davidson", "Pedidos, demanda prevista, sus resultados y el pago"],
     ["Áreas solicitantes", "Los más de 2.000 empleados que generan solicitudes no son de Compras", "El material o servicio pedido"],
     ["Fabricación (centros de producción)", "Compras le sirve; su planificación (MRP/DRP) origina la demanda de piezas", "Piezas a tiempo para no parar la línea"],
     ["Desarrollo de Productos (Ingeniería)", "Área distinta de Compras, con la que comparte los proyectos de nuevos modelos", "Piezas y suministradores listos para el lanzamiento"],
     ["Logística", "Mueve el material del almacén del suministrador al de Harley-Davidson", "Entregas previstas y recepciones registradas"],
     ["Cuentas de Acreedores Comerciales", "Área de Finanzas que paga; fue encuestada como parte implicada externa a Compras", "Facturas conciliadas para pagar"]],
    fracs=[0.24, 0.44, 0.32], size=9)
P("**Trabajadores del negocio** (dentro de la frontera, no son actores): comprador, comprador de desarrollo, "
  "dirección de compras, planificación y control de compras, y recepcionista de almacén.")

H("1.3 CDU primera descomposición", 2)
P("Un solo diagrama, con **cuatro procesos** y el **mismo juego de actores** que el core: ninguno desaparece. Los "
  "procesos salen de las tres fases del anexo 6b; la fase 1 se partió en dos porque sus actores son distintos "
  "(quien pide no es quien recibe ni quien paga).")
IMGP("cdu-descomposicion-hd", 6.0, "Figura 3 — Primera descomposición: cuatro procesos de negocio.")
TBL(["Proceso", "Origen en el caso", "Actores", "Resultado de valor"],
    [["**CDU-01** Requisición y emisión del pedido de compra", "anexo 6b, fase 1 a-b · anexo 6a: Requisitos, Realización de pedidos", "Áreas solicitantes · Fabricación · Proveedor", "Un pedido en firme en manos del suministrador"],
     ["**CDU-02** Recepción, seguimiento y pago al suministrador", "anexo 6b, fase 1 c-d · anexo 6a: Logística de entrada, Recepción", "Proveedor · Logística · Cuentas de Acreedores", "Material recibido y factura pagada sin discrepancias"],
     ["**CDU-03** Gestión de la información y la relación con suministradores", "anexo 6b, fase 2", "Proveedor", "Un suministrador evaluado e informado, tratado como socio"],
     ["**CDU-04** Seguimiento de compras en proyectos de nuevos productos", "anexo 6b, fase 3 · anexo 6a: Desarrollo", "Desarrollo de Productos · Proveedor", "Piezas y suministradores listos en coste y plazo para el lanzamiento"]],
    fracs=[0.27, 0.25, 0.22, 0.26], size=9)
NOTE("**Lo que quedó fuera del negocio, y por qué**\n"
     "El anexo 6a marca tres actividades como «no entra dentro del ámbito del proyecto SiL'K»: **Pedido / "
     "Programación** (pedidos de los clientes), **Movimiento interno de materiales** y **Distribución** (producto "
     "acabado al cliente). No se modelan. Por eso el **cliente** y el **concesionario** no son actores de este negocio.")

# =====================================================================
# §2 STAKEHOLDERS
# =====================================================================
H("2. Identificación de stakeholders · criterio 2 — 10 pts", 1, brk=True)
P("**Stakeholder** es toda persona, grupo u organización con un interés en el sistema. Se identificaron con cuatro "
  "barridos sobre el caso: el anexo 4 (promotores, comité y equipo), los grupos de gobierno (págs. 3, 4 y 9), las "
  "partes encuestadas (pág. 8) y los externos. Entra a la lista quien aporta **un interés propio** que ningún otro "
  "trae. El tipo de interés anticipa la clase de driver que aporta en el §3.")
sec = SEC(True); pie(sec)
TBL(["Id", "Stakeholder", "Interés", "Posición", "Interés propio (concern)", "Fuente"],
    STK, fracs=[0.06, 0.25, 0.11, 0.10, 0.37, 0.11], size=8.5, usable=9.4)
NOTE("**Dos poblaciones con la misma palabra**\n"
     "La traducción del caso llama «suministrador» tanto a los **proveedores de piezas** de Harley-Davidson "
     "(`STK-08`, actor del negocio) como a los **proveedores de software** que concursan (`STK-17`, que no es actor: "
     "no participa en la operación de las compras). En este documento «suministrador» es siempre el primero.")
NOTE("**Lo que quedó fuera, y por qué**\n"
     "**Recursos Humanos** fue encuestado (pág. 8), pero su interés —la formación— ya lo trae Gestión del Cambio: "
     "entra como restricción `RE-10`. Los **proveedores de software no elegidos** y la **empresa de estudios del "
     "sector** intervienen solo en la selección, no en el sistema. Los miembros del equipo con nombre propio "
     "(Carter, Jarosz, Christianson, Doman, Peissig, Pues, Sarder, Walker) se agrupan en `STK-06`: representan a "
     "su centro o división, con el mismo interés.")

# =====================================================================
# §3 DRIVERS
# =====================================================================
sec = SEC(False); pie(sec)
H("3. Drivers arquitectónicos · criterio 3 — 20 pts", 1)
P("Los **drivers arquitectónicos** son los factores críticos que guían el diseño; hay tres tipos. Los **RF** moldean "
  "la estructura y se entregan como casos de uso expandidos. Los **de calidad** definen cómo debe comportarse el "
  "sistema y se entregan como escenarios con número. Los **de restricción** son condiciones impuestas desde afuera "
  "y se entregan como listado por categoría.")
H("3.1 Drivers de requerimientos funcionales", 2)
P("Salen de las doce actividades de las tres fases (anexo 6b), de los diez criterios funcionales de la "
  "especificación (anexo 10) y de los beneficios esperados (anexo 3).")
TBL(["Id", "El sistema debe…", "Proceso", "Fuente"], RF, fracs=[0.09, 0.55, 0.11, 0.25], size=9)
P("**Alcance por fases.** Como en el ejemplo de clase, el alcance se reparte en entregas; aquí son las tres fases "
  "del anexo 6b.")
TBL(["Fase", "Tema principal", "Requerimientos que incluye"],
    [["1", "Procesos y sistemas de transacciones", "RF-01 a RF-09, RF-18"],
     ["2", "Información sobre suministradores", "RF-10 a RF-14"],
     ["3", "Seguimiento de proyectos", "RF-15 a RF-17"]],
    fracs=[0.10, 0.45, 0.45], size=9, centro_desde=None)
P("**Casos de uso del sistema.** Cada uno nombra una meta completa del actor; ninguno es un «crear / editar / "
  "consultar».")
TBL(["Id", "Caso de uso", "Proceso", "Actores"], CU, fracs=[0.09, 0.45, 0.11, 0.35], size=9)
TBL(["Id", "Caso de uso de apoyo", "Relación", "Cuándo"], CU_APOYO, fracs=[0.09, 0.37, 0.28, 0.26], size=9)
NOTE("**Cómo leer las relaciones**\n"
     "**«include»** — el caso base lo ejecuta **siempre**; la flecha va del base al incluido. Aquí se usa para "
     "**reutilizar**: dos o tres casos base comparten el incluido.\n"
     "**«extend»** — ocurre **a veces**, bajo la condición entre corchetes; la flecha va de la extensión al base.\n"
     "Los cuatro diagramas están en el **plano del sistema**: actores y casos de uso sin la barra de negocio.")
for n, cap in [("cdu-expandido-hd-01-requisicion", "Figura 4 — CDU-01 expandido."),
               ("cdu-expandido-hd-02-recepcion", "Figura 5 — CDU-02 expandido."),
               ("cdu-expandido-hd-03-suministradores", "Figura 6 — CDU-03 expandido."),
               ("cdu-expandido-hd-04-proyectos", "Figura 7 — CDU-04 expandido.")]:
    IMGP(n, 6.3, cap)

H("Descripción textual — CU-02 Emitir pedido de compra", 3)
TBL(["Campo", "Contenido"],
    [["**Nombre**", "CU-02 Emitir pedido de compra"],
     ["**Actores**", "Comprador (inicia) · Suministrador"],
     ["**Propósito**", "Convertir la demanda aprobada en un pedido en firme con el suministrador asignado, al precio del contrato."],
     ["**Resumen**", "El caso de uso se inicia cuando el Comprador toma solicitudes aprobadas o propuestas generadas desde MRP/DRP. El sistema agrupa la demanda contra el contrato vigente y emite el pedido. Finaliza cuando el Suministrador lo recibe y confirma."]],
    fracs=[0.16, 0.84], size=9)
TBL(["Acción del actor", "Respuesta del sistema"],
    [["**1.** El Comprador selecciona las solicitudes aprobadas y las propuestas pendientes.", ""],
     ["", "**2.** El sistema agrupa la demanda por suministrador y contrato vigente (incluye CU-15). *Si no hay contrato vigente, ver curso alterno de la línea 2.*"],
     ["**3.** El Comprador revisa cantidades, fechas de entrega y centro de destino, y confirma.", ""],
     ["", "**4.** El sistema registra el pedido de compra con su número único y lo envía al Suministrador."],
     ["**5.** El Suministrador recibe el pedido y confirma fecha y cantidad.", ""],
     ["", "**6.** El sistema deja el pedido en firme y devuelve la fecha confirmada al sistema MRP/DRP del centro."]],
    fracs=[0.45, 0.55], size=9)
BUL(["**En la línea 2:** no hay contrato vigente para el artículo. El Comprador solicita cotización a los "
     "suministradores (CU-16) y, con la oferta elegida, se continúa en la línea 3.",
     "**En la línea 5:** el Suministrador propone otra fecha. El sistema avisa al Comprador, que acepta o renegocia; "
     "con la fecha acordada se continúa en la línea 6.",
     "**Prioridad:** alta — es el caso que más RF concentra (RF-04, RF-05, RF-13)."], size=9.5)

H("3.2 Drivers de atributos de calidad", 2)
NOTE("**Qué taxonomía se usa**\n"
     "Las categorías siguen el ejemplo de clase (desempeño, disponibilidad, seguridad, usabilidad, modificabilidad) "
     "y la lista de drivers de calidad de clase (escalabilidad, fiabilidad). Se agregan **compatibilidad** y "
     "**portabilidad** porque el caso las evalúa por su nombre (anexo 10). La tabla ubica cada una en el modelo "
     "ISO/IEC 25010 que se determina en el §6.4.\n"
     "**Prioridad:** el par (importancia para el negocio, dificultad técnica), cada uno en A alta, M media o B baja, "
     "como en el ejemplo de clase.\n"
     "**De dónde salen los números:** el caso da cifras de **negocio** (34 M USD, 70 %, 85 %), no de comportamiento "
     "del sistema. Las medidas son **supuestos de diseño**, derivados de los volúmenes del caso (200 compradores, "
     "800 usuarios objetivo, más de 2.000 solicitantes).")
sec = SEC(True); pie(sec)
PRI = {a[0]: "(%s, %s)" % (a[5][0], a[6][0]) for a in AC}
TBL(["Id", "Categoría", "Característica ISO/IEC 25010", "Motivo en el caso", "Medida de la respuesta", "Prioridad", "Stakeholders", "Fuente"],
    [[a[0], a[1], a[2], a[3], a[4], PRI[a[0]], a[7], a[8]] for a in AC],
    fracs=[0.06, 0.10, 0.15, 0.18, 0.27, 0.07, 0.09, 0.08], size=8, usable=9.4)
P("**Escenarios de atributos de calidad (EaC).** Cada driver se especifica en seis partes: quién o qué lo provoca "
  "(fuente de estímulo), qué ocurre (estímulo), sobre qué parte (artefacto), en qué condiciones (entorno), qué hace "
  "el sistema (respuesta) y cómo se comprueba (medida de la respuesta). Sin medida no es un driver.")
CAT = {a[0]: a[1] for a in AC}
TBL(["ID", "Categoría", "Escenario", "Prioridad"],
    [[e[0], CAT[e[0]],
      "**Fuente de estímulo:** %s.\n**Estímulo:** %s.\n**Artefacto:** %s.\n**Entorno:** %s.\n"
      "**Respuesta:** %s.\n**Medida de la respuesta:** %s." % (e[1], e[2], e[3], e[4], e[5], e[6]),
      PRI[e[0]]] for e in EAC],
    fracs=[0.08, 0.14, 0.68, 0.10], size=8.5, usable=9.4)
NOTE("**Prioridad**\n"
     "Con los dos ejes —importancia para el negocio y dificultad técnica— los que más pesan en el diseño son "
     "**EAC-01, EAC-04 y EAC-06** — los tres (A, A) —, seguidos de EAC-02, EAC-05 y EAC-09, que son (A, M). Las restricciones no se priorizan: "
     "todas son obligatorias.")
H("3.3 Drivers de restricción", 2)
P("Por las seis categorías de clase. El caso no cita ninguna norma legal: las dos regulatorias son **supuestos** de "
  "traer el caso al presente, y van rotuladas.")
TBL(["Id", "Categoría", "Restricción", "Fuente", "Stakeholders"], RE,
    fracs=[0.06, 0.13, 0.50, 0.19, 0.12], size=8.5, usable=9.4)

# =====================================================================
# §4 MATRICES
# =====================================================================
sec = SEC(True); pie(sec)
H("4. Matrices de trazabilidad · criterio 4 — 15 pts", 1)
P("Las cuatro matrices cruzan los artefactos de los criterios 1, 2 y 3. Están **acopladas**: la matriz 3 no se "
  "llenó a mano, se **derivó** de la 1 y la 2 (un stakeholder se relaciona con un caso de uso si le interesa algún "
  "requisito que ese caso realiza). Así no pueden contradecirse.")
X = "X"
H("4.1 Matriz 1 — Stakeholders vs. Requerimientos", 2)
rfh = ["%02d" % n for n in range(1, 19)]
TBL(["Stakeholder \\ RF-"] + rfh,
    [["%s %s" % (s, STK_CORTO[s])] + [X if n in STK_RF[s] else "" for n in range(1, 19)] for s in ids_stk],
    fracs=[0.28] + [0.04] * 18, size=7.5, usable=9.4, centro_desde=1)
P("Los requerimientos de calidad y de restricción también tienen dueño:", size=9.5)
drv = [a[0] for a in AC] + [r[0] for r in RE]
TBL(["Stakeholder"] + [d.replace("EAC-", "E").replace("RE-", "R") for d in drv],
    [["%s %s" % (s, STK_CORTO[s])] + [X if d in STK_DRV[s] else "" for d in drv] for s in ids_stk],
    fracs=[0.25] + [0.03] * 25, size=7, usable=9.4, centro_desde=1)
P("E01-E09 son los escenarios de calidad EAC-01 a EAC-09; R01-R16, las restricciones RE-01 a RE-16. **Lectura:** ningún "
  "requerimiento queda sin stakeholder y ningún stakeholder queda sin requerimiento. `STK-11` (Gestión del Cambio) "
  "no pide funciones: su fila en RF está vacía y su interés aparece en EAC-05 y RE-10.", size=9.5)

sec = SEC(True); pie(sec)
H("4.2 Matriz 2 — Requerimientos vs. Casos de Uso", 2)
cuh = ["CU-%02d" % n for n in range(1, 15)]
TBL(["Requerimiento"] + cuh,
    [["RF-%02d %s" % (n, RF_CORTO[n])] + [X if c in RF_CU[n] else "" for c in range(1, 15)] for n in range(1, 19)],
    fracs=[0.30] + [0.05] * 14, size=7.5, usable=9.4, centro_desde=1)
P("**Lectura:** todo requerimiento lo realiza al menos un caso de uso (ninguna fila vacía) y todo caso de uso "
  "responde a algún requerimiento (ninguna columna vacía). RF-13 y RF-18 cruzan cuatro casos cada uno: el "
  "intercambio con el suministrador y la integración con lo existente son **transversales**, y eso es lo que "
  "justifica en el §5 un Servicio de Integración y un API Gateway propios. Los casos de apoyo CU-15 a CU-20 "
  "heredan la traza de su caso base.", size=9.5)

sec = SEC(True); pie(sec)
H("4.3 Matriz 3 — Stakeholders vs. Casos de Uso", 2)
TBL(["Stakeholder"] + cuh,
    [["%s %s" % (s, STK_CORTO[s])] + [X if c in STK_CU[s] else "" for c in range(1, 15)] for s in ids_stk],
    fracs=[0.30] + [0.05] * 14, size=7.5, usable=9.4, centro_desde=1)
P("**Lectura:** derivada de las matrices 1 y 2. La fila de `STK-06` (compradores) es la más densa: son los usuarios "
  "principales. La de `STK-11` queda vacía por la razón ya dicha. Las columnas CU-02, CU-06 y CU-07 concentran más "
  "interesados: son los casos de la fase 1, y por eso la fase 1 va primero.", size=9.5)

sec = SEC(True); pie(sec)
H("4.4 Matriz 4 — Requerimientos vs. Requerimientos", 2)
P("Matriz cuadrada de **dependencia**, con la plantilla de la nota técnica de trazabilidad: las columnas originan "
  "la dependencia y las filas dependen. Se lee **«la fila depende de la columna»**. La diagonal no aplica.", size=9.5)
TBL(["Depende ↓ / de →"] + rfh,
    [["RF-%02d %s" % (n, RF_CORTO[n])] + ["—" if c == n else (X if c in DEP_RF.get(n, []) else "") for c in range(1, 19)]
     for n in range(1, 19)],
    fracs=[0.28] + [0.04] * 18, size=7.5, usable=9.4, centro_desde=1)
P("**Lectura:** las columnas más marcadas son **RF-10** (registro único de suministradores, seis dependientes), "
  "**RF-04** (pedido de compra, cuatro) y **RF-18** (integración, tres). Son la base de todo lo demás, y confirman "
  "el orden de las fases: primero las transacciones, y el registro de suministradores antes que su evaluación. "
  "RF-01, RF-10 y RF-18 no dependen de nadie: por ahí se empieza a construir.", size=9.5)

# =====================================================================
# §5 ESTILOS Y DESPLIEGUE
# =====================================================================
sec = SEC(False); pie(sec)
H("5. Estilos arquitectónicos y diagrama de despliegue · criterio 5 — 20 pts", 1)
H("5.1 La decisión", 2)
P("**Estilo principal: arquitectura orientada a servicios (SOA), con un servicio por proceso de negocio** "
  "(CDU-01 a CDU-04), más un servicio de integración; **en capas** por dentro y **basada en eventos** entre "
  "servicios. Es la misma combinación del ejemplo de clase (perspectiva lógica capas/SOA y bloques basados en eventos). Un **estilo arquitectónico** establece las restricciones "
  "sobre la arquitectura de una familia de diseños; se elige en función de los drivers, no por preferencia.")
H("5.2 Por qué SOA — en función de los criterios anteriores", 2)
TBL(["Escalón de la lámina «Funcionamiento de la Arquitectura (SOA)»", "Cómo se cumple en SiL'K", "Criterio que lo respalda"],
    [["*«Define las necesidades del negocio»*", "La Estrategia de Gestión de Suministros y el negocio delimitado", "§1 — caso de negocio"],
     ["*«Desarrolla procesos de negocio como Servicios»*", "Los cuatro procesos de la primera descomposición son los cuatro servicios: la granularidad ya viene decidida", "§1.3 · matriz 2"],
     ["*«Permite que cada Servicio evolucione independientemente»*", "Las tres fases de implantación se entregan servicio por servicio, sin detener lo ya entregado", "RE-05 · RE-12 · EAC-07"],
     ["*«Plantea aplicaciones distribuidas, multi-nivel»*", "Siete centros, cinco filiales y suministradores externos acceden a la misma plataforma", "RE-11 · RE-03 · EAC-03"]],
    fracs=[0.32, 0.44, 0.24], size=9)
P("La razón de fondo es de **integración**: el problema que el caso describe son sistemas de compras distintos en "
  "cada centro (pág. 4) y la obligación de convivir con lo existente (`RE-01`, `RE-13`, `RE-14`). SOA expone cada "
  "proceso con un contrato estable, detrás del cual puede haber el paquete comprado (`RE-02`) o un sistema de planta.")
H("5.3 Estilos complementarios — cada uno con su driver", 2)
TBL(["Estilo", "Dónde se aplica", "Driver"],
    [["**En capas**", "Dentro de cada servicio: presentación, lógica de negocio y datos", "EAC-07"],
     ["**Cliente-servidor (N niveles)**", "Navegador, portal y tableta como clientes; servicios y base de datos como niveles", "EAC-03 · RE-11"],
     ["**Llamada y retorno**", "Operaciones interactivas: emitir un pedido, aprobar, consultar", "EAC-02 · EAC-05"],
     ["**Basado en eventos**", "Entre servicios y hacia los centros: «pedido emitido», «material recibido», «factura conciliada»", "EAC-01 · EAC-09 · RE-12"],
     ["**Tuberías y filtros**", "Carga del almacén analítico: extraer, depurar duplicados, consolidar", "RF-14"]],
    fracs=[0.24, 0.56, 0.20], size=9)
H("5.4 Estilos descartados", 2)
TBL(["Estilo", "Por qué no"],
    [["**Monolítico** (un ERP completo)", "Lo prohíbe el caso: *«no estaba buscando una solución completa de planificación de recursos empresariales»* (`RE-04`). Además obligaría a implantar todo de una vez, contra `RE-05`"],
     ["**Microservicios**", "La granularidad por proceso ya basta; partir más fino multiplica la operación sin un driver que lo pida, y el núcleo es un paquete de mercado (`RE-02`)"],
     ["**Par a par**", "Hay un dueño claro de los datos (Compras): no hay pares equivalentes"]],
    fracs=[0.26, 0.74], size=9)
H("5.5 Patrones arquitectónicos usados", 2)
P("De la lista de clase, de menor alcance que el estilo y con una regla cada uno: **API Gateway** (una sola puerta "
  "de entrada para suministradores y clientes web), **Single Sign-On** y **Access Token** (identidad corporativa y "
  "de suministradores), **Load Balance** (reparto entre nodos), **Circuit Breaker** (un sistema de planta caído no "
  "arrastra a los servicios), **Store and forward** (el agente de planta y la tableta guardan y reenvían), "
  "**Webhook** (aviso al sistema del suministrador) y **Log aggregation** (bitácora única).")
H("5.6 Lo que cambia al traer el caso al presente", 2)
TBL(["En el caso (1998-1999)", "Hoy", "Driver"],
    [["«Red Internet de Suministros»; intercambio electrónico de documentos", "Portal web del suministrador y API sobre HTTPS", "RE-03 · EAC-04"],
     ["Un sistema de compras por centro, modificado localmente", "Una plataforma única en la nube, configurada y no personalizada", "RE-08 · EAC-07"],
     ["Servidores propios por planta", "Contenedores e infraestructura definida como código", "EAC-03 · EAC-08"],
     ["Usuario y contraseña por sistema", "Inicio de sesión único con doble factor", "EAC-04"],
     ["Lista de control de funcionalidades y demostraciones", "Además, escenarios de atributos de calidad medibles", "§3.2 · §6"],
     ["ISO/IEC 9126", "Familia ISO/IEC 25000", "§6.4"]],
    fracs=[0.38, 0.42, 0.20], size=9)

H("5.7 Perspectiva lógica: capas dentro de cada servicio", 2)
TBL(["Elemento", "Responsabilidad"],
    [["**Capa de presentación**", "Recibe la interacción del usuario y le muestra resultados: aplicación web, portal del suministrador y app de recepción"],
     ["**Capa de servicios web**", "Expone los servicios para integrar sistemas externos: API Gateway y contratos de cada servicio"],
     ["**Capa de negocio**", "Coordina la ejecución de los casos de uso: los cuatro servicios, uno por proceso"],
     ["**Capa de datos**", "Almacena los objetos y oculta al resto que es una base relacional"],
     ["**Capa de integración**", "Conecta con los sistemas existentes: MRP/DRP de planta, Cuentas de Acreedores, ingeniería"]],
    fracs=[0.28, 0.72], size=9)
H("5.8 Diagrama de bloques — arquitectura basada en eventos", 2)
P("El **diagrama de bloques de alto nivel** es el primer paso antes del detalle: quién produce, quién enruta y quién "
  "consume. Toda flecha lleva el nombre del evento que transporta.")
sec = SEC(True); pie(sec)
IMGP("bloques-hd", 9.3, "Figura 8 — Diagrama de bloques de SiL'K: productores, enrutador y consumidores de eventos.")
sec = SEC(False); pie(sec)
P("**Cómo se integra el bus de eventos.** Es un componente central con una interfaz para publicar y suscribirse; "
  "los publicadores no conocen a los suscriptores.")
TBL(["Evento", "Publicador", "Suscriptores", "Para qué"],
    [["Solicitud aprobada", "Servicio Requisición y Pedido", "El mismo servicio (bandeja del comprador)", "Que el comprador la convierta en pedido"],
     ["Pedido emitido", "Servicio Requisición y Pedido", "Suministradores · Recepción y Facturas · MRP/DRP de planta", "Avisar al suministrador y esperar la entrega"],
     ["Requisitos publicados", "Agente de integración de la planta", "Servicio Requisición y Pedido", "Generar propuestas de pedido (CU-03)"],
     ["Material recibido", "App de recepción", "Recepción y Facturas · Suministradores · MRP/DRP de planta", "Conciliar y medir el plazo real"],
     ["Factura conciliada", "Servicio Recepción y Facturas", "Sistema de Cuentas de Acreedores", "Pagar"],
     ["Retraso detectado", "Servicio Recepción y Facturas", "Suministradores · comprador", "Reclamar y evaluar (CU-18, CU-10)"]],
    fracs=[0.17, 0.25, 0.32, 0.26], size=9)
P("**Beneficios para SiL'K**, los cuatro de clase: comunicación desacoplada (una planta caída no detiene a las "
  "demás, `RE-12`), flexibilidad (cada fase agrega suscriptores sin tocar lo entregado, `RE-05`), escalabilidad "
  "(`EAC-03`) y reutilización de los eventos (el almacén analítico los recibe todos, `RF-14`).")
H("5.9 Diagrama de despliegue", 2)
P("El **diagrama de despliegue** (o de distribución) muestra los nodos físicos y qué componentes ejecuta cada uno. "
  "Notación de clase: nodo como cubo; `«device»` para el hardware y `«executionEnvironment»` para el software que "
  "aloja componentes; componentes **dentro** del nodo; conexión de línea llena con el protocolo; zonas FrontEnd y BackEnd.")
sec = SEC(True); pie(sec)
IMGP("despliegue-hd", 9.4, "Figura 9 — Diagrama de despliegue de SiL'K.")
sec = SEC(False); pie(sec)
TBL(["Nodo", "Componentes", "Por qué está ahí"],
    [["PC de oficina", "Aplicación web SiL'K", "Compradores, solicitantes y dirección: sin instalación (EAC-05)"],
     ["Tableta del muelle", "App de recepción con cola local", "Recibir aunque no haya red (EAC-01)"],
     ["Equipo y servidor del suministrador", "Portal del suministrador · cliente de API", "Dos formas de acceso: una persona o su sistema (RE-03)"],
     ["Borde de red", "API Gateway · proveedor de identidad · pasarela VPN", "Única entrada, autenticada y limitada (EAC-04)"],
     ["Clúster de contenedores", "Cuatro servicios de negocio · portal · Servicio de Integración", "Un servicio por proceso (§5.1); escala por nodos (EAC-03)"],
     ["Clúster de mensajería", "Bus de eventos · cola de reintentos", "Desacopla servicios y centros (EAC-01, EAC-09)"],
     ["Servidor de base de datos", "BD transaccional · bitácora de auditoría", "Un registro único (RF-10) y rastro de auditoría (RE-15)"],
     ["Almacén analítico", "Almacén de datos · tablero", "El gasto consolidado no compite con la operación (EAC-02, RF-14)"],
     ["Región secundaria", "Réplica y clúster en espera", "Recuperación ante desastre (EAC-01)"],
     ["Servidor de planta (uno por centro)", "MRP/DRP · agente de integración · sistema local en retiro", "Los sistemas existentes no se mueven (RE-13, RE-14)"],
     ["Servidores corporativos", "Cuentas de Acreedores · directorio · sistemas de ingeniería", "Sistemas existentes de la sede (RE-13)"]],
    fracs=[0.24, 0.36, 0.40], size=9)
NOTE("**Supuestos de dimensionamiento**\n"
     "El caso no trae ningún dato de hardware. Para 800 usuarios concurrentes (`EAC-02`) con crecimiento a 3.000 "
     "(`EAC-03`) se supone: clúster de 3 nodos de 8 vCPU y 32 GB (24 vCPU y 96 GB en total, con capacidad para perder "
     "un nodo), base de datos primaria y en espera en zonas distintas, y mensajería de 3 nodos. Son valores de "
     "partida para la prueba de carga del paso 5 (§6.1), no un compromiso.")

# =====================================================================
# §6 PASOS + MODELO DE CALIDAD
# =====================================================================
H("6. Drivers de calidad y de restricción en los pasos, y modelo de calidad · criterio 6 — 20 pts", 1, brk=True)
H("6.1 Los pasos para definir la arquitectura, con sus drivers", 2)
P("Los siete pasos de la lámina *Pasos para la definición de una Arquitectura de software*. En cada uno se indica "
  "qué drivers de calidad y de restricción lo gobiernan: no son un anexo del diseño, lo deciden.")
TBL(["#", "Paso", "Qué se hizo para SiL'K", "Drivers de calidad", "Drivers de restricción"],
    [["1", "Creación del **caso de negocio**", "Negocio delimitado, contexto, core y descomposición (§1)", "—", "RE-04 ámbito · RE-06 valor"],
     ["2", "**Entendimiento de los requisitos**", "Stakeholders, RF, escenarios de calidad y restricciones; matrices (§2-§4)", "EAC-01 a EAC-09, escritos como EaC", "RE-01 a RE-16, por categoría"],
     ["3", "**Creación y selección** de la arquitectura", "SOA con un servicio por proceso y estilos complementarios (§5)", "EAC-06 y EAC-07 deciden SOA; EAC-01 y EAC-09 piden eventos", "RE-01, RE-02, RE-13 (integrar) · RE-04 (no monolítico)"],
     ["4", "**Documentación y comunicación**", "Este documento: vista de escenarios (CDU) y vista física (despliegue)", "Cada EaC ubicado en un nodo (§6.2)", "RE-10: comunicar a 800 personas, como los boletines del caso"],
     ["5", "**Análisis o evaluación**", "Recorrer los EaC sobre el despliegue y medir con el modelo de calidad (§6.4)", "Las nueve medidas son el criterio de aprobación", "RE-01: revisión del grupo de Integración de Arquitecturas"],
     ["6", "**Implementación** basada en la arquitectura", "Tres fases; cada fase entrega servicios completos", "EAC-03: crecer de 800 a 3.000 entre fases", "RE-05 fases · RE-12 no parar la línea · RE-14 coexistencia"],
     ["7", "**Aseguramiento** de que la implementación esté acorde", "En cada fase se vuelven a medir los EaC y se revisa la conformidad", "Las medidas del §3.2 como pruebas de aceptación", "RE-15: rastro de auditoría"]],
    fracs=[0.04, 0.19, 0.31, 0.23, 0.23], size=8.5)
NOTE("**El caso ya hacía una parte del paso 5**\n"
     "El equipo de SiL'K evaluó a los finalistas con *«diez escenarios posibles, basados en los requisitos "
     "tecnológicos y del proceso»* (pág. 12) y con una lista de control con umbral del 90 % (pág. 11). Lo que se "
     "agrega al traerlo al presente es que los escenarios sean de **atributos de calidad** y tengan **medida**.")
H("6.2 Los escenarios de calidad incorporados a la solución", 2)
P("Cada escenario del §3.2 se convierte en una decisión de arquitectura y queda ubicado en el despliegue del §5.9. "
  "Es la respuesta al numeral 4 de la tarea.")
TBL(["EaC", "Decisión de arquitectura (táctica)", "Patrón", "Dónde queda en el despliegue"],
    [["EAC-01 Disponibilidad", "Redundancia en dos zonas, base en espera activa, región secundaria; la recepción trabaja sin conexión", "Circuit Breaker · Store and forward", "Borde · clúster · BD · región secundaria · tableta · agente de planta"],
     ["EAC-02 Desempeño", "Reparto de carga; las consultas analíticas salen de la base transaccional", "Load Balance", "Borde · almacén analítico"],
     ["EAC-03 Escalabilidad", "Servicios sin estado en contenedores; se agregan nodos", "Load Balance", "Clúster de contenedores"],
     ["EAC-04 Seguridad", "Entrada única, doble factor, autorización por suministrador, cifrado en tránsito y en reposo, bitácora", "API Gateway · SSO · Access Token", "Borde · BD (bitácora)"],
     ["EAC-05 Usabilidad", "Una sola aplicación web con catálogo guiado; la interfaz separada de la lógica", "—", "PC de oficina · portal web"],
     ["EAC-06 Compatibilidad", "Adaptadores por sistema, contratos de servicio estables, VPN a los centros", "Store and forward · Webhook", "Servicio de Integración · agente de planta"],
     ["EAC-07 Modificabilidad", "Un servicio por proceso, capas dentro de cada uno, reglas por configuración", "Log aggregation", "Clúster de contenedores"],
     ["EAC-08 Portabilidad", "Contenedores e infraestructura como código; base de datos relacional estándar", "—", "Clúster · BD"],
     ["EAC-09 Fiabilidad", "Mensajes idempotentes, reintentos, transacciones y conciliación a tres bandas", "Store and forward", "Clúster de mensajería · BD"]],
    fracs=[0.17, 0.38, 0.19, 0.26], size=8.5)
H("6.3 Las restricciones incorporadas a la solución", 2)
TBL(["Restricción", "Decisión que impone"],
    [["RE-01 · RE-13 · RE-14 (compatibilidad e integración)", "Servicio de Integración y agente en cada planta; los sistemas existentes no se modifican"],
     ["RE-02 (paquete de mercado)", "El paquete queda detrás de los contratos de servicio: se configura, no se personaliza"],
     ["RE-03 (acceso por Internet)", "Portal y API públicos detrás del API Gateway"],
     ["RE-04 (no es un ERP)", "Solo los cuatro servicios del ámbito; lo demás se integra, no se reemplaza"],
     ["RE-05 · RE-12 (fases, sin parar la línea)", "Un servicio por fase, desplegado sin interrupción; los eventos aíslan a la planta"],
     ["RE-06 · RE-07 (coste y soporte)", "Infraestructura que crece por demanda; un proveedor con hoja de ruta"],
     ["RE-08 (proceso común)", "Un solo servicio por proceso para todos los centros, con reglas configurables por división"],
     ["RE-10 (cambio y formación)", "Una interfaz única y guiada; entornos de formación por fase"],
     ["RE-11 (centros y filiales)", "Acceso web desde cualquier centro; región secundaria"],
     ["RE-15 · RE-16 (control interno y datos personales)", "Bitácora de solo inserción, segregación de funciones y cifrado"]],
    fracs=[0.38, 0.62], size=9)

H("6.4 Determinación del modelo de calidad", 2)
P("Un **modelo de calidad** descompone la calidad del producto en características y subcaracterísticas que se "
  "pueden medir. El pensamiento ISO no es una norma suelta, es una **familia**:")
TBL(["Norma", "Qué aporta", "Uso en SiL'K"],
    [["**ISO/IEC 9126** (2001)", "El modelo clásico: seis características —funcionalidad, fiabilidad, usabilidad, eficiencia, mantenibilidad, portabilidad— y métricas internas, externas y en uso", "Es el modelo del programa del curso; sirve de referencia y de puente"],
     ["**ISO/IEC 25000** — SQuaRE", "La familia que la sucede, en cinco divisiones: 2500n gestión, 2501n modelo, 2502n medición, 2503n requisitos, 2504n evaluación", "Marco general"],
     ["**ISO/IEC 25010**", "El modelo de calidad del producto: ocho características", "**Modelo adoptado**"],
     ["**ISO/IEC 25023**", "Medidas para cada característica", "Origen de las métricas"],
     ["**ISO/IEC 25040**", "El proceso de evaluación", "Cómo se aplica en los pasos 5 y 7"]],
    fracs=[0.22, 0.50, 0.28], size=9)
NOTE("**Por qué 25010 y no 9126**\n"
     "La consigna pide métodos actuales, y la 25010 sustituye a la 9126. Además, lo que más pesa en este caso "
     "—**seguridad** y **compatibilidad**— en la 9126 eran subcaracterísticas de *funcionalidad*; en la 25010 son "
     "características de primer nivel. El caso mismo eliminó a un proveedor por compatibilidad.")
P("**El modelo determinado para SiL'K.** Cada característica se concreta en una subcaracterística, una métrica y un "
  "umbral, y se traza al driver del §3. Es el árbol que se mide en los pasos 5 y 7.")
sec = SEC(True); pie(sec)
TBL(["Característica ISO/IEC 25010", "Subcaracterística", "Equivalente en ISO/IEC 9126", "Driver", "Métrica", "Umbral"],
    [["Adecuación funcional", "Completitud funcional", "Funcionalidad › adecuación", "RF-01 a RF-18", "% de los criterios de la especificación funcional cubiertos sin personalizar", "≥ 95 % (el caso exigía 90 %)"],
     ["Eficiencia de desempeño", "Comportamiento temporal", "Eficiencia › comportamiento temporal", "EAC-02", "Tiempo de respuesta, percentil 95", "≤ 2 s con 800 usuarios"],
     ["Eficiencia de desempeño", "Capacidad", "Eficiencia › utilización de recursos", "EAC-03", "Usuarios soportados sin cambio de código", "3.000"],
     ["Compatibilidad", "Interoperabilidad · coexistencia", "Funcionalidad › interoperabilidad", "EAC-06 · RE-13 · RE-14", "% de interfaces estándar; esfuerzo de integrar un sistema", "100 % · ≤ 10 días-persona"],
     ["Usabilidad", "Capacidad de aprendizaje · operabilidad", "Usabilidad › facilidad de aprendizaje", "EAC-05", "Tiempo y pasos de la primera solicitud; % de éxito", "≤ 3 min · ≤ 5 pasos · 90 %"],
     ["Fiabilidad", "Disponibilidad · recuperabilidad", "Fiabilidad › recuperabilidad", "EAC-01", "% de disponibilidad mensual; tiempo de relevo", "99,9 % · ≤ 15 min"],
     ["Fiabilidad", "Tolerancia a fallos", "Fiabilidad › tolerancia a fallos", "EAC-09", "Registros duplicados ante reintentos", "0"],
     ["Seguridad", "Confidencialidad · autenticidad · responsabilidad", "Funcionalidad › seguridad", "EAC-04 · RE-15 · RE-16", "Lecturas cruzadas; % de accesos con doble factor; % de operaciones en bitácora", "0 · 100 % · 100 %"],
     ["Mantenibilidad", "Modularidad · capacidad de ser modificado", "Mantenibilidad › facilidad de cambio", "EAC-07", "Tiempo de un cambio de regla; servicios tocados", "≤ 1 día hábil · 1"],
     ["Portabilidad", "Adaptabilidad · capacidad de ser instalado", "Portabilidad › adaptabilidad", "EAC-08", "Tiempo de levantar la solución en otro entorno", "≤ 5 días hábiles"]],
    fracs=[0.15, 0.17, 0.17, 0.13, 0.24, 0.14], size=8.5, usable=9.4)
P("**Cómo se usa.** En el paso 5 se evalúa la arquitectura contra los diez umbrales antes de construir; en el paso 7 "
  "se vuelve a medir al cerrar cada una de las tres fases. Una característica por debajo de su umbral bloquea el "
  "paso a la fase siguiente. Las ocho características de la norma están cubiertas; las tres con más peso para este "
  "caso son **compatibilidad, seguridad y fiabilidad**, las mismas que la prioridad del §3.2.")

H("7. Supuestos y límites", 2)
BUL(["Las medidas de calidad, las dos restricciones regulatorias y el dimensionamiento son **supuestos de diseño**; "
     "el caso no trae esos datos.",
     "No se elige proveedor de software: el caso termina sin decidirlo y la rúbrica no lo pide. La arquitectura vale "
     "para cualquiera de los tres finalistas, porque el paquete queda detrás de los contratos de servicio.",
     "No se incluye un diagrama de componentes aparte: los componentes van dentro de sus nodos en el despliegue.",
     "Se entrega la descripción textual de un caso de uso (CU-02) como muestra de la plantilla; los otros trece "
     "quedan especificados por su diagrama y su traza."], size=9.5)

MD.append("\n## Preguntas de repaso\n")
MD.append("1. ¿Por qué el negocio es la gestión de suministros y no la selección del software?\n"
          "2. ¿Por qué el comprador aparece en el contexto y no en el core?\n"
          "3. ¿De qué dos matrices se deriva la de Stakeholders vs. Casos de Uso?\n"
          "4. ¿Qué escalón de la lámina de SOA fija la granularidad de los servicios?\n"
          "5. ¿Qué dos características son de primer nivel en ISO/IEC 25010 y no lo eran en la 9126?\n")

out_docx = os.path.join(TAREAS, BASE + ".docx")
doc.save(out_docx)
with open(os.path.join(TAREAS, BASE + ".md"), "w", encoding="utf-8") as f:
    f.write("\n".join(MD))
print("docx:", out_docx)
if shutil.which("soffice"):
    tmp = tempfile.mkdtemp(prefix="entrega-hd-pdf-")
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", tmp, out_docx],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    shutil.move(os.path.join(tmp, BASE + ".pdf"), os.path.join(TAREAS, PDF))
    print("pdf:", os.path.join(TAREAS, PDF))
else:
    print("Sin soffice: exporta el .docx a PDF a mano como", PDF)
shutil.rmtree(IMG, ignore_errors=True)
