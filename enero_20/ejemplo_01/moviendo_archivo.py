import shutil

#esto lo usaremos para no tener problemas para encontrar archivos en el mismo directorio
import os
BASE_DIR=os.path.dirname(__file__)
BASE_DIR_NEW=BASE_DIR+'/nueva_carpeta'
nombre_archivo="new_archivo.txt"
RUTA_ARCHIVO=os.path.join(BASE_DIR,nombre_archivo)
# hasta aca es lo que vamos a usar siempre
RUTA_ARCHIVO_NUEVO=os.path.join(BASE_DIR_NEW,nombre_archivo)
try:
    if not os.path.exists(BASE_DIR_NEW):
        os.makedirs(BASE_DIR_NEW) #creacion de directorio si no existe
        #existe tb el mkdir
    # movió el archivo a la nueva ruta    
    # si el archivo existe ya en el nuevo directorio, lo sobreescribe
    shutil.move(RUTA_ARCHIVO,RUTA_ARCHIVO_NUEVO)
except PermissionError:
    print("No tenemos permisos")
except Exception as e:
    print(f"Ocurrio un error:{e}")

#a1: ERROR ->Hernan, Karina,Osvaldo, Jocelyne, Yuri,,Wladimir,Constanza
#a2: OK ->