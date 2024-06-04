from django import forms
from inventory.models import Venta

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente', 'producto', 'cantidad', 'fecha_venta']
