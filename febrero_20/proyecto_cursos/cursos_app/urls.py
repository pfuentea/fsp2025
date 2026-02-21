from django.urls import path
from . import views
from .views import estudiante,curso,site


urlpatterns =[
    path('',site.index, name='index'),
    
    path('curso_list',curso.curso_list, name='curso_list'),
    path('curso_detail/<int:curso_id>',curso.curso_detail, name='curso_detail'),
    path('curso_create/',curso.curso_create, name='curso_create'),
    path('curso_edit/<int:curso_id>',curso.curso_edit, name='curso_edit'),
    
    path('estudiante_list/',estudiante.estudiante_list, name='estudiante_list'),
    path('estudiante_detail/<int:estudiante_id>',estudiante.estudiante_detail, name='estudiante_detail'),
    path('estudiante_create/',estudiante.estudiante_create, name='estudiante_create'),
    path('estudiante_edit/<int:estudiante_id>',estudiante.estudiante_edit, name='estudiante_edit'),
    

] 