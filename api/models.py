from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class StationUnit(models.Model):
    station_name = models.CharField(max_length=200, unique=True)
    register_date = models.DateTimeField(default=timezone.now)
    station_key = models.IntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return f"User: {self.author.username}, Station Name: {self.station_name}"


class WeatherStation(models.Model):
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    temperature = models.FloatField(null=True, blank=True)
    humidity = models.FloatField(null=True, blank=True)
    pressure = models.FloatField(null=True, blank=True)
    time = models.DateTimeField(default=timezone.now)
    station_key = models.IntegerField(null=False)
    station = models.ForeignKey(StationUnit, on_delete=models.CASCADE, default=0)


    def __str__(self):
        return f"Station: {self.station.station_name}, Time: {self.time}"
