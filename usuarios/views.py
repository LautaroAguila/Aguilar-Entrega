from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate, login as django_login
from usuarios.forms import FormularioDeCreacionDeUsuario, FormularioEdicionPerfil, MensajeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import DatosExtra, Mensaje
from django.contrib.auth.models import User

def login(request):

    formulario = AuthenticationForm()

    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST, data = request.POST)
        if formulario.is_valid():
            
            usuario = formulario.get_user()

            django_login(request, usuario)

            DatosExtra.objects.get_or_create(user=usuario)

            return redirect('inicio:inicio')
    return render(request, 'usuarios/login.html', {'form' : formulario})

def register (request):

    formulario = FormularioDeCreacionDeUsuario()

    if request.method == 'POST':
        formulario = FormularioDeCreacionDeUsuario(request.POST)
        if formulario.is_valid():
            
            formulario.save()
            return redirect('usuarios:login')
    return render(request, 'usuarios/register.html', {'form' : formulario})

@login_required
def editar_perfil(request):
    datos_extra = request.user.datosextra
    formulario = FormularioEdicionPerfil(instance=request.user, initial={'avatar': datos_extra.avatar})

    if request.method == 'POST':
        formulario = FormularioEdicionPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            
            new_avatar = formulario.cleaned_data.get('avatar')
            datos_extra.avatar = new_avatar if new_avatar else datos_extra.avatar

            #datos_extra.avatar = formulario.cleaned_data['avatar']
            datos_extra.save()

            formulario.save()
            return redirect('inicio:inicio')

    return render(request, 'usuarios/editar_perfil.html', {'form' : formulario})

@login_required
def perfil(request):
    return render(request, 'usuarios/perfil.html')
class CambiarPassword(LoginRequiredMixin, PasswordChangeView):
    
    template_name = 'usuarios/cambiar_password.html'

    success_url = reverse_lazy('usuarios:editar_perfil')


@login_required
def chat(request, usuario_id=None):
    if usuario_id:
        destinatario = User.objects.get(id=usuario_id)
        mensajes = Mensaje.objects.filter(
            remitente=request.user, destinatario=destinatario
        ) | Mensaje.objects.filter(
            remitente=destinatario, destinatario=request.user
        ).order_by('fecha')
    else:
        destinatario = None
        mensajes = None

    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.save()
            return redirect('usuarios:chat', usuario_id=mensaje.destinatario.id)
    else:
        form = MensajeForm()

    usuarios = User.objects.exclude(id=request.user.id)
    return render(request, 'chats/chat.html', {
        'form': form,
        'mensajes': mensajes,
        'destinatario': destinatario,
        'usuarios': usuarios,
    })

