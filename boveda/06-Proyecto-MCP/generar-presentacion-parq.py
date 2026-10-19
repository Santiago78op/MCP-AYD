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


def cabecera(slide, n, antetitulo, titulo):
    fondo(slide)
    texto(slide.shapes, 120, 84, 1400, 34, antetitulo.upper(), tam=15, color=ACENTO, negrita=True)
    texto(slide.shapes, 120, 126, 1680, 100, titulo, tam=38, negrita=True, interlineado=1.0)
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
            alto_titulo=None):
    """Una tarjeta = un grupo: fondo, icono, numero grande, titulo y cuerpo, apilados con su alto real."""
    g = slide.shapes.add_group_shape()
    rect(g.shapes, x, y, w, h)
    cw, cy = w - 80, y + 36
    if icono:
        g.shapes.add_picture(icono_png(icono), px(x + 40), px(cy), px(64), px(64))
        cy += 92
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
    if lineas(titulo, 1680, 38, True) > 1:
        raise SystemExit("lámina %d: el título %r ocupa más de una línea" % (n, titulo))
    s = prs.slides.add_slide(VACIA)
    cabecera(s, n, antetitulo, titulo)
    y = 250
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
s, G, y = nueva(2, "El caso", "SERVIparq quiere que el cajón rote",
                bajada="Ciudad de México, 2012. Un cajón de estacionamiento vale hasta **200 mil pesos**: la meta es que lo usen muchos conductores, no uno solo.")
(x1, w1), (x2, w2), (x3, w3) = COLS3
G.append(tarjeta(s, x1, y, w1, TOPE - y, grande="70 / 30", titulo="Así se reparte lo cobrado",
                 cuerpo="70 % para operar y mantener los equipos.\n30 % se reinvierte en la comunidad."))
G.append(tarjeta(s, x2, y, w2, TOPE - y, grande="6", titulo="problemas en el diagnóstico",
                 cuerpo="Vecinos no consultados, cuidacarros, instrucciones confusas, reclamos sin respuesta, falta de personal y desconfianza."))
G.append(tarjeta(s, x3, y, w3, TOPE - y, icono="users", titulo="Smartmedia mide con personas",
                 cuerpo="Pide tareas reales con el parquímetro y mide si la gente encuentra y entiende la información. Hasta recrearon una calle en una sala."))

# ---------------------------------------------------------------- 3 Guatemala
s, G, y = nueva(3, "Investigación", "Guatemala: el cobro y los cuidacarros")
tarjeta(s, x1, y, w1, TOPE - y, grande="Q3", titulo="por cada 30 minutos",
        cuerpo="Acuerdo COM-40-2022 de la Municipalidad de Guatemala, vigente desde febrero de 2024. Banqueta por colores: blanco se puede, rojo no. EMETRA anunció pago por aplicación.")
G.append(tarjeta(s, x2, y, w2, TOPE - y, grande="2,500", titulo="objetos que apartaban lugares",
                 cuerpo="Retirados en un operativo de la Policía Municipal de Tránsito (2023). Cobrar por dejar estacionar podría ser extorsión: se denuncia al 1551. Zona 13, abril de 2026: 33 personas cobraban entre Q35 y US$50."))
G.append(tarjeta(s, x3, y, w3, TOPE - y, grande="Q12 M", titulo="cobró MarbEx en 2025, Antigua Guatemala",
                 cuerpo="Marbete digital por placa: Q7 M en 2024. En 2026 la Corte de Constitucionalidad suspendió la base de datos de placas y la multa de Q500."))

