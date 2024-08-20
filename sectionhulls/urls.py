from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.HullsPageView.as_view(), name="hulls-main"),
    path("хантер", views.HunterPageView.as_view(), name="hunter"),
    path("васп", views.VaspPageView.as_view(), name="vasp"),
    path("титан", views.TitanPageView.as_view(), name="titan"),
    path("диктатор", views.DictatorPageView.as_view(), name="dictator"),
    path("хорнет", views.HornetPageView.as_view(), name="hornet"),
    path("мамонт", views.MammothPageView.as_view(), name="mammoth"),
    path("викинг", views.VikingPageView.as_view(), name="viking")
]
