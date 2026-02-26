from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    

class Libro(models.Model):
    titulo= models.CharField(max_length=100)
    descripcion=models.TextField(blank=True)
    autores = models.ManyToManyField(Autor,related_name='libros')
    creador = models.ForeignKey(User,on_delete=models.CASCADE,related_name='libros')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo