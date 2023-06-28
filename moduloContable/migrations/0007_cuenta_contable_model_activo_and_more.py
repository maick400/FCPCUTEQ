# Generated by Django 4.2.1 on 2023-06-14 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduloContable', '0006_alter_cuenta_contable_model_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuenta_contable_model',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='cuenta_contable_model',
            name='cuc_reg',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='cuenta_contable_model',
            name='mayor_movimiento',
            field=models.TextField(default='MAY', max_length=3),
        ),
        migrations.AddField(
            model_name='cuenta_contable_model',
            name='naturaleza',
            field=models.TextField(default='A', max_length=3),
        ),
        migrations.AddField(
            model_name='cuenta_contable_model',
            name='nivel',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='cuenta_contable_model',
            name='nombre_cuenta',
            field=models.TextField(default='', max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='cuenta_contable_model',
            name='codigo',
            field=models.TextField(default='', max_length=30, unique=True),
        ),
    ]