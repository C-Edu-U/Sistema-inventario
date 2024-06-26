# Generated by Django 4.2.9 on 2024-06-04 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("descripcion", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("apellidos", models.CharField(max_length=150)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("telefono", models.CharField(blank=True, max_length=15, null=True)),
                ("direccion", models.TextField(blank=True, null=True)),
                (
                    "fecha_registro",
                    models.DateTimeField(default=django.utils.timezone.now),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Producto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("descripcion", models.TextField(blank=True, null=True)),
                (
                    "precio_unitario",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("existencia", models.IntegerField(default=0)),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventory.categoria",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Proveedor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=100)),
                ("contacto", models.CharField(max_length=150)),
                ("telefono", models.CharField(max_length=15)),
                ("direccion", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Venta",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cantidad", models.IntegerField()),
                ("fecha_venta", models.DateField()),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventory.cliente",
                    ),
                ),
                (
                    "producto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventory.producto",
                    ),
                ),
                (
                    "vendedor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Compra",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cantidad", models.IntegerField()),
                ("fecha_compra", models.DateField(default=django.utils.timezone.now)),
                (
                    "producto",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventory.producto",
                    ),
                ),
                (
                    "proveedor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="inventory.proveedor",
                    ),
                ),
            ],
        ),
    ]
