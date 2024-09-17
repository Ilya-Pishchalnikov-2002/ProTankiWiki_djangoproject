from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.RanksPageView.as_view(), name="ranks-main"),
    path("<str:r>", views.RanksDetailView.as_view(), name="ranks-detail")
]
