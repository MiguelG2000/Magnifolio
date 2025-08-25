from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import PerfilForm

from usuarios.models import Usuario


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            messages.error(request, "Por favor, complete todos los campos.")
            return redirect("login")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, f"¡Bienvenido {user.username}!")
            return redirect("index")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
            return redirect("login")

    return render(request, "login.html")

def usuario_logout(request):
    logout(request)
    messages.success(request, "Has cerrado sesión correctamente.")
    return redirect("index")

def index(request):
    return render(request, "index.html")

def lista_portafolios(request):
    usuarios = Usuario.objects.filter(visible=True)
    context = {
        "usuarios": usuarios,
    }
    return render(request, 'index.html', context)

@login_required
def mi_perfil(request):
    return render(request, 'mi_perfil.html')