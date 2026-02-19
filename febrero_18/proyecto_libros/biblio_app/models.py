from django.db import models

# Create your models here.

class Autor(models.Model):
    nombre=models.CharField(max_length=120)
    nacionalidad = models.CharField(max_length=100,blank=True)
    # libros -> se usa para relacionar con los libros del autor

    def __str__(self):
        return f"{self.nombre}"


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    anio_publicacion=models.IntegerField()
    disponible = models.BooleanField(default=True)    

    autor = models.ForeignKey(Autor,related_name='libros',on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo}/{self.autor.nombre}"
    


