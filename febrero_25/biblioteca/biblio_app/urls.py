from django.urls import path
from .views import index,LibroCreateView,LibroDetailView,LibroListView,MiLoginView,MiLogoutView,signup_view,AutorListView,AutorCreateView,AutorDetailView,LibroUpdateView,AutorUpdateView


urlpatterns = [
    path('', index,name='index'), 

    # CBV: Class Base View
    path('libros/', LibroListView.as_view(),name='libro_list'), 
    path('libros/<int:pk>', LibroDetailView.as_view(),name='libro_detail'), 
    path('libros/crear/', LibroCreateView.as_view(),name='libro_create'), 
    path('libros/<int:pk>/editar/', LibroUpdateView.as_view(),name='libro_update'),

    path('autores/', AutorListView.as_view(),name='autor_list'), 
    path('autores/<int:pk>', AutorDetailView.as_view(),name='lautor_detail'), 
    path('autores/crear/', AutorCreateView.as_view(),name='autor_create'), 
    path('autores/<int:pk>/editar/', AutorUpdateView.as_view(),name='autor_update'),

    #AUTH
    path('login/', MiLoginView.as_view(),name='login'), 
    path('logout/', MiLogoutView.as_view(),name='logout'),
    path('signup/', signup_view,name='signup'),  
    
    
]