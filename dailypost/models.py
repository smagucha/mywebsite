from django.db import models


class dailypost(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField()

    class Meta:
        verbose_name_plural = "dailypost"
        permissions = [
            ("Can_view_my_post", "view mypost"),
            ("Can_add_my_post", "add mypost"),
            ("Can_change_my_post", "Can change data in mypost"),
            ("Can_delete_my_post", "Can remove data in mypost"),
        ]
