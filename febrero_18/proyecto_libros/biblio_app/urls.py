from django.urls import path
from . import views
urlpatterns =[
    path('',views.index, name='index'),
    # rutas de autores
    path('autor_crear/',views.autor_crear, name='autor_crear'),
    path('autor_list/',views.autor_list, name='autor_list'),
    path('autor_detail/<int:autor_id>',views.autor_detail, name='autor_detail'),


    #rutas de libros
    path('libro_crear/',views.libro_crear, name='libro_crear'),

    
    path('servicios/',views.index, name='servicios'), 
    path('contacto/',views.index, name='contacto'), 
    path('nosotros/',views.index, name='nosotros'),
]