class Volador:
    def moverse(self):
        print("El pato vuela")
    def comer(self):
        print("el pato come semillas")

class Nadador:
    def moverse(self):
        print("El pato nada")

class Pato(Nadador,Volador):
    def moverse(self):
        Volador().moverse()
        Nadador().moverse()


donald=Pato()
donald.moverse()
donald.comer()
#help(donald)