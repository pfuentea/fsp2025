from django.shortcuts import render
# Create your views here.

def index(request):
    #Acá va la lógica del negocio
    # render es un método que nos sirve para RENDERIZAR una
    # plantilla HTML

    #creamos una variable de contexto, que es un diccionario
    usuario='Gloria'
    lugar='Santiago'

    title=f'Reg Civ de {lugar}'

    context={
        'nombre':usuario,
        'ciudad':lugar,
        'title':title,
    }
    return render(request,'index.html',context=context )

def servicios(request):
    context={}
    return render(request,'servicios.html',context=context )


def nosotros(request):
    context={}
    return render(request,'nosotros.html',context=context )

def contacto(request):
    context={}
    return render(request,'contacto.html',context=context )