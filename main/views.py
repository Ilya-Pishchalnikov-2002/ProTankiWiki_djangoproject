from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404


class HomePageView(View):
    def get(self, request):
        return render(request, "main/homepage.html")
