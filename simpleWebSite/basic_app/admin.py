from django.contrib import admin
from basic_app.models import user_model
# Register your models here.

admin.site.register(user_model.UserModel)