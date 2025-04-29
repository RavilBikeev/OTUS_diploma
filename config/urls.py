from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.shortcuts import redirect
from users.views import custom_login_view


urlpatterns = [
    path("", lambda request: redirect("news:list", permanent=False)),
    path("admin/", admin.site.urls),
    path("news/", include("news.urls")),
    path("documents/", include("documents.urls")),
    path("", include("users.urls")),
    path("users/", include("users.urls")),
    path("logout/", LogoutView.as_view(next_page="/login"), name="logout"),
    path("login/", custom_login_view, name="login"),
    path("select2/", include("django_select2.urls")),
    path("employees/", include("core.urls")),
    path("faq/", include("faq.urls", namespace="faq")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
