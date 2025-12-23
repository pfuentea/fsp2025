class Test:
    def __init__(self):
        self.__privado=1 
        self._protegido=2
        self.publico=3

objeto=Test()
print(f"Publico:{objeto.publico}")
print(f"Protegido:{objeto._protegido}")
objeto._Test__privado=5
print(f"Privado:{objeto._Test__privado}")

print(dir(objeto))

# Name mangling: Cambio de nombre interno de un atributo


#ejemplo 2:
class Persona:
    def __init__(self,nombre):
        self.nombre=nombre
        self._edad=30
        self.__dni=12365098-3
p=Persona("Miguel")
print(f"{p.__dni}") # Intentar de acceder al valor de un atributo protegido nos entrega una excepción de tipo AttributeError: 'Persona' object has no attribute '__dni'


