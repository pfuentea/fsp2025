#by Karina
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def calcular_precio_final(self):
        return self.precio


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
        return self.precio * (1 - self.descuento)


class Suscripcion(Producto):
    def __init__(self, nombre, precio, porcentaje_mensual):
        super().__init__(nombre, precio)
        self.porcentaje_mensual = porcentaje_mensual

    def calcular_precio_final(self):
        return self.precio * (1 + self.porcentaje_mensual)


productos = [
    ProductoFisico("Notebook", 850000, 15000),
    ProductoDigital("Curso Python Online", 120000, 0.15),
    Suscripcion("Streaming Premium", 12990, 0.05),
    ProductoFisico("Mouse Inalámbrico", 19990, 5000),
    ProductoDigital("Ebook Programación", 15990, 0.10)
]

fisicos = []
digitales = []
suscripciones = []

for p in productos:
    if isinstance(p, ProductoDigital):
        precio = p.calcular_precio_final() * 0.95
        digitales.append((p.nombre, precio))
    elif isinstance(p, Suscripcion):
        precio = p.calcular_precio_final()
        suscripciones.append((p.nombre, precio))
    else:
        precio = p.calcular_precio_final()
        fisicos.append((p.nombre, precio))

print("PRODUCTOS FÍSICOS")
for nombre, precio in fisicos:
    print(f"{nombre}: ${precio:,.0f}")

print("\nPRODUCTOS DIGITALES")
for nombre, precio in digitales:
    print(f"{nombre}: ${precio:,.0f}")

print("\nSUSCRIPCIONES")
for nombre, precio in suscripciones:
    print(f"{nombre}: ${precio:,.0f}")