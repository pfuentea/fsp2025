from django.urls import path
from . import views

urlpatterns = [
    path('',views.index ) ,# primera ruta de nuestra APP
]
