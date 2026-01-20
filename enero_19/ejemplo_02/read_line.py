import os
BASE_DIR=os.path.dirname(__file__)
RUTA_ARCHIVO=os.path.join(BASE_DIR,"prueba.txt")

def read_01():
    print("---  Usando read() ---")
    with open(RUTA_ARCHIVO,"r",encoding="utf-8") as archivo:
        contenido=archivo.read()
        print(contenido)
        print(f"Tipo devuelto:{type(contenido)}")

def read_02():
    print("---  Usando readline() ---")
    with open(RUTA_ARCHIVO,"r",encoding="utf-8") as archivo:
        while True:
            linea = archivo.readline()
            if linea == "":
                break
            print(linea)
    print(f"Tipo devuelto:{type(linea)}")

def read_03():
    print("---  Usando readlines() ---")
    with open(RUTA_ARCHIVO,"r",encoding="utf-8") as archivo:
        lineas=archivo.readlines()
        print(lineas)
        print(f"Tipo devuelto:{type(lineas)}")
        if lineas:
            print(f"Tipo del primer elemento:{type(lineas[0])}")


try:
    read_01()
    read_02()
    read_03()
except FileNotFoundError:
        print("Archivo no encontrado")
except Exception as e:
    print(f"Error! {e}")
finally:
    
    print("Gracias por usar el programa")