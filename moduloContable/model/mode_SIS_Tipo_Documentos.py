from django.db import models


class Model_SIS_Tipo_Documentos(models.Model):

    codigo=models.BigAutoField(primary_key=True)
    nombre=models.TextField(max_length=3,blank=False,null=False)
    interno_externo=models.TextField(blank=False,null=False)
    prefijo=models.TextField(max_length=100,blank=False,null=False)    
    ultimo_numero=models.TextField(max_length=100,blank=False,null=False)
    estado=models.BooleanField(blank=False,null=False)


    def __str__(self) -> str:
        return self.nombre
    
    class Meta: 
        app_label = "moduloContable"
        managed = True
        db_table = 'SIS_Tipo_Documentos'
        verbose_name = 'un Socio'
        verbose_name_plural = 'Socios'