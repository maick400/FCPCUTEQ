from django.db import models

class Model_CNT_Tipo_Transaccion_Contable(models.Model):

    id_transaccion_contable=models.TextField(primary_key=True, max_length=5)
    tipo_transaccion=models.TextField(null=False,blank=False)
    ultimo_numero = models.IntegerField(null=False, blank=False)
    estado = models.BooleanField(null=False, blank=False)

    class Meta: 
        app_label = "moduloContable"
        managed = True
        db_table = 'cnt_tipotransaccion_contable'
        verbose_name = 'un Socio'
        verbose_name_plural = 'Socios'