from django.shortcuts import render,redirect
from .forms import ArchivoForm
from django.contrib import messages
from .models import Archivo
from django.conf import settings
from django.conf.urls.static import static

# Create your views here.

def index(request):
    context={
        
    }
    return render(request,'index.html',context=context)

def crear_archivo(request):
    if request.method=='POST':
        form=ArchivoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            
            messages.success(request,"Archivo cargado correctamente")
            return redirect('lista_archivos')
        
    else:
        form=ArchivoForm()

    context={
        'form':form,
    }
    return render(request,'crear_archivo.html',context=context)

def list_archivos(request):
    archivos=Archivo.objects.all()

    context={
        'archivos':archivos,
        'ruta':ruta_raiz(),
    }
    return render(request,'listar_archivos.html',context=context)

def ruta_raiz():
    if settings.DEBUG:
        return settings.MEDIA_ROOT
