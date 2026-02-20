from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=120)
    email=models.EmailField(unique=True)
    # cursos es un campo que utilizaremos para ver los cursos de los estudiantes

    def __str__(self):
        return self.nombre
    
class Curso(models.Model):
    nombre= models.CharField(max_length=120)
    codigo= models.CharField(max_length=20,unique=True)
    estudiantes = models.ManyToManyField(Estudiante,related_name='cursos',blank=True)

    def __str__(self):
        return f"{self.nombre}({self.codigo})"

