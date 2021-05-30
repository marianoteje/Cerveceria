from django.http import request
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, TemplateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.compras.models import *
from apps.produccion.models import *
from apps.ventas.models import *
from datetime import datetime
from django.db.models import Sum

def proximos_vencimientos(request):
    model = Compra
    today = datetime.today()
    queryset = Compra.objects.all().filter(activa = True, fecha_vencimiento__gte = datetime.now(), id_ingrediente__stock__lte = 0.0 ).order_by('fecha_vencimiento')
    print(queryset)
    return render(request, 'proximos_vencimientos.html', {'compras': queryset})


def ventas_a_cliente(request):
    model = Cliente
    querysetClientes = Cliente.objects.filter(activo = True)
    querysetClienteSeleccionado = request.GET.get("buscar")
    if querysetClienteSeleccionado != '':
        queryset = Ventas.objects.all().filter(cliente = querysetClienteSeleccionado)
        return render(request, 'venta_a_cliente.html', {'clientes': querysetClientes,'ventas': queryset})
    else:
        return render(request, 'venta_a_cliente.html', {'clientes': querysetClientes})



def producciones_de_un_mes(request):
    model = Produccion
    querysetMes = request.GET.get("mes")
    querysetAño = request.GET.get("anio")
 
    print(querysetAño)
    
    if querysetMes != '' and querysetAño == '' : 
        querysetProducciones = Produccion.objects.all().filter(activo = True, fecha_produccion__month = querysetMes)
        return render(request, 'producciones_de_un_mes.html', {'producciones': querysetProducciones})
    if querysetMes != '' and querysetAño != '' : 
        querysetProducciones = Produccion.objects.all().filter(activo = True, fecha_produccion__month = querysetMes, fecha_produccion__year = querysetAño)
        return render(request, 'producciones_de_un_mes.html', {'producciones': querysetProducciones})
    if querysetMes == '' and querysetAño == '' : 
        return render(request, 'producciones_de_un_mes.html')