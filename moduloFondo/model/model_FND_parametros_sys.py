from django.db import models

class Model_FND_Parametros_sys(models.Model):
    nombre_fondo = models.CharField(max_length=300,null=False, blank=False)
    nombre_contador = models.CharField(max_length=100,null=False, blank=False)
    matricula_contador = models.CharField(max_length=100,null=False, blank=False)
    cedula_rep_legal = models.CharField(max_length=10,null=False, blank=False)
    nombre_rep_legal = models.CharField(max_length=100,null=False, blank=False)
    ced_representante_Creditos = models.CharField(max_length=200,null=False, blank=False)
    nombre_rep_credito = models.CharField(max_length=200,null=False, blank=False)
    fecha_const_fondo = models.DateField(null=False, blank=False)
    correo = models.EmailField(max_length=100,null=False, blank=False)
    smtp_server = models.CharField(max_length=100,null=False, blank=False)
    smtp_port = models.IntegerField(null=False, blank=False)
    smtp_cuenta = models.IntegerField(null=False, blank=False)
    smtp_password = models.TextField(max_length=2000,null=False, blank=False)
    tipo_aportaciion = models.CharField(max_length=1,null=False, blank=False)
    valor_aplicable_aportación = models.DecimalField(max_digits=10, decimal_places=2,null=False, blank=False)


    class Meta: 
        app_label = "moduloFondo"
        managed = True
        db_table = 'fnd_parametros_sistema'
        verbose_name = 'un Parametro'
        verbose_name_plural = 'Parametros'