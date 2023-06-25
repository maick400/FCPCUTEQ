from django.db import models 
from moduloFondo.model.model_FND_operadora_telf import *
from moduloFondo.model.choices.choices_model_FND_fondo_telefonos   import * 

class Models_Fnd_Telofonos_Fondo(models.Model):
    operadora = models.ForeignKey(Model_FND_operadora_telf, null=False, blank=False, on_delete=models.CASCADE )
    fijo_movil = models.TextField(max_length=1, null= False, blank=False, choices=TIPO_TELEFONO)
    numero = models.IntegerField(max_length=9, blank=False, null=False)
    activo = models.BooleanField(default=1, choices=BOOLEANS)
    publico = models.BooleanField(default=0, null= False, blank=False, choices=BOOLEANS)
    

    class Meta:
        app_label = "moduloFondo"
        managed = True
        db_table = 'fnd_telefonos_fondo'
        verbose_name = 'Teléfono del fondo'
        verbose_name_plural = 'Teléfonos del fondo'