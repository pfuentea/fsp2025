from django.db import models

class Autor(models.Model):
    nombre = models.CharField(max_length=120)
    nacionalidad = models.CharField(max_length=80, blank=True, null=True)

    def __str__(self):
        return self.nombre


class Libro(models.Model):
    titulo = models.CharField(max_length=150)
    anio = models.PositiveIntegerField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name="libros")

    def __str__(self):
        return f"{self.titulo} ({self.anio})"