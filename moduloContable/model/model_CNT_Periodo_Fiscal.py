from django.db import models
from moduloContable.model.model_CNT_Anio_Fiscal import Model_CNT_Anio_Fiscal as anioFiscal

class Model_CNT_Periodo_Fiscal(models.Model):

    anio_fiscal=models.ForeignKey(anioFiscal,null=False,blank=False,on_delete=models.CASCADE)
    id_PeriodoFiscal=models.IntegerField(blank=False,null=False)
    numero=models.IntegerField(blank=False,null=False)
    nombre=models.TextField(max_length=100,blank=False,null=False)
    inicio=models.DateField(blank=False,null=False)
    fin=models.DateField(blank=False,null=False)
    estado=models.TextField(blank=False,null=False,max_length=3)

    def __str__(self) -> str:
        return self.Nombre
    
    class Meta: 
        app_label = "moduloContable"
        managed = True
        db_table = 'CNT_Periodo_Fiscal'
        verbose_name = 'un Socio'
        verbose_name_plural = 'Socios'