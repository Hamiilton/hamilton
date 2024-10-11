from django.db import models
from datetime import date
from django.core.validators import MinValueValidator,MaxValueValidator
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

class Producto(models.Model):
    codigo=models.CharField(verbose_name='Codigo del prodducto',
                            max_length=100,
                            unique=True,
                            null=False)
    nombre=models.CharField(verbose_name='Nombre del producto',
                            max_length=100,
                            null=False)
    descripcion=models.CharField(verbose_name='Descripcion del producto',
                                max_length=255,
                                null=False)
    presentacion=models.CharField(verbose_name='Presentacion del producto',
                                max_length=100,
                                null=False)
    pais_origen=models.CharField(verbose_name='Pais de origen del producto',
                                max_length=100,
                                null=False)
    activo=models.BooleanField(verbose_name='Producto activo #####',
                            default=True,
                            null=False)
    fecha_fabric=models.DateField(verbose_name='Fecha de fabricacion del producto',
                                default=date.today,
                                null=False)
    fecha_vencimineto=models.DateField(verbose_name='Fecha de vencimineto del producto',
                                null=True)
    precio=models.DecimalField(verbose_name='Precio del producto',
                            max_digits=20,
                            decimal_places=2)
    stok=models.IntegerField(verbose_name='Stok del producto',
                            default=0,
                            validators=[MinValueValidator(0),MaxValueValidator(1000)],
                            null=False)

class Persona(models.Model):
    codigo=models.CharField(verbose_name='Numero de documento',
                            db_index=True,
                            max_length=100,
                            null=False)
    nombre=models.CharField(verbose_name='Nombre de la perosna',
                            max_length=100,
                            null=False,
                            db_index=True)
    apellido=models.CharField(verbose_name='Apellido de la persona',
                            max_length=150,
                            null=False,
                            help_text='Agrege su apellido')
    ciudad=models.CharField(verbose_name='Ciudad de la persona',
                            max_length=200,
                            help_text='Ingrese su ciudad',
                            default='Soacha',
                            db_index=True,
                            null=False)
    direccion=models.CharField(verbose_name='Direccion de la persona',
                            max_length=200,
                            null=False,
                            help_text='Ingrese su direccion')
    telefono=models.CharField(verbose_name='Telefono de la persona',
                            max_length=50,
                            null=False,
                            help_text='Ingrese su numero de telefono',
                            unique=True)
    correo=models.CharField(verbose_name='Correo de la persona',
                            max_length=200,
                            null=False,
                            db_index=True,
                            help_text='Ingrese su correo')
    GENERO__OPC=[('M','Mssculino'),
                ('F','Femenino')]
    genero=models.CharField(verbose_name='Genero de la persona',
                            max_length=1,
                            choices=GENERO__OPC)
    ACTIVO_OPC=[(1,'Activo'),
                (2,'Inactivo')]
    activo=models.PositiveIntegerField(verbose_name='Estado activo de la persona',
                            choices=ACTIVO_OPC,
                            default=True,
                            help_text='Ingrese el estado de activida de la persona')
    TIPO_PERSONA=[(0,'Natural'),(1,'Juridica')]
    tipo_persona=models.CharField(verbose_name='Tipo de persona',
                                max_length=20,
                                null=False,
                                help_text='Igrese si es persona natural y juridica',
                                choices=TIPO_PERSONA,
                                default='Natural')
    
class Cliente(models.Model):
    nombre=models.CharField(verbose_name='Nombre del cliente',
                            max_length=100,
                            null=False)
    email=models.EmailField(verbose_name='Correo del cliente')
    def __str__(self) -> str:
        return self.nombre
    
class pedido_cliente(models.Model):
    fecha_pedido=models.DateField()
    valor_pedido=models.IntegerField()
    cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE,related_name='Pedidos')
    def __str__(self) -> str:
        return self.fecha_pedido
    
## UNO A MUCHOS
class Continente(models.Model):
    codigo=models.CharField(verbose_name='Codigo del coontinente',
                            max_length=45,
                            null=False)
    nombre=models.CharField(verbose_name='Nombre del continente',
                            max_length=45,
                            null=False)
    def __str__(self):
        return self.nombre

class Pais(models.Model):
    codigo=models.CharField(verbose_name='Codigo del pais',
                            max_length=45,
                            null=False)
    nombre=models.CharField(verbose_name='Nombre del pais',
                            max_length=45,
                            null=False)
    continente_id=models.ForeignKey(Continente,
                                    on_delete=models.CASCADE,
                                    related_name='Codigo_continente')
    def __str__(self):
        return self.nombre
class Provincia(models.Model):
    codigo=models.CharField(verbose_name='Codigo de la provincia',
                            max_length=45,
                            null=False)
    nombre=models.CharField(verbose_name='Nombre de la provincia',
                            max_length=45,
                            null=False)
    pais_id=models.ForeignKey(Pais,
                                on_delete=models.CASCADE,
                                related_name='Codigo_provincia')
    def __str__(self):
        return self.nombre
class Municipio(models.Model):
    codigo=models.CharField(verbose_name='Codigo del municipio',
                            max_length=45,
                            null=False)
    nombre=models.CharField(verbose_name='Nombre del municipio',
                            max_length=45,
                            null=False)
    municipio_id=models.ForeignKey(Provincia,
                                    on_delete=models.CASCADE,
                                    related_name='Codigo_provincia')
    def __str__(self):
        return self.nombre
##UNO A UNO
class Usuario(models.Model):
    nombre=models.CharField(max_length=100,
                            verbose_name='Nombre del usuario',
                            help_text='Ingrese su nombre',
                            null=False)
    email=models.EmailField(max_length=100,
                            verbose_name='Correo de el usuario',
                            help_text='Ingrese su correo',
                            null=False,
                            db_index=True)
    def __str__(self):
        return self.nombre

class Perfil(models.Model):
    usuario=models.OneToOneField(Usuario,on_delete=models.CASCADE)
    fecha_nacimiento_usuario=models.DateField(verbose_name='Fecha de nacimineto',
                                            null=False,
                                            help_text='Ingrese su fecha de  nacimineto en formato aaaa/mm/dd',
                                            )
    direccion=models.CharField(max_length=100,
                            verbose_name='Direccion del usuario',
                            null=False,
                            help_text='Ingrese su direccion de residencia actual')
    def __str__(self):
        return f'Perfil de {self.usuario.nombre}'
    
##MUCHOS A MUCHOS

class Instructor(models.Model):
    nombre=models.CharField(max_length=100,
                            verbose_name='Nombre del instructor',
                            null=False)
    profesion=models.CharField(max_length=100,
                            verbose_name='Profesion del instructor',
                            null=False)
    especialidad=models.CharField(max_length=100,
                                verbose_name='Especialida  del instructor',
                                null=False)
    fecha_contratacion=models.DateField(verbose_name='Fceha de contratacion del instructor',
                                        null=False)
    def __str__(self):
        return self.nombre,self.profesion
    
class Aprendiz(models.Model):
    nombre=models.CharField(verbose_name='Nombre del aprendiz',
                            max_length=100,
                            null=False)
    apellido=models.CharField(verbose_name='Apellido del aprendiz',
                        max_length=100,
                        null=False)
    instructores=models.ManyToManyField(Instructor,related_name='aprendices')

    def __str__(self):
        return self.nombre,self.apellido