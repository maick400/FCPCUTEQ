from django.db import models
from moduloContable.model.model_CNT_Tipo_Transaccion_Contable import *
from moduloContable.model.model_CNT_Documento import *



class Model_CNT_Diario_Cuentas_Plantilla(models.Model):
    # pk and fk's
    cuenta_plantilla=models.BigAutoField(primary_key=True)
    transaccion_contable=models.ForeignKey(Model_CNT_Tipo_Transaccion_Contable,blank=False,null=False,on_delete=models.CASCADE)
    documento=models.ForeignKey(Model_CNT_Documentos,blank=False,null=False,on_delete=models.CASCADE)
    identificacador = models.TextField(blank=False, null=False, max_length=500)
    descripcion=models.CharField(blank=False,null=False,max_length=100)
    automatizada=models.BooleanField(blank=False,null=False)
    
    def __str__(self) -> str:
        return self.descripcion
    

    class Meta: 
        app_label = "moduloContable"
        managed = True
        db_table = 'cnt_diario_cuentas_plantilla'
        verbose_name = 'un Socio'
        verbose_name_plural = 'Socios'



