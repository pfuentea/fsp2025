class Empleado:
    def __init__(self,nombre,dni):
        self.nombre=nombre
        self.dni=dni
    def trabajar(self):
        print("Empleado general trabajando")

class Desarrollador(Empleado):
    def trabajar(self):
        print("Codificando...")

    def escribir_codigo(self):
        print(f"{self.nombre} está escribiendo código")

class Disenador(Empleado):
    def trabajar(self):
        print("Diseñando interfaces...")
    def crear_mockups(self):
        print(f"{self.nombre} está creando mockups")

class Gerente(Empleado):
    def trabajar(self):
        print("Planificando estrategias...")
    def supervisar_equipo(self):
        print(f"{self.nombre} está supervisando el equipo")

personal=[Desarrollador("Karina","19876937-0"),Disenador("Constanza","20543716-4"),Gerente("Juan Manuel","18765354-k")]

for e in personal:
    e.trabajar()
    if isinstance(e,Desarrollador):
        e.escribir_codigo()
    if isinstance(e,Disenador):
        e.crear_mockups()
    if isinstance(e,Gerente):
        e.supervisar_equipo()