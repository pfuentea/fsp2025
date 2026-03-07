from django.shortcuts import render,redirect 
from .forms import RegisterForm,PostForm,RespuestaForm
from django.contrib import messages
from django.contrib.auth import login
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    return render(request,'index.html')

def register_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro exitoso. ¡Bienvenido!")
            return redirect("index")
        messages.error(request, "Revisa el formulario.")
    else:
        form = RegisterForm()
    context= {
            "form": form
            }
    return render(request, "register.html",context=context)

def lista_posts(request):
    #posts=Post.objects.all()
    posts=Post.objects.filter(padre__isnull=True)

    context={
        'posts':posts
    }
    return render(request,'posts_lista.html',context=context)

@login_required
def create_posts(request):
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.autor=request.user
            post.save()
            return redirect('lista_posts')
    else:
        form=PostForm
    context={
        'form':form,
    }
    return render(request,'form_posts.html',context=context)

@login_required
def crear_respuesta(request,post_id,post_padre):
    post_super=post_padre
    post_padre=Post.objects.get(id=post_id)
    if request.method=='POST':
        form=RespuestaForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.autor=request.user
            post.padre=post_padre
            post.save()
            return redirect('detalle_posts' ,post_super, post_super)
    else:
        form=RespuestaForm()
    context={
        'form':form,
        'post_padre':post_padre,
    }
    return render(request,'form_respuesta.html',context=context)

def detalle_posts(request,post_id,post_padre):
    post=Post.objects.get(id=post_id)
    form=RespuestaForm()
    respuestas_hijas=post.hijos.all()
    post_padre=Post.objects.get(id=post_padre)

    context={
        'post':post,
        'form':form,
        'respuestas_hijas':respuestas_hijas,
        'post_padre':post_padre,
    }
    return render(request,'detalle_post.html',context=context)