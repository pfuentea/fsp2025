from django.urls import path
from . import views

urlpatterns = [
 path('dashboard/', views.dashboard,name='dashboard' ),
 path('', views.dashboard,name='dashboard' ),
 path('contacto/', views.contacto,name='contacto' ),
 path('landing/', views.landing,name='landing' ),

]