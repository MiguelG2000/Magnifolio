from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Usuario(AbstractUser):
    descripcion = models.TextField(max_length=300, null=True, blank=True)
    foto_perfil = models.ImageField(upload_to='fotos/', null=True, blank=True)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.username