from django.db import models
from apps.produccion.models import Barril

# Create your models here.

class Situacion_frente_iva (models.Model):
    codigo = models.IntegerField(null=False, blank=True)
    descripcion = models.TextField(null=False, blank=True)

    def __str__(self):
        return self.descripcion

#1	IVA Responsable Inscripto
#2	IVA Responsable no Inscripto
#3	IVA no Responsable
#4	IVA Sujeto Exento
#5	Consumidor Final
#6	Responsable Monotributo
#7	Sujeto no Categorizado
#8	Proveedor del Exterior
#9	Cliente del Exterior
#10	IVA Liberado – Ley Nº 19.640
#11	IVA Responsable Inscripto – Agente de Percepción
#12	Pequeño Contribuyente Eventual
#13	Monotributista Social
#14	Pequeño Contribuyente Eventual Social

class Cliente (models.Model):
    razon_social = models.CharField(max_length=255, null=False, blank= False)
    ciudad = models.CharField(max_length=255, null=False, blank= False)
    telefono = models.CharField(max_length=100, null=False, blank= False)
    email = models.EmailField(null=False, blank= True)
    direccion = models.CharField(max_length=100, null=False, blank= False)
    cuit = models.CharField(max_length=15, null=False, blank= False)
    situacion_frente_iva = models.ForeignKey(Situacion_frente_iva, null=False, blank=False, default=0, on_delete=models.PROTECT)
    comentarios = models.TextField(null=True, blank=True, default='Sin comentarios')
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.razon_social

class Forma_de_pago (models.Model):
    codigo = models.IntegerField(null=False, blank=False)
    descripcion = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.descripcion


#forma de pago
# 01 Efectivo
# 02 Debito
# 03 Credito


class Ventas (models.Model):
    fecha = models.DateField(null=False, blank=False, verbose_name='Fecha de venta')
    descripcion = models.TextField(null=False, blank=True, default='Sin descripcion')
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    barriles = models.ManyToManyField(Barril)
    cliente = models.ForeignKey(Cliente, null=False, blank=False, default=0, on_delete=models.PROTECT)
    forma_de_pago = models.ForeignKey(Forma_de_pago, null=False, blank=False, default=0, on_delete=models.PROTECT)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion

