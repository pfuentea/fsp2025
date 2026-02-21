from django.db import models

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    unidad = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nombre

class Receta(models.Model):
    nombre = models.CharField(max_length=150, unique=True)
    descripcion = models.TextField( blank=True)
    tiempo_minutos = models.IntegerField()

    ingredientes= models.ManyToManyField(Ingrediente,related_name='recetas',blank=True)

    def __str__(self):
        return self.nombre