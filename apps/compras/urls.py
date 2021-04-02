from django.urls import path
from .views import CreateProveedor


urlpatterns = [
    path('crear_proveedor/', CreateProveedor.as_view(), name='crear_proveedor'),
]