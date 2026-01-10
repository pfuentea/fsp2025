def validar_edad(edad):
    if edad <0:
        raise ValueError("La edad no puede ser negativa")
    print(f"Edad válida:{edad} años")

def entero(numero):
    try:
        new_numero=int(numero)
    except ValueError:
        raise ValueError("No se puede convertir a entero el valor")

#entero("dos")
try:
    validar_edad(25)
    #validar_edad(-3)
    #ValueError: invalid literal for int() with base 10: 'dos'
    #int("dos")
    entero("dos")
except ValueError as e:
    print(f"Error:{e}")