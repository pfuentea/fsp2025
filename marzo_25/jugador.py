from .dado import Dado

class Jugador:
    def __init__(self,nombre):
        self.nombre = nombre
        self.dados=[]

    def lanzar_dados(self,cantidad=1):
        self.dados= [Dado() for _ in range(cantidad)]
        return [dado.lanzar()  for dado in self.dados]
    
    def obtener_nombre(self):
        return self.nombre
    
