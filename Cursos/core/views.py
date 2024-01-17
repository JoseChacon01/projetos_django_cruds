from multiprocessing import context
from django.shortcuts import render, redirect
from .models import Cursos
from .forms import CursosForm

# Create your views here.

def cursos_listar(request):
    cursos = Cursos.objects.all()
    contexto = {
        'lista_de_cursos': cursos
    }
    return render(request, 'cursos.html', contexto)


def cursos_cadastrar(request):
    form = CursosForm(request.POST or None)

    if form.is_valid(): #se os dados forem validos, salve no banco
        form.save()
        return redirect ('cursos_listar') #após salvar os dados, deve retornar para primeira pagina ('cursos/')

    contexto = {
        'form_cursos': form
    }
    return render(request, 'cursos_cadastrar.html', contexto)


def editar_curso(request, id): #define um id para cada cursos, diferenciando-os
    cursos = Cursos.objects.get(pk=id)

    form = CursosForm(request.POST or None, instance=cursos)

    if form.is_valid():
        form.save()
        return redirect('cursos_listar')

    contexto = {
        'form_cursos': form
    }    

    return render(request, 'cursos_cadastrar.html', contexto)

def remover_cursos(request, id):
    cursos = Cursos.objects.get(pk=id)  
    cursos.delete()
    return redirect('cursos_listar')  