# ---------------------------------------------------------------- 4 problemas
s, G, y = nueva(4, "Los seis problemas", "Tres problemas no son de pantalla", empuje=True)
for (x, w), ic, tit, cue in zip(COLS4, ["users", "map-pin", "wrench", "hand-coins"],
                                ["Gobierno", "Información", "Capacidad", "Cobro informal"],
                                ["P-01 Vecinos no consultados.\nP-06 Nadie ve a dónde va el dinero.",
                                 "P-03 Instrucciones confusas y solo monedas.\nP-04 No se sabe cómo reclamar una multa.",
                                 "P-05 Falta personal. El equipo ya podía cobrar con tarjeta y avisar vandalismo: estaba apagado.",
                                 "P-02 Cuidacarros («franeleros» en el caso): apartan el lugar y cobran por él."]):
    G.append(tarjeta(s, x, y, w, TOPE - y, icono=ic, titulo=tit, cuerpo=cue, tam_cuerpo=18, alto_titulo=46 * 2 * 1.05))

# ---------------------------------------------------------------- 5 el 72 %
s, G, y = nueva(5, "Requisitos de desempeño", "Qué debe lograr el conductor")
for i, (t, c) in enumerate([("Antes del uso", "Encontrar la zona, un cajón y su parquímetro"),
                            ("Durante", "Entender tarifa y tiempo máximo, y pagar"),
                            ("Después", "Saber cuándo vence y cómo reclamar")]):
    rect(s.shapes, 120 + i * 570, y, 540, 165)
    texto(s.shapes, 150 + i * 570, y + 22, 480, 44, t, tam=20, negrita=True)
    texto(s.shapes, 150 + i * 570, y + 70, 480, 70, c, tam=16, color=SUAVE)
y2 = y + 195
G.append(tarjeta(s, 120, y2, 820, TOPE - y2, grande="72 %", tam_grande=80, titulo="el nivel que acordaron",
                 cuerpo="80 % encuentra la información (va con prisa)\n× 90 % la usa bien\n= 72 % completa la tarea."))
g = s.shapes.add_group_shape()
rect(g.shapes, 980, y2, 820, TOPE - y2)
texto(g.shapes, 1020, y2 + 36, 740, 50, "Un número por tarea", tam=22, negrita=True)
for i, (t, v) in enumerate([("Pagar por placa (si falla, multa injusta)", "81 %"),
                            ("Entender la tarifa", "72 %"), ("Saber cómo reclamar", "72 %"),
                            ("Ubicar el número del parquímetro", "64 %")]):
    yy = y2 + 110 + i * 82
    texto(g.shapes, 1020, yy, 560, 76, t, tam=17, color=SUAVE, ancla=MSO_ANCHOR.MIDDLE)
    texto(g.shapes, 1590, yy, 170, 76, v, tam=30, negrita=True, color=ACENTO, alinear=PP_ALIGN.RIGHT, ancla=MSO_ANCHOR.MIDDLE)
G.append(g)

# ---------------------------------------------------------------- 6 el negocio
s, G, y = nueva(6, "Caso de negocio", "El negocio y sus cinco procesos", empuje=True)
texto(s.shapes, 120, y, 600, TOPE - y,
      "**Negocio:** gestionar el estacionamiento en la calle.\n\n"
      "**Actores:** conductor, comité vecinal, Delegación, oficial de tránsito, banco y proveedor del parquímetro.\n\n"
      "**Trabajadores:** el verificador y el personal de SERVIparq.\n\n"
      "**No es actor:** el cuidacarros. No participa de forma legal, pero el diseño lo toma en cuenta.",
      tam=18, color=SUAVE, interlineado=1.15)
G.append(imagen(s, svg_png("1-caso-negocio/cdu-descomposicion-parq.svg"), 780, y, 1020, TOPE - y))

