from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import DetailView, ListView
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import News, Like, Tag
from .forms import CommentForm, NewsForm


class NewsListView(ListView):
    model = News
    template_name = "news/news_list.html"
    context_object_name = "news_list"

    def get_queryset(self):
        queryset = News.objects.all().order_by("-created_at")
        tag_id = self.request.GET.get("tag")
        if tag_id:
            queryset = queryset.filter(tags__id=tag_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        context["current_tag_id"] = self.request.GET.get("tag")
        return context


def is_admin(user):
    return hasattr(user, "employee") and user.employee.is_admin


@login_required
# @user_passes_test(is_admin)
def create_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("news:list")
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
            return redirect("news:list")
    else:
        form = NewsForm(instance=news)
    return render(request, "news/news_form.html", {"form": form, "edit": True})


@login_required
@require_POST
def like_news(request, pk):
    news = News.objects.get(pk=pk)
    like, created = Like.objects.get_or_create(user=request.user, news=news)
    if not created:
        like.delete()
        liked = False
    else:
        liked = True
    return JsonResponse({"liked": liked, "likes_count": news.likes.count()})


class NewsDetailView(DetailView):
    model = News
    template_name = "news/news_detail.html"
    context_object_name = "news"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        context["comments"] = self.object.comments.select_related("author").order_by(
            "-created_at"
        )
        context["liked_user_ids"] = set(
            self.object.likes.values_list("user_id", flat=True)
        )
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.news = self.object
            comment.save()
        return redirect("news:news_detail", pk=self.object.pk)
