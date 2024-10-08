from django.contrib import admin
from django.urls import path, include
from main import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.HomePageView.as_view(), name="home"),
    path("cannons/", include("sectioncannons.urls")),
    path("hulls/", include("sectionhulls.urls")),
    path("paints/", include("sectionpaints.urls")),
    path("kits/", include("sectionkits.urls")),
    path("ranks/", include("sectionranks.urls"))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
