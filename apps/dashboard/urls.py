from django.urls import path
from .views import *

urlpatterns = [
    path('proximosvencimientos/', proximos_vencimientos, name='proximosvencimientos'),
    path('ventasAClientes/', ventas_a_cliente, name='ventasAClientes'),
    path('produccionesDeUnMes/', producciones_de_un_mes, name='produccionesDeUnMes'),
    
]