from django.contrib import admin
from . import models


@admin.register(models.Hull)
class HullAdmin(admin.ModelAdmin):
    list_display = ["name", "slug_name", "image", "category"]
    list_filter = ["category"]
    ordering = ["name"]


@admin.register(models.Hunter)
class HunterAdmin(admin.ModelAdmin):
    list_display = ["modification", "image", "rank_required", "cost",
                    "armor", "max_speed", "turning_speed", "weight", "power"]
    ordering = ["modification"]


@admin.register(models.Vasp)
class VaspAdmin(admin.ModelAdmin):
    list_display = ["modification", "image", "rank_required", "cost",
                    "armor", "max_speed", "turning_speed", "weight", "power"]
    ordering = ["modification"]


@admin.register(models.Titan)
class TitanAdmin(admin.ModelAdmin):
    list_display = ["modification", "image", "rank_required", "cost",
                    "armor", "max_speed", "turning_speed", "weight", "power"]
    ordering = ["modification"]


@admin.register(models.Dictator)
class DictatorAdmin(admin.ModelAdmin):
    list_display = ["modification", "image", "rank_required", "cost",
                    "armor", "max_speed", "turning_speed", "weight", "power"]
    ordering = ["modification"]


@admin.register(models.Hornet)
class HornetAdmin(admin.ModelAdmin):
    list_display = ["modification", "image", "rank_required", "cost",
                    "armor", "max_speed", "turning_speed", "weight", "power"]
    ordering = ["modification"]


@admin.register(models.Mammoth)
class MammothAdmin(admin.ModelAdmin):
    list_display = ["modification", "image", "rank_required", "cost",
                    "armor", "max_speed", "turning_speed", "weight", "power"]
    ordering = ["modification"]


@admin.register(models.Viking)
class VikingAdmin(admin.ModelAdmin):
    list_display = ["modification", "image", "rank_required", "cost",
                    "armor", "max_speed", "turning_speed", "weight", "power"]
    ordering = ["modification"]
