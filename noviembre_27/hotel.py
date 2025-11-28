habitaciones={
    1:("Habitación single",35000),
    2:("Habitación doble",55000),
    3:("Habitación triple",75000),
    4:("Habitación deluxe",120000),
    5:("Suite presidencial",250000),
}

# diccionario ={llave:valor}

print("==Bienvenido al sistema de reservas==")
try:
    tipo_habitacion=int(input("Seleccione el tipo de habitación (1-5):"))
    total_noches=int(input("Ingrese el total de noches:"))

    habitacion_y_precio=habitaciones.get(tipo_habitacion) # el método get me trae el valor en el diccionario de la llave "tipo_habitacion"

    if habitacion_y_precio is None:
        print("Opción no válida")
    else:
        nombre_habitacion , precio_habitacion = habitacion_y_precio #("Suite presidencial",250000), acá separo la tupla
        # para calcular el total con descuento precio_habitacion=precio_habitacion*(1-descuento)
        total_a_pagar=precio_habitacion*total_noches
        print(f"Habitación:{nombre_habitacion}")
        print(f"Precio por noche: {precio_habitacion}")
        print(f"Cantidad de noches:{total_noches}")
        print(f"Total a pagar:{total_a_pagar}")

except:
    print("Error: debes ingresar una opción válida")

