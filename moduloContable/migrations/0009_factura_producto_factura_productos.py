# Generated by Django 4.2.1 on 2023-06-14 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moduloContable', '0008_alter_cuenta_contable_model_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('fecha', models.DateField()),
                ('cedula', models.TextField()),
                ('personal', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Producto', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Factura_Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=5)),
                ('descuento', models.DecimalField(decimal_places=2, max_digits=5)),
                ('id_factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduloContable.factura')),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moduloContable.producto')),
            ],
        ),
    ]
