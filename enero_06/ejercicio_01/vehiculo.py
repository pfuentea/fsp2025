class Vehiculo:
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo

    def moverse(self):
        print("El vehículo se mueve")

class Auto(Vehiculo):
    

    def moverse(self):
        print("Conduciendo por la carretera")

class Bicicleta(Vehiculo):
    def moverse(self):
        print("Pedaleando")

class Motocicleta(Vehiculo):
    def __init__(self,marca,modelo,cilindrada):
        super().__init__(marca,modelo)
        self.cilindrada=cilindrada

veh1=Auto("Toyota","Yaris")
veh2=Bicicleta("Trek","Marlin 7")
veh3=Motocicleta("Honda", "Nx190",190)

flota=[veh1,veh2,veh3]
n_veh=0
n_auto=0
n_bici=0
n_moto=0
for v in flota:
    print(f"{v.marca}/{v.modelo}")
    v.moverse()
    if isinstance(v,Vehiculo):
        n_veh+=1
    if isinstance(v,Auto):
        n_auto+=1
    if isinstance(v,Bicicleta):
        n_bici+=1
    if isinstance(v,Motocicleta):
        n_moto+=1
        
print(f"Existen {n_veh} Vehiculos")
print(f"Existen {n_auto} Autos")
print(f"Existen {n_bici} Bicicletas")
print(f"Existen {n_moto} Motos")
