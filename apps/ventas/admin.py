from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.
class AdminCliente(admin.ModelAdmin):

    fields = ('razon_social','ciudad','telefono', 'email','direccion','cuit','situacion_frente_iva', 'comentarios')
    list_display = ('razon_social','ciudad','telefono', 'email','direccion','cuit','situacion_frente_iva', 'comentarios')
    list_display_links = list_display

class AdminSituacion(admin.ModelAdmin):

    fields = ('codigo','descripcion')
    list_display = ('codigo','descripcion')
    list_display_links = list_display

class AdminFormadePago(admin.ModelAdmin):

    fields = ('codigo','descripcion')
    list_display = ('codigo','descripcion')
    list_display_links = list_display

admin.site.register(Cliente,AdminCliente)
admin.site.register(Situacion_frente_iva,AdminSituacion)
admin.site.register(Forma_de_pago,AdminFormadePago)
