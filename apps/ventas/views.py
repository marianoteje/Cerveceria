from django.shortcuts import render
from django.views.generic import CreateView, ListView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms.form_cliente import ClientesForm
from .models import Cliente

# Create your views here.

class CreateCliente(CreateView):
    model = Cliente
    form_class = ClientesForm
    template_name = 'crear_cliente.html'
    success_url = reverse_lazy('ventas:crear_cliente')