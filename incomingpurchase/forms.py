from django.forms import ModelForm
from .models import incoming_purchase


class incoming_purchaseform(ModelForm):
    class Meta:
        model = incoming_purchase
        fields = '__all__'