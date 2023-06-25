from django.db import models

from moduloCreditos.model.model_CRE_tipo_credito import Model_CRE_tipo_credito

class Model_CRE_solicitud_garante (models.Model):
    id_solicitud_credito = models.BigAutoField(primary_key=True)
    #id_socio = models.ForeignKey(on_delete=models.CASCADE ,null=False)        
    monto_garantia = models.DecimalField(max_digits=12, decimal_places=2, null=False)    
    fecha_creacion = models.DateTimeField(null=False)
    fecha_modificacion = models.DateTimeField(null = False)


    def __str__(self) -> str:
        return (self.id_solicitud_credito)

    class Meta:
        app_label = "moduloCreditos"
        managed = True
        db_table = 'cre_solicitud_garante'
        verbose_name = 'una solicitud de garante'
        verbose_name_plural = 'solicitudes de garante'