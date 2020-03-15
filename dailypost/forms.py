from django.forms import ModelForm

from .models import dailypost


class PostForm(ModelForm):
    class Meta:
        model = dailypost
        fields = '__all__'
