# Generated by Django 3.1.7 on 2021-04-02 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0001_initial'),
        ('produccion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produccion',
            name='ingrediente',
            field=models.ManyToManyField(to='compras.Ingrediente'),
        ),
    ]