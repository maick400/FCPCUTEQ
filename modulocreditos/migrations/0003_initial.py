# Generated by Django 4.2.1 on 2023-06-17 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('modulocreditos', '0002_delete_tipocredito'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoCredito',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('tipo_credito', models.TextField(max_length=100, unique=True)),
            ],
        ),
    ]
