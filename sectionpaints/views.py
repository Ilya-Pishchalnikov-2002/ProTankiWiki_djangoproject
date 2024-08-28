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


class PaintsDetailView(View):
    def get(self, request, p):
        query = Paint.objects.filter(slug_name=p)

        if query.exists():
            paint_detail = query.get(slug_name=p)
            kits = TankKit.objects.filter(paint=paint_detail.id)

            data = {"paint": paint_detail,
                    "kits": kits}
            return render(request, "sectionpaints/paints_detail.html", context=data)

        else:
            data = {"paint": p}
            return render(request, "sectionpaints/paints_no_such_paint.html", context=data)
