class Animal:
    def __init__(self,nombre):
        self.nombre=nombre

    def emitir_sonido(self):
        print("Sonido Genérico")

class Perro(Animal):

    def emitir_sonido(self):
        print("GUAU!!")

    def comer(self):
        print("el perro come")

class Gato(Animal):

    def emitir_sonido(self):
        print("MIAU!!")

cachupin=Perro("Cachupin")
leon=Gato("León")

print("el perro ladra")
cachupin.emitir_sonido()
cachupin.comer()
print("el gato maulla")
leon.emitir_sonido()

