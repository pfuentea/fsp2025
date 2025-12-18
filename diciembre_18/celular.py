#BY Hernan
class Celular:
    def __init__(self,marca,modelo,almacenamiento):
        self.marca=marca
        self.modelo=modelo
        self.almacenamiento=almacenamiento
        
    def encender(self):
        print(f"Encendido {self.marca} y {self.modelo}")

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Almacenamiento: {self.almacenamiento}GB")

celu1=Celular("Motorola","Moto-G",128)
celu2=Celular("Apple","Iphone-14",256)
celu3=Celular("Samsung","Galaxy-S23",512)

celu1.mostrar_info()
celu2.mostrar_info()
celu3.mostrar_info()

celu1.encender()
celu2.encender()
celu3.encender()