from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.GunsPageView.as_view(), name="guns-main")
]
