/**
 * pruebas/cobertura.mjs — sonda de COBERTURA del contenido.
 *
 * Las otras tres pruebas verifican que el servidor funcione. Esta verifica que
 * el servidor ENCUENTRE lo que la boveda sabe: cada consulta que un estudiante
 * haria de verdad tiene que devolver la nota correcta.
 *
 * Es la prueba que atrapa la desincronizacion silenciosa: se agrega una nota
 * nueva y nadie le pone alias, entonces existe pero es inalcanzable.
 *
 * Uso:  VAULT_PATH="/ruta" node pruebas/cobertura.mjs
 */
import { Client } from "@modelcontextprotocol/client";
import { StdioClientTransport } from "@modelcontextprotocol/client/stdio";
import { existsSync } from "node:fs";

const VAULT = process.env.VAULT_PATH;
if (!VAULT || !existsSync(VAULT)) {
  console.error('Falta VAULT_PATH. Ej: VAULT_PATH="/ruta/a/la/boveda" node pruebas/cobertura.mjs');
  process.exit(1);
}

/**
 * Cada caso: la herramienta, el argumento, y que subcadena TIENE que aparecer.
 * Si el esperado empieza con "!", el caso exige un ERROR que contenga el resto.
 */
const CASOS = [
  // --- notas nuevas de clase: se encuentran por su nombre?
  ["leer_nota", { nombre: "Drivers arquitectonicos" }, "puente entre los requerimientos"],
  ["leer_nota", { nombre: "Diagrama de contexto" }, "Streamlines"],
  ["leer_nota", { nombre: "Categorias de estructuras" }, "componentes y conectores"],
  ["leer_nota", { nombre: "Metodo de diseno centrado en la arquitectura" }, "Creacion del caso de negocio"],
  ["leer_nota", { nombre: "Convenios del diagrama de CUN" }, "navegabilidad"],
  ["leer_nota", { nombre: "Arquitectura y proceso de desarrollo" }, "moderacion cautelosa"],

  // --- busqueda: los conceptos clave aparecen?
  ["buscar", { consulta: "driver de restriccion" }, "Drivers arquitect"],
  ["buscar", { consulta: "streamline" }, "Diagrama de contexto"],
  ["buscar", { consulta: "navegabilidad" }, "Convenios"],
  ["buscar", { consulta: "primera descomposicion" }, "descomposici"],
  ["buscar", { consulta: "escalabilidad" }, "Drivers arquitect"],
  ["buscar", { consulta: "matriz de dependencias" }, "trazabilidad"],
  ["buscar", { consulta: "paso 0" }, "caso de negocio"],
  ["buscar", { consulta: "reutilizacion" }, "include"],

  // --- glosario: los terminos nuevos estan?
  ["glosario", { termino: "driver arquitectonico" }, "factores cr"],
  ["glosario", { termino: "navegabilidad" }, "inicia"],
  ["glosario", { termino: "streamline" }, "flujo de informaci"],
  ["glosario", { termino: "paso 0" }, "caso de negocio"],
  ["glosario", { termino: "FURPS" }, "facilidad de uso"],
  ["glosario", { termino: "categorias de estructuras" }, "asignaci"],

  // --- metodo_tarea: los alias de las guias resuelven?
  ["metodo_tarea", { entregable: "drivers de restriccion" }, "restricci"],
  ["metodo_tarea", { entregable: "matriz de dependencias" }, "dependencia"],
  ["metodo_tarea", { entregable: "por donde empiezo" }, "enunciado"],
  ["metodo_tarea", { entregable: "ejemplos resueltos" }, "Tienda Electr"],
  ["metodo_tarea", { entregable: "stakeholders" }, "necesidad oculta"],
  ["metodo_tarea", { entregable: "que estilo uso" }, "cuatro escalones"],
  ["metodo_tarea", { entregable: "seleccion de estilo" }, "NO contestar SOA"],
  ["metodo_tarea", { entregable: "core" }, "core"],

  // --- diagramas y flashcards de las notas nuevas
  ["obtener_diagrama", { nombre: "Drivers arquitectónicos#mermaid-1" }, "flowchart"],
  ["obtener_diagrama", { nombre: "Método de diseño centrado en la arquitectura#mermaid-1" }, "flowchart"],
  // una nota con varios diagramas exige el id exacto y sugiere los disponibles:
  ["obtener_diagrama", { nombre: "Drivers arquitectonicos" }, "!por su id exacto"],
  ["obtener_flashcards", { tema: "Drivers arquitectonicos y contexto" }, "factores cr"],
  ["obtener_flashcards", { tema: "CUN, convenios y metodo" }, "paso 0"],

  // --- REGRESION M-01: consultas en lenguaje natural que antes daban 0 resultados
  ["buscar", { consulta: "diferencia entre include y extend" }, "inclusi"],
  ["buscar", { consulta: "priorizar drivers" }, "priorizar"],
  ["buscar", { consulta: "cuantos actores debe tener un caso de uso" }, "Convenios"],

  // --- REGRESION M-03: leer_nota resuelve los alias del frontmatter
  ["leer_nota", { nombre: "drivers" }, "factores cr"],
  ["leer_nota", { nombre: "driver arquitectonico" }, "factores cr"],

  // --- REGRESION: la linea que explica el formato NO debe salir como tarjeta
  ["obtener_flashcards", { tema: "Drivers arquitectonicos y contexto", cantidad: 1 }, "driver arquitect"],

  // --- capturas_U2 (2026-09-15): como se disena y como se modela
  ["leer_nota", { nombre: "Como se modela la arquitectura" }, "ADL"],
  ["leer_nota", { nombre: "Que se tiene en cuenta para el diseno" }, "contexto"],
  ["leer_nota", { nombre: "Diagrama de componentes" }, "interfaz"],
  ["leer_nota", { nombre: "Interfaces de componentes" }, "requerida"],
  ["leer_nota", { nombre: "Diagrama de paquetes" }, "import"],
  ["leer_nota", { nombre: "Diagrama de secuencia" }, "loop"],
  ["leer_nota", { nombre: "Diagrama de clases" }, "multiplicidad"],
  ["leer_nota", { nombre: "Ejemplo resuelto - Parque de atracciones" }, "Molinete"],
  ["leer_nota", { nombre: "Diagrama de bloques de alto nivel" }, "SCADA"],
  ["leer_nota", { nombre: "Arquitectura monolitica" }, "base de codigo unica"],
  ["leer_nota", { nombre: "Arquitectura en capas" }, "cliente"],
  ["leer_nota", { nombre: "Arquitectura en la nube" }, "nube"],
  ["buscar", { consulta: "diagrama de distribucion" }, "despliegue"],
  ["buscar", { consulta: "patron arquitectonico" }, "Estilos arquitect"],
  ["glosario", { termino: "entorno de ejecucion" }, "dispositivo"],
  ["glosario", { termino: "interfaz provista" }, "ofrece"],
  ["obtener_flashcards", { tema: "Diagrama de componentes" }, "?"],

  // --- capturas_U2_F2 (2026-09-16): patrones, estilos, referencia, 4+1 y fundamentos
  ["leer_nota", { nombre: "Patrones de diseno" }, "Creacionales"],
  ["leer_nota", { nombre: "Patrones arquitectonicos" }, "Circuit Breaker"],
  ["buscar", { consulta: "Object Pool" }, "Patrones de dise"],
  ["buscar", { consulta: "impacto global sobre la aplicacion" }, "Patrones arquitect"],
  ["obtener_flashcards", { tema: "Patrones de diseño y arquitectónicos" }, "?"],
  ["leer_nota", { nombre: "Arquitectura de referencia" }, "mapeado"],
  ["buscar", { consulta: "modelo de referencia" }, "Arquitectura de referencia"],
  ["buscar", { consulta: "arquitectura candidata" }, "Arquitectura de referencia"],
  ["leer_nota", { nombre: "Catalogo de estilos arquitectonicos" }, "Blackboard"],
  ["buscar", { consulta: "llamada y retorno" }, "Catálogo de estilos"],
  ["glosario", { termino: "modelo de referencia" }, "descomposici"],
  ["buscar", { consulta: "Proceso Unificado Racional" }, "Modelo 4+1"],
  ["buscar", { consulta: "de localizacion" }, "Categorías de estructuras"],
  ["buscar", { consulta: "diagrama de flexibilidad" }, "Equilibrio de restricciones"],
  ["buscar", { consulta: "transformacion impuesta" }, "Estilos arquitect"],
  ["glosario", { termino: "elementos, forma y razon" }, "motivaci"],

  // --- capturas_U2_F3 (2026-09-17): capas, flujo de datos, llamada y retorno, RPC, SOA, MVC
  ["leer_nota", { nombre: "Arquitectura en capas" }, "Ejercicios que dejó la clase"],
  ["buscar", { consulta: "thin client" }, "Arquitectura en capas"],
  ["leer_nota", { nombre: "Tuberias y filtros" }, "no necesariamente realizan"],
  ["leer_nota", { nombre: "Arquitectura centrada en el flujo de datos" }, "hasta completarse"],
  ["buscar", { consulta: "pipes and filters" }, "Tuberías y filtros"],
  ["buscar", { consulta: "batch sequential" }, "flujo de datos"],
  ["leer_nota", { nombre: "Arquitectura de llamada y retorno" }, "estado de bloqueo"],
  ["leer_nota", { nombre: "Llamada a procedimiento remoto" }, "serializables"],
  ["buscar", { consulta: "RPC" }, "Llamada a procedimiento remoto"],
  ["leer_nota", { nombre: "Arquitectura orientada a servicios" }, "Enterprise Service Bus"],
  ["buscar", { consulta: "SOA" }, "Arquitectura orientada a servicios"],
  ["buscar", { consulta: "bus empresarial" }, "Arquitectura orientada a servicios"],
  ["leer_nota", { nombre: "Modelo-Vista-Controlador" }, "SI Evento Z"],
  ["buscar", { consulta: "MVC" }, "Modelo-Vista-Controlador"],
  ["buscar", { consulta: "modelo activo" }, "Modelo-Vista-Controlador"],
  ["glosario", { termino: "sincrono" }, "correspondencia temporal"],
  ["obtener_flashcards", { tema: "Flujo de datos" }, "?"],

  // --- Tarea 2 FarmaHosp (2026-09-17): estilo, bloques y despliegue
  ["metodo_tarea", { entregable: "Entrega - Tarea 2 FarmaHosp" }, "Funcionamiento de la Arquitectura (SOA)"],
  ["metodo_tarea", { entregable: "Avance - Tarea 2 FarmaHosp" }, "100 pts cubiertos"],
  ["buscar", { consulta: "Servidor de virtualización VMware" }, "Entrega - Tarea 2"],

  // --- Caso Harley-Davidson (2026-10-12): enunciado estudiado
  ["metodo_tarea", { entregable: "Plan - Caso Harley-Davidson" }, "modelo de calidad"],
  ["metodo_tarea", { entregable: "harley" }, "SiL'K"],
  ["buscar", { consulta: "Requerimientos vrs. Requerimientos" }, "Plan - Caso Harley-Davidson"],
  ["enunciado", { nombre: "Caso Harley-Davidson" }, "GrupoN_CasoHD.pdf"],
  ["metodo_tarea", { entregable: "Entrega - Caso Harley-Davidson" }, "ISO/IEC 25010"],
  ["metodo_tarea", { entregable: "Avance - Caso Harley-Davidson" }, "Lo que falta"],
  ["metodo_tarea", { entregable: "Guion - Presentación Caso Harley-Davidson" }, "El reloj"],
  ["buscar", { consulta: "CU-20 Escalar riesgo de lanzamiento" }, "Entrega - Caso Harley-Davidson"],
  ["leer_nota", { nombre: "Ejemplo resuelto - Sistema de Transporte READM" }, "EAC-01"],
  ["buscar", { consulta: "bus de eventos" }, "Ejemplo resuelto - Sistema de Transporte READM"],
  ["glosario", { termino: "EAC" }, "escenario de atributo de calidad"],
  ["obtener_flashcards", { tema: "READM" }, "?"],

  // --- Lectura de MDA y modelo en espiral (2026-10-13)
  ["leer_nota", { nombre: "Arquitectura dirigida por modelos MDA" }, "Platform Independent Model"],
  ["leer_nota", { nombre: "Arquitectura de software en el modelo en espiral" }, "integridad conceptual"],
  ["buscar", { consulta: "requerimientos significativos arquitectónicamente" }, "Arquitectura de software en el modelo en espiral"],
  ["glosario", { termino: "PIM" }, "Platform Independent Model"],
  ["obtener_flashcards", { tema: "MDA" }, "?"],

  // --- Notas tecnicas NT2 y NT3 de la unidad 3 (2026-10-16)
  ["leer_nota", { nombre: "Arquitectura de la informacion" }, "investigación, organización y diseño"],
  ["leer_nota", { nombre: "Arquitectura agil" }, "Requisitos Significantes para la Arquitectura"],
  ["leer_nota", { nombre: "Requisitos significativos para la arquitectura" }, "impacto medible"],
  ["buscar", { consulta: "arquitecto de información" }, "Arquitectura de la información"],
  ["buscar", { consulta: "RSA" }, "Requisitos significativos para la arquitectura"],
  ["glosario", { termino: "Historia de usuario" }, "XP"],
  ["obtener_flashcards", { tema: "Arquitectura de la información y ágil" }, "?"],

  // --- Calidad del Software, teoria de clase: capturas_U3_F1 (2026-10-16)
  ["leer_nota", { nombre: "Calidad del software" }, "trascendental"],
  ["leer_nota", { nombre: "Norma ISO 9126" }, "Calidad interna/externa"],
  ["leer_nota", { nombre: "Familia de normas ISO 25000" }, "2503n"],
  ["leer_nota", { nombre: "Atributos observables y no observables vía ejecución" }, "Bass et al. (1998)"],
  ["leer_nota", { nombre: "Escenarios de calidad" }, "criterio para testear el requerimiento"],
  ["buscar", { consulta: "Garvin" }, "Calidad del software"],
  ["buscar", { consulta: "tolerancia a fallos" }, "Norma ISO 9126"],
  ["buscar", { consulta: "no observables vía ejecución" }, "Atributos observables y no observables vía ejecución"],
  ["buscar", { consulta: "identificación de contribuyentes" }, "Escenarios de calidad"],
  ["glosario", { termino: "ISO 9000:2000" }, "características inherentes"],
  ["glosario", { termino: "McCall" }, "primitivas"],
  ["obtener_flashcards", { tema: "Calidad del software e ISO 9126" }, "?"],

  // --- Unidad 3 de clase y lecturas de calidad del parcial 3 (2026-10-16)
  ["leer_nota", { nombre: "Metodologías predictivas y ágiles" }, "Planning fallacy"],
  ["leer_nota", { nombre: "Proceso Scrum en la arquitectura de software" }, "arquitectura base"],
  ["leer_nota", { nombre: "Proceso general de diseño de la arquitectura" }, "caja negra"],
  ["leer_nota", { nombre: "Ciclo de desarrollo de la arquitectura" }, "Construcción"],
  ["leer_nota", { nombre: "Arquitectura empresarial" }, "cartera de aplicaciones"],
  ["leer_nota", { nombre: "Modelos de calidad del software" }, "CMMI"],
  ["leer_nota", { nombre: "Calidad en uso" }, "eficacia, productividad, seguridad y satisfacción"],
  ["buscar", { consulta: "Scrum Master" }, "Metodologías predictivas y ágiles"],
  ["buscar", { consulta: "niveles de diseño" }, "Proceso general de diseño de la arquitectura"],
  ["buscar", { consulta: "guiado por arquitecturas" }, "Ciclo de desarrollo de la arquitectura"],
  ["buscar", { consulta: "inventario de la información" }, "Arquitectura de la información"],
  ["buscar", { consulta: "representación escalonada" }, "Modelos de calidad del software"],
  ["buscar", { consulta: "métrica indirecta" }, "Calidad en uso"],
  ["glosario", { termino: "CMMI" }, "escalonada"],
  ["glosario", { termino: "Calidad en uso" }, "contexto específico de uso"],
  ["obtener_flashcards", { tema: "Metodologías, Scrum y ciclo de la arquitectura" }, "?"],
  ["obtener_flashcards", { tema: "Modelos de calidad y calidad en uso" }, "?"],

  ["metodo_tarea", { entregable: "Repaso - Parcial 3" }, "Autoevaluación"],

  ["metodo_tarea", { entregable: "preguntas" }, "pendientes"],

  // --- referencias y enunciado
  ["referencia", { herramienta: "StarUML" }, "StarUML"],
  ["enunciado", { nombre: "Caso 1 - FarmaHosp" }, "FarmaHosp"],
];

