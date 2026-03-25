import random

class Dado:
    def __init__(self,caras=6):
        self.caras=caras
        self.__valor=None

    def lanzar(self):
        self.__valor=random.randint(1,self.caras)
        return self.__valor

    def obtener_valor(self):
        return self.__valor
