from django.contrib import admin
from . import models


@admin.register(models.Paint)
class HullAdmin(admin.ModelAdmin):
    list_display = ["name", "slug_name", "image_icon", "image_view", "rank_required", "cost", "have_resist",
                    "resist_smoky", "resist_firebird", "resist_twins", "resist_hammer", "resist_railgun",
                    "resist_isida", "resist_vulcan", "resist_thunder", "resist_freeze", "resist_ricochet",
                    "resist_shaft", "resist_mines", "resist_all"]
    ordering = ["rank_required", "id"]
