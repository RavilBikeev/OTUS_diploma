from django.urls import path
from .views import profile_view
from . import views


app_name = "users"

urlpatterns = [
    path("profile/", profile_view, name="profile"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
]
