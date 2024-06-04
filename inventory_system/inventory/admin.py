from django.contrib import admin
from .models import Cliente, Compra, Producto, Venta, Proveedor, Categoria

admin.site.register(Venta)
admin.site.register(Compra)
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Cliente)
admin.site.register(Categoria)