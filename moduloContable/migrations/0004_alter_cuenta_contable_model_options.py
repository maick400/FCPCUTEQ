# Generated by Django 4.2.1 on 2023-06-12 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moduloContable', '0003_alter_cuenta_contable_model_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cuenta_contable_model',
            options={'managed': True, 'verbose_name': 'Cuenta Contable', 'verbose_name_plural': 'Cuentas Contables'},
        ),
    ]
