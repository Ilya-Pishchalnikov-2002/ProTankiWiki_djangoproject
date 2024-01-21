from django.contrib import admin
from django.urls import path, include
from main import views

admin.site.site_header = "Типа моя админка"
admin.site.index_title = "Админка епта"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.HomePageView.as_view(), name="home")
]
