from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    login,
    usuario_logout,
    index,
    mi_perfil,
    editar_perfil,
    usuario_registro,
    mi_portafolio,
    portafolio,
    terminos,
    acerca_mi
)

urlpatterns = [
    path("login/", login, name="login"),
    path("logout/", usuario_logout, name="logout"),
    path("registro/", usuario_registro, name="registro"),
    path("", index, name="index"),
    path("mi_perfil/", mi_perfil, name="mi_perfil"),
    path("editar_perfil/", editar_perfil, name="editar_perfil"),
    path("mi_portafolio/", mi_portafolio, name="mi_portafolio"),
    path("portafolio/<str:username>/", portafolio, name="portafolio"),
    path("terminos/", terminos, name="terminos"),
    path("acerca_mi/", acerca_mi, name="acerca_mi"),
]
