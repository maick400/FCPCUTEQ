# Generated by Django 4.2.1 on 2023-06-26 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moduloFondo', '0002_alter_model_fnd_parametros_sys_provincia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model_fnd_parametros_sys',
            name='provincia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduloFondo.model_fnd_provincia'),
        ),
    ]
