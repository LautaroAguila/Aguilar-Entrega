from django.template import Template, Context, loader
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render
from inicio.models import Auto


def mi_vista(request):
    return HttpResponse('papanatas')

def inicio(request):
    return render(request, 'inicio/index.html')

def vista_datos1 (request, nombre):
    nombre_mayus = nombre.upper()
    return HttpResponse(f'HOLA {nombre_mayus} !')

def primer_template(request) : 

    archivo_del_template = open(r'templates\inicio\primer_template.html')
    template = Template(archivo_del_template.read())
    archivo_del_template.close()
    contexto = Context()

    render_template = template.render(contexto)

    return HttpResponse(render_template)
def segundo_template(request) : 


    fecha_actual = datetime.now()
    datos = {   'fecha_actual' : fecha_actual,
                'numeros' : list(range(1,11))
            }

    #v1
    # archivo_del_template = open(r'templates\segundo_template.html')
    # template = Template(archivo_del_template.read())
    # archivo_del_template.close()
    #contexto = Context(datos)
    #render_template = template.render(contexto)
    #return HttpResponse(render_template)
    
    #v2
    # template = loader.get_template('segundo_template.html')
    # render_template = template.render(datos)
    # return HttpResponse(render_template)

    #v3
    return render(request, 'inicio/segundo_template.html', datos)

def crear_auto (request, marca, modelo, anio):

    auto = Auto(marca = marca,modelo = modelo ,anio = anio)
    auto.save()
    return render(request, 'inicio/creacion_auto_correcta.html', {'auto':auto})