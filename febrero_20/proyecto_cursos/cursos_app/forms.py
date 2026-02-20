from django import forms
from .models import Estudiante,Curso

class EstudianteForm(forms.ModelForm):
    class Meta:
        model=Estudiante
        fields=['nombre','email']

class CursoForm(forms.ModelForm):
    class Meta:
        model=Curso
        fields=['nombre','codigo','estudiantes']

        widget={
            'estudiantes':forms.SelectMultiple()
        }