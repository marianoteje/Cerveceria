from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, TemplateView
from django.urls import reverse_lazy
from .forms.form_barril import BarrilForm
from .forms.form_fermentado import FermentadoForm
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

    