from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.User)
admin.site.register(models.Favorite)
admin.site.register(models.Blog)
admin.site.register(models.Keyword)
admin.site.register(models.Blog_Keyword)