class Producto:
    def __init__(self,nombre,precio):
        self.nombre=nombre
        #self.__precio=precio
        self.set_precio(precio)

    #GETTER
    def get_precio(self):
        return self.__precio
    
    #SETTER
    def set_precio(self,nuevo_precio):
        if nuevo_precio >0:
            self.__precio=nuevo_precio
        else:
            print("Error:el precio debe ser mayor a cero!")

#Crear un producto con precio válido
prod1=Producto("Árbol de Pascua",40000)
#Mostrar el precio usando el getter
print(f"El precio del producto es:{prod1.get_precio()}")
#Intentar cambiar el precio a un valor negativo (debe mostrar un error)
prod1.set_precio(-10000)
#Modificar correctamente el precio y verificar el nuevo valor
prod1.set_precio(30000)
print(f"El precio del producto es:{prod1.get_precio()}")