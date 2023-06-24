from django.db import models
from moduloFondo.model.model_FND_socio import Model_FND_socio
from moduloFondo.model.model_FND_tipo_descuento import Model_FND_tipo_descuento
from moduloFondo.model.model_FND_Personal import Model_FND_Personal

class Model_FND_socio_aportaciones(models.Model):
    id_socio = models.ForeignKey(Model_FND_socio, on_delete=models.CASCADE, null=False, blank=False)
    id_tipo_descuento = models.ForeignKey(Model_FND_tipo_descuento, on_delete=models.CASCADE, null=False, blank=False)
    id_personal = models.ForeignKey(Model_FND_Personal, on_delete=models.CASCADE, null=False, blank=False)
    fecha_aportacion = models.DateField(null=False, blank=False)
    monto = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    #id_asiento_contable = models.ForeignKey('Model_CNT_asiento_contable', on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        app_label = "moduloFondo"
        managed = True
        db_table = 'fnd_socio_aportaciones'
        verbose_name = 'una aportación'
        verbose_name_plural = 'Aportaciones'