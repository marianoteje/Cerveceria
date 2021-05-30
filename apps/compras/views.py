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
    queryset = Compra.objects.filter(activa = True).order_by('-id')
    context_object_name = 'compras'
    template_name = 'listar_compra.html'


class listarProveedorFull(ListView):
    model = Proveedor
    queryset = Proveedor.objects.all()
    context_object_name = 'proveedores'
    template_name = 'listar_proveedor.html'

class ListarIngredienteFull(ListView):
    model = Ingrediente
    queryset = Ingrediente.objects.all()
    context_object_name = 'ingredientes'
    template_name = 'listar_ingrediente.html'

class ListarCompraFull(ListView):
    model = Compra
    queryset = Compra.objects.all().order_by('-id')
    context_object_name = 'compras'
    template_name = 'listar_compra.html'
class listarProveedorNoActivos(ListView):
    model = Proveedor
    context_object_name = 'proveedores'
    template_name = 'listar_proveedor.html'

class editarProveedor(UpdateView):
    model = Proveedor
    form_class = ProveedorForm
    template_name = 'editar_proveedor.html'
    success_url = reverse_lazy('compras:listar_proveedor')

class editarIngrediente(UpdateView):
    model = Ingrediente
    form_class = IngredienteForm
    template_name = 'editar_ingrediente.html'
    success_url = reverse_lazy('compras:listar_ingrediente')

class editarCompra(UpdateView):
    model = Compra
    form_class = CompraForm
    template_name = 'editar_compra.html'
    success_url = reverse_lazy('compras:listar_compra')
  
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


class reactivarCompra(DeleteView):
    model = Compra
    template_name = 'reactivar_compra.html'

    def post(self, request, pk, *args, **kwargs):
        object = Compra.objects.get (id = pk)
        object.activa = True
        object.save()
        return redirect('compras:listar_compra')



class reactivarIngrediente(DeleteView):
    model = Ingrediente
    template_name = 'reactivar_ingrediente.html'

    def post(self, request, pk, *args, **kwargs):
        object = Ingrediente.objects.get (id = pk)
        object.activo = True
        object.save()
        return redirect('compras:listar_ingrediente')


class reactivarProveedor(DeleteView):
    model = Proveedor
    template_name = 'reactivar_proveedor.html'

    def post(self, request, pk, *args, **kwargs):
        object = Proveedor.objects.get (id = pk)
        object.activo = True
        object.save()
        return redirect('compras:listar_proveedor')