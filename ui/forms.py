from django.forms import ModelForm
from api.models import StationUnit


class StationForm(ModelForm):
    class Meta:
        model = StationUnit
        fields = ['station_name']

