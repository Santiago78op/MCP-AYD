#!/usr/bin/env python3
"""
generar-excalidraw.py — construye archivos .excalidraw con coordenadas explícitas.

Existe porque es la ÚNICA vía programable para controlar el layout de un diagrama
(ver 06-Proyecto-MCP/estilo-diagramas.md §5, palanca 3): el MCP de StarUML no
tiene herramientas de posicionamiento.

Respeta las convenciones de estilo de esa guía: retícula de 20 px, roughness 0,
trazo #1e1e1e, Helvetica, y los tamaños estándar por elemento.

Uso:
    python generar-excalidraw.py <nombre-del-diagrama>
    python generar-excalidraw.py <nombre-de-carpeta>    (genera el lote entero)
    python generar-excalidraw.py --referencia          (refresca practica/ y examen/)
    python generar-excalidraw.py --referencia examen   (solo una de las dos)

Cada lamina se escribe en ../02-Diagramas/<carpeta>/, donde la carpeta es la
SECCION DE LA ENTREGA que la usa (2-caso-negocio, 3.1-drivers-rf,
3.2-drivers-calidad, 3.3-drivers-restriccion, 3.4-priorizacion,
4-matrices-trazabilidad) o `ejemplos-clase` para los casos de otro dominio.
Correr sin argumento lista lo disponible.
"""

import json
import math
import os
import shutil
import sys

# --------------------------------------------------------------------------
# Convenciones de estilo (estilo-diagramas.md §5)
# --------------------------------------------------------------------------
TRAZO = "#1e1e1e"
FONDO_SISTEMA = "#f5f5f5"
FUENTE = 2          # Helvetica
GRID = 20

_contador = [0]


def _base(tipo, x, y, w, h, **kw):
    _contador[0] += 1
    n = _contador[0]
    el = {
        "id": f"el{n:03d}",
        "type": tipo,
        "x": x, "y": y, "width": w, "height": h,
        "angle": 0,
        "strokeColor": TRAZO,
        "backgroundColor": "transparent",
        "fillStyle": "solid",
        "strokeWidth": 1,
        "strokeStyle": "solid",
        "roughness": 0,
        "opacity": 100,
        "groupIds": [],
        "frameId": None,
        "roundness": None,
        "seed": 100000 + n * 7919,
        "version": 1,
        "versionNonce": 200000 + n * 6151,
        "isDeleted": False,
        "boundElements": None,
        "updated": 1,
        "link": None,
        "locked": False,
    }
    el.update(kw)
    return el


def texto(t, x, y, w, tam=16, align="center", **kw):
    """Texto autónomo, alineado dentro de un ancho dado."""
    lineas = t.split("\n")
    alto = int(tam * 1.25 * len(lineas))
    return _base("text", x, y, w, alto,
                 text=t, originalText=t,
                 fontSize=tam, fontFamily=FUENTE,
                 textAlign=align, verticalAlign="top",
                 containerId=None, lineHeight=1.25, autoResize=False, **kw)


def elipse(x, y, w, h, etiqueta, tam=16):
    """Caso de uso: elipse + su nombre centrado."""
    e = _base("ellipse", x, y, w, h)
    lineas = etiqueta.split("\n")
    ty = y + h / 2 - (tam * 1.25 * len(lineas)) / 2
    return [e, texto(etiqueta, x, int(ty), w, tam)]


def caja(x, y, w, h, etiqueta, fondo="transparent", grosor=1, tam=16):
    """Rectángulo con su rótulo centrado arriba."""
    r = _base("rectangle", x, y, w, h,
              backgroundColor=fondo, strokeWidth=grosor,
              roundness={"type": 3})
    return [r, texto(etiqueta, x, y + 12, w, tam)]


# --------------------------------------------------------------------------
# Tablas
#
# Excalidraw NO tiene elemento tabla: una tabla es una rejilla de rectangulos
# con texto encima. Por eso el ancho de cada columna se fija aca a mano y el
# texto se parte a mano — es la palanca 3 de estilo-diagramas.md §5
# (coordenadas explicitas), la unica via programable de controlar el layout.
# --------------------------------------------------------------------------
ANCHO_CARACTER = 0.52   # Helvetica: ancho medio de caracter, en fracciones del tamaño


def _partir(t, ancho_px, tam):
    """Parte un texto en las lineas que caben en ancho_px, por palabras."""
    maxc = max(1, int(ancho_px / (tam * ANCHO_CARACTER)))
    lineas = []
    for parrafo in str(t).split("\n"):
        palabras = parrafo.split()
        if not palabras:
            lineas.append("")
            continue
        actual = palabras[0]
        for pal in palabras[1:]:
            if len(actual) + 1 + len(pal) <= maxc:
                actual += " " + pal
            else:
                lineas.append(actual)
                actual = pal
        lineas.append(actual)
    return lineas


