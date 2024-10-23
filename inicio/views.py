from django.template import Template, Context, loader
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect
from inicio.models import Computadora
from inicio.forms import *
from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request, 'inicio/index.html')

def buscar_computadora (request):
    formulario = BuscarComputadoraFormulario(request.GET)

    if formulario.is_valid():
        cpu = formulario.cleaned_data.get('cpu')
        compus = Computadora.objects.filter(cpu__icontains = cpu)
    else:
        compus = Computadora.objects.all()
    return render(request, 'inicio/buscar_computadora.html', {'compus':compus, 'form' : formulario})


def about (request):
    return render(request, 'inicio/about.html')

def ver_computadora(request, id):
    compu = Computadora.objects.get(id=id)
    return render(request, 'inicio/ver_computadora.html', {'compu' : compu} )

@login_required
def eliminar_computadora(request, id):
    compu = Computadora.objects.get(id=id)
    compu.delete()
    return redirect('inicio:buscar_computadora')

def editar_computadora(request, id):

    compu = Computadora.objects.get(id=id)

    formulario = EditarComputadoraFormulario(initial={'cpu': compu.cpu, 'gpu' : compu.gpu, 'ram' : compu.ram})

    if request.method == 'POST':
        formulario = EditarComputadoraFormulario(request.POST)
        if formulario.is_valid():
            compu.cpu = formulario.cleaned_data.get('cpu')
            compu.gpu = formulario.cleaned_data.get('gpu')
            compu.ram = formulario.cleaned_data.get('ram')
            compu.save()
            return redirect('inicio:buscar_computadora')
    return render(request, 'inicio/editar_computadora.html', {'compu':compu,'form' : formulario})

def crear_computadora (request):

    print('Request', request)
    print('GET', request.POST)
    print('POST', request.GET)

    formulario = CrearComputadoraFormulario()

    if request.method == 'POST':    
        #computadora = Computadora(cpu = request.POST.get('cpu'),gpu = request.POST.get('gpu') ,ram = request.POST.get('ram'))
        #computadora.save()
        formulario = CrearComputadoraFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            computadora = Computadora(cpu = data.get('cpu'),gpu = data.get('gpu') ,ram = data.get('ram'))
            computadora.save()
            return redirect('inicio:buscar_computadora')

    return render(request, 'inicio/crear_computadora.html', {'form': formulario})
