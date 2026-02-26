from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AutorForm, LibroForm
from .models import Libro

# Create your views here.
def index(request):
    return render(request,'index.html')

def lista_libros(request):
    libros = Libro.objects.all().order_by("titulo")
    return render(request, "lista_libros.html", {"libros": libros})

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