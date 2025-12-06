#Crear un diccionario productos donde cada clave sea un ID ("P001", "P002", etc.)
#Cada valor será un diccionario con los campos: nombre, precio, stock
productos={
    "P001":{"nombre":"teclado","precio":10000,"stock":10},
    "P002":{"nombre":"mouse","precio":5000,"stock":20},
}

def menu():
    print("Seleccione una opción")
    print("1: agregar un producto")
    print("2: para modificar stock")
    print("3: eliminar un producto")
    print("4: ver los productos")
    print("5: mostrar productos con stock <10")
    print("6:ver producto por su ID")
    print("0: para salir")

def get_codigo():
    id_prod=input("El código del producto:").upper()
    if id_prod in productos:
        return id_prod
    else:
        print("producto no existe!")
        return False
    
def siguiente_codigo(diccionario): #P001  # B001
    lista_llave=list(diccionario.keys())
    ultima_llave=lista_llave[-1] # len(productos)-1
    prefijo=ultima_llave[0] # en este caso es la P
    numero=int(ultima_llave[1:]) #010 
    siguiente_numero=numero+1
    return f"{prefijo}{siguiente_numero:03d}"

contador=0
while True:
    menu()
    opcion=input("Ingrese una opción:")
    
    if opcion=="0":
        print("Gracias por usar nuestro sistema")
        break
    #Agregar un nuevo producto al diccionario
    elif opcion=="1":
        print("Ingrese los datos del nuevo producto")
        new_prod=input("Ingrese el producto, precio y stock, separado por coma:")
        # new_prod=producto,precio,stock
        nuevo_prod=list(new_prod.split(","))
        #generar los códigos de manera correcta (deuda tecnica)
        
        nuevo_cod=siguiente_codigo(productos)

        # como la llave no existe la crea, pero si existe la actualiza
        try:
            productos[nuevo_cod]={
                "nombre":nuevo_prod[0],
                "precio":int(nuevo_prod[1]),
                "stock":int(nuevo_prod[2])
                }
        except ValueError as e:
            print("Debe ingresar un número:",e)
        except IndexError as e:
            print("Debe ingresar 3 elementos:",e)
    elif opcion=="2": #modificar stock
        # pedir el id producto -> id_prod
        id_prod=get_codigo()
        if id_prod:
        #pedir el nuevo stock
            try:
                nuevo_stock=int(input("Ingrese el nuevo stock:"))
                productos[id_prod]["stock"] =nuevo_stock
            except:
                print("stock incorercto")
                    
    elif opcion=="3":
        #eliminar producto
        # pedir el id producto -> id_prod
        id_prod=get_codigo()
        if id_prod:
            productos.pop(id_prod)

    elif opcion=="4":
        #ver productos
        
        for id_prod,producto in productos.items():
            print(f"Producto :{id_prod}")
            print(f"Nombre:{producto["nombre"]}")
            print(f"Precio:{producto["precio"]}")
            print(f"Stock:{producto["stock"]}")
            print("--------------------")
    elif opcion=="5":
        # mostrar productos con stock <10
        for id_prod,producto in productos.items():
            if producto["stock"] <10:
                print(f"Producto :{id_prod}")
                print(f"Nombre:{producto["nombre"]}")
                print(f"Precio:{producto["precio"]}")
                print(f"Stock:{producto["stock"]}")
                print("--------------------")
        #solucion 2
        # bajo_stock= {k: v for k, v in productos.items()  if v["stock"] <10}
        # print("Stock Bajo:",bajo_stock)
    #Acceder a los datos de un producto por su ID
    elif opcion=="6":
        id_prod=get_codigo()
        if id_prod:
            print(f"^Los datos del producto son {productos[id_prod]}")
            contador +=1

print(f"Usted consultó {contador} veces ")