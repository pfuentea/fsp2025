from .cliente import Cliente

class ClienteRegular(Cliente):

    def mostrar_info(self):
        print(f"Nombre:{self.__nombre}")