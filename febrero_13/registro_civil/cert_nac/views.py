from django.shortcuts import render
# Create your views here.

def index(request,usuario="",veces=1):
    #Acá va la lógica del negocio
    # render es un método que nos sirve para RENDERIZAR una
    # plantilla HTML

    # voy a crear una variable de sesion para guardar al usuario
    

    #creamos una variable de contexto, que es un diccionario
    if usuario != "":
        usuario=usuario
    else:
        usuario='Visitante'

    request.session['username']=usuario


    lugar='Santiago'

    repeticiones=[v for v in range(1,veces+1)]

    title=f'Reg Civ de {lugar}'

    context={
        'nombre':usuario,
        'ciudad':lugar,
        'title':title,
        'opcion':2,
        'veces':repeticiones,
    }
    return render(request,'index.html',context=context )

def servicios(request):


    context={}
    return render(request,'servicios.html',context=context )

def nosotros(request):
    context={}
    return render(request,'nosotros.html',context=context )

def contacto(request):
    
    usuario=request.session['username']

    context={
        'usuario':usuario,
    }
    return render(request,'contacto.html',context=context )