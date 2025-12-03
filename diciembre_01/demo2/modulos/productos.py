from .validaciones import validar_int, validar_float,validar_str

inventario=[]

def crear_producto():
    print("Ingrese los datos del producto:")
    nombre=input("Nombre del producto:")
    categoria=input("Categoria del producto:")
    precio=float(input("Ingrese el precio del producto:"))

    stock=input("Ingrese el stock del producto")
    if validar_int(stock):
        print("Stock es un entero")
        stock=int(stock)
    else:
        print("Stock no es un entero")
        stock=0

    if validar_float(precio):
        print("Precio es un entero")
        precio=float(precio)
    else:
        print("Precio no es un entero")
        precio=0
    if validar_str(nombre):
        pass
    else:
        nombre="Sin nombre"

    if validar_str(categoria):
        pass
    else:
        categoria="Sin Categoria"

    en_oferta="n"
    if precio<10:
        en_oferta="s"
    producto={
        "nombre":nombre,
        "categoria":categoria,
        "precio":precio,
        "stock":stock,
        "en_oferta":en_oferta
    }
    inventario.append(producto)

def mostrar_inventario():
    for prod in inventario:
        print(f"Nombre:{prod['nombre']}")
        print(f"Categoria:{prod['categoria']}")
        print(f"Precio:{prod['precio']}")
        print(f"Stock:{prod['stock']}")
        print(f"En oferta:{prod['en_oferta']}")

'''
# de esta manera va construyendose la lista INVENTARIO
# cada producto es un diccionario
[
    {
        "nombre":"pan",
        "categoria":"pan",
        "precio":1800.0,
        "stock":20,
        "en_oferta":"n"
    },
    {
        "nombre":"sopa",
        "categoria":"caldo",
        "precio":2000.0,
        "stock":30,
        "en_oferta":"n"
    },
]
'''