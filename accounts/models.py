from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # name = models.CharField(max_length=200, blank=True)
    class meta:
        verbose_name = 'profile'

    def __str__(self):
        return str(self.user)
