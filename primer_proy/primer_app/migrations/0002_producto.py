# Generated by Django 5.1.1 on 2024-10-09 19:24

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primer_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100, unique=True, verbose_name='Codigo del prodducto')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del producto')),
                ('descripcion', models.CharField(max_length=255, verbose_name='Descripcion del producto')),
                ('presentacion', models.CharField(max_length=100, verbose_name='Presentacion del producto')),
                ('pais_origen', models.CharField(max_length=100, verbose_name='Pais de origen del producto')),
                ('activo', models.BooleanField(default=True, verbose_name='Producto activo #####')),
                ('fecha_fabric', models.DateField(default=datetime.date.today, verbose_name='Fecha de fabricacion del producto')),
                ('fecha_vencimineto', models.DateField(null=True, verbose_name='Fecha de vencimineto del producto')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Precio del producto')),
                ('stok', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1000)], verbose_name='Stok del producto')),
            ],
        ),
    ]
