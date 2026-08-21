#!/usr/bin/env bash
#
# instalar.sh — instala el tutor de Análisis y Diseño de Sistemas en macOS.
#
# FILOSOFÍA DE ESTE SCRIPT: detectar antes de instalar.
#
# Nunca instala algo que ya está. Si encuentra una versión insuficiente, te dice
# el comando exacto y se detiene, en vez de instalar una segunda copia por su
# cuenta. Ese es el pedido explícito: no terminar con varias versiones de node,
# de npm o de lo que sea.
#
# Es IDEMPOTENTE: correrlo dos veces no rompe nada ni duplica nada.
#
# Uso:
#   bash instalar.sh                 instala lo que falte
#   bash instalar.sh --verificar     solo diagnostica, no toca nada
#   bash instalar.sh --ayuda
#
# Escrito para bash 3.2, el que trae macOS de fábrica.

set -u

# ---------------------------------------------------------------------------
# Presentación
# ---------------------------------------------------------------------------

if [ -t 1 ]; then
  ROJO=$'\033[31m'; VERDE=$'\033[32m'; AMBAR=$'\033[33m'; AZUL=$'\033[34m'
  NEGRITA=$'\033[1m'; FIN=$'\033[0m'
else
  ROJO=''; VERDE=''; AMBAR=''; AZUL=''; NEGRITA=''; FIN=''
fi

FALLAS=0
AVISOS=0
ACCIONES=0

ok()      { printf "  %sOK%s      %s\n" "$VERDE" "$FIN" "$1"; }
ya()      { printf "  %sYA%s      %s\n" "$AZUL" "$FIN" "$1"; }
hecho()   { printf "  %sHECHO%s   %s\n" "$VERDE" "$FIN" "$1"; ACCIONES=$((ACCIONES+1)); }
aviso()   { printf "  %sAVISO%s   %s\n" "$AMBAR" "$FIN" "$1"; AVISOS=$((AVISOS+1)); }
falla()   { printf "  %sFALTA%s   %s\n" "$ROJO" "$FIN" "$1"; FALLAS=$((FALLAS+1)); }
comando() { printf "          %s→ %s%s\n" "$NEGRITA" "$1" "$FIN"; }
nota()    { printf "          %s\n" "$1"; }
titulo()  { printf "\n%s%s%s\n" "$NEGRITA" "$1" "$FIN"; }

REPO="$(cd "$(dirname "$0")" && pwd)"
MCP="$REPO/ayds-mcp"
BOVEDA="$REPO/boveda"

SOLO_VERIFICAR=0
case "${1:-}" in
  --verificar|-v) SOLO_VERIFICAR=1 ;;
  --ayuda|-h)
    sed -n '2,20p' "$0" | sed 's/^# \{0,1\}//'
    exit 0
    ;;
  "") ;;
  *) echo "Opción desconocida: $1 (probá --ayuda)"; exit 1 ;;
esac

printf "%s=== Tutor AYDS — instalación ===%s\n" "$NEGRITA" "$FIN"
printf "Repo:    %s\n" "$REPO"
printf "Bóveda:  %s\n" "$BOVEDA"
[ "$SOLO_VERIFICAR" -eq 1 ] && printf "%sModo verificación: no se instala nada.%s\n" "$AMBAR" "$FIN"

# ---------------------------------------------------------------------------
titulo "0. El sistema"
# ---------------------------------------------------------------------------

SO="$(uname -s)"
ARQ="$(uname -m)"

if [ "$SO" = "Darwin" ]; then
  ok "macOS $(sw_vers -productVersion 2>/dev/null || echo '')  ($ARQ)"
  if [ "$ARQ" = "arm64" ]; then
    ok "Apple Silicon"
  else
    aviso "arquitectura $ARQ (no Apple Silicon) — funciona igual, pero este script está pensado para el M5"
  fi
else
  aviso "sistema $SO: este script está pensado para macOS. Los pasos de Homebrew y Claude Desktop no aplican."
fi

# ---------------------------------------------------------------------------
titulo "1. Node.js — el único requisito real del servidor"
# ---------------------------------------------------------------------------

