from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.account_information)
admin.site.register(models.blog_content)
admin.site.register(models.favorite_information)
