from django.db import models

from moduloFondo.model.model_FND_operadora_telf import Model_FND_operadora_telf
from moduloFondo.model.model_FND_socio import Model_FND_socio


class Model_FND_contacto_socio(models.Model):
    id_socio = models.ForeignKey(Model_FND_socio, on_delete=models.CASCADE, null=False, blank=False)
    id_operadora = models.ForeignKey(Model_FND_operadora_telf, on_delete=models.CASCADE, null=False, blank=False)
    numero = models.CharField(max_length=10, null=False, blank=False, unique=True)
    estado = models.BooleanField(null=False, blank=False)
    predeterminado = models.BooleanField(null=False, blank=False,unique=True)

    class Meta:
        app_label = "moduloFondo"
        managed = True
        db_table = 'FND_contacto_socio'
        verbose_name = 'un Contacto Socio'
        verbose_name_plural = 'Contactos Socios'