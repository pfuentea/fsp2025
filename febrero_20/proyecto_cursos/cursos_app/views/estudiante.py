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
    }
    return render(request,'estudiante_create.html',context=context)

