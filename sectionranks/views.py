from django.shortcuts import render
from django.urls import reverse
from django.views import View
from sectionranks.models import Rank
from sectionkits.models import ArmamentKit, SupplyKit, TankKit


class RanksPageView(View):
    def get(self, request):

        rank_list = Rank.objects.all()

        data = {"rank_list": rank_list}
        return render(request, "sectionranks/ranks_main.html", context=data)


class RanksDetailView(View):
    @staticmethod
    def get_prev_next_rank(rank):
        result = []

        query1 = Rank.objects.filter(id=rank.id - 1)
        if query1.exists():
            result.append(query1[0])
        else:
            result.append(None)

        query2 = Rank.objects.filter(id=rank.id + 1)
        if query2.exists():
            result.append(query2[0])
        else:
            result.append(None)

        return result

    def get(self, request, r):
        query = Rank.objects.filter(slug_name=r)

        if query.exists():
            rank_detail = query.get(slug_name=r)
            prev_next = self.get_prev_next_rank(rank_detail)
            arm_kits = ArmamentKit.objects.filter(rank_start=rank_detail.id)
            supply_kits = SupplyKit.objects.filter(rank_start=rank_detail.id)
            kits = TankKit.objects.filter(rank_start=rank_detail.id)

            data = {"rank": rank_detail, "prev_rank": prev_next[0], "next_rank": prev_next[1],
                    "arm_kits": arm_kits, "supply_kits": supply_kits, "kits": kits}
            return render(request, "sectionranks/ranks_detail.html", context=data)

        else:
            data = {"rank": r}
            return render(request, "sectionranks/ranks_no_such_rank.html", context=data)
