from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

DOCUMENT_CATEGORIES = [
    ("general", "Общие"),
    ("hr", "HR"),
    ("finance", "Финансы"),
    ("legal", "Юридические"),
    ("tech", "Технические"),
]


class Document(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    file = models.FileField(upload_to="documents/", verbose_name="Файл")
    category = models.CharField(
        max_length=50, choices=DOCUMENT_CATEGORIES, verbose_name="Категория"
    )
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата загрузки")
    uploaded_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, verbose_name="Загрузил"
    )

    class Meta:
        verbose_name = "Документ"
        verbose_name_plural = "Документы"
        ordering = ["-uploaded_at"]

    def __str__(self):
        return self.title
