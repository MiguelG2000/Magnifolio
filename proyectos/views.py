from lib2to3.fixes.fix_input import context

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from django.contrib import messages
from .forms import ProyectoForm, FotoProyectoForm
from .models import Proyecto, FotoProyecto

@login_required
def agregar_proyecto(request):
    FotoFormSet = modelformset_factory(FotoProyecto, form=FotoProyectoForm, extra=1)

    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        formset = FotoFormSet(request.POST, request.FILES, queryset=FotoProyecto.objects.none())

        if form.is_valid() and formset.is_valid():
            proyecto = form.save(commit=False)
            proyecto.usuario = request.user
            proyecto.save()

            for foto_form in formset.cleaned_data:
                if foto_form:
                    imagen = foto_form['imagen']
                    FotoProyecto.objects.create(proyecto=proyecto, imagen=imagen)

            return redirect('mi_portafolio')
    else:
        form = ProyectoForm()
        formset = FotoFormSet(queryset=FotoProyecto.objects.none())

    context = {
        'form': form,
        'formset': formset
    }
    return render(request, 'agregar_proyecto.html', context)

@login_required
def editar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, proyecto_id=proyecto_id, usuario=request.user)
    FotoFormSet = modelformset_factory(FotoProyecto, form=FotoProyectoForm, extra=1, can_delete=True)

    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        formset = FotoFormSet(request.POST, request.FILES, queryset=FotoProyecto.objects.filter(proyecto=proyecto))

        if form.is_valid() and formset.is_valid():
            form.save()

            for foto_form in formset:
                if foto_form.cleaned_data.get('DELETE'):
                    if foto_form.instance.pk:
                        foto_form.instance.delete()
                elif foto_form.cleaned_data.get('imagen'):
                    foto_form.save(commit=False)
                    foto_form.instance.proyecto = proyecto
                    foto_form.save()

            return redirect('mi_portafolio')
    else:
        form = ProyectoForm(instance=proyecto)
        formset = FotoFormSet(queryset=FotoProyecto.objects.filter(proyecto=proyecto))

    context = {
        'form': form,
        'formset': formset
    }
    return render(request, 'agregar_proyecto.html', context)

@login_required
def eliminar_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, proyecto_id=proyecto_id, usuario=request.user)

    if request.method == 'POST':
        proyecto.delete()
        messages.success(request, "Proyecto eliminado correctamente.")
        return redirect('mi_portafolio')

    context = {
        'proyecto': proyecto
    }

    return render(request, 'eliminar_proyecto.html', context)