from django.forms import ModelForm
from .models import   stock

class stockform(ModelForm):
    class Meta:
        model = stock
        fields = '__all__'