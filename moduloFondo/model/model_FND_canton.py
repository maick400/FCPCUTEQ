from django.db import models
from moduloFondo.model.model_FND_provincia import *

class Model_Fnd_Canton (models.Model):
    id = models.AutoField(primary_key=True)
    provincia = models.ForeignKey(Model_Fnd_Provincia, on_delete=models.CASCADE)
    codigo = models.TextField( max_length=2 , null= False, blank=False)
    canton = models.TextField(null=False, blank=False, max_length=200)
    
    
    class Meta:
        app_label = "moduloFondo"
        managed = True
        db_table = 'fnd_canton'
        verbose_name = 'Un cantón'
        verbose_name_plural = 'Cantones'