from django.urls import path
from . import views

urlpatterns = [
    path('clientes/', views.reporte_clientes, name='reporte_clientes'),
]
