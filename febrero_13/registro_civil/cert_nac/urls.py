from django.urls import path
from . import views

# LISTADO DE TRAMITES QUE PODREMOS REALiZAR
urlpatterns =[
    path('',views.index, name='index'), 
    path('<str:usuario>',views.index, name='index'), 
    path('<str:usuario>/<int:veces>',views.index, name='index'), 
    path('servicios/',views.servicios, name='servicios'), 
    path('contacto/',views.contacto, name='contacto'), 
    path('nosotros/',views.nosotros, name='nosotros'), 

] 
