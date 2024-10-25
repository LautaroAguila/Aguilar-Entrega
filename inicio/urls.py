from django.urls import path
from inicio.views import *

app_name = 'inicio'

urlpatterns = [
    path('', inicio, name='inicio'),
    path('about/', about , name='about'),
]