from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AutorForm,LibroFormSet
from .models import Autor
# Create your views here.

def index(request):
    context={}
    return render(request,'index.html',context=context)
    html="<html><body> <h1> Bienvenido </h1></body></html>"
    return HttpResponse(html)

def crear_autor(request):
    if request.method=='POST':
        form=AutorForm(request.POST)
        if form.is_valid():
            autor=form.save()

            formset= LibroFormSet(request.POST,instance=autor)
            if formset.is_valid():
                formset.save()
                return redirect('lista_autores')
    else:
        form=AutorForm()
        formset=LibroFormSet()

    context={
        'form':form,
        'formset':formset,
    }
    return render(request,'crear_autor.html',context=context)
            
def lista_autores(request):
    autores=Autor.objects.all()

    context={
            'autores':autores,
        }
    return render(request,'lista_autores.html',context=context)
