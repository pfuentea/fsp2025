#By Gloria

class Mascota:
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre
        self.edad = edad
        self.tipo = tipo

    def presentarse(self):
        print(f"Soy {self.nombre}, un/a {self.tipo} de {self.edad} años.")

    def es_joven(self):
        return self.edad < 5


mascota1 = Mascota("Firulais", 3, "perro")
mascota2 = Mascota("Michi", 7, "gato")
mascota3 = Mascota("Lola", 1, "conejo")

lista_mascotas = [mascota1, mascota2, mascota3]

mascotas_jovenes = []

for mascota in lista_mascotas:
    mascota.presentarse()
    print(mascota.es_joven())

    if mascota.es_joven():
        mascotas_jovenes.append(mascota)

print("Mascotas jóvenes:")

for mascota in mascotas_jovenes:
    mascota.presentarse()