from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
# Create your views here.

def index(request):
    return render(request,'index.html')



from .forms import ArticuloForm, RegisterForm
from .models import Articulo, Categoria

def home(request):
    q = request.GET.get("q", "").strip()
    categoria_slug = request.GET.get("cat", "").strip()

    articulos = Articulo.objects.filter(publicado=True).select_related("categoria", "autor")

    if categoria_slug:
        articulos = articulos.filter(categoria__slug=categoria_slug)

    if q:
        articulos = articulos.filter(Q(titulo__icontains=q) | Q(contenido__icontains=q))

    paginator = Paginator(articulos, 6)  # 6 por página
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    categorias = Categoria.objects.all()

    return render(request, "wiki/home.html", {
        "page_obj": page_obj,
        "q": q,
        "categorias": categorias,
        "categoria_slug": categoria_slug,
    })


def category_list(request, slug):
    categoria = get_object_or_404(Categoria, slug=slug)
    articulos = Articulo.objects.filter(publicado=True, categoria=categoria).select_related("autor", "categoria")

    paginator = Paginator(articulos, 6)
    page_obj = paginator.get_page(request.GET.get("page"))

    return render(request, "wiki/category_list.html", {
        "categoria": categoria,
        "page_obj": page_obj
    })


def article_detail(request, slug):
    articulo = get_object_or_404(Articulo.objects.select_related("autor", "categoria"), slug=slug)

    # si no está publicado, solo autor o staff lo puede ver
    if not articulo.publicado:
        if not request.user.is_authenticated or (request.user != articulo.autor and not request.user.is_staff):
            raise Http404("Artículo no disponible")

    relacionados = Articulo.objects.filter(
        publicado=True,
        categoria=articulo.categoria
    ).exclude(pk=articulo.pk)[:5]

    return render(request, "wiki/article_detail.html", {
        "articulo": articulo,
        "relacionados": relacionados
    })


@login_required
def article_create(request):
    if request.method == "POST":
        form = ArticuloForm(request.POST)
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.autor = request.user
            articulo.save()
            messages.success(request, "Artículo creado correctamente.")
            return redirect("article_detail", slug=articulo.slug)
        messages.error(request, "Revisa los errores del formulario.")
    else:
        form = ArticuloForm()

    return render(request, "wiki/article_form.html", {
        "form": form,
        "modo": "crear",
    })


@login_required
def article_edit(request, slug):
    articulo = get_object_or_404(Articulo, slug=slug)

    if request.user != articulo.autor and not request.user.is_staff:
        messages.error(request, "No tienes permisos para editar este artículo.")
        return redirect("article_detail", slug=articulo.slug)

    if request.method == "POST":
        form = ArticuloForm(request.POST, instance=articulo)
        if form.is_valid():
            form.save()
            messages.success(request, "Artículo actualizado correctamente.")
            return redirect("article_detail", slug=articulo.slug)
        messages.error(request, "Revisa los errores del formulario.")
    else:
        form = ArticuloForm(instance=articulo)

    return render(request, "wiki/article_form.html", {
        "form": form,
        "modo": "editar",
        "articulo": articulo
    })


@login_required
def article_delete(request, slug):
    articulo = get_object_or_404(Articulo, slug=slug)

    if request.user != articulo.autor and not request.user.is_staff:
        messages.error(request, "No tienes permisos para eliminar este artículo.")
        return redirect("article_detail", slug=articulo.slug)

    if request.method == "POST":
        articulo.delete()
        messages.success(request, "Artículo eliminado.")
        return redirect("home")

    return render(request, "wiki/article_confirm_delete.html", {"articulo": articulo})


def register_view(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registro exitoso. ¡Bienvenido!")
            return redirect("home")
        messages.error(request, "Revisa el formulario.")
    else:
        form = RegisterForm()

    return render(request, "wiki/register.html", {"form": form})