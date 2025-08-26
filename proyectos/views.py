from lib2to3.fixes.fix_input import context

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.forms import modelformset_factory
from .forms import ProyectoForm, FotoProyectoForm
from .models import Proyecto, FotoProyecto

@login_required
def agregar_proyecto(request):
    FotoFormSet = modelformset_factory(FotoProyecto, form=FotoProyectoForm, extra=3)

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