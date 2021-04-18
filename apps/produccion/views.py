from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, TemplateView, FormView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms.models import formset_factory
from .forms.form_barril import BarrilForm
from .forms.form_fermentado import FermentadoForm
from .forms.form_produccion import ProduccionForm, IngredienteProduccionForm
from .models import Produccion, Barril, Fermentado, Lote


class CreateBarril(CreateView):
    model = Barril
    form_class = BarrilForm
    template_name = 'crear_barril.html'
    success_url = reverse_lazy('produccion:crear_barril')

class CreateFermentado(FormView):
   
    form_class = ProduccionForm
    ingredientes_formset = formset_factory(IngredienteProduccionForm)
    template_name = 'crear_fermentado.html'
    success_url = reverse_lazy('produccion:listar_fermentado')

class CreateProduccion(FormView):
    model = Produccion
    
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

class listarFermentadoPorFechaDesc(ListView):
    model = Fermentado
    queryset = Fermentado.objects.filter(activo = True).order_by('-fecha_inicio')
    context_object_name = 'fermentados'
    template_name = 'listar_fermentado.html'

class listarProduccion(ListView):
    model = Produccion
    queryset = Produccion.objects.filter(activo = True)
    context_object_name = 'producciones'
    template_name = 'listar_produccion.html'


class editarBarril(UpdateView):
    model = Barril
    form_class = BarrilForm
    template_name = 'editar_barril.html'
    success_url = reverse_lazy('produccion:listar_barril')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['barril'] = Barril.objects.filter(activo= True)
        return context
        
class editarFermentado(UpdateView):
    model = Fermentado
    form_class = FermentadoForm
    template_name = 'editar_fermentado.html'
    success_url = reverse_lazy('produccion:listar_fermentado')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['fermentado'] = Fermentado.objects.filter(activo= True)
        return context
        

class editarProduccion(UpdateView):
    model = Produccion
    form_class = ProduccionForm
    template_name = 'editar_produccion.html'
    success_url = reverse_lazy('produccion:listar_produccion')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['produccion'] = Produccion.objects.filter(activo= True)
        return context

class eliminarBarril(DeleteView):
    model = Barril
    template_name = 'eliminar_barril.html'

    def post(self, request, pk, *args, **kwargs):
        object = Barril.objects.get (id = pk)
        object.activo = False
        object.save()
        return redirect('produccion:listar_barril')


class eliminarFermentado(DeleteView):
    model = Fermentado
    template_name = 'eliminar_fermentado.html'

    def post(self, request, pk, *args, **kwargs):
        object = Fermentado.objects.get (id = pk)
        object.activo = False
        object.save()
        return redirect('produccion:listar_fermentado')