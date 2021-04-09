from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, TemplateView
from django.urls import reverse_lazy
from .forms.form_barril import BarrilForm
from .forms.form_fermentado import FermentadoForm
from .forms.form_produccion import ProduccionForm
from .models import Produccion, Barril, Fermentado, Lote


class CreateBarril(CreateView):
    model = Barril
    form_class = BarrilForm
    template_name = 'crear_barril.html'
    success_url = reverse_lazy('produccion:crear_barril')

class CreateFermentado(CreateView):
    model = Fermentado
    form_class = FermentadoForm
    template_name = 'crear_fermentado.html'
    success_url = reverse_lazy('produccion:crear_fermentado')

class CreateProduccion(CreateView):
    model = Produccion
    form_class = ProduccionForm
    template_name = 'crear_produccion.html'
    success_url = reverse_lazy('produccion:crear_produccion')

class listarBarril(ListView):
    model = Barril
    queryset = Barril.objects.filter(activo = True)
    context_object_name = 'barriles'
    template_name = 'listar_barril.html'
class listarFermentado(ListView):
    model = Fermentado
    queryset = Fermentado.objects.filter(activo = True)
    context_object_name = 'fermentados'
    template_name = 'listar_fermentado.html'

class listarProduccion(ListView):
    model = Produccion
    queryset = Produccion.objects.filter(activo = True)
    context_object_name = 'producciones'
    template_name = 'listar_produccion.html'