from django.forms import ModelForm
from .models import sale


class salesform(ModelForm):
    class Meta:
        model = sale
        fields = '__all__'