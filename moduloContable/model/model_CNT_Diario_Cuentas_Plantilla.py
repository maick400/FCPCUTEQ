from django.db import models
from moduloContable.model.model_CNT_Transaccion_Contable import Model_CNT_Transaccion_Contable as TransaccionCont


class Model_CNT_Diario_Cuentas_Plantilla(models.Model):

    Cont_Transaccion_Contableid=models.ForeignKey(TransaccionCont,blank=False,null=False,on_delete=models.CASCADE)
    #Sis_Tipo_DocumentosCodigo=models.ForeignKey()

    id_cuentas_plantillas=models.BigAutoField(primary_key=True,blank=False,null=False)
    descripcion=models.CharField(blank=False,null=False,max_length=100)
    automatizada=models.BooleanField(blank=False,null=False)

    def __str__(self) -> str:
        return self.descripcion
    

    class Meta: 
        app_label = "moduloContable"
        managed = True
        db_table = 'CNT_Diario_Cuentas_Plantilla'
        verbose_name = 'un Socio'
        verbose_name_plural = 'Socios'



