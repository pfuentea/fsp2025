# 1. Definir la clase Persona con atributos nombre y edad
class Persona:
    def __init__(self,nombre,edad=0): # 2. Inicializar la edad en 0 o en un valor recibido
        self.nombre=nombre
        self.edad=edad
'''
ADVERTENCIA: NO HAGAN ESTO EN CASA NIÑOS Y NIÑAS!
class Usuario:
    def put_nombre(self,nombre):
        self.nombre=nombre
    def saludar(self):
        print(f"hola me llamo {self.nombre}")

juan=Usuario()
#juan.put_nombre("Juan")
juan.saludar()
'''



    