from django.urls import path
from . import views
from .views import NewsDetailView


app_name = "news"

urlpatterns = [
    path("", views.news_list, name="list"),
    path("create/", views.create_news, name="create"),
    path("<int:pk>/edit/", views.edit_news, name="edit"),
    path("<int:pk>/", NewsDetailView.as_view(), name="detail"),
]
