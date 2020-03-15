from django.db import models
from django.urls import reverse


class mydatabase(models.Model):
	firstname =models.CharField(max_length=30)
	surname   =models.CharField(max_length=30)
	lastname   =models.CharField(max_length=30)
	email       =models.EmailField(max_length=100)
	phonenumber =models.CharField(max_length=30)
	country=models.CharField(max_length=30)
	city=models.CharField(max_length=30)
	def __str__(self):
		return "{} {}".format(self.firstname, self.lastname)
		#return '{}'.format(self.id)
	#planning to use in the future
	
	
	class Meta:
		verbose_name_plural='mydatabase'
		"""
		permissions = [
			("Can_view_mydatabase", "view mydatabase"),
			("Can_add_mydatabase", "add entry to the mydatabase"),
			("Can_change_mydatabase", "Can change data in mydatabase"),
			("Can_delete_mydatabase", "Can remove data in mydatabase"),
			]
		"""
	def get_absolute_url(self):
		return reverse('dynamic_lookup_view', kwargs={'id': self.id})


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
"""

content_type = ContentType.objects.get(app_label='mysite', model='mydatabase')
content_type = ContentType.objects.get_for_model(mydatabase)
permission = Permission.objects.create(
	codename='can_publish',
	name='Can_view_mydatabase',
	content_type=content_type,
)

permission = Permission.objects.create(
    codename='Can_view_mydatabase',
    name='view mydatabase',
    content_type=content_type
    )

user = User.objects.get(username=username)
group = Group.objects.get(name='wizard')
group.permissions.add(permission)
user.groups.add(group)
"""
