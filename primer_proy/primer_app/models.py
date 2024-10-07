from django.db import models

# Create your models here.

class Propietario(models.Model):
    nombre=models.CharField(verbose_name='Nombre del propietario',max_length=100)
    apellido=models.CharField(verbose_name='Apellido del propietario',max_length=100)
    ciudad=models.CharField(verbose_name='Ciudad del propietario',max_length=100)
    direccion=models.CharField(verbose_name='Direccion del propietarip',max_length=100)
    telefono=models.CharField(verbose_name='Telefono del propietario',max_length=100)
    correo=models.CharField(verbose_name='Correco del propietario',max_length=100)
    contraseña=models.CharField(verbose_name='Contraseña del propietario',max_length=100)
    activo=models.BooleanField(verbose_name='Usuario activo',default=True)

    def __str__(self):
        return self.nombre, self.apellido

# class Mascota(models.Model):
#     codigo=models.CharField('Codigo',max_length=100)
#     nombre=models.CharField('Nombre de la mascota',max_length=100)
#     especie=models.CharField('Especie de la m ascota',max_length=100)






