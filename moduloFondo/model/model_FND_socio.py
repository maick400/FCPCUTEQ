from django.db import models
from django.contrib.auth.models import User
from moduloFondo.model.choices.choices_FND_socios import *
from moduloFondo.model.Model_FND_provincia import Model_FND_provincia

class Model_FND_socio(models.Model):
    id_socio = models.BigAutoField(primary_key=True, null=False, blank=False, verbose_name='ID Socio')    
    id_usuario = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, verbose_name='Usuario', db_column='id_usuario')
    id_provincia = models.ForeignKey(Model_FND_provincia,max_length=5, null=False, blank=False,on_delete=models.CASCADE, verbose_name='Provincia', db_column='codigo_provincia')
    nombres = models.TextField(max_length=200, null=False, blank=False, verbose_name='Nombres')
    apellido_paterno = models.TextField(max_length=100, null=False, blank=False, verbose_name='Apellido Paterno')
    apellido_materno = models.TextField(max_length=100, null=False, blank=False, verbose_name='Apellido Materno')
    genero = models.TextField(max_length=5, null=False, blank=False, choices=GENEROS_CHOICES, verbose_name='Género')
    tipo_identificacion = models.TextField(max_length=5, null=False, blank=False, verbose_name='Tipo de Identificación')
    identificacion = models.TextField(max_length=12, null=False, blank=False, verbose_name='Identificación')
    fecha_nacimiento = models.DateField(null=False, blank=False, auto_now=False, auto_now_add=False, verbose_name='Fecha de Nacimiento')
    estado_civil = models.TextField(max_length=5, null=False, blank=False, choices=ESTADOS_CIVILES_CHOICES, default='SOL', verbose_name='Estado Civil')
    pais = models.TextField(max_length=5, null=False, blank=False, verbose_name='País')
    ciudad = models.TextField(max_length=100, null=False, blank=False, verbose_name='Ciudad')
    provincia = models.TextField(max_length=5, null=False, blank=False, verbose_name='Provincia')
    direccion = models.TextField(max_length=100, null=False, blank=False, verbose_name='Dirección')
    foto_ruta = models.TextField(max_length=None, null=False, blank=False, verbose_name='Ruta de Foto')
    total_ahorrado = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name='Total Ahorrado')
    total_garantizado = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name='Total Garantizado')
    total_monto_creditos_vigente = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False, verbose_name='Total Monto Créditos Vigente')
    numero_aportaciones = models.IntegerField(null=False, blank=False, verbose_name='Número de Aportaciones')
    numero_aportaciones_consecutivas = models.IntegerField(null=False, blank=False, verbose_name='Número de Aportaciones Consecutivas')
    estado_participe = models.TextField(max_length=5, null=False, blank=False, choices=ESTADO_CHOICES, default='A', verbose_name='Estado Participe')
    tipo_sistema = models.TextField(max_length=5, null=False, blank=False, verbose_name='Tipo de Sistema')
    base_calculo_aportacion = models.TextField(max_length=5, null=False, blank=False, verbose_name='Base de Cálculo de Aportación')
    tipo_relacion = models.TextField(max_length=5, null=False, blank=False, verbose_name='Tipo de Relación')
    estado_registro = models.TextField(max_length=5, null=False, blank=False, verbose_name='Estado de Registro')
    fecha_creacion = models.DateTimeField(null=False, blank=False, auto_now_add=True, verbose_name='Fecha de Creación')
    fecha_modificacion = models.DateTimeField(null=False, blank=False, auto_now=True, verbose_name='Fecha de Modificación')
   
    
    class Meta: 
        app_label = "moduloFondo"
        constraints = [
            models.UniqueConstraint(fields=['identificacion'], name='uq_fnd_socio_identificacion'),
        ]
        indexes = [
            models.Index(fields=['id_socio'])
        ] 
        managed = True
        db_table = 'fnd_socio'
        verbose_name = 'un Socio'
        verbose_name_plural = 'Socios'

urls_socio = {
            'crear': 'fondo/socio/socio_crear.html',
            'editar': 'fondo/socio/socio_editar.html',
            'listar': 'fondo/socio/socio_lista.html',
            'buscar': 'fondo/socio/socio_buscar.html'
        }