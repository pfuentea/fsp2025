class MedioPago:
    def pagar(self,monto):
        return monto
    
class TarjetaCredito(MedioPago):
    def __init__(self,interes=0.05):
        self.interes=interes
        self.mantencion=10000
    def pagar(self,monto):
        return monto*(1+self.interes)

class Efectivo(MedioPago):
    def pagar(self,monto):
        return monto

class Tranferencia(MedioPago):
    def __init__(self,descuento=0.01):
        self.descuento=descuento

    def pagar(self,monto):
        return monto*(1-self.descuento)
    
medios=[
    ("MasterPlop",TarjetaCredito(0.08)),
    ("Efectivo",Efectivo()),
    ("Transferencia",Tranferencia(0.05))
]

monto_a_pagar=50000

for nombre,medio in medios:
    total=medio.pagar(monto_a_pagar)
    print(f"{nombre}: monto base:{monto_a_pagar}, total final={total}")