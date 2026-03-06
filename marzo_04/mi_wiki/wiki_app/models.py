from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.

class Categoria(models.Model):
    nombre=models.CharField(max_length=100,unique=True)
    slug=models.SlugField(max_length=140,unique=True,blank=True)

    def save(self,*args,**kwargs):
        if not self.slug:
            base=slugify(self.nombre)
            slug=base
            i=1
            while Categoria.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                i+=1
                slug=f"{base}-{i}"
            self.slug=slug
        super().save(*args,**kwargs)

    def __str__(self):
        return self.nombre
    
class Articulo(models.Model):
    titulo = models.CharField(max_length=140,unique=True)
    slug = models.SlugField(max_length=170,unique=True,blank=True)
    contenido=models.TextField()
    categoria=models.ForeignKey(Categoria,related_name='articulos',on_delete=models.PROTECT)
    autor=models.ForeignKey(User,related_name='articulos',on_delete=models.CASCADE)
    publicado=models.BooleanField(default=False)
    creado_en=models.DateField(auto_now_add=True)
    modificado_en=models.DateField(auto_now=True)

    def save(self,*args,**kwargs):
        if not self.slug:
            base=slugify(self.titulo)
            slug=base
            i=1
            while Categoria.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                i+=1
                slug=f"{base}-{i}"
            self.slug=slug
        super().save(*args,**kwargs)

    def __str__(self):
        return self.titulo
    
    