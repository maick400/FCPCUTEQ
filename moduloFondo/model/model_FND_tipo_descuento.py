from django.db import models

class Model_FND_tipo_descuento(models.Model):
    id_tipo_descuento = models.BigAutoField(primary_key=True)
    tipo_descuento = models.CharField(max_length=100,  blank=False, null=False)
    descuento = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)

    class Meta:
        app_label = "moduloFondo"
        managed = True
        db_table = 'fnd_tipo_descuento'
        verbose_name = 'un tipo de descuento'
        verbose_name_plural = 'Tipos de descuentos'