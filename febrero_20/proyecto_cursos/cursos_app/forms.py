from django import forms
from .models import Estudiante,Curso

class EstudianteForm(forms.ModelForm):
    class Meta:
        model=Estudiante
        fields=['nombre','email']

        widgets={
            "nombre":forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Nombre"
                }),
            "email":forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"correo@dominio.com"
                })
        }

class CursoForm(forms.ModelForm):
    class Meta:
        model=Curso
        fields=['nombre','codigo','estudiantes']

        widgets={
            'estudiantes':forms.SelectMultiple(attrs={"class":"form-select"}),
            'codigo':forms.TextInput(attrs={"class":"form-control","placeholder":"COD-001"}),
            'nombre':forms.TextInput(attrs={"class":"form-control","placeholder":"Nombre del curso"}),
        }