from django.shortcuts import render
from django.contrib.auth.models import User

def reporte_usuarios(request):
    usuarios = User.objects.all()
    context = {
        'usuarios': usuarios
    }
    return render(request, 'reportes_usuarios/reporte_usuarios.html', context)
