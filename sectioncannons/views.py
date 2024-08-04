from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from sectioncannons.models import *


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

        data = {"cannon_modifications": cannon_modifications}

        return render(request, "sectioncannons/cannons_smoki.html", context=data)