# Por qué Node acá: las dependencias de runtime del servidor son JavaScript
# puro. No hay compilador de C ni base de datos. Python 3 SÍ hace falta, pero
# para las herramientas de la bóveda, no para el servidor: se chequea abajo.

NODE_OK=0
if command -v node >/dev/null 2>&1; then
  NODE_BIN="$(command -v node)"
  NODE_VER="$(node -p 'process.versions.node' 2>/dev/null)"
  NODE_MAY="$(node -p 'process.versions.node.split(".")[0]' 2>/dev/null)"
  NODE_ARQ="$(node -p 'process.arch' 2>/dev/null)"

  if [ "${NODE_MAY:-0}" -ge 20 ] 2>/dev/null; then
    ya "node $NODE_VER ($NODE_ARQ) en $NODE_BIN"
    NODE_OK=1
    if [ "$ARQ" = "arm64" ] && [ "$NODE_ARQ" != "arm64" ]; then
      aviso "node es $NODE_ARQ y el Mac es arm64: corre bajo Rosetta"
      nota "No hace falta cambiarlo para que funcione, pero un node arm64 es más rápido."
    fi
  else
    falla "node $NODE_VER es demasiado viejo (hace falta 20 o superior)"
    nota "NO lo actualizo por mi cuenta para no dejarte dos versiones instaladas."
    nota "Elegí UNA de estas, la que uses habitualmente:"
    comando "brew upgrade node"
    comando "nvm install 22 && nvm use 22"
  fi
else
  falla "node no está instalado"
  nota "Es lo único que falta instalar de verdad. Elegí UNA vía:"
  if command -v brew >/dev/null 2>&1; then
    comando "brew install node        # tenés Homebrew, es la vía más simple"
  else
    nota "No tenés Homebrew. Opciones:"
    comando 'brew: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)" && brew install node'
    comando "o descargar el instalador de https://nodejs.org (elegí la versión LTS, arm64)"
  fi
fi

if command -v npm >/dev/null 2>&1; then
  ya "npm $(npm -v)"
else
  [ "$NODE_OK" -eq 1 ] && falla "npm no está (raro: viene con node)"
fi

# ---------------------------------------------------------------------------
titulo "2. Lo que quizá ya tenés"
# ---------------------------------------------------------------------------

# Nada de esto lo instala el script: o ya está, o es opcional.

if [ -d "/Applications/Obsidian.app" ]; then
  ya "Obsidian instalado"
else
  aviso "no encuentro Obsidian en /Applications"
  nota "Opcional: el servidor MCP funciona sin Obsidian (lee los .md directo)."
  nota "Obsidian sirve para leer y editar la bóveda cómodamente."
  comando "brew install --cask obsidian    # o descargarlo de obsidian.md"
fi

if command -v claude >/dev/null 2>&1; then
  ya "Claude Code (CLI) en $(command -v claude)"
  CLAUDE_OK=1
else
  aviso "no encuentro el CLI 'claude'"
  nota "Hace falta si querés usar el servidor desde Claude Code."
  CLAUDE_OK=0
fi

if [ -d "/Applications/Claude.app" ]; then
  ya "Claude Desktop instalado"
  DESKTOP_OK=1
else
  aviso "no encuentro Claude Desktop (opcional si usás Claude Code)"
  DESKTOP_OK=0
fi

if [ -d "/Applications/StarUML.app" ]; then
  ya "StarUML instalado"
  if command -v curl >/dev/null 2>&1 && curl -s -m 2 http://127.0.0.1:58321/ >/dev/null 2>&1; then
    ok "su API Server responde en el puerto 58321"
  else
    aviso "su API Server no responde (¿la app está cerrada?)"
    nota "Hace falta v7+, la app abierta, y el apiServer activado en:"
    nota '  ~/Library/Application Support/StarUML/settings.json  →  {"apiServer": true, "apiServerPort": 58321}'
  fi
  nota "Para manejarlo desde Claude Code (opcional, requiere node 22+):"
  comando "claude mcp add staruml -- npx -y staruml-mcp-server"
  nota "OJO medido: sin licencia, StarUML marca TODA exportación — SVG incluido."
  nota "La lámina final sale de generar-excalidraw.py; StarUML es para modelar y validar."
  nota "Detalle: boveda/06-Proyecto-MCP/estilo-diagramas.md §5 ter y §6."
