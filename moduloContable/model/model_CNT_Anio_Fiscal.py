from django.db import models


class Model_CNT_Anio_Fiscal(models.Model):
    
    id_AnioFiscal=models.BigAutoField(primary_key=True)
    anio=models.IntegerField(null=False,blank=False)
    inicio=models.DateField(null=False,blank=False)
    fin=models.DateField(null=False,blank=False)
    estado=models.TextField( max_length=3)


    def __str__(self) -> str:
        return self.anio
    
    class Meta: 
        app_label = "moduloContable"
        managed = True
        db_table = 'cnt_anio_fiscal'
        verbose_name = 'un Socio'
        verbose_name_plural = 'Socios'