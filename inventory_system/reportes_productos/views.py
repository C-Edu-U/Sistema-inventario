from django.shortcuts import render
from inventory.models import Producto

def reporte_productos(request):
    productos = Producto.objects.all()
    context = {
        'productos': productos
    }
    return render(request, 'reportes_productos/reporte_productos.html', context)
