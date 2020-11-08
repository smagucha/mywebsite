from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError
from .models import sale
from stock.models import product


class salesform(ModelForm):
	#item = forms.CharField(validators=[validate_slug])
	"""
	value =product.objects.get(id = 1)
	x = value.numberofitem
	print (x)

	def  iszero(value):
		if x == 0:
			raise ValidationError(
				_('%(value)s out of stock'),
				params={'value': value},)
	"""
	
	class Meta:
		model =sale
		fields = '__all__'

	
	"""
	def  iszero(value):
		if value == 0:
			raise ValidationError(
				_('%(value)s out of stock'),
				params={'value': value},)
	
	
    """

#print(value.numberofitem)