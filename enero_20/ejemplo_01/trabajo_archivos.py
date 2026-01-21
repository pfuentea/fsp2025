#esto lo usaremos para no tener problemas para encontrar archivos en el mismo directorio
import os
BASE_DIR=os.path.dirname(__file__)
nombre_archivo="salida.txt"
RUTA_ARCHIVO=os.path.join(BASE_DIR,nombre_archivo)
# hasta aca es lo que vamos a usar siempre

#creamos la variable del archivo nuevo en la misma ruta
nuevo_nombre="new_archivo.txt"
RUTA_ARCHIVO_NUEVO=os.path.join(BASE_DIR,nuevo_nombre)

#con esto podemos renombrar un archivo
os.rename(RUTA_ARCHIVO,RUTA_ARCHIVO_NUEVO)

