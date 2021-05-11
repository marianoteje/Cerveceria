from django.urls import path
from .views import *

urlpatterns = [
    path('crear_proveedor/', CreateProveedor.as_view(), name='crear_proveedor'),
    path('crear_ingrediente/', CreateIngrediente.as_view(), name='crear_ingrediente'),
    path('crear_compra/', CreateCompra.as_view(), name='crear_compra'),
    path('listar_ingrediente/',ListarIngrediente.as_view(), name='listar_ingrediente'),
    path('listar_proveedor/',listarProveedor.as_view(), name='listar_proveedor'),
    path('listar_compra/',ListarCompra.as_view(), name='listar_compra'),
    path('listar_ingrediente_full/',ListarIngredienteFull.as_view(), name='listar_ingrediente_full'),
    path('listar_proveedor_full/',listarProveedorFull.as_view(), name='listar_proveedor_full'),
    path('listar_compra_full/',ListarCompraFull.as_view(), name='listar_compra_full'),
    path('editar_proveedor/<int:pk>', editarProveedor.as_view(), name='editar_proveedor'),
    path('editar_ingrediente/<int:pk>', editarIngrediente.as_view(), name='editar_ingrediente'),
    path('editar_compra/<int:pk>', editarCompra.as_view(), name='editar_compra'),
    path('eliminar_compra/<int:pk>', eliminarCompra.as_view(), name='eliminar_compra'),
    path('eliminar_ingrediente/<int:pk>', eliminarIngrediente.as_view(), name='eliminar_ingrediente'),
    path('eliminar_proveedor/<int:pk>', eliminarProveedor.as_view(), name='eliminar_proveedor')
]