from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.db.models import Q
from sectioncannons.models import *
from sectionpaints.models import Paint
from sectionkits.models import TankKit


class CannonsPageView(View):
    def get(self, request):
        cannons_close = Cannon.objects.filter(category="Ближний бой")
        cannons_short = Cannon.objects.filter(category="Малая дальность")
        cannons_meduim = Cannon.objects.filter(category="Средняя дальность")
        cannons_long = Cannon.objects.filter(category="Большая дальность")

        data = {"close_combat": cannons_close,
                "short_range": cannons_short,
                "medium_range": cannons_meduim,
                "long_range": cannons_long}

        return render(request, "sectioncannons/cannons_main.html", context=data)


class SmokiPageView(View):
    def get(self, request):
        cannon_modifications = Smoki.objects.all()
        resist_paints = Paint.objects.filter(Q(resist_smoky__isnull=False) &
                                             Q(resist_all__isnull=True)).order_by('resist_smoky')

        kits = TankKit.objects.filter(cannon=cannon_modifications[0].cannon)

        data = {"cannon_modifications": cannon_modifications,
                "resist_paints": resist_paints,
                "kits": kits}

        return render(request, "sectioncannons/cannons_smoki.html", context=data)


class FirebirdPageView(View):
    def get(self, request):
        cannon_modifications = Firebird.objects.all()
        resist_paints = Paint.objects.filter(Q(resist_firebird__isnull=False) &
                                             Q(resist_all__isnull=True)).order_by('resist_firebird')

        kits = TankKit.objects.filter(cannon=cannon_modifications[0].cannon)

        data = {"cannon_modifications": cannon_modifications,
                "resist_paints": resist_paints,
                "kits": kits}

        return render(request, "sectioncannons/cannons_firebird.html", context=data)


class TwinsPageView(View):
    def get(self, request):
        cannon_modifications = Twins.objects.all()
        resist_paints = Paint.objects.filter(Q(resist_twins__isnull=False) &
                                             Q(resist_all__isnull=True)).order_by('resist_twins')

        kits = TankKit.objects.filter(cannon=cannon_modifications[0].cannon)

        data = {"cannon_modifications": cannon_modifications,
                "resist_paints": resist_paints,
                "kits": kits}

        return render(request, "sectioncannons/cannons_twins.html", context=data)


class RailgunPageView(View):
    def get(self, request):
        cannon_modifications = Railgun.objects.all()
        resist_paints = Paint.objects.filter(Q(resist_railgun__isnull=False) &
                                             Q(resist_all__isnull=True)).order_by('resist_railgun')

        kits = TankKit.objects.filter(cannon=cannon_modifications[0].cannon)

        data = {"cannon_modifications": cannon_modifications,
                "resist_paints": resist_paints,
                "kits": kits}

        return render(request, "sectioncannons/cannons_railgun.html", context=data)


class HammerPageView(View):
    def get(self, request):
        cannon_modifications = Hammer.objects.all()
        resist_paints = Paint.objects.filter(Q(resist_hammer__isnull=False) &
                                             Q(resist_all__isnull=True)).order_by('resist_hammer')

        kits = TankKit.objects.filter(cannon=cannon_modifications[0].cannon)

        data = {"cannon_modifications": cannon_modifications,
                "resist_paints": resist_paints,
                "kits": kits}

        return render(request, "sectioncannons/cannons_hammer.html", context=data)


class IsidaPageView(View):
    def get(self, request):
        cannon_modifications = Isida.objects.all()
        resist_paints = Paint.objects.filter(Q(resist_isida__isnull=False) &
                                             Q(resist_all__isnull=True)).order_by('resist_isida')

        kits = TankKit.objects.filter(cannon=cannon_modifications[0].cannon)

        data = {"cannon_modifications": cannon_modifications,
                "resist_paints": resist_paints,
                "kits": kits}

        return render(request, "sectioncannons/cannons_isida.html", context=data)


class VulcanPageView(View):
    def get(self, request):
        cannon_modifications = Vulcan.objects.all()
        resist_paints = Paint.objects.filter(Q(resist_vulcan__isnull=False) &
                                             Q(resist_all__isnull=True)).order_by('resist_vulcan')

        kits = TankKit.objects.filter(cannon=cannon_modifications[0].cannon)

        data = {"cannon_modifications": cannon_modifications,
                "resist_paints": resist_paints,
                "kits": kits}

        return render(request, "sectioncannons/cannons_vulcan.html", context=data)


class FreezePageView(View):
    def get(self, request):
        cannon_modifications = Freeze.objects.all()
        resist_paints = Paint.objects.filter(Q(resist_freeze__isnull=False) &
                                             Q(resist_all__isnull=True)).order_by('resist_freeze')

        kits = TankKit.objects.filter(cannon=cannon_modifications[0].cannon)

        data = {"cannon_modifications": cannon_modifications,
                "resist_paints": resist_paints,
                "kits": kits}

        return render(request, "sectioncannons/cannons_freeze.html", context=data)


class ThunderPageView(View):
    def get(self, request):
        cannon_modifications = Thunder.objects.all()
        resist_paints = Paint.objects.filter(Q(resist_thunder__isnull=False) &
                                             Q(resist_all__isnull=True)).order_by('resist_thunder')

        kits = TankKit.objects.filter(cannon=cannon_modifications[0].cannon)

        data = {"cannon_modifications": cannon_modifications,
                "resist_paints": resist_paints,
                "kits": kits}

        return render(request, "sectioncannons/cannons_thunder.html", context=data)


class RicochetPageView(View):
    def get(self, request):
        cannon_modifications = Ricochet.objects.all()
        resist_paints = Paint.objects.filter(Q(resist_ricochet__isnull=False) &
                                             Q(resist_all__isnull=True)).order_by('resist_ricochet')

        kits = TankKit.objects.filter(cannon=cannon_modifications[0].cannon)

        data = {"cannon_modifications": cannon_modifications,
                "resist_paints": resist_paints,
                "kits": kits}

        return render(request, "sectioncannons/cannons_ricochet.html", context=data)


class ShaftPageView(View):
    def get(self, request):
        cannon_modifications = Shaft.objects.all()
        resist_paints = Paint.objects.filter(Q(resist_shaft__isnull=False) &
                                             Q(resist_all__isnull=True)).order_by('resist_shaft')

        kits = TankKit.objects.filter(cannon=cannon_modifications[0].cannon)

        data = {"cannon_modifications": cannon_modifications,
                "resist_paints": resist_paints,
                "kits": kits}

        return render(request, "sectioncannons/cannons_shaft.html", context=data)
