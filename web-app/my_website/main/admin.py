from django.contrib import admin
from .models import Task, SomeInfo
# Register your models here.

admin.site.register(Task)
admin.site.register(SomeInfo)