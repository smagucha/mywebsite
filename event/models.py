from django.db import models


class events(models.Model):
	objects = None
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

