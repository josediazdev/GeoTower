from rest_framework import serializers
from .models import WeatherStation

class WeatherStationSerializer(serializers.ModelSerializer):
    """
    Serializador para el modelo WeatherStation.
    Convierte instancias de WeatherStation a y desde formatos JSON/XML.
    """
    class Meta:
        model = WeatherStation
        # Especifica el modelo que se serializará.

        fields = ['latitude', 'longitude', 'temperature', 'humidity', 'pressure', 'time', 'station_key']
        # Especifica los campos del modelo que se incluirán en la serialización.
