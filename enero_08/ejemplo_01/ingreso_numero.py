
try:
    edad=int(input("Ingrese su edad:"))
    print(f"Edad ingresada es:{edad}")
except ValueError:
    print("El valor ingresado no es un entero")