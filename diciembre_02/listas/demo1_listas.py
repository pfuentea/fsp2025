# tarea: agregar try y except donde corresponda
tareas=['hacer la comida','programar','estudiar','revisar código']

while True:
    print("Tareas actuales:")
    
    if len(tareas) == 0 : # el método len nos dice la cantidad de elementos (largo de la lista)
        print("No hay tareas en la lista")
    else:
        for indice,tarea in enumerate(tareas):
            print(f"{indice+1}:{tarea}")

    #esto es el programa principal, que hacemos hasta que salgamos
    print("Seleccione una opción:")
    print("1) Agregar una tarea")
    print("2) Eliminar una tarea")
    print("3) Salir")

    opcion=int(input("Elige una opcion 1-2-3:"))
    if opcion == 1:
        nueva_tarea= input("Ingrese la nueva tarea:")
        tareas.append(nueva_tarea) #append agrega un elemnto al final de la lista
        print("tarea agregada exitosamente!")
    elif opcion == 2:
        # si no hay tareas enviar mensaje de error
        if len(tareas) == 0 :
            print("No existen tareas para elimnar")
        # si hay al menos una tarea, pedimos al usuario el numero y la eliminamos
        else:
            indice=int(input("Ingrese la tarea a eliminar:"))
            tarea_completa=tareas.pop(indice-1)
            print("Tarea eliminada exitosamente!")
    elif opcion==3:
        if len(tareas) > 0 :
            print("Salimos, pero quedan tareas pendientes")
        else:
            print("Todas las tareas completadas")
        break
    else: # cualquier opcion que no este entre 1-2-3
        print("Opción no válida")