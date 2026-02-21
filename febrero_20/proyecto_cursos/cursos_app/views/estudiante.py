from django.shortcuts import render, redirect
from ..models import Estudiante
from ..forms import EstudianteForm

# vista lista de estudiantes
def estudiante_list(request):
    estudiantes=Estudiante.objects.all()
    context={
        'estudiantes':estudiantes,
    }
    return render(request,'estudiante_list.html',context=context)

def estudiante_detail(request,estudiante_id):
    estudiante=Estudiante.objects.get(id=estudiante_id)
    cursos=estudiante.cursos.all()
    context={
        'estudiante':estudiante,
        'cursos':cursos
    }
    return render(request,'estudiante_detail.html',context=context)


# vista de creacion de estudiantes
def estudiante_create(request):
    if request.method=='POST':
        form=EstudianteForm(request.POST)
        if form.is_valid():
            estudiante=form.save()
            return redirect('estudiante_list')
    else:
        form=EstudianteForm()
    context={
        'form':form,
        'button_label':'Crear',
    }
    return render(request,'estudiante_create.html',context=context)

def estudiante_edit(request,estudiante_id):

    estudiante=Estudiante.objects.get(id=estudiante_id)
    if request.method=='POST':
        form=EstudianteForm(request.POST, instance=estudiante)
        if form.is_valid():
            estudiante=form.save()
            return redirect('estudiante_detail',estudiante_id=estudiante_id)
    else:
        form=EstudianteForm( instance=estudiante)
    context={
        'form':form,
        'button_label':'Guardar',
    }
    return render(request,'estudiante_create.html',context=context)