from django.contrib import admin
from . import models


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(models.Brand, BrandAdmin)
