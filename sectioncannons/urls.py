from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.CannonsPageView.as_view(), name="cannons-main"),
    path("смоки", views.SmokiPageView.as_view(), name="smoki"),
    path("огнемёт", views.FirebirdPageView.as_view(), name="firebird"),
    path("твинс", views.TwinsPageView.as_view(), name="twins"),
    path("рельса", views.RailgunPageView.as_view(), name="railgun"),
    path("молот", views.HammerPageView.as_view(), name="hammer"),
    path("изида", views.IsidaPageView.as_view(), name="isida"),
    path("вулкан", views.VulcanPageView.as_view(), name="vulcan"),
    path("фриз", views.FreezePageView.as_view(), name="freeze"),
    path("гром", views.ThunderPageView.as_view(), name="thunder"),
    path("рикошет", views.RicochetPageView.as_view(), name="ricochet"),
    path("шафт", views.ShaftPageView.as_view(), name="shaft")
]
