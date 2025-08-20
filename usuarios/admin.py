from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(DjangoUserAdmin):
    #Cuando se edita el usuario
    fieldsets = DjangoUserAdmin.fieldsets + (
        ('Información Adicional', {'fields': ('descripcion', 'foto_perfil')}),
    )

    #Cuando se crea un nuevo usuario
    add_fieldsets = DjangoUserAdmin.add_fieldsets + (
        ('Información Adicional', {'fields': ('descripcion', 'foto_perfil')}),
    )