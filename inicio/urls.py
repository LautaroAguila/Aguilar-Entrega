from django.urls import path
from inicio.views import *

urlpatterns = [
    path('mi-vista/', mi_vista),
    path('', inicio),
    path('vista-datos1/<nombre>/', vista_datos1),
    path('primer-template/', primer_template),
    path('segundo-template/', segundo_template)
]