from .jugador import Jugador
from .juegodobles import JuegoDobles

def jugar_dobles():
    print("-----JUEGO DE DOBLES-------")
    nombre=input("Ingrese el nombre del jugador:")
    if not nombre:
        nombre="Jugador 1"
    jugador=Jugador(nombre)
    juego=JuegoDobles(jugador)
    juego.jugar()

def juego2():
    pass

def main():
    # un while para jugar varias veces el mismo juego o elegir otro
    jugar_dobles()

if __name__=="__main__":
    main()