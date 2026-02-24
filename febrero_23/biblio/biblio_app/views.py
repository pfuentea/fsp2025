from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import AutorForm,LibroFormSet, RegistroModelForm
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

def registro_view(request):
    if request.method=='POST':
        form=RegistroModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Usuario registrado exitosamente!")

    
            return redirect('registro')
        else:
            messages.error(request,"error en los datos del formulario!")

    else:
        form=RegistroModelForm()
        

    context={
        'form':form,
    }
    return render(request,'registro.html',context=context)