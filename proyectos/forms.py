from django import forms
from django.forms import modelformset_factory
from .models import Proyecto, FotoProyecto

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['titulo', 'descripcion', 'link_repo']
        widgets = {
            'titulo': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Título del proyecto'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500',
                'rows': 4,
                'placeholder': 'Descripción del proyecto'
            }),
            'link_repo': forms.URLInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500',
                'placeholder': 'URL del repositorio (opcional)'
            }),
        }

class FotoProyectoForm(forms.ModelForm):
    class Meta:
        model = FotoProyecto
        fields = ['imagen']
        widgets = {
            'imagen': forms.ClearableFileInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500',
            }),
        }

FotoProyectoFormSet = modelformset_factory(
    FotoProyecto,
    form=FotoProyectoForm,
    extra=1,
    can_delete=False
)
