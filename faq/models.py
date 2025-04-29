from django.db import models


FAQ_CATEGORIES = [
    ("general", "Общие вопросы"),
    ("hr", "HR"),
    ("tech", "Технические вопросы"),
    ("finance", "Финансы"),
    ("other", "Другое"),
]


class FAQ(models.Model):
    question = models.CharField(max_length=255, verbose_name="Вопрос")
    answer = models.TextField(verbose_name="Ответ")
    category = models.CharField(
        max_length=50,
        choices=FAQ_CATEGORIES,
        default="general",
        verbose_name="Категория",
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Часто задаваемые вопросы"
        ordering = ["-created_at"]

    def __str__(self):
        return self.question
