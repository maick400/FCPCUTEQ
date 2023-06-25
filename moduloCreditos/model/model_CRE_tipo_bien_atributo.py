from django.db import models

from moduloCreditos.model.model_CRE_tipo_bien import Model_CRE_tipo_bien

class Model_CRE_tipo_bien_atributo(models.Model):
    id_tipo_bien =  models.ForeignKey(Model_CRE_tipo_bien, on_delete=models.CASCADE, null=False, blank=False)
    atributo = models.CharField(max_length=100, null=False, blank=False)
    tipo_dato = models.CharField(max_length=100, null=False, blank=False)
    obligatorio = models.BooleanField(null=False)
    fecha_creacion = models.DateTimeField(null=False)
    fecha_modificacion = models.DateTimeField(null = False)

    class Meta:
        app_label = "moduloCreditos"
        managed = True
        db_table = 'cre_tipo_bien_atributos'
        verbose_name = 'un atributo de un tipo de bien'
        verbose_name_plural = 'atributos de un tipo de bien'