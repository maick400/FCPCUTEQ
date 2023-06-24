from django.db import models
from moduloContable.model.model_CNT_Anio_Fiscal import Model_CNT_Anio_Fiscal 

class Model_CNT_Periodo_Fiscal(models.Model):
    id_periodo_fiscal=models.AutoField(primary_key=True)
    anio_fiscal=models.ForeignKey(Model_CNT_Anio_Fiscal,null=False,blank=False,on_delete=models.CASCADE)
    numero=models.IntegerField(blank=False,null=False)
    nombre=models.CharField(max_length=100,blank=False,null=False)
    inicio=models.DateField(blank=False,null=False)
    fin=models.DateField(blank=False,null=False)
    estado=models.TextField(blank=False,null=False)

    def __str__(self) -> str:
        return self.Nombre
    
    class Meta: 
        app_label = "moduloContable"
        managed = True
        db_table = 'cnt_periodo_fiscal'
        verbose_name = 'un Socio'
        verbose_name_plural = 'Socios'