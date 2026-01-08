#By Karina

# función para convertir kilómetros a millas
def convertir_km_a_millas():

    # bucle 
    while True:
        try:
          
            km = float(input("Ingrese la distancia en kilómetros: "))
            millas = km * 0.621371

        except ValueError:
           
            print(" Error: debe ingresar un número válido.")

        else:

            print(f"✓ {km} km equivalen a {millas:.2f} millas")
            break  

        finally:
            print("Intento de conversión finalizado")

convertir_km_a_millas()