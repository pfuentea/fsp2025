from django.shortcuts import render, redirect
from ..models import Curso
from ..forms import CursoForm

def curso_list(request):
    cursos=Curso.objects.all()
    context={
        'cursos':cursos
    }
    return render(request,'curso_list.html',context=context)

# vista mostrar el detalle de un curso
def curso_detail(request,curso_id):
    curso=Curso.objects.get(id=curso_id)
    estudiantes= curso.estudiantes.all()
    context={
        'curso':curso,
        'estudiantes':estudiantes,
    }
    return render(request,'curso_detail.html',context=context)

# vista de cracion de curso
def curso_create(request):
    if request.method=='POST':
        form=CursoForm(request.POST)
        if form.is_valid():
            curso=form.save()
            return redirect('curso_list')
    else:
        form=CursoForm()
    context={
        'form':form,
        'button_label':'Crear',
    }
    return render(request,'curso_create.html',context=context)


def curso_edit(request,curso_id):
    curso=Curso.objects.get(id=curso_id)

    if request.method=='POST':
        form=CursoForm(request.POST, instance=curso)
        if form.is_valid():
            curso=form.save()
            return redirect('curso_detail',curso_id=curso_id)
    else:
        form=CursoForm(instance=curso)
    context={
        'form':form,
        'button_label':'Guardar',
    }
    return render(request,'curso_create.html',context=context)
