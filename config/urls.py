from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("news/", include("news.urls")),
    path("documents/", include("documents.urls")),
    path("", include("users.urls")),
    path("users/", include("users.urls")),
    path("logout/", LogoutView.as_view(next_page="/login"), name="logout"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
