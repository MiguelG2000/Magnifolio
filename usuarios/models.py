from django.db import models

# Create your models here.
class Usuario(models.Model):
    usuario_id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    descripcion = models.TextField(max_length=300, null=False)
    foto_perfil = models.ImageField(upload_to='fotos/', null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} - {self.apellido}"