from django.urls import path
from . import views


app_name = 'ui'
urlpatterns = [
        path('', views.index , name='index' ),
        path('dashboard/', views.dashboard , name='dashboard' ),
        path('dashboard/station/<int:station_id>/', views.StationDetail , name='station-detail' ),
        path('dashboard/station/delete/<int:station_id>/', views.StationDelete , name='station-delete' ),
        path('dashboard/guides/', views.Guides , name='guides' ),
        ]

