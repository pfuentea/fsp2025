#By Gloria
def division_segura():
    try:
        numerador = int(input("Ingrese el numerador: "))
        denominador = int(input("Ingrese el denominador: "))

        resultado = numerador // denominador

    except ZeroDivisionError:
        print("Error: no se puede dividir por cero.")

    except ValueError:
        print("Error: debe ingresar solo números enteros.")
    else:
        print("Resultado:", resultado)

    finally:
        print("Proceso de división finalizado.")

division_segura()