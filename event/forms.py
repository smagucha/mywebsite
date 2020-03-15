from django.forms import ModelForm
from .models import  events

class myevent(ModelForm):
	
    class Meta:
        model = events
        fields = '__all__'
