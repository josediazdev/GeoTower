# Generated by Django 5.1.6 on 2025-03-09 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_stationunit_station_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='weatherstation',
            name='station_key',
            field=models.IntegerField(default=0),
        ),
    ]
