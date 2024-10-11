# Generated by Django 5.1.1 on 2024-10-11 21:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primer_app', '0005_cliente_pedido_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ingrese su nombre', max_length=100, verbose_name='Nombre del usuario')),
                ('email', models.EmailField(db_index=True, help_text='Ingrese su correo', max_length=100, verbose_name='Correo de el usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_nacimiento_usuario', models.DateField(help_text='Ingrese su fecha de  nacimineto en formato aaaa/mm/dd', verbose_name='Fecha de nacimineto')),
                ('direccion', models.CharField(help_text='Ingrese su direccion de residencia actual', max_length=100, verbose_name='Direccion del usuario')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='primer_app.usuario')),
            ],
        ),
    ]