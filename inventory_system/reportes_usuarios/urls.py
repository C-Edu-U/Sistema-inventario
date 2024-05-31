from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.reporte_usuarios, name='reporte_usuarios'),
]
