import crud

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
archivo_csv=BASE_DIR / "estudiantes.csv"

def guardar_csv(archivo=archivo_csv):
    estudiantes=crud.obtener_todos_estudiantes()
    if not estudiantes:
        print("no hay estudiantes para guardar")
    try:
        with open(archivo,"w",encoding='utf-8') as f:
            for estudiante in estudiantes:
                rut=next(iter(estudiante.keys()))
                datos=estudiante[rut]
                f.write(f"{rut};{datos["nombre"][0]};{datos["nombre"][1]};{datos["email"]};{datos["edad"]}\n")
        print("Guardado el archivo con éxito")
    except OSError as e:
        print("Error al escribir el archivo")
    
#escritura
def cargar_csv(archivo=archivo_csv):
    nuevas=[]
    global estudiantes
    try:
        with open(archivo,"r",encoding='utf-8') as f:
            lineas=f.readlines()
            if not lineas:
                print("Archivo vacío!")
                return
            for linea in lineas:
                rut,nombre,apellido,email,edad=linea.split(";")
                #podrían existir validaciones de todos los campos antes de crear un registro

                nuevas.append({rut:{"nombre":(nombre,apellido),
                                    "email":email,
                                    "edad":edad}})
        #estudiantes=nuevas
        crud.cargar_todos_estudiantes(nuevas)
        print("El archivo fue cargado exitosamente!")
    except FileNotFoundError:
        print("El archivo no existe!")

    except OSError as e:
        print("Error al leer el archivo")
