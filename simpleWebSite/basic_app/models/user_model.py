from django.db import models
from django.db.models.fields import EmailField


class User(models.Model):

    first_name = models.CharField(max_length=64)
    last_name =models.CharField(max_length=64)
    username = models.CharField(max_length=248)
    email = models.EmailField()
    