const texto = (r) =>
  (Array.isArray(r.content) ? r.content : [])
    .map((b) => (b && typeof b === "object" && "text" in b ? String(b.text) : ""))
    .join("\n");

const norm = (s) =>
  s.normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase();

const cliente = new Client({ name: "sonda-cobertura", version: "1.0.0" });
await cliente.connect(
  new StdioClientTransport({
    command: process.execPath,
    args: ["dist/src/index.js"],
    env: { ...process.env, VAULT_PATH: VAULT },
    stderr: "ignore",
  })
);

let ok = 0;
const fallas = [];

for (const [tool, args, esperado] of CASOS) {
  const etiqueta = `${tool}(${JSON.stringify(args)})`;
  let r;
  try {
    r = await cliente.callTool({ name: tool, arguments: args });
  } catch (e) {
    fallas.push(`${etiqueta} -> EXCEPCION: ${e.message}`);
    continue;
  }
  const t = texto(r);
  const esperaError = esperado.startsWith("!");
  const buscado = esperaError ? esperado.slice(1) : esperado;

  if (esperaError && !r.isError) {
    fallas.push(`${etiqueta} -> se esperaba un error y devolvio contenido`);
  } else if (!esperaError && r.isError) {
    fallas.push(`${etiqueta} -> isError: ${t.slice(0, 120)}`);
  } else if (!norm(t).includes(norm(buscado))) {
    fallas.push(`${etiqueta} -> no contiene "${buscado}" (${t.length} chars)`);
  } else {
    ok++;
  }
}

await cliente.close();

console.log("");
console.log("=".repeat(72));
if (fallas.length === 0) {
  console.log(`COBERTURA OK — ${ok}/${CASOS.length} consultas encuentran su contenido`);
} else {
  console.log(`COBERTURA: ${ok}/${CASOS.length} ok, ${fallas.length} fallas`);
  for (const f of fallas) console.log(`  [FALLA] ${f}`);
}
console.log("=".repeat(72));
process.exit(fallas.length === 0 ? 0 : 1);
