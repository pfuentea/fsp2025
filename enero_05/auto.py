class Motor:
    def encender(self):
        print("Motor encendido")

#en este caso la dependencia entre objetos es alta= ACOPLAMIENTO ALTO
class Auto:
    def __init__(self):
        self.motor=Motor()

    def arrancar(self):
        self.motor.encender()

#en este caso la dependencia entre objetos es baja= ACOPLAMIENTO BAJO
class Auto2:
    def __init__(self,motor):
        self.motor=motor

    def arrancar(self):
        self.motor.encender()