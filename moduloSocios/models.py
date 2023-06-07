from django.db import models

# Create your models here.

# ***************************************** TABLAS MAESTRAS *****************************************
class Socio(models.Model):
    id_socio =  models.BigAutoField(primary_key=True)
    cedula = models.CharField(null=False, blank= False, max_length=10, unique=True, verbose_name="Cédula", )
    nombres = models.CharField(max_length=200,  blank=False, null=False)
    genero = models.CharField(max_length=3, blank=False)
    estado_civil = models.CharField(max_length=3, null=False, blank=False)
    direccion = models.CharField(null=False, blank=False, max_length=500)
    fecha_nacimiento = models.DateField(null=False, blank=False)    
    telefono = models.CharField(null=True, blank=True, max_length=16)
    celular = models.CharField(null=False, blank=False, max_length=15)
    email = models.EmailField(null=False, blank=False, unique=True)
    
    def __str__(self) -> str:
        return self.nombres
    
    class Meta: 
        managed = True
        db_table = 'socios'
        verbose_name = 'un Socio'
        verbose_name_plural = 'Socios'

        
        
    
# ***************************************** TRANSACCIONALES *****************************************

    

    