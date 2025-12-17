from validaciones import validar_correo,validar_edad,validar_nombre,validar_rut

estudiantes=[]

def buscar_indice_por_rut(rut):
    for indice, alumno in enumerate(estudiantes):
        if rut in alumno:
            return indice
    return -1

def obtener_estudiante_por_rut(rut):
    # busco el indice del estudiante que tenga el rut ingresado
    # retorno el diccionario con los datos del estudiante 
    indice=buscar_indice_por_rut(rut)
    if indice == -1:
        return None
    return estudiantes[indice][rut]

# CRUD (create-read-update-delete)
# create
def crear_estudiante():
    try:
        rut=validar_rut(input("Ingrese el rut del estudiante:"))
        nombre=validar_nombre(input("Ingrese el nombre:"))
        apellido=validar_nombre(input("Ingrese el apellido:"))
        email=validar_correo(input("Ingrese el email:"))
        edad=validar_edad(input("Ingrese la edad:"))
        estudiante={
            rut:{
                "nombre":(nombre,apellido),
                "email":email,
                "edad":edad
            }
        }
        estudiantes.append(estudiante)
    except ValueError as e:
        print(f"Error:{e}")

# read (by_id, all)
def listar_todos():
    for indice, estudiante in enumerate(estudiantes):
        rut=next(iter(estudiante.keys()))
        datos=estudiante[rut]
        print(f"Estudiante con el rut:{rut}")
        print(f"Nombre:{datos["nombre"][0]}")
        print(f"Apellido:{datos["nombre"][1]}")
        print(f"Correo:{datos["email"]}")
        print(f"Edad:{datos["edad"]}")

def buscar_estudiante():
    try:
        rut=validar_rut(input("Ingrese el rut del estudiante a buscar:"))
        datos=obtener_estudiante_por_rut(rut)
        
        if datos is None:
            print("El estudiante no existe")
        else:
            print(f"Estudiante con el rut:{rut}")
            print(f"Nombre:{datos["nombre"][0]}")
            print(f"Apellido:{datos["nombre"][1]}")
            print(f"Correo:{datos["email"]}")
            print(f"Edad:{datos["edad"]}")
    except ValueError as e:
        print(f"Error:{e}")

# update
def editar_estudiante():
    try:
        rut=validar_rut(input("Ingrese el rut del estudiante a buscar:"))
        indice=buscar_indice_por_rut(rut)
        if indice == -1:
            print("No existe estudiante con ese rut")
            return
        datos=estudiantes[indice][rut]
        ''' esto es lo que obtengo en datos
        { "nombre":"Pedro",
        "email":"pedro@gmail.com",
        "edad":25
        }
        '''
        print("Deje en blanco paramantener el valor actual.")
        print(f"Nombre:{datos["nombre"][0]}")
        print(f"Apellido:{datos["nombre"][1]}")
        print(f"Email:{datos["email"]}")
        print(f"Edad:{datos["edad"]}")
        nuevo_nombre=input("Nuevo nombre:")
        nuevo_apellido=input("Nuevo apellido:")
        nuevo_correo=input("Nuevo email:")
        nueva_edad=input("Nueva edad:")

        if nuevo_nombre:
            nombre=validar_nombre(nuevo_nombre)
        else:
            nombre=datos["nombre"][0]

        if nuevo_apellido:
            apellido=validar_nombre(nuevo_apellido)
        else:
            apellido=datos["nombre"][1]
        
        datos["nombre"]=(nombre,apellido)

        if nuevo_correo:
            datos["email"]=validar_correo(nuevo_correo)
        if nueva_edad:
            datos["edad"]=validar_edad(nueva_edad)
    except ValueError as e:
        print(f"Error:{e}")
# delete
def borrar_estudiante():
    try:
        rut=validar_rut(input("Ingrese el rut del estudiante a buscar:"))
        indice=buscar_indice_por_rut(rut)
        if indice == -1:
            print("No existe estudiante con ese rut")
            return
        confirm=input(f"Está seguro que quiere borrar el estudiante con rut:{rut}?(s/n)").strip().lower()
        
        if confirm =="s":
            estudiantes.pop(indice)
            print("Estudiante eliminado")
        elif confirm =="n":
            print("Borrado cancelado")
        else:
            print("Opción no válida")

    except ValueError as e:
        print(f"Error:{e}")

def obtener_todos_estudiantes():
    return estudiantes

def cargar_todos_estudiantes(nuevos_estudiantes):
    global estudiantes
    estudiantes=list(nuevos_estudiantes)