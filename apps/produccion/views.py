from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, TemplateView, FormView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.forms.models import formset_factory
from .forms.form_barril import BarrilForm
from .forms.form_fermentado import FermentadoForm
from .forms.form_produccion import ProduccionForm
from .forms.form_lote import LoteForm
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
    success_url = reverse_lazy('produccion:listar_fermentado')

class CreateProduccion(CreateView):
    model = Produccion
    form_class = ProduccionForm
    template_name = 'crear_produccion.html'
    success_url = reverse_lazy('produccion:crear_produccion')

class CreateLote(CreateView):
    model = Lote
    form_class = LoteForm
    template_name = 'crear_lote.html'
    success_url = reverse_lazy('produccion:crear_lote')
class listarBarril(ListView):
    model = Barril
    queryset = Barril.objects.filter(activo = True)
    context_object_name = 'barriles'
    template_name = 'listar_barril.html'

class listarBarrilFull(ListView):
    model = Barril
    queryset = Barril.objects.all()
    context_object_name = 'barriles'
    template_name = 'listar_barril.html'
class listarFermentado(ListView):
    model = Fermentado
    queryset = Fermentado.objects.filter(activo = True).order_by('-id')
    context_object_name = 'fermentados'
    template_name = 'listar_fermentado.html'

class listarFermentadoFull(ListView):
    model = Fermentado
    queryset = Fermentado.objects.all().order_by('-id')
    context_object_name = 'fermentados'
    template_name = 'listar_fermentado.html'

class listarProduccion(ListView):
    model = Produccion
    queryset = Produccion.objects.filter(activo = True)
    context_object_name = 'producciones'
    template_name = 'listar_produccion.html'


class listarProduccionFull(ListView):
    model = Produccion
    queryset = Produccion.objects.all()
    context_object_name = 'producciones'
    template_name = 'listar_produccion.html'

class listarLote(ListView):
    model = Lote
    queryset = Lote.objects.filter(activo = True).order_by('-id')
    context_object_name = 'lotes'
    template_name = 'listar_lote.html'

class listarLoteFull(ListView):
    model = Lote
    queryset = Lote.objects.all().order_by('-id')
    context_object_name = 'lotes'
    template_name = 'listar_lote.html'
class editarBarril(UpdateView):
    model = Barril
    form_class = BarrilForm
    template_name = 'editar_barril.html'
    success_url = reverse_lazy('produccion:listar_barril')

        
class editarFermentado(UpdateView):
    model = Fermentado
    form_class = FermentadoForm
    template_name = 'editar_fermentado.html'
    success_url = reverse_lazy('produccion:listar_fermentado')
        
class editarProduccion(UpdateView):
    model = Produccion
    form_class = ProduccionForm
    template_name = 'editar_produccion.html'
    success_url = reverse_lazy('produccion:listar_produccion')

class editarLote(UpdateView):
    model = Lote
    form_class = LoteForm
    template_name = 'editar_lote.html'
    success_url = reverse_lazy('produccion:listar_lote')

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



class eliminarProduccion(DeleteView):
    model = Produccion
    template_name = 'eliminar_produccion.html'

    def post(self, request, pk, *args, **kwargs):
        object = Produccion.objects.get (id = pk)
        object.activo = False
        object.save()
        return redirect('produccion:listar_produccion')


class eliminarLote(DeleteView):
    model = Lote
    template_name = 'eliminar_lote.html'

    def post(self, request, pk, *args, **kwargs):
        object = Lote.objects.get (id = pk)
        object.activo = False
        object.save()
        return redirect('produccion:listar_lote')


class reactivarBarril(DeleteView):
    model = Barril
    template_name = 'reactivar_barril.html'

    def post(self, request, pk, *args, **kwargs):
        object = Barril.objects.get (id = pk)
        object.activo = True
        object.save()
        return redirect('produccion:listar_barril')

class reactivarFermentado(DeleteView):
    model = Fermentado
    template_name = 'reactivar_fermentado.html'

    def post(self, request, pk, *args, **kwargs):
        object = Fermentado.objects.get (id = pk)
        object.activo = True
        object.save()
        return redirect('produccion:listar_fermentado')



class reactivarProduccion(DeleteView):
    model = Produccion
    template_name = 'reactivar_produccion.html'

    def post(self, request, pk, *args, **kwargs):
        object = Produccion.objects.get (id = pk)
        object.activo = True
        object.save()
        return redirect('produccion:listar_produccion')


class reactivarLote(DeleteView):
    model = Lote
    template_name = 'reactivar_lote.html'

    def post(self, request, pk, *args, **kwargs):
        object = Lote.objects.get (id = pk)
        object.activo = True
        object.save()
        return redirect('produccion:listar_lote')