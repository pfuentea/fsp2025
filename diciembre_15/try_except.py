class MuyGrandeException(Exception):
    pass

def dividir_desde_input():
    '''
    Pediremos dos números por consola y los intentaremos dividir
    ValueError: invalid literal for int() with base 10: 'e'
    ZeroDivisionError: division by zero

    el bloque completo es try-except-else-finally , con estos últimos dos opcionales
    '''
    try:
        dividendo=int(input("Ingrese el dividendo:"))
        divisor=int(input("Ingrese el divisor:"))

        if dividendo>1000:
            raise MuyGrandeException("El número es muy grande")

        if divisor==0:
            raise ZeroDivisionError("El divisor no puede ser 0")
        
        resultado=dividendo/divisor
    #estas excepciones serán capturadas en caso de error
    except ValueError as e:
        print("Error: debes ingresar solo números")
        print(f"Detalle del error:{e}")
    except ZeroDivisionError as e:
        print(f"Error en la division:{e}")
    except Exception as e:
        print("Ocurrió un error inesperado")
        print(f"Tipo:{type(e).__name__}")
        print(f"Detalle del error:{e}")
    else:  # se ejecuta si no existe ninguna excepcion
        print("División realizada con éxito")
        print(f"El resultado de {dividendo}/{divisor} es {resultado}")
    finally: # un bloque que se ejecutara siempre si hay una excepción o no
        print("Fin de la operación!")

dividir_desde_input()