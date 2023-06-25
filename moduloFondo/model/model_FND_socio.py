from django.db import models
from django.contrib.auth.models import User
from moduloFondo.model.choices.choices_FND_socios import *

class Model_FND_socio(models.Model):
    id_socio = models.BigAutoField(primary_key=True)
    genero = models.CharField(max_length=3, null=False, blank=False, choices=GENEROS_CHOICES)
    estado_civil = models.CharField(max_length=3, null=False, blank=False, choices=ESTADOS_CIVILES_CHOICES)
    direccion = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)
    fecha_nacimiento = models.DateField(null=False, blank=False)
    tipo_prestacion = models.CharField(max_length=3, null=False, blank=False, choices=TIPO_PRESTACION_CHOICES)
    estado = models.CharField(max_length=3, null=False, blank=False, choices=ESTADO_CHOICES)
    contacto_referencia = models.CharField(max_length=10,null=False, blank=False)
    total_ahorrado = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    total_garantizado = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    foto = models.CharField(max_length=1000, null=False, blank=False)
    total_creditos = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    id_usuario = models.ForeignKey(User,on_delete=models.CASCADE,null=False, blank=False)
    pPresta = models.BooleanField(null=False, blank=False)
    
    class Meta: 
        app_label = "moduloFondo"
        managed = True
        db_table = 'fnd_socio'
        verbose_name = 'un Socio'
        verbose_name_plural = 'Socios'
        