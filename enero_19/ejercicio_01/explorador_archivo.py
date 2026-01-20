import os
BASE_DIR=os.path.dirname(__file__)

def read_01(nombre_archivo):
    RUTA_ARCHIVO=os.path.join(BASE_DIR,nombre_archivo)
    
    info=os.stat(RUTA_ARCHIVO)
    print(f"Tamaño:{info.st_size}")
    with open(RUTA_ARCHIVO,"r",encoding="utf-8") as archivo:
        if info.st_size <100:
            print("---  Usando read() ---")
            contenido=archivo.read()
            print(contenido)
        else:
            print("---  Usando readline() ---")
            while True:
                linea=archivo.readline()
                if linea == "":
                    break
                print(linea)

try:
    archivo=input("Ingrese el nombre del archivo:")
    read_01(archivo)
except FileNotFoundError:
        print("Archivo no encontrado")
except Exception as e:
    print(f"Error! {e}")
finally:
    print("Gracias por usar el programa")
