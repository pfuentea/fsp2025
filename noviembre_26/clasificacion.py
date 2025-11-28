producto=input("Ingrese el nombre del producto:")
stock=input("esta en stock? (s/n):")
categoria=input("Ingrese la categoria del producto:")

if stock=="s":
    print("El producto esta en Stock")
else:
    print("El producto no esta en Stock")

mensaje=f"El producto {producto}, pertenece a "
#mensaje="El producto"+producto+", pertenece a "

if categoria=="electrodomestico":
    print(mensaje+categoria)
elif categoria=="telefono":
    print(mensaje+categoria)
elif categoria=="computadora":
    print(mensaje+categoria)  
elif categoria=="accesorio":
    print(mensaje+categoria)
else:
    print(f"El producto {producto} no tiene categoria asociada")

'''
#solucion 2
if categoria=="electrodomestico" or categoria=="telefono" or categoria=="computadora" or categoria=="accesorio":
    print(mensaje+categoria)

#solucion 3
categorias=['electrodomestico','telefono','computadora','accesorio']

if categoria in categorias:
    print(mensaje+categoria)
'''