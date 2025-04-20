from django.urls import path
from . import views

app_name = "news"

urlpatterns = [
    path("", views.news_list, name="news_list"),
    path("create/", views.create_news, name="create"),
    path("edit/<int:pk>/", views.edit_news, name="edit"),
]
