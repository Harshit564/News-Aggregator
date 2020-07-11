from django.contrib import admin
from news import models

admin.site.register(models.NewsSourceModel)
admin.site.register(models.UrlModel)
admin.site.register(models.CategoryUrlsModel)