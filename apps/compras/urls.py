from django.urls import path
from .views import CreateProveedor, CreateIngrediente, CreateCompra, ListarIngrediente, listarProveedor, ListarCompra

urlpatterns = [
    path('crear_proveedor/', CreateProveedor.as_view(), name='crear_proveedor'),
    path('crear_ingrediente/', CreateIngrediente.as_view(), name='crear_ingrediente'),
    path('crear_compra/', CreateCompra.as_view(), name='crear_compra'),
    path('listar_ingrediente/',ListarIngrediente.as_view(), name='listar_ingrediente'),
    path('listar_proveedor/',listarProveedor.as_view(), name='listar_proveedor'),
    path('listar_compra/',ListarCompra.as_view(), name='listar_compra'),
]