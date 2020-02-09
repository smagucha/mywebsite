from django import forms
from django.forms import ModelForm
from .models import (
    mydatabase, MYPost, incoming_purchase,
    neworderux, newstock, salex, EVENTform
)


class myform(ModelForm):
    class Meta:
        model = mydatabase
        fields = '__all__'


class PostForm(forms.ModelForm):
    class Meta:
        model = MYPost
        fields = '__all__'


class incoming_purchaseform(ModelForm):
    class Meta:
        model = incoming_purchase
        fields = '__all__'


class orderusform(ModelForm):
    class Meta:
        model = neworderux
        fields = '__all__'


class stockform(ModelForm):
    class Meta:
        model = newstock
        fields = '__all__'


class salesform(ModelForm):
    class Meta:
        model = salex
        fields = '__all__'


class salesform(ModelForm):
    class Meta:
        model = salex
        fields = '__all__'


class myevent(ModelForm):
    class Meta:
        model = EVENTform
        fields = '__all__'
