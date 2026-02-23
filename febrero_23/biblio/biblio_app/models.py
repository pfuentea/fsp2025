from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor,related_name='libros',on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo