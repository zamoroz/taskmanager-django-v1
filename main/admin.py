from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.task)
admin.site.register(models.task_status)