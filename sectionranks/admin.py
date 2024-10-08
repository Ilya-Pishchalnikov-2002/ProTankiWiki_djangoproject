from django.contrib import admin
from . import models


@admin.register(models.Rank)
class RankAdmin(admin.ModelAdmin):
    list_display = ["rank_name", "slug_name", "rank_icon", "exp_start", "exp_next", "cry_bonus"]
    ordering = ["id"]
