from django.db import models
class  stock(models.Model):
	qualityofitem = models.CharField(max_length= 30)
	numberofitem  = models.IntegerField()
	expirydate    = models.CharField(max_length=30)
	officer       = models.CharField(max_length=30)

	class Meta:
		verbose_name_plural='stock'
		permissions = [
			("Can_view_newstock", "view newstock"),
			("Can_add_newstock", "add entry to the newstock"),
			("Can_change_newstock", "Can change data in newstock"),
			("Can_delete_newstock", "Can remove data innewstock"),
			]
