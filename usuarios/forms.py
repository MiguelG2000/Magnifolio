from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
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

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Correo electrónico')
    first_name = forms.CharField(max_length=30, required=True, label='Nombre')
    last_name = forms.CharField(max_length=30, required=True, label='Apellido')

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
            grupo_usuarios, created = Group.objects.get_or_create(name='usuarios')
            user.groups.add(grupo_usuarios)

        return user