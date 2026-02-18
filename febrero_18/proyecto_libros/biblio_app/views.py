from django.shortcuts import render, redirect

from .models import Libro
from .forms import LibroForm
# Create your views here.


def index(request):
    #USAMOS ORM de DJANGO
    libros=Libro.objects.all() # select * from libros

    context={
        'libros':libros,
    }
    return render(request,'index.html',context=context)

def crear(request):

    if request.method =='POST':
        print(request.POST)
        form=LibroForm(request.POST)  
        if form.is_valid():
            form.save() # en este momento se CREA el registro en la base de datos  
            return redirect('index')

    else: #caso de GET
        form = LibroForm() # creamos un formulario vacio para mostrar en el template

    context={
        'form':form,
    }
    return render(request,'crear.html',context=context)