from django.urls import path
from . import views
from .views import NewsListView, NewsDetailView


app_name = "news"

urlpatterns = [
    path("", views.NewsListView.as_view(), name="list"),
    path("create/", views.create_news, name="create"),
    path("<int:pk>/edit/", views.edit_news, name="edit"),
    path("<int:pk>/", NewsDetailView.as_view(), name="detail"),
    path("<int:pk>/like/", views.like_news, name="like_news"),
]
