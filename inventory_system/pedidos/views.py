from django.shortcuts import render, redirect
from .forms import VentaForm, DetalleVentaFormSet
from inventory.models import Venta

def crear_pedido(request):
    if request.method == 'POST':
        venta_form = VentaForm(request.POST)
        detalle_formset = DetalleVentaFormSet(request.POST)
        if venta_form.is_valid() and detalle_formset.is_valid():
            venta = venta_form.save(commit=False)
            venta.vendedor = request.user
            venta.save()
            detalles = detalle_formset.save(commit=False)
            total = 0
            for detalle in detalles:
                detalle.venta = venta
                detalle.precio = detalle.producto.precio_unitario
                total += detalle.precio * detalle.cantidad
                detalle.save()
                detalle.producto.existencia -= detalle.cantidad
                detalle.producto.save()
            venta.total = total
            venta.save()
            return redirect('index')
    else:
        venta_form = VentaForm()
        detalle_formset = DetalleVentaFormSet()
    return render(request, 'pedidos/pedido_form.html', {
        'venta_form': venta_form,
        'detalle_formset': detalle_formset
    })

