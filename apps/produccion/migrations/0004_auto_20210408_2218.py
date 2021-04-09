# Generated by Django 3.1.7 on 2021-04-09 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produccion', '0003_auto_20210402_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingrediente_Produccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=11, verbose_name='Cantidad de ingredientes usados')),
            ],
        ),
        migrations.AddField(
            model_name='fermentado',
            name='produccion',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to='produccion.produccion'),
        ),
        migrations.AlterField(
            model_name='lote',
            name='id_produccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='produccion.produccion', verbose_name='Produccion'),
        ),
        migrations.AlterField(
            model_name='produccion',
            name='ingrediente',
            field=models.ManyToManyField(to='produccion.Ingrediente_Produccion'),
        ),
    ]
