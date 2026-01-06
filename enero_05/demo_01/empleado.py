from persona import Persona

# la clase derivada dice entre parentesis desde donde hereda
class Empleado(Persona):
    def __init__(self,nombre,edad,cargo):
        super().__init__(nombre,edad)
        self.cargo=cargo
    
    def presentarse(self):
        print(f"Hola mi nombre es {self.nombre} y tengo {self.edad} años y mi cargo es {self.cargo}")
    
    def trabajar(self):
        print(f"{self.nombre} está trabajando como {self.cargo}")