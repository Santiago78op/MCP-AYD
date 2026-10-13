# -*- coding: utf-8 -*-
"""Valida la estructura y la disposicion de un PDF de entrega.

    python3 validar-entrega-pdf.py ../08-Tareas/Grupo2_CasoHD.pdf

Comprueba, y sale con codigo 1 si algo falla:
  · numeracion de titulos sin saltos y referencias "§x.y" que existen
  · cada "Figura N." en la misma pagina que su imagen, y numeradas de corrido
  · nada fuera de los margenes
  · ningun titulo solo al pie de la pagina
  · ninguna pagina por debajo del 45 % de ocupacion (salvo la ultima)
  · ninguna raya larga
Informa ademas tamanos de pagina, fuentes incrustadas, autor y conteo de identificadores.

Necesita pymupdf (pip install pymupdf). Nacio de la validacion manual del Caso
Harley-Davidson: las seis paginas a medio llenar y la figura fuera de margen
no se veian en el .docx, solo midiendo el PDF.
"""
import re
import sys

import pymupdf

MARGEN_LATERAL = 0.8 * 72     # los de generar-entrega-*.py en apaisado
PIE = 0.7 * 72
MIN_OCUPACION = 45


def main(ruta):
    d = pymupdf.open(ruta)
    fallas = []
    titulos, figuras, ocup = [], [], []
    for i, p in enumerate(d):
        W, H = p.rect.width, p.rect.height
        ys = []
        for b in p.get_text("dict")["blocks"]:
            x0, y0, x1, y1 = b["bbox"]
            if y0 > H - PIE:
                continue
            ys.append(y1)
            if x0 < MARGEN_LATERAL - 3 or x1 > W - MARGEN_LATERAL + 3 or y1 > H - PIE + 4:
                fallas.append("p%d: contenido fuera de margen %s" % (i + 1, [round(v) for v in b["bbox"]]))
            if b["type"] == 1:
                figuras.append(i + 1)
                continue
            for l in b["lines"]:
                t = "".join(s["text"] for s in l["spans"]).strip()
                tam = max(s["size"] for s in l["spans"])
                negrita = any(s["flags"] & 16 for s in l["spans"])
                if tam >= 11.4 and re.match(r"^\d(\.\d)?\.? ", t):
                    titulos.append(t.split(" ")[0].rstrip("."))
                if tam >= 10.4 and negrita and re.match(r"^(\d(\.\d)?\.? |[A-Z]{2,3}-\d\d )", t) \
                        and l["bbox"][3] > (H - PIE) * 0.92:
                    fallas.append("p%d: título solo al pie: %s" % (i + 1, t[:40]))
        ocup.append(round(max(ys) / (H - PIE) * 100) if ys else 0)

    texto = [p.get_text() for p in d]
    todo = "\n".join(texto)
    leyendas = [(i + 1, int(m)) for i, t in enumerate(texto) for m in re.findall(r"Figura (\d+)\.", t)]
    for pag, n in leyendas:
        if pag not in figuras:
            fallas.append("p%d: la leyenda de la Figura %d no está con su imagen" % (pag, n))
    nums = [n for _, n in leyendas]
    if nums != list(range(1, len(nums) + 1)):
        fallas.append("figuras fuera de secuencia: %s" % nums)
    for i, o in enumerate(ocup[:-1]):
        if o < MIN_OCUPACION:
            fallas.append("p%d: ocupada al %d %%" % (i + 1, o))
    principales = [t for t in titulos if "." not in t]
    if principales != [str(k) for k in range(1, len(principales) + 1)]:
        fallas.append("títulos de nivel 1 fuera de secuencia: %s" % principales)
    for ref in sorted(set(re.findall(r"§(\d\.\d)", todo))):
        if ref not in titulos:
            fallas.append("referencia a §%s, que no existe" % ref)
    if "—" in todo:
        fallas.append("%d rayas largas" % todo.count("—"))

    fuentes = sorted({f[3].split("+")[-1] for p in d for f in p.get_fonts(full=True)})
    print("archivo: %s · %d páginas · tamaños %s" % (ruta.split("/")[-1], len(d),
          sorted({(round(p.rect.width), round(p.rect.height)) for p in d})))
    print("autor: %s · título: %s" % (d.metadata.get("author"), d.metadata.get("title")))
    print("fuentes:", ", ".join(fuentes))
    print("títulos:", " ".join(titulos))
    print("figuras: %d, en las páginas %s" % (len(leyendas), [p for p, _ in leyendas]))
    print("ocupación mínima: %d %% (página %d)" % (min(ocup[:-1]), ocup.index(min(ocup[:-1])) + 1))
    ids = {k: len(set(re.findall(k + r"-\d\d", todo))) for k in ("STK", "RF", "CU", "EAC", "AC", "RE", "CDU")}
    print("identificadores:", {k: v for k, v in ids.items() if v})
    if fallas:
        print("\nFALLAS (%d):" % len(fallas))
        for f in fallas:
            print("  -", f)
        return 1
    print("\nSin fallas.")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1]))
