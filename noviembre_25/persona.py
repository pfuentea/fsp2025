# Los objetos van a poseer dos miembros
# 1.-los atributos
# 2.-los métodos == ACCIONES QUE PUEDE REALIZAR

class Persona:

    banco="BancoEstafo" #atributos de clase
    
    #método CONSTRUCTOR
    def __init__(self,nombre,edad): 
        self.nombre=nombre
        if(edad >=0):
            self.edad=edad
        else:
            self.edad=0

    #los métodos que son de INSTANCIA deben tener como primer parametro "self"    
    def saludar(self):
        print(f"Hola mi nombre es {self.nombre} y mi edad es {self.edad}")
    
    # los otros tipos de método tendran un modificador al inicio
    
    @classmethod
    def cambio_banco(cls):
        cls.banco="BANCHOCHICLE"

# primero vamos a INSTANCIAR LA CLASE == crear un objeto de la clase
numero = 8
persona1 = Persona("Pedro", 32)
persona2 = Persona("Marcelo",-23)
persona1.saludar()

persona2.saludar()

#print(f"Nombre:{persona1.nombre}")

