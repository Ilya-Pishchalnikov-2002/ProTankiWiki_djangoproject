from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.HullsPageView.as_view(), name="hulls-main"),
    path("hanter", views.HunterPageView.as_view(), name="hunter"),
    path("vasp", views.VaspPageView.as_view(), name="vasp"),
    path("titan", views.TitanPageView.as_view(), name="titan"),
    path("dictator", views.DictatorPageView.as_view(), name="dictator"),
    path("hornet", views.HornetPageView.as_view(), name="hornet"),
    path("mamont", views.MammothPageView.as_view(), name="mammoth"),
    path("viking", views.VikingPageView.as_view(), name="viking")
]
