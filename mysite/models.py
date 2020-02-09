from django.db import models
class mydatabase(models.Model):
	firstname =models.CharField(max_length=30)
	surname   =models.CharField(max_length=30)
	lastname   =models.CharField(max_length=30)
	email       =models.EmailField(max_length=100)
	phonenumber =models.CharField(max_length=30)
	city=models.CharField(max_length=30)
	def __str__(self):
		return "{} {}".format(self.firstname, self.lastname)
		#return '{}'.format(self.id)
	class Meta:
		verbose_name_plural='mydatabase'
		permissions = [
			("Can_view_mydatabase", "view mydatabase"),
			("Can_add_mydatabase", "add entry to the mydatabase"),
			("Can_change_mydatabase", "Can change data in mydatabase"),
			("Can_delete_mydatabase", "Can remove data in mydatabase"),
			]
	country=models.CharField(max_length=30)
class MYPost(models.Model):
	title = models.CharField(max_length=20)
	text  = models.TextField()
	class Meta:
		verbose_name_plural = "MYPost"
		permissions = [
			("Can_view_my_post", "view mypost"),
			("Can_add_my_post", "add entry to the mypost"),
			("Can_change_my_post", "Can change data in mypost"),
			("Can_delete_my_post", "Can remove data in mypost"),
			]
class incoming_purchase(models.Model):
	item             =models.CharField(max_length=30)
	description      = models.TextField()
	delivery     = models.CharField(max_length=30)
	numberofitem     = models.IntegerField()
	damagegoods      = models.IntegerField()
	deliveryofficer  = models.CharField(max_length=30)
	receivingofficer = models.CharField(max_length=30)
	expirinv_orderydate       = models.CharField(max_length=30)
	invoiceNo		 = models.CharField(max_length=30)
	receipt          = models.CharField(max_length=30)
	def __str__(self):
		return '{}'.format(self.item)
	class Meta:
		verbose_name_plural='incoming_purchase'
		permissions = [
			("Can_view_incoming_purchase", "view incoming_purchase"),
			("Can_add_incoming_purchase", "add entry to the incoming_purchase"),
			("Can_change_incoming_purchase", "Can change data in incoming_purchase"),
			("Can_delete_incoming_purchase", "Can remove data in incoming_purchase"),
			]
class neworderux	(models.Model):
	Orderper             = models.CharField(max_length=30)
	dateorder            = models.CharField(max_length=30)
	expecteddatedelivery = models.CharField(max_length=30)
	deliveryofficer      = models.CharField(max_length=30)
	invoiceNo            = models.CharField(max_length=30)
	receipt              = models.CharField(max_length=30)
	class Meta:
		verbose_name_plural='neworderux'
		permissions = [
			("Can_view_neworderux", "view neworderux"),
			("Can_add_neworderux", "add entry to the neworderux"),
			("Can_change_neworderux", "Can change data in neworderux"),
			("Can_delete_neworderux", "Can remove data in neworderux"),
			]
class  newstock(models.Model):
	qualityofitem = models.CharField(max_length= 30)
	numberofitem  = models.IntegerField()
	expirydate    = models.CharField(max_length=30)
	officer       = models.CharField(max_length=30)
	class Meta:
		verbose_name_plural='newstock'
		permissions = [
			("Can_view_newstock", "view newstock"),
			("Can_add_newstock", "add entry to the newstock"),
			("Can_change_newstock", "Can change data in newstock"),
			("Can_delete_newstock", "Can remove data innewstock"),
			]
class salex(models.Model):
	buyer        = models.CharField(max_length=30)
	numberofitem = models.IntegerField()
	receipt      = models.CharField(max_length=30)
	stateofgood  = models.CharField(max_length=30)
	class Meta:
		verbose_name_plural='salex'
		permissions = [
			("Can_view_salex", "view salex"),
			("Can_add_salex", "add entry to thesalex"),
			("Can_change_salex", "Can change data in salex"),
			("Can_delete_salex", "Can remove data in salex"),
			]
class EVENTform(models.Model):
	description=models.CharField(max_length=30)
	message=models.TextField()
	class Meta:
		verbose_name_plural='EVENTform'
		permissions = [
			("Can_view_EVENTform", "viewEVENTform"),
			("Can_add_EVENTform", "add entry to the EVENTform"),
			("Can_change_EVENTform", "Can change data in EVENTform"),
			("Can_delete_EVENTform", "Can remove data in EVENTform"),
			]
class customerorder(models.Model):
	numberofitem  = models.IntegerField()
	class Meta:
		verbose_name_plural='customerorder'
		permissions = [
			("Can_view_customerorder", "view customerorder"),
			("Can_add_customerorder", "add entry to the customerorder"),
			("Can_change_customerorder", "Can change data in customerorder"),
			("Can_delete_customerorder", "Can remove data in customerorder"),
			]
