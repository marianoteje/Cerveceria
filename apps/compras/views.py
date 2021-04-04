from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, TemplateView
from django.urls import reverse_lazy
from .forms.form_proveedor import ProveedorForm
from .forms.form_ingredientes import IngredienteForm
from .forms.form_compra import CompraForm
from .models import Proveedor,Ingrediente, Compra

class Home(TemplateView):
    template_name = 'index.html'
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


class CreateCompra(CreateView):
    model = Compra
    form_class = CompraForm
    template_name = 'crear_compra.html'
    success_url = reverse_lazy('compras:crear_compra')


class listarProveedor(ListView):
    model = Proveedor
    queryset = Proveedor.objects.filter(activo = True)
    context_object_name = 'proveedores'
    template_name = 'listar_proveedor.html'

class ListarIngrediente(ListView):
    model = Ingrediente
    queryset = Ingrediente.objects.filter(activo = True)
    context_object_name = 'ingredientes'
    template_name = 'listar_ingrediente.html'

class ListarCompra(ListView):
    model = Compra
    queryset = Compra.objects.filter(activa = True)
    context_object_name = 'compras'
    template_name = 'listar_compra.html'
