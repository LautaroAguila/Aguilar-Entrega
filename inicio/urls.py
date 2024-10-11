from django.urls import path
from inicio.views import *

app_name = 'inicio'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('buscar-computadora/', buscar_computadora , name='buscar_computadora'),
    path('crear-computadora/', crear_computadora , name='crear_computadora'),
]