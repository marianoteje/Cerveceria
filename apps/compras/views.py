from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, TemplateView, UpdateView, DeleteView
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

class listarProveedorNoActivos(ListView):
    model = Proveedor
    context_object_name = 'proveedores'
    template_name = 'listar_proveedor.html'

class ListarIngredienteNoActivos(ListView):
    model = Ingrediente
    context_object_name = 'ingredientes'
    template_name = 'listar_ingrediente.html'

class ListarCompraNoActivos(ListView):
    model = Compra
    context_object_name = 'compras'
    template_name = 'listar_compra.html'

class editarProveedor(UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'editar_proveedor.html'
    success_url = reverse_lazy('compras:listar_proveedor')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proveedor'] = Proveedor.objects.filter(activo= True)
        return context

class editarIngrediente(UpdateView):
    model = Ingrediente
    form_class = IngredienteForm
    template_name = 'editar_ingrediente.html'
    success_url = reverse_lazy('compras:listar_ingrediente')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ingrediente'] = Ingrediente.objects.filter(activo= True)
        return context


class editarCompra(UpdateView):
    model = Compra
    form_class = CompraForm
    template_name = 'editar_compra.html'
    success_url = reverse_lazy('compras:listar_compra')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['compra'] = Compra.objects.filter(activa= True)
        return context


class eliminarCompra(DeleteView):
    model = Compra
    template_name = 'eliminar_compra.html'

    def post(self, request, pk, *args, **kwargs):
        object = Compra.objects.get (id = pk)
        object.activa = False
        object.save()
        return redirect('compras:listar_compra')



class eliminarIngrediente(DeleteView):
    model = Ingrediente
    template_name = 'eliminar_ingrediente.html'

    def post(self, request, pk, *args, **kwargs):
        object = Ingrediente.objects.get (id = pk)
        object.activo = False
        object.save()
        return redirect('compras:listar_ingrediente')


class eliminarProveedor(DeleteView):
    model = Proveedor
    template_name = 'eliminar_proveedor.html'

    def post(self, request, pk, *args, **kwargs):
        object = Proveedor.objects.get (id = pk)
        object.activo = False
        object.save()
        return redirect('compras:listar_proveedor')