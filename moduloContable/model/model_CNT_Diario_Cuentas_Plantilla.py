from django.db import models
<<<<<<< HEAD
from moduloContable.model.model_CNT_Tipo_Transaccion_Contable import *
from moduloContable.model.model_CNT_Documento import *



class Model_CNT_Diario_Cuentas_Plantilla(models.Model):
    # pk and fk's
    id_cuentas_plantillas=models.BigAutoField(primary_key=True)
    transaccion_contable=models.ForeignKey(Model_CNT_Tipo_Transaccion_Contable,blank=False,null=False,on_delete=models.CASCADE)
    documento=models.ForeignKey(Model_CNT_Documentos,blank=False,null=False,on_delete=models.CASCADE)
    identificacador = models.TextField(blank=False, null=False, max_length=500)
    descripcion=models.CharField(blank=False,null=False,max_length=100)
=======
from moduloContable.model.model_CNT_Transaccion_Contable import Model_CNT_Transaccion_Contable as TransaccionCont
from moduloContable.model.mode_SIS_Tipo_Documentos import *

class Model_CNT_Diario_Cuentas_Plantilla(models.Model):

    Cont_Transaccion_Contableid=models.ForeignKey(TransaccionCont,blank=False,null=False,on_delete=models.CASCADE)
    Sis_Tipo_DocumentosCodigo=models.ForeignKey(Model_SIS_Tipo_Documentos,on_delete=models.CASCADE,null=False,default="")
    id_cuentas_plantillas=models.BigAutoField(primary_key=True,blank=False,null=False)
    descripcion=models.TextField(blank=False,null=False,max_length=100)
>>>>>>> main
    automatizada=models.BooleanField(blank=False,null=False)
    
    def __str__(self) -> str:
        return self.descripcion
    

    class Meta: 
        app_label = "moduloContable"
        managed = True
        db_table = 'cnt_diario_cuentas_plantilla'
        verbose_name = 'un Socio'
        verbose_name_plural = 'Socios'



