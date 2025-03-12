# Generated by Django 5.1.6 on 2025-03-08 13:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_stationunit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weatherstation',
            name='author',
        ),
        migrations.AddField(
            model_name='weatherstation',
            name='station',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.stationunit'),
        ),
    ]
