from django.db import models

# Create your models here.

class Persona(models.Model):
    tipo_doc=models.CharField(max_length=20,null=False)
    documento=models.CharField(max_length=10,null=False,unique=True)
    nombre=models.CharField(max_length=100,null=False)
    apellido=models.CharField(max_length=100,null=False)
    telefono=models.CharField(max_length=20,null=False)
    genero=models.CharField(max_length=20,null=False)