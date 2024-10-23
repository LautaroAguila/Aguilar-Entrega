from django.urls import path
from inicio.views import *

app_name = 'inicio'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('buscar-computadora/', buscar_computadora , name='buscar_computadora'),
    path('crear-computadora/', crear_computadora , name='crear_computadora'),
    path('ver-computadora/<int:id>/', ver_computadora , name='ver_computadora'),
    path('eliminar-computadora/<int:id>/', eliminar_computadora , name='eliminar_computadora'),
    path('editar-computadora/<int:id>/', editar_computadora , name='editar_computadora'),
    path('about/', about , name='about'),
]