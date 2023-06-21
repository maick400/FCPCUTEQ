# Generated by Django 4.2.1 on 2023-06-21 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduloFondo', '0009_alter_model_fnd_parametros_sys_correo_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='model_fnd_parametros_sys',
            old_name='tipo_Aportaciion',
            new_name='tipo_Aportacion',
        ),
        migrations.RenameField(
            model_name='model_fnd_parametros_sys',
            old_name='valor_aplicable_aportación',
            new_name='valor_aplicable_aportacion',
        ),
        migrations.AlterField(
            model_name='model_fnd_empleado_cargo',
            name='cargo',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='model_fnd_parametros_sys',
            name='smtp_password',
            field=models.BinaryField(editable=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='model_fnd_socio',
            name='contacto_referencia',
            field=models.CharField(max_length=10),
        ),
    ]