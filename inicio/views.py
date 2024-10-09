from django.template import Template, Context, loader
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from inicio.models import Computadora


def mi_vista(request):
    return HttpResponse('papanatas')

def inicio(request):
    return render(request, 'inicio/index.html')

def primer_template(request) : 
    contexto = Context()
    return render(request, 'inicio/primer_template.html')
def segundo_template(request) : 
    fecha_actual = datetime.now()
    datos = {   'fecha_actual' : fecha_actual,
                'numeros' : list(range(1,11))
            }
    return render(request, 'inicio/segundo_template.html', datos)

def crear_computadora (request, cpu, gpu, ram):

    computadora = computadora(cpu = cpu,gpu = gpu ,ram = ram)
    computadora.save()
    return render(request, 'inicio/creacion_computadora_correcta.html', {'computadora':computadora})

def buscar_computadora (request):

    return render(request, 'inicio/buscar_computadora.html', {'computadora':''})
def crear_computadora (request):

    return render(request, 'inicio/crear_computadora.html', {'computadora':''})
