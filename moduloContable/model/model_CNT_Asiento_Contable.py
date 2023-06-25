from django.db import models
from moduloContable.model.model_CNT_Documento import *
from moduloContable.model.model_CNT_Diario_Cuentas_Plantilla import * 
from moduloContable.model.model_CNT_Periodo_Fiscal import * 
from moduloContable.model.model_CNT_Tipo_Transaccion_Contable import * 
from moduloFondo.model.model_FND_Personal import *
# from moduloContable.model.model_CNT_Tipo_Transaccion_Contable import * 


class Model_Asiento_Contable(models.Model):

    id_asiento_contable = models.BigAutoField(primary_key=True)
    # ! foraneas
    plantilla = models.ForeignKey(Model_CNT_Diario_Cuentas_Plantilla,null=True, blank=True, on_delete=models.CASCADE)
    periodo_fiscal = models.ForeignKey( Model_CNT_Periodo_Fiscal,null=False, blank=False, on_delete=models.CASCADE)
    # ! documento
    documeto = models.ForeignKey(Model_CNT_Documentos, null=False, blank=False, on_delete=models.CASCADE)
    nombre_documento = models.TextField (blank=False, null=False, max_length=200)
    numero_documento = models.TextField()
    # ! transaccion
    transacción = models.ForeignKey(Model_CNT_Tipo_Transaccion_Contable, null=False, blank=False, on_delete=models.CASCADE)
    transaccion_contable = models.TextField(null=False, blank=False, max_length=500)
    numero_transaccion = models.TextField ( null=True, blank=True, max_length=200 )
    
    # ! personal que ha creado 
    personal = models.ForeignKey(Model_FND_Personal,  null= False, blank=False, on_delete=models.CASCADE, related_name="personal")    
    nombre_personal = models.TextField(null=False, blank=False, max_length= 200)
    
    #! contador 
    contador = models.ForeignKey(Model_FND_Personal,  null= False, blank=False, on_delete=models.CASCADE, related_name='contador')  
    nombre_contador = models.TextField(null=False, blank=False, max_length= 200)
    
    #! Gerente
    gerente = models.ForeignKey(Model_FND_Personal,  null= False, blank=False, on_delete=models.CASCADE, related_name='gerente')  
    nombre_gerente = models.TextField(null=False, blank=False, max_length= 200)
    
    #!presidente
    presidente = models.ForeignKey(Model_FND_Personal,  null= False, blank=False, on_delete=models.CASCADE,related_name='presidente')  
    nombre_presidente = models.TextField(null=False, blank=False, max_length= 200)
    
    
    
    fecha_emision = models.DateTimeField(auto_now_add=True)
    fecha_cierre = models.DateTimeField()
    fecha_mayorización = models.DateTimeField(blank=True, null=True)
    detalle = models.TextField (null=False, blank=False, max_length=500)
    descripcion = models.TextField ( null= True, blank=True, max_length=500)
    estado = models.TextField(null=False, blank=False, max_length=3)
    total_debe = models.DecimalField(decimal_places=2, max_digits=15 )
    total_haber  = models.DecimalField(decimal_places=2, max_digits=15)
    
    
    
    
    
    
    
    
    
    
    

    
    


    class Meta: 
        app_label = "moduloContable"
        managed = True
        db_table = 'cnt_Asiento_contable'
        verbose_name = 'un Socio'
        verbose_name_plural = 'Socios'
