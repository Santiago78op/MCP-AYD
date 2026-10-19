# -*- coding: utf-8 -*-
"""Arma la presentacion de la Tarea 3 (Caso 4, Repensando los parquimetros) ya animada.

    python3 generar-presentacion-parq.py

Sale ../08-Tareas/Grupo2_CasoParquimetros_Presentacion.pptx con:
  · estilo sobrio tipo keynote: fondo casi negro, una sola tipografia (Arial, que tiene
    la computadora del aula), numeros grandes, tarjetas redondeadas, sin cremas ni degradados;
  · cada tarjeta es UN grupo que entra con un clic (desvanecido con subida), igual que
    animar-pptx.py: animada pieza por pieza, Keynote la desarma a mitad de la subida;
  · transicion de desvanecido, y de empuje donde empieza cada orador;
  · el guion de cada lamina en las notas del orador, leido de
    ../08-Tareas/Guion - Presentación Caso Parquímetros.md
Ademas escribe un guion por integrante en ../08-Tareas/guiones-caso-parquimetros/.

Aborta si los clics de una lamina no coinciden con los «(clic)» de su guion.
"""
import os
import re
import subprocess
import tempfile

from lxml import etree
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR, MSO_AUTO_SIZE
from pptx.util import Emu, Pt

AQUI = os.path.dirname(os.path.abspath(__file__))
TAREAS = os.path.join(AQUI, "..", "08-Tareas")
DIAG = os.path.join(AQUI, "..", "02-Diagramas", "caso-parquimetros")
FOTOS = os.path.join(AQUI, "..", "adjuntos", "caso-parquimetros")   # fotos del PDF del caso (Morales Zaragoza)
GUION = os.path.join(TAREAS, "Guion - Presentación Caso Parquímetros.md")
SALIDA = os.path.join(TAREAS, "Grupo2_CasoParquimetros_Presentacion.pptx")
FUENTE = "Arial"
P_NS = "http://schemas.openxmlformats.org/presentationml/2006/main"

FONDO = RGBColor(0x0F, 0x10, 0x12)
TARJETA = RGBColor(0x1B, 0x1D, 0x21)
BORDE = RGBColor(0x2C, 0x30, 0x36)
TEXTO = RGBColor(0xF2, 0xF3, 0xF5)
SUAVE = RGBColor(0xA8, 0xAE, 0xB8)
ACENTO = RGBColor(0x5A, 0xA2, 0xFF)
BLANCO = RGBColor(0xFF, 0xFF, 0xFF)

# La base sale de una presentacion que Keynote ya abrio bien: el patron de notas que crea
# python-pptx por defecto hace que Keynote rechace el archivo entero (verificado el 2026-10-19).
prs = Presentation(os.path.join(AQUI, "plantillas", "base-presentacion-16x9.pptx"))
prs.slide_width, prs.slide_height = Emu(12192000), Emu(6858000)
K = 12192000 / 1920.0                      # todo se dibuja en px de una lamina de 1920 x 1080
VACIA = prs.slide_layouts[0]               # «DEFAULT»: sin marcadores de posicion
TMP = tempfile.mkdtemp(prefix="presentacion-parq-")


def px(v):
    return Emu(int(round(v * K)))


def icono_png(nombre, color="#5AA2FF", tam=256):
    """Los trazos de Lucide (iconos/, licencia ISC) recoloreados a PNG."""
    crudo = open(os.path.join(AQUI, "iconos", nombre + ".svg"), encoding="utf-8").read()
    crudo = crudo.replace("currentColor", color).replace('stroke-width="2"', 'stroke-width="1.6"')
    svg = os.path.join(TMP, nombre + ".svg")
    png = os.path.join(TMP, "%s-%s.png" % (nombre, color.strip("#")))
    open(svg, "w", encoding="utf-8").write(crudo)
    subprocess.run(["rsvg-convert", "-w", str(tam), "-h", str(tam), svg, "-o", png], check=True)
    return png


def fondo(slide):
    f = slide.background.fill
    f.solid()
    f.fore_color.rgb = FONDO


def texto(shapes, x, y, w, h, t, tam=20, color=TEXTO, negrita=False, alinear=PP_ALIGN.LEFT,
          ancla=MSO_ANCHOR.TOP, interlineado=1.12):
    """Caja de texto. Cada linea de t es un parrafo; **x** va en negrita."""
    tb = shapes.add_textbox(px(x), px(y), px(w), px(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.auto_size = MSO_AUTO_SIZE.NONE      # alto fijo: cada visor lo resolvia distinto
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = ancla
    for i, linea in enumerate(t.split("\n")):
        par = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        par.alignment = alinear
        par.line_spacing = interlineado
        for j, trozo in enumerate(re.split(r"\*\*", linea)):
            if not trozo:
                continue
            r = par.add_run()
            r.text = trozo
            r.font.name = FUENTE
            r.font.size = Pt(tam)
            r.font.bold = negrita or (j % 2 == 1)
            r.font.color.rgb = color
    return tb


def rect(shapes, x, y, w, h, relleno=TARJETA, borde=BORDE, redondeo=0.06):
    s = shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, px(x), px(y), px(w), px(h))
    s.adjustments[0] = redondeo
    s.fill.solid()
    s.fill.fore_color.rgb = relleno
    if borde is None:
        s.line.fill.background()
    else:
        s.line.color.rgb = borde
        s.line.width = Pt(0.75)
    s.shadow.inherit = False
    return s


# Los cinco bloques de la exposicion. La barra de avance lleva los mismos nombres de forma en
# todas las laminas («!!» es la convencion de PowerPoint para emparejar objetos), asi la
# transicion Morph (Movimiento magico en Keynote) desliza el segmento activo de un bloque al otro.
BLOQUES = [("El caso", 1, 3), ("El problema", 4, 5), ("La solución", 6, 9),
           ("Calidad e información", 10, 12), ("Cómo se construye", 13, 15)]
GRIS_HECHO = RGBColor(0x55, 0x5B, 0x66)
TAM_TITULO = 36


def avance(slide, n):
    for k, (nombre, a, b) in enumerate(BLOQUES):
        x, w = 120 + k * 340, 320
        activo, hecho = a <= n <= b, n > b
        barra = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, px(x), px(44), px(w), px(6))
        barra.name = "!!avance%d" % k
        barra.fill.solid()
        barra.fill.fore_color.rgb = ACENTO if activo else (GRIS_HECHO if hecho else BORDE)
        barra.line.fill.background()
        barra.shadow.inherit = False
        r = texto(slide.shapes, x, 58, w, 26, nombre, tam=11, negrita=activo, color=TEXTO if activo else SUAVE)
        r.name = "!!rotulo%d" % k


