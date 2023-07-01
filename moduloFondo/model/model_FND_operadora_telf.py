from typing import Any
from django.db import models

class Model_FND_operadora_telf(models.Model):
    operadora_id = models.BigAutoField(primary_key=True)
    operadora = models.TextField(max_length=20,blank=False,null=False,unique=True,verbose_name="operadora")

    def __str__(self) -> str:
        return self.operadora


    class Meta:
        app_label = "moduloFondo"
        constraints=[
            models.UniqueConstraint(fields=["operadora_id"],name="uq_fnd_operadora_id"),
            models.UniqueConstraint(fields=["operadora_id"],name="uq_fnd_operadora")
        ]
        indexes=[models.Index(fields=["operadora_id"])]
        managed = True
        db_table = 'fnd_operadora_telf'
        verbose_name = 'una operadora'
        verbose_name_plural = 'las operadoras'


urls_operadora = {
            'crear': 'fondo/operadora/operadora_crear.html',
            'editar': 'fondo/operadora/operadora_editar.html',
            'listar': 'fondo/operadora/operadora_lista.html',
            'buscar': 'fondo/operadora/operadora_busqueda.html'
        }