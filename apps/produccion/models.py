from django.db import models
from apps.compras.models import Ingrediente
from Validaciones.validaciones import *

class Barril (models.Model):
    codigo = models.IntegerField(null=False, blank=True)
    capacidad = models.IntegerField(null=False, blank=True, default= '0')
    activo = models.BooleanField(default=True)
    


class Produccion (models.Model):
    #agregue el campo descripcion 
    descripcion = models.TextField(null=False, blank=True, default='sin descripcion')
    fecha_produccion = models.DateTimeField(null=False, blank=False, verbose_name='Fecha')
    cantidad_agua = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Litros de agua usados')
    temperatura_maceracion = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Temperatura de macerado')
    #agregue el campo tiempo macerado
    tiempo_maceracion = models.DurationField(verbose_name='Tiempo maceracion')
    #tiempo_maceracion = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Tiempo de macerado')
    temperatura_coccion = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Temperatura cocción')
    tiempo_coccion = models.DurationField(verbose_name='Tiempo de cocción')
    #tiempo_coccion = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Tiempo de cocción')
    ingredientes = models.ManyToManyField(Ingrediente,through='Ingrediente_Produccion')
    activo = models.BooleanField(default=True)

    def __str__(self):
       return self.descripcion

class Ingrediente_Produccion(models.Model):
    ingrediente = models.ForeignKey(Ingrediente, null=False, blank=False, default=0, on_delete=models.PROTECT)
    produccion = models.ForeignKey(Produccion, null=False, blank=False, default=0, on_delete=models.PROTECT)
    cantidad = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Cantidad de ingredientes usados')

    def __str__(self):
       return self.cantidad

class Fermentado (models.Model):
    fecha_inicio = models.DateTimeField(null=False, blank=False, verbose_name='Fecha inicio')
    fecha_fin = models.DateTimeField(null=False, blank=False, verbose_name='Fecha fin')
    litros_entrada = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name='Litros de entrada')
    litros_salida = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name='Litros de salida')
    activo = models.BooleanField(default=True)
    produccion = models.ForeignKey(Produccion, null=False, blank=False, default=0, on_delete=models.PROTECT)

class Lote (models.Model):
    fecha_llenado = models.DateTimeField(null=False, blank=False)
    fecha_carbonatado = models.DateTimeField(null=False, blank=False)
    barriles = models.ManyToManyField(Barril)
    id_produccion = models.ForeignKey(Produccion, on_delete=models.PROTECT, verbose_name='Produccion')
    activo = models.BooleanField(default=True)







