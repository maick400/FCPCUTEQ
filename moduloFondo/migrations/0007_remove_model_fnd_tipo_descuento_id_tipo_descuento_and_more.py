# Generated by Django 4.2.1 on 2023-06-28 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moduloFondo', '0006_delete_model_fnd_provincia_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model_fnd_tipo_descuento',
            name='id_tipo_descuento',
        ),
        migrations.AddField(
            model_name='model_fnd_tipo_descuento',
            name='codigo',
            field=models.TextField(default='DESC', max_length=5, primary_key=True, serialize=False),
        ),
    ]
