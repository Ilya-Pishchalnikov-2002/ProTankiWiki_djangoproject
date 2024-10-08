from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.CannonsPageView.as_view(), name="cannons-main"),
    path("smoki", views.SmokiPageView.as_view(), name="smoki"),
    path("ognemet", views.FirebirdPageView.as_view(), name="firebird"),
    path("twins", views.TwinsPageView.as_view(), name="twins"),
    path("relsa", views.RailgunPageView.as_view(), name="railgun"),
    path("molot", views.HammerPageView.as_view(), name="hammer"),
    path("isida", views.IsidaPageView.as_view(), name="isida"),
    path("vulcan", views.VulcanPageView.as_view(), name="vulcan"),
    path("friz", views.FreezePageView.as_view(), name="freeze"),
    path("grom", views.ThunderPageView.as_view(), name="thunder"),
    path("ricoshet", views.RicochetPageView.as_view(), name="ricochet"),
    path("shaft", views.ShaftPageView.as_view(), name="shaft")
]
