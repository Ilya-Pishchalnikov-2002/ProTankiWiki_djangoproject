from django.shortcuts import render
from django.urls import reverse
from django.views import View
from sectionpaints.models import Paint
from sectionkits.models import TankKit


class PaintsPageView(View):
    def get(self, request):
        paint_list = Paint.objects.all()

        data = {"paint_list": paint_list}

        return render(request, "sectionpaints/paints_main.html", context=data)
