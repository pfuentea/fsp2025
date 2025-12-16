'''
Ejercicio:

1.- Leer un archivo de texto con los datos de usuarios
2.- validar cada registro usando try/except
3.- Construir una lista de usuarios válidos
4.- Escribir los usuarios válidos en un archivo nuevo
5.- Escribir los usuarios inválidos en un archivo de errores
Validaciones:
a.- Nombre tenga al menos 2 letras: Ed
b.- validad edad entre 0 y 120
c.- validar que correo tenga @ y un . 
'''
def validar_usuario(linea):
    #Ana;25;ana@ejemplo.com
    partes=linea.strip().split(";") #lista de 3 elemento: 0,1,2

    if len(partes)!=3:
        raise ValueError("Formato incorrecto, no vienen 3 campos.")
    nombre=partes[0]
    edad=partes[1]
    correo=partes[2]
    # validar nombre
    if len(nombre.strip()) <2:
        raise ValueError("Nombre muy corto") 
    
    #validar edad
    try:
        edad=int(edad)
    except ValueError as e:
        raise ValueError("Edad no es un número entero")

    if edad<0 or edad>120:
        raise ValueError("Edad fuera del rango normal (0-120)") 
    
    #validar email : validar que correo tenga @ y un . 
    #si no esta el @ o el . , 
    #si la @ no esta en el correo o el punto no esta en el correo
    if "@" not in correo or "." not in correo:
        raise ValueError("Correo no válido")
    
    return {"nombre":nombre,"edad":edad,"email":correo}

def procesar_archivo():
    usuario_validos=[]
    errores=[]

    try:
        with open("usuarios_raw.txt","r",encoding="utf-8") as archivo:
            lineas = archivo.readlines()
            for linea in lineas:
                try:
                    usuario=validar_usuario(linea)
                    usuario_validos.append(usuario)
                except Exception as e:
                    errores.append(linea)
    except FileNotFoundError as e:
        print("Archivo no encontrado")
    else:
        print("Archivo procesado correctamente")
    finally:
        print("Fin de la lectura del archivo")


    with open("nuevo_archivo.txt","w",encoding="utf-8") as f1:
        for usuario in usuario_validos:
            f1.write(f"{usuario["nombre"]};{usuario["edad"]};{usuario["email"]}\n")

    with open("errores.txt","a",encoding="utf-8") as f2:
        for error in errores:
            f2.write(error)

    print("Termino del procesamiento")
    print(f"Lineas con usuarios válidos:{len(usuario_validos)}")
    print(f"Lineas con errores:{len(errores)}")

procesar_archivo()