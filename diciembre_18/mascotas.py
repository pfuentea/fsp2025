#By Constanza

class Mascota ():
    def __init__(self, nombre, edad, tipo):
        self.nombre= nombre
        self.edad=edad
        self.tipo= tipo
        
    def presentarse (self):
        print(f"Soy {self.nombre}, un/a {self.tipo} de {self.edad} años")
    def es_joven(self):
        resultado = self.edad <5
        if resultado:
            print(f"{self.nombre} es joven (tiene menos de 5 años).")
        else:
            print(f"{self.nombre} ya no es tan joven (tiene 5 años o más).")
            
        return resultado
       
    
mascota1 = Mascota("Zara", 3, "gata")
mascota1.presentarse()
mascota1.es_joven ()

print("-" * 30)

mascota2 = Mascota("Simba", 7, "perro")
mascota2.presentarse()
mascota2.es_joven ()


print("-" * 30)

mascota3 =Mascota("Nala", 4 ,"perro")
mascota3.presentarse()
mascota3.es_joven()