from django.contrib import admin
from .models import Cliente, Compra, Producto, Vendedor, Venta

admin.site.register(Cliente)
admin.site.register(Compra)
admin.site.register(Producto)
admin.site.register(Vendedor)
admin.site.register(Venta)
