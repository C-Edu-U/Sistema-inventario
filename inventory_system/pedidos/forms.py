from django import forms
from inventory.models import Venta, DetalleVenta, Producto

class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = ['producto', 'cantidad', 'precio']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['producto'].queryset = Producto.objects.filter(existencia__gt=0)

class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta
        fields = ['cliente']

DetalleVentaFormSet = forms.inlineformset_factory(
    Venta, DetalleVenta, form=DetalleVentaForm, extra=1, can_delete=True
)
