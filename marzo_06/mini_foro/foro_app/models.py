from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    autor=models.ForeignKey(User,on_delete=models.CASCADE)
    titulo= models.CharField(max_length=255,blank=True,null=True)
    contenido=models.TextField()
    fecha_creacion=models.DateTimeField(auto_now_add=True)
    padre=models.ForeignKey('self',on_delete=models.CASCADE,
                            null=True, blank=True,
                            related_name='hijos')

    def __str__(self):
        return self.titulo