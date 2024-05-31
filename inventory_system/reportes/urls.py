from django.urls import path
from . import views

urlpatterns = [
    path('ventas/', views.reporte_ventas, name='reporte_ventas'),
]
