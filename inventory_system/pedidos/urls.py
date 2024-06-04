from django.urls import path
from django.views.generic import TemplateView
from .views import crear_pedido


app_name = 'pedidos'

urlpatterns = [
    path('nuevo/', crear_pedido, name='crear_pedido'),
    path('exitoso/', TemplateView.as_view(template_name="pedidos/pedido_exitoso.html"), name='pedido_exitoso'),
]
