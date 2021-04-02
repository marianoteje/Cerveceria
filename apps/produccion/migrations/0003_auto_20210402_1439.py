# Generated by Django 3.1.7 on 2021-04-02 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0002_produccion_ingrediente'),
    ]

    operations = [
        migrations.AddField(
            model_name='barril',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='fermentado',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='lote',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='produccion',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]
