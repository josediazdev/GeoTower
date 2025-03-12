from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from .models import WeatherStation
from .serializers import WeatherStationSerializer
from rest_framework_api_key.permissions import HasAPIKey
from api.models import StationUnit


from rest_framework import generics
from django.shortcuts import get_object_or_404
from .models import WeatherStation, StationUnit
from .serializers import WeatherStationSerializer


class WeatherStationListCreate(generics.ListCreateAPIView):
    """
    Vista de API para listar y crear instancias de WeatherStation.

    Permite obtener una lista de todos los datos meteorológicos y crear nuevos datos.
    Al crear, asocia los datos meteorológicos con una estación existente 
    en función de la clave de la estación.
    """

    queryset = WeatherStation.objects.all()
    # Conjunto de consultas que devuelve todos los objetos WeatherStation.

    serializer_class = WeatherStationSerializer
    # Serializador utilizado para convertir los objetos WeatherStation a y desde JSON.

    def perform_create(self, serializer):
        """
        Sobreescribe el método perform_create para asociar los datos meteorológicos con una estación.

        """
        station_key = serializer.validated_data.get('station_key')
        # Obtiene la clave de la estación de los datos validados del serializador.

        station = get_object_or_404(StationUnit, station_key=station_key)
        # Obtiene la instancia de StationUnit correspondiente a la clave de la estación.
        # Devuelve un error 404 si la estación no existe.

        serializer.save(station=station)
        # Guarda los datos meteorológicos en la base de datos, asociándolos con la estación obtenida.
        # Así correspondemos los datos con la estación específica en función de la station_key

    # permission_classes = [HasAPIKey]
    # Deshabilitamos el requerimiento de API KEY para acceder al recurso de listar/crear
    # Descomentar para solicitar API KEY al momento de interactuar con la API en esta vista


class WeatherStationUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = WeatherStation.objects.all()
    serializer_class = WeatherStationSerializer
    lookup_field = "pk"

    permission_classes = [HasAPIKey]
    # Deshabilitamos el requerimiento de API KEY para acceder al recurso de actualizar/borrar
    # Descomentar para solicitar API KEY al momento de interactuar con la API en esta vista
