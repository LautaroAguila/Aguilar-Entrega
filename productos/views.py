from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *
from productos.models import Notebook, Computadora
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class CrearNotebook(LoginRequiredMixin, CreateView):
    model = Notebook
    template_name = "productos/notebook/crear_notebook.html"
    success_url = reverse_lazy('productos:listado_notebooks')
    fields = ['modelo', 'marca', 'fecha', 'imagen']

class ListadoNotebooks(ListView):
    model = Notebook
    template_name = "productos/notebook/listado_notebooks.html"
    context_object_name = 'notebooks'

class VerNotebook(DetailView):
    model = Notebook
    template_name = "productos/notebook/ver_notebook.html"

class EditarNotebook(LoginRequiredMixin, UpdateView):
    model = Notebook
    template_name = "productos/notebook/editar_notebook.html"
    success_url = reverse_lazy('productos:listado_notebooks')
    fields = ['modelo', 'marca', 'fecha', 'imagen']

class EliminarNotebook(LoginRequiredMixin, DeleteView):
    model = Notebook
    template_name = "productos/notebook/eliminar_notebook.html"
    success_url = reverse_lazy('productos:listado_notebooks')

class CrearComputadora(LoginRequiredMixin, CreateView):
    model = Computadora
    template_name = "productos/computadora/crear_computadora.html"
    success_url = reverse_lazy('productos:listado_computadoras')
    fields = ['nombre', 'cpu', 'gpu', 'ram', 'imagen']

class ListadoComputadoras(ListView):
    model = Computadora
    template_name = "productos/computadora/listado_computadoras.html"
    context_object_name = 'computadoras'

class VerComputadora(DetailView):
    model = Computadora
    template_name = "productos/computadora/ver_computadora.html"

class EditarComputadora(LoginRequiredMixin, UpdateView):
    model = Computadora
    template_name = "productos/computadora/editar_computadora.html"
    success_url = reverse_lazy('productos:listado_computadoras')
    fields = ['nombre', 'cpu', 'gpu', 'ram', 'imagen']

class EliminarComputadora(LoginRequiredMixin, DeleteView):
    model = Computadora
    template_name = "productos/computadora/eliminar_computadora.html"
    success_url = reverse_lazy('productos:listado_computadoras')
