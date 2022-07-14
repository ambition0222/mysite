from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.User)    # 模型中的User
admin.site.register(models.ConfirmString)