class Producto:
    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio
    def calcular_precio_final(self):
        pass

class ProductoFisico(Producto):
    # se aplica costo de envio
    pass

class ProductoDigital(Producto):
    # se aplica descuento
    pass

class Suscripcion(Producto):
    # se agrega un porcentaje mensual
    pass