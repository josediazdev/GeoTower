from django.urls import path
from .views import WeatherStationListCreate, WeatherStationUpdateDestroy

app_name = 'api'
urlpatterns = [
        path('list_create/', WeatherStationListCreate.as_view(), name='list-create' ),
        path('update_destroy/<int:pk>/', WeatherStationUpdateDestroy.as_view(), name='update-destroy' ),
        ]
