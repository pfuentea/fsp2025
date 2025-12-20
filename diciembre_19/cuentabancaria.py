class CuentaBancaria:
    def __init__(self,titular):
        self.titular=titular
        self.__saldo=0

    def depositar(self,monto):
        if monto>0:
            self.__saldo += monto
            print("Deposito correcto")
    
    def retirar(self,monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
            print("Retiro correcto")
        else:
            print("No hay suficiente saldo")

    def ver_saldo(self):
        return self.__saldo
    
cuenta_24500_03=CuentaBancaria("Teleton")
print(f"Saldo:{cuenta_24500_03.ver_saldo()}")
cuenta_24500_03.depositar(25000)
print(f"Saldo:{cuenta_24500_03.ver_saldo()}")
cuenta_24500_03.retirar(30000)
cuenta_24500_03.retirar(5000)
print(f"Saldo:{cuenta_24500_03.ver_saldo()}")
cuenta_24500_03.__saldo=10000000
print(f"Saldo:{cuenta_24500_03.ver_saldo()}")