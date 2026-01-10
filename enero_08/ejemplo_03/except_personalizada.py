class EdadInvalidaError(Exception):
    pass

def validar_edad(edad):
    if edad <0:
        raise EdadInvalidaError("La edad no puede ser negativa")
    print(f"Edad válida:{edad} años")


try:
    validar_edad(-3)
except EdadInvalidaError:
    print("Error en el ingreso de la edad")