def cabecera(slide, n, antetitulo, titulo):
    fondo(slide)
    avance(slide, n)
    a = texto(slide.shapes, 120, 112, 1400, 34, antetitulo.upper(), tam=15, color=ACENTO, negrita=True)
    a.name = "!!antetitulo"
    t = texto(slide.shapes, 120, 150, 1680, 160, titulo, tam=TAM_TITULO, negrita=True, interlineado=1.02)
    t.name = "!!titulo"
    texto(slide.shapes, 120, 1020, 1200, 28, "Grupo 2 · Caso 4: Repensando los parquímetros", tam=11, color=SUAVE)
    texto(slide.shapes, 1700, 1020, 100, 28, str(n), tam=11, color=SUAVE, alinear=PP_ALIGN.RIGHT)


def lineas(t, ancho, tam, negrita=False):
    """Cuantas lineas ocupa t en un ancho de px: 1 pt = 2 px en esta reticula, y un caracter
    de Arial mide en promedio 0,52 em (0,56 en negrita)."""
    por_linea = max(1, int(ancho / (tam * 2 * (0.56 if negrita else 0.52))))
    total = 0
    for par in t.split("\n"):
        palabras, n, largo = par.replace("**", "").split(" "), 1, 0
        for w in palabras:
            if largo and largo + 1 + len(w) > por_linea:
                n, largo = n + 1, len(w)
            else:
                largo += (1 if largo else 0) + len(w)
        total += n
    return total


def alto(t, ancho, tam, negrita=False, inter=1.12):
    return lineas(t, ancho, tam, negrita) * tam * 2 * inter * 1.05


def tarjeta(slide, x, y, w, h, icono=None, grande=None, titulo=None, cuerpo=None, tam_grande=54, tam_cuerpo=17,
            alto_titulo=None, foto=None, alto_visual=None):
    """Una tarjeta = un grupo: fondo, icono, numero grande, titulo y cuerpo, apilados con su alto real."""
    g = slide.shapes.add_group_shape()
    rect(g.shapes, x, y, w, h)
    cw, cy = w - 80, y + 36
    if foto:
        # la foto del caso en lugar del icono: muestra el problema en el aparato real
        from PIL import Image
        iw, ih = Image.open(foto).size
        hf = cw * ih / iw
        g.shapes.add_picture(foto, px(x + 40), px(cy), px(cw), px(hf))
        cy += hf + 14
    elif icono:
        g.shapes.add_picture(icono_png(icono), px(x + 40), px(cy), px(64), px(64))
        cy += alto_visual + 14 if alto_visual else 92   # alto_visual: los titulos alineados con una tarjeta con foto
    if grande:
        hg = alto(grande, cw, tam_grande, True, 1.0)
        texto(g.shapes, x + 40, cy, cw, hg, grande, tam=tam_grande, negrita=True, color=ACENTO, interlineado=1.0)
        cy += hg + 8
    if titulo:
        ht = alto_titulo or alto(titulo, cw, 22, True, 1.0)
        texto(g.shapes, x + 40, cy, cw, ht, titulo, tam=22, negrita=True, interlineado=1.0)
        cy += ht + 14
    if cuerpo:
        hc = alto(cuerpo, cw, tam_cuerpo)
        if cy + hc > y + h - 20:
            raise SystemExit("tarjeta %r: el cuerpo no cabe (%d px de %d)" % ((titulo or grande)[:30], cy + hc - y, h))
        texto(g.shapes, x + 40, cy, cw, hc, cuerpo, tam=tam_cuerpo, color=SUAVE)
    return g


def imagen(slide, ruta, x, y, w_max, h_max, panel=True):
    """Lamina blanca sobre panel blanco redondeado, ajustada sin deformar."""
    from PIL import Image
    iw, ih = Image.open(ruta).size
    esc = min(w_max / iw, h_max / ih)
    w, h = iw * esc, ih * esc
    x0, y0 = x + (w_max - w) / 2, y + (h_max - h) / 2
    g = slide.shapes.add_group_shape()
    if panel:
        rect(g.shapes, x0 - 20, y0 - 20, w + 40, h + 40, relleno=BLANCO, borde=None, redondeo=0.03)
    g.shapes.add_picture(ruta, px(x0), px(y0), px(w), px(h))
    return g


