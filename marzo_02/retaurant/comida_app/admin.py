from django.contrib import admin
from .models import Ingrediente, Sandwich,Pedido,DetallePedido
# Register your models here.

#admin.site.register(Ingrediente)
@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display=('nombre','categoria','precio')
    list_filter=('categoria',)
    search_fields=('nombre','categoria',) # busca en el nombre y la categoria
    ordering = ('nombre',)
    list_per_page= 3

#admin.site.register(Sandwich)
@admin.register(Sandwich)
class SandwichAdmin(admin.ModelAdmin):
    list_display=('nombre','precio_base')
    filter_horizontal=('ingredientes',)

admin.site.register(Pedido)
#admin.site.register(DetallePedido)

@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    list_display=('pedido','sandwich','cantidad','observacion','total_admin')
    list_filter=('pedido',)
    @admin.display(description="Total")
    def total_admin(self,obj):
        return obj.total_por_fila()