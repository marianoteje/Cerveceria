# Generated by Django 3.1.7 on 2021-04-10 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0006_auto_20210410_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='produccion',
            name='descripcion',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]
