class Auto:
    def __init__(self,marca,color):
        self.marca=marca
        self.color=color
        self.velocidad=0
        
    def acelerar(self):
        print("Aceleramos el auto")
        self.velocidad+=10

    def frenar(self):
        if self.velocidad > 0:
            print("Frenamos el auto")
            self.velocidad-=5

    def mostrar_estado(self):
        print(f"El auto de marca {self.marca} y color {self.color} va a {self.velocidad} km/h.")

cacharro=Auto("Renault","Amarillo")
cacharro2=Auto("Renault","Azul")

cacharro.mostrar_estado()
cacharro2.mostrar_estado()
cacharro.acelerar()
cacharro2.acelerar()
cacharro.mostrar_estado()
cacharro2.mostrar_estado()
cacharro.acelerar()
cacharro2.frenar()
cacharro.mostrar_estado()
cacharro2.mostrar_estado()
cacharro.frenar()
cacharro2.frenar()
cacharro.mostrar_estado()
cacharro2.mostrar_estado()