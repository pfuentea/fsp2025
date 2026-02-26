from django.shortcuts import render,redirect
from .models import Libro,Autor
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .forms import LibroForm,SignupForm,AutorForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import login

# Create your views here.

def index(request):
    return render(request,'index.html')

class LibroListView(ListView):
    model= Libro
    template_name = 'libros/list.html'
    context_object_name ='libros'

    def get_queryset(self):
        return Libro.objects.filter(creador=self.request.user)

class LibroDetailView(DetailView):
    model= Libro
    template_name = 'libros/detail.html'
    context_object_name ='libros'

class LibroCreateView(CreateView):
    model= Libro
    template_name = 'libros/form.html'
    form_class=LibroForm
    success_url=reverse_lazy('libro_list')
    
    def form_valid(self,form):
        form.instance.creador=self.request.user
        messages.success(self.request,"libro creado exitosamente")
        return super().form_valid(form)
    

class LibroUpdateView(UpdateView):
    model=Libro
    form_class=LibroForm #uso el mismo form que para la creación
    template_name='libros/form.html'
    success_url=reverse_lazy('libro_list')

    
class MiLoginView(LoginView):
    template_name='auth/login.html'

class MiLogoutView(LogoutView):
    next_page=reverse_lazy('login')

def signup_view(request):
    if request.method == 'POST':
        form= SignupForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            login(request,user)
            messages.success(request,"Cuenta creada con exito!")
            return redirect('libro_list')
    else:
        form=SignupForm()
    context={
        'form':form,
    }
    return render(request,'auth/signup.html',context=context)
    
class AutorListView(ListView):
    model= Autor
    template_name = 'autor/list.html'
    context_object_name ='autores'


class AutorDetailView(DetailView):
    model= Autor
    template_name = 'autor/detail.html'
    context_object_name ='autores'

class AutorCreateView(CreateView):
    model= Autor
    template_name = 'autor/form.html'
    form_class=AutorForm
    success_url=reverse_lazy('autor_list')
    def form_valid(self,form):
        messages.success(self.request,"autor creado exitosamente")
        return super().form_valid(form)
    
class AutorUpdateView(UpdateView):
    model=Autor
    form_class=AutorForm #uso el mismo form que para la creación
    template_name='autor/form.html'
    success_url=reverse_lazy('autor_list')