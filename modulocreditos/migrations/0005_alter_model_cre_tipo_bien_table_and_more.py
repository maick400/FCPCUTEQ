# Generated by Django 4.2.1 on 2023-06-18 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moduloCreditos', '0004_model_cre_tipo_bien_atributo'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='model_cre_tipo_bien',
            table='cre_tipo_bien',
        ),
        migrations.AlterModelTable(
            name='model_cre_tipo_bien_atributo',
            table='cre_tipo_bien_atributos',
        ),
    ]
