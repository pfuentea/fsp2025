class Animal:
    pass

class Perro(Animal):
    pass

fido = Perro()
# 4: Juan, 
# 3: Hernan, Karina, Gloria, Camila,
# 2: Hector, Sandra, Juan Manuel, Jocelyne 
# 1: Yerko, Rafael 
# 0: 


if isinstance(fido,Perro) :
    print("fido es un perro")

if isinstance(fido,Animal) :
    print("fido es un animal")

if type(fido) == Perro:
    print("fido es de tipo perro")

if type(fido) == Animal:
    print("fido es de tipo animal")