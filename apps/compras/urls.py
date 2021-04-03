from django.urls import path
from .views import CreateProveedor
from .views import CreateIngrediente
from .views import CreateCompra


urlpatterns = [
    path('crear_proveedor/', CreateProveedor.as_view(), name='crear_proveedor'),
    path('crear_ingrediente/', CreateIngrediente.as_view(), name='crear_ingrediente'),
    path('crear_compra/', CreateCompra.as_view(), name='crear_compra'),
    
]