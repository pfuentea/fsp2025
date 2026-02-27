from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('archivos/crear', views.crear_archivo,name='crear_archivo'),
    path('archivos/', views.list_archivos,name='lista_archivos'),
]