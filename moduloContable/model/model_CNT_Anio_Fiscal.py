from django.db import models


class Model_CNT_Anio_Fiscal(models.Model):
    id_AnioFiscal=models.BigAutoField(primary_key=True)
    anio=models.IntegerField(null=False,blank=False,unique=False)
    inicio=models.DateField(null=False,blank=False)
    fin=models.DateField(null=False,blank=False)
    activo=models.TextField(unique=False,blank=False,null=False,max_length=3,default="")


    def __str__(self) -> str:
        return self.anio
    
    class Meta: 
        app_label = "moduloContable"
        managed = True
        db_table = 'Model_CNT_Anio_Fiscal'
        verbose_name = 'un Socio'
        verbose_name_plural = 'Socios'