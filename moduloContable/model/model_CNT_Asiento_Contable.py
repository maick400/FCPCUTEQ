from django.db import models
from moduloContable.model.model_CNT_Periodo_Fiscal import Model_CNT_Periodo_Fiscal as PeriodoFiscal
from moduloContable.model.model_CNT_Diario_Cuentas_Plantilla import Model_CNT_Diario_Cuentas_Plantilla as CuentaPlantilla
from moduloContable.model.mode_SIS_Tipo_Documentos import Model_SIS_Tipo_Documentos as sisDocumentos
from moduloContable.model.model_CNT_Transaccion_Contable import transaccionContable as transaccionContable


class Model_Asiento_Contable(models.Model):

    CONT_Diario_PlantillaID=models.ForeignKey(CuentaPlantilla,blank=False,null=False,on_delete=models.CASCADE,default="")
    Sis_Tipo_DocumentosCodigo=models.ForeignKey(sisDocumentos,blank=False,null=False,on_delete=models.CASCADE,default="")
    periodoFiscalId=models.ForeignKey(PeriodoFiscal,blank=False,null=False,on_delete=models.CASCADE,default="") 
    CONT_Transaccion_ContableCod=models.ForeignKey(transaccionContable,blank=False,null=False,on_delete=models.CASCADE,default="")
    
    #PersonaId=models.ForeignKey(,blank=False,null=False)    
    #Representante_Legal=models.IntegerField(blank=False,null=False)    
    
    
    id_asiento_contable=models.BigAutoField(primary_key=True)
    transaccion_contable=models.TextField(max_length=3,blank=False,null=False)
    numero_transaccion=models.IntegerField(blank=False,null=False)
    descripcion=models.TextField(max_length=100,blank=False,null=False)    
    documento=models.TextField(max_length=100,blank=False,null=False)
    numero_documento=models.TextField(max_length=100,blank=False,null=False)
    nombre_persona1=models.TextField(max_length=100,blank=False,null=False)    
    estado=models.BooleanField(blank=False,null=False)
    nombre_representante=models.TextField(max_length=100,blank=False,null=False)    
    total_debe=models.FloatField(blank=False,null=False)
    total_haber=models.FloatField(blank=False,null=False)
    balance=models.FloatField(blank=False,null=False)
    bit=models.BooleanField(blank=False,null=False)


    class Meta: 
        app_label = "moduloContable"
        managed = True
        db_table = 'CNT_Asiento_Contable'
        verbose_name = 'un Socio'
        verbose_name_plural = 'Socios'
