from django.db import models
from moduloContable.model.model_CNT_Asiento_Contable import Model_Asiento_Contable as asientoContable


class Model_CNT_Detalle_Asiento_Contable(models.Model):
    
    id_asiento_contable=models.ForeignKey(asientoContable,on_delete=models.CASCADE,null=False)
    nombre_cuenta=models.IntegerField(blank=False,null=False)
    detalle=models.CharField(blank=False,null=False)
    debe=models.FloatField(blank=False,null=False)
    haber=models.FloatField(blank=False,null=False)

    def __str__(self) -> str:
        return self.detalle
    
    class Meta: 
        app_label = "moduloContable"
        managed = True
        db_table = 'CNT_Detalle_Asiento_Contable'
        verbose_name = 'un Socio'
        verbose_name_plural = 'Socios'

