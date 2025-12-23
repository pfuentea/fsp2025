class Persona:
    def __init__(self,nombre):
        self.nombre=nombre

    def saludar(self,*args):
        #print(f"tipo:{type(args)}")
        if len(args) ==0:
            print(f"Hola! mi nombre es {self.nombre}")
        elif len(args) == 1:
            print(f"Hola!{args[0]}, mi nombre es {self.nombre}")
        elif len(args) == 2:
            print(f"Hola!{args[0]} de {args[1]}, mi nombre es {self.nombre}")
        else:
            print("Más argumentos de los requeridos")

p1=Persona("Marcela")

p1.saludar()
p1.saludar("José")
p1.saludar("Rocio","Copiapó")
p1.saludar("Rocio","Copiapó",34)

print(p1)
