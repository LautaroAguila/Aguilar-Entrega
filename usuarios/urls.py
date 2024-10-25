from django.urls import path
from usuarios import views
from django.contrib.auth.views import LogoutView
app_name = 'usuarios'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', LogoutView.as_view(template_name = 'usuarios/logout.html'), name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('perfil/password/', views.CambiarPassword.as_view(), name='cambiar_password'),
    path('chat/<int:usuario_id>/', views.chat, name='chat'),
]