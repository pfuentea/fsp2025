class Libro:
    def __init__(self,titulo,autor,stock,precio):
        self.titulo=titulo
        self.autor=autor
        self.stock=stock
        self.set_precio(precio)

    #GETTER
    def get_precio(self):
        return self.__precio
    
    #SETTER
    def set_precio(self,nuevo_precio):
        if nuevo_precio >0:
            self.__precio=nuevo_precio

    def vender(self,unidades):
        if unidades>0:
            if  self.stock>=unidades:
                self.stock-=unidades
            else:
                print("No existe suficiente stock")
        else:
            print("Las unidades deben ser positivas")
    def mostrar_info(self):
        print(f"Titulo:{self.titulo}, autor:{self.autor},stock:{self.stock},precio:{self.get_precio()}")

libro1=Libro("El señor de los anillos","Tolkien",5,10000)
libro1.mostrar_info()
print("*"*30)
libro1.vender(2)
libro1.mostrar_info()
print("*"*30)
libro1.set_precio(12000)
libro1.mostrar_info()