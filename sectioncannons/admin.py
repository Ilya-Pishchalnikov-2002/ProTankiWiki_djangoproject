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
    list_display = ["modification", "image", "rank_required", "cost",
                    "damage_min", "damage_max", "impact_force", "recoil_force", "reload_speed", "rotation_speed",
                    "max_dmg_range", "min_dmg_range", "weak_dmg_percent", "critical_chance", "critical_damage"]
    ordering = ["modification"]


@admin.register(models.Firebird)
class FirebirdAdmin(admin.ModelAdmin):
    list_display = ["modification", "image", "rank_required", "cost",
                    "damage_hp_sec", "reload_speed", "attack_duration", "rotation_speed",
                    "max_dmg_range", "min_dmg_range", "weak_dmg_percent", "burning_time"]
    ordering = ["modification"]


@admin.register(models.Twins)
class TwinsAdmin(admin.ModelAdmin):
    list_display = ["modification", "image", "rank_required", "cost",
                    "damage_min", "damage_max", "impact_force", "recoil_force", "reload_speed", "rotation_speed",
                    "projectile_speed", "max_dmg_range", "min_dmg_range", "weak_dmg_percent"]
    ordering = ["modification"]


@admin.register(models.Hammer)
class HammerAdmin(admin.ModelAdmin):
    list_display = ["modification", "image", "rank_required", "cost",
                    "damage_shot", "damage_pellet", "impact_force_shot", "impact_force_pellet", "recoil_force",
                    "reload_speed", "reload_speed_clip", "rotation_speed", "max_dmg_range", "min_dmg_range",
                    "weak_dmg_percent", "pellet_count", "spread_angle_vertical", "spread_angle_horizonatal"]
    ordering = ["modification"]


@admin.register(models.Railgun)
class RailgunAdmin(admin.ModelAdmin):
    list_display = ["modification", "image", "rank_required", "cost",
                    "damage_min", "damage_max", "impact_force", "recoil_force", "reload_speed", "shot_delay",
                    "rotation_speed", "penetration_percent"]
    ordering = ["modification"]


@admin.register(models.Isida)
class IsidaAdmin(admin.ModelAdmin):
    list_display = ["modification", "image", "rank_required", "cost",
                    "damage_hp_sec", "healing_hp_sec", "selfhealing_percent", "reload_speed", "attack_duration",
                    "healing_idle_duration", "rotation_speed", "attack_range"]
    ordering = ["modification"]


@admin.register(models.Vulcan)
class VulcanAdmin(admin.ModelAdmin):
    list_display = ["modification", "image", "rank_required", "cost",
                    "damage_hp_sec", "impact_force", "recoil_force", "overheating_time", "self_heating",
                    "self_heat_limit", "barrel_spin_up_time", "barrel_spin_down_time", "rotation_speed",
                    "rotation_deceleration", "max_dmg_range", "min_dmg_range", "weak_dmg_percent"]
    ordering = ["modification"]


@admin.register(models.Thunder)
class ThunderAdmin(admin.ModelAdmin):
    list_display = ["modification", "image", "rank_required", "cost",
                    "damage_min", "damage_max", "impact_force", "impact_force_splash", "recoil_force",
                    "reload_speed", "rotation_speed", "max_dmg_range", "min_dmg_range", "weak_dmg_percent",
                    "max_dmg_radius", "min_dmg_radius", "weak_splash_dmg_percent"]
    ordering = ["modification"]


@admin.register(models.Freeze)
class FreezeAdmin(admin.ModelAdmin):
    list_display = ["modification", "image", "rank_required", "cost",
                    "damage_hp_sec", "reload_speed", "attack_duration", "rotation_speed",
                    "max_dmg_range", "min_dmg_range", "weak_dmg_percent"]
    ordering = ["modification"]


@admin.register(models.Ricochet)
class RicochetAdmin(admin.ModelAdmin):
    list_display = ["modification", "image", "rank_required", "cost",
                    "damage_min", "damage_max", "impact_force", "recoil_force", "reload_speed", "energy_consumption",
                    "charging_speed", "rotation_speed", "projectile_speed", "max_dmg_range", "min_dmg_range",
                    "weak_dmg_percent"]
    ordering = ["modification"]


@admin.register(models.Shaft)
class ShaftAdmin(admin.ModelAdmin):
    list_display = ["modification", "image", "rank_required", "cost",
                    "damage_sniper_min", "damage_sniper_max", "damage_arcade_min", "damage_arcade_max",
                    "impact_force_sniper", "impact_force_arcade", "recoil_force", "reload_speed_arcade",
                    "energy_consumption", "sniper_loading_time", "charging_speed", "rotation_speed",
                    "aiming_speed_horiz", "aiming_speed_vertic", "penetration_percent"]
    ordering = ["modification"]
