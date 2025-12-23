class CuentaCorreo:
    def __init__(self,usuario,dominio,password):
        self.usuario=usuario
        self._dominio=dominio
        self.__password=password

    def mostrar_correo(self):
        print(f"Email:{self.usuario}@{self._dominio}:{self.__password}")
    
    

email1=CuentaCorreo('jperez','gmail.com','1234Password-Segura.')
# Si queremos ver un atributo privado lo podemos revisar desde dentro de la clase e informarla hacia fuera
#print(f"Email:{email1.usuario}@{email1._dominio}:{email1.__password}")

email1.mostrar_correo()