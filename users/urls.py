from django.urls import path
from .views import profile_view, custom_login_view
from . import views
from django.contrib.auth.views import LogoutView


app_name = "users"

urlpatterns = [
    path("profile/", profile_view, name="profile"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
    path("logout/", LogoutView.as_view(next_page="/login"), name="logout"),
]
