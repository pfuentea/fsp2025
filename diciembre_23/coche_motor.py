class Motor:
    def __init__(self,tipo,potencia):
        self.tipo=tipo
        self.potencia=potencia

    def encender(self):
        print(f"Motor encendido:{self.tipo},HP:{self.potencia}")

class Coche:
    def __init__(self,marca,modelo,motor):
        self.marca=marca
        self.modelo=modelo
        self.motor=motor

    def arrancar(self):
        self.motor.encender() 

m1=Motor("Eléctrico",800)

auto=Coche("Suzuki","Ñuñuki",m1)

auto.arrancar()
