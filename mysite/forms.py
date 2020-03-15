from django.forms import ModelForm
from .models import mydatabase


class myform(ModelForm):
    class Meta:
        model = mydatabase
        fields = '__all__'
