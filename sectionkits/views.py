from django.shortcuts import render
from django.urls import reverse
from django.views import View
from sectionkits.models import ArmamentKit, SupplyKit, TankKit


class KitsPageView(View):
    def get(self, request):
        armkit_list = ArmamentKit.objects.all()
        supplykit_list = SupplyKit.objects.all()
        tankkit_list = TankKit.objects.all()

        data = {"armkit_list": armkit_list,
                "supplykit_list": supplykit_list,
                "kits": tankkit_list}

        return render(request, "sectionkits/kits_main.html", context=data)
