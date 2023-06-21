from django.db import models

class Model_CRE_credito_bien(models.Model):
    id_credito_bien = models.BigAutoField(primary_key=True)
    bien = models.CharField(max_length=200, blank=False, null=False)
    avaluo = models.DecimalField(max_digits=12, decimal_places=2, blank=False, null = False)
    atributos = models.CharField(max_length=99999, blank=True, null=True)

    class Meta:
        app_label = "moduloCreditos"
        managed = True
        db_table = 'cre_tipo_credito_bien'
        verbose_name = 'un crédito por bien'
        verbose_name_plural = 'créditos por bien'