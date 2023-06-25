from django.db import models
from moduloFondo.model.model_FND_socio import Model_FND_socio as SOCIO
from moduloFondo.model.model_FND_tipo_identificación import * 
from moduloFondo.model.model_FND_provincia import * 
from moduloFondo.model.model_FND_canton import * 




class Model_FND_Parametros_sys(models.Model):
    
    tipo_de_idemtificacion_fcpc = models.ForeignKey(Model_Fnd_Tipo_Identificacion, null=False, blank=False, on_delete=models.CASCADE)
    identificacion = models.TextField(max_length=13, null= False, blank=False )
    n_resolucion = models.TextField(max_length=15, null= False, blank=False )
    fecha_resolucion = models.DateField(null=False, blank=False)
    provincia = models.ForeignKey (Model_Fnd_Provincia, null=False, blank=False, on_delete=models.CASCADE)
    canton = models.ForeignKey(Model_Fnd_Canton, null=False, blank=False, on_delete=models.CASCADE)
    direccion = models.TextField(max_length=60, null=False, blank=False)
    email = models.TextField(max_length=60, null=False, blank=True)
    tipo_sistema = 
    
    
    
    
    
    nombre_fondo = models.CharField(max_length=300,null=False, blank=False)
    contador = models.ForeignKey(SOCIO,null=False, blank=False, on_delete=models.CASCADE, related_name='contador')
    matricula_contador = models.CharField(max_length=100,null=False, blank=False)
    representante_legal = models.ForeignKey(SOCIO,null=False, blank=False, on_delete=models.CASCADE, related_name='representante_legal')
    responsable_creditos = models.ForeignKey(SOCIO,null=False, blank=False, on_delete=models.CASCADE, related_name='responsable_creditos')
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