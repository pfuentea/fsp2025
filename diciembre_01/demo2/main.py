from modulos.productos import crear_producto,mostrar_inventario

while True:
    crear_producto()

    opcion=input("Desea registrar otro producto?(s/n):")
    if opcion =="n":
        break
    else:
        continue

mostrar_inventario() 


