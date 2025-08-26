from django.urls import path
from .views import (
    login,
    usuario_logout,
    index,
    mi_perfil,
    editar_perfil
)

urlpatterns = [
    path("login/", login, name="login"),
    path("logout/", usuario_logout, name="logout"),
    path("", index, name="index"),
    path("mi_perfil/", mi_perfil, name="mi_perfil"),
    path("editar_perfil/", editar_perfil, name="editar_perfil"),
]
