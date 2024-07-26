from django.contrib import admin
from . import models


@admin.register(models.ArmamentKit)
class ArmamentKitAdmin(admin.ModelAdmin):
    list_display = ["name", "image", "discount", "cost", "rank_start", "rank_end", "content"]
    ordering = ["rank_start", "id"]


@admin.register(models.SupplyKit)
class SupplyKitAdmin(admin.ModelAdmin):
    list_display = ["name", "image", "discount", "cost", "rank_start", "rank_end", "supply_count"]
    ordering = ["rank_start", "id"]


@admin.register(models.TankKit)
class TankKitAdmin(admin.ModelAdmin):
    list_display = ["name", "image", "discount", "cost", "rank_start", "rank_end",
                    "cannon", "cannon_modification", "hull", "hull_modification", "paint"]
    ordering = ["rank_start", "id"]
