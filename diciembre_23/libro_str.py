class Libro:
    def __init__(self,titulo, autor,anio_publicacion):
        self.titulo=titulo
        self.autor=autor
        self.anio=anio_publicacion

    def __str__(self):
        return f"Título: {self.titulo} - Autor: {self.autor} - Año: {self.anio}"
    #al definir __str__ estoy cambiando algo interno del objeto??

    
l1=Libro("El Señor de los Anillos","Tolkien",1937)
l2=Libro("El Señor de los Anillos","Tolkien",1937)
print(dir(l1)) 



# <__main__.Libro object at 0x00000224A3716A50>
# Título: El Señor de los Anillos - Autor: Tolkien - Año: 1937
