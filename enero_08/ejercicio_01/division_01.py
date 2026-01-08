#By Jocelyne
# 
def dividir():
    try:
        numero1=float(input("Debe ingresar el primer número: "))
        numero2=float(input("Debe ingresar el segundo número: "))
        resultado=numero1/numero2
    except ValueError:
        print("El número ingresado no es válido")
    except ZeroDivisionError:
        print("El número no se puede dividir por 0")
    else:
        print(f"El resultado es: {resultado} ")    
    finally:
        print("Proceso Terminado")

dividir() 