def _a_reticula(v, paso=GRID):
    """Redondea hacia arriba a la retícula de 20 px (estilo-diagramas.md §5)."""
    return int(-(-v // paso) * paso)


def tabla(x, y, columnas, filas, tam=13, pad=12,
          fondo_encabezado=FONDO_SISTEMA, destacar=(), alineaciones=None):
    """Rejilla de celdas.

    columnas:     [(titulo, ancho_px)]
    filas:        [[celda, celda, ...]]  — una celda por columna
    destacar:     indices de fila (0-based sobre `filas`) que van sombreados;
                  se usa para la MEDIDA, que es la parte que convierte el
                  deseo en driver y tiene que saltar a la vista.
    alineaciones: "left" | "center" por columna. Por omision todo a la
                  izquierda; las matrices centran las columnas de marca,
                  que llevan una sola X o i.

    Devuelve (elementos, alto_total).
    """
    els = []
    anchos = [a for _, a in columnas]
    alin = list(alineaciones) if alineaciones else ["left"] * len(columnas)
    cursor = y
    bloques = [[t for t, _ in columnas]] + [list(f) for f in filas]

    for n, fila in enumerate(bloques):
        encabezado = n == 0
        resaltada = (not encabezado) and (n - 1) in destacar
        partidas = [_partir(c, anchos[i] - 2 * pad, tam)
                    for i, c in enumerate(fila)]
        alto = _a_reticula(max(len(pz) for pz in partidas) * tam * 1.25 + 2 * pad)
        cx = x
        for i, lineas in enumerate(partidas):
            fondo = fondo_encabezado if (encabezado or resaltada) else "transparent"
            els.append(_base("rectangle", cx, cursor, anchos[i], alto,
                             backgroundColor=fondo))
            ty = cursor + (alto - len(lineas) * tam * 1.25) / 2
            if alin[i] == "center":
                tx, tw = cx, anchos[i]
            else:
                tx, tw = cx + pad, anchos[i] - 2 * pad
            els.append(texto("\n".join(lineas), tx, int(ty), tw, tam,
                             align=alin[i], _halo=False))
            cx += anchos[i]
        cursor += alto

    return els, cursor - y


def matriz(x, y, etiqueta_esquina, ancho_etiqueta, encabezados, ancho_col,
           filas, tam=13):
    """Matriz de trazabilidad: primera columna con la etiqueta de fila y el
    resto centradas, porque cada celda es una sola marca.

    encabezados: los rotulos de columna (sin la esquina)
    filas:       [(etiqueta_fila, [marca, marca, ...])]
    """
    cols = [(etiqueta_esquina, ancho_etiqueta)] + [(h, ancho_col) for h in encabezados]
    alin = ["left"] + ["center"] * len(encabezados)
    datos = [[etq] + list(marcas) for etq, marcas in filas]
    return tabla(x, y, cols, datos, tam=tam, alineaciones=alin)


def titulo(t, x, y, w, tam=20):
    """Titulo de lamina, alineado a la izquierda sobre la tabla."""
    return texto(t, x, y, w, tam, align="left", _halo=False)


def actor(x, y, nombre, tam=14):
    """Monigote UML: cabeza, tronco, brazos, piernas, nombre debajo.

    El bloque ocupa 100 x 120 (tamaño estándar de la guía §2.2).
    """
    cx = x + 50
    partes = [
        _base("ellipse", cx - 14, y, 28, 28),                                    # cabeza
        _base("line", cx, y + 28, 0, 36, points=[[0, 0], [0, 36]]),              # tronco
        _base("line", cx - 24, y + 40, 48, 0, points=[[0, 0], [48, 0]]),         # brazos
        _base("line", cx, y + 64, -20, 30, points=[[0, 0], [-20, 30]]),          # pierna izq
        _base("line", cx, y + 64, 20, 30, points=[[0, 0], [20, 30]]),            # pierna der
        texto(nombre, x - 20, y + 100, 140, tam),
    ]
    return partes


def entidad(x, y, w, h, nombre, tam=14):
    """Entidad o agente externo: rectangulo con el nombre centrado."""
    r = _base("rectangle", x, y, w, h, roundness={"type": 3})
    lineas = nombre.split("\n")
    ty = y + h / 2 - (tam * 1.25 * len(lineas)) / 2
    return [r, texto(nombre, x, int(ty), w, tam)]


def actor_negocio(x, y, nombre, tam=14):
    """Actor de NEGOCIO: monigote + barra diagonal + estereotipo textual.

    La barra diagonal sobre el hombro es el icono UML de actor de negocio;
    el estereotipo textual va arriba porque es el que siempre es valido.
    """
    cx = x + 50
    partes = [texto("\u00abactor de negocio\u00bb", x - 30, y - 24, 160, 11)]
    partes += actor(x, y, nombre, tam)
    # barra diagonal del icono de actor de negocio: al costado del torso,
    # NO sobre la cabeza (ahi se encimaria, y el paso 1 del checklist lo prohibe)
    partes.append(_base("line", cx - 38, y + 66, 26, -22,
                        points=[[0, 0], [26, -22]]))
    return partes


def elipse_negocio(x, y, w, h, etiqueta, tam=16):
    """Caso de uso de NEGOCIO: elipse + diagonal + estereotipo sobre el nombre."""
    e = _base("ellipse", x, y, w, h)
    lineas = etiqueta.split("\n")
    alto_total = 13 * 1.25 + tam * 1.25 * len(lineas)
    ty = y + h / 2 - alto_total / 2
    els = [e,
           texto("\u00abcaso de uso de negocio\u00bb", x, int(ty), w, 12),
           texto(etiqueta, x, int(ty + 17), w, tam)]
    # diagonal del icono de negocio, en la esquina inferior izquierda
    els.append(_base("line", x + w * 0.10, y + h * 0.80, 26, -20,
                     points=[[0, 0], [26, -20]]))
    return els


def linea(x1, y1, x2, y2, punta=None, punteada=False, etiqueta=None, off=(0, 0)):
    """Asociación o relación. punta: None | 'arrow' | 'triangle_outline'.

    off desplaza la etiqueta respecto del punto medio, para separar las
    etiquetas de dos flujos que corren casi paralelos.
    """
    els = [_base("arrow", x1, y1, x2 - x1, y2 - y1,
                 points=[[0, 0], [x2 - x1, y2 - y1]],
                 lastCommittedPoint=None,
                 startBinding=None, endBinding=None,
                 startArrowhead=None, endArrowhead=punta,
                 strokeStyle="dashed" if punteada else "solid",
                 elbowed=False)]
    if etiqueta:
        mx, my = (x1 + x2) / 2 + off[0], (y1 + y2) / 2 + off[1]
        els.append(texto(etiqueta, int(mx - 70), int(my - 22), 140, 12))
    return els


def envolver(elementos):
    # las claves con guion bajo son directivas para emitir_svg, no parte del
    # formato .excalidraw: se descartan antes de serializar
    limpios = [{k: v for k, v in e.items() if not k.startswith("_")}
               for e in elementos]
    return {
        "type": "excalidraw",
        "version": 2,
        "source": "generar-excalidraw.py",
        "elements": limpios,
        "appState": {
            "viewBackgroundColor": "#ffffff",
            "gridSize": GRID,
            "currentItemStrokeColor": TRAZO,
            "currentItemRoughness": 0,
            "currentItemFontFamily": FUENTE,
        },
        "files": {},
    }


# --------------------------------------------------------------------------
# Salida SVG — misma lista de elementos, vectorial y sin marca de agua
# (estilo-diagramas.md §6: se exporta SVG, no PNG)
# --------------------------------------------------------------------------
def emitir_svg(elementos, margen=40):
    xs, ys = [], []
    for e in elementos:
        xs += [e["x"], e["x"] + e["width"]]
        ys += [e["y"], e["y"] + e["height"]]
    minx, miny = min(xs) - margen, min(ys) - margen
    w = max(xs) - minx + margen
    h = max(ys) - miny + margen

    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{minx} {miny} {w} {h}" '
        f'width="{w}" height="{h}" font-family="Helvetica, Arial, sans-serif">',
        # dos marcadores distintos: la generalizacion UML es un TRIANGULO HUECO,
        # un flujo o dependencia es una flecha comun. Usar el mismo para ambos
        # cambia la semantica del diagrama.
        '<defs>'
        '<marker id="gen" viewBox="0 0 12 12" refX="11" refY="6" '
        'markerWidth="12" markerHeight="12" orient="auto">'
        f'<polygon points="0,0 12,6 0,12" fill="#ffffff" stroke="{TRAZO}" '
        'stroke-width="1"/></marker>'
        '<marker id="flecha" viewBox="0 0 10 10" refX="9" refY="5" '
        'markerWidth="9" markerHeight="9" orient="auto">'
        f'<polygon points="0,0 10,5 0,10" fill="{TRAZO}"/></marker>'
        '</defs>',
        f'<rect x="{minx}" y="{miny}" width="{w}" height="{h}" fill="#ffffff"/>',
    ]

    for e in elementos:
        t, x, y, ew, eh = e["type"], e["x"], e["y"], e["width"], e["height"]
        gr = e.get("strokeWidth", 1)
        if t == "ellipse":
            out.append(
                f'<ellipse cx="{x + ew / 2}" cy="{y + eh / 2}" rx="{ew / 2}" ry="{eh / 2}" '
                f'fill="none" stroke="{TRAZO}" stroke-width="{gr}"/>')
        elif t == "rectangle":
            fill = e.get("backgroundColor", "transparent")
            fill = "none" if fill == "transparent" else fill
            rx = 12 if e.get("roundness") else 0
            dash = ' stroke-dasharray="10 6"' if e.get("strokeStyle") == "dashed" else ""
            out.append(
                f'<rect x="{x}" y="{y}" width="{ew}" height="{eh}" rx="{rx}" '
                f'fill="{fill}" stroke="{TRAZO}" stroke-width="{gr}"{dash}/>')
        elif t == "line" and e.get("_arco"):
            cx, cy, r, lado = e["_arco"]
            p0, p1, barrido = {
                "arriba": ((cx - r, cy), (cx + r, cy), 1),
                "abajo": ((cx - r, cy), (cx + r, cy), 0),
                "izq": ((cx, cy - r), (cx, cy + r), 0),
                "der": ((cx, cy - r), (cx, cy + r), 1),
            }[lado]
            out.append(
                f'<path d="M {p0[0]} {p0[1]} A {r} {r} 0 0 {barrido} {p1[0]} {p1[1]}" '
                f'fill="none" stroke="{TRAZO}" stroke-width="{gr}"/>')
        elif t in ("line", "arrow"):
            (dx1, dy1), (dx2, dy2) = e["points"][0], e["points"][-1]
            ah = e.get("endArrowhead")
            marca = {"triangle_outline": "gen", "arrow": "flecha"}.get(ah)
            punta = f' marker-end="url(#{marca})"' if marca else ""
            dash = ' stroke-dasharray="8 6"' if e.get("strokeStyle") == "dashed" else ""
            out.append(
                f'<line x1="{x + dx1}" y1="{y + dy1}" x2="{x + dx2}" y2="{y + dy2}" '
                f'stroke="{TRAZO}" stroke-width="{gr}"{dash}{punta}/>')
        elif t == "text":
            tam = e["fontSize"]
            paso = tam * 1.25
            alin = e.get("textAlign", "center")
            ancla = {"center": "middle", "left": "start", "right": "end"}[alin]
            tx = {"middle": x + ew / 2, "start": x, "end": x + ew}[ancla]
            # el halo blanco existe para que un rotulo se lea sobre una linea
            # que lo cruza; dentro de una celda solo engorda el trazo
            halo = ('' if e.get("_halo", True) is False else
                    ' paint-order="stroke" stroke="#ffffff" stroke-width="4"'
                    ' stroke-linejoin="round"')
            for i, linea_txt in enumerate(e["text"].split("\n")):
                esc = (linea_txt.replace("&", "&amp;")
                                .replace("<", "&lt;").replace(">", "&gt;"))
                out.append(
                    f'<text x="{tx}" y="{y + paso * (i + 1) - tam * 0.28}" '
                    f'font-size="{tam}" fill="{TRAZO}" text-anchor="{ancla}"'
                    f'{halo}>{esc}</text>')

    out.append("</svg>")
    return "\n".join(out)


# --------------------------------------------------------------------------
# Diagrama: casos de uso del Sistema Hospitalario
#   (el caso resuelto en clase — Ejemplos resueltos de casos de negocio)
#
# Layout según estilo-diagramas.md §3.1:
#   · actores en la banda izquierda, en escalera
#   · el PADRE de la generalización arriba; cada hijo en su propia fila
#   · límite del sistema como recuadro que CONTIENE las elipses
#   · el caso heredado a la altura del padre; los especializados debajo,
#     cada uno a la altura de su actor  →  cero cruces y cero roces
# --------------------------------------------------------------------------
def cdu_hospital():
    els = []

    # --- actores en escalera: el PADRE arriba, los hijos en filas propias.
    #     La escalera es lo que le da a la asociación de cada hijo un carril
    #     libre: si los dos hijos comparten fila, la línea del lejano tiene
    #     que pasar por debajo del nombre del cercano.
    els += actor(160, 60, "Cliente")
    els += actor(280, 300, "Administrador\nHospitalización")
    els += actor(40, 460, "Administrador\nConsulta Externa")

    # --- límite del sistema
    els += caja(460, 40, 440, 600, "Sistema Hospitalario",
                fondo=FONDO_SISTEMA, grosor=2)

    # --- casos de uso: el heredado a la altura del padre, luego los especializados
    els += elipse(520, 100, 320, 90, "Despachar medicamentos\nen farmacia")
    els += elipse(520, 300, 320, 90, "Asignar camas")
    els += elipse(520, 500, 320, 90, "Asignar citas")

    # --- generalizaciones: hijo -> padre, triángulo hueco, padre ARRIBA
    els += linea(330, 300, 225, 196, punta="triangle_outline")
    els += linea(90, 460, 190, 196, punta="triangle_outline")

    # --- asociaciones actor-caso: SIN punta, y arrancan en la punta del brazo
    els += linea(244, 120, 537, 125)     # Cliente         -> Despachar medicamentos
    els += linea(364, 340, 524, 345)     # Adm. Hosp.      -> Asignar camas
    els += linea(124, 500, 537, 520)     # Adm. Cons. Ext. -> Asignar citas

    return els


# --------------------------------------------------------------------------
# BLOQUE 1.1 — Diagrama de contexto del NEGOCIO
#   Caso: Centro de Salud Publico (Guatemala)
#   Reglas (estilo-diagramas.md 8, BLOQUE 1.1):
#     · el negocio como CAJA NEGRA unica al centro, sin interior
#     · entidades de negocio a izquierda y derecha
#     · sistemas externos arriba y abajo  ->  sus flechas no cruzan las de las
#       personas
#     · toda flecha con nombre, en sustantivo; ida y vuelta = dos flechas
# --------------------------------------------------------------------------
def contexto_centro_salud():
    F = "arrow"          # todo streamline es direccional
    els = []

    # --- la caja negra: el negocio
    els += elipse(430, 340, 380, 200, "Centro de Salud\nP\u00fablico")

    # --- entidades de negocio: izquierda
    els += entidad(40, 180, 220, 70, "Paciente")
    els += entidad(40, 620, 220, 70, "Promotor de salud\ncomunitario")

    # --- entidades de negocio: derecha
    els += entidad(980, 160, 240, 70, "Direcci\u00f3n de \u00c1rea\nde Salud (MSPAS)")
    els += entidad(980, 400, 240, 70, "Hospital nacional\nde referencia")
    els += entidad(980, 640, 240, 70, "Almac\u00e9n de insumos\ny medicamentos")

    # --- sistemas externos: arriba y abajo
    els += entidad(510, 40, 220, 70, "RENAP")
    els += entidad(510, 780, 220, 70, "SIGSA")

    # --- streamlines desde y hacia el paciente
    els += linea(262, 200, 452, 372, punta=F, etiqueta="Solicitud de cita",
                 off=(-30, -28))
    els += linea(444, 400, 262, 232, punta=F, etiqueta="Cita confirmada",
                 off=(30, 50))

    # --- promotor comunitario
    els += linea(262, 668, 452, 508, punta=F, etiqueta="Censo comunitario",
                 off=(-30, 46))
    els += linea(446, 478, 262, 638, punta=F, etiqueta="Calendario de jornadas",
                 off=(30, -26))

    # --- Direccion de Area de Salud
    els += linea(978, 180, 792, 368, punta=F, etiqueta="Norma de atenci\u00f3n")
    els += linea(800, 396, 978, 212, punta=F, etiqueta="Reporte de morbilidad",
                 off=(-30, 50))

    # --- Hospital nacional de referencia
    els += linea(808, 424, 978, 424, punta=F, etiqueta="Referencia de paciente", off=(0, -6))
    els += linea(978, 452, 808, 452, punta=F, etiqueta="Contrarreferencia", off=(0, 30))

    # --- Almacen de insumos
    els += linea(796, 508, 978, 660, punta=F, etiqueta="Requisici\u00f3n de insumos")
    els += linea(978, 692, 790, 528, punta=F, etiqueta="Despacho de insumos",
                 off=(-30, 48))

    # --- sistemas externos (arriba y abajo): las etiquetas se separan en X
    #     porque las dos lineas corren casi verticales y a 80 px una de otra
    els += linea(596, 112, 566, 348, punta=F, etiqueta="Validaci\u00f3n de CUI",
                 off=(-118, 0))
    els += linea(650, 344, 674, 112, punta=F, etiqueta="Consulta de identidad",
                 off=(126, 0))
    els += linea(620, 540, 620, 776, punta=F, etiqueta="Registro diario\nde consultas")

    return els


# --------------------------------------------------------------------------
# BLOQUE 1.2 — CDU de alto nivel: el CORE del negocio
#   Reglas (estilo-diagramas.md 8, BLOQUE 1.2):
#     · estereotipos DE NEGOCIO en todos los elementos
#     · solo casos primarios: los servicios esenciales que recibe el cliente
#     · actor principal del lado de lectura (izquierda); secundarios del opuesto
#     · casos ordenados por IMPORTANCIA, de arriba abajo
#     · el recuadro del negocio contiene los casos; los actores quedan fuera
# --------------------------------------------------------------------------
def cdu_negocio_centro_salud():
    els = []

    # --- frontera del negocio
    els += caja(420, 40, 460, 640, "Centro de Salud P\u00fablico",
                fondo=FONDO_SISTEMA, grosor=2)

    # --- casos de uso de negocio, ordenados por importancia
    els += elipse_negocio(460, 120, 380, 100, "Atender consulta m\u00e9dica")
    els += elipse_negocio(460, 300, 380, 100, "Aplicar esquema\nde vacunaci\u00f3n")
    els += elipse_negocio(460, 500, 380, 100, "Referir paciente a\nhospital nacional")

    # --- actor principal (izquierda) y secundario (derecha)
    els += actor_negocio(60, 300, "Paciente")
    els += actor_negocio(1000, 480, "Hospital nacional\nde referencia")

    # --- asociaciones: SIN punta de flecha
    els += linea(146, 320, 470, 182)
    els += linea(146, 360, 462, 350)
    els += linea(146, 396, 472, 528)
    els += linea(996, 520, 838, 548)

    return els


# --------------------------------------------------------------------------
# PASO 3 del Caso 1 — CDU de alto nivel: el CORE del negocio de FarmaHosp
#
# Molde de la catedra, verificado en sus 4 casos (estilo-diagramas.md 8, 1.2):
#   · UNA sola elipse, que nombra el negocio COMPLETO (la frontera del paso 0)
#   · todos los actores alrededor, en circulo
#   · lineas SIN punta (comunicacion en los dos sentidos)
#   · estereotipos de negocio: las barras diagonales
#
# Quien es actor sale de la frontera declarada en la Entrega (seccion 0):
# el personal clinico es TRABAJADOR (no se dibuja); los actores son quienes
# interactuan desde afuera del ciclo de vida del MAC.
# --------------------------------------------------------------------------
def cdu_core_farmahosp():
    els = []

    # --- el negocio completo, sin abrir: UNA elipse
    els += elipse_negocio(380, 250, 380, 170,
                          "Gestión del Ciclo de Vida del\nMedicamento de Alto Costo (MAC)")

    # --- los actores, en circulo
    els += actor_negocio(60, 300, "Paciente")
    els += actor_negocio(180, 60, "Proveedor de MAC")
    els += actor_negocio(880, 60, "MSPAS")
    els += actor_negocio(1000, 300, "Contraloría General\nde Cuentas")
    els += actor_negocio(510, 580, "Sistema legacy\nde admisiones")

    # --- asociaciones SIN punta (los 4 cores de la catedra van asi)
    els += linea(168, 340, 384, 336)      # Paciente
    els += linea(268, 172, 452, 280)      # Proveedor de MAC
    els += linea(908, 172, 692, 280)      # MSPAS
    els += linea(996, 340, 756, 336)      # Contraloria
    els += linea(562, 576, 568, 422)      # Legacy de admisiones

    return els


# --------------------------------------------------------------------------
# PASO 4 del Caso 1 — Primera descomposicion: los procesos del negocio
#
# Molde de la catedra (Tienda Electronica / Fabrica): UN solo diagrama,
# los CUN en COLUMNA al centro, los MISMOS actores del core a los lados.
# Nombres como sustantivo derivado de verbo ("Prescripcion del tratamiento").
# Los 6 primeros procesos son las 6 etapas del ciclo de vida del enunciado;
# el 7o es la categoria GERENCIAL de la nota tecnica (control y auditoria).
# Almacenamiento va sin actor: es la excepcion de CU de apoyo de los convenios.
# --------------------------------------------------------------------------
def cdu_descomposicion_farmahosp():
    els = []
    EX, EW, EH, PASO = 430, 340, 90, 130

    nombres = [
        "Adquisición de MAC",
        "Almacenamiento y\nconservaci\u00f3n de MAC",
        "Prescripción del tratamiento",
        "Dispensación del MAC",
        "Administraci\u00f3n del MAC\nal paciente",
        "Seguimiento y\nfarmacovigilancia",
        "Control y auditor\u00eda de\nla gesti\u00f3n de MAC",
    ]
    ys = [60 + i * PASO for i in range(7)]
    for n, y in zip(nombres, ys):
        els += elipse_negocio(EX, y, EW, EH, n, tam=14)

    # categorias de la NT, como rotulos de zona a la izquierda de la columna
    els.append(texto("SOPORTE", 330, ys[0] + 100, 80, 12))
    els.append(texto("NÚCLEO", 330, ys[3] + 40, 80, 12))
    els.append(texto("GERENCIAL", 320, ys[6] + 35, 100, 12))

    # actores: el mismo juego del core, a los lados
    els += actor_negocio(120, 60, "Proveedor de MAC")
    els += actor_negocio(120, 470, "Paciente")
    els += actor_negocio(950, 300, "Sistema legacy\nde admisiones")
    els += actor_negocio(950, 690, "MSPAS")
    els += actor_negocio(950, 850, "Contralor\u00eda General\nde Cuentas")

    # asociaciones SIN punta
    els += linea(226, 105, 432, 105)          # Proveedor  - Adquisicion
    els += linea(226, 500, 436, 380)          # Paciente   - Prescripcion
    els += linea(226, 515, 434, 495)          # Paciente   - Dispensacion
    els += linea(226, 530, 434, 630)          # Paciente   - Administracion
    els += linea(226, 545, 438, 755)          # Paciente   - Seguimiento
    els += linea(946, 345, 768, 372)          # Legacy     - Prescripcion
    els += linea(946, 735, 772, 758)          # MSPAS      - Seguimiento
    els += linea(946, 895, 772, 895)          # Contraloria- Control y auditoria

    return els


# --------------------------------------------------------------------------
# PASO 5 del Caso 1 — CDU expandido del proceso Prescripcion (plano del SISTEMA)
#
# Cambia el plano: actores y elipses SIN estereotipo de negocio, y el recuadro
# es el sistema. Molde de la catedra ("Procesamiento de Pedido" expandido):
#   · include con flecha punteada BASE -> INCLUIDO
#   · extend con flecha punteada EXTENSION -> BASE, con su condicion
#   · generalizacion de actores: el padre con el CU compartido, cada hijo
#     con el suyo (el patron del Hospital de la catedra)
# --------------------------------------------------------------------------
def cdu_expandido_prescripcion():
    els = []

    els += caja(400, 40, 880, 820, "FarmaHosp — Prescripción",
                fondo=FONDO_SISTEMA, grosor=2)

    # CU base
    els += elipse(440, 180, 280, 90, "Prescribir MAC", tam=15)

    # incluidos (columna derecha): los 4 que el enunciado exige al prescribir
    els += elipse(920, 70, 330, 80, "Validar protocolo clínico", tam=13)
    els += elipse(920, 180, 330, 80, "Verificar interacciones\nmedicamentosas", tam=13)
    els += elipse(920, 290, 330, 80, "Verificar contraindicaciones\ny alergias", tam=13)
    els += elipse(920, 400, 330, 80, "Consultar inventario\nen tiempo real", tam=13)

    # extension: solo ocurre si no hay stock
    els += elipse(440, 440, 310, 90, "Solicitar compra urgente\no reemplazo terapéutico", tam=13)

    # CU propio del medico de urgencias (ABAC del acuerdo de calidad 4)
    els += elipse(440, 650, 330, 90, "Acceder a diagnóstico sensible\ncon justificación auditada", tam=13)

    # --- actores del SISTEMA (sin estereotipo de negocio), en escalera
    els += actor(140, 110, "Médico")
    els += actor(250, 340, "Médico tratante")
    els += actor(70, 540, "Médico de\nurgencias")

    # generalizacion: hijo -> padre, triangulo hueco, padre ARRIBA
    els += linea(296, 344, 208, 240, punta="triangle_outline")
    els += linea(124, 540, 176, 244, punta="triangle_outline")

    # asociaciones (sin punta): padre con el CU compartido; cada hijo el suyo
    els += linea(244, 152, 442, 222)
    els += linea(336, 382, 442, 478)
    els += linea(156, 582, 442, 692)

    # include: BASE -> incluido, punteada
    els += linea(716, 200, 918, 110, punta="arrow", punteada=True,
                 etiqueta="«include»", off=(30, -18))
    els += linea(720, 220, 918, 220, punta="arrow", punteada=True,
                 etiqueta="«include»", off=(20, -14))
    els += linea(716, 244, 918, 330, punta="arrow", punteada=True,
                 etiqueta="«include»", off=(46, 8))
    els += linea(704, 260, 918, 438, punta="arrow", punteada=True,
                 etiqueta="«include»", off=(66, 36))

    # extend: EXTENSION -> BASE, punteada, con la condicion
    els += linea(590, 438, 578, 274, punta="arrow", punteada=True,
                 etiqueta="«extend»\n[sin stock]", off=(74, 10))

    return els


# --------------------------------------------------------------------------
# Laminas: drivers de atributos de calidad del Caso 1 (FarmaHosp)
#
# NO son diagramas y no se dibujan como casos de uso: un atributo de calidad
# NO es un caso de uso (estilo-diagramas.md §8). Son los 8 escenarios de SEIS
# partes de la Entrega §3.2, puestos en lamina. El contenido es el del
# entregable — si cambia alli, se regenera aca.
# --------------------------------------------------------------------------
RESUMEN_CALIDAD = [
    ["AC-01", "Validación paciente-medicamento < 500 ms / < 2 s",
     "Eficiencia", "Fiabilidad", "STK-03 enfermero"],
    ["AC-02", "Operación offline ≥ 4 h con reconciliación",
     "Fiabilidad", "Funcionalidad", "STK-02 / STK-03"],
    ["AC-03", "Registros inmutables y trazables sin degradar",
     "Funcionalidad (seguridad: no repudio)", "Eficiencia", "STK-11 Contraloría"],
    ["AC-04", "Autorización contextual ABAC con excepción auditada",
     "Funcionalidad (seguridad: confidencialidad)", "Eficiencia", "STK-06 paciente"],
    ["AC-05", "Pico de 10x con presupuesto fijo",
     "Eficiencia", "Fiabilidad", "STK-13 operaciones"],
    ["AC-06", "Integración legacy SOAP + nacional XML/DTD",
     "Funcionalidad (interoperabilidad)", "Fiabilidad, eficiencia", "STK-07 MSPAS"],
    ["AC-07", "Mantenible por el equipo interno tras la consultora",
     "Mantenibilidad", "—", "STK-08 equipo interno"],
    ["AC-08", "Temperaturas inalterables y verificables criptográficamente",
     "Funcionalidad (seguridad: integridad)", "—", "STK-11 Contraloría"],
]

FICHAS_CALIDAD = {
    "ac-01": (
        "AC-01 — Eficiencia (comportamiento temporal)",
        "Secundario: fiabilidad  ·  Origen: acuerdo de calidad 1 + escenario crítico 3",
        [("Fuente", "El enfermero de piso, desde la Toughpad junto a la cama"),
         ("Estímulo", "Escanea la pulsera del paciente y el código del medicamento para validar"),
         ("Artefacto", "El módulo de administración (validación paciente-medicamento)"),
         ("Entorno", "Operación normal de red; y condición degradada (Wi-Fi inestable del piso)"),
         ("Respuesta", "Confirma la correspondencia o dispara la alerta roja de discrepancia"),
         ("MEDIDA", "< 500 ms (p95) en red normal y < 2 s en degradada, con 15.000 pacientes y "
                    "800 SKUs en base — la alerta de 4 s del escenario 3 es el contraejemplo")]),
    "ac-02": (
        "AC-02 — Fiabilidad (tolerancia a fallos y recuperabilidad)",
        "Secundario: funcionalidad (exactitud)  ·  Origen: acuerdo 2 + escenario crítico 5",
        [("Fuente", "La caída del servidor central (o del enlace)"),
         ("Estímulo", "Los puestos de farmacia y las tablets pierden conectividad"),
         ("Artefacto", "Los módulos de dispensación y administración"),
         ("Entorno", "Hora pico — lunes 8:30, el peor momento posible"),
         ("Respuesta", "Siguen operando con registro local; al reconectar, la trazabilidad se "
                       "reconcilia automáticamente"),
         ("MEDIDA", "Operación offline ≥ 4 horas; 100 % de los registros reconciliados, "
                    "0 duplicados")]),
    "ac-03": (
        "AC-03 — Funcionalidad → seguridad: no repudio",
        "En ISO 25010 sería de primer nivel  ·  Secundario: eficiencia  ·  "
        "Origen: acuerdo 3 + escenario crítico 4",
        [("Fuente", "Cualquier usuario — incluido el administrador del sistema"),
         ("Estímulo", "Intenta modificar o eliminar un registro histórico (inventario, "
                      "prescripción, dispensación, administración)"),
         ("Artefacto", "El almacén de registros del sistema"),
         ("Entorno", "Operación normal"),
         ("Respuesta", "La modificación se rechaza; todo cambio entra como evento nuevo "
                       "trazado a su usuario"),
         ("MEDIDA", "0 modificaciones históricas posibles; 100 % de eventos con usuario; el "
                    "rendimiento de operación no se degrada por el historial (escrituras "
                    "dentro de AC-01)")]),
    "ac-04": (
        "AC-04 — Funcionalidad → seguridad: confidencialidad",
        "ISO 25010: primer nivel  ·  Secundario: eficiencia  ·  "
        "Origen: acuerdo 4 + política de datos del hospital",
        [("Fuente", "Un médico de urgencias que NO es el tratante (y, en el caso negativo, "
                    "personal de admisión)"),
         ("Estímulo", "Solicita el diagnóstico sensible (VIH, cáncer) de un paciente"),
         ("Artefacto", "El módulo de expedientes y su motor de autorización (ABAC)"),
         ("Entorno", "Emergencia, fuera del horario del tratante"),
         ("Respuesta", "A urgencias: concede con justificación obligatoria y registro en el log. "
                       "A admisión: niega siempre — ni el director accede sin orden judicial"),
         ("MEDIDA", "100 % de accesos de excepción con justificación registrada; 0 accesos de "
                    "personal no autorizado; decisión de autorización sin volverse cuello de "
                    "botella (< 200 ms)")]),
    "ac-05": (
        "AC-05 — Eficiencia (utilización de recursos bajo sobrecarga)",
        "Secundario: fiabilidad  ·  Origen: acuerdo 5 + escenario crítico 5",
        [("Fuente", "Los usuarios concurrentes de todo el hospital"),
         ("Estímulo", "Un pico de 10× el tráfico normal"),
         ("Artefacto", "El sistema completo, sobre el data center fijo (32 vCPU / 128 GB / "
                       "SAN 10 TB, sin autoescalado)"),
         ("Entorno", "Lunes 8:30 — sobrecarga"),
         ("Respuesta", "Sigue atendiendo priorizando el tráfico crítico (dispensaciones); "
                       "degrada lo no crítico"),
         ("MEDIDA", "0 colapsos; las dispensaciones se mantienen dentro de la medida de AC-01; "
                    "sin hardware adicional (mitigación arquitectónica: caché, colas, réplicas "
                    "de lectura)")]),
    "ac-06": (
        "AC-06 — Funcionalidad → interoperabilidad",
        "ISO 25010: primer nivel  ·  Secundarios: fiabilidad, eficiencia  ·  "
        "Origen: acuerdo 6 + escenario crítico 6",
        [("Fuente", "El sistema legacy de admisiones (COBOL/SOAP, 3-5 s, 7:00-17:00) y el "
                    "sistema nacional de farmacovigilancia (XML/DTD, 8:00-16:00)"),
         ("Estímulo", "El sistema necesita identidad del paciente; debe entregar un reporte de "
                      "efecto adverso"),
         ("Artefacto", "Los adaptadores de integración"),
         ("Entorno", "El incidente ocurre fuera de la ventana del sistema externo (la anafilaxia "
                     "de las 19:30)"),
         ("Respuesta", "Los datos de admisiones se replican/cachean para no bloquear la "
                       "operación; los reportes se encolan y reintentan en ventana hábil — el "
                       "plazo legal lo cumple el registro local"),
         ("MEDIDA", "La respuesta al farmacéutico no espera al legacy (dentro de AC-01); "
                    "100 % de reportes entregados ≤ 24 h")]),
    "ac-07": (
        "AC-07 — Mantenibilidad (cambiabilidad y analizabilidad)",
        "Origen: acuerdo 7 + restricciones del equipo",
        [("Fuente", "El equipo interno de TI: 3 personas, Java 8 / Spring Boot / Oracle PL/SQL "
                    "/ Angular"),
         ("Estímulo", "Un cambio normativo del MSPAS o una corrección, después de que la "
                      "consultora se fue"),
         ("Artefacto", "El código del sistema y su documentación viva"),
         ("Entorno", "Mantenimiento post-entrega, sin apoyo externo, con rotación de personal alta"),
         ("Respuesta", "El equipo implementa el cambio solo con su experiencia real y la "
                       "documentación"),
         ("MEDIDA", "El cambio afecta un solo módulo (cambiar farmacovigilancia sin tocar "
                    "inventario); resuelto sin intervención externa; evolución incremental por "
                    "módulos posible")]),
    "ac-08": (
        "AC-08 — Funcionalidad → seguridad: integridad",
        "ISO 25010: primer nivel  ·  Origen: acuerdo 8 + escenario crítico 1",
        [("Fuente", "Un auditor de la Contraloría (o el farmacéutico jefe que evalúa un lote)"),
         ("Estímulo", "Verifica que las lecturas de temperatura que justificaron descartar un "
                      "lote no fueron manipuladas"),
         ("Artefacto", "El registro de lecturas de los sensores IoT"),
         ("Entorno", "Auditoría posterior al descarte (el informe forense del escenario 4)"),
         ("Respuesta", "El sistema demuestra criptográficamente la integridad de la serie "
                       "(hash encadenado o firma de sensores — la técnica se decide en diseño; "
                       "el driver fija la propiedad)"),
         ("MEDIDA", "100 % de las lecturas verificables; cualquier alteración posterior es "
                    "detectable")]),
}


def tabla_drivers_calidad():
    """Lamina resumen: los 8 drivers de calidad con su atributo dominante."""
    cols = [("ID", 100), ("Acuerdo de calidad del enunciado", 420),
            ("Atributo dominante", 260), ("Otros", 180), ("Stakeholder detrás", 220)]
    els = [
        titulo("Drivers de atributos de calidad — FarmaHosp", 40, 40, 1180),
        texto("Taxonomía declarada: los seis atributos del programa (ISO 9126).\n"
              "Seguridad e interoperabilidad van bajo funcionalidad; en ISO 25010 serían "
              "características de primer nivel.\n"
              "Cada AC-nn se especifica como escenario de seis partes — ver su ficha.",
              40, 76, 1180, 13, align="left", _halo=False),
    ]
    rejilla, _ = tabla(40, 150, cols, RESUMEN_CALIDAD)
    return els + rejilla


def _ficha(clave):
    """Lamina de un driver: el escenario de SEIS partes, con la medida resaltada."""
    def construir():
        cabecera, sub, partes = FICHAS_CALIDAD[clave]
        els = [
            titulo(cabecera, 40, 40, 940),
            texto(sub, 40, 74, 940, 13, align="left", _halo=False),
        ]
        cols = [("Parte del escenario", 200), ("Contenido", 740)]
        # la MEDIDA es la ultima de las seis y va sombreada: sin numero no es
        # un driver, es un deseo
        rejilla, _ = tabla(40, 120, cols, [list(f) for f in partes], destacar=(5,))
        return els + rejilla
    return construir


# --------------------------------------------------------------------------
# Laminas: las tres matrices de trazabilidad del Caso 1 (criterio 4)
#
# Tampoco son diagramas: son TABLAS (Entrega §4). La regla comun es que una
# matriz solo sirve si se lee en los dos sentidos, y que el hallazgo son los
# HUECOS — por eso cada lamina lleva su leyenda de celda y su lectura al pie.
# Los ids no se renumeran: son los de §1-§3.
# --------------------------------------------------------------------------
CDU_CORTOS = ["CDU-01\nAdquis.", "CDU-02\nAlmac.", "CDU-03\nPrescr.",
              "CDU-04\nDispen.", "CDU-05\nAdmin.", "CDU-06\nSeguim.",
              "CDU-07\nControl"]

STK_CDU = [
    ("STK-01 Médico tratante",   ["", "", "X", "i", "i", "X", ""]),
    ("STK-02 Farmacéutico",      ["i", "X", "", "X", "i", "", ""]),
    ("STK-03 Enfermero",         ["", "", "", "X", "X", "i", ""]),
    ("STK-04 Director Admin.",   ["X", "i", "", "", "", "", "X"]),
    ("STK-05 Jefe Farmacovig.",  ["", "", "", "", "i", "X", "i"]),
    ("STK-06 Paciente",          ["", "", "X", "i", "X", "X", ""]),
    ("STK-07 MSPAS",             ["", "", "", "", "", "X", "X"]),
    ("STK-08 Equipo interno TI", ["i"] * 7),
    ("STK-09 Consultora",        ["i"] * 7),
    ("STK-10 Junta Directiva",   ["i", "", "", "", "", "", "X"]),
    ("STK-11 Contraloría",       ["i", "i", "", "", "", "", "X"]),
    ("STK-12 Proveedor de MAC",  ["X", "i", "", "", "", "", ""]),
    ("STK-13 Operaciones TI",    ["i"] * 7),
]

DEPENDENCIAS_RF = [
    ["RF-02 recepción de lotes", "RF-01", "no se recibe sin orden de compra"],
    ["RF-06 incidente y bloqueo", "RF-05", "sin monitoreo no hay incidente que registrar"],
    ["RF-07 alerta de guardia", "RF-06", "alerta lo que el incidente detectó"],
    ["RF-08 sobrescribir descarte", "RF-06", "se sobrescribe la decisión que el incidente disparó"],
    ["RF-09 proyección de faltantes", "RF-02, RF-10",
     "proyecta sobre inventario y prescripciones programadas"],
    ["RF-10 prescribir", "RF-11, RF-12, RF-13, RF-14", "los cuatro include obligatorios"],
    ["RF-14 consultar inventario", "RF-02", "consulta los lotes registrados"],
    ["RF-15 sugerir MAC", "RF-10, RF-11", "sugiere sobre protocolo e historial de prescripción"],
    ["RF-17 dispensar", "RF-10, RF-14, RF-02", "dispensa una prescripción, contra inventario real"],
    ["RF-18 etiqueta QR", "RF-17", "etiqueta el lote asignado"],
    ["RF-19 / RF-20 / RF-21 opciones A/B/C", "RF-17", "las tres extienden la dispensación"],
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
    ["RF-32 trazabilidad QR", "RF-18, RF-23", "muestra la cadena etiqueta → administración"],
    ["RF-33 informe forense", "RF-02, RF-05, RF-17, RF-23", "recorre la cadena completa del lote"],
    ["RF-34 tablero financiero", "RF-02, RF-17", "agrega costos y desperdicio"],
    ["RF-35 auditar autorizaciones", "RF-01, RF-08", "audita compras y sobrescrituras"],
    ["RF-36 información pública", "RF-34", "publica los agregados anonimizados"],
    ["RF-37 HL7 / API nacional", "RF-28, RF-29", "expone lo que farmacovigilancia registra"],
]

TRONCO_COLS = ["01", "02", "05", "10", "14", "17", "18", "23", "24", "28", "29", "33"]
TRONCO_RF = [
    ("RF-01", {"01": "—"}),
    ("RF-02", {"01": "X", "02": "—"}),
    ("RF-05", {"05": "—"}),
    ("RF-10", {"10": "—", "14": "X"}),
    ("RF-14", {"02": "X", "14": "—"}),
    ("RF-17", {"02": "X", "10": "X", "14": "X", "17": "—"}),
    ("RF-18", {"17": "X", "18": "—"}),
    ("RF-23", {"17": "X", "23": "—", "24": "X"}),
    ("RF-24", {"18": "X", "24": "—"}),
    ("RF-28", {"23": "X", "28": "—"}),
    ("RF-29", {"28": "X", "29": "—"}),
    ("RF-33", {"02": "X", "05": "X", "17": "X", "23": "X", "33": "—"}),
]

# CDU -> los RF que cubre. RF-14 y RF-22 aparecen en DOS filas a proposito:
# es la inclusion por reutilizacion de §3.1 hecha visible, no un error.
COBERTURA_CDU = {
    "CDU-01": [1, 2, 3, 4],
    "CDU-02": [5, 6, 7, 8, 9],
    "CDU-03": [10, 11, 12, 13, 14, 15, 16],
    "CDU-04": [14, 17, 18, 19, 20, 21, 22],
    "CDU-05": [22, 23, 24, 25, 26, 27],
    "CDU-06": [28, 29, 30, 31, 32],
    "CDU-07": [33, 34, 35, 36, 37],
}


def _pie(lineas, x, y, ancho, tam=13):
    """Las dos lecturas al pie: una matriz solo sirve leida en los dos sentidos."""
    return texto("\n".join(lineas), x, y, ancho, tam, align="left", _halo=False)


def matriz_stk_cdu():
    els = [
        titulo("Matriz 1 — Stakeholders vs. CDU", 40, 40, 1100),
        texto("Celda:  X = participa directamente en el proceso  ·  "
              "i = tiene interés en su resultado sin participar",
              40, 74, 1100, 13, align="left", _halo=False),
    ]
    rejilla, alto = matriz(40, 110, "Stakeholder", 260, CDU_CORTOS, 120, STK_CDU)
    els += rejilla
    els.append(_pie([
        "Lectura por columna — ¿para quién es cada proceso?  Ninguna columna vacía. "
        "El más poblado es CDU-05 (administración), coherente con que sea el acto de valor central.",
        "Lectura por fila — ¿dónde aparece cada stakeholder?  Ninguna fila vacía. Tres filas son "
        "enteramente i (STK-08, STK-09, STK-13):",
        "no es un hueco, es su naturaleza — quien construye, mantiene y opera tiene interés "
        "transversal sin participar en ningún proceso.",
        "Es la demostración en matriz de que NO todo stakeholder es actor.",
    ], 40, 110 + alto + 30, 1100))
    return els


def matriz_dependencias_rf():
    els = [
        titulo("Matriz 2a — Drivers RF vs. Drivers RF · tabla completa de dependencias",
               40, 40, 1200),
        texto("Se lee: «la fila depende de la columna». Con 37 RF la matriz 37×37 sería casi "
              "vacía, así que se presenta en dos vistas —\n"
              "decisión declarada: esta tabla completa, y la matriz del tronco (matriz 2b) con "
              "los 12 RF que concentran las dependencias.",
              40, 74, 1200, 13, align="left", _halo=False),
    ]
    cols = [("RF que depende", 300), ("Depende de", 230), ("Razón", 570)]
    rejilla, _ = tabla(40, 130, cols, DEPENDENCIAS_RF)
    return els + rejilla


def matriz_tronco_rf():
    filas = [(etq, [marcas.get(c, "") for c in TRONCO_COLS])
             for etq, marcas in TRONCO_RF]
    els = [
        titulo("Matriz 2b — Drivers RF vs. Drivers RF · el tronco", 40, 40, 1000),
        texto("Se lee: «la fila depende de la columna». Asimétrica, y la diagonal "
              "queda excluida (—), según la NT1 de la cátedra.",
              40, 74, 1000, 13, align="left", _halo=False),
    ]
    rejilla, alto = matriz(40, 110, "dep. ↓  /  de →", 200, TRONCO_COLS, 66, filas)
    els += rejilla
    els.append(_pie([
        "Lectura por fila — ¿qué necesito antes de construir esto?  Filas vacías (autónomos, "
        "candidatos a construirse primero): RF-01, RF-05, RF-11/12/13.",
        "Coincide con la restricción RE-18: dispensación y almacén primero.",
        "Lectura por columna — ¿si cambio esto, qué se rompe?  Las más pobladas son RF-02 "
        "(4 dependientes), RF-17 (6) y RF-23 (5):",
        "el registro de lotes, la dispensación y la administración son los RF críticos. "
        "Sin ciclos: ningún par depende mutuamente.",
    ], 40, 110 + alto + 30, 1100))
    return els


def matriz_cdu_rf():
    cols = [f"{n:02d}" for n in range(1, 38)]
    filas = [(cdu, ["X" if n in rfs else "" for n in range(1, 38)])
             for cdu, rfs in COBERTURA_CDU.items()]
    els = [
        titulo("Matriz 3 — CDU vs. Drivers RF · cobertura", 40, 40, 1600),
        texto("Celda:  X = ese proceso cubre ese driver.  Las columnas son RF-01 … RF-37.",
              40, 74, 1600, 13, align="left", _halo=False),
    ]
    rejilla, alto = matriz(40, 110, "Proceso", 120, cols, 46, filas)
    els += rejilla
    els.append(_pie([
        "Lectura por columna — ¿todo RF tiene quién lo cubra?  Ninguna columna vacía: los 37 RF "
        "están cubiertos. Es la prueba de completitud del criterio 3.",
        "Lectura por fila — ¿todo proceso justifica su existencia?  Ninguna fila vacía, y el "
        "reparto es parejo (4-7 RF por proceso): ningún CDU sobrecargado ni de más.",
        "El hallazgo fino: RF-14 aparece en dos filas (CDU-03 y CDU-04) y RF-22 también "
        "(CDU-04 y CDU-05). No es un error de la matriz:",
        "es la inclusión por reutilización de §3.1 hecha visible — consultar inventario lo "
        "comparten prescribir y dispensar; el doble registro INCAP exige que",
        "dispensación y administración coincidan.",
    ], 40, 110 + alto + 30, 1900))
    return els


# --------------------------------------------------------------------------
# Laminas: drivers de restriccion (Entrega §3.3)
#
# Una restriccion es una decision de diseno YA TOMADA que el arquitecto no
# negocia. No tiene medida (se cumple o no) y NO se prioriza: todas son
# obligatorias. La columna "que decision bloquea" es la que convierte la cita
# en driver — una restriccion sirve para descartar alternativas.
# Las explicitas van TEXTUALES: parafrasear es donde se pierde el requisito.
# --------------------------------------------------------------------------
RESTRICCIONES_EXPLICITAS = [
    ["RE-01", "«No se puede usar una base de datos que no soporte transacciones ACID "
              "para el módulo de inventario»", "técnica",
     "Descarta NoSQL sin ACID para inventario — el MongoDB de la consultora incluido"],
    ["RE-02", "«No se puede depender de la nube pública para el almacenamiento de datos "
              "sensibles… solo… análisis estadístico agregado (datos anonimizados)»", "técnica",
     "Descarta bases y SaaS en la nube para lo clínico; todo en el data center local"],
    ["RE-03", "«No se puede usar una tecnología que requiera licencias de pago anuales… "
              "(ej. Oracle Enterprise, SQL Server Enterprise). Se prefiere software "
              "open-source»", "negocio",
     "Descarta las bases comerciales — incluida la Oracle que el equipo interno prefiere"],
    ["RE-04", "«No se puede obligar a los enfermeros a usar dispositivos personales (BYOD)… "
              "el hospital provee los Toughpads»", "negocio",
     "El cliente de enfermería se diseña para las Toughpad, no para «cualquier teléfono»"],
    ["RE-05", "«No se puede diseñar un sistema monolítico, porque el módulo de "
              "farmacovigilancia tiene ciclos de entrega diferentes…»", "técnica",
     "Obliga módulos desplegables por separado; descarta el despliegue único"],
    ["RE-06", "«No se pueden almacenar contraseñas ni credenciales en texto plano en "
              "ninguna capa»", "técnica",
     "Descarta configuraciones y logs con secretos; obliga hashing y gestión de secretos"],
    ["RE-07", "«No se puede implementar una solución que requiera entrenamiento de más de "
              "2 horas para los enfermeros»", "negocio",
     "Acota la complejidad de la interfaz de enfermería; descarta flujos que exijan curso"],
    ["RE-08", "«No se puede generar un único punto de falla en la autenticación; si… (LDAP) "
              "cae, el hospital debe seguir operando con… respaldo (ej. OTP por SMS)»", "técnica",
     "Descarta autenticar solo contra LDAP; obliga el mecanismo de respaldo"],
]

RESTRICCIONES_IMPLICITAS = [
    ["RE-09", "Reporte de efectos adversos ≤ 24 h en XML con la DTD del MSPAS",
     "regulatoria — Norma Técnica de Farmacovigilancia",
     "El formato y el plazo no se negocian; se realiza en RF-29 y AC-06"],
    ["RE-10", "Doble registro farmacéutico-enfermero para oncológicos y opioides; "
              "alerta si discrepancia > 5 min", "regulatoria — INCAP",
     "Obliga la coincidencia en tiempo real; se realiza en RF-22"],
    ["RE-11", "Responder solicitudes ciudadanas de datos estadísticos (no personales) "
              "en 10 días hábiles", "regulatoria — Ley de Acceso a la Información Pública",
     "Obliga la vía de datos anonimizados; se realiza en RF-36"],
    ["RE-12", "Diagnósticos sensibles visibles solo para tratante, farmacéutico y enfermero "
              "asignado; el director solo con orden judicial",
     "regulatoria — Política de Datos del Hospital",
     "Fija el modelo de autorización; se realiza en AC-04 y RF-16"],
    ["RE-13", "Data center fijo: 32 vCPU / 128 GB / SAN 10 TB, sin autoescalado",
     "técnica del entorno",
     "Descarta resolver el pico con hardware; obliga la mitigación arquitectónica de AC-05"],
    ["RE-14", "Tablets Panasonic Toughpad, Android 9, 3 GB RAM ya compradas",
     "técnica del entorno",
     "El cliente móvil debe correr ahí: descarta frameworks pesados y Android nuevos"],
    ["RE-15", "Escáneres Bluetooth con 5 % de fallo: la entrada manual del código es "
              "obligatoria", "técnica del entorno",
     "Obliga el respaldo manual de RF-25; descarta flujos solo-escáner"],
    ["RE-16", "Wi-Fi inestable en el sótano de farmacia; internet de 50 Mbps compartido "
              "con priorización de tráfico crítico", "técnica del entorno",
     "Descarta diseños que asuman red confiable; empuja AC-01 degradado y AC-02"],
    ["RE-17", "El sistema debe poder ser mantenido exclusivamente por el equipo interno "
              "(3 personas, Java 8 / Oracle PL/SQL / Angular) tras los 12 meses",
     "organizativa",
     "Acota el stack a lo que el interno pueda heredar; es el origen de AC-07"],
    ["RE-18", "Entrega en 12 meses, con evolución incremental: dispensación y almacén → "
              "prescripción → farmacovigilancia", "organizativa",
     "Fija el orden de construcción y refuerza RE-05 (módulos separados)"],
]


def restricciones_explicitas():
    els = [
        titulo("Drivers de restricción — las 8 explícitas del enunciado", 40, 40, 1300),
        texto("Textuales, sin parafrasear: parafrasear es donde se pierde el requisito.\n"
              "Una restricción no tiene medida (se cumple o no) y NO se prioriza: todas son "
              "obligatorias. La última columna es la que la convierte en driver.",
              40, 74, 1300, 13, align="left", _halo=False),
    ]
    cols = [("ID", 90), ("Restricción (textual)", 620), ("Tipo", 110),
            ("Qué decisión bloquea", 480)]
    rejilla, _ = tabla(40, 130, cols, RESTRICCIONES_EXPLICITAS)
    return els + rejilla


def restricciones_implicitas():
    els = [
        titulo("Drivers de restricción — las implícitas", 40, 40, 1300),
        texto("Repartidas por el enunciado fuera de su sección de restricciones; se barren "
              "por origen: regulatorias, técnicas del entorno y organizativas.",
              40, 74, 1300, 13, align="left", _halo=False),
    ]
    cols = [("ID", 90), ("Restricción", 420), ("Origen", 280),
            ("Qué decisión bloquea / dónde se realiza", 510)]
    rejilla, alto = tabla(40, 120, cols, RESTRICCIONES_IMPLICITAS)
    els += rejilla
    els.append(_pie([
        "La tensión que resuelven juntas: RE-03 (sin licencias: descarta Oracle Enterprise) "
        "choca con la preferencia del equipo interno (Oracle), y RE-17 exige que ese mismo",
        "equipo mantenga el sistema. Leídas juntas acotan el stack por las dos puntas: el "
        "lenguaje que el interno domina + una base open source con ACID (RE-01).",
        "Los stakeholders recortados en §1.1 se saldan acá: INCAP es RE-10; el personal de "
        "admisiones es la cara negativa de RE-12; la capacitación limitada es RE-07.",
    ], 40, 120 + alto + 30, 1300))
    return els


# --------------------------------------------------------------------------
# Laminas: priorizacion de los 5 drivers mas criticos (Entrega §3.4)
#
# El metodo es ADD: DOS ejes, no una nota unica. La importancia para el
# negocio la asignan los stakeholders; la dificultad tecnica, el arquitecto.
# Compiten solo los AC-nn: las restricciones NO se priorizan.
# --------------------------------------------------------------------------
DOS_EJES = [
    ["AC-01", "Validación < 500 ms / < 2 s",
     "A — STK-03: evita el error fatal del escenario 3",
     "A — el número con red degradada y equipo mixto; el enunciado mismo lo pregunta", "(A, A)"],
    ["AC-02", "Offline ≥ 4 h con reconciliación",
     "A — STK-02/STK-03: sin esto la quimioterapia se detiene",
     "A — reconciliar sin duplicar es un problema de consistencia distribuida", "(A, A)"],
    ["AC-03", "Inmutabilidad y trazabilidad total",
     "A — STK-11: el proyecto nace de auditorías fallidas",
     "M — event sourcing / bitácora inmutable es patrón conocido; el reto es no degradar",
     "(A, M)"],
    ["AC-04", "Confidencialidad ABAC con excepción",
     "A — STK-06: ley + estigma de VIH/cáncer",
     "M — ABAC es patrón establecido; la excepción auditada lo complica poco", "(A, M)"],
    ["AC-05", "Pico de 10x con presupuesto fijo",
     "A — STK-13: el lunes 8:30 ya colapsó una vez",
     "A — sin autoescalado ni hardware nuevo: solo arquitectura (caché, colas, réplicas)",
     "(A, A)"],
    ["AC-06", "Interoperabilidad legacy + nacional",
     "A — STK-07: plazo legal de 24 h",
     "M — cola local con reintento en ventana es patrón estándar", "(A, M)"],
    ["AC-07", "Mantenibilidad por el equipo interno",
     "A — STK-08: sin esto el sistema muere a los 12 meses",
     "M — la decisión dura es temprana (stack, módulos); después es disciplina", "(A, M)"],
    ["AC-08", "Integridad criptográfica de sensores",
     "M — STK-11: importante, pero parcialmente subsumido por AC-03",
     "M — hash encadenado es técnica conocida", "(M, M)"],
]

TOP_5 = [
    ["1", "AC-02", "Operación offline ≥ 4 h con reconciliación",
     "Conectividad: el enunciado da Wi-Fi inestable en el sótano y 50 Mbps compartidos — en el "
     "contexto local la intermitencia no es un caso raro, es el estado normal de la red. "
     "Diseñar asumiendo conexión confiable haría el sistema inútil justo donde opera la farmacia"],
    ["2", "AC-01", "Validación paciente-medicamento < 500 ms / < 2 s",
     "Dispositivos y red reales: el número hay que lograrlo en Toughpads Android 9 de 3 GB "
     "(gama baja, ya compradas — RE-14) y sobre la red degradada. En otro contexto se resuelve "
     "con mejor hardware; acá el hardware es un dato, no una variable"],
    ["3", "AC-05", "Pico de 10x con presupuesto fijo",
     "Presupuesto público: no hay autoescalado, no hay nube para lo sensible (RE-02, RE-13) y el "
     "presupuesto de un hospital nacional no crece con la demanda. El pico se absorbe con "
     "arquitectura o no se absorbe — el autoescalado, razonable en otro contexto, acá es inviable"],
    ["4", "AC-07", "Mantenibilidad por el equipo interno",
     "Capital humano: 3 personas de TI, rotación alta por contratos de 12 meses, y sin dinero "
     "para consultoras permanentes ni licencias (RE-03, RE-17). En este contexto, un sistema que "
     "solo su constructor puede mantener es un sistema muerto a mediano plazo — y condiciona la "
     "decisión más temprana de todas: el stack"],
    ["5", "AC-03", "Inmutabilidad y trazabilidad total",
     "Marco regulatorio local: la Contraloría General de Cuentas audita sin previo aviso y el "
     "proyecto nace de auditorías fallidas (Q 2.5 M perdidos, registros en papel). En la gestión "
     "pública guatemalteca la trazabilidad ante la Contraloría no es un plus: es la supervivencia "
     "institucional del proyecto"],
]


def priorizacion_dos_ejes():
    els = [
        titulo("Priorización — la matriz de los dos ejes · los 8 candidatos", 40, 40, 1300),
        texto("Método ADD: dos ejes, no una nota única. La IMPORTANCIA para el negocio la "
              "asignan los stakeholders; la DIFICULTAD o riesgo técnico, el arquitecto.\n"
              "Se ataca primero la intersección (A, A): alto valor y alta dificultad, donde una "
              "decisión equivocada cuesta más deshacerla.\n"
              "Compiten solo los drivers de calidad AC-nn: las restricciones NO se priorizan "
              "(todas se cumplen) y la funcionalidad tiene su completitud en §3.1.",
              40, 74, 1300, 13, align="left", _halo=False),
    ]
    cols = [("ID", 90), ("Driver", 300), ("Importancia (quién la sostiene)", 400),
            ("Dificultad (por qué)", 420), ("Par", 90)]
    rejilla, alto = tabla(40, 150, cols, DOS_EJES)
    els += rejilla
    els.append(_pie([
        "Tres quedan en (A, A) y cuatro en (A, M): para los dos lugares restantes se desempata "
        "con el contexto guatemalteco, que es exactamente lo que la rúbrica pide.",
    ], 40, 150 + alto + 30, 1300))
    return els


def priorizacion_top5():
    els = [
        titulo("Los 5 drivers más críticos según el contexto guatemalteco", 40, 40, 1300),
        texto("«Según el contexto guatemalteco» — interpretación declarada: la rúbrica lo exige "
              "y no lo define en ningún material de clase (pregunta pendiente para la "
              "catedrática).\n"
              "Mientras tanto se declara la interpretación: los ejes del contexto nacional que el "
              "propio enunciado pone sobre la mesa — marco regulatorio local (MSPAS, Contraloría,\n"
              "Ley de Acceso, INCAP), presupuesto público fijo sin autoescalado ni licencias "
              "renovables, infraestructura real (50 Mbps compartidos, Wi-Fi inestable), capital "
              "humano\n(3 personas de TI, alta rotación) y criticidad social (referencia nacional, "
              "1.200 pacientes diarios).",
              40, 74, 1300, 13, align="left", _halo=False),
    ]
    cols = [("#", 60), ("ID", 90), ("Driver", 280),
            ("Justificación en el contexto guatemalteco", 870)]
    rejilla, alto = tabla(40, 170, cols, TOP_5)
    els += rejilla
    els.append(_pie([
        "Por qué quedaron fuera los otros (A, M) — el desempate, dicho: AC-04 (ABAC) y AC-06 "
        "(interoperabilidad) son de importancia alta pero su dificultad es media porque se",
        "resuelven con patrones establecidos, que condicionan menos la estructura temprana que el "
        "stack (AC-07) o la inmutabilidad transversal (AC-03). Y AC-08 queda",
        "parcialmente cubierto por la decisión que se tome para AC-03.  Quedar fuera del top 5 NO "
        "los vuelve opcionales: siguen siendo drivers y entran a las matrices.",
    ], 40, 170 + alto + 30, 1300))
    return els


DIAGRAMAS = {
    "cdu-hospital": cdu_hospital,
    "contexto-centro-salud": contexto_centro_salud,
    "cdu-negocio-centro-salud": cdu_negocio_centro_salud,
    "cdu-core-farmahosp": cdu_core_farmahosp,
    "cdu-descomposicion-farmahosp": cdu_descomposicion_farmahosp,
    "cdu-expandido-prescripcion": cdu_expandido_prescripcion,
    "tabla-drivers-calidad": tabla_drivers_calidad,
    "matriz-1-stakeholders-cdu": matriz_stk_cdu,
    "matriz-2a-dependencias-rf": matriz_dependencias_rf,
    "matriz-2b-tronco-rf": matriz_tronco_rf,
    "matriz-3-cdu-rf": matriz_cdu_rf,
    "restricciones-explicitas": restricciones_explicitas,
    "restricciones-implicitas": restricciones_implicitas,
    "priorizacion-dos-ejes": priorizacion_dos_ejes,
    "priorizacion-top5": priorizacion_top5,
}
DIAGRAMAS.update({f"ficha-{k}": _ficha(k) for k in FICHAS_CALIDAD})

# Cada lamina vive en la carpeta de la SECCION DE LA ENTREGA que la usa, para
# que buscarla no requiera recordar como se llama el archivo: el nombre de la
# carpeta es el numero de seccion. Los ejemplos de otro dominio van aparte,
# porque no son del caso.
SUBCARPETA = {
    # §2 — el caso de negocio (criterio 1)
    "cdu-core-farmahosp": "2-caso-negocio",
    "cdu-descomposicion-farmahosp": "2-caso-negocio",
    # §3.1 — drivers RF (CDU expandidos)
    "cdu-expandido-prescripcion": "3.1-drivers-rf",
    # §3.3 — drivers de restriccion
    "restricciones-explicitas": "3.3-drivers-restriccion",
    "restricciones-implicitas": "3.3-drivers-restriccion",
    # §3.4 — priorizacion
    "priorizacion-dos-ejes": "3.4-priorizacion",
    "priorizacion-top5": "3.4-priorizacion",
    # §4 — matrices de trazabilidad
    "matriz-1-stakeholders-cdu": "4-matrices-trazabilidad",
    "matriz-2a-dependencias-rf": "4-matrices-trazabilidad",
    "matriz-2b-tronco-rf": "4-matrices-trazabilidad",
    "matriz-3-cdu-rf": "4-matrices-trazabilidad",
    # los casos que resolvio la catedratica y las demostraciones en otro dominio
    "cdu-hospital": "ejemplos-clase",
    "contexto-centro-salud": "ejemplos-clase",
    "cdu-negocio-centro-salud": "ejemplos-clase",
}
# §3.2 — drivers de atributos de calidad
SUBCARPETA["tabla-drivers-calidad"] = "3.2-drivers-calidad"
SUBCARPETA.update({f"ficha-{k}": "3.2-drivers-calidad" for k in FICHAS_CALIDAD})


# Dos carpetas de trabajo con la MISMA estructura: `practica/` para entrenar sin
# reloj y `examen/` para el dia del parcial. Cada una tiene las subcarpetas por
# seccion (para dejar ahi lo propio) y adentro `referencia/`, que es una COPIA
# de solo lectura de los .svg generados, con esas mismas subcarpetas.
# El original vive siempre en la carpeta de su seccion en 02-Diagramas.
DESTINOS = ["practica", "examen"]


def _refrescar_uno(base):
    """Rehace <base>/referencia/ y las carpetas de trabajo de <base>.

    Espeja las MISMAS subcarpetas por seccion que 02-Diagramas: si buscar una
    lamina requiere recordar en que carpeta esta, la copia tiene que estar en
    la misma carpeta o no sirve de referencia.
    """
    raiz = os.path.join("../02-Diagramas", base)
    referencia = os.path.join(raiz, "referencia")
    if os.path.isdir(referencia):
        shutil.rmtree(referencia)

    copiados = 0
    for nombre in DIAGRAMAS:
        carpeta = SUBCARPETA.get(nombre, "")
        origen = os.path.join("../02-Diagramas", carpeta, f"{nombre}.svg")
        if not os.path.exists(origen):
            print(f"  falta {origen} — generalo primero")
            continue
        destino = os.path.join(referencia, carpeta)
        os.makedirs(destino, exist_ok=True)
        shutil.copy2(origen, os.path.join(destino, f"{nombre}.svg"))
        copiados += 1

    # las carpetas de trabajo van vacias pero creadas: en el examen no se
    # pierde tiempo decidiendo donde guardar
    for carpeta in sorted(set(SUBCARPETA.values())):
        if carpeta == "ejemplos-clase":
            continue
        propia = os.path.join(raiz, carpeta)
        os.makedirs(propia, exist_ok=True)
        marca = os.path.join(propia, ".gitkeep")
        if not os.path.exists(marca):
            open(marca, "w").close()

    print(f"{raiz}/  —  referencia con {copiados} .svg + carpetas de trabajo")
    return copiados


def refrescar_referencia(cual=None):
    """--referencia [practica|examen]; sin argumento, las dos."""
    objetivos = [cual] if cual else DESTINOS
    for base in objetivos:
        if base not in DESTINOS:
            print(f"destino desconocido: {base}. Disponibles: {', '.join(DESTINOS)}")
            return 1
        _refrescar_uno(base)
    return 0


def main():
    if len(sys.argv) >= 2 and sys.argv[1] == "--referencia":
        return refrescar_referencia(sys.argv[2] if len(sys.argv) > 2 else None)

    if len(sys.argv) < 2:
        print(__doc__)
        for carpeta in sorted(set(SUBCARPETA.values())):
            laminas = [n for n in DIAGRAMAS if SUBCARPETA.get(n) == carpeta]
            print(f"\n{carpeta}/")
            for n in laminas:
                print(f"    {n}")
        return 1

    # sin nombre exacto: se acepta el nombre de una subcarpeta y se generan
    # todas sus laminas de una pasada
    pedido = sys.argv[1]
    if pedido in DIAGRAMAS:
        lote = [pedido]
    elif pedido in set(SUBCARPETA.values()):
        lote = [n for n in DIAGRAMAS if SUBCARPETA.get(n) == pedido]
    else:
        print(__doc__)
        print("Disponibles:", ", ".join(DIAGRAMAS))
        print("Carpetas:", ", ".join(sorted(set(SUBCARPETA.values()))))
        return 1

    for nombre in lote:
        # el contador de ids es global: sin reiniciarlo, generar una carpeta
        # entera en un solo proceso le da a la 2da lamina ids distintos que
        # generarla sola. El generador se documenta como DETERMINISTA, asi que
        # cada lamina arranca siempre en el001.
        _contador[0] = 0
        elementos = DIAGRAMAS[nombre]()
        destino = os.path.join("../02-Diagramas", SUBCARPETA.get(nombre, ""))
        os.makedirs(destino, exist_ok=True)

        ruta_ex = os.path.join(destino, f"{nombre}.excalidraw")
        with open(ruta_ex, "w", encoding="utf-8") as f:
            json.dump(envolver(elementos), f, ensure_ascii=False, indent=2)

        ruta_svg = os.path.join(destino, f"{nombre}.svg")
        with open(ruta_svg, "w", encoding="utf-8") as f:
            f.write(emitir_svg(elementos))

        print(f"{ruta_ex}   —  {len(elementos)} elementos (editable)")
        print(f"{ruta_svg}  —  vectorial, sin marca de agua")
    return 0



# ==========================================================================
# PRIMER PARCIAL 2026 — Caso "SmartPress" (AutoParts Guatemala S.A.)
#
# Frontera declarada: el negocio modelado es la GESTION DEL CONTROL DE
# CALIDAD EN LINEA de la produccion de piezas de precision, no la planta
# completa. Personas (operario, supervisor, ingeniero de calidad, director,
# equipo de TI) son TRABAJADORES; las areas y los sistemas externos son
# ACTORES DE NEGOCIO.
# ==========================================================================
def core_negocio_smartpress():
    els = []
    els += elipse_negocio(440, 330, 460, 200,
                          "Gesti\u00f3n del Control de Calidad\nen L\u00ednea de la Producci\u00f3n de\nPiezas de Precisi\u00f3n\n(SmartPress)", tam=15)

    els += actor_negocio(120, 60, "Proveedor de\nmateria prima")
    els += actor_negocio(560, 40, "\u00c1rea de Producci\u00f3n")
    els += actor_negocio(1000, 60, "Sistema de Control\nde M\u00e1quina (PLC)")
    els += actor_negocio(60, 430, "Cliente (ensambladora\nautomotriz)")
    els += actor_negocio(1120, 430, "Ente certificador\n(ISO 9001 / IATF 16949)")
    els += actor_negocio(300, 700, "\u00c1rea de Mantenimiento")
    els += actor_negocio(860, 700, "Sistemas legacy\n(ERP / Mantenimiento)")

    # asociaciones sin punta (molde de los cuatro cores de la catedra)
    els += linea(245, 140, 547, 345)
    els += linea(610, 175, 647, 330)
    els += linea(1030, 215, 790, 345)
    els += linea(185, 480, 446, 453)
    els += linea(1090, 480, 864, 453)
    els += linea(350, 670, 555, 516)
    els += linea(910, 670, 762, 522)
    return els


def descomposicion_smartpress():
    els = []
    EX, EW, EH = 460, 380, 100
    nombres = [
        "Recepci\u00f3n y calificaci\u00f3n\nde materia prima",
        "Preparaci\u00f3n y calibraci\u00f3n\nde la m\u00e1quina",
        "Monitoreo y control en l\u00ednea\ndel ciclo de producci\u00f3n",
        "Inspecci\u00f3n final y mejora\ndel modelo predictivo",
        "Trazabilidad, embarque y\nauditor\u00eda de calidad",
    ]
    ys = [60 + i * 150 for i in range(5)]
    for n, y in zip(nombres, ys):
        els += elipse_negocio(EX, y, EW, EH, n, tam=14)

    els.append(texto("N\u00daCLEO", 350, 400, 90, 12))
    els.append(texto("GERENCIAL", 340, 700, 110, 12))

    els += actor_negocio(120, 60, "Proveedor de\nmateria prima")
    els += actor_negocio(120, 280, "\u00c1rea de Producci\u00f3n")
    els += actor_negocio(120, 520, "\u00c1rea de Mantenimiento")
    els += actor_negocio(990, 60, "Sistemas legacy\n(ERP / Mantenimiento)")
    els += actor_negocio(990, 280, "Sistema de Control\nde M\u00e1quina (PLC)")
    els += actor_negocio(990, 470, "Sistema de medici\u00f3n\nl\u00e1ser (CMM)")
    els += actor_negocio(990, 650, "Cliente (ensambladora\nautomotriz)")
    els += actor_negocio(990, 830, "Ente certificador\n(ISO 9001 / IATF 16949)")

    els += linea(245, 105, 458, 110)
    els += linea(245, 320, 458, 262)
    els += linea(245, 340, 458, 405)
    els += linea(245, 560, 470, 440)
    els += linea(955, 120, 842, 258)
    els += linea(955, 330, 842, 410)
    els += linea(955, 520, 842, 560)
    els += linea(955, 700, 842, 706)
    els += linea(955, 880, 830, 748)
    return els


def cdu_expandido_monitoreo():
    """CUN-03 expandido — plano del SISTEMA (sin estereotipos de negocio)."""
    els = []
    els += caja(420, 40, 900, 810,
                "SmartPress \u2014 Monitoreo y control en l\u00ednea del ciclo",
                fondo=FONDO_SISTEMA, grosor=2)

    els += elipse(470, 220, 320, 100, "Supervisar ciclo de\nproducci\u00f3n en l\u00ednea", tam=15)
    els += elipse(970, 100, 310, 80, "Capturar mediciones de\nsensores v\u00eda OPC-UA", tam=13)
    els += elipse(970, 210, 310, 80, "Predecir calidad de la pieza\n(inferencia ML)", tam=13)
    els += elipse(970, 330, 310, 80, "Registrar trazabilidad\ndel ciclo", tam=13)
    els += elipse(960, 450, 330, 90, "Ejecutar acci\u00f3n correctiva\nsobre la m\u00e1quina", tam=13)
    els += elipse(470, 400, 320, 90, "Almacenar y reconciliar\ndesde buffer local", tam=13)
    els += elipse(960, 600, 330, 90, "Notificar deriva de sensor\na Mantenimiento", tam=13)
    els += elipse(470, 570, 320, 90, "Consultar tablero de\nestado en tiempo real", tam=13)
    els += elipse(470, 720, 320, 90, "Atender alerta de desviaci\u00f3n\ny acci\u00f3n sugerida", tam=13)

    els += actor(50, 180, "Operario de m\u00e1quina")
    els += actor(170, 460, "Personal de piso")
    els += actor(50, 740, "Supervisor de turno")
    els += actor(1400, 250, "Sistema de Control\nde M\u00e1quina (PLC)")

    # generalizacion: hijo -> padre, linea llena + triangulo hueco
    els += linea(150, 330, 205, 440, punta="triangle_outline")
    els += linea(150, 716, 202, 608, punta="triangle_outline")

    # asociaciones (sin punta)
    els += linea(185, 240, 470, 260)
    els += linea(295, 500, 468, 605)
    els += linea(185, 790, 470, 770)
    els += linea(1378, 265, 1290, 168)
    els += linea(1378, 300, 1294, 490)

    # include: BASE -> incluido, punteada
    els += linea(760, 240, 968, 150, punta="arrow", punteada=True,
                 etiqueta="\u00abinclude\u00bb", off=(20, -22))
    els += linea(790, 268, 968, 250, punta="arrow", punteada=True,
                 etiqueta="\u00abinclude\u00bb", off=(10, -16))
    els += linea(770, 300, 968, 370, punta="arrow", punteada=True,
                 etiqueta="\u00abinclude\u00bb", off=(30, 14))

    # extend: EXTENSION -> BASE, punteada, con la condicion entre corchetes
    els += linea(958, 482, 792, 292, punta="arrow", punteada=True,
                 etiqueta="\u00abextend\u00bb\n[predicci\u00f3n = defectuosa]", off=(58, 34))
    els += linea(630, 398, 630, 322, punta="arrow", punteada=True,
                 etiqueta="\u00abextend\u00bb\n[ca\u00edda de red]", off=(-118, 6))
    els += linea(958, 630, 794, 316, punta="arrow", punteada=True,
                 etiqueta="\u00abextend\u00bb\n[deriva de sensor]", off=(122, 84))
    return els


def cdu_expandido_trazabilidad():
    """CUN-05 expandido — plano del SISTEMA."""
    els = []
    els += caja(420, 40, 900, 700,
                "SmartPress \u2014 Trazabilidad, embarque y auditor\u00eda",
                fondo=FONDO_SISTEMA, grosor=2)

    els += elipse(470, 160, 330, 100, "Gestionar la trazabilidad\nde la pieza producida", tam=14)
    els += elipse(970, 95, 310, 80, "Etiquetar pieza con\nc\u00f3digo QR \u00fanico", tam=13)
    els += elipse(970, 215, 310, 80, "Sellar registro de\nproducci\u00f3n inmutable", tam=13)
    els += elipse(960, 320, 330, 90, "Registrar inspecci\u00f3n CMM y\ncorrelacionar con producci\u00f3n", tam=13)
    els += elipse(470, 420, 330, 100, "Consultar trazabilidad\nforense de un lote", tam=14)
    els += elipse(960, 480, 330, 90, "Verificar integridad del\nregistro inmutable", tam=13)
    els += elipse(470, 580, 330, 100, "Emitir expediente de\ncalidad del embarque", tam=14)

    els += actor(150, 140, "Ingeniero de Calidad")
    els += actor(150, 390, "Auditor externo\n(ISO / IATF)")
    els += actor(150, 640, "Cliente (ensambladora\nautomotriz)")
    els += actor(1400, 320, "Sistema de medici\u00f3n\nl\u00e1ser (CMM)")

    els += linea(275, 190, 468, 208)
    els += linea(275, 430, 468, 455)
    els += linea(275, 670, 474, 505)
    els += linea(275, 690, 468, 640)
    els += linea(1378, 360, 1294, 365)

    els += linea(780, 180, 968, 140, punta="arrow", punteada=True,
                 etiqueta="\u00abinclude\u00bb", off=(14, -20))
    els += linea(800, 208, 968, 255, punta="arrow", punteada=True,
                 etiqueta="\u00abinclude\u00bb", off=(8, -18))
    els += linea(800, 470, 958, 512, punta="arrow", punteada=True,
                 etiqueta="\u00abinclude\u00bb", off=(6, -20))
    els += linea(958, 350, 792, 240, punta="arrow", punteada=True,
                 etiqueta="\u00abextend\u00bb\n[pieza en el muestreo 5%]", off=(60, 30))
    return els


DIAGRAMAS.update({
    "core-negocio-smartpress": core_negocio_smartpress,
    "descomposicion-smartpress": descomposicion_smartpress,
    "cdu-expandido-monitoreo": cdu_expandido_monitoreo,
    "cdu-expandido-trazabilidad": cdu_expandido_trazabilidad,
})
SUBCARPETA.update({
    "core-negocio-smartpress": "examen/2-caso-negocio",
    "descomposicion-smartpress": "examen/2-caso-negocio",
    "cdu-expandido-monitoreo": "examen/3.1-drivers-rf",
    "cdu-expandido-trazabilidad": "examen/3.1-drivers-rf",
})



# --------------------------------------------------------------------------
# PARCIAL — Diagrama de CONTEXTO de SmartPress
#
# Convenios de la catedra: ELIPSE = El Producto (un solo ovalo, nombra un
# SISTEMA) · RECTANGULO = entidades o agentes externos · FLECHA = streamline,
# SIEMPRE con nombre y en sustantivo. Ojo: aca las flechas SI son flujos de
# informacion con nombre (a diferencia del CDU, donde la navegabilidad solo
# indica quien inicia).
# --------------------------------------------------------------------------
def contexto_smartpress():
    els = []
    els += elipse(700, 440, 380, 180,
                  "SmartPress\nSistema de Control de Calidad\nen L\u00ednea de Producci\u00f3n", tam=16)

    RW, RH = 260, 80
    els += entidad(120, 100, RW, RH, "Proveedor de\nmateria prima")
    els += entidad(120, 260, RW, RH, "Sistema de Control\nde M\u00e1quina (PLC)")
    els += entidad(120, 420, RW, RH, "Sistema de medici\u00f3n\nl\u00e1ser (CMM)")
    els += entidad(120, 580, RW, RH, "Sistemas legacy\n(ERP / Mantenimiento)")
    els += entidad(120, 740, RW, RH, "\u00c1rea de\nMantenimiento")

    els += entidad(1520, 100, RW, RH, "Operario de m\u00e1quina")
    els += entidad(1520, 260, RW, RH, "Supervisor de turno")
    els += entidad(1520, 420, RW, RH, "Ingeniero de Calidad")
    els += entidad(1520, 580, RW, RH, "Director de Planta")
    els += entidad(1520, 740, RW, RH, "Cliente (ensambladora\nautomotriz)")

    els += entidad(760, 860, RW, RH, "Ente certificador\n(ISO 9001 / IATF 16949)")

    # --- streamlines de ENTRADA (entidad -> El Producto)
    els += linea(382, 140, 790, 453, punta="arrow",
                 etiqueta="Certificado de calidad\ndel lote", off=(-30, -46))
    els += linea(382, 300, 753, 468, punta="arrow",
                 etiqueta="Mediciones de sensores\n(OPC-UA)", off=(-20, -44))
    els += linea(382, 460, 708, 505, punta="arrow",
                 etiqueta="Resultados de\ninspecci\u00f3n dimensional", off=(-10, 26))
    els += linea(382, 620, 712, 562, punta="arrow",
                 etiqueta="\u00d3rdenes de producci\u00f3n\ny programaci\u00f3n", off=(0, 20))
    els += linea(1518, 480, 1072, 530, punta="arrow",
                 etiqueta="Configuraci\u00f3n del\nmodelo predictivo", off=(0, 20))

    # --- streamlines de SALIDA (El Producto -> entidad)
    els += linea(748, 490, 384, 330, punta="arrow",
                 etiqueta="Orden de ajuste\nde par\u00e1metros", off=(-20, -2))
    els += linea(758, 595, 384, 780, punta="arrow",
                 etiqueta="Aviso de deriva\nde sensor", off=(-30, 24))
    els += linea(1005, 458, 1518, 140, punta="arrow",
                 etiqueta="Alerta de desviaci\u00f3n\nen tiempo real", off=(30, -44))
    els += linea(1040, 475, 1518, 300, punta="arrow",
                 etiqueta="Tablero de desempe\u00f1o\ndel turno", off=(20, -44))
    els += linea(1075, 509, 1518, 450, punta="arrow",
                 etiqueta="Datos hist\u00f3ricos\nde proceso", off=(0, -44))
    els += linea(1072, 556, 1518, 620, punta="arrow",
                 etiqueta="Indicadores de calidad\ny costo de scrap", off=(0, 20))
    els += linea(1035, 588, 1518, 780, punta="arrow",
                 etiqueta="Expediente de trazabilidad\nde la pieza", off=(30, 22))
    els += linea(890, 622, 890, 856, punta="arrow",
                 etiqueta="Registro de auditor\u00eda\ninmutable", off=(120, -10))

    return els


DIAGRAMAS["contexto-smartpress"] = contexto_smartpress
SUBCARPETA["contexto-smartpress"] = "examen/2-caso-negocio"



# ==========================================================================
# PARCIAL SmartPress — láminas de DRIVERS y MATRICES
# Todas viven bajo 02-Diagramas/examen/<sección>/.
# No son diagramas: son tablas. Un atributo de calidad NO es un caso de uso
# (estilo-diagramas.md §8), y las matrices de trazabilidad tampoco.
# ==========================================================================

RF_SMARTPRESS = [
    ["RFG-001", "Capturar 500 mediciones/s por máquina en 25 máquinas, en tiempo real, vía OPC-UA",
     "CUN-03", "CU-002 (principal), CU-001, CU-006"],
    ["RFG-002", "Ejecutar inferencia ML sobre las 500 mediciones y predecir la calidad antes de que termine el ciclo",
     "CUN-03", "CU-003 (principal), CU-001"],
    ["RFG-003", "Enviar orden de ajuste o de paro al PLC cuando la predicción es «defectuosa»",
     "CUN-03", "CU-005 (principal), CU-001"],
    ["RFG-004", "Registrar trazabilidad completa por pieza: máquina, turno, operario, lote, parámetros e inspección",
     "CUN-03, CUN-05", "CU-004 (principal), CU-010, CU-012"],
    ["RFG-005", "Etiquetar cada pieza con un código QR único que porte su expediente",
     "CUN-05", "CU-011 (principal), CU-010, CU-016"],
    ["RFG-006", "Sellar los registros de producción de forma inmutable y verificable",
     "CUN-05", "CU-012 (principal), CU-015"],
    ["RFG-007", "Correlacionar la inspección CMM (15 dimensiones, 5% de piezas) con los datos de producción y reentrenar",
     "CUN-04, CUN-05", "CU-013 (principal), CU-003"],
    ["RFG-008", "Consultar trazabilidad forense de un lote sobre el histórico de 7 años",
     "CUN-05", "CU-014 (principal), CU-015"],
    ["RFG-009", "Detectar deriva de sensores y notificar a Mantenimiento antes de que cause defectos",
     "CUN-03", "CU-007 (principal), CU-002"],
    ["RFG-010", "Presentar tablero de estado y desempeño de turno en tiempo real, con acción correctiva sugerida",
     "CUN-03", "CU-008 (principal), CU-009"],
    ["RFG-011", "Bufferizar localmente y reconciliar al reconectar, sin pérdida de mediciones",
     "CUN-03", "CU-006 (principal), CU-002, CU-004"],
    ["RFG-012", "Integrarse con ERP y sistema de mantenimiento legacy (REST, 1-2 s) para órdenes y programación",
     "CUN-02", "— (no expandido)"],
    ["RFG-013", "Registrar el lote de materia prima, sus propiedades y el certificado del proveedor",
     "CUN-01", "— (no expandido)"],
    ["RFG-014", "Actualizar el modelo predictivo (shadow, A/B, canary) sin detener la producción",
     "CUN-04", "— (no expandido)"],
]


def drivers_rf_smartpress():
    els = [
        titulo("Drivers de Requisitos Funcionales — SmartPress", 40, 40, 1420),
        texto("«Funcionalidades específicas que MOLDEAN la estructura». Se entregan como CDU expandidos: "
              "los de CUN-03 y CUN-05 están dibujados (3.1-drivers-rf);\nlos de CUN-01, CUN-02 y CUN-04 quedan sin "
              "expandir porque el enunciado pide solamente 2 CUN.",
              40, 76, 1420, 13, align="left", _halo=False),
    ]
    cols = [("ID", 110), ("Driver RF", 660), ("CUN de origen", 170), ("CU del sistema que lo realiza", 400)]
    rejilla, _ = tabla(40, 140, cols, RF_SMARTPRESS)
    return els + rejilla


# --- Atributos de calidad: resumen y escenarios de SEIS partes ------------
AC_RESUMEN = [
    ["AC-01", "Rendimiento (latencia)", "Inferencia ML dentro del ciclo de producción",
     "< 1 s (ciclo 45 s) y < 5 s (ciclo 120 s)",
     "Procesamiento en el BORDE: la latencia a internet es impredecible y no cabe en la ventana del ciclo"],
    ["AC-02", "Rendimiento (respuesta de control)", "El PLC pide una orden de ajuste",
     "< 200 ms extremo a extremo",
     "Separar el canal de control del canal de analítica: el lazo duro no comparte cola ni recursos"],
    ["AC-03", "Disponibilidad / fiabilidad", "Caída de red de 30 s durante la producción",
     "0 mediciones pérdidas, 100% de trazabilidad reconstruida, 0 cortes visibles",
     "Store-and-forward con buffer local en el borde y reconciliación idempotente"],
    ["AC-04", "Escalabilidad", "Pico de volumen 10x en el turno de la noche",
     "Se mantiene AC-01 (p95) con 10x el caudal, sin pérdida de mensajes",
     "Ingesta desacoplada por cola y particionamiento por máquina y por tiempo"],
    ["AC-05", "Seguridad (integridad y autenticación)", "Se emite una orden de ajuste al PLC",
     "100% de órdenes firmadas, 0 aceptadas sin firma válida, 0 bytes en texto plano",
     "Broker de comandos con firma digital y autenticación mutua sobre OPC-UA"],
    ["AC-06", "Seguridad (no repudio) / consulta", "Consulta forense de un lote de hace 7 años",
     "< 10 min de respuesta, 7 años de retención, 100% verificable por hash",
     "Almacenamiento por niveles (caliente/tibio/frío) + registro WORM con hash encadenado"],
    ["AC-07", "Mantenibilidad", "El científico de datos consultor se retira a los 6 meses",
     "Traspaso <= 6 meses con US$ 20,000; despliegue de modelo con 0 s de paro",
     "LIMITA el número de componentes y de tecnologías: solo lo que 4 personas pueden operar"],
    ["AC-08", "Usabilidad", "Operario que rota de turno toma la estación por primera vez",
     "<= 3 horas de capacitación",
     "Capa de presentación de piso reducida, distinta del tablero del supervisor"],
]


def drivers_calidad_smartpress():
    els = [
        titulo("Drivers de atributos de calidad — SmartPress (resumen)", 40, 40, 1600),
        texto("Taxonomia declarada: las SIETE de clase (rendimiento, escalabilidad, disponibilidad, seguridad, "
              "mantenibilidad, usabilidad, fiabilidad). No se mezcla con ISO 9126 ni FURPS.\n"
              "Todos llevan número: un driver de calidad sin medida no es un driver, es un deseo. "
              "El escenario completo de seis partes está en la lámina siguiente.",
              40, 76, 1600, 13, align="left", _halo=False),
    ]
    cols = [("ID", 90), ("Atributo", 250), ("Escenario (resumen)", 340),
            ("MEDIDA", 400), ("Foco arquitectónico: que decisión fuerza", 520)]
    rejilla, _ = tabla(40, 140, cols, AC_RESUMEN)
    return els + rejilla


AC_ESCENARIOS = [
    ["AC-01", "Sensores de la máquina", "Se completan las 500 mediciones de un ciclo",
     "Motor de inferencia ML", "Producción normal, 25 máquinas", "Emite la predicción de calidad de la pieza",
     "< 1 s (ciclo 45 s) / < 5 s (ciclo 120 s)"],
    ["AC-02", "PLC Siemens S7-1500", "Envía una solicitud de ajuste vía OPC-UA",
     "Servicio de control", "Red industrial Ethernet/IP, 5 ms", "Responde con la orden de ajuste",
     "< 200 ms extremo a extremo"],
    ["AC-03", "Red industrial", "Caída de red de 30 s", "Ingesta + buffer local",
     "Planta 24/7, 3 turnos", "Conserva el buffer, reconstruye la trazabilidad y sigue operando",
     "0 mediciones pérdidas; 100% de piezas trazables; 0 cortes visibles"],
    ["AC-04", "Turno de la noche", "El volumen de datos sube 10x", "Pipeline de ingesta y almacenamiento",
     "Presupuesto de infraestructura fijo", "Absorbe el pico sin degradar el servicio",
     "Se mantiene AC-01 (p95) con 10x el caudal"],
    ["AC-05", "Emisor de una orden (o un atacante)", "Se emite «reducir temperatura 3 °C»",
     "Canal de comandos al PLC", "Red de planta", "Solo se ejecutan órdenes firmadas y autenticadas",
     "100% firmadas; 0 aceptadas sin firma válida; TLS obligatorio"],
    ["AC-06", "Auditor IATF o cliente con reclamo", "Consulta forense de un lote de hace 7 años",
     "Repositorio histórico", "1.3 PB acumulados", "Devuelve el expediente completo y verificable",
     "< 10 min; retención 7 años; 100% con hash verificable"],
    ["AC-07", "Equipo de TI interno (4 personas)", "El científico de datos se retira a los 6 meses",
     "Sistema completo, incluido el pipeline de ML", "US$ 20,000 de capacitación",
     "El equipo opera, respalda, recupera y despliega modelos",
     "Traspaso <= 6 meses; 0 s de paro al desplegar un modelo"],
    ["AC-08", "Operario de máquina que rota de turno", "Se le asigna la estación por primera vez",
     "Interfaz de piso", "Personal sin perfil técnico", "Opera el tablero y atiende alertas sin asistencia",
     "<= 3 horas de capacitación"],
]


def escenarios_calidad_smartpress():
    els = [
        titulo("Drivers de calidad — escenarios de SEIS partes", 40, 40, 1700),
        texto("Fuente · Estímulo · Artefacto · Entorno · Respuesta · MEDIDA. La última columna va sombreada: "
              "es la que convierte el deseo en driver.\nUn atributo de calidad NO es un caso de uso; no se dibuja "
              "como elipse, se especifica como escenario.",
              40, 76, 1700, 13, align="left", _halo=False),
    ]
    cols = [("ID", 80), ("Fuente", 230), ("Estímulo", 280), ("Artefacto", 240),
            ("Entorno", 220), ("Respuesta", 300), ("MEDIDA", 330)]
    rejilla, _ = tabla(40, 140, cols, AC_ESCENARIOS)
    return els + rejilla


# --- Restricciones: las TRES categorías que pide el enunciado -------------
RES_TECNICAS = [
    ["RES-T01", "El protocolo con las máquinas debe ser OPC-UA; no se puede sustituir", "Junta Directiva",
     "Descarta cualquier protocolo propio o más liviano para el lazo de control"],
    ["RES-T02", "25 PLC Siemens S7-1500, 500 mediciones/s cada uno", "Infraestructura de planta",
     "Fija el caudal de ingesta: 12,500 mediciones/s en régimen normal"],
    ["RES-T03", "Red industrial Ethernet/IP, 5 ms de latencia, con caídas esporádicas", "Infraestructura de planta",
     "Prohíbe asumir red confiable: obliga a buffer local (AC-03)"],
    ["RES-T04", "Internet de 100 Mbps compartido; no se puede depender únicamente de la nube para tiempo real",
     "Infraestructura / Junta", "Descarta la inferencia en la nube; obliga a cómputo en el borde"],
    ["RES-T05", "Data center local: 4 servidores VMware, 64 vCPU, 256 GB RAM, 20 TB SAN", "Infraestructura",
     "20 TB se agotan en 4 días de datos crudos: descarta guardar todo on-premise"],
    ["RES-T06", "No se pueden almacenar todos los datos crudos de sensores en la base transaccional",
     "Junta Directiva", "PROHIBE de frente la tabla única SensorReadings de la Parte III"],
    ["RES-T07", "La base de datos debe soportar particionamiento y retención de datos", "Junta Directiva",
     "Descarta una tabla plana sin estrategia de partición"],
    ["RES-T08", "No se puede diseñar un sistema monolítico: ingesta, ML y trazabilidad escalan distinto",
     "Junta Directiva", "Obliga a servicios desplegables por separado (y tensiona con AC-07)"],
    ["RES-T09", "Los datos de producción deben viajar cifrados; nada en texto plano por la red",
     "Política de seguridad", "Obliga a TLS en todo canal, incluido el de comandos"],
    ["RES-T10", "A la nube solo pueden salir análisis agregados; los datos crudos no salen de la planta",
     "Política de seguridad", "Define qué capa puede externalizarse: la tibia, nunca la cruda"],
    ["RES-T11", "Stack del equipo: .NET, SQL Server, Azure, Angular; ML en Python/TensorFlow/Scikit-learn",
     "Equipo y habilidades", "Acota las tecnologías elegibles a lo que 4 personas pueden operar"],
]

RES_NEGOCIO = [
    ["RES-N01", "Presupuesto de infraestructura: US$ 150,000 para el próximo año (hardware, licencias y cloud)",
     "Presupuesto", "Descarta ampliar la SAN a escala de petabytes"],
    ["RES-N02", "Presupuesto de capacitación: US$ 20,000", "Presupuesto",
     "Limita cuantas tecnologías nuevas puede absorber el equipo"],
    ["RES-N03", "Equipo interno de 4 personas, sin experiencia en Big Data ni ML", "Equipo y habilidades",
     "Es el techo real de complejidad operativa del sistema"],
    ["RES-N04", "El científico de datos es consultor y está disponible solo 6 meses", "Equipo y habilidades",
     "Obliga a que el pipeline de ML sea operable sin el (AC-07)"],
    ["RES-N05", "La planta opera 24/7 en 3 turnos: no se puede parar la producción para mantenimiento ni actualizaciones",
     "Junta Directiva", "Obliga a despliegue canary / shadow y a cero ventana de mantenimiento"],
    ["RES-N06", "ISO 9001: trazabilidad de toda acción que afecte la calidad", "Regulación",
     "Obliga a bitácora de acciones, no solo de mediciones"],
    ["RES-N07", "IATF 16949: los sistemas de control de calidad deben ser validados y los cambios gestionados formalmente",
     "Regulación", "Obliga a inmutabilidad, versionado de modelos y gestión formal de cambios"],
    ["RES-N08", "Retención legal de los datos de producción: 7 años", "Regulación",
     "1.3 PB acumulados: obliga a archivo frío por niveles"],
    ["RES-N09", "Confidencialidad: los datos de producción no pueden salir de la planta en texto plano",
     "Política de la empresa", "Refuerza RES-T10 y descarta SaaS de analítica sobre datos crudos"],
    ["RES-N10", "La capacitación de un operario no puede exceder 3 horas", "Junta Directiva",
     "Descarta una interfaz de piso rica: obliga a separarla del tablero del supervisor"],
    ["RES-N11", "US$ 2.5 millones en penalizaciones en 6 meses justifican el proyecto", "Caso de negocio",
     "Acota el plazo: la solución debe dar resultado antes de que el cliente rescinda"],
]

RES_SISTEMA = [
    ["RES-S01", "Integración con el ERP legacy (Oracle Forms) por API REST lenta: 1-2 s de respuesta",
     "Expectativa 8 del cliente", "Prohíbe consultar el ERP dentro del lazo de tiempo real: obliga a caché"],
    ["RES-S02", "Integración con el sistema de mantenimiento legacy, con la misma limitación",
     "Expectativa 8 del cliente", "Obliga a sincronización asincrónica de la programación de mantenimiento"],
    ["RES-S03", "Integración con 25 PLC simultaneos vía OPC-UA, en lectura y escritura",
     "Infraestructura de planta", "Define la topología de conectores en el borde, uno por máquina"],
    ["RES-S04", "Integración con el CMM: inspección destructiva, 3 min por pieza, solo el 5% de las piezas",
     "Etapa 4 del proceso", "El reentrenamiento solo dispone del 5% etiquetado: condiciona el diseño del modelo"],
    ["RES-S05", "El código QR es el contrato de trazabilidad con el cliente: su contenido y verificación son externos",
     "Etapa 5 del proceso", "Fija el formato del expediente por pieza como interfaz pública"],
]


def _lamina_restricciones(titulo_txt, subtitulo, datos, ancho_res=640):
    def construir():
        ancho = 110 + ancho_res + 250 + 520
        els = [
            titulo(titulo_txt, 40, 40, ancho),
            texto(subtitulo, 40, 76, ancho, 13, align="left", _halo=False),
        ]
        cols = [("ID", 110), ("Restricción", ancho_res), ("Origen", 250),
                ("Qué decisión bloquea", 520)]
        rejilla, _ = tabla(40, 140, cols, datos)
        return els + rejilla
    return construir


SUB_RES = ("Las restricciones NO se priorizan: todas son obligatorias, y ninguna lleva medida (se cumple o no se cumple).\n"
           "Clasificadas en las TRES categorías que pide el enunciado — Técnicas, de Negocio y de Sistema —, "
           "no en las seis de clase. La última columna es la que las convierte en driver.")


# --- Matrices de trazabilidad --------------------------------------------
CU_COLS = ["CU-001", "CU-002", "CU-003", "CU-004", "CU-005", "CU-006", "CU-007", "CU-008",
           "CU-009", "CU-010", "CU-011", "CU-012", "CU-013", "CU-014", "CU-015", "CU-016"]

P, X, _n = "\u25cf", "X", ""
RF_CU = [
    ("RFG-001  Capturar 500 med/s v\u00eda OPC-UA",   [X, P, _n, _n, _n, X, _n, _n, _n, _n, _n, _n, _n, _n, _n, _n]),
    ("RFG-002  Inferencia ML dentro del ciclo",   [X, _n, P, _n, _n, _n, _n, _n, _n, _n, _n, _n, _n, _n, _n, _n]),
    ("RFG-003  Orden de ajuste / paro al PLC",    [X, _n, _n, _n, P, _n, _n, _n, X, _n, _n, _n, _n, _n, _n, _n]),
    ("RFG-004  Trazabilidad completa por pieza",  [X, _n, _n, P, _n, X, _n, _n, _n, X, _n, X, _n, X, _n, X]),
    ("RFG-005  Etiquetado QR \u00fanico",            [_n, _n, _n, _n, _n, _n, _n, _n, _n, X, P, _n, _n, X, _n, X]),
    ("RFG-006  Sellado inmutable y verificable",  [_n, _n, _n, X, _n, _n, _n, _n, _n, X, _n, P, _n, _n, X, _n]),
    ("RFG-007  Correlacionar CMM y reentrenar",   [_n, _n, X, X, _n, _n, _n, _n, _n, X, _n, _n, P, _n, _n, _n]),
    ("RFG-008  Consulta forense a 7 a\u00f1os",      [_n, _n, _n, X, _n, _n, _n, _n, _n, _n, _n, X, _n, P, X, _n]),
    ("RFG-009  Detectar deriva de sensores",      [X, X, _n, _n, _n, _n, P, _n, X, _n, _n, _n, X, _n, _n, _n]),
    ("RFG-010  Tablero en tiempo real",           [X, _n, X, _n, _n, _n, X, P, X, _n, _n, _n, _n, _n, _n, _n]),
    ("RFG-011  Buffer local y reconciliaci\u00f3n",  [X, X, _n, X, _n, P, _n, _n, _n, _n, _n, _n, _n, _n, _n, _n]),
    ("RFG-014  Actualizar modelo sin parar",      [_n, _n, X, _n, _n, _n, _n, _n, _n, _n, _n, _n, X, _n, _n, _n]),
]


def matriz_rf_cdu_smartpress():
    els = [
        titulo("Matriz de trazabilidad — Drivers RF vs. CDU (SmartPress)", 40, 40, 1740),
        texto("Plantilla de la NT1, figura 1, pág. 91.   Celda:  ● = caso de uso PRINCIPAL (dueño del "
              "requerimiento)  ·  X = participa en su realización  ·  vacío = no interviene.\n"
              "RFG-012 y RFG-013 no aparecen: pertenecen a CUN-01 y CUN-02, que el enunciado no manda expandir.",
              40, 76, 1740, 13, align="left", _halo=False),
    ]
    rejilla, alto = matriz(40, 140, "Requerimiento", 400, CU_COLS, 90, RF_CU)
    els += rejilla
    els.append(_pie([
        "Lectura por fila — ¿dónde se realiza cada requerimiento?  Ninguna fila vacía: todo RF expandido "
        "tiene al menos un CU dueño.",
        "Lectura por columna — ¿de dónde viene cada caso de uso?  Ninguna columna vacía: no hay CU inventado "
        "sin requerimiento que lo origine.",
        "La columna más poblada es CU-004 (Registrar trazabilidad del ciclo), coherente con que la pérdida de "
        "trazabilidad sea el problema que originó el proyecto.",
    ], 40, 140 + alto + 30, 1740))
    return els


CTRL_COLS = ["CU-002", "CU-003", "CU-004", "CU-005", "CU-012", "CU-013", "CU-014", "CU-015"]
T = "▲"
CONTROL = [
    ["AC-01  Inferencia < 1 s / < 5 s", "Calidad", X, P, _n, _n, _n, _n, _n, _n,
     T + " La escritura sincrónica en la tabla única roba tiempo al ciclo de inferencia"],
    ["AC-02  Respuesta al PLC < 200 ms", "Calidad", X, _n, _n, P, _n, _n, _n, _n,
     T + " La contención de escritura en la misma instancia degrada el lazo de control"],
    ["AC-03  Caída de red 30 s sin pérdida", "Calidad", X, _n, X, _n, _n, _n, _n, _n,
     "Exige buffer en el borde, no una tabla central única"],
    ["AC-04  Pico de 10x sin degradación", "Calidad", P, _n, X, _n, _n, _n, _n, _n,
     T + " 125,000 filas/s contra índices B-tree: el diseño no escala"],
    ["AC-05  Órdenes firmadas y autenticadas", "Calidad", _n, _n, _n, P, X, _n, _n, X,
     "Canal de comandos separado del almacén de datos"],
    ["AC-06  Forense < 10 min sobre 7 años", "Calidad", _n, _n, X, _n, P, _n, P, X,
     T + " Imposible sobre EAV plano: exige niveles e índice de trazabilidad"],
    ["AC-07  Mantenible por 4 personas", "Calidad", X, X, X, _n, X, X, X, _n,
     T + " Justifica SQL Server para el MAESTRO de trazabilidad, no para el crudo"],
    ["RES-T06  Nada crudo en la transaccional", "Restricción", P, _n, P, _n, _n, _n, _n, _n,
     T + " PROHIBICIÓN EXPLÍCITA: la decisión del equipo la viola de frente"],
    ["RES-T07  BD con particionamiento y retención", "Restricción", X, _n, P, _n, X, _n, X, _n,
     T + " Una tabla plana sin estrategia de partición no cumple"],
    ["RES-T05  20 TB de SAN", "Restricción", X, _n, X, _n, _n, _n, X, _n,
     T + " 5 TB/día agotan la SAN en 4 días"],
    ["RES-N08  Retención 7 años (1.3 PB)", "Restricción", _n, _n, X, _n, X, _n, P, X,
     T + " Obliga a archivo frío por niveles, no a una tabla única"],
    ["RES-N06/N07  ISO 9001 / IATF 16949", "Restricción", _n, _n, X, X, P, X, X, P,
     T + " Exigen inmutabilidad y validación, que la tabla plana no ofrece"],
    ["RES-T10  Solo agregados a la nube", "Restricción", X, _n, X, _n, _n, _n, _n, _n,
     "Define qué capa puede salir de la planta"],
]


def matriz_control_smartpress():
    ancho = 380 + 130 + 8 * 92 + 620
    els = [
        titulo("Matriz de control — Drivers de calidad y restricción vs. CDU", 40, 40, ancho),
        texto("Responde a la Parte III: son los drivers que, de haberse trazado, habrían impedido la decisión de la "
              "tabla única SensorReadings.\nCelda:  ● = el CU es el punto donde el driver se realiza o se viola  "
              "·  X = el driver lo condiciona  ·  ▲ = control directo sobre la decisión cuestionada.",
              40, 76, ancho, 13, align="left", _halo=False),
    ]
    cols = ([("Driver", 380), ("Tipo", 130)]
            + [(c, 92) for c in CTRL_COLS]
            + [("Control sobre la decisión de SensorReadings", 620)])
    alin = ["left", "left"] + ["center"] * 8 + ["left"]
    rejilla, alto = tabla(40, 140, cols, CONTROL, alineaciones=alin)
    els += rejilla
    els.append(_pie([
        "1.  RES-T06 cruza CU-002 y CU-004 — los dos casos de uso que la tabla única pretendía servir. "
        "La celda está marcada: la restricción habría bloqueado la decisión antes de la primera línea de SQL.",
        "2.  La columna CU-004 concentra 9 drivers de control. Un caso de uso con esa densidad de restricciones "
        "es un punto de ARQUITECTURA, no de implementación.",
        "3.  AC-07 aparece a favor y en contra: la mantenibilidad justifica SQL Server, pero solo donde el volumen "
        "lo permite. Trazado por caso de uso, el argumento del equipo se salva a medias en vez de perderse entero.",
    ], 40, 140 + alto + 30, ancho))
    return els


DIAGRAMAS.update({
    "drivers-rf-smartpress": drivers_rf_smartpress,
    "drivers-calidad-smartpress": drivers_calidad_smartpress,
    "escenarios-calidad-smartpress": escenarios_calidad_smartpress,
    "restricciones-tecnicas-smartpress": _lamina_restricciones(
        "Drivers de restricción — TÉCNICAS (tecnologías y plataformas)", SUB_RES, RES_TECNICAS),
    "restricciones-negocio-smartpress": _lamina_restricciones(
        "Drivers de restricción — DE NEGOCIO (presupuesto, tiempo, leyes y normativas)", SUB_RES, RES_NEGOCIO),
    "restricciones-sistema-smartpress": _lamina_restricciones(
        "Drivers de restricción — DE SISTEMA (interacción con otros sistemas)", SUB_RES, RES_SISTEMA),
    "matriz-rf-cdu-smartpress": matriz_rf_cdu_smartpress,
    "matriz-control-smartpress": matriz_control_smartpress,
})
SUBCARPETA.update({
    "drivers-rf-smartpress": "examen/3.1-drivers-rf",
    "drivers-calidad-smartpress": "examen/3.2-drivers-calidad",
    "escenarios-calidad-smartpress": "examen/3.2-drivers-calidad",
    "restricciones-tecnicas-smartpress": "examen/3.3-drivers-restriccion",
    "restricciones-negocio-smartpress": "examen/3.3-drivers-restriccion",
    "restricciones-sistema-smartpress": "examen/3.3-drivers-restriccion",
    "matriz-rf-cdu-smartpress": "examen/4-matrices-trazabilidad",
    "matriz-control-smartpress": "examen/4-matrices-trazabilidad",
})


# ==========================================================================
# TAREA 2 — FarmaHosp (continuación): criterio 6, bloques y despliegue
#
# Datos copiados de `08-Tareas/Entrega - Tarea 2 FarmaHosp.md` §5 y §6.
# Si cambia la Entrega, se cambia aca.
# ==========================================================================
def _rect(x, y, w, h, fondo="transparent", punteado=False, grosor=1, redondo=False):
    kw = dict(backgroundColor=fondo, strokeWidth=grosor,
              strokeStyle="dashed" if punteado else "solid")
    if redondo:
        kw["roundness"] = {"type": 3}
    return _base("rectangle", x, y, w, h, **kw)


def bloque(x, y, w, h, etiqueta, fondo="transparent", tam=13, punteado=False):
    """Bloque del diagrama de alto nivel: rectangulo con el texto centrado."""
    lineas = etiqueta.split("\n")
    ty = y + h / 2 - (tam * 1.25 * len(lineas)) / 2
    return [_rect(x, y, w, h, fondo, punteado, redondo=True),
            texto(etiqueta, x + 6, int(ty), w - 12, tam, _halo=False)]


def ruta(puntos, punta="arrow", punteada=False, etiqueta=None, pos=None, ancho=160, tam=11):
    """Linea ortogonal por tramos; la punta va solo en el ultimo tramo."""
    els = []
    for i in range(len(puntos) - 1):
        (x1, y1), (x2, y2) = puntos[i], puntos[i + 1]
        ultimo = i == len(puntos) - 2
        els.append(_base("arrow", x1, y1, x2 - x1, y2 - y1,
                         points=[[0, 0], [x2 - x1, y2 - y1]],
                         lastCommittedPoint=None, startBinding=None, endBinding=None,
                         startArrowhead=None, endArrowhead=punta if ultimo else None,
                         strokeStyle="dashed" if punteada else "solid", elbowed=False))
    if etiqueta:
        px, py = pos
        n = len(etiqueta.split("\n"))
        els.append(texto(etiqueta, int(px - ancho / 2), int(py - tam * 1.25 * n / 2), ancho, tam))
    return els


def cubo(x, y, w, h, estereotipo, nombre, d=20, fondo="transparent", tam=13, rotulo=None):
    """Nodo UML: caja 3D. El frente ocupa (x, y+d) a (x+w-d, y+h).

    rotulo=(tx, tw) ubica estereotipo y nombre alineados a la izquierda en ese
    tramo, para que las conexiones que entran por arriba no crucen el texto."""
    els = [_rect(x, y + d, w - d, h - d, fondo)]
    for (x1, y1, x2, y2) in [(x, y + d, x + d, y), (x + d, y, x + w, y),
                             (x + w, y, x + w - d, y + d), (x + w, y, x + w, y + h - d),
                             (x + w, y + h - d, x + w - d, y + h)]:
        els.append(_base("line", x1, y1, x2 - x1, y2 - y1, points=[[0, 0], [x2 - x1, y2 - y1]]))
    if rotulo:
        tx, tw = rotulo
        els.append(texto(estereotipo, tx, y + d + 6, tw, 11, align="left", _halo=False))
        els.append(texto(nombre, tx, y + d + 22, tw, tam, align="left", _halo=False))
    else:
        els.append(texto(estereotipo, x + 4, y + d + 6, w - d - 8, 11, _halo=False))
        els.append(texto(nombre, x + 4, y + d + 22, w - d - 8, tam, _halo=False))
    return els


def componente(x, y, w, h, nombre, tam=12):
    """Componente UML 2.x: rectangulo + icono de componente arriba a la derecha."""
    els = [_rect(x, y, w, h, "#ffffff")]
    ix, iy = x + w - 20, y + 6
    els += [_rect(ix, iy, 12, 14, "#ffffff"), _rect(ix - 4, iy + 3, 8, 3, "#ffffff"),
            _rect(ix - 4, iy + 8, 8, 3, "#ffffff")]
    lineas = nombre.split("\n")
    ty = y + h / 2 - (tam * 1.25 * len(lineas)) / 2 + 2
    els.append(texto(nombre, x + 4, int(ty), w - 28, tam, _halo=False))
    return els


VERDE, NARANJA, GRIS, AMARILLO = "#e8f5e9", "#fff1e0", "#f1f1f1", "#fff8dc"


def bloques_farmahosp():
    els = [titulo("Diagrama de bloques de alto nivel — FarmaHosp", 40, 10, 1400),
           texto("Estilo principal SOA (un servicio por proceso CDU-01..07) · cada servicio en capas · "
                 "llamada y retorno (flechas llenas) · eventos (bus) · tuberías y filtros (telemetría). "
                 "Entradas arriba, salidas a la derecha; toda flecha nombra lo que fluye.",
                 40, 44, 2200, 13, align="left", _halo=False)]
    # rotulos de banda (carril izquierdo)
    for t, y in [("ENTRADAS", 96), ("ACCESO", 328), ("SERVICIOS\nDE NEGOCIO", 520),
                 ("DATOS", 752), ("BUS", 898)]:
        els.append(texto(t, 40, y, 90, 12, align="left", _halo=False))
    # --- entradas
    E = [(40, 240, "Sensores IoT de cámaras\n(vía Gateway IoT)"),
         (340, 300, "Enfermería\nToughpad + escáner Bluetooth"),
         (700, 300, "Farmacia (sótano)\nestación offline-first"),
         (1060, 300, "Portal clínico y administrativo\nmédico · director · jefe FV"),
         (1420, 300, "Paciente\nconsulta de trazabilidad QR")]
    for x, w, t in E:
        els += bloque(x, 120, w, 90, t, VERDE)
    # --- acceso
    els += bloque(340, 300, 1020, 80, "Balanceador y API Gateway\nreparte la carga y prioriza dispensación y administración (AC-05)", AMARILLO)
    els += bloque(1420, 300, 300, 80, "Identidad y acceso\nLDAP + OTP · ABAC (RE-08, AC-04)", AMARILLO)
    els += ruta([(490, 210), (490, 300)], etiqueta="HTTPS · sincroniza\nal volver (AC-02)", pos=(575, 255))
    els += ruta([(850, 210), (850, 300)], etiqueta="HTTPS\nWi-Fi inestable", pos=(925, 255))
    els += ruta([(1210, 210), (1210, 300)], etiqueta="HTTPS", pos=(1160, 255), ancho=80)
    els += ruta([(1570, 210), (1570, 250), (1330, 250), (1330, 300)], etiqueta="Internet · HTTPS", pos=(1450, 232))
    els += ruta([(1360, 340), (1420, 340)], etiqueta="token", pos=(1390, 326), ancho=50, tam=10)
    # --- servicios de negocio (SOA)
    els.append(_rect(340, 440, 1540, 190, "#f5f5f5"))
    els.append(texto("Un servicio por proceso · cada servicio en capas: API → lógica de negocio → acceso a datos",
                     360, 452, 1500, 13, align="left", _halo=False))
    S = ["Adquisición\nCDU-01\nRF-01..04", "Almacenamiento\ne Inventario\nCDU-02 · RF-05..09",
         "Prescripción\nCDU-03\nRF-10..16", "Dispensación\nCDU-04\nRF-17..22",
         "Administración\nCDU-05\nRF-23..27", "Farmacovigilancia\nCDU-06\nRF-28..32",
         "Auditoría y Tablero\nCDU-07\nRF-33..37", "Sincronización\noffline\nAC-02 · RF-26"]
    for i, t in enumerate(S):
        els += bloque(360 + i * 190, 500, 170, 110, t, "#ffffff")
    els += ruta([(850, 380), (850, 440)], etiqueta="REST · llamada y retorno", pos=(960, 410), ancho=180)
    # --- datos
    els += bloque(340, 720, 380, 90, "Base transaccional PostgreSQL\ninventario con ACID (RE-01)")
    els += bloque(780, 720, 360, 90, "Réplica en sitio alterno\ninformes y tablero (RF-33, RF-34)")
    els += bloque(1200, 720, 320, 90, "Bitácora inmutable\nsolo inserción + hash (AC-03)")
    els += bloque(1580, 720, 300, 90, "Caché Redis\nlecturas rápidas (AC-01, AC-05)")
    els += ruta([(530, 630), (530, 720)], etiqueta="lee y escribe\n(JDBC)", pos=(615, 675), ancho=120)
    els += ruta([(720, 765), (780, 765)])
    els += ruta([(1360, 630), (1360, 720)], etiqueta="registra\ncada cambio", pos=(1440, 675), ancho=110)
    els += ruta([(1730, 630), (1730, 720)], etiqueta="consulta", pos=(1680, 675), ancho=80)
    els.append(texto("replicación", 700, 812, 100, 11))
    # --- bus
    els += bloque(340, 880, 1540, 60, "BUS DE EVENTOS (RabbitMQ · AMQP) — asíncrono: absorbe el pico del lunes (AC-05) "
                  "y guarda lo que no puede entregarse (AC-06)", "#fdf3c4")
    els += ruta([(1170, 630), (1170, 880)], punta=None)
    els += ruta([(1550, 630), (1550, 880)], punta=None)
    els.append(texto("publican y consumen eventos", 1180, 842, 360, 11))
    # --- soporte
    els.append(_rect(40, 1020, 860, 160, "#ffffff", redondo=True))
    els.append(texto("Pipeline de telemetría — TUBERÍAS Y FILTROS (AC-08 · RF-05 · RF-06)",
                     220, 1034, 660, 13, align="left", _halo=False))
    F = ["Recibir", "Validar", "Sellar\n(hash encadenado)", "Detectar\nruptura", "Publicar\nevento"]
    for i, t in enumerate(F):
        els += bloque(60 + i * 170, 1090, 140, 60, t, "#ffffff", tam=12)
        if i < 4:
            els += ruta([(200 + i * 170, 1120), (230 + i * 170, 1120)])
    els += ruta([(130, 210), (130, 1090)], etiqueta="lecturas cada\n5 min · MQTT", pos=(195, 640), ancho=120)
    els += ruta([(810, 1090), (810, 940)], etiqueta="publica: ruptura\nde cadena de frío", pos=(700, 978), ancho=150)
    els += bloque(960, 1020, 420, 160, "Notificaciones\nSMS · WhatsApp · correo\n(RF-07, RF-31)", "#ffffff")
    els += bloque(1440, 1020, 440, 160, "Integración — adaptadores\nlegacy SOAP · MSPAS XML/DTD · HL7 FHIR\n"
                  "cola «guardar y reenviar» (AC-06)", "#ffffff")
    els += ruta([(1170, 940), (1170, 1020)], etiqueta="alertas y\nrecordatorios", pos=(1255, 980), ancho=120)
    els += ruta([(1660, 940), (1660, 1020)], etiqueta="reportes y\nconsultas", pos=(1735, 980), ancho=100)
    # --- salidas: sistemas externos
    els.append(texto("SALIDAS — sistemas externos", 2020, 270, 300, 12, align="left", _halo=False))
    els += bloque(2020, 300, 280, 80, "Directorio activo LDAP", GRIS)
    els += ruta([(1720, 340), (2020, 340)], etiqueta="LDAPS · OTP por SMS\nsi LDAP cae (RE-08)", pos=(1870, 316), ancho=170)
    els += bloque(2020, 1000, 280, 50, "Nube pública (analítica)", GRIS)
    els += bloque(2020, 1070, 280, 50, "Legacy de admisiones", GRIS)
    els += bloque(2020, 1140, 280, 50, "Sistema nacional MSPAS", GRIS)
    els += bloque(2020, 1240, 280, 60, "Pasarela SMS / WhatsApp", GRIS)
    els += ruta([(1880, 1030), (2020, 1030)], etiqueta="solo anonimizado", pos=(1950, 1016), ancho=140)
    els += ruta([(1880, 1095), (2020, 1095)], etiqueta="SOAP · 7-17 h", pos=(1950, 1081), ancho=140)
    els += ruta([(1880, 1165), (2020, 1165)], etiqueta="XML/DTD · 8-16 h", pos=(1950, 1151), ancho=140)
    els += ruta([(1170, 1180), (1170, 1270), (2020, 1270)], etiqueta="mensajes de notificación", pos=(1600, 1256), ancho=200)
    els.append(texto("Verde: entradas (usuarios y dispositivos) · Amarillo: acceso · Gris: sistemas externos · "
                     "Flecha llena: llamada y retorno síncrona · Bus: eventos asíncronos · "
                     "Todo lo sensible reside en el data center local (RE-02).",
                     40, 1330, 1900, 12, align="left", _halo=False))
    return els


def despliegue_farmahosp():
    els = [titulo("Diagrama de despliegue (distribución) — FarmaHosp", 40, 10, 1400),
           texto("Nodo = cubo · «device» = hardware · «executionEnvironment» = software, siempre dentro de un "
                 "dispositivo (una máquina virtual) · componentes dentro del nodo que los ejecuta · "
                 "conexión = línea llena con el protocolo como estereotipo.",
                 40, 44, 2250, 13, align="left", _halo=False)]
    # --- zonas (detras de todo), como la captura 58
    els.append(_rect(20, 80, 1900, 500, VERDE, punteado=True))
    els.append(texto("FrontEnd — clientes y dispositivos", 30, 88, 400, 13, align="left", _halo=False))
    els.append(_rect(20, 600, 1900, 860, NARANJA, punteado=True))
    els.append(texto("BackEnd — hospital", 30, 1432, 400, 13, align="left", _halo=False))
    els.append(_rect(1980, 600, 330, 860, GRIS, punteado=True))
    els.append(texto("Sistemas externos", 1990, 1432, 300, 13, align="left", _halo=False))
    # --- clientes
    els += cubo(40, 120, 400, 250, "«device»", "Toughpad Panasonic (Android 9 · 3 GB)")
    els += cubo(60, 190, 340, 170, "«executionEnvironment»", "Android 9", d=12)
    for i, t in enumerate(["App de\nEnfermería", "Validación\nlocal (AC-01)", "BD local cifrada\n(SQLite)", "Bandeja de\nsincronización"]):
        els += componente(75 + (i % 2) * 160, 250 + (i // 2) * 55, 150, 48, t, 11)
    els += cubo(40, 420, 220, 110, "«device»", "Escáner Bluetooth\n(5 % de fallo)")
    els += ruta([(140, 370), (140, 420)], punta=None, etiqueta="«Bluetooth»", pos=(210, 395), ancho=100)
    els += cubo(480, 120, 400, 250, "«device»", "Estación de farmacia (sótano)")
    els += cubo(500, 190, 340, 170, "«executionEnvironment»", "Navegador", d=12)
    for i, t in enumerate(["App de Farmacia\n(offline-first)", "BD local\n(IndexedDB)", "Bandeja de\nsincronización"]):
        els += componente(515 + (i % 2) * 160, 250 + (i // 2) * 55, 150, 48, t, 11)
    els += cubo(500, 420, 200, 90, "«device»", "Impresora de etiquetas")
    els += ruta([(600, 370), (600, 420)], punta=None, etiqueta="«USB»", pos=(650, 395), ancho=60)
    els += cubo(920, 120, 320, 200, "«device»", "PC clínica y administrativa")
    els += cubo(940, 190, 260, 120, "«executionEnvironment»", "Navegador", d=12)
    els += componente(960, 250, 200, 48, "Portal web\n(Angular)", 11)
    els += cubo(1280, 120, 300, 200, "«device»", "Smartphone del paciente")
    els += cubo(1300, 190, 240, 120, "«executionEnvironment»", "Navegador", d=12)
    els += componente(1320, 250, 180, 48, "Consulta QR\n(RF-32)", 11)
    els += cubo(1640, 110, 240, 100, "«device»", "Sensores IoT de cámaras")
    els += cubo(1640, 290, 240, 150, "«device»", "Gateway IoT")
    els += componente(1660, 360, 180, 48, "Buffer local\n(guardar y reenviar)", 11)
    els += ruta([(1760, 210), (1760, 290)], punta=None, etiqueta="«MQTT»", pos=(1820, 250), ancho=70)
    # --- data center principal
    els += cubo(300, 620, 1580, 580, "«device»",
                "Servidor de virtualización VMware — data center principal\n32 vCPU · 128 GB RAM · SAN 10 TB",
                rotulo=(1100, 640))
    els += cubo(340, 700, 360, 130, "«executionEnvironment»", "VM-05/06 Identidad · 1 vCPU · 4 GB c/u", d=12, tam=12)
    els += componente(360, 760, 150, 50, "Keycloak\nLDAP + OTP", 11)
    els += componente(530, 760, 150, 50, "Autorización\nABAC", 11)
    els += cubo(740, 700, 360, 130, "«executionEnvironment»", "VM-01/02 Nginx · 1 vCPU · 2 GB c/u", d=12, tam=12)
    els += componente(760, 760, 310, 50, "Balanceo y prioridad de tráfico\n(AC-05)", 11)
    els += cubo(1140, 700, 260, 130, "«executionEnvironment»", "VM-09 · 1 vCPU · 8 GB", d=12, tam=12)
    els += componente(1160, 760, 210, 50, "Caché Redis", 11)
    els += cubo(1440, 700, 260, 130, "«executionEnvironment»", "VM-11 · 1 vCPU · 4 GB", d=12, tam=12)
    els += componente(1460, 760, 210, 50, "Observabilidad\nPrometheus + Grafana", 11)
    els += cubo(340, 880, 660, 300, "«executionEnvironment»", "VM-03/04 Servidor de aplicaciones (JRE 17) · 5 vCPU · 14 GB c/u",
                d=12, tam=12)
    SV = ["Adquisición", "Almacenamiento\ne Inventario", "Prescripción", "Dispensación",
          "Administración", "Farmacovigilancia", "Auditoría y\nTablero", "Sincronización\noffline"]
    for i, t in enumerate(SV):
        els += componente(355 + (i % 4) * 155, 950 + (i // 4) * 105, 145, 70, t, 11)
    els += cubo(1040, 880, 300, 300, "«executionEnvironment»", "VM-10 PostgreSQL 16 · 8 vCPU · 48 GB", d=12, tam=12)
    els += componente(1060, 960, 250, 60, "BD transaccional\n(ACID · RE-01)", 11)
    els += componente(1060, 1060, 250, 60, "Bitácora inmutable\n(solo inserción · AC-03)", 11)
    els += cubo(1380, 880, 460, 300, "«executionEnvironment»", "VM-07/08 Integración y eventos · 2 vCPU · 8 GB c/u",
                d=12, tam=12)
    for i, t in enumerate(["Bus de eventos\n(RabbitMQ)", "Pipeline de\ntelemetría", "Integración\nSOAP · XML/DTD · FHIR", "Notificaciones\nSMS · WhatsApp · correo"]):
        els += componente(1395 + (i % 2) * 215, 960 + (i // 2) * 100, 200, 70, t, 11)
    # conexiones de los clientes al balanceador
    els += ruta([(320, 370), (320, 540), (780, 540), (780, 700)], punta=None, etiqueta="«wifi · HTTPS»", pos=(430, 526), ancho=120)
    els += ruta([(820, 370), (820, 520), (860, 520), (860, 700)], punta=None, etiqueta="«wifi inestable · HTTPS»", pos=(990, 506), ancho=170)
    els += ruta([(940, 320), (940, 700)], punta=None, etiqueta="«Ethernet 1 Gbps\n· HTTPS»", pos=(1010, 420), ancho=120)
    els += ruta([(1400, 320), (1400, 560), (1020, 560), (1020, 700)], punta=None, etiqueta="«Internet · HTTPS»", pos=(1200, 546), ancho=140)
    els += ruta([(1760, 440), (1760, 850), (1600, 850), (1600, 880)], punta=None, etiqueta="«MQTT / TLS»", pos=(1820, 560), ancho=100)
    # conexiones dentro del data center
    els += ruta([(740, 765), (700, 765)], punta=None)
    els += ruta([(900, 830), (900, 880)], punta=None, etiqueta="«HTTP»", pos=(940, 855), ancho=60)
    els += ruta([(520, 830), (520, 880)], punta=None, etiqueta="«OIDC»", pos=(560, 855), ancho=60)
    els += ruta([(980, 880), (980, 845), (1270, 845), (1270, 830)], punta=None)
    els.append(texto("«TCP»", 1180, 822, 60, 11))
    els += ruta([(990, 880), (990, 865), (1420, 865), (1420, 880)], punta=None)
    els.append(texto("«AMQP»", 1290, 868, 70, 11))
    els += ruta([(1000, 1030), (1040, 1030)], punta=None)
    els.append(texto("«JDBC»", 990, 1036, 60, 11))
    els += ruta([(1380, 1030), (1340, 1030)], punta=None)
    els.append(texto("«JDBC»", 1330, 1036, 60, 11))
    # LDAP a la izquierda del data center
    els += cubo(40, 700, 220, 110, "«device»", "Directorio activo\nLDAP")
    els += ruta([(260, 765), (340, 765)], punta=None, etiqueta="«LDAPS»", pos=(300, 750), ancho=70)
    # sitio alterno
    els += cubo(1040, 1240, 420, 200, "«device»", "Servidor de respaldo — sitio alterno")
    els += cubo(1060, 1310, 380, 120, "«executionEnvironment»", "VM PostgreSQL réplica", d=12, tam=12)
    els += componente(1080, 1370, 330, 44, "Réplica de lectura (informes y tablero)", 11)
    els += ruta([(1190, 1180), (1190, 1240)], punta=None, etiqueta="«replicación streaming · TCP»", pos=(1330, 1212), ancho=210)
    # externos
    X = [("Legacy de admisiones · COBOL · 7-17 h", "«SOAP · HTTPS»"),
         ("Sistema nacional MSPAS (farmacovigilancia)", "«HTTPS · XML/DTD»"),
         ("Pasarela SMS / WhatsApp", "«HTTPS · API»"),
         ("Nube pública · analítica anonimizada", "«HTTPS · anonimizado»")]
    for i, (t, proto) in enumerate(X):
        y = 880 + i * 78
        els += cubo(2000, y, 300, 66, "«device»", t, d=14, tam=11)
        yc = y + 44
        els += ruta([(1840, yc), (2000, yc)], punta=None)
        els.append(texto(proto, 1845, yc - 16, 150, 10))
    return els


DIAGRAMAS.update({
    "bloques-farmahosp": bloques_farmahosp,
    "despliegue-farmahosp": despliegue_farmahosp,
})
SUBCARPETA.update({
    "bloques-farmahosp": "6-bloques-despliegue",
    "despliegue-farmahosp": "6-bloques-despliegue",
})


def _arco_el(cx, cy, r, lado):
    """Semicirculo: polilinea en el .excalidraw, arco de verdad en el SVG."""
    ang = {"arriba": (180, 360), "abajo": (0, 180), "izq": (90, 270), "der": (-90, 90)}[lado]
    pts = []
    for i in range(13):
        a_ = math.radians(ang[0] + (ang[1] - ang[0]) * i / 12)
        pts.append([round(cx + r * math.cos(a_), 1), round(cy + r * math.sin(a_), 1)])
    x0, y0 = pts[0]
    el = _base("line", x0, y0, 0.1, 0.1,
               points=[[round(px - x0, 1), round(py - y0, 1)] for px, py in pts])
    el["_arco"] = (cx, cy, r, lado)
    return el


R_BOLA, R_COPA, VARILLA = 14, 24, 56


def bola(cx, cy, x_comp, y_comp, nombre, lado_texto="der"):
    """Interfaz PROVISTA: circulo unido por varilla al componente que la ofrece."""
    els = [_base("ellipse", cx - R_BOLA, cy - R_BOLA, 2 * R_BOLA, 2 * R_BOLA),
           _base("line", x_comp, y_comp, cx - x_comp if cx != x_comp else 0,
                 cy - y_comp if cy != y_comp else 0,
                 points=[[0, 0], [cx - x_comp, cy - y_comp]])]
    if lado_texto == "der":
        els.append(texto(nombre, cx + R_BOLA + 8, cy - 8, 220, 13, align="left"))
    else:
        els.append(texto(nombre, cx - R_BOLA - 228, cy - 8, 220, 13, align="right"))
    return els


def copa(cx, cy, lado, x_comp, y_comp):
    """Interfaz REQUERIDA: semicirculo (receptaculo) + varilla a su componente."""
    return [_arco_el(cx, cy, R_COPA, lado),
            _base("line", x_comp, y_comp, cx - x_comp, cy - y_comp,
                  points=[[0, 0], [cx - x_comp, cy - y_comp]])]


def componentes_farmahosp():
    els = [titulo("Diagrama de componentes — FarmaHosp", 40, 10, 1400),
           texto("Círculo = interfaz PROVISTA (la ofrece el componente del que sale la varilla) · "
                 "semicírculo = interfaz REQUERIDA (la necesita el componente del que sale su varilla) · "
                 "semicírculo abrazando al círculo = ENSAMBLE · separados, la punteada va del semicírculo "
                 "al círculo (captura 31) · quien depende va arriba.",
                 40, 44, 2200, 13, align="left", _halo=False)]
    C = componente
    # --- grupo
    els.append(_rect(20, 270, 1420, 1000, "#f7f7f7", punteado=True))
    els.append(texto("Servicios de negocio (SOA) — uno por proceso CDU-01..07", 1000, 244, 440, 13,
                     align="left", _halo=False))
    # --- clientes (y=110..200)
    els += C(60, 110, 260, 90, "PortalWeb\n(Angular · médico, director, jefe FV)")
    els += C(420, 110, 260, 90, "AppFarmacia\n(offline-first · RE-16)")
    els += C(780, 110, 260, 90, "AppEnfermeria\n(Toughpad · RE-14)")
    els += C(1900, 110, 260, 90, "GatewayIoT\n(cámaras · RF-05)")
    # --- fila 2 (y=360..450)
    els += C(60, 360, 260, 90, "SvcAuditoria\nCDU-07 · RF-33..37")
    els += C(420, 360, 260, 90, "SvcSincronizacion\nAC-02 · RF-26")
    els += C(780, 360, 260, 90, "SvcAdministracion\nCDU-05 · RF-23..27")
    els += C(1900, 360, 260, 90, "PipelineTelemetria\nAC-08 · RF-05, RF-06")
    # --- fila 3 (y=620..710)
    els += C(780, 620, 260, 90, "SvcDispensacion\nCDU-04 · RF-17..22")
    els += C(1140, 620, 260, 90, "SvcFarmacovigilancia\nCDU-06 · RF-28..32")
    # --- fila 4 (y=880..970)
    els += C(780, 880, 260, 90, "SvcPrescripcion\nCDU-03 · RF-10..16")
    # --- fila 5 (y=1140..1230)
    els += C(420, 1140, 260, 90, "SvcAdquisicion\nCDU-01 · RF-01..04")
    els += C(780, 1140, 260, 90, "SvcInventario\nCDU-02 · RF-05..09 · RE-01")
    # --- transversales
    els.append(texto("Servicios transversales — los usa todo el grupo", 1560, 244, 420, 13,
                     align="left", _halo=False))
    els += C(1560, 360, 260, 90, "SvcIntegracion\nAC-06 · RF-29, RF-37")
    els += C(1560, 620, 260, 90, "SvcNotificacion\nRF-07 · RF-31")
    els += C(1560, 880, 260, 90, "SvcIdentidad\nRE-08 · AC-04")
    els += C(1560, 1140, 260, 90, "BitacoraInmutable\nAC-03")

    def ensamble(cx, y_consumidor, y_proveedor, nombre, x_comp=None):
        """Consumidor arriba, proveedor abajo, en el mismo eje."""
        cy = y_proveedor - VARILLA
        return (bola(cx, cy, cx, y_proveedor, nombre)
                + copa(cx, cy, "arriba", cx, y_consumidor))

    # --- ENSAMBLES (el consumidor está justo encima del proveedor)
    els += ensamble(190, 200, 360, "IAuditoria")          # PortalWeb
    els += ensamble(550, 200, 360, "ISincronizacion")     # AppFarmacia
    els += ensamble(910, 200, 360, "IAdministracion")     # AppEnfermeria
    els += ensamble(2030, 200, 360, "ILectura")           # GatewayIoT
    els += ensamble(910, 450, 620, "IDispensacion")       # SvcAdministracion
    els += ensamble(910, 710, 880, "IPrescripcion")       # SvcDispensacion
    els += ensamble(910, 970, 1140, "IInventario")        # SvcPrescripcion
    # IOrdenCompra: ensamble horizontal (Adquisición provee, Inventario requiere)
    els += bola(736, 1185, 680, 1185, "IOrdenCompra", lado_texto="izq")
    els += copa(736, 1185, "der", 780, 1185)

    # --- DEPENDENCIAS CON RECORRIDO: copa en el consumidor + punteada a la bola
    # AppEnfermeria → ISincronizacion
    els += copa(850, 224, "arriba", 850, 200)
    els += ruta([(850, 248), (850, 304), (564, 304)], punteada=True)
    # AppFarmacia → IDispensacion
    els += copa(396, 155, "der", 420, 155)
    els += ruta([(372, 155), (340, 155), (340, 564), (896, 564)], punteada=True)
    # PortalWeb → IPrescripcion
    els += copa(36, 155, "der", 60, 155)
    els += ruta([(12, 155), (12, 824), (896, 824)], punteada=True)
    # SvcAdministracion → IFarmacovigilancia (la bola la ofrece SvcFarmacovigilancia)
    els += bola(1270, 564, 1270, 620, "IFarmacovigilancia")
    els += copa(1000, 474, "arriba", 1000, 450)
    els += ruta([(1000, 498), (1000, 564), (1256, 564)], punteada=True)
    # SvcDispensacion → IInventario
    els += copa(1064, 665, "izq", 1040, 665)
    els += ruta([(1088, 665), (1120, 665), (1120, 1084), (924, 1084)], punteada=True)
    # SvcPrescripcion → IOrdenCompra
    els += copa(840, 994, "arriba", 840, 970)
    els += ruta([(840, 1018), (840, 1060), (700, 1060), (700, 1185), (722, 1185)], punteada=True)
    # PipelineTelemetria → IRegistroEvento
    els += copa(2030, 474, "arriba", 2030, 450)
    els += ruta([(2030, 498), (2030, 1300), (1504, 1300), (1504, 1199)], punteada=True)

    # --- el grupo requiere las cuatro interfaces transversales
    for y, n in [(405, "IAdmisiones · IReporteMSPAS"), (665, "INotificacion"),
                 (925, "IAutenticacion · IAutorizacion"), (1185, "IRegistroEvento")]:
        els += bola(1504, y, 1560, y, n, lado_texto="izq")
        els += ruta([(1440, y), (1490, y)], punteada=True)

    els.append(texto("Lectura: AppEnfermeria requiere IAdministracion e ISincronizacion · AppFarmacia requiere "
                     "IDispensacion e ISincronizacion · PortalWeb requiere IAuditoria e IPrescripcion · la cadena "
                     "de negocio va Administración → Dispensación → Prescripción → Inventario → Adquisición.",
                     40, 1330, 2000, 12, align="left", _halo=False))
    return els


DIAGRAMAS["componentes-farmahosp"] = componentes_farmahosp
SUBCARPETA["componentes-farmahosp"] = "6-bloques-despliegue"


if __name__ == "__main__":
    sys.exit(main())
