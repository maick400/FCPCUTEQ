from django.db import models


class Model_CNT_Documentos(models.Model):

    codigo = models.TextField(primary_key=True, max_length=5)
    documento = models.TextField(max_length=200, unique=True, null=True, blank=True)
    origen = models.TextField(max_length=1, null=False, blank=False)
    prefijo = models.TextField(max_length=5, null=True, blank=True)
    ultimo_numero = models.IntegerField(null=True, blank=False, default=0)
    numeracion_automatica = models.BooleanField(null=False, blank= False, default=0)
    activo = models.BooleanField(null=False, blank=False , default=1)
    
    def __str__(self) -> str:
        return self.descripcion
    

    class Meta: 
        app_label = "moduloContable"
        managed = True
        db_table = 'cnt_documentos'
        verbose_name = 'un Socio'
        verbose_name_plural = 'Socios'



