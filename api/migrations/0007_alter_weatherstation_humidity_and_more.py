# Generated by Django 5.1.6 on 2025-03-09 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_weatherstation_station_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weatherstation',
            name='humidity',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='weatherstation',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='weatherstation',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='weatherstation',
            name='pressure',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='weatherstation',
            name='station_key',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='weatherstation',
            name='temperature',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
