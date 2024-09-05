from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.KitsPageView.as_view(), name="kits-main")
]
