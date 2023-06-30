from django.db import models

class Model_FND_tipo_descuento(models.Model):
    codigo = models.TextField(primary_key=True, max_length=5, null=False, blank=False, default= 'DESC')
    tipo_descuento = models.CharField(max_length=100,  blank=False, null=False)

    class Meta:
        app_label = "moduloFondo"
        managed = True
        db_table = 'fnd_tipo_descuento'
        verbose_name = 'un tipo de descuento'
        verbose_name_plural = 'Tipos de descuentos'