else
  aviso "no encuentro StarUML (opcional: solo para los diagramas formales)"
fi

if command -v git >/dev/null 2>&1; then
  ya "git $(git --version | awk '{print $3}')"
else
  aviso "git no está (te va a hacer falta para el repo)"
  comando "xcode-select --install"
fi

# Python 3: lo usan las herramientas de la bóveda, no el servidor.
#   boveda/sincronizar.py          valida el espejo con el repo SO2_MT
#   boveda/06-Proyecto-MCP/generar-excalidraw.py   diagramas -> .excalidraw + .svg
#   boveda/06-Proyecto-MCP/generar-mdj.py          diagramas -> .mdj de StarUML
# Solo biblioteca estándar: no hay pip ni dependencias que instalar.
# OJO: en Windows existe un "python3" falso (el alias de Microsoft Store que
# solo abre la tienda). Por eso no alcanza con command -v: hay que EJECUTARLO.
PY_OK=0
PYBIN=""
for cand in python3 python; do
  if command -v "$cand" >/dev/null 2>&1 && "$cand" -c "pass" >/dev/null 2>&1; then
    PYBIN="$cand"
    break
  fi
done
if [ -n "$PYBIN" ]; then
  ya "Python $($PYBIN -V 2>&1 | awk '{print $2}') (como '$PYBIN')"
  PY_OK=1
else
  falla "no hay un Python 3 que ejecute — lo necesitan sincronizar.py y los generadores"
  nota "Solo usan la biblioteca estándar (sin pip). Una vía alcanza:"
  comando "xcode-select --install    # o: brew install python"
fi

# ---------------------------------------------------------------------------
titulo "3. Integridad del repo"
# ---------------------------------------------------------------------------

for d in "$MCP" "$BOVEDA"; do
  if [ -d "$d" ]; then ok "existe $(basename "$d")/"; else falla "falta la carpeta $(basename "$d")/"; fi
done

for f in "$MCP/package.json" "$MCP/src/index.ts" "$BOVEDA/Índice.md" "$BOVEDA/03-Glosario.md"; do
  if [ -f "$f" ]; then ok "existe ${f#$REPO/}"; else falla "falta ${f#$REPO/}"; fi
done

N_NOTAS=$(find "$BOVEDA/01-Notas" -name '*.md' 2>/dev/null | wc -l | tr -d ' ')
if [ "$N_NOTAS" -gt 0 ]; then ok "$N_NOTAS notas en 01-Notas/"; else falla "01-Notas/ está vacía"; fi

# node_modules copiado de otra máquina: rompe el build.
# (Solo es un problema fuera de Windows: en Windows ese binario es el correcto.)
if [ "$SO" = "Darwin" ] || [ "$SO" = "Linux" ]; then
 if [ -d "$MCP/node_modules/@typescript/typescript-win32-x64" ]; then
  falla "node_modules viene de una máquina Windows"
  nota "El compilador de TypeScript trae un binario por plataforma."
  comando "rm -rf '$MCP/node_modules' '$MCP/dist'"
 fi
fi

# ---------------------------------------------------------------------------
titulo "4. Instalación del servidor"
# ---------------------------------------------------------------------------

if [ "$FALLAS" -gt 0 ]; then
  aviso "salteo la instalación: primero hay que resolver lo que falta arriba"
elif [ "$SOLO_VERIFICAR" -eq 1 ]; then
  nota "(modo verificación: no instalo)"
