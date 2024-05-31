from django.shortcuts import render
from .models import Venta

def lista_ventas(request):
    ventas = Venta.objects.all()
    return render(request, 'inventory/lista_ventas.html', {'ventas': ventas})
