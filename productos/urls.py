from    django.urls import path
from productos import views

app_name= 'productos'

urlpatterns = [
    path('notebooks/crear/', views.CrearNotebook.as_view(), name='crear_notebook'),
    path('notebooks/', views.ListadoNotebooks.as_view(), name='listado_notebooks'),
    path('notebooks/<int:pk>/', views.VerNotebook.as_view(), name='ver_notebook'),
    path('notebooks/<int:pk>/editar/', views.EditarNotebook.as_view(), name='editar_notebook'),
    path('notebooks/<int:pk>/eliminar/', views.EliminarNotebook.as_view(), name='eliminar_notebook'),
    path('computadoras/crear/', views.CrearComputadora.as_view(), name='crear_computadora'),
    path('computadoras/', views.ListadoComputadoras.as_view(), name='listado_computadoras'),
    path('computadoras/<int:pk>/', views.VerComputadora.as_view(), name='ver_computadora'),
    path('computadoras/<int:pk>/editar/', views.EditarComputadora.as_view(), name='editar_computadora'),
    path('computadoras/<int:pk>/eliminar/', views.EliminarComputadora.as_view(), name='eliminar_computadora'),
    
]