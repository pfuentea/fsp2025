#By Sandra
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def calcular_precio_final(self):
        return self.precio

class ProductoFisico(Producto):
    costo_envio = 13500 

    def calcular_precio_final(self):
        return self.precio + self.costo_envio

class ProductoDigital(Producto):
    descuento = 0.10  

    def calcular_precio_final(self):
        return self.precio * (1 - self.descuento)

class Suscripcion(Producto):
    recargo_mensual = 0.05 

    def calcular_precio_final(self):
        return self.precio * (1 + self.recargo_mensual)

productos = [
    ProductoFisico("Pantalla dibujo gráfico", 400000),
    ProductoDigital("dibujo gráfico personalizado", 40000),
    Suscripcion("Curso completo", 18000)
    ]

for p in productos:
    print(p.nombre, "precio final:", p.calcular_precio_final())