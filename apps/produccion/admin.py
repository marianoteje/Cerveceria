from django.contrib import admin
from .models import *

# Register your models here.

class AdminBarril(admin.ModelAdmin):

    fields = ('codigo','capacidad')
    list_display = ('id','codigo','capacidad')
    list_display_links = list_display


class AdminFermentado(admin.ModelAdmin):

    fields=('fecha_inicio','fecha_fin','hora_inicio','hora_fin', 'litros_entrada','litros_salida','produccion')
    list_display = ('id','fecha_inicio','fecha_fin','hora_inicio','hora_fin','litros_entrada','litros_salida','produccion')


class AdminProduccion(admin.ModelAdmin):
    fields=('descripcion','fecha_produccion','cantidad_agua','temperatura_maceracion','tiempo_maceracion' ,'temperatura_coccion','tiempo_coccion')
    list_display = ('id','descripcion','fecha_produccion','cantidad_agua','temperatura_maceracion','tiempo_maceracion', 'temperatura_coccion','tiempo_coccion')
    list_display_links = list_display

class AdminLote(admin.ModelAdmin):
    fields=('fecha_llenado','fecha_carbonatado','barriles','id_produccion')
    list_display = ('id','fecha_llenado','fecha_carbonatado','id_produccion')
    list_display_links = list_display

admin.site.register(Barril,AdminBarril)
admin.site.register(Fermentado,AdminFermentado)
admin.site.register(Produccion,AdminProduccion)
admin.site.register(Lote,AdminLote)