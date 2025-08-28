from django.urls import path
from .views import (
    agregar_proyecto,
    editar_proyecto,
    eliminar_proyecto,
)

urlpatterns = [
    path('agregar/', agregar_proyecto, name='agregar_proyecto'),
    path('editar/<int:proyecto_id>/', editar_proyecto, name='editar_proyecto'),
    path('eliminar/<int:proyecto_id>/', eliminar_proyecto, name='eliminar_proyecto'),
]