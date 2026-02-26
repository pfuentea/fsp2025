from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('libros/', views.lista_libros, name="lista_libros"),

    path("autor/crear/", views.crear_autor, name="crear_autor"),
    path("libro/crear/", views.crear_libro, name="crear_libro"),
]