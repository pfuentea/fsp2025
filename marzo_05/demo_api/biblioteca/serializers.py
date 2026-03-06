from rest_framework import serializers
from .models import Autor,Libro

class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Autor
        fields=['id','nombre']

class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model=Libro
        fields=['id','titulo','precio','autor']

class AutorDetailSerializer(serializers.ModelSerializer):
    libros=LibroSerializer(many=True,read_only=True)

    class Meta:
        model=Autor
        fields=['id','nombre','libros']