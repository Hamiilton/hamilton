# Generated by Django 5.1.1 on 2024-10-09 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('primer_app', '0002_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(db_index=True, max_length=100, verbose_name='Numero de documento')),
                ('nombre', models.CharField(db_index=True, max_length=100, verbose_name='Nombre de la perosna')),
                ('apellido', models.CharField(help_text='Agrege su apellido', max_length=150, verbose_name='Apellido de la persona')),
                ('ciudad', models.CharField(db_index=True, default='Soacha', help_text='Ingrese su ciudad', max_length=200, verbose_name='Ciudad de la persona')),
                ('direccion', models.CharField(help_text='Ingrese su direccion', max_length=200, verbose_name='Direccion de la persona')),
                ('telefono', models.CharField(help_text='Ingrese su numero de telefono', max_length=50, unique=True, verbose_name='Telefono de la persona')),
                ('correo', models.CharField(db_index=True, help_text='Ingrese su correo', max_length=200, verbose_name='Correo de la persona')),
                ('genero', models.CharField(choices=[('M', 'Mssculino'), ('F', 'Femenino')], max_length=1, verbose_name='Genero de la persona')),
                ('activo', models.PositiveIntegerField(choices=[(1, 'Activo'), (2, 'Inactivo')], default=True, help_text='Ingrese el estado de activida de la persona', verbose_name='Estado activo de la persona')),
            ],
        ),
    ]
