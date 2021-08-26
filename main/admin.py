from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Questions)
admin.site.register(models.Test)
admin.site.register(models.Key)
admin.site.register(models.Grades)
