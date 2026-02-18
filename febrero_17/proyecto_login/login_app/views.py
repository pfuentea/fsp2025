from django.shortcuts import render
from .forms import LoginForm
# Create your views here.

def index(request):
    
    context={

    }
    return render(request,'index.html',context=context)

def login_view(request):
    USER_FIX="admin"
    PASS_FIX="12345"
    msg=""

    if request.method =='POST': # esto es cuando hago envio del formulario
        print(request.POST)
        form=LoginForm(request.POST)

        if form.is_valid():
            
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]

            if username==USER_FIX and password==PASS_FIX:
                #guardamos la session
                return render(request,'dashboard.html')
            else:
                msg="Error en las credenciales"
        


    else: # esto es cuando entro a la pagina de login
        form=LoginForm()

    context={
        'form':form,
        'msg':msg,
    }
    return render(request,'login.html',context=context)

