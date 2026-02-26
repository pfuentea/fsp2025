from django import forms
from .models import Autor, Libro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ["nombre", "nacionalidad"]
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "nacionalidad": forms.TextInput(attrs={"class": "form-control"}),
        }


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ["titulo", "anio", "autor"]
        widgets = {
            "titulo": forms.TextInput(attrs={"class": "form-control"}),
            "anio": forms.NumberInput(attrs={"class": "form-control"}),
            "autor": forms.Select(attrs={"class": "form-select"}),
        }