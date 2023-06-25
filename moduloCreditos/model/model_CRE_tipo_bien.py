from django.db import models

class Model_CRE_tipo_bien(models.Model):
    id_tipo_bien =  models.BigAutoField(primary_key=True)
    nombre_bien = models.CharField(max_length=100, null=False, blank=False)
    avaluo = models.DecimalField(max_digits=12, decimal_places=2, null=False, blank = False)
    observacion = models.CharField(max_length=500, null=True, blank=True)
    es_aceptado = models.BooleanField(null=False)
    fecha_creacion = models.DateTimeField(null=False)
    fecha_modificacion = models.DateTimeField(null = False)

    def __str__(self) -> str:
        return self.nombre_bien

    class Meta:
        app_label = "moduloCreditos"
        managed = True
        db_table = 'cre_tipo_bien'
        verbose_name = 'un tipo de bien'
        verbose_name_plural = 'tipo de bienes'