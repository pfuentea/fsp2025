class Procesador:
    def __init__(self,marca,velocidad):
        self.marca=marca
        self.velocidad=velocidad
    def mostrar_info(self):
        print(f"Marca:{self.marca},velocidad:{self.velocidad}")

class MemoriaRAM:
    def __init__(self,capacidad_gb,tipo):
        self.capacidad=capacidad_gb
        self.tipo=tipo
    def mostrar_info(self):
        print(f"Memoria: capacidad:{self.capacidad},tipo:{self.tipo}")

class DiscoDuro:
    def __init__(self,capacidad_gb,tipo):
        self.capacidad=capacidad_gb
        self.tipo=tipo
    def mostrar_info(self):
        print(f"Memoria: capacidad:{self.capacidad},tipo:{self.tipo}")

class Computadora:
    def __init__(self,marca,procesador,memoria,disco):
        self.marca=marca
        self.procedor=procesador
        self.memoria=memoria
        self.disco=disco

    def mostrar_info(self):
        print(f"Marca:{self.marca}")
        self.procedor.mostrar_info()
        self.memoria.mostrar_info()
        self.disco.mostrar_info()

cpu=Procesador("Intel","2GHz")
mem=MemoriaRAM("16G","SSD4")
hd=DiscoDuro("1 Tera","SSD")
notebook=Computadora("Dell",cpu,mem,hd)

notebook.mostrar_info()