def svg_png(rel, ancho=2400):
    salida = os.path.join(TMP, os.path.basename(rel).replace(".svg", ".png"))
    subprocess.run(["rsvg-convert", "-w", str(ancho), "-b", "white", os.path.join(DIAG, rel), "-o", salida], check=True)
    return salida


COLS4 = [(120, 400), (540, 400), (960, 400), (1380, 420)]
COLS3 = [(120, 540), (690, 540), (1260, 540)]
LAMINAS = []          # (slide, [grupos animados], empuje)
TOPE = 980            # nada baja de aqui: el pie va en 1020


def nueva(n, antetitulo, titulo, empuje=False, bajada=None):
    """Devuelve la lamina, su lista de grupos animados y la y donde empieza el contenido."""
    nl = lineas(titulo, 1680, TAM_TITULO, True)
    if nl > 2:
        raise SystemExit("lámina %d: el título %r ocupa más de dos líneas" % (n, titulo))
    s = prs.slides.add_slide(VACIA)
    cabecera(s, n, antetitulo, titulo)
    y = 150 + nl * TAM_TITULO * 2 * 1.06 + 34
    if bajada:
        hb = alto(bajada, 1680, 20)
        texto(s.shapes, 120, y, 1680, hb, bajada, tam=20, color=SUAVE)
        y += hb + 30
    grupos = []
    LAMINAS.append((s, grupos, empuje))
    return s, grupos, y + 20


# ---------------------------------------------------------------- 1 portada
s = prs.slides.add_slide(VACIA)
fondo(s)
LAMINAS.append((s, [], False))
s.shapes.add_picture(icono_png("parking-meter"), px(120), px(130), px(110), px(110))
texto(s.shapes, 120, 290, 1600, 40, "ANÁLISIS Y DISEÑO DE SISTEMAS II · TAREA 3 · CASO 4", tam=16, color=ACENTO, negrita=True)
texto(s.shapes, 120, 340, 1700, 130, "Repensando los parquímetros", tam=54, negrita=True, interlineado=1.0)
texto(s.shapes, 120, 480, 1600, 60, "SIEP: una solución desde la arquitectura del software", tam=26, color=SUAVE)
for i, (nom, rol) in enumerate([("Santiago Julián Barrera Reyes", "Scrum Master · coordinador"),
                                ("Jemima Solmaira Chavajay Quiejú", "Product Owner"),
                                ("Byron Josué Par Rancho", "Equipo de desarrollo")]):
    texto(s.shapes, 120, 660 + i * 76, 900, 40, nom, tam=19, negrita=True)
    texto(s.shapes, 1000, 660 + i * 76, 700, 40, rol, tam=19, color=SUAVE)
texto(s.shapes, 120, 1000, 1600, 30, "Grupo 2 · ECYS, USAC · MBA. MSc. Claudia Rojas de Morán · octubre de 2026", tam=13, color=SUAVE)

# ---------------------------------------------------------------- 2 el caso
s, G, y = nueva(2, "El caso", "SERVIparq quiere que el cajón rote, pero el programa tiene seis problemas",
                bajada="Ciudad de México, 2012. Un cajón de estacionamiento vale hasta **200 mil pesos**: la meta es que lo usen muchos conductores, no uno solo.")
# la foto del caso: el aparato del que se habla, con sus partes rotuladas por la autora
rect(s.shapes, 120, y, 400, TOPE - y, relleno=BLANCO, borde=None, redondeo=0.04)
hf = 370 * 640 / 856
yf = y + (TOPE - y - hf - 24 - 60) / 2          # foto y pie centrados en el panel
s.shapes.add_picture(os.path.join(FOTOS, "parquimetro-partes.png"), px(135), px(yf), px(370), px(hf))
texto(s.shapes, 140, yf + hf + 24, 360, 60, "El parquímetro de SERVIparq\n(Morales Zaragoza, 2015)", tam=13,
      color=RGBColor(0x44, 0x4A, 0x52), alinear=PP_ALIGN.CENTER)
(x1, w1), (x2, w2), (x3, w3) = COLS4[1:]
G.append(tarjeta(s, x1, y, w1, TOPE - y, grande="70/30", tam_grande=44, titulo="Así se reparte lo cobrado",
                 cuerpo="70 % para operar y mantener los equipos.\n30 % se reinvierte en la comunidad.", tam_cuerpo=16))
G.append(tarjeta(s, x2, y, w2, TOPE - y, grande="6", tam_grande=44, titulo="problemas en el diagnóstico",
                 cuerpo="Consulta, cuidacarros, instrucciones, reclamos, personal y desconfianza.",
                 tam_cuerpo=16))
G.append(tarjeta(s, x3, y, w3, TOPE - y, icono="users", titulo="Pruebas con personas",
                 cuerpo="Smartmedia mide con tareas reales si la gente encuentra y entiende la información.",
                 tam_cuerpo=16))
(x1, w1), (x2, w2), (x3, w3) = COLS3

# ---------------------------------------------------------------- 3 Guatemala
s, G, y = nueva(3, "Investigación", "En Guatemala se cobra Q3 por media hora, y también cobran los cuidacarros")
tarjeta(s, x1, y, w1, TOPE - y, grande="Q3", titulo="por cada 30 minutos",
        cuerpo="Acuerdo COM-40-2022 de la Municipalidad de Guatemala, vigente desde febrero de 2024. Banqueta por colores: blanco se puede, rojo no. EMETRA anunció pago por aplicación.")
