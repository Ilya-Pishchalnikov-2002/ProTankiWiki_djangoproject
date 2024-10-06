from django.shortcuts import render
from django.urls import reverse
from django.views import View


class HomePageView(View):
    def get(self, request):
        return render(request, "main/homepage.html")
