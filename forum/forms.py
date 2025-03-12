from .models import Response
from django.forms import ModelForm


class ResponseForm(ModelForm):
    class Meta:
        model = Response
        fields = ['response']
