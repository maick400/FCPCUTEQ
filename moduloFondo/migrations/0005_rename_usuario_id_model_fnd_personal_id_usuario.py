# Generated by Django 4.2.1 on 2023-06-17 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moduloFondo', '0004_alter_model_fnd_empleado_cargo_table_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='model_fnd_personal',
            old_name='usuario_id',
            new_name='id_usuario',
        ),
    ]
