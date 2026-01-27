from pathlib import Path

BASE_DIR=Path(__file__).resolve().parent.parent
DIR_REPORTE=BASE_DIR / "reportes"
DIR_LOGS=BASE_DIR / "logs"
DIR_DATOS=BASE_DIR / "datos"
#print(BASE_DIR)

# crear los archivos y rutas que utilizaremos
archivo_reporte="resumen.txt"
RUTA_REPORTE=DIR_REPORTE/archivo_reporte

# print(RUTA_REPORTE)

# DEBEMOS PREGUNTAR SI EXISTE EL DIRECTORIO, SI NO EXISTE CREARLO



