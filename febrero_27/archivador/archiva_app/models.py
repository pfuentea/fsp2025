from django.db import models

# Create your models here.

class Archivo(models.Model):
    nombre = models.CharField(max_length=120)
    ruta= models.FileField(upload_to='archivo/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre}"
    
