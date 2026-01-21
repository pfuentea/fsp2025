from abc import ABC, abstractmethod 

class Cliente(ABC):
    def __init__(self,nombre,direccion,email,telefono,rut):
        self.__nombre=nombre
        self.__direccion=direccion
        self.__email=email
        self.__telefono=telefono
        self.__rut=rut

    # esto deben hacerlo para encapsular el resto de los atributos
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,valor):
        self.__nombre=valor

    @abstractmethod
    def mostrar_info():
        pass

    def __str__(self):
        return f"Nombre:{self.__nombre}, rut:{self.__rut}"
    


