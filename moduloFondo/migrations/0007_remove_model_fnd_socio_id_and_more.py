# Generated by Django 4.2.1 on 2023-06-17 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduloFondo', '0006_model_fnd_operadora_telf_model_fnd_tipo_descuento_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model_fnd_socio',
            name='id',
        ),
        migrations.AlterField(
            model_name='model_fnd_socio',
            name='id_socio',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