else
  cd "$MCP" || exit 1

  # 4.1 dependencias
  if [ -d node_modules ] && [ -f node_modules/.package-lock.json ]; then
    ya "dependencias instaladas"
    nota "Si algo falla, borralas y volvé a correr: rm -rf node_modules"
  else
    printf "          instalando dependencias...\n"
    if npm install --silent 2>&1 | tail -3; then
      hecho "npm install"
    else
      falla "npm install falló"
    fi
  fi

  # 4.2 compilación
  NECESITA_BUILD=0
  if [ ! -f dist/src/index.js ]; then
    NECESITA_BUILD=1
  else
    for f in src/*.ts pruebas/*.ts; do
      [ -f "$f" ] || continue
      if [ "$f" -nt dist/src/index.js ]; then NECESITA_BUILD=1; break; fi
    done
  fi

  if [ "$NECESITA_BUILD" -eq 0 ]; then
    ya "compilado y al día"
  else
    printf "          compilando...\n"
    if npm run build >/dev/null 2>&1; then
      hecho "npm run build"
    else
      falla "la compilación falló — corré 'npm run build' para ver el error"
    fi
  fi

  # 4.3 las tres auditorías
  if [ -f dist/pruebas/verificaciones.js ]; then
    if node dist/pruebas/verificaciones.js >/dev/null 2>&1; then
      ok "pruebas de lógica (seguridad, Unicode, escritura)"
    else
      falla "las pruebas de lógica fallaron — corré: npm run verificar"
    fi
  fi

  if [ -f pruebas/auditar-boveda.mjs ]; then
    if VAULT_PATH="$BOVEDA" node pruebas/auditar-boveda.mjs >/dev/null 2>&1; then
      ok "integridad de la bóveda y la documentación"
    else
      aviso "la auditoría de la bóveda encontró algo — corré: npm run auditar-boveda"
    fi
  fi

  if [ -f dist/pruebas/auditoria.js ]; then
    if VAULT_PATH="$BOVEDA" node dist/pruebas/auditoria.js >/dev/null 2>&1; then
      ok "las 12 herramientas responden por el protocolo MCP"
    else
      falla "la auditoría del protocolo falló — corré: npm run auditoria"
    fi
  fi

  cd "$REPO" || exit 1
fi

# ---------------------------------------------------------------------------
titulo "5. Conexión con Claude Code"
# ---------------------------------------------------------------------------

EJECUTABLE="$MCP/dist/src/index.js"

if [ "$CLAUDE_OK" -eq 0 ]; then
  aviso "sin el CLI 'claude' no puedo registrar el servidor"
elif [ ! -f "$EJECUTABLE" ]; then
  aviso "todavía no hay compilado: el registro va después del build"
elif claude mcp get tutor-ayds >/dev/null 2>&1; then
  ya "el servidor 'tutor-ayds' ya está registrado en Claude Code"
  nota "Si cambiaste la ruta del repo, volvé a registrarlo:"
  comando "claude mcp remove tutor-ayds && bash instalar.sh"
elif [ "$SOLO_VERIFICAR" -eq 1 ]; then
  nota "(modo verificación: no registro)"
else
  if claude mcp add tutor-ayds --env "VAULT_PATH=$BOVEDA" -- "$(command -v node)" "$EJECUTABLE" >/dev/null 2>&1; then
    hecho "servidor registrado en Claude Code"
  else
    aviso "no pude registrarlo automáticamente. A mano:"
    comando "claude mcp add tutor-ayds --env VAULT_PATH=\"$BOVEDA\" -- $(command -v node) \"$EJECUTABLE\""
  fi
fi

# ---------------------------------------------------------------------------
titulo "6. Claude Desktop (opcional, a mano)"
# ---------------------------------------------------------------------------

CONFIG="$HOME/Library/Application Support/Claude/claude_desktop_config.json"

if [ "$DESKTOP_OK" -eq 0 ]; then
  nota "Claude Desktop no está instalado: se puede saltear."
else
  # A propósito NO editamos el JSON: puede tener otros servidores configurados y
  # un merge automático es la clase de cosa que rompe algo en silencio.
  nota "Agregá esto a $CONFIG"
  nota "(si el archivo ya tiene otros servidores, pegá solo la parte de \"tutor-ayds\"):"
  cat <<FIN_JSON

{
  "mcpServers": {
    "tutor-ayds": {
      "command": "$(command -v node 2>/dev/null || echo /opt/homebrew/bin/node)",
      "args": ["$EJECUTABLE"],
      "env": {
        "VAULT_PATH": "$BOVEDA"
      }
    }
  }
}

FIN_JSON
  nota "La ruta de node va COMPLETA a propósito: Claude Desktop no hereda tu PATH."
  nota "Después de editar el JSON, salí de la app del todo y volvé a abrirla."
fi

# ---------------------------------------------------------------------------
titulo "7. Obsidian"
# ---------------------------------------------------------------------------

nota "Abrir Obsidian → 'Open folder as vault' → elegir:"
nota "  $BOVEDA"
nota "Plugin recomendado: Spaced Repetition (para las flashcards de 04-Flashcards/)."

# ---------------------------------------------------------------------------
titulo "8. El espejo con el repo de trabajo (SO2_MT)"
# ---------------------------------------------------------------------------

# boveda/ es un ESPEJO del vault de trabajo del repo SO2_MT: se estudia en dos
# máquinas y los dos lados tienen que quedar idénticos. Eso no se revisa a ojo:
# lo valida boveda/sincronizar.py (compara contenido archivo por archivo).
# Las únicas diferencias legítimas son .claude/ y CLAUDE.md.

VAULT_TRABAJO="${VAULT_TRABAJO:-$HOME/Desktop/SO2/AYD_2/Ayd}"

if [ -d "$VAULT_TRABAJO" ]; then
  ok "repo de trabajo encontrado: $VAULT_TRABAJO"
  if [ "$PY_OK" -eq 1 ] && [ -f "$BOVEDA/sincronizar.py" ]; then
    # Bajo Git Bash (Windows) el Python nativo no entiende rutas /c/...:
    # se convierten con cygpath. En macOS/Linux cygpath no existe y no hace falta.
    SYNC="$BOVEDA/sincronizar.py"; RV="$VAULT_TRABAJO"; RT="$REPO"
    if command -v cygpath >/dev/null 2>&1; then
      SYNC="$(cygpath -w "$SYNC")"; RV="$(cygpath -w "$RV")"; RT="$(cygpath -w "$RT")"
    fi
    if "$PYBIN" "$SYNC" --raiz-vault "$RV" --raiz-tutor "$RT" >/dev/null 2>&1; then
      ok "espejo validado: el vault y la bóveda son idénticos"
    else
      aviso "hay desfases entre el vault y la bóveda — vé el detalle con:"
      comando "$PYBIN \"$SYNC\" --raiz-vault \"$RV\" --raiz-tutor \"$RT\""
      nota "Para reparar copiando del vault hacia la bóveda, agregá --aplicar."
    fi
  elif [ "$PY_OK" -eq 0 ]; then
    aviso "sin python3 no puedo validar el espejo (ver sección 2)"
  fi
else
  aviso "no encuentro el repo de trabajo en $VAULT_TRABAJO"
  nota "La bóveda funciona sola, pero la regla del espejo necesita los dos repos:"
  comando "git clone https://github.com/Santiago78op/SO2_MT.git \"$HOME/Desktop/SO2\""
  nota "Si ya vive en otra ruta: VAULT_TRABAJO=/esa/ruta bash instalar.sh --verificar"
fi

# ---------------------------------------------------------------------------
titulo "RESULTADO"
# ---------------------------------------------------------------------------

printf "  %s pendientes, %s avisos, %s acciones realizadas\n" "$FALLAS" "$AVISOS" "$ACCIONES"

if [ "$FALLAS" -gt 0 ]; then
  printf "\n%sHay cosas pendientes. Resolvelas y volvé a correr:%s bash instalar.sh\n\n" "$ROJO" "$FIN"
  exit 1
fi

printf "\n%sListo.%s Probalo con:\n\n" "$VERDE" "$FIN"
printf "  claude\n"
printf "  > ¿Qué notas tengo sobre arquitectura de software?\n\n"
printf "Y para las tareas:\n\n"
printf "  > ¿Por dónde empiezo el Caso 1 de FarmaHosp?\n\n"
