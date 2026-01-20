import os
import sys
BASE_DIR=os.path.dirname(__file__)
RUTA_ARCHIVO=os.path.join(BASE_DIR,"prueba.txt")

def leer_archivo():
    try:
        fd1=sys.stdin.fileno() # teclado es 0 
        print(f"el FD de la entrada estandar es:{fd1}")
        print("Intentando abrir Archivo")
        archivo = open(RUTA_ARCHIVO,'r',encoding="utf-8")

        print(f"Archivo abierto:{archivo.name}, en modo {archivo.mode}")
        print(f"File descriptor: {archivo.fileno()} ")
        print("Leyendo archivo...")
        contenido= archivo.read() # leemos el archivo COMPLETO
        print("Archivo leído!")
        print("--- Contenido del archivo ---")
        print(contenido)

        print("cerrando Archivo")
        print(f"Archivo cerrado?:{archivo.closed}")
        print("Ahora si lo cerramos")
        archivo.close()
        print(f"Archivo cerrado?:{archivo.closed}")

    except FileNotFoundError:
        print("Archivo no encontrado")
    except Exception as e:
        print(f"Error! {e}")
    finally:
        
        print("Gracias por usar el programa")
        
leer_archivo()