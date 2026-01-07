# by Gloria
# CLASE BASE
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def calcular_precio_final(self):
        return self.precio

# SUBCLASES
class ProductoFisico(Producto):
    def __init__(self, nombre, precio, costo_envio):
        super().__init__(nombre, precio)
        self.costo_envio = costo_envio

    def calcular_precio_final(self):
        return self.precio + self.costo_envio


class ProductoDigital(Producto):
    def __init__(self, nombre, precio, descuento):
        super().__init__(nombre, precio)
        self.descuento = descuento  

    def calcular_precio_final(self):
        return self.precio - (self.precio * self.descuento / 100)


class Suscripcion(Producto):
    def __init__(self, nombre, precio, porcentaje_mensual):
        super().__init__(nombre, precio)
        self.porcentaje_mensual = porcentaje_mensual

    def calcular_precio_final(self):
        return self.precio + (self.precio * self.porcentaje_mensual / 100)



# PASO 1: LISTA DE PRODUCTOS

productos = [
    ProductoFisico("Notebook", 800000, 20000),
    ProductoDigital("Curso Python", 50000, 15),
    Suscripcion("Spotify", 8000, 10),
    Producto("Papel de fotocopia",5000)
]


# Clasificación + validación dinámica

for producto in productos:

    print("---------------")

    precio_final = producto.calcular_precio_final()
    if isinstance(producto, ProductoDigital):
        print("Tipo: Producto Digital")
        # descuento adicional
        precio_final -= precio_final * 0.05
        print(f"{producto.nombre} - Precio final con descuento adicional: ${precio_final}")

    elif isinstance(producto, Suscripcion):
        print("Tipo: Suscripción")
        print("facturación mensual")
        print(f"{producto.nombre} - Pago mensual: ${precio_final}")

    elif isinstance(producto, ProductoFisico):
        print("Tipo: Producto Físico")
        print(f"{producto.nombre} - Precio final con envío: ${precio_final}")

    else:
        print("Tipo: Producto genérico")
        print(f"{producto.nombre} - Precio final: ${precio_final}")