from django.db import models
from django.contrib.auth.models import User

class Model_FND_socio(models.Model):
    id_socio = models.BigAutoField(primary_key=True)
    genero = models.CharField(max_length=1, null=False, blank=False)
    estado_civil = models.CharField(max_length=3, null=False, blank=False)
    direccion = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=200, null=False, blank=False)
    fecha_nacimiento = models.DateField(null=False, blank=False)
    tipo_prestacion = models.CharField(max_length=3, null=False, blank=False)
    estado = models.CharField(max_length=3, null=False, blank=False)
    contacto_referencia = models.IntegerField(null=False, blank=False)
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