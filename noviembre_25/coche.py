from datetime import datetime

class Coche:
    def __init__(self,p_marca,p_modelo,p_year,p_color):
        self.marca=p_marca
        self.modelo=p_modelo
        self.year=p_year
        self.color=p_color
    
    def detalles(self):
        print(f"Marca:{self.marca}, modelo:{self.modelo}, año:{self.year}, color:{self.color}")
    # este método especial nos permite usar el método print para ver los valores de los atributos del objeto  
    def __str__(self):
        return f"Marca:{self.marca}, modelo:{self.modelo}, año:{self.year}, color:{self.color}"


marca=input("Ingrese la Marca:")
color=input("Ingrese el color:")
modelo=input("Ingrese la modelo:")
year=int(input("Ingrese el año:"))
auto1=Coche(marca,modelo,year,color)

if (year >=2022):
    print("es un coche nuevo")
else:
    print("es un coche viejo")


while (True):
    print("Elija una opcion")
    print("a)modificar marca")
    print("b)modificar modelo")
    print("c)modificar año")
    print("d)modificar color")
    print("e)salir")
    opcion=input("Ingrese su selección: ")
    if opcion == "a":
        pass
        # instrucciones para modificar marca
    elif opcion == "b":
        pass
        # instrucciones para modificar modelo
    elif opcion == "c":
        pass
    # instrucciones para modificar año
    elif opcion == "d":
        pass
    # instrucciones para modificar color
    elif opcion == "e":
        break
    else:
        print("opcion no valida")
        continue

#auto1.detalles()

print(auto1)
