from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from api.models import StationUnit, WeatherStation
from .forms import StationForm
from django.contrib import messages
from tools import get_randnum, get_current_year


def index(request):
    """
    Vista para la página de inicio.

    Redirige a los usuarios autenticados al panel de control y muestra la página
    de inicio para los usuarios no autenticados.

    Returns:
        Si el usuario está autenticado, redirige al panel de control.
        De lo contrario, renderiza la página de inicio.
    """
    if request.user.is_authenticated:
        # Verifica si el usuario está autenticado.

        return redirect('dashboard/')
        # Redirige al usuario autenticado al panel de control.

    context = {'title': 'Start', 'current_year': get_current_year()}
    return render(request, 'ui/start.html', context)


@login_required
def dashboard(request):
    """
    Vista para el panel de control del usuario.

    Muestra las estaciones del usuario, estaciones generales y datos meteorológicos.
    Permite crear nuevas estaciones a través de un formulario.

    Returns:
        Renderiza la página del panel de control con datos de estaciones y un formulario.
    """

    stations = StationUnit.objects.filter(author=request.user).order_by('-register_date')
    # Obtiene las estaciones del usuario actual, ordenadas por fecha de registro descendente.

    general_stations = StationUnit.objects.order_by('-register_date')
    # Obtiene todas las estaciones, ordenadas por fecha de registro descendente.

    weatherstations = WeatherStation.objects.order_by('-time')
    # Obtiene todos los datos meteorológicos, ordenados por tiempo descendente.

    results = []
    # Lista para almacenar los resultados combinados de estaciones y datos meteorológicos.

    for station in general_stations:
        # Itera sobre todas las estaciones generales.
        for weatherstation in weatherstations:
            # Itera sobre todos los datos meteorológicos.
            if station.id == weatherstation.station.id:
                # Si el ID de la estación coincide con el ID de la estación en los datos meteorológicos.

                results.append({
                    'station_id': weatherstation.station.id,
                    'time': weatherstation.time,
                    'latitude': weatherstation.latitude,
                    'longitude': weatherstation.longitude,
                    'temperature': weatherstation.temperature,
                    'humidity': weatherstation.humidity,
                    'pressure': weatherstation.pressure,
                    'station_name': weatherstation.station.station_name,
                })
                # Agrega un diccionario con los datos combinados a la lista de resultados.

                break
                # Rompe el bucle interno después de encontrar una coincidencia.
                # se hace para obtener solo el registro más actualizado a mostrar en el dashboard

    # Al momento de enviar una solicitud POST para almacenar una estación nueva en la base de datos
    if request.method == "POST":
        form = StationForm(request.POST)

        if form.is_valid():

            instance = form.save(commit=False)
            # Guarda el formulario sin guardar en la base de datos todavía.

            # Capitaliza el station_name
            instance.station_name = form.cleaned_data['station_name'].capitalize()

            # Verifying existence
            station_exists = StationUnit.objects.filter(station_name=instance.station_name).exists()

            if station_exists:
                messages.error(request, f'Station name already exists')
                return redirect('ui:dashboard')

            instance.station_key = get_randnum()
            # Genera y asigna una clave de estación aleatoria

            instance.author = request.user
            # Asigna el usuario actual como autor de la estación.

            instance.save()
            # Guarda la estación en la base de datos.

            messages.info(request, f'Station created with ID: {instance.station_key}')

            return redirect('ui:dashboard')

    else:
        form = StationForm()

    context = {
        'form': form,
        'stations': stations,
        'general_stations': general_stations,
        'results': results,
    }

    return render(request, 'ui/dashboard.html', context)


@login_required
def StationDetail(request, station_id):
    stations = StationUnit.objects.filter(author=request.user).order_by('-register_date')
    one_station = get_object_or_404(StationUnit, id=station_id)
    weatherstations_one_station = WeatherStation.objects.filter(station=station_id)

    context = {
            'stations': stations, 
            'one_station': one_station,
            'ws_os': weatherstations_one_station, 
            }

    return render(request, 'ui/station_detail.html', context)


@login_required
def StationDelete(request, station_id):
    stations = StationUnit.objects.filter(author=request.user).order_by('-register_date')
    one_station = get_object_or_404(StationUnit, id=station_id)

    if request.method == "POST":
        one_station.delete()
        messages.success(request, 'Station deleted successfully')
        return redirect('ui:dashboard')

    context = {
            'stations': stations, 
            'one_station': one_station,
            }
    return render(request, 'ui/station_confirm_delete.html', context)


@login_required
def Guides(request):
    return render(request, 'ui/guides.html')
