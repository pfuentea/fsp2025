#By Jocelyne

def millas():
    valor_millas=0.621371

    while True:
        ingreso=input("Ingrese una distancia en kilómetros: " )
        try:
            km=float(ingreso)
            millas1=km*valor_millas
            print(f"Los {km} kilómetros equivalen  a: {millas1:.2f} millas")
            break
        except ValueError:
            print("Ingrese un número válido, use un número con decimales")

millas()