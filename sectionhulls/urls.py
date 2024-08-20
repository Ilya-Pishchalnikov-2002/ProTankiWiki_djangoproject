from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.HullsPageView.as_view(), name="hulls-main")
]
