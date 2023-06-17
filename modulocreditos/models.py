from django.db import models

# Create your models here.
class TipoCredito(models.Model): 
    id = models.BigIntegerField(primary_key=True)
    tipo_credito = models.TextField(unique=True, max_length=100)
