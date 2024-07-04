from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404


class CannonsPageView(View):
    def get(self, request):
        return render(request, "sectionguns/cannons_main.html")
