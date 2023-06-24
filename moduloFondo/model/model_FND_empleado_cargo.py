from django.db import models

class Model_FND_Empleado_Cargo(models.Model):
    id_cargo_empleado =  models.BigAutoField(primary_key=True)
    cargo = models.CharField(max_length=200,  blank=False, null=False)

    class Meta:
        app_label = "moduloFondo"
        managed = True
        db_table = 'fnd_empleado_cargo'
        verbose_name = 'un Cargo'
        verbose_name_plural = 'Cargos'