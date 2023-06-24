from django.db import models
from moduloContable.model.model_CNT_Tipo_Transaccion_Contable import Model_CNT_Tipo_Transaccion_Contable as transaccionContable

class Model_CNT_Transaccion_Contable(models.Model):

    id_tipo_transaccion=models.ForeignKey(transaccionContable,blank=False,null=False,on_delete=models.CASCADE)
    
    id_transaccion_contable=models.BigAutoField(blank=False,null=False,primary_key=True)
    detalle=models.TextField(blank=False,null=False,max_length=100)
    ultima_linea=models.IntegerField(blank=False,null=False)
    estado=models.BooleanField(blank=False,null=False)

    def __str__(self) -> str:
        return self.detalle
    

    class Meta: 
        app_label = "moduloContable"
        managed = True
        db_table = 'CNT_Transaccion_Contable'
        verbose_name = 'un Socio'
        verbose_name_plural = 'Socios'
