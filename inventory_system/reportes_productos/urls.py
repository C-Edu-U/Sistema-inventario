from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.reporte_productos, name='reporte_productos'),
]
