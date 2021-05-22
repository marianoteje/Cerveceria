from django.urls import path
from .views import *

urlpatterns = [
    path('crear_cliente/', CreateCliente.as_view(), name='crear_cliente'),
    path('listar_cliente/', ListarCliente.as_view(), name='listar_cliente'),
    path('listar_cliente_full/', ListarClienteFull.as_view(), name='listar_cliente_full'),
    path('editar_cliente/<int:pk>', EditarCliente.as_view(), name='editar_cliente'),
    path('eliminar_cliente/<int:pk>', eliminarCliente.as_view(), name='eliminar_cliente'),
    path('crear_venta/', CreateVenta.as_view(), name='crear_venta'),
    path('listar_venta/', ListarVenta.as_view(), name='listar_venta'),
    path('listar_venta_full/', ListarVentaFull.as_view(), name='listar_venta_full'),
    path('eliminar_venta/<int:pk>', EliminarVenta.as_view(), name='eliminar_venta'),
    path('editar_venta/<int:pk>', EditarVenta.as_view(), name='editar_venta'),
    path('reactivar_cliente/<int:pk>', reactivarCliente.as_view(), name='reactivar_cliente'),
    
]