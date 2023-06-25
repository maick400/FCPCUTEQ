from django.db import models

class Model_CNT_Cuenta_Contable(models.Model):
    
    codigo_cuenta = models.TextField(primary_key=True)
    cuenta_padre = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=False)
    nombre_cuenta=models.TextField(null=False, blank=False)
    naturaleza=models.TextField(null=False, blank=False)
    movimiento_mayor=models.TextField(null=False, blank=False)
    nivel=models.SmallIntegerField(null=False, blank=False)
    cuc_reg=models.BooleanField(null=False, blank=False)
    activa=models.BooleanField(null=False, blank=False)

    def __str__(self) -> str:
        return self.nombre_cuenta
    

    class Meta: 
        app_label = "moduloContable"
        managed = True
        db_table = 'cnt_cuenta_contable'
        verbose_name = 'un Socio'
        verbose_name_plural = 'Socios'