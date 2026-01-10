class ErrorValidation(Exception):
    pass

def procesar_pago(monto):
    if monto <=0:
        raise ValueError("El monto debe ser mayor a cero")
    
def ejecutar_pago():
    try:
        procesar_pago(-50)
    except ValueError as e:
        print("Error detectado en la función interna")
        raise ErrorValidation("El monto no cumple las reglas")

ejecutar_pago()