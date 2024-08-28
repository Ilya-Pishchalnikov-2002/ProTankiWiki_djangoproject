from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.PaintsPageView.as_view(), name="paints-main"),
    path("<str:p>", views.PaintsDetailView.as_view(), name="paints-detail")
]
