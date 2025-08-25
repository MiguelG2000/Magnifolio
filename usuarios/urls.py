from django.urls import path
from .views import (
    login,
    usuario_logout,
    index,
    mi_perfil
)

urlpatterns = [
    path("login/", login, name="login"),
    path("logout/", usuario_logout, name="logout"),
    path("", index, name="index"),
    path("mi_perfil/", mi_perfil, name="mi_perfil"),
]
