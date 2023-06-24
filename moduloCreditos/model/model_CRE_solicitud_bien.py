from django.db import models

from moduloCreditos.model.model_CRE_solicitud_credito import Model_CRE_solicitud_credito

class Model_CRE_solicitud_bien (models.Model):    
    id_solicitud_bien = models.BigAutoField(primary_key=True)
    id_solicitud_credito = models.ForeignKey(Model_CRE_solicitud_credito, default="", on_delete=models.CASCADE, null =False)
    avaluo = models.DecimalField(max_digits=12, decimal_places=2, blank=False, null=False)
    bien = models.CharField(max_length=200, blank=False, null=False)
    estado = models.CharField(max_length=1, blank=False, null=False)
    atributo = models.CharField(max_length=99999, blank=False, null=False)

    def __str__(self) -> str:
        return (self.id_solicitud_bien)

    class Meta:
        app_label = "moduloCreditos"
        managed = True
        db_table = 'cre_solicitud_bien'
        verbose_name = 'una solicitud por bien'
        verbose_name_plural = 'solicitudes por bien'