# ---------------------------------------------------------------- 7 alternativas
s, G, y = nueva(7, "Posibles soluciones", "Cuatro alternativas, una combinación")
for (x, w), tag, tit, cue in zip(COLS4, ["DENTRO", "NÚCLEO", "DESPUÉS", "ALREDEDOR"],
                                 ["S-1 Rediseñar solo la información", "S-2 Pago por placa, conectado",
                                  "S-3 Sensores y tarifa por demanda", "S-4 Gobierno comunitario"],
                                 ["Barato y rápido. No resuelve la falta de personal ni la desconfianza.",
                                  "Monedas, tarjeta o celular con el equipo ya comprado. Ataca 5 de los 6 problemas.",
                                  "Como San Francisco. Caro, expuesto al vandalismo y sin datos todavía.",
                                  "Consulta previa, tablero público y protocolo con los cuidacarros."]):
    g = tarjeta(s, x, y, w, TOPE - y, titulo=tit, cuerpo=cue, tam_cuerpo=18, alto_titulo=46 * 3 * 1.05)
    texto(g.shapes, x + 40, TOPE - 80, w - 80, 44, tag, tam=20, negrita=True, color=ACENTO)
    G.append(g)

# ---------------------------------------------------------------- 8 arquitectura
s, G, y = nueva(8, "Arquitectura del software", "Un servicio por proceso, con eventos")
for i, t in enumerate(["Zonas y comunidad", "Cobro por placa", "Verificación y sanción", "Transparencia", "Red y mantenimiento"]):
    rect(s.shapes, 120, y + i * 96, 580, 80)
    texto(s.shapes, 150, y + i * 96, 530, 80, "**CDU-0%d**  %s" % (i + 1, t), tam=17, ancla=MSO_ANCHOR.MIDDLE)
G.append(imagen(s, svg_png("3-arquitectura/bloques-parq.svg"), 780, y, 1020, 500))
g = s.shapes.add_group_shape()
for i, t in enumerate(["El pago queda en la placa: no hay boleto", "Se encienden el pago con tarjeta y la alarma",
                       "La multa nace solo si el oficial la confirma", "Todo lo cobrado se publica"]):
    rect(g.shapes, 120 + i * 425, TOPE - 150, 400, 150)
    texto(g.shapes, 150 + i * 425, TOPE - 150, 340, 150, t, tam=17, negrita=True, ancla=MSO_ANCHOR.MIDDLE)
G.append(g)

# ---------------------------------------------------------------- 9 despliegue
s, G, y = nueva(9, "Despliegue", "Dónde corre cada parte")
imagen(s, svg_png("3-arquitectura/despliegue-parq.svg", 3000), 120, y, 1680, TOPE - y)

# ---------------------------------------------------------------- 10 calidad
s, G, y = nueva(10, "Calidad del software", "Los números que nos comprometemos", empuje=True)
for (x, w), gr, tit, cue in zip(COLS4, ["72 %", "2 s", "0", "100 %"],
                                ["Eficacia", "Rendimiento", "Disponibilidad", "Seguridad"],
                                ["de los conductores paga sin ayuda la primera vez (calidad en uso, ISO 9126).",
                                 "para que el verificador sepa si una placa pagó, en 95 de cada 100 consultas.",
                                 "pagos perdidos aunque se caiga la señal: el equipo guarda y reenvía.",
                                 "de las multas con foto, hora, ubicación y confirmación del oficial."]):
    G.append(tarjeta(s, x, y, w, TOPE - y, grande=gr, tam_grande=52, titulo=tit, cuerpo=cue, tam_cuerpo=18))

# ---------------------------------------------------------------- 11 arquitectura de la informacion
s, G, y = nueva(11, "Arquitectura de la información", "La información, por momento de uso",
                bajada="Organizar y nombrar los contenidos para que la persona encuentre lo que busca. No es la arquitectura del software.")
for (x, w), ic, tit, cue in zip(COLS3, ["map-pin", "parking-meter", "bell"], ["Antes", "Durante", "Después"],
                                ["Señal con el color de la banqueta.\nMapa de la zona en la app.\nNúmero grande del parquímetro.",
                                 "Tres pasos: placa, tiempo y pago.\nLa tarifa siempre arriba.\n«Este es el único cobro».",
                                 "Comprobante con folio y hora de vencimiento.\nAviso 10 min antes.\nCómo reclamar o reportar un cobro."]):
    G.append(tarjeta(s, x, y, w, TOPE - y, icono=ic, titulo=tit, cuerpo=cue, tam_cuerpo=19))

