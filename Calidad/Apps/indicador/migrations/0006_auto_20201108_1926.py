# Generated by Django 3.1.2 on 2020-11-09 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indicador', '0005_auto_20201108_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indicador',
            name='periodicidad',
            field=models.CharField(choices=[('Diaria', 'Diaria'), ('Mensual', 'Mensual')], default='Mensual', max_length=7),
        ),
    ]