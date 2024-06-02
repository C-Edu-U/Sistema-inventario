from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)
    fecha_registro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=150)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(default="Sin descripción")
    precio_compra = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_caducidad = models.DateField(default=timezone.now)
    existencia = models.IntegerField(default=0)  # Nuevo campo

    def __str__(self):
        return self.nombre

class Compra(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_compra = models.DateField(default=timezone.now)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.producto.existencia += self.cantidad
        self.producto.save()


class Vendedor(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)
    fecha_contratacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

class Venta(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=0)
    fecha_venta = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.producto.existencia -= self.cantidad
        self.producto.save()
