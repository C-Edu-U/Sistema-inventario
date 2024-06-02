from django.contrib import admin
from .models import Cliente, Compra, Producto, Vendedor, Venta, Proveedor

admin.site.register(Venta)
admin.site.register(Compra)
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Vendedor)
admin.site.register(Cliente)
