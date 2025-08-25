from django import forms
from django.core.exceptions import ValidationError
from .models import Usuario


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['first_name', 'last_name', 'email', 'descripcion', 'foto_perfil', 'visible']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and Usuario.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise ValidationError("Este correo electrónico ya está en uso.")
        return email

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        if descripcion and len(descripcion) > 300:
            raise ValidationError("La descripción no puede superar los 300 caracteres.")
        return descripcion
