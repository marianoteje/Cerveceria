from django.contrib import admin
from .models import *

# Register your models here.
class AdminIngrediente(admin.ModelAdmin):

    fields = ('nombre','stock', 'activo')
    list_display = ('id','nombre','stock', 'activo')
    list_display_links = list_display

class AdminProveedores(admin.ModelAdmin):

    fields = ('nombre','descripcion','telefono','email','direccion', 'activo')
    list_display = ('id','nombre','descripcion','telefono','email','direccion', 'activo')
    list_display_links = list_display

class AdminCompra(admin.ModelAdmin):

    fields = ('id_proveedor','id_ingrediente','costo','fecha_compra','fecha_vencimiento','cantidad','comentario', 'activa')
    list_display = ('id','id_proveedor','id_ingrediente','costo','fecha_compra','fecha_vencimiento','cantidad','comentario', 'activa')
    list_display_links = list_display



admin.site.register(Ingrediente,AdminIngrediente)
admin.site.register(Proveedor,AdminProveedores)
admin.site.register(Compra,AdminCompra)