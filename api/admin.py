from django.contrib import admin
from .models import WeatherStation, StationUnit


admin.site.register(WeatherStation)
admin.site.register(StationUnit)
