from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.index,name='index'), 
    #Rutas de AUTH
    path("register/", views.register_view, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    #Rutas de la APP
    path("posts/", views.lista_posts, name="lista_posts"), 
    path("posts/new", views.create_posts, name="create_posts"), 
    path("posts/<int:post_id>/<int:post_padre>/", views.detalle_posts, name="detalle_posts"), 
    path("post/responder/<int:post_id>/<int:post_padre>",views.crear_respuesta,name="crear_respuesta" ),
    
    

]   