G.append(tarjeta(s, x2, y, w2, TOPE - y, grande="2,500", titulo="objetos que apartaban lugares",
                 cuerpo="Retirados en un operativo de la PMT (2023). Cobrar por dejar estacionar puede ser extorsión: se denuncia al 1551. Zona 13, 2026: 33 personas cobraban hasta US$50."))
G.append(tarjeta(s, x3, y, w3, TOPE - y, grande="Q12 M", titulo="cobró MarbEx en 2025, Antigua Guatemala",
                 cuerpo="Marbete digital por placa: Q7 M en 2024. En 2026 la Corte de Constitucionalidad suspendió la base de datos de placas y la multa de Q500."))

# ---------------------------------------------------------------- 4 problemas
s, G, y = nueva(4, "Los seis problemas", "Tres de los seis problemas no se arreglan con una pantalla mejor", empuje=True)
for (x, w), ic, tit, cue in zip(COLS4, ["users", "map-pin", "wrench", "hand-coins"],
                                ["Gobierno", "Información", "Capacidad", "Cobro informal"],
                                ["P-01 Vecinos no consultados.\nP-06 Nadie ve a dónde va el dinero.",
                                 "P-03 Instrucciones confusas y solo monedas.\nP-04 No se sabe cómo reclamar una multa.",
                                 "P-05 Falta personal. El equipo ya podía cobrar con tarjeta y avisar vandalismo: estaba apagado.",
                                 "P-02 Cuidacarros («franeleros» en el caso): apartan el lugar y cobran por él."]):
    foto = os.path.join(FOTOS, "parquimetro-panel-de-uso.png") if tit == "Información" else None
    G.append(tarjeta(s, x, y, w, TOPE - y, icono=ic, titulo=tit, cuerpo=cue, tam_cuerpo=18, alto_titulo=46 * 2 * 1.05,
                     foto=foto, alto_visual=320 * 286 / 635))

# ---------------------------------------------------------------- 5 el 72 %
s, G, y = nueva(5, "Requisitos de desempeño", "El 72 % es el éxito esperado, pero cada tarea merece su propio número")
for i, (t, c) in enumerate([("Antes del uso", "Encontrar la zona, un cajón y su parquímetro"),
                            ("Durante", "Entender tarifa y tiempo máximo, y pagar"),
                            ("Después", "Saber cuándo vence y cómo reclamar")]):
    rect(s.shapes, 120 + i * 570, y, 540, 165)
    texto(s.shapes, 150 + i * 570, y + 22, 480, 44, t, tam=20, negrita=True)
    texto(s.shapes, 150 + i * 570, y + 70, 480, 70, c, tam=16, color=SUAVE)
y2 = y + 195
G.append(tarjeta(s, 120, y2, 820, TOPE - y2, grande="72 %", tam_grande=64, titulo="el nivel que acordaron",
                 cuerpo="80 % encuentra la información (va con prisa)\n× 90 % la usa bien\n= 72 % completa la tarea."))
g = s.shapes.add_group_shape()
rect(g.shapes, 980, y2, 820, TOPE - y2)
texto(g.shapes, 1020, y2 + 36, 740, 50, "Un número por tarea", tam=22, negrita=True)
for i, (t, v) in enumerate([("Pagar por placa (si falla, multa injusta)", "81 %"),
                            ("Entender la tarifa", "72 %"), ("Saber cómo reclamar", "72 %"),
                            ("Ubicar el número del parquímetro", "64 %")]):
    yy = y2 + 96 + i * 74
    texto(g.shapes, 1020, yy, 560, 76, t, tam=17, color=SUAVE, ancla=MSO_ANCHOR.MIDDLE)
    texto(g.shapes, 1590, yy, 170, 76, v, tam=30, negrita=True, color=ACENTO, alinear=PP_ALIGN.RIGHT, ancla=MSO_ANCHOR.MIDDLE)
G.append(g)

# ---------------------------------------------------------------- 6 el negocio
s, G, y = nueva(6, "Caso de negocio", "El negocio son cinco procesos; el cuidacarros queda fuera, pero cuenta", empuje=True)
texto(s.shapes, 120, y, 600, TOPE - y,
      "**Negocio:** gestionar el estacionamiento en la calle.\n\n"
      "**Actores:** conductor, comité vecinal, Delegación, oficial de tránsito, banco y proveedor del parquímetro.\n\n"
      "**Trabajadores:** el verificador y el personal de SERVIparq.\n\n"
      "**No es actor:** el cuidacarros. No participa de forma legal, pero el diseño lo toma en cuenta.",
      tam=16, color=SUAVE, interlineado=1.12)
G.append(imagen(s, svg_png("1-caso-negocio/cdu-descomposicion-parq.svg"), 780, y, 1020, TOPE - y))

# ---------------------------------------------------------------- 7 alternativas
s, G, y = nueva(7, "Posibles soluciones", "Elegimos pagar por placa con el equipo que ya se compró")
for (x, w), tag, tit, cue in zip(COLS4, ["DENTRO", "NÚCLEO", "DESPUÉS", "ALREDEDOR"],
                                 ["S-1 Rediseñar solo la información", "S-2 Pago por placa, conectado",
                                  "S-3 Sensores y tarifa por demanda", "S-4 Gobierno comunitario"],
                                 ["Barato y rápido. No resuelve la falta de personal ni la desconfianza.",
                                  "Monedas, tarjeta o celular con el equipo ya comprado. Ataca 5 de los 6 problemas.",
                                  "Como San Francisco. Caro, expuesto al vandalismo y sin datos todavía.",
                                  "Consulta previa, tablero público y protocolo con los cuidacarros."]):
    g = tarjeta(s, x, y, w, TOPE - y, titulo=tit, cuerpo=cue, tam_cuerpo=18, alto_titulo=46 * 3 * 1.05)
    if tag == "NÚCLEO":
        fondo_tarjeta = g.shapes[0]
        fondo_tarjeta.line.color.rgb = ACENTO
        fondo_tarjeta.line.width = Pt(2.25)
    texto(g.shapes, x + 40, TOPE - 80, w - 80, 44, tag, tam=20, negrita=True, color=ACENTO)
    G.append(g)

