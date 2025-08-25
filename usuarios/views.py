import base64
from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import UsuarioForm

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
    usuario = request.user  # El usuario autenticado

    if request.method == "POST":
        form = UsuarioForm(request.POST, request.FILES, instance=usuario)

        if form.is_valid():
            usuario = form.save(commit=False)

            # 🔹 Manejo de imagen recortada
            cropped_data = request.POST.get("foto_perfil_cropped")
            if cropped_data:
                try:
                    format, imgstr = cropped_data.split(";base64,")
                    ext = format.split("/")[-1]
                    file_name = f"{usuario.username}_perfil.{ext}"
                    usuario.foto_perfil.save(
                        file_name,
                        ContentFile(base64.b64decode(imgstr)),
                        save=True
                    )
                except Exception as e:
                    messages.error(request, f"Error al procesar la imagen: {str(e)}")

            usuario.save()
            messages.success(request, "Tu perfil se actualizó correctamente ✅")
            return redirect(reverse_lazy('mi_perfil'))
        else:
            # Si el formulario no es válido, mostrar errores
            errors = form.errors.as_data()
            error_messages = []
            for field, error_list in errors.items():
                for error in error_list:
                    error_messages.append(f"{field}: {error.message}")
            messages.error(request, "\n".join(error_messages))
    else:
        form = UsuarioForm(instance=usuario)

    context = {
        "user": usuario,
        "form": form
    }
    return render(request, 'mi_perfil.html', context)