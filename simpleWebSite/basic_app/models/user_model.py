from django.db import models
from django.db.models.fields import EmailField
from django.forms.widgets import PasswordInput, Widget


class User(models.Model):

    first_name = models.CharField(max_length=64)
    last_name =models.CharField(max_length=64)
    username = models.CharField(max_length=248,unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=264,default=" ")
