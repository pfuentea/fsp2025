from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario",max_length=50)
    correo = forms.EmailField(label="Correo electrónico")
    password = forms.CharField(label="Contraseña",widget=forms.PasswordInput)