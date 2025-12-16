'''
SISTEMA DE GESTION DE ALUMNOS

{"12345654-0":
    { "nombre":"Pedro",
      "email":"pedro@gmail.com",
      "edad":25
    }
}
'''
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent
archivo_csv=BASE_DIR / "estudiantes.csv"
estudiantes=[]

# VALIDACIONES
#validar nombre
def validar_nombre(nombre):
    nombre=nombre.strip()
    if len(nombre)<2:
        raise ValueError("El nombre debe tener más de 2 letras")
    return nombre

#validar correo
def validar_correo(email):
    if "@" not in email or "." not in email:
        raise ValueError("Email inválido!")

    return email

#validad edad
def validar_edad(edad):
    try:
        edad=int(edad)
    except ValueError:
        raise ValueError("Edad debe ser un número")
    
    if edad <0 or edad >120:
        raise ValueError("Edad fuera del rango 0-120")

    return edad
#validar rut
def validar_rut(rut):
    rut=rut.strip()
    if "-" in rut:
        numero,dv=rut.split("-")
        dv=dv.lower()
        if not numero.isdigit():
            raise ValueError("El rut no es correcto (1)")
        
        if dv == "" or ( not dv.isdigit() and dv !="k"):
            raise ValueError("El rut no es correcto (2)")
    else:
        raise ValueError("El rut debe tener guión")
    
    return f"{numero}-{dv}"
        

# BUSQUEDAS
#buscar estudiante por rut
# busco dentro de la lista un elemento que tenga como llave el rut
# si lo encuentro, devuelvo el indice donde está el estudiante
# si no devuelvo -1
def buscar_indice_por_rut(rut):
    for i, alumno in enumerate(estudiantes):
        if rut in alumno:
            return i
    
    return -1


def obtener_estudiante_por_rut(rut):
    # busco el indice del estudiante que tenga el rut ingresado
    # retorno el diccionario con los datos del estudiante 
    indice=buscar_indice_por_rut(rut)
    if indice == -1:
        return None
    return estudiantes[indice]


# CRUD (create-read-update-delete)
# create
def crear_estudiante():
    try:
        rut=validar_rut(input("Ingrese el rut del estudiante:"))
        nombre=validar_nombre(input("Ingrese el nombre:"))
        email=validar_correo(input("Ingrese el email:"))
        edad=validar_edad(input("Ingrese la edad:"))
        estudiante={
            rut:{
                "nombre":nombre,
                "email":email,
                "edad":edad
            }
        }
        estudiantes.append(estudiante)
    except ValueError as e:
        print(f"Error:{e}")

# read (by_id, all)
def buscar_estudiante():
    try:
        rut=validar_rut(input("Ingrese el rut del estudiante a buscar:"))
        datos=obtener_estudiante_por_rut(rut)
        if datos is None:
            print("El estudiante no existe")
        else:
            print(f"Estudiante con el rut:{rut}")
            print(f"Nombre:{datos["nombre"]}")
            print(f"Correo:{datos["email"]}")
            print(f"Edad:{datos["edad"]}")
    except ValueError as e:
        print(f"Error:{e}")

# update
def editar_estudiante():
    pass
# delete

# TRABAJO CON ARCHIVOS
#lectura
#escritura
# MENU
def mostrar_menu():
    print("===== SISTEMA DE GESTION DE ESTUDIANTES=====")
    print("1.- Crear Estudiante")
    print("2.- Buscar Estudiante")
    print("3.- Editar Estudiante")
    print("4.- Borrar Estudiante")
    print("0.- Salir")

# PROGRAMA PRINCIPAL
def main():
    while True:
        mostrar_menu()
        opcion=input("Selecciona una opción:")
        if opcion=="1":
            crear_estudiante()
        elif opcion=="2":
            buscar_estudiante()
        elif opcion=="3":
            editar_estudiante()
        elif opcion=="4":
            pass
        elif opcion=="5":
            pass
        elif opcion=="6":
            pass
        elif opcion=="7":
            pass
        elif opcion=="0":
            break

main()


