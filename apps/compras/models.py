from django.db import models

class Proveedor (models.Model):
    nombre = models.CharField(max_length=255, null=False, blank= False)
    descripcion = models.TextField(null=False, blank=True, default='Sin descripcion')
    telefono = models.CharField(max_length=100, null=False, blank=True)
    email = models.EmailField(max_length=255, null=False, blank=True)
    direccion = models.CharField(max_length=255, null=False, blank=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

class Ingrediente (models.Model):
    nombre = models.CharField(max_length=255, null=False, blank=False)
    stock = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Stock en kg')
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Compra (models.Model):
    id_proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT, verbose_name='Proveedor')
    id_ingrediente = models.ForeignKey(Ingrediente, on_delete=models.PROTECT, verbose_name='Ingrediente')
    costo = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_compra = models.DateField(null=False, blank=False, verbose_name='Fecha de compra')
    fecha_vencimiento = models.DateField(null=True, verbose_name='Fecha de vencimiento')
    cantidad = models.DecimalField(max_digits=6, decimal_places=2)
    comentario = models.TextField(null=False, blank=True)
    activa = models.BooleanField(default=True)




