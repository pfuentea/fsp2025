from django.urls import path
from .views import CustomLoginViews,CustomLogoutView,register_view,profile_view,profile_edit_view

app_name="core_auth"

urlpatterns=[
    path("login/",CustomLoginViews.as_view(),name="login"),
    path("logout/",CustomLogoutView.as_view(),name="logout"),
    path("register/",register_view,name="register"),
    path("profile/",profile_view,name="profile"),
    path("profile/edit/",profile_edit_view,name="profile_edit"),
]