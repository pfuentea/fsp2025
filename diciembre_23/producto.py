class Producto:
    # atributo de clase: todos las instancias tendrán este atributo con el mismo valor
    descuento=0.1

    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.set_precio(precio)
        
    #GETTER
    def get_precio(self):
        return self.__precio
    #SETTER
    def set_precio(self,nuevo_precio):
        if Producto.validar_precio(nuevo_precio):
            self.__precio=nuevo_precio
        else:
            print("El precio debe ser positivo")

    def aplicar_descuento(self):
        return self.__precio*(1-self.descuento)
    
    @staticmethod
    def validar_precio(precio):
        return precio>0
    
    @classmethod
    def set_descuento(cls,nuevo_descuento):
        if 1>=nuevo_descuento>=0:
            cls.descuento=nuevo_descuento
        else:
            print("Descuento debe estar entre 0 y 1")

    def mostrar_producto(self):
        print(f"Nombre:{self.nombre}, precio:{self.get_precio()},descuento:{self.descuento}")

producto1=Producto("Portaminas",1200)
producto2=Producto("Goma",890)

producto1.mostrar_producto()
producto2.mostrar_producto()

print(f"El {producto1.nombre} con descuento vale:{producto1.aplicar_descuento()}")
print(f"El {producto2.nombre} con descuento vale:{producto2.aplicar_descuento()}")
#para aplicar un método de CLASE se escribe CLASE.METODO()
Producto.set_descuento(0.25)

producto1.mostrar_producto()
print(f"El {producto1.nombre} con descuento vale:{producto1.aplicar_descuento()}")

producto1.set_precio(1500)
producto1.mostrar_producto()
producto2.mostrar_producto()