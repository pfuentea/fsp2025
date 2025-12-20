#By Gloria
class DispositivoInteligente:
    def __init__(self, modelo):
        self.modelo = modelo          # atributo público
        self.__encendido = False      # atributo privado
        self.__conectado = False      # atributo privado

    def encender(self):
        self.__encendido = True

    def conectar(self):
        if self.__encendido:
            self.__conectado = True

    def estado(self):
        if self.__encendido and self.__conectado:
            return "Conectado"
        return "Desconectado"


# Prueba con dos dispositivos
disp1 = DispositivoInteligente("Smart TV")
disp2 = DispositivoInteligente("Router")

disp1.encender()
disp1.conectar()

disp2.encender()

print(disp1.modelo, disp1.estado())
print(disp2.modelo, disp2.estado())