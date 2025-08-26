from django.urls import path
from .views import agregar_proyecto

urlpatterns = [
    path('agregar/', agregar_proyecto, name='agregar_proyecto'),
]