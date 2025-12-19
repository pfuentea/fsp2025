#By Karina
# Definir la clase Mascota
class Mascota:  
    def __init__(self, nombre, edad, tipo):
        self.nombre = nombre    # Nombre de la mascota
        self.edad = edad        # Edad de la mascota (en años)
        self.tipo = tipo        # Tipo de mascota (perro, gato, etc.)

    def presentarse(self):
        print(f"Soy {self.nombre}, un/a {self.tipo} de {self.edad} años.")
  
    def es_joven(self):
        return self.edad < 5 #True
    
mascota1 = Mascota("Luna", 3, "perro")
mascota2 = Mascota("Michi", 7, "gato")
mascota3 = Mascota("Rocky", 2, "perro")

# Guarda las mascotas en una lista
lista_mascotas = [mascota1, mascota2, mascota3]

# Recorre la lista de mascotas
for mascota in lista_mascotas:
    mascota.presentarse()  # Llamo al método presentarse

    # Verifica si la mascota es joven
    if mascota.es_joven():
        print("Es una mascota joven.")
    else:
        print("No es una mascota joven.")

    print("**=^.^=**")