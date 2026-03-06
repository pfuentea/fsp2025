from django.shortcuts import render

from rest_framework import viewsets
from .models import Autor,Libro
from .serializers import AutorSerializer,LibroSerializer,AutorDetailSerializer
# Create your views here.

class AutorViewSet(viewsets.ModelViewSet):
    queryset= Autor.objects.all()

    def get_serializer_class(self):
        if self.action =="retrieve":
            return AutorDetailSerializer
        return AutorSerializer
    
class LibroViewSet(viewsets.ModelViewSet):
    queryset=Libro.objects.all()
    serializer_class =LibroSerializer