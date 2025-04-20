from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    # image = models.ImageField(upload_to="news_images/", blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    news = models.ManyToManyField(News, related_name="tags")

    def __str__(self):
        return self.name
