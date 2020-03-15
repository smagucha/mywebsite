from django.db import models


class incoming_purchase(models.Model):
    item = models.CharField(max_length=30)
    description = models.TextField()
    delivery = models.CharField(max_length=30)
    numberofitem = models.IntegerField()
    damagegoods = models.IntegerField()
    deliveryofficer = models.CharField(max_length=30)
    receivingofficer = models.CharField(max_length=30)
    expirinv_orderydate = models.CharField(max_length=30)
    invoiceNo = models.CharField(max_length=30)
    receipt = models.CharField(max_length=30)

    def __str__(self):
        return '{}'.format(self.item)

    class Meta:
        verbose_name_plural = 'incoming_purchase'
        permissions = [
            ("Can_view_incoming_purchase", "view incoming_purchase"),
            ("Can_add_incoming_purchase", "add entry to the incoming_purchase"),
            ("Can_change_incoming_purchase", "Can change data in incoming_purchase"),
            ("Can_delete_incoming_purchase", "Can remove data in incoming_purchase"),
        ]
