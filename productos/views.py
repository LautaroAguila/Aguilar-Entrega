from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *
from productos.models import Paleta
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class CrearPaleta(LoginRequiredMixin, CreateView):
    model = Paleta
    template_name = "productos/crear_paleta.html"
    success_url = reverse_lazy('productos:listado_paletas')
    fields = ['modelo', 'marca', 'fecha']

class ListadoPaletas(ListView):
    model = Paleta
    template_name = "productos/listado_paletas.html"
    context_object_name = 'paletas'

class VerPaleta(DetailView):
    model = Paleta
    template_name = "productos/ver_paleta.html"

class EditarPaleta(LoginRequiredMixin, UpdateView):
    model = Paleta
    template_name = "productos/editar_paleta.html"
    success_url = reverse_lazy('productos:listado_paletas')
    fields = ['modelo', 'marca', 'fecha']

class EliminarPaleta(LoginRequiredMixin, DeleteView):
    model = Paleta
    template_name = "productos/eliminar_paleta.html"
    success_url = reverse_lazy('productos:listado_paletas')
