from django.db import models

# Create your models here.

'''
SANDIWICH -> INGREDIENTES
PEDIDOS -> DETALL_PEDIDO  ==  VARIOS SANDWICH
'''

class Ingrediente(models.Model):
    class Category(models.TextChoices):
        PAN = "PAN","Pan"
        QUESO = "QUESO","Queso"
        SALSA = "SALSA","Salsa"
        VEGETAL = "VEGETAL","Vegetal"
        PROTEINA = "PROTEINA","Proteina"
        EXTRA = "EXTRA","Extra"

    nombre= models.CharField(max_length=50,unique=True)
    precio=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    categoria=models.CharField(max_length=50,choices=Category.choices)
    # sandwich_de_ingrediente
    # extras_en_pedidos

    def __str__(self):
        return f"{self.name}(+{self.precio})"
    
class Sandich(models.Model):
    nombre=models.CharField(max_length=50, unique=True)
    precio_base=models.DecimalField(max_digits=10,decimal_places=2)
    ingredientes=models.ManyToManyField(Ingrediente,blank=True,related_name="sandwich_de_ingrediente")

    def __str__(self):
        return f"{self.nombre} (${self.precio_base})"

class Pedido(models.Model):
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pedido #{self.id}"
    
class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido,related_name="items",on_delete=models.CASCADE)
    sandwich=models.ForeignKey(Sandich,on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(default=1)
    extras = models.ManyToManyField(Ingrediente,related_name="extras_en_pedidos")
    observacion = models.CharField(max_length=255,blank=True)

    def precio_unitario(self):
        total_extras= sum( i.precio for i in self.extras.all()   )
        return self.sandwich.precio_base + total_extras
    
    def total_por_fila(self):
        return self. precio_unitario() * self.cantidad
    
    def __str__(self):
        return f"{self.cantidad} x {self.sandwich.nombre}"
    
    
    