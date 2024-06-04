from django.shortcuts import render
from inventory.models import Venta, Cliente, Producto
from django.contrib.auth.models import User
from django.db.models import Sum, F
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def reportes_generales(request):
    return render(request, 'reportes_generales/reportes_generales.html')

def reporte_ventas(request):
    ventas = Venta.objects.annotate(
        total_detalle=Sum(F('detalles__precio') * F('detalles__cantidad'))
    )
    total_ventas = ventas.aggregate(total=Sum('total_detalle'))['total']

    context = {
        'ventas': ventas,
        'total_ventas': total_ventas,
    }
    return render(request, 'reportes_generales/reporte_ventas.html', context)

def reporte_usuarios(request):
    usuarios = User.objects.all()
    context = {
        'usuarios': usuarios
    }
    return render(request, 'reportes_generales/reporte_usuarios.html', context)

def reporte_clientes(request):
    clientes = Cliente.objects.all()
    context = {
        'clientes': clientes
    }
    return render(request, 'reportes_generales/reporte_clientes.html', context)

def reporte_productos(request):
    productos = Producto.objects.all()
    context = {
        'productos': productos
    }
    return render(request, 'reportes_generales/reporte_productos.html', context)

