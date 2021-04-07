from django.urls import path
from .views import CreateBarril, CreateFermentado

urlpatterns = [
    path('crear_barril/', CreateBarril.as_view(), name='crear_barril'),
    path('crear_fermentado/', CreateFermentado.as_view(), name='crear_fermentado')
]