# ---------------------------------------------------------------- 12 prototipo
s, G, y = nueva(12, "Parte desarrollada", "Prototipo: la pantalla del parquímetro")
imagen(s, os.path.join(DIAG, "4-prototipo", "prototipo-cuatro-pantallas.png"), 120, y, 1680, TOPE - y - 70)
texto(s.shapes, 120, TOPE - 40, 1680, 40, "Tarifario real de la capital · pago por placa · aviso contra el cobro informal · modo de prueba que mide el 72 %",
      tam=16, color=SUAVE, alinear=PP_ALIGN.CENTER)

# ---------------------------------------------------------------- 13 ciclo de vida
s, G, y = nueva(13, "Arquitectura en el ciclo de vida", "Espiral por fuera, Scrum por dentro", empuje=True,
                bajada="Siete factores de la clase: la pantalla se descubre probando, cada Delegación es distinta y hay riesgos fuertes al inicio.")
g = s.shapes.add_group_shape()
for i, (t, c) in enumerate([("Espiral", "Cada vuelta empieza revisando los riesgos: legales, vandalismo y aceptación de los vecinos."),
                            ("Scrum con arquitectura", "Pasos 1, 2, 4 y 9 de la lámina: especificar y priorizar casos de uso, arquitectura base en el primer sprint y refinarla en cada sprint.")]):
    rect(g.shapes, 120 + i * 850, y, 830, 250)
    texto(g.shapes, 160 + i * 850, y + 28, 760, 50, t, tam=24, negrita=True, color=ACENTO)
    texto(g.shapes, 160 + i * 850, y + 90, 760, 150, c, tam=18, color=SUAVE)
G.append(g)
g = s.shapes.add_group_shape()
y3 = y + 280
for i, (f, c) in enumerate([("Fase 0", "Consulta en la colonia piloto y conteo de cuidacarros"),
                            ("Fase 1", "Pago por placa, verificación y multa con evidencia"),
                            ("Fase 2", "App del conductor, alarma y reportes"),
                            ("Fase 3", "Con datos: sensores y tarifa por demanda")]):
    rect(g.shapes, 120 + i * 425, y3, 400, TOPE - y3)
    texto(g.shapes, 150 + i * 425, y3 + 28, 340, 70, f, tam=30, negrita=True, color=ACENTO)
    texto(g.shapes, 150 + i * 425, y3 + 100, 340, TOPE - y3 - 120, c, tam=18)
G.append(g)

