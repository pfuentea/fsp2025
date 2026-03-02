from django import forms
from .models import Ingrediente,Sandich,DetallePedido

class IngredienteForm(forms.ModelForm):
    class Meta:
        model= Ingrediente
        fields=['nombre','categoria','precio']


class SandwichForm(forms.ModelForm):
    class Meta:
        model= Sandich
        fields=['nombre','precio_base','ingredientes']

class DetallePedidoForm(forms.ModelForm):
    class Meta:
        model= DetallePedido
        fields=['sandwich','cantidad','extras','observacion']