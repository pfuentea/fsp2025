class CuentaBancaria:
    def __init__(self,titular,saldo=0):
        self.titular=titular
        self.saldo = saldo

    def depositar(self,monto):
        if monto>0:
            self.saldo+=monto
            print(f"Deposito exitoso:${monto}")
        return self

    def retirar(self,monto):
        if monto <self.saldo:
            self.saldo-=monto
            print(f"Retiro exitoso: ${monto}")
        return self

    def mostrar_saldo(self):
        print(f"El saldo de la cuenta de {self.titular} es:{self.saldo}")
        return self

c1=CuentaBancaria("Gloria",10000)
c1.mostrar_saldo().depositar(5000).mostrar_saldo().retirar(2000).mostrar_saldo()
