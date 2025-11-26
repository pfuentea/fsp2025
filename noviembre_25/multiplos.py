# BY SANDRA

numero = int(input("Ingresa un número entero: "))

# Para verificar si es divisible por 2 Y por 3 (par y múltiplo de 3)

if numero % 2 == 0 and numero % 3 == 0:
    print("El número es par y múltiplo de 3.")
elif numero % 2 == 0:
    print("El número es par solamente (no es múltiplo de 3).")
elif numero % 3 == 0 and numero %2 != 0:
    print("El número es impar y múltiplo de 3.")
else:
    print("impar y no multiplo de 3")