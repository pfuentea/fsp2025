#By Camila

def division_segura():
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        
        resultado = num1 / num2

    except ValueError:
        print("Error: Solo puedes ingresar números.")
    
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")

    else:
        print(f"La división es: {resultado}")

    finally:
        print("Proceso finalizado.")

division_segura()