from pathlib import Path
# BASE_DIR nos traerá la ruta ABSOLUTA de donde estamos ejecutando el programa
BASE_DIR = Path(__file__).resolve().parent

#print(BASE_DIR)

archivo1=BASE_DIR / "documentos/prueba.txt"
archivo_errores=BASE_DIR / "documentos/errores.txt"

print(archivo1)

if archivo1.exists():
    print("El archivo existe!")
    # Podremos abrir el archivo sin problema
else:
    print("El archivo no existe")