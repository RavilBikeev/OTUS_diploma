from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from .models import News
from .forms import NewsForm


def is_admin(user):
    return hasattr(user, "employee") and user.employee.is_admin


@login_required
def news_list(request):
    news_items = News.objects.all().order_by("-created_at")
    return render(request, "news/news_list.html", {"news_items": news_items})


@login_required
# @user_passes_test(is_admin)
def create_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("news")
    else:
        form = NewsForm()
    return render(request, "news/news_form.html", {"form": form})


@login_required
# @user_passes_test(is_admin)
def edit_news(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            form.save()
            return redirect("news")
    else:
        form = NewsForm(instance=news)
    return render(request, "news/news_form.html", {"form": form, "edit": True})
