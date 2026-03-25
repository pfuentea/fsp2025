class JuegoDobles:
    def __init__(self,jugador):
        self.jugador=jugador

    def jugar(self):
        resultados=self.jugador.lanzar_dados(2)
        print(f"{self.jugador.obtener_nombre()} lanzó:{resultados}")

        if resultados[0]==resultados[1]:
            print("Gano!")
        else:
            print("Perdió. Los resultados son distintos")
