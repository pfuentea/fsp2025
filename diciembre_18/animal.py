class Animal:
    #1.- crear el constructor 
    def __init__(self,nombre):
        self.nombre=nombre

    def hablar(self):
        print(f"mi nombre es :{self.nombre}") 

def mostrar_animales(lista):
    for objeto in lista:
        if isinstance(objeto,Animal):
            objeto.hablar()
        else:
            print(f"el valor es: {objeto}")
    
mi_gato=Animal("Felix")
otro_gato=Animal("Garfield")
mi_gato.hablar()
print(isinstance(mi_gato,Animal)) # True
print(isinstance(mi_gato,int)) # False

lista_animales=[mi_gato,otro_gato,23,"Hola mundo"]

mostrar_animales(lista_animales)