class Docente:
    def __init__(self,nombre,especialidad):
        self.nombre=nombre
        self.especialidad=especialidad
    
    def __str__(self):
        return f"Nombre:{self.nombre},{self.especialidad}"

class Curso:
    def __init__(self,nombre,codigo, docente):
        self.nombre=nombre
        self.codigo=codigo
        self.docente=docente # acá se aplica la COMPOSICIÓN

    def mostrar_info(self):
        print(f"Curso:{self.nombre} ({self.codigo})")
        print(self.docente)

class Alumno:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        self.cursos=[] # aplicamos la AGREGACIÓN

    def inscribir(self,curso):
        # es que no se pueda inscribir el mismo curso 2 veces
        self.cursos.append(curso)

    def mostrar_cursos(self):
        if len(self.cursos)==0:
            print(f"El alumno {self.nombre} aún no tiene cursos")
        else:
            print(f"Cursos del alumno {self.nombre}:")
            for c in self.cursos:
                c.mostrar_info()

docente1=Docente("Juan Pérez","Bases de datos")
docente2=Docente("Rubén Muñoz","Programación")

curso_python=Curso("FullStack Python","fsp2025",docente1)
curso_java=Curso("Java","jv2025",docente2)

alumno1=Alumno("Pedro Gajardo",33)
alumno2=Alumno("Anita Gonzalez",26)

alumno1.inscribir(curso_python)
alumno1.inscribir(curso_java)

alumno1.mostrar_cursos()
alumno2.mostrar_cursos()