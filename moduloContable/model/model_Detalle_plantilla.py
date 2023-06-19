from django.db import models
from moduloContable.model.model_CNT_Cuenta_Contable import Model_CNT_Cuenta_Contable as cuentaContable
from moduloContable.model.model_CNT_Diario_Cuentas_Plantilla import Model_CNT_Diario_Cuentas_Plantilla as cuentaPlantilla

class Model_CNT_Detalle_plantilla(models.Model):
    
    cont_cuenta_contableCodigo=models.ForeignKey(cuentaContable,blank=False,null=False,on_delete=models.CASCADE)
    cont_diario_plantillaid=models.ForeignKey(cuentaPlantilla,blank=False,null=False,on_delete=models.CASCADE)
    debe_haber=models.CharField(max_length=1,blank=False,null=False)

    class Meta: 
        app_label = "moduloContable"
        managed = True
        db_table = 'CNT_Detalle_plantilla'
        verbose_name = 'un Socio'
        verbose_name_plural = 'Socios'