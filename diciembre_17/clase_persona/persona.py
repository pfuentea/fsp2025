# el nombre de la clase se escribe en Pascal case=la primera letra de cada palabra en mayúscula
class Persona:
    # __init__ es lo que llamaremos el CONSTRUCTOR
    # se ejecuta de manera automatica, una sola 
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    
    def presentarse(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

    def cumplir_anios(self):
        self.edad+=1

persona1=Persona("José(1)",33)
persona2=Persona("José(2)",33)

persona1.presentarse()
persona2.presentarse()

persona1.cumplir_anios()
persona1.presentarse()
#Hola, mi nombre es José(1) y tengo 34 años.

persona3=persona1
persona3.presentarse()
#Hola, mi nombre es José(1) y tengo 34 años.
persona1.cumplir_anios()
persona3.presentarse()
#Hola, mi nombre es José(1) y tengo 35 años.
