from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms.form_proveedor import ProveedorForm
from .forms.form_ingredientes import IngredienteForm
from .models import Proveedor
from .models import Ingrediente


class CreateProveedor(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'crear_proveedor.html'
    success_url = reverse_lazy('compras:crear_proveedor')


class CreateIngrediente(CreateView):
    model = Ingrediente
    form_class = IngredienteForm
    template_name = 'crear_ingrediente.html'
    success_url = reverse_lazy('compras:crear_ingrediente')

   