from django.db import models


class sale(models.Model):
    buyer = models.CharField(max_length=30)
    numberofitem = models.IntegerField()
    receipt = models.CharField(max_length=30)
    stateofgood = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = 'sale'
        permissions = [
            ("Can_view_sale", "view sale"),
            ("Can_add_sale", "add entry to sale"),
            ("Can_change_sale", "Can change data in sale"),
            ("Can_delete_sale", "Can remove data in sale"),
        ]
