from django.forms import ModelForm

from .models import   Category, product

class AddCatergory(ModelForm):
	class Meta:
		model = Category
		fields = '__all__'

class AddProduct(ModelForm):
	class Meta:
		model = product
		fields = '__all__'

