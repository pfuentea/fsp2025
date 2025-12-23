class Cuenta:
    def __init__(self,nombre):
        self.__nombre=nombre

    #GETTER se crean con el decorador property
    @property
    def nombre(self):
        return self.__nombre

    #SETTER se crean con el decorador atributo.setter
    @nombre.setter
    def nombre(self, valor):
        if not valor:
            raise ValueError("Nombre no puede estar vacío")
        self.__nombre=valor
    
    # El DELETER sirve para ELIMINAR UN ATRIBUTO
    # TRATEN DE NO USARLO NUNCA!!!
    @nombre.deleter
    def nombre(self):
        del self.__nombre

c1=Cuenta("Jaime Muñoz")

print(f"Nombre de la cuenta:{c1.nombre}")
c1.nombre="Pedro Pascual"
print(f"Nombre de la cuenta:{c1.nombre}")