# ---------------------------------------------------------------- 8 arquitectura
s, G, y = nueva(8, "Arquitectura del software", "Cada proceso es un servicio, y los servicios se avisan con eventos")
for i, t in enumerate(["Zonas y comunidad", "Cobro por placa", "Verificación y sanción", "Transparencia", "Red y mantenimiento"]):
    rect(s.shapes, 120, y + i * 96, 580, 80)
    texto(s.shapes, 150, y + i * 96, 530, 80, "**CDU-0%d**  %s" % (i + 1, t), tam=17, ancla=MSO_ANCHOR.MIDDLE)
g = imagen(s, svg_png("3-arquitectura/bloques-parq.svg"), 780, y, 1020, TOPE - 190 - y)
g.efecto = "barrido"
G.append(g)
g = s.shapes.add_group_shape()
for i, t in enumerate(["El pago queda en la placa: no hay boleto", "Se encienden el pago con tarjeta y la alarma",
                       "La multa nace solo si el oficial la confirma", "Todo lo cobrado se publica"]):
    rect(g.shapes, 120 + i * 425, TOPE - 150, 400, 150)
    texto(g.shapes, 150 + i * 425, TOPE - 150, 340, 150, t, tam=17, negrita=True, ancla=MSO_ANCHOR.MIDDLE)
G.append(g)

# ---------------------------------------------------------------- 9 despliegue
s, G, y = nueva(9, "Despliegue", "El parquímetro sigue cobrando aunque se caiga la señal")
imagen(s, svg_png("3-arquitectura/despliegue-parq.svg", 3000), 120, y, 1680, TOPE - y)

# ---------------------------------------------------------------- 10 calidad
s, G, y = nueva(10, "Calidad del software", "Nos comprometemos con cuatro números que se pueden medir", empuje=True)
for (x, w), gr, tit, cue in zip(COLS4, ["72 %", "2 s", "0", "100 %"],
                                ["Eficacia", "Rendimiento", "Disponibilidad", "Seguridad"],
                                ["de los conductores paga sin ayuda la primera vez (calidad en uso, ISO 9126).",
                                 "para que el verificador sepa si una placa pagó, en 95 de cada 100 consultas.",
                                 "pagos perdidos aunque se caiga la señal: el equipo guarda y reenvía.",
                                 "de las multas con foto, hora, ubicación y confirmación del oficial."]):
    G.append(tarjeta(s, x, y, w, TOPE - y, grande=gr, tam_grande=52, titulo=tit, cuerpo=cue, tam_cuerpo=18))

# ---------------------------------------------------------------- 11 arquitectura de la informacion
s, G, y = nueva(11, "Arquitectura de la información", "La información se ordena por lo que el conductor hace en cada momento")


def pantalla(paso):
    """La columna del parquimetro en una captura del prototipo (capturas a 2x)."""
    from PIL import Image
    salida = os.path.join(TMP, "pantalla-%d.png" % paso)
    Image.open(os.path.join(DIAG, "4-prototipo", "prototipo-paso-%d.png" % paso)).crop((60, 40, 1210, 1300)).save(salida)
    return salida


for (x, w), tit, cue, vis in zip(COLS3, ["Antes", "Durante", "Después"],
                                 ["Señal con el color de la banqueta, la tarifa y el número del parquímetro.",
                                  "Tres pasos: placa, tiempo y pago, con la tarifa siempre arriba.",
                                  "Comprobante con folio y hora de vencimiento, y cómo reclamar."],
                                 [None, 1, 4]):
    g = s.shapes.add_group_shape()
    rect(g.shapes, x, y, w, TOPE - y)
    alto_vis = TOPE - y - 250
    if vis is None:
        # la senal de la cuadra, dibujada: lo que el conductor ve antes de bajarse
        sx, sy, sw = x + 90, y + 40, w - 180
        rect(g.shapes, sx, sy, sw, alto_vis - 20, relleno=BLANCO, borde=None, redondeo=0.05)
        r = rect(g.shapes, sx + sw / 2 - 60, sy + 30, 120, 120, relleno=RGBColor(0x0B, 0x5C, 0xAD), borde=None, redondeo=0.12)
        texto(g.shapes, sx + sw / 2 - 60, sy + 30, 120, 120, "P", tam=60, negrita=True, color=BLANCO,
              alinear=PP_ALIGN.CENTER, ancla=MSO_ANCHOR.MIDDLE)
        texto(g.shapes, sx + 10, sy + 165, sw - 20, 40, "Zona con parquímetro", tam=14, negrita=True,
              color=RGBColor(0x11, 0x14, 0x18), alinear=PP_ALIGN.CENTER)
        texto(g.shapes, sx + 10, sy + 200, sw - 20, 70, "Q3 por 30 min\nParquímetro 0412", tam=12,
              color=RGBColor(0x44, 0x4A, 0x52), alinear=PP_ALIGN.CENTER)
    else:
        from PIL import Image
        ruta = pantalla(vis)
        iw, ih = Image.open(ruta).size
        h = alto_vis - 20
        w_img = h * iw / ih
        g.shapes.add_picture(ruta, px(x + (w - w_img) / 2), px(y + 40), px(w_img), px(h))
    texto(g.shapes, x + 40, TOPE - 200, w - 80, 46, tit, tam=24, negrita=True, color=ACENTO)
    texto(g.shapes, x + 40, TOPE - 148, w - 80, 120, cue, tam=16, color=SUAVE)
    G.append(g)

