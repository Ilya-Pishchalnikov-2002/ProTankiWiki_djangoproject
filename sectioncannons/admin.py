from django.contrib import admin
from . import models


@admin.register(models.Cannon)
class CannonAdmin(admin.ModelAdmin):
    exclude = ["slug_name"]
    list_display = ["name", "slug_name", "image", "category"]
    list_filter = ["category"]
    ordering = ["name"]


@admin.register(models.Smoki)
class SmokiAdmin(admin.ModelAdmin):
    list_display = ["modification", "image",
                    "damage_min", "damage_max", "impact_force", "recoil_force", "reload_speed", "rotation_speed",
                    "max_dmg_range", "min_dmg_range", "weak_dmg_percent", "critical_chance", "critical_damage",
                    "rank_required", "cost"]
    ordering = ["modification"]


@admin.register(models.Firebird)
class FirebirdAdmin(admin.ModelAdmin):
    list_display = ["modification", "image",
                    "damage_hp_sec", "reload_speed", "attack_duration", "rotation_speed",
                    "max_dmg_range", "min_dmg_range", "weak_dmg_percent", "burning_time",
                    "rank_required", "cost"]
    ordering = ["modification"]
