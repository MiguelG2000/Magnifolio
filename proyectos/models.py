from django.db import models
from usuarios.models import Usuario

# Create your models here.
class Proyecto(models.Model):
    proyecto_id = models.AutoField(primary_key=True, unique=True)
    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.CASCADE,
        related_name="proyectos"
    )
    titulo = models.CharField(max_length=100, null=False)
    descripcion = models.TextField(max_length=300, null=False)
    link_repo = models.URLField(null=True, blank=True)
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.titulo} ({self.usuario.first_name})"

class FotoProyecto(models.Model):
    proyecto = models.ForeignKey(
        Proyecto,
        on_delete=models.CASCADE,
        related_name='fotos'
    )
    imagen = models.ImageField(upload_to='proyectos/')

    def __str__(self):
        return f"Foto de {self.proyecto.titulo}"