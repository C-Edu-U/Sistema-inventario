from django.urls import path
from . import views
from .views import reportes_generales

urlpatterns = [
    path('reportes_generales/', reportes_generales, name='reportes_generales'),
    path('ventas/', views.reporte_ventas, name='reporte_ventas'),
    path('usuarios/', views.reporte_usuarios, name='reporte_usuarios'),
    path('clientes/', views.reporte_clientes, name='reporte_clientes'),
    path('productos/', views.reporte_productos, name='reporte_productos'),
]
