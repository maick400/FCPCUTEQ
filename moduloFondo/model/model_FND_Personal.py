from django.db import models
from moduloFondo.model.model_FND_empleado_cargo import Model_FND_Empleado_Cargo
from django.contrib.auth.models import User

class Model_FND_Personal(models.Model):
    id_personal =  models.BigAutoField(primary_key=True)
    id_cargo_empleado = models.ForeignKey(Model_FND_Empleado_Cargo,on_delete=models.CASCADE,null=False, blank=False)
    fecha_ingreso = models.DateField(null=False, blank=False)
    sueldo = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    identificacion = models.CharField(null=False, blank=False, max_length=15,unique=True)
    estado = models.CharField(null=False, blank=False, max_length=3)
    fecha_pago = models.DateField(null=False, blank=False)
    id_usuario = models.ForeignKey(User,on_delete=models.CASCADE,null=False, blank=False)
    total_ahorrado = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    
    
    
    
    class Meta: 
        app_label = "moduloFondo"
        managed = True
        db_table = 'FND_Personal'
        verbose_name = 'un Empleado'
        verbose_name_plural = 'Empleados'