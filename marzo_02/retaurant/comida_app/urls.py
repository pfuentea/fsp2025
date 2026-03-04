from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),

    # CRUD (Ingredientes)
    path('ingredientes/', views.IngredientesListView.as_view(),name='ingredientes_list'), 
    path('ingredientes/nuevo/', views.IngredientesCreateView.as_view(),name='ingredientes_create'),
    path('ingredientes/<int:pk>/editar/', views.IngredientesUpdateView.as_view(),name='ingredientes_edit'),
    path('ingredientes/<int:pk>/eliminar/', views.IngredientesDeleteView.as_view(), name='ingredientes_delete'),
    

    # falta edita, detalle, borrar
    path('sandwiches/', views.SandwichesListView.as_view(),name='sandwiches_list'),
    path('sandwiches/nuevo/', views.SandwichesCreateView.as_view(),name='sandwiches_create'),
    path('sandwiches/<int:pk>/editar/', views.SandwichesUpdateView.as_view(),name='sandwiches_edit'),
    path('sandwiches/<int:pk>/eliminar/', views.SandwichesDeleteView.as_view(), name='sandwiches_delete'),
    
    #pedidos
    path('pedidos/', views.PedidosListView.as_view(),name='pedidos_list'),
    path('pedidos/nuevo/', views.PedidosCreateView.as_view(),name='pedidos_create'),
    path('pedidos/<int:pk>/', views.PedidosDetailView.as_view(),name='pedidos_detail'),

    #detalle del pedido 
    path('pedidos/<int:pedido_id>/items/nuevo/', views.PedidosItemCreateView.as_view(), name='pedidos_item_create'),
    path('pedidos/<int:pedido_id>/items/<int:pk>/editar/', views.PedidoItemUpdateView.as_view(), name='pedido_item_update'),
    path('pedidos/<int:pedido_id>/items/<int:pk>/eliminar/', views.PedidoItemDeleteView.as_view(), name='pedido_item_delete'),
    
 

]



'''
    # CRUD Sandwich + ingredientes
    
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