class Automovil:
    def __init__(self):
        self.encendido=False
        self.combustible=10
        self.velocidad=0

    def encender(self):
        if self.combustible >0:
            self.encendido=True
            print("El automovil ha sido encendido")

    def acelerar(self):
        if self.encendido:
            if self.combustible>0:
                self.combustible -= 1
                self.velocidad += 10
                print("Aceleración exitosa!")
            else:
                self.encendido=False
                self.velocidad=0
                print("No tenemos combustible para acelerar.")
        else:
            print("No podemos acelerar un auto apagado")

auto=Automovil()
auto.encender()

for intento in range(12):
    auto.acelerar()
            