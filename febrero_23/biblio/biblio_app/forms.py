from django.forms import inlineformset_factory
from .models import Autor,Libro,Usuario
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

class RegistroModelForm(forms.ModelForm):

    password=forms.CharField(
        widget=forms.PasswordInput,
        min_length=6,
        label="Contraseña"
    )

   

    class Meta:
        model=Usuario
        fields=['nombre','email','edad','password']
        widgets={
        "nombre":forms.TextInput(attrs={"class":"form-control"}),
        "email":forms.EmailInput(attrs={"class":"form-control"}),
        "edad":forms.NumberInput(attrs={"class":"form-control"}),
        "password":forms.PasswordInput(attrs={"class":"form-control"}),
    }

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre","").strip()

        if len(nombre)<3:
            raise forms.ValidationError("El nombre debe tener al menos 3 caracteres")

        if nombre.lower() == "admin":
            raise forms.ValidationError("El nombre no puede ser admin")
        return nombre
    
    def clean_edad(self):
        edad  = self.cleaned_data.get("edad")

        if edad <18:
            raise forms.ValidationError("Debes ser mayor de edad para registrarte")
        
        return edad
    
    def clean(self):
        cleaned_data= super().clean()

        return cleaned_data
    
