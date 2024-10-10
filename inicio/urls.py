from django.urls import path
from inicio.views import *

app_name = 'inicio'

urlpatterns = [
    path('mi-vista/', mi_vista, name='mi_vista'),
    path('', inicio, name='inicio'),
    path('primer-template/', primer_template, name='primer_template'),
    path('segundo-template/', segundo_template, name='segundo_template'),
    path('crear-computadora-correcta/<str:cpu>/<str:gpu>/<int:ram>/', crear_computadora_correcta , name='crear_computadora_correcta'),
    path('buscar-computadora/', buscar_computadora , name='buscar_computadora'),
    path('crear-computadora/', crear_computadora , name='crear_computadora'),
]