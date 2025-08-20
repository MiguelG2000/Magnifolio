from django.urls import path
from .views import (
    login,
    usuario_logout,
    index
)

urlpatterns = [
    path("", login, name="login"),
    path("logout/", usuario_logout, name="logout"),
    path("home/", index, name="index"),
]