# ---------------------------------------------------------------- 12 prototipo
s, G, y = nueva(12, "Parte desarrollada", "El prototipo mide si llegamos al 72 % mientras se prueba")
imagen(s, os.path.join(DIAG, "4-prototipo", "prototipo-cuatro-pantallas.png"), 120, y, 1680, TOPE - y - 70)
texto(s.shapes, 120, TOPE - 40, 1680, 40, "Tarifario real de la capital · pago por placa · aviso contra el cobro informal · modo de prueba que mide el 72 %",
      tam=16, color=SUAVE, alinear=PP_ALIGN.CENTER)

# ---------------------------------------------------------------- 13 ciclo de vida
s, G, y = nueva(13, "Arquitectura en el ciclo de vida", "Se construye en espiral por fuera y con Scrum por dentro", empuje=True,
                bajada="Siete factores de la clase: la pantalla se descubre probando, cada Delegación es distinta y hay riesgos fuertes al inicio.")
g = s.shapes.add_group_shape()
for i, (t, c) in enumerate([("Espiral", "Cada vuelta empieza revisando los riesgos: legales, vandalismo y aceptación de los vecinos."),
                            ("Scrum con arquitectura", "Pasos 1, 2, 4 y 9 de la lámina: especificar y priorizar casos de uso, arquitectura base en el primer sprint y refinarla en cada sprint.")]):
    rect(g.shapes, 120 + i * 850, y, 830, 240)
    texto(g.shapes, 160 + i * 850, y + 22, 760, 50, t, tam=22, negrita=True, color=ACENTO)
    texto(g.shapes, 160 + i * 850, y + 88, 760, 115, c, tam=16, color=SUAVE)
G.append(g)
g = s.shapes.add_group_shape()
y3 = y + 262
for i, (f, c) in enumerate([("Fase 0", "Consulta en la colonia piloto y conteo de cuidacarros"),
                            ("Fase 1", "Pago por placa, verificación y multa con evidencia"),
                            ("Fase 2", "App del conductor, alarma y reportes"),
                            ("Fase 3", "Con datos: sensores y tarifa por demanda")]):
    rect(g.shapes, 120 + i * 425, y3, 400, TOPE - y3)
    texto(g.shapes, 150 + i * 425, y3 + 20, 340, 70, f, tam=26, negrita=True, color=ACENTO)
    texto(g.shapes, 150 + i * 425, y3 + 92, 340, TOPE - y3 - 100, c, tam=16)
g.efecto = "barrido"
G.append(g)

# ---------------------------------------------------------------- 14 cobros ajenos
s, G, y = nueva(14, "Factores externos", "Al cobro informal se le gana con información, datos y acuerdos")
for (x, w), ic, tit, cue in zip(COLS4, ["parking-meter", "smartphone", "shield-check", "hand-coins"],
                                ["Información", "Software", "Ciclo de vida", "Opción para la Delegación"],
                                ["La pantalla y la señal dicen que el único cobro es el del parquímetro, y cuánto es.",
                                 "Reporte sin dar el nombre. El sistema marca las cuadras llenas donde casi nadie paga.",
                                 "Antes de instalar: contar a los cuidacarros y acordar un protocolo con la PDH, como en Antigua.",
                                 "Trabajo formal de orientación al usuario, pagado con el 30 % comunitario."]):
    G.append(tarjeta(s, x, y, w, TOPE - y, icono=ic, titulo=tit, cuerpo=cue, tam_cuerpo=18, alto_titulo=46 * 2 * 1.05))

# ---------------------------------------------------------------- 15 cierre
s, G, y = nueva(15, "Cierre", "Tres ideas para llevarse")
for i, t in enumerate(["La pantalla era la mitad del problema.",
                       "Lo que faltaba ya estaba en el equipo.",
                       "Lo que se cobra se publica: sin confianza no hay sistema."]):
    yy = y + 30 + i * 180
    texto(s.shapes, 120, yy, 120, 150, str(i + 1), tam=66, negrita=True, color=ACENTO, interlineado=1.0)
    texto(s.shapes, 280, yy + 20, 1520, 150, t, tam=32, negrita=True)
texto(s.shapes, 120, TOPE - 50, 1600, 50, "Gracias. ¿Preguntas?", tam=24, color=SUAVE)


