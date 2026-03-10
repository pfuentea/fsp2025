from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,related_name="profile",on_delete=models.CASCADE)
    telefono=models.CharField(max_length=20, blank=True,null=True)
    fecha_nacimiento=models.DateField(blank=True,null=True)
    bio=models.TextField(blank=True,null=True)
    foto=models.ImageField(upload_to='profiles/',blank=True,null=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"