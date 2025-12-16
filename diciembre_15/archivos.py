'''
vamos a crear dos métodos, uno para guardar un mensaje 
en un archivo y otro para leerlo
'''

def guardar_mensaje():
    # modo "w" es para escribir (write)
    with open("mensaje.txt","w",encoding="utf-8") as archivo_mensaje:
        while True:
            mensaje=input("Ingrese el mensaje a guardar en el archivo o 0 si no quiere escribir más:")
            if mensaje=="0":
                break
            archivo_mensaje.write(mensaje+"\n")

def leer_mensaje():
    # modo "r" es para escribir (read)
    # Que problema podría existir al abrir un archivo??
    #
    try: 
        with open("mensaje.txt","r",encoding="utf-8") as archivo_mensaje:
            linea=archivo_mensaje.read()
            print("contenido del archivo")
            print(linea)
    except FileNotFoundError as e:
        print("El archivo no existe")

'''
guardar un archivo en formato CSV (separado por comas)
ingresar nombre, edad, correo por consola
'''
def ingreso_usuario():
    nombre=input("Ingrese el nombre:")
    edad=input("Ingrese la edad:")
    correo=input("Ingrese el correo:")
    # modo "a" es para agregar (append)
    with open("./archivos/usuarios.txt","a",encoding="utf-8") as archivo:
        archivo.write(f"{nombre},{edad},{correo}\n")

'''
modos en archivos:
r : leer
w : escribir TODO
a : agregar
x : crear archivo (da un error si ya existe)
r+ :Leer y escribir (r con a) no borra nada
w+ : Leer y escribir (r con w) borra todo antes de escribir
'''
#guardar_mensaje()
#leer_mensaje()

ingreso_usuario()
    
