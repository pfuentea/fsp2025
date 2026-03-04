from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView, DeleteView,DetailView
from .models import Ingrediente,Sandwich,DetallePedido,Pedido
from .forms import IngredienteForm,SandwichForm,DetallePedidoForm
from django.urls import reverse_lazy,reverse

# Create your views here.

def index(request):
    return render(request,'index.html')

class IngredientesListView(ListView):
    model=Ingrediente
    template_name='lista_ingrediente.html'
    context_object_name="ingredientes"
    ordering=['categoria','-nombre']

class IngredientesCreateView(CreateView):
    model=Ingrediente
    form_class=IngredienteForm
    template_name='form_ingrediente.html'
    success_url=reverse_lazy("ingredientes_list")

class IngredientesUpdateView(UpdateView):
    model=Ingrediente
    form_class=IngredienteForm
    template_name='form_ingrediente.html'
    success_url=reverse_lazy("ingredientes_list")

class IngredientesDeleteView(DeleteView):
    model=Ingrediente
    template_name="confirmar_borrado.html"
    
    def get_success_url(self):
        return reverse("ingredientes_list")

class SandwichesListView(ListView):
    model=Sandwich
    template_name='lista_sandwich.html'
    context_object_name="sandwiches"
    ordering=['nombre']

class SandwichesCreateView(CreateView):
    model=Sandwich
    form_class=SandwichForm
    template_name='form_sandwich.html'
    success_url=reverse_lazy("sandwiches_list")

class SandwichesUpdateView(UpdateView):
    model=Sandwich
    form_class=SandwichForm
    template_name='form_sandwich.html'
    success_url=reverse_lazy("sandwiches_list")

class SandwichesDeleteView(DeleteView):
    model=Sandwich
    template_name="confirmar_borrado.html"
    
    def get_success_url(self):
        return reverse("sandwiches_list")

class PedidosListView(ListView):
    model=Pedido
    template_name='lista_pedido.html'
    context_object_name="pedidos"
    ordering=['-updated_at']

class PedidosCreateView(CreateView):
    model=Pedido
    fields=[]
    template_name='pedido_crear.html'

    def get_success_url(self):
        return reverse("pedidos_detail",kwargs={"pk":self.object.pk})

class PedidosItemCreateView(CreateView):
    model=DetallePedido
    form_class = DetallePedidoForm
    template_name='form_pedido_item.html'

    def dispatch(self,request,*args,**kwargs):
        self.pedido=Pedido.objects.get(id=kwargs["pedido_id"])
        return super().dispatch(request,*args,**kwargs)

    def form_valid(self, form):
        form.instance.pedido = self.pedido
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("pedidos_detail", kwargs={"pk": self.pedido.pk})

class PedidosDetailView(DetailView):
    model=Pedido
    template_name="pedido_detail.html"
    context_object_name="pedido"

class PedidoItemUpdateView(UpdateView):
    model=DetallePedido
    form_class=DetallePedidoForm
    template_name='form_pedido_item.html'

    def dispatch(self,request,*args,**kwargs):
        self.pedido=Pedido.objects.get(id=kwargs["pedido_id"])
        return super().dispatch(request,*args,**kwargs)
    
    def get_success_url(self):
        return reverse("pedidos_detail", kwargs={"pk": self.pedido.pk})
    
    def get_queryset(self):
        return DetallePedido.objects.filter(pedido=self.pedido)
    
class PedidoItemDeleteView(DeleteView):
    model=DetallePedido
    template_name="confirmar_borrado.html"
    
    def dispatch(self,request,*args,**kwargs):
        self.pedido=Pedido.objects.get(id=kwargs["pedido_id"])
        return super().dispatch(request,*args,**kwargs)
   
    def get_success_url(self):
        return reverse("pedidos_detail", kwargs={"pk": self.pedido.pk})