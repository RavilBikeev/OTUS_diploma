from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import profile_view

app_name = "users"

urlpatterns = [
    path("profile/", profile_view, name="profile"),
]
