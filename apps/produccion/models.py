from django.db import models
from apps.compras.models import Ingrediente
from Validaciones.validaciones import *

class Barril (models.Model):
    codigo = models.CharField(max_length=100, null=False, blank=True)
    capacidad = models.IntegerField(null=False, blank=True, default= '0')
    activo = models.BooleanField(default=True)
    
    def __str__(self):
       return self.codigo

class Produccion (models.Model):
    
    descripcion = models.TextField(null=False, blank=True, default='sin descripcion')
    fecha_produccion = models.DateTimeField(null=False, blank=False, verbose_name='Fecha')
    cantidad_agua = models.DecimalField(max_digits=11, decimal_places=2, verbose_name='Litros de agua usados')
    temperatura_maceracion = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Temperatura de macerado')
    tiempo_maceracion = models.DurationField(verbose_name='Tiempo maceracion')
    temperatura_coccion = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Temperatura cocción')
    tiempo_coccion = models.DurationField(verbose_name='Tiempo de cocción')
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
    fecha_inicio = models.DateField(null=False, blank=False, verbose_name='Fecha inicio')
    hora_inicio = models.TimeField(default='00:00', null=False, blank=False, verbose_name='Hora inicio')
    fecha_fin = models.DateField(null=False, blank=False, verbose_name='Fecha Fin')
    hora_fin = models.TimeField(default='00:00', null=False, blank=False, verbose_name='Hora Fin')
    litros_entrada = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name='Litros de entrada')
    litros_salida = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name='Litros de salida')
    activo = models.BooleanField(default=True)
    produccion = models.ForeignKey(Produccion, null=False, blank=False, default=0, on_delete=models.PROTECT)

class Lote (models.Model):
    fecha_llenado = models.DateField(null=False, blank=False, verbose_name='Fecha llenado')
    hora_llenado = models.TimeField(default='00:00', null=False, blank=True, verbose_name='Hora lleando')
    fecha_carbonatado = models.DateField(null=False, blank=False, verbose_name='Fecha carbonatado')
    hora_carbonatado = models.TimeField(default='00:00', null=False, blank=True, verbose_name='Hora carbonatado')
    barriles = models.ManyToManyField(Barril)
    id_produccion = models.ForeignKey(Produccion, on_delete=models.PROTECT, verbose_name='Produccion')
    activo = models.BooleanField(default=True)







