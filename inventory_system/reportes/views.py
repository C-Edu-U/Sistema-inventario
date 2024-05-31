from django.shortcuts import render
from inventory.models import Venta
from django.db.models import Sum

def reporte_ventas(request):
    ventas = Venta.objects.values('producto__nombre').annotate(
        total_vendido=Sum('cantidad'),
        total_ingresos=Sum('precio_total')
    )
    context = {
        'ventas': ventas
    }
    return render(request, 'reportes/reporte_ventas.html', context)
