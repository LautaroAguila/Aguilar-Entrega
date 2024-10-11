from django.template import Template, Context, loader
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect
from inicio.models import Computadora
from inicio.forms import *


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
