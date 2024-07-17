from django.contrib import admin
from . import models


@admin.register(models.Hull)
class HullAdmin(admin.ModelAdmin):
    exclude = ["slug_name"]
    list_display = ["name", "slug_name", "image", "category"]
    list_filter = ["category"]
    ordering = ["name"]
