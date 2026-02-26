from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AutorForm, LibroForm
from .models import Libro

# Create your views here.
def index(request):
    return render(request,'index.html')

def lista_libros(request):
    libros = Libro.objects.all().order_by("-titulo")
    libros_por_autor = Libro.objects.filter(autor__nombre='Pablo Neruda')
    autor ='Pablo Neruda'
    titulos_con_poema = Libro.objects.filter(titulo__icontains='poema') # LIKE '%poema%'
    libros_mayor_1950 = Libro.objects.filter(anio__gt=1950 ) # gt = greater than 


    context={
        "libros": libros,
        "libros_por_autor":libros_por_autor,
        'autor':autor,
        'titulos_con_poema':titulos_con_poema,
        'libros_mayor_1950':libros_mayor_1950,
             }
    return render(request, "lista_libros.html",context=context )

def crear_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Autor creado correctamente.")
            return redirect("crear_autor")
    else:
        form = AutorForm()

    return render(request, "crear_autor.html", {"form": form})

def crear_libro(request):
    if request.method == "POST":
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Libro creado correctamente.")
            return redirect("crear_libro")
    else:
        form = LibroForm()

    return render(request, "crear_libro.html", {"form": form})