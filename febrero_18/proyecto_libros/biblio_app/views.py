from django.shortcuts import render, redirect

from .models import Libro,Autor
from .forms import LibroForm,AutorForm
# Create your views here.


def index(request):
    #USAMOS ORM de DJANGO
    libros=Libro.objects.all() # select * from libros

    context={
        'libros':libros,
    }
    return render(request,'index.html',context=context)

def libro_crear(request):

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
    return render(request,'libro_crear.html',context=context)

def autor_list(request):
    autores=Autor.objects.all()
    
    context={
        'autores':autores,
    }

    return render(request,'autor_list.html',context=context)

def autor_crear(request):
    '''
    un comentario
    de varias
    lineas
    '''

    # este comentario es de usa sola línea

    if request.method =='POST':
        form=AutorForm(request.POST)
        if form.is_valid():
            autor=form.save()
            return redirect('autor_list')
    else:
        form= AutorForm()

    context={
        'form':form,
    }

    return render(request,'autor_crear.html',context=context)

def autor_detail(request,autor_id):
    autor=Autor.objects.get(id=autor_id)
    libros=autor.libros.all()

    context={
        'libros':libros,
        'autor':autor,
    }

    return render(request,'autor_detail.html',context=context)
