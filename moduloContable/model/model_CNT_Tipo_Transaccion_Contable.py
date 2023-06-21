from typing import Any
from django.db import models

class Model_CNT_Tipo_Transaccion_Contable(models.Model):

    id_transaccion_contable=models.BigAutoField(null=False,blank=False,primary_key=True)
    tipo_transaccion=models.TextField(null=False,blank=False)

    def __str__(self) -> str:
        return self.tipo_transaccion


    class Meta: 
        app_label = "moduloContable"
        managed = True
        db_table = 'CNT_Tipo_Transaccion_Contable'
        verbose_name = 'un Socio'
        verbose_name_plural = 'Socios'