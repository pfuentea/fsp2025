import os
BASE_DIR=os.path.dirname(__file__)
nombre_archivo="salida.txt"
RUTA_ARCHIVO=os.path.join(BASE_DIR,nombre_archivo)

with open(RUTA_ARCHIVO,"w",encoding="utf-8") as archivo:
    archivo.write("Hola mundo 2\n")
    archivo.write("cómo están?\n")

    while True:
        mensaje=input("Ingrese su mensaje o vacio para salir:")
        if mensaje =="":
            break
        archivo.write(mensaje)
        archivo.write("\n") # agregamos salto de linea
        # para crear un TAB \t , para un salto de linea es \n

    varias_lineas=['primera linea\n','segunda linea\n','tercera linea\n']
    archivo.writelines(varias_lineas)