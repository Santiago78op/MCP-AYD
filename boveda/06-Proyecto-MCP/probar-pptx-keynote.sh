#!/bin/bash
# Reproduce un .pptx en Keynote, lo exporta a video y extrae cuadros, para VER
# que las animaciones funcionan (solo macOS con Keynote y swift).
#
#     bash probar-pptx-keynote.sh ../08-Tareas/Grupo2_CasoHD_Presentacion.pptx [carpeta-de-salida]
#
# Deja en la carpeta: prueba.m4v y cuadros/c0000.png ... (cinco por segundo).
# Lo que hay que mirar: que la cantidad de estados estables sea laminas + clics,
# y que cada tarjeta se mueva entera. LibreOffice NO sirve para esto: convierte
# el .pptx a PDF sin ejecutar ninguna animacion.
set -e
PPTX="$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
SAL="${2:-$(mktemp -d)}"
AQUI="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$SAL/cuadros"
cp "$PPTX" "$SAL/prueba.pptx"
osascript <<OSA
with timeout of 300 seconds
tell application "Keynote"
  set d to open POSIX file "$SAL/prueba.pptx"
  delay 4
  export d to (POSIX file "$SAL/prueba.m4v") as QuickTime movie with properties {movie format:format720p}
  set n to count of slides of d
  close d saving no
  return "laminas: " & n
end tell
end timeout
OSA
swift "$AQUI/cuadros-de-video.swift" "$SAL/prueba.m4v" "$SAL/cuadros" 0.2 2>/dev/null | tail -2
echo "salida en: $SAL"
