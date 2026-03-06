from django.contrib import admin
from .models import Articulo, Categoria

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "slug")
    search_fields = ("nombre",)
    prepopulated_fields = {"slug": ("nombre",)}

@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor", "categoria", "publicado", "modificado_en")
    list_filter = ("publicado", "categoria")
    search_fields = ("titulo", "contenido")
    prepopulated_fields = {"slug": ("titulo",)}
