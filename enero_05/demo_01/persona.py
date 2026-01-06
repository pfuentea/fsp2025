class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        if edad >0:
            self.edad=edad
        else:
            self.edad=0

    def presentarse(self):
        print(f"Hola mi nombre es {self.nombre} y tengo {self.edad} años")



    
