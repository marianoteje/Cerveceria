from django.urls import path
from .views import *

urlpatterns = [
    path('crear_cliente/', CreateCliente.as_view(), name='crear_cliente'),
]