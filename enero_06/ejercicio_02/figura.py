class Figura:
    def dibujar(self):
        pass

class Rectangulo(Figura):
    def dibujar(self):
        print("Dibujo un rectangulo")

class Circulo(Figura):
    def dibujar(self):
        print("Dibujo un circulo")

class Triangulo(Figura):
    def dibujar(self):
        print("Dibujo un triangulo")

class Rombo(Figura):
    pass

print("INIT:Creacion de figuras")
lista_figura=[Circulo(),Rectangulo(),Triangulo(),Rombo()]
print("FIN :Creacion de figuras")

opcion=input("Presione una tecla")

for f in lista_figura:
    f.dibujar()





