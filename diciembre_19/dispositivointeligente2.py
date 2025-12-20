class DispositivoInteligente:
    def __init__(self,modelo):
        self.modelo=modelo
        self.__encendido=False
        self.__conectado=False

    def encender(self):
        self.__encendido=True

    def conectar(self):
        if self.__encendido:   #Porque no va el True
            self.__conectado= True
        else:
            self.__conectado=False

    def estado (self):
        if self.__conectado:
            return 'Conectado'
        else:
            return 'Desconectado'

dispositivo1= DispositivoInteligente('Samsung XX')
dispositivo2= DispositivoInteligente('Iphone XX')
dispositivo3= DispositivoInteligente('Motorola XX')
'''
class DispositivoInteligente:
    def __init__(self, modelo):
        self.modelo = modelo          
        self.__encendido = False     
        self.__conectado = False      

    def encender(self):
        self.__encendido = True
       

    def conectar(self):
        
        if self.__encendido:
            self.__conectado = True
        else:
           
            self.__conectado = False

    def estado(self):
        return "Conectado" if self.__conectado else "Desconectado"



d1 = DispositivoInteligente("Smart TV Samsung")
d2 = DispositivoInteligente("iPhone 13")
'''
print(dispositivo1.modelo, "-", dispositivo1.estado())  
print(dispositivo2.modelo, "-", dispositivo2.estado())  
print(dispositivo3.modelo,"-",dispositivo3.estado())


dispositivo1.conectar()
print(dispositivo1.modelo, "-", dispositivo1.estado())  


dispositivo1.encender()
dispositivo1.conectar()
print(dispositivo1.modelo, "-", dispositivo1.estado()) 


dispositivo2.encender()
print(dispositivo2.modelo, "-", dispositivo2.estado())  # Desconectado

dispositivo3.conectar()
print(dispositivo1.modelo, "-", dispositivo1.estado())  


dispositivo3.encender()
dispositivo3.conectar()
print(dispositivo1.modelo, "-", dispositivo1.estado())