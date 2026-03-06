from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    # libros

    def __str__(self):
        return self.nombre
    
class Libro(models.Model):
    autor=models.ForeignKey(Autor,related_name='libros',on_delete=models.CASCADE)
    titulo=models.CharField(max_length=100)
    precio=models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.titulo