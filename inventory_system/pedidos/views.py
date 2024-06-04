from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from inventory.models import Venta
from .forms import PedidoForm


def crear_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.vendedor = request.user  # Asigna el usuario conectado como vendedor
            pedido.save()
            return redirect('pedidos:pedido_exitoso')  # Redirige a una página de éxito
    else:
        form = PedidoForm()
    return render(request, 'pedidos/pedido_form.html', {'form': form})
