from django import forms
from .models import Archivo

class ArchivoForm(forms.ModelForm):
    class Meta:
        model= Archivo
        fields = ['nombre','ruta']

    def clean_archivo(self):
        f= self.cleaned_data.get("ruta")
        if not f:
            return f
        
        max_mb=5
        if f.size > max_mb *1024*1024: # 5 megas == (5000 kilos)
            raise forms.ValidationError(f"El archivo no puede superar los {max_mb}MB ")
        
        nombre=f.name.lower()
        # agregar validacion para no permitir .js .exe. .py script ejecutable 
        return f