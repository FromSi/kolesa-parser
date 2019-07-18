from django.contrib import admin
from . import models


admin.site.register(models.Ad)    # Объявления
admin.site.register(models.Task)  # Задачи

