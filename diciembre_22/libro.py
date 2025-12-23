class Libro:
    def __init__(self,titulo,autor,anio):
        self.titulo=titulo
        self.autor=autor
        self.anio=anio

    def mostrar_libro(self):
        print(f"{self.titulo} - {self.autor} ({self.anio})")

libro1=Libro("Don Quijote de la Mancha","Miguel de Cervantes",1605)
libro2=Libro("El Alquimista","Paulo Cohelo",1988)
libro3=Libro("Cien años de soledad","Gabriel Garcia Marquez",1967)
libro4=Libro("Rayuela","Julio Cortazar",1963)
libro5=Libro("Platero y yo", "Juan Ramón Jiménez", 1914)
libro6=Libro("El sentido de lo humano", "humberto maturana", 2020)

libros=[libro1,libro2,libro3,libro4,libro5,libro6]
for l in libros:
    l.mostrar_libro()
