---
tema: Diagramas
fuente: "— (Carpeta de trabajo del día del parcial)"
fecha: 2026-09-15
---

# Examen — la carpeta del día del parcial

Misma estructura que `practica/`, pero para trabajar **con reloj**. Las carpetas por sección ya
están creadas y vacías: en el examen no se pierde un minuto decidiendo dónde guardar.

```
examen/
├── 2-caso-negocio/            ← acá va lo tuyo del criterio 1
├── 3.1-drivers-rf/
├── 3.2-drivers-calidad/
├── 3.3-drivers-restriccion/
├── 3.4-priorizacion/
├── 4-matrices-trazabilidad/
└── referencia/                ← los 23 .svg del Caso 1, en las mismas carpetas
```

Refrescar la referencia: `python3 generar-excalidraw.py --referencia examen` desde
`06-Proyecto-MCP/`.

---

## La regla de alcance, que es donde se pierden más puntos

> **Lo que la pregunta pide, más UN solo agregado vital por entregable. Nada más.**

En examen, **agregar de más es un error**. «Vital» es estrecho — solo cuatro cosas califican, y son
las que evitan perder puntos, no las que lucen mejor:

1. Declarar la **frontera** en una línea.
2. Poner **IDs** (`STK-01`, `CDU-03`, `RF-17`, `AC-02`, `RE-05`) desde el primer entregable.
3. **Nombrar todas las flechas** de cualquier diagrama.
4. Declarar **lo que quedó fuera y por qué**.

Cómo se trabaja: **primero lo que más vale** (orden por puntaje), tablas y listas en vez de prosa,
sin explorar alternativas. Si algo es ambiguo, **se asume y se declara la asunción en una línea** —
no se pregunta. Si un punto se traba, se marca `PENDIENTE` y se avanza.

## El orden por puntaje, para atacar de mayor a menor

| Criterio | Puntos | Qué entregar |
|---|---|---|
| 3 — Drivers arquitectónicos | **30** | RF (CDU expandidos) · calidad · restricción · top 5 |
| 1 — Caso de negocio | **25** | Contexto · core · primera descomposición |
| 2 — Stakeholders | **25** | La tabla, clasificados, con su necesidad oculta |
| 4 — Matrices de trazabilidad | **20** | STK×CDU · RF×RF · CDU×RF |

## Los cuatro errores que invalidan un artefacto

- **Un caso de uso llamado crear / editar / eliminar / consultar.** Eso es descomposición
  funcional. La prueba: *¿el actor se iría satisfecho si solo ocurriera esto?*
- **Un atributo de calidad dibujado como caso de uso.** Va como escenario de **6 partes**, y
  **sin número en la medida no es un driver, es un deseo**.
- **Mezclar los estereotipos de negocio y de sistema** en un mismo diagrama.
- **Priorizar restricciones.** No se priorizan: todas son obligatorias. Los drivers de calidad sí,
  y con **dos ejes** — importancia (la ponen los stakeholders) y dificultad (la pone el arquitecto).

## Chequeo de 30 segundos antes de entregar

- [ ] ¿Respondí **todo** lo que pedía?
- [ ] ¿Todo tiene **nombre e ID**?
- [ ] ¿Declaré la **frontera** y las **omisiones**?
- [ ] ¿Cada driver de calidad tiene **número** en la medida?
- [ ] ¿Las flechas de los diagramas están **todas nombradas**?

---

> [!warning] `referencia/` es del Caso 1, no del examen
> Son las láminas de FarmaHosp. Sirven como **molde** —la forma de la tabla, las seis partes, cómo
> se lee una matriz— no como respuesta. El caso del parcial va a ser otro: copiar el contenido de
> acá es la forma más rápida de contestar lo que no se preguntó.
