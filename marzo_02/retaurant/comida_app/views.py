from django.shortcuts import render
from django.views.generic import ListView,CreateView
from .models import Ingrediente,Sandich,DetallePedido,Pedido
from .forms import IngredienteForm,SandwichForm,DetallePedidoForm
# Create your views here.

def index(request):
    return render(request,'index.html')

class IngredientesListView(ListView):
    model=Ingrediente
    template_name='lista_ingrediente.html'
    context_objects_name="ingredientes"

class IngredientesCreateView(CreateView):
    model=Ingrediente
    form_class=IngredienteForm
    template_name='form_ingrediente.html'
    success_url="ingredientes_list"
