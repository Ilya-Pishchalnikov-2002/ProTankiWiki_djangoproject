from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.CannonsPageView.as_view(), name="cannons-main"),
    path("смоки", views.SmokiPageView.as_view(), name="smoki")
]
