from django.shortcuts import render
from django.urls import reverse
from django.views import View
from sectionhulls.models import *
from sectionkits.models import TankKit


class HullsPageView(View):
    def get(self, request):
        hulls_light = Hull.objects.filter(category="Лёгкий")
        hulls_medium = Hull.objects.filter(category="Средний")
        hulls_heavy = Hull.objects.filter(category="Тяжёлый")

        data = {"light_hulls": hulls_light,
                "medium_hulls": hulls_medium,
                "heavy_hulls": hulls_heavy}

        return render(request, "sectionhulls/hulls_main.html", context=data)


class HunterPageView(View):
    def get(self, request):
        hull_modifications = Hunter.objects.all()

        kits = TankKit.objects.filter(hull=hull_modifications[0].hull)

        data = {"hull_modifications": hull_modifications,
                "kits": kits}

        return render(request, "sectionhulls/hulls_hunter.html", context=data)


class VaspPageView(View):
    def get(self, request):
        hull_modifications = Vasp.objects.all()

        kits = TankKit.objects.filter(hull=hull_modifications[0].hull)

        data = {"hull_modifications": hull_modifications,
                "kits": kits}

        return render(request, "sectionhulls/hulls_vasp.html", context=data)


class TitanPageView(View):
    def get(self, request):
        hull_modifications = Titan.objects.all()

        kits = TankKit.objects.filter(hull=hull_modifications[0].hull)

        data = {"hull_modifications": hull_modifications,
                "kits": kits}

        return render(request, "sectionhulls/hulls_titan.html", context=data)


class DictatorPageView(View):
    def get(self, request):
        hull_modifications = Dictator.objects.all()

        kits = TankKit.objects.filter(hull=hull_modifications[0].hull)

        data = {"hull_modifications": hull_modifications,
                "kits": kits}

        return render(request, "sectionhulls/hulls_dictator.html", context=data)


class HornetPageView(View):
    def get(self, request):
        hull_modifications = Hornet.objects.all()

        kits = TankKit.objects.filter(hull=hull_modifications[0].hull)

        data = {"hull_modifications": hull_modifications,
                "kits": kits}

        return render(request, "sectionhulls/hulls_hornet.html", context=data)


class MammothPageView(View):
    def get(self, request):
        hull_modifications = Mammoth.objects.all()

        kits = TankKit.objects.filter(hull=hull_modifications[0].hull)

        data = {"hull_modifications": hull_modifications,
                "kits": kits}

        return render(request, "sectionhulls/hulls_mammoth.html", context=data)


class VikingPageView(View):
    def get(self, request):
        hull_modifications = Viking.objects.all()

        kits = TankKit.objects.filter(hull=hull_modifications[0].hull)

        data = {"hull_modifications": hull_modifications,
                "kits": kits}

        return render(request, "sectionhulls/hulls_viking.html", context=data)
