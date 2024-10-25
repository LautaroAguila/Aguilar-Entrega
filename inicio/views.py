from django.template import Template, Context, loader
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render, redirect
from productos.models import Computadora
from inicio.forms import *
from django.contrib.auth.decorators import login_required


def inicio(request):
    compus = Computadora.objects.all()
    return render(request, 'inicio/index.html', {'compus':compus})

def about (request):
    return render(request, 'inicio/about.html')

