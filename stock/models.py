from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=200, db_index=True)
	slug = models.SlugField(max_length=200, unique=True)
	class Meta:
		ordering = ('name',)
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name

class product(models.Model):
	category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
	name = models.CharField(max_length = 200)
	description = models.TextField(blank=True)
	storelocation = models.CharField(max_length = 200, blank =True)
	numberofitem  = models.PositiveIntegerField()
	"""
	def get_computed(self):
		finalstock = self.numberofitem
		if final is not isnull:
			finalstock = self.numberofitem - self.quantity
			self.total = finalstock
			return result
		else:
			return ("out of stock")

    def save(self, *args, **kwargs):
    	self.computed = self.get_computed()
    	super(product, self).save(*args, **kwargs)
	"""

	def __str__(self):
		return self.name


	