# ---------------------------------------------------------------- 14 cobros ajenos
s, G, y = nueva(14, "Factores externos", "Ganarle al cobro informal")
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
def timing_xml(ids):
    n = [2]

    def nid():
        n[0] += 1
        return n[0]
    clics = []
    for sp in ids:
        dest = '<p:tgtEl><p:spTgt spid="%d"/></p:tgtEl>' % sp
        efecto = (
            '<p:par><p:cTn id="%d" presetID="42" presetClass="entr" presetSubtype="0" fill="hold" nodeType="clickEffect">'
            '<p:stCondLst><p:cond delay="0"/></p:stCondLst><p:childTnLst>'
            '<p:set><p:cBhvr><p:cTn id="%d" dur="1" fill="hold"><p:stCondLst><p:cond delay="0"/></p:stCondLst></p:cTn>'
            '%s<p:attrNameLst><p:attrName>style.visibility</p:attrName></p:attrNameLst>'
            '</p:cBhvr><p:to><p:strVal val="visible"/></p:to></p:set>'
            '<p:animEffect transition="in" filter="fade"><p:cBhvr><p:cTn id="%d" dur="600"/>%s</p:cBhvr></p:animEffect>'
            '<p:anim calcmode="lin" valueType="num"><p:cBhvr><p:cTn id="%d" dur="600" fill="hold"/>%s'
            '<p:attrNameLst><p:attrName>ppt_x</p:attrName></p:attrNameLst></p:cBhvr><p:tavLst>'
            '<p:tav tm="0"><p:val><p:strVal val="#ppt_x"/></p:val></p:tav>'
            '<p:tav tm="100000"><p:val><p:strVal val="#ppt_x"/></p:val></p:tav></p:tavLst></p:anim>'
            '<p:anim calcmode="lin" valueType="num"><p:cBhvr><p:cTn id="%d" dur="600" decel="100000" fill="hold"/>%s'
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
guion, orador, titulos, bloques = {}, {}, {}, {}
actual = None
for linea in open(GUION, encoding="utf-8").read().split("\n"):
    m = re.match(r"^## (\d+) · (.+?) · (\w+) · ([\d:]+)", linea)
    if m:
        actual = int(m.group(1))
        guion[actual], titulos[actual], orador[actual] = [], m.group(2), m.group(3)
        bloques[actual] = [linea]
    elif linea.startswith("## "):
        actual = None
    elif actual:
        bloques[actual].append(linea)
        if linea.startswith(">"):
            guion[actual].append(linea[1:].strip())

informe = []
for num, (slide, grupos, empuje) in enumerate(LAMINAS, 1):
    clics_guion = sum(l.count("(clic)") for l in guion.get(num, []))
    if clics_guion != len(grupos):
        raise SystemExit("lámina %d: %d grupos animados y %d «(clic)» en el guion" % (num, len(grupos), clics_guion))
    sld = slide._element
    trans = etree.fromstring('<p:transition xmlns:p="%s" spd="med">%s</p:transition>'
                             % (P_NS, '<p:push dir="l"/>' if empuje else '<p:fade/>'))
    sld.append(trans)
    if grupos:
        sld.append(etree.fromstring(timing_xml([g.shape_id for g in grupos])))
    notas = "\n".join(guion.get(num, [])).replace("*(clic)*", "[CLIC]")
    slide.notes_slide.notes_text_frame.text = "%s · %s\n\n%s" % (orador.get(num, ""), titulos.get(num, ""),
                                                                 re.sub(r"\*+", "", notas))
    informe.append((num, "empuje" if empuje else "fundido", len(grupos), orador.get(num, "")))

prs.core_properties.author = "Santiago Barrera"
prs.core_properties.last_modified_by = "Santiago Barrera"
prs.core_properties.title = "Repensando los parquímetros: SIEP"
prs.save(SALIDA)

# --- un guion por integrante, con sus laminas completas y las de entrada y salida
carpeta = os.path.join(TAREAS, "guiones-caso-parquimetros")
os.makedirs(carpeta, exist_ok=True)
ROLES = {"Santiago": ("Santiago Julián Barrera Reyes", "Scrum Master / coordinador"),
         "Jemima": ("Jemima Solmaira Chavajay Quiejú", "Product Owner"),
         "Byron": ("Byron Josué Par Rancho", "Equipo de desarrollo")}
for quien, (nombre, rol) in ROLES.items():
    mias = [n for n in sorted(orador) if orador[n] == quien]
    out = ["---", "tema: Guion de presentación", "fuente: \"Generado por 06-Proyecto-MCP/generar-presentacion-parq.py "
           "desde Guion - Presentación Caso Parquímetros.md\"", "fecha: 2026-10-19", "tarea: Tarea 3 - Caso Parquímetros",
           "---", "", "# Guion de %s · %s" % (nombre, rol), "",
           "Láminas a cargo: %s. Reloj total de la presentación: 15 minutos." % ", ".join(str(n) for n in mias), "",
           "**Antes de hablar:** quién te pasa la palabra y con qué frase; **al terminar:** a quién se la pasás.", ""]
    for n in mias:
        prev = orador.get(n - 1)
        if prev and prev != quien:
            out.append("> *Entra después de %s (lámina %d).*\n" % (prev, n - 1))
        out += bloques[n]
        nxt = orador.get(n + 1)
        if nxt and nxt != quien:
            out.append("> *Al terminar, le pasa la palabra a %s (lámina %d).*\n" % (nxt, n + 1))
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
