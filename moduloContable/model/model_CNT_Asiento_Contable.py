from django.db import models
#from Model_CNT_Periodo_Fiscal import Model_CNT_Periodo_Fiscal as PeriodoFiscal


class Model_Asiento_Contable(models.Model):

    #CONT_Diario_PlantillaID=models.IntegerField(null=False,blank=False)
    #Sis_Tipo_DocumentosCodigo=models.CharField(max_length=3,blank=False,null=False)
    #periodoFiscalId=models.ForeignKey(PeriodoFiscal,null=False,blank=False) #ya ta
    #CONT_Transaccion_ContableCod=models.CharField(max_length=3,blank=False,null=False)
    #PersonaId=models.ForeignKey(,blank=False,null=False)    
    #Representante_Legal=models.IntegerField(blank=False,null=False)    
    
    
    id_asiento_contable=models.BigAutoField(primary_key=True)
    transaccion_contable=models.CharField(max_length=3,blank=False,null=False)
    numero_transaccion=models.IntegerField(blank=False,null=False)
    descripcion=models.CharField(max_length=100,blank=False,null=False)    
    documento=models.CharField(max_length=100,blank=False,null=False)
    numero_documento=models.CharField(max_length=100,blank=False,null=False)
    nombre_persona1=models.CharField(max_length=100,blank=False,null=False)    
    estado=models.BooleanField(blank=False,null=False)
    nombre_representante=models.CharField(max_length=100,blank=False,null=False)    
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
