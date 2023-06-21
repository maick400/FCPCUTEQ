from django.db import models

class Model_CNT_Cuenta_Contable(models.Model):

    cuenta_contableCodigo = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.CASCADE)
    nombre_cuenta=models.TextField(null=False,max_length=100,unique=False,blank=False)
    naturaleza=models.TextField(null=False,max_length=100,unique=False,blank=False)
    movimiento_mayor=models.TextField(null=False,max_length=100,unique=False,blank=False)
    nivel=models.SmallIntegerField(null=False,unique=False,blank=False)
    cuc_reg=models.BooleanField(null=False,blank=False,unique=False)
    estado=models.BooleanField(null=False,blank=False,unique=False)

    def __str__(self) -> str:
        return self.nombre_cuenta
    

    class Meta: 
        app_label = "moduloContable"
        managed = True
        db_table = 'CNT_Cuenta_Contable'
        verbose_name = 'un Socio'
        verbose_name_plural = 'Socios'