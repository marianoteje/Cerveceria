from django.urls import path
from .views import *

urlpatterns = [
    path('crear_barril/', CreateBarril.as_view(), name='crear_barril'),
    path('crear_fermentado/', CreateFermentado.as_view(), name='crear_fermentado'),
    path('crear_produccion/', CreateProduccion.as_view(), name='crear_produccion'),
    path('crear_lote/', CreateLote.as_view(), name='crear_lote'),
    path('listar_fermentado/', listarFermentado.as_view(), name='listar_fermentado'),
    path('listar_barril/', listarBarril.as_view(), name='listar_barril'),
    path('listar_produccion/', listarProduccion.as_view(), name='listar_produccion'),
    path('listar_lote/', listarLote.as_view(), name='listar_lote'),
    path('editar_barril/<int:pk>', editarBarril.as_view(), name='editar_barril'),
    path('editar_fermentado/<int:pk>', editarFermentado.as_view(), name='editar_fermentado'),
    path('editar_produccion/<int:pk>', editarProduccion.as_view(), name='editar_produccion'),
    path('editar_lote/<int:pk>', editarLote.as_view(), name='editar_lote'),
    path('eliminar_barril/<int:pk>', eliminarBarril.as_view(), name='eliminar_barril'),
    path('eliminar_fermentado/<int:pk>', eliminarFermentado.as_view(), name='eliminar_fermentado'),
    path('eliminar_produccion/<int:pk>', eliminarProduccion.as_view(), name='eliminar_produccion'),
    path('eliminar_lote/<int:pk>', eliminarLote.as_view(), name='eliminar_lote'),
    
    
]