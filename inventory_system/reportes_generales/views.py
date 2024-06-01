from django.shortcuts import render
from inventory.models import Venta, Cliente, Producto
from django.contrib.auth.models import User

def reporte_ventas(request):
    ventas = Venta.objects.all()
    context = {
        'ventas': ventas
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
