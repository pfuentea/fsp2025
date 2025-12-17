import crud
import archivos_csv

def mostrar_menu():
    print("===== SISTEMA DE GESTION DE ESTUDIANTES=====")
    print("1.- Crear Estudiante")
    print("2.- Buscar Estudiante")
    print("3.- Editar Estudiante")
    print("4.- Borrar Estudiante")
    print("5.- Listar todos los estudiante")
    print("6.- Guardar en CSV")
    print("7.- Cargar en CSV")
    print("0.- Salir")

# PROGRAMA PRINCIPAL
def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion=input("Selecciona una opción:")
        if opcion=="1":
            crud.crear_estudiante()
        elif opcion=="2":
            crud.buscar_estudiante()
        elif opcion=="3":
            crud.editar_estudiante()
        elif opcion=="4":
            crud.borrar_estudiante()
        elif opcion=="5":
            crud.listar_todos()
        elif opcion=="6":
            archivos_csv.guardar_csv()
        elif opcion=="7":
            archivos_csv.cargar_csv()
        elif opcion=="0":
            break