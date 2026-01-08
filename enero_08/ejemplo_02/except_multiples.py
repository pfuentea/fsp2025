try:
    numero=int(input("Ingrese un entero para dividir al 10:"))
    resultado=10/numero

except ValueError:
    print("El valor ingresado no es un entero")

except ZeroDivisionError:
    print("Un número no se puede dividir por cero")
    