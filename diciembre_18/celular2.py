# By Sandra
class Celular:
    #1. Crear el constructor.
    def __init__ (self,marca,modelo,almacenamiento):
        self.marca=marca
        self.modelo=modelo
        self.almacenamiento=almacenamiento
        self.esta_encendido=False

    def encender(self):
        self.esta_encendido=True
        print(f'Encendiendo el {self.modelo} de {self.marca}')

    def mostrar_info (self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        if self.esta_encendido:
            print("Almacenamiento:", self.almacenamiento)

##
celular1 = Celular("Samsung", "Galaxy S23", "256GB")
celular2 = Celular("Apple", "iPhone 14", "128GB")
celular3 = Celular("Motorola", "Edge 40", "256GB")

# Guardar en lista
celulares = [celular1, celular2, celular3]

# Recorrer la lista con un for y usar los métodos

celular1.mostrar_info()

for celular in celulares:
    celular.encender()
    celular.mostrar_info()