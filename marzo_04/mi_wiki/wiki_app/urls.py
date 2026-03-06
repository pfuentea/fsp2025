from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
urlpatterns = [
    path('',views.home,name='home'),

    path("categoria/<slug:slug>/", views.category_list, name="category_list"),
    path("articulo/<slug:slug>/", views.article_detail, name="article_detail"),

    path("articulos/nuevo/", views.article_create, name="article_create"),
    path("articulos/<slug:slug>/editar/", views.article_edit, name="article_edit"),
    path("articulos/<slug:slug>/eliminar/", views.article_delete, name="article_delete"),

    path("register/", views.register_view, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

]