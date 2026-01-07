class Usuario:
    def __init__(self,nombre):
        self.nombre=nombre
    def saludar(self):
        print(f"Hola! soy {self.nombre} y estoy saludando!")

class Administrador(Usuario):
    def acceder_panel(self):
        print(f"{self.nombre} accediendo al panel...")

class Cliente(Usuario):
    def realizar_compra(self):
        print(f"{self.nombre} esta realizando la compra")

usuarios=[Cliente("Pedro"),Administrador("Ana"),Usuario("Laura")]

for u in usuarios:
    if isinstance(u,Administrador):
        u.acceder_panel()    
    if isinstance(u,Cliente):
        u.realizar_compra()
    if isinstance(u,Usuario):
        u.saludar()

# cuantos print van a aparecer?
# 3: Hernan, Karina, Gloria, Constanza, Juan Manuel, Jocelyne
# 2: Camila 
# 1: Osvaldo
