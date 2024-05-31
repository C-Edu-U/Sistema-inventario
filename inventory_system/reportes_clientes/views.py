from django.shortcuts import render
from inventory.models import Cliente

def reporte_clientes(request):
    clientes = Cliente.objects.all()
    context = {
        'clientes': clientes
    }
    return render(request, 'reportes_clientes/reporte_clientes.html', context)
