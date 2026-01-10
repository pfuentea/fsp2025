

try:
    archivo=open("datos.txt")
    contenido=archivo.read()
except FileNotFoundError:
    print("Archivo no encontrado")

finally: # SIEMPRE se ejecuta finally
    try: # if archivo:
        archivo.close()
        print("Archivo cerrado ") # como nunca se abrió, no existe la variable
    except NameError:
        print("La variable 'archivo' no existe")