from django.db import models
from moduloFondo.model.model_FND_empleado_cargo import Model_FND_Empleado_Cargo
from moduloFondo.model.choices.choices_FND_Personal import * 
from django.contrib.auth.models import User

class Model_FND_Personal(models.Model):
    id_personal =  models.BigAutoField(primary_key=True)
    id_usuario = models.ForeignKey(User,on_delete=models.CASCADE,null=False, blank=False , verbose_name= 'Usuario', db_column='id_usuario')
    nombres = models.TextField(max_length=300, null=False, blank=False, verbose_name= 'Nombres')
    apellido_paterno = models.TextField(max_length=200, null=False, blank=False ,  verbose_name= 'Apellido Paterno' )
    apellido_materno  = models.TextField(max_length=200, null=False, blank=False, verbose_name='Apellido Materno')
    sexo = models.TextField(max_length=5, null=False, blank=False, choices=SEXO , verbose_name='Sexo')
    foto = models.ImageField(upload_to='moduloFondo/Personal', null=False, blank= False, default='moduloFondo/Personal/user.png', verbose_name='Foto')
    tipo_identificacion = models.TextField(null=False, blank=False, max_length=3, choices = TIPO_IDENTIFICACION, verbose_name='Tipo identificación')
    identificación = models.TextField (null=False, blank=False, max_length=30, verbose_name='Identificación')
    direccion = models.TextField(max_length=500, null=False, blank=False, verbose_name='Dirección')
    activo = models.BooleanField(default=1, null=False, blank=False, choices=BO0LEANS, verbose_name='Activa' )
    fecha_creacion = models.DateField(auto_now_add=True)
    fecha_modificación = models.DateField(null= True, blank= True)
    
    
    class Meta: 
        app_label = "moduloFondo"
        constraints = [ 
                       models.UniqueConstraint(fields=['identificación'], name='un_fnd_personal_identificacion' ),
                       ]
        managed = True
        db_table = 'fnd_personal'
        verbose_name = 'un Empleado'
        verbose_name_plural = 'Empleados'