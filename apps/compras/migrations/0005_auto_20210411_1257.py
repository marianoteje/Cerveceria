# Generated by Django 3.1.7 on 2021-04-11 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compras', '0004_auto_20210402_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingrediente',
            name='stock',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7, null=True, verbose_name='Stock en kg'),
        ),
    ]