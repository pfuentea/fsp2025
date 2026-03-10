from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class RegisterForm(UserCreationForm):
    first_name=forms.CharField(max_length=50,required=True,label="Nombre")
    last_name=forms.CharField(max_length=50,required=True,label="Apellido")
    email=forms.EmailField(required=True,label="Correo Electrónico")

    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password1","password2"]

    def save(self,commit=True):
        user=super().save(commit=False)
        user.first_name=self.cleaned_data["first_name"]
        user.last_name=self.cleaned_data["last_name"]
        user.email=self.cleaned_data["email"]
        if commit:
            user.save()

        return user
    
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email"]
        labels={
            "first_name":"Nombre",
            "last_name":"Apellido",
            "email":"Correo Electrónico",
        }

class ProfileUpdateForm(forms.ModelForm):
    fecha_nacimiento=forms.DateField(required=False,widget=forms.DateInput(attrs={"type":"date"}))
    class Meta:
        model=Profile
        fields=["telefono","fecha_nacimiento","foto","bio"]
        labels ={
            "telefono":"Telefóno",
            "fecha_nacieminto":"Fecha de nacimiento",
            "foto":"Foto",
            "bio":"Biografía",
        }
        widgets={
            "bio":forms.Textarea(attrs={"rows":4})
        }