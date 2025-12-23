class Empleado:
    aumento_general=1.05

    def __init__(self,nombre,salario):
        self.nombre=nombre
        self.salario=salario
    #Método de CLASE
    @classmethod
    def set_aumento(cls,nuevo_aumento):
        cls.aumento_general=nuevo_aumento
    #Método estático
    @staticmethod
    def sobre_el_minimo(sueldo):
        return sueldo > 500000
    def mostrar_empleado(self):
        print(f"Nombre:{self.nombre}, sueldo:{self.salario}, aumento : {self.aumento_general}").
    
if Empleado.sobre_el_minimo(501000):
    print("Sueldo sobre el mínimo")
else:
    print("Sueldo bajo el mínimo")

#Crear varios empleados con salarios distintos
empleado1=Empleado("Hernan Garrido",3000000)
empleado2=Empleado("Yuri Leal",700000)
empleado3=Empleado("Yerko Arancibio",450000)

empleados=[empleado1,empleado2,empleado3]
for e in empleados:
    e.mostrar_empleado()
print("Aplicamos el aumento")
Empleado.set_aumento(1.2)

empleado4=Empleado("Hector",1000000) 
# el aumento queda aplicado a las instancias ceradas antes de el nuevo monto y a las que vengan después también
empleados.append(empleado4)
for e in empleados:
    e.mostrar_empleado()

for e in empleados:
    e.mostrar_empleado()
    sueldo_target=e.salario

    if Empleado.sobre_el_minimo(sueldo_target):
        print("Sueldo sobre el mínimo")
    else:
        print("Sueldo bajo el mínimo")



