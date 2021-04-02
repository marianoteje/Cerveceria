from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms.form_proveedor import ProveedorForm
from .models import Proveedor


class CreateProveedor(CreateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'crear_proveedor.html'
    success_url = reverse_lazy('compras:crear_proveedor')

   