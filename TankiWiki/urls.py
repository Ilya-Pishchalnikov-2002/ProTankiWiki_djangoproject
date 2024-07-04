from django.contrib import admin
from django.urls import path, include
from main import views
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Типа моя админка"
admin.site.index_title = "Админка епта"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.HomePageView.as_view(), name="home"),
    path("cannons/", include("sectioncannons.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
