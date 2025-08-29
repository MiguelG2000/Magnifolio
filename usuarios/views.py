import base64
from lib2to3.fixes.fix_input import context

from django.core.files.base import ContentFile
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .forms import UsuarioForm, RegistroForm

from usuarios.models import Usuario
from proyectos.models import Proyecto

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
    usuarios_list = Usuario.objects.filter(visible=True)
    paginator = Paginator(usuarios_list, 5)

    page_number = request.GET.get('page')
    usuarios = paginator.get_page(page_number)
    context = {
        "usuarios": usuarios,
    }
    return render(request, "index.html", context)

@login_required
def mi_perfil(request):
    return render(request, 'mi_perfil.html')

@login_required
def editar_perfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UsuarioForm(request.POST, request.FILES, instance=usuario)

        if form.is_valid():
            usuario = form.save(commit=False)

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
            errors = form.errors.as_data()
            error_messages = []
            for field, error_list in errors.items():
                for error in error_list:
                    error_messages.append(f"{field}: {error.message}")
            messages.error(request, "\n".join(error_messages))
    else:
        form = UsuarioForm(instance=usuario)

    context = {
        "form": form
    }
    return render(request, 'editar_perfil.html', context)

def usuario_registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Usuario creado exitosamente.')
            return redirect('login')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = RegistroForm()

    context = {
        'form': form
    }
    return render(request, 'registro.html', context)

#-------------------------------------------------------------------------------------------------------
@login_required
def lista_portafolios(request):
    usuarios = Usuario.objects.filter(visible=True)
    context = {
        "usuarios": usuarios,
    }
    return render(request, 'index.html', context)

@login_required
def mi_portafolio(request):
    proyectos = Proyecto.objects.filter(usuario = request.user)
    context = {
        "proyectos": proyectos,
    }
    return render(request, 'proyectos.html', context)


def portafolio(request, username):
    usuario = get_object_or_404(Usuario, username=username)
    proyectos = usuario.proyectos.all()
    context = {
        "usuario": usuario,
        "proyectos": proyectos,
    }
    return render(request, 'portafolio.html', context)

def terminos(request):
    return render(request, 'terminos.html')

def acerca_mi(request):
    return render(request, 'acerca_mi.html')