# ======================================================================= animacion
def timing_xml(objetivos):
    """objetivos: [(spid, efecto)] con efecto «subir» (desvanecido con subida) o «barrido» (de izquierda
    a derecha, para lo que se lee en ese sentido: un flujo, una linea de tiempo)."""
    n = [2]

    def nid():
        n[0] += 1
        return n[0]
    clics = []
    for sp, tipo in objetivos:
        dest = '<p:tgtEl><p:spTgt spid="%d"/></p:tgtEl>' % sp
        if tipo == "barrido":
            efecto = (
                '<p:par><p:cTn id="%d" presetID="22" presetClass="entr" presetSubtype="8" fill="hold" nodeType="clickEffect">'
                '<p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>'
                '<p:set><p:cBhvr><p:cTn id="%d" dur="1" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst></p:cTn>'
                '%s<p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst>'
                '</p:cBhvr><p:to><p:strVal val="visible"/></p:to></p:set>'
                '<p:animEffect transition="in" filter="wipe(left)"><p:cBhvr><p:cTn id="%d" dur="700"/>%s</p:cBhvr></p:animEffect>'
                '</p:childTnLst></p:cTn></p:par>' % (nid(), nid(), dest, nid(), dest))
            clics.append(
                '<p:par><p:cTn id="%d" fill="hold"><p:stCondLst><p:cond delay="indefinite"/></p:stCondLst><p:childTnLst>'
                '<p:par><p:cTn id="%d" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>%s'
                '</p:childTnLst></p:cTn></p:par></p:childTnLst></p:cTn></p:par>' % (nid(), nid(), efecto))
            continue
        efecto = (
            '<p:par><p:cTn id="%d" presetID="42" presetClass="entr" presetSubtype="0" fill="hold" nodeType="clickEffect">'
            '<p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>'
            '<p:set><p:cBhvr><p:cTn id="%d" dur="1" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst></p:cTn>'
            '%s<p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst>'
            '</p:cBhvr><p:to><p:strVal val="visible"/></p:to></p:set>'
            '<p:animEffect transition="in" filter="fade"><p:cBhvr><p:cTn id="%d" dur="500"/>%s</p:cBhvr></p:animEffect>'
            '<p:anim calcmode="lin" valueType="num"><p:cBhvr><p:cTn id="%d" dur="500" fill="hold"/>%s'
            '<p:attrNameLst><p:attrName>ppt_x</p:attrName></p:attrNameLst></p:cBhvr><p:tavLst>'
            '<p:tav tm="0"><p:val><p:strVal val="#ppt_x"/></p:val></p:tav>'
            '<p:tav tm="100000"><p:val><p:strVal val="#ppt_x"/></p:val></p:tav></p:tavLst></p:anim>'
            '<p:anim calcmode="lin" valueType="num"><p:cBhvr><p:cTn id="%d" dur="500" decel="100000" fill="hold"/>%s'
            '<p:attrNameLst><p:attrName>ppt_y</p:attrName></p:attrNameLst></p:cBhvr><p:tavLst>'
            '<p:tav tm="0"><p:val><p:strVal val="#ppt_y+.06"/></p:val></p:tav>'
            '<p:tav tm="100000"><p:val><p:strVal val="#ppt_y"/></p:val></p:tav></p:tavLst></p:anim>'
            '</p:childTnLst></p:cTn></p:par>'
            % (nid(), nid(), dest, nid(), dest, nid(), dest, nid(), dest))
        clics.append(
            '<p:par><p:cTn id="%d" fill="hold"><p:stCondLst><p:cond delay="indefinite"/></p:stCondLst><p:childTnLst>'
            '<p:par><p:cTn id="%d" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>%s'
            '</p:childTnLst></p:cTn></p:par></p:childTnLst></p:cTn></p:par>' % (nid(), nid(), efecto))
    return ('<p:timing xmlns:p="%s"><p:tnLst><p:par><p:cTn id="1" dur="indefinite" restart="never" nodeType="tmRoot">'
            '<p:childTnLst><p:seq concurrent="1" nextAc="seek"><p:cTn id="2" dur="indefinite" nodeType="mainSeq">'
            '<p:childTnLst>%s</p:childTnLst></p:cTn>'
            '<p:prevCondLst><p:cond evt="onPrev" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:prevCondLst>'
            '<p:nextCondLst><p:cond evt="onNext" delay="0"><p:tgtEl><p:sldTgt/></p:tgtEl></p:cond></p:nextCondLst>'
            '</p:seq></p:childTnLst></p:cTn></p:par></p:tnLst></p:timing>' % (P_NS, "".join(clics)))


# --- guion: el texto citado de cada "## N · Titulo · Orador · reloj"
guion, orador, titulos, bloques, reloj = {}, {}, {}, {}, {}
actual = None
for linea in open(GUION, encoding="utf-8").read().split("\n"):
    m = re.match(r"^## Diapositiva (\d+) · (.+?) · (\w+) · ([\d:]+)", linea)
    if m:
        actual = int(m.group(1))
        guion[actual], titulos[actual], orador[actual] = [], m.group(2), m.group(3)
        reloj[actual] = m.group(4)
        bloques[actual] = [linea]
    elif linea.startswith("## "):
        actual = None
    elif actual:
        bloques[actual].append(linea)
        if linea.startswith(">"):
            guion[actual].append(linea[1:].strip())

# lo que se ve en pantalla: el guion tiene que nombrar cada diapositiva con su antetitulo y su titular,
# si no el orador no sabe que parte le toca
pantalla = {}
for num, (slide, grupos, empuje) in enumerate(LAMINAS, 1):
    d = {sh.name: sh.text_frame.text for sh in slide.shapes if sh.has_text_frame}
    pantalla[num] = (d.get("!!antetitulo", "PORTADA"), d.get("!!titulo", "Repensando los parquímetros"))
    linea = "**Página %d de %d** · en pantalla: «%s»" % (num, len(LAMINAS), pantalla[num][1])
    if titulos.get(num) != pantalla[num][0] or linea not in bloques.get(num, []):
        raise SystemExit("diapositiva %d: el guion no coincide con la pantalla (%s · «%s»)" % ((num,) + pantalla[num]))

