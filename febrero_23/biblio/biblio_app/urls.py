from django.urls import path
from . import views

urlpatterns =[
    path('',views.index, name='index'),
    path('autores/crear',views.crear_autor, name="crear_autor"),
    path('autores/',views.lista_autores, name="lista_autores"),
    path('registro/',views.registro_view, name="registro"),
]
