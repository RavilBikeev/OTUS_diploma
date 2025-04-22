from django import forms
from .models import News, Comment
from django_select2.forms import Select2MultipleWidget


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ["title", "content", "author", "is_published", "tags"]
        widgets = {
            "tags": Select2MultipleWidget(attrs={"data-placeholder": "Выберите теги"}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(
                attrs={"rows": 3, "placeholder": "Напишите комментарий..."}
            )
        }
