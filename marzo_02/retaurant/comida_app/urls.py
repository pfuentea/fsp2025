from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),

    # CRUD (Ingredientes)
    path('ingredientes/', views.IngredientesListView.as_view(),name='ingredientes_list'), 
    path('ingredientes/nuevo', views.IngredientesCreateView.as_view(),name='ingredientes_create'),
    # falta edita, detalle, borrar
'''
    # CRUD Sandwich + ingredientes
    path('sandwiches/', views.SandwichesListView.as_view(),name='sandwiches_list'),
    path('sandwiches/nuevo', views.SandwichesCreateView.as_view(),name='sandwiches_create'),
# falta edita, detalle, borrar

    #Pedidos
    path('pedidos/nuevo', views.PedidosCreateView.as_view(),name='pedido_create'),
    path('pedidos/<int:pk>', views.PedidosDetailView.as_view(),name='pedido_detalle'),
    # falta edita, detalle, borrar

    #Detalle pedido
    path('pedidos/<int:orde_id>/items/nuevo', views.PedidoDetalleCreateView.as_view(),name='pedido_detalle_create'),
    # falta edita, detalle, borrar

'''

]