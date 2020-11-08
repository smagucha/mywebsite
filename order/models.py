from django.db import models
from sales.models import sale

class order(models.Model):
    Orderper = models.CharField(max_length=30)
    dateorder = models.CharField(max_length=30)
    expecteddatedelivery = models.CharField(max_length=30)
    deliveryofficer = models.CharField(max_length=30)
    invoiceNo = models.CharField(max_length=30)
    receipt = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'order'
        permissions = [
            ("Can_view_order", "view order"),
            ("Can_add_order", "add entry to the order"),
            ("Can_change_order", "Can change data in order"),
            ("Can_delete_order", "Can remove data in order"),
        ]
