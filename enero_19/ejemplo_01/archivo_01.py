import os
BASE_DIR=os.path.dirname(__file__)
RUTA_ARCHIVO=os.path.join(BASE_DIR,"prueba.txt")

def leer_archivo():
    try:
        print("Intentando abrir Archivo")
        archivo = open(RUTA_ARCHIVO,'r',encoding="utf-8")
        print("Archivo abierto")
        print("Leyendo archivo...")
        contenido= archivo.read() # leemos el archivo COMPLETO
        print("Archivo leído!")
        print("--- Contenido del archivo ---")
        print(contenido)

        print("cerrando Archivo")
        archivo.close()
        print(f"Archivo cerrado?:{archivo.closed}")

    except FileNotFoundError:
        print("Archivo no encontrado")
    except Exception as e:
        print(f"Error! {e}")
    finally:
        
        print("Gracias por usar el programa")
        
leer_archivo()