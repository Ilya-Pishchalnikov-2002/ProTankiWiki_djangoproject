from django.contrib import admin
from . import models


@admin.register(models.Cannon)
class CannonAdmin(admin.ModelAdmin):
    exclude = ["slug_name"]
    list_display = ["name", "slug_name", "image", "category"]
    ordering = ["category"]
