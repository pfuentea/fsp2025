from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),

    # CRUD (Ingredientes)
    path('ingredientes/', views.IngredientesListView.as_view(),name='ingredientes_list'), 
    path('ingredientes/nuevo', views.IngredientesCreateView.as_view(),name='ingredientes_create'),
    # falta edita, detalle, borrar


]