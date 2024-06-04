from django.contrib import admin
from .models import Categoria, Producto, Cliente, Venta, DetalleVenta

class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta
    extra = 1

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'descripcion', 'precio_unitario', 'existencia', 'categoria')
    list_filter = ('categoria',)
    search_fields = ('nombre',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellidos', 'email', 'telefono')
    search_fields = ('nombre', 'apellidos', 'email')

@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'vendedor', 'fecha', 'total')
    list_filter = ('fecha', 'vendedor')
    search_fields = ('cliente__nombre', 'cliente__apellidos', 'vendedor__username')
    date_hierarchy = 'fecha'
    inlines = [DetalleVentaInline]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.prefetch_related('cliente', 'vendedor')
        return queryset

@admin.register(DetalleVenta)
class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'venta', 'producto', 'cantidad', 'precio')
    search_fields = ('venta__cliente__nombre', 'producto__nombre')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.prefetch_related('venta', 'producto')
        return queryset