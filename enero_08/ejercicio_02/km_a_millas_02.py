#By Gloria

while True:
    try:
        km = float(input("Ingrese una distancia en kilómetros: "))
        millas = km * 0.621371
        print(f"{km} km equivalen a {millas:.2f} millas")
        break
    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número válido.")