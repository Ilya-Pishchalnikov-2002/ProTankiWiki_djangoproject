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
