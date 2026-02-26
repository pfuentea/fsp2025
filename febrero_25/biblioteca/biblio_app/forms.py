from django import forms
from django.contrib.auth.models import User
from .models import Libro,Autor

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields =['titulo','descripcion','autores']
        widgets ={
            'titulo':forms.TextInput(attrs={"class":"form-control"}),
            'descripcion':forms.Textarea(attrs={"rows":3,"class":"form-control"}),
            "autores":forms.SelectMultiple(attrs={"class":"form-select"})
        }


class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields =['nombre']
        widgets ={
            'nombre':forms.TextInput(attrs={"class":"form-control"}),
        }

class SignupForm(forms.ModelForm):
    password1= forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2= forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        model= User
        fields =['username','email']
        widgets={
            'username':forms.TextInput(attrs={"class":"form-control"}),
            'email':forms.EmailInput(attrs={"class":"form-control"}),
        }

    def clean(self):
        cleaned = super().clean()
        if cleaned.get("password1") != cleaned.get("password2"):
            self.add_error("password","Las passwords deben ser iguales")
        return cleaned