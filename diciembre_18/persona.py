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

persona1=Persona("Pedro",21)
persona2=Persona("Lucia",25)

persona1.presentarse()
persona2.presentarse()

persona2.cumplir_anios()
persona1.presentarse()
persona2.presentarse()

persona2.edad=31
persona2.presentarse()

persona2.profesion="Enfermera"
persona2.presentarse()
print(f"Mi profesion es: {persona2.profesion}")


