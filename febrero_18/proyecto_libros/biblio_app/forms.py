from django import forms
from .models import Libro,Autor

class AutorForm(forms.ModelForm):
    class Meta:
        model=Autor

        fields=['nombre','nacionalidad']


class LibroForm(forms.ModelForm):
    class Meta:
        model=Libro

        fields=['titulo','anio_publicacion','disponible','autor']

        widget={
            "autor":forms.Select(),
        }