informe = []
for num, (slide, grupos, empuje) in enumerate(LAMINAS, 1):
    clics_guion = sum(l.count("(clic)") for l in guion.get(num, []))
    if clics_guion != len(grupos):
        raise SystemExit("lámina %d: %d grupos animados y %d «(clic)» en el guion" % (num, len(grupos), clics_guion))
    sld = slide._element
    # Morph en PowerPoint 2019 o posterior; Keynote lo importa como Movimiento magico (verificado el
    # 2026-10-19 exportando a video). Las versiones viejas toman el desvanecido de respaldo.
    sld.append(etree.fromstring(
        '<mc:AlternateContent xmlns:mc="http://schemas.openxmlformats.org/markup-compatibility/2006">'
        '<mc:Choice xmlns:p159="http://schemas.microsoft.com/office/powerpoint/2015/09/main" Requires="p159">'
        '<p:transition xmlns:p="%s" spd="med"><p159:morph option="byObject"/></p:transition></mc:Choice>'
        '<mc:Fallback><p:transition xmlns:p="%s" spd="med"><p:fade/></p:transition></mc:Fallback>'
        '</mc:AlternateContent>' % (P_NS, P_NS)))
    if grupos:
        sld.append(etree.fromstring(timing_xml([(g.shape_id, getattr(g, "efecto", "subir")) for g in grupos])))
    # Sin notas del orador: el guion va en archivos aparte (guion general y uno por integrante),
    # asi el .pptx que se entrega no lleva comentarios.
    informe.append((num, "morph", len(grupos), orador.get(num, "")))

prs.core_properties.author = "Santiago Barrera"
prs.core_properties.last_modified_by = "Santiago Barrera"
prs.core_properties.title = "Repensando los parquímetros: SIEP"
import datetime
prs.core_properties.created = prs.core_properties.modified = datetime.datetime(2026, 10, 19, 9, 0)
prs.save(SALIDA)

# --- un guion por integrante, con sus laminas completas y las de entrada y salida
carpeta = os.path.join(TAREAS, "guiones-caso-parquimetros")
os.makedirs(carpeta, exist_ok=True)
ROLES = {"Santiago": ("Santiago Julián Barrera Reyes", "Scrum Master / coordinador"),
         "Jemima": ("Jemima Solmaira Chavajay Quiejú", "Product Owner"),
         "Byron": ("Byron Josué Par Rancho", "Equipo de desarrollo")}
RECORTE_10 = {"Santiago": "la 13 se reduce a las cuatro fases; hablás de 0:00 a 2:30 y de 8:00 a 10:00.",
              "Jemima": "se omite la 12 (el prototipo se menciona en la 11); hablás de 2:30 a 4:00 y de 6:30 a 8:00.",
              "Byron": "se omite la 9 (el despliegue se nombra en la 8); hablás de 4:00 a 6:30."}


def segundos(r):
    m, s = r.split(":")
    return int(m) * 60 + int(s)


def minutos(seg):
    return "%d:%02d" % (seg // 60, seg % 60)


for quien, (nombre, rol) in ROLES.items():
    mias = [n for n in sorted(orador) if orador[n] == quien]
    out = ["---", "tema: Guion de presentación", "fuente: \"Generado por 06-Proyecto-MCP/generar-presentacion-parq.py "
           "desde Guion - Presentación Caso Parquímetros.md\"", "fecha: 2026-10-19", "tarea: Tarea 3 - Caso Parquímetros",
           "---", "", "# Guion de %s · %s" % (nombre, rol), "",
           "## Tus diapositivas", "",
           "| Diapositiva | Arriba dice | Titular en pantalla | Empieza en | Dura |", "|---|---|---|---|---|"]
    for n in mias:
        fin = segundos(reloj[n + 1]) if n + 1 in reloj else 15 * 60
        out.append("| **%d** | %s | %s | %s | %s |" % (n, pantalla[n][0], pantalla[n][1], reloj[n],
                                                     minutos(fin - segundos(reloj[n]))))
    total = sum((segundos(reloj[n + 1]) if n + 1 in reloj else 15 * 60) - segundos(reloj[n]) for n in mias)
    out += ["", "Hablás **%s** de los 15 minutos. Si dan 10 minutos: %s" % (minutos(total), RECORTE_10[quien]), "",
           "**Antes de hablar:** quién te pasa la palabra y con qué frase; **al terminar:** a quién se la pasás.", ""]
    for n in mias:
        prev = orador.get(n - 1)
        if prev and prev != quien:
            out.append("> *Entra después de %s (diapositiva %d).*\n" % (prev, n - 1))
        out += bloques[n]
        nxt = orador.get(n + 1)
        if nxt and nxt != quien:
            out.append("> *Al terminar, le pasa la palabra a %s (diapositiva %d).*\n" % (nxt, n + 1))
    out += ["", "## Preguntas que te tocan", ""]
    tabla = open(GUION, encoding="utf-8").read().split("## Preguntas probables y quién responde")[1].split("## Si dan")[0]
    filas = [l for l in tabla.strip().split("\n")[2:] if l.split("|")[2].strip().startswith(quien)]
    out += ["| Pregunta | Respuesta | Dónde está en el PDF |", "|---|---|---|"] + filas
    open(os.path.join(carpeta, "Guion - %s.md" % quien), "w", encoding="utf-8").write("\n".join(out) + "\n")

print("lámina  transición  clics  orador")
for r in informe:
    print("  %2d     %-9s   %d      %s" % r)
print("clics en total:", sum(r[2] for r in informe))
print("pptx:", SALIDA)
