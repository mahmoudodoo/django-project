from django.db import models
from django.contrib.auth.models import User


class UserModel(models.Model):
    username = models.OneToOneField(User ,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=64)
    last_name =models.CharField(max_length=64)
