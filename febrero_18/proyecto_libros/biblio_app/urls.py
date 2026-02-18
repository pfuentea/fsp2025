from django.urls import path
from . import views
urlpatterns =[
    path('',views.index, name='index'),
    path('crear/',views.crear, name='crear'),

    path('servicios/',views.index, name='servicios'), 
    path('contacto/',views.index, name='contacto'), 
    path('nosotros/',views.index, name='nosotros'),
]