from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms.models import formset_factory
from .forms.form_cliente import ClientesForm
from .forms.form_venta import VentaForm
from .models import Cliente, Ventas

# Create your views here.

class CreateCliente(CreateView):
    model = Cliente
    form_class = ClientesForm
    template_name = 'crear_cliente.html'
    success_url = reverse_lazy('ventas:crear_cliente')


class ListarCliente(ListView):
    model = Cliente
    queryset = Cliente.objects.filter(activo = True)
    context_object_name = 'clientes'
    template_name = 'listar_cliente.html'

class ListarClienteFull(ListView):
    model = Cliente
    queryset = Cliente.objects.all()
    context_object_name = 'clientes'
    template_name = 'listar_cliente.html'

class EditarCliente(UpdateView):
    model = Cliente
    form_class = ClientesForm
    template_name = 'editar_cliente.html'
    success_url = reverse_lazy('ventas:listar_cliente')

    
class eliminarCliente(DeleteView):
    model = Cliente
    template_name = 'eliminar_cliente.html'

    def post(self, request, pk, *args, **kwargs):
        object = Cliente.objects.get (id = pk)
        object.activo = False
        object.save()
        return redirect('ventas:listar_cliente')
class CreateVenta(CreateView):
    model = Ventas
    form_class = VentaForm
    template_name = 'crear_venta.html'
    success_url = reverse_lazy('ventas:crear_venta')
class ListarVenta(ListView):
    model = Ventas
    queryset = Ventas.objects.filter(activo = True).order_by('-id')
    context_object_name = 'ventas'
    template_name = 'listar_ventas.html'

class ListarVentaFull(ListView):
    model = Ventas
    queryset = Ventas.objects.all().order_by('-id')
    context_object_name = 'ventas'
    template_name = 'listar_ventas.html'

class EliminarVenta(DeleteView):
    model = Ventas
    template_name = 'eliminar_venta.html'

    def post(self, request, pk, *args, **kwargs):
        object = Ventas.objects.get (id = pk)
        object.activo = False
        object.save()
        return redirect('ventas:listar_venta')

class EditarVenta(UpdateView):
    model = Ventas
    form_class = VentaForm
    template_name = 'editar_venta.html'
    success_url = reverse_lazy('ventas:listar_venta')


class reactivarCliente(DeleteView):
    model = Cliente
    template_name = 'reactivar_cliente.html'

    def post(self, request, pk, *args, **kwargs):
        object = Cliente.objects.get (id = pk)
        object.activo = True
        object.save()
        return redirect('ventas:listar_cliente')