class Personaje:

    total_personajes=0
    # el primer método que se ejecuta o que es llamado es el constructor
    def __init__(self,nombre):
       self.nombre = nombre
       self._ciudad="" # atributo "protegido" 
       Personaje.total_personajes +=1

    @classmethod
    def cantidad_total(cls):
        return f"La cantidad total de personajes es {cls.total_personajes}"
    
    @staticmethod
    def es_dano_valido(dano):
        if dano >0:
            return True
        return False


class Guerrero(Personaje):

    def __init__(self,nombre,vida):
        super().__init__(nombre)
        self.__vida = vida # atributo "privado"

    def atacar(self):
        return 20
    def recibir_dano(self,dano):
        # asegurarnos que tenga la vida suficiente 
        if dano >0:
            self.__vida -= (dano-5)
            print(f"{self.nombre} recibe {dano-5} puntos de daño")
        else:
            print("El daño debe ser mayor a cero.")
    
    def mostrar_estado(self):
        print(f"{self.nombre} tiene {self.__vida} de vida")

    
    
class Mago(Personaje):   
    def __init__(self,nombre,vida):
        super().__init__(nombre)
        self.__vida = vida # atributo "privado" 
    def atacar(self):
        return 15
    def recibir_dano(self,dano):
        # asegurarnos que tenga la vida suficiente 
        if dano >0:
            self.__vida -= (dano+2)
            print(f"{self.nombre} recibe {dano+2} puntos de daño")
        else:
            print("El daño debe ser mayor a cero.")
    def mostrar_estado(self):
        print(f"{self.nombre} tiene {self.__vida} de vida")


#p1=Personaje("Legolas",30)
#p1.mostrar_estado()
p2=Guerrero("Aragorn",40)
p3=Mago("Gandalf",50)
p4=Guerrero("Boromir",40)
p2.mostrar_estado()
p2.recibir_dano(20)
p2.mostrar_estado()

p3.mostrar_estado()
p3.recibir_dano(20)
p3.mostrar_estado()

print(f"{p2.nombre} ataca con {p2.atacar()} de daño")
print(f"{p3.nombre} ataca con {p3.atacar()} de daño")

print(Guerrero.cantidad_total())

if Personaje.es_dano_valido(-20):
    print("Es un daño válido!")
else:
    print("No es un daño válido!")
