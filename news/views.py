from django.shortcuts import render
from .models import News


def news_list(request):
    news_items = News.objects.filter(is_published=True).order_by("-created_at")
    return render(request, "news/news_list.html", {"news_items": news_items})
