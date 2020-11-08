from django.db import models
from stock.models import product


class sale(models.Model):
    buyer = models.CharField(max_length=30)
    item = models.ForeignKey(product, related_name='names',on_delete=models.CASCADE)
    phone=models.PositiveIntegerField()
    quantity=models.PositiveIntegerField()
    #stockavailable = models.ForeignKey(product, related_name= 'numberofitem1',on_delete=models.CASCADE, null = True)
    email=models.EmailField()
    available = models.BooleanField(default=True) 

    class Meta:
        verbose_name_plural = 'sale'
        permissions = [
            ("Can_view_sale", "view sale"),
            ("Can_add_sale", "add entry to sale"),
            ("Can_change_sale", "Can change data in sale"),
            ("Can_delete_sale", "Can remove data in sale"),
        ]

