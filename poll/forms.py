from django.forms import ModelForm

from .models import Availability

class PollForm(ModelForm):
    class Meta:
        model = Availability
        fields = ['person', 'date', 'available']