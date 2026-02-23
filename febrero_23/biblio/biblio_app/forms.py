from django.forms import inlineformset_factory
from .models import Autor,Libro
from django import forms

class AutorForm(forms.ModelForm):
    class Meta:
        model=Autor
        fields=['nombre']

LibroFormSet= inlineformset_factory(
    Autor,
    Libro,
    fields=('titulo',),
    extra=3, #cantidad de formularios relacionados
    can_delete=True # para que permita la eliminación de libros
)

