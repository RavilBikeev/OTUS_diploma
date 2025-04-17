from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'admin', 'Администратор'
        HR = 'hr', 'HR'
        MANAGER = 'manager', 'Менеджер'
        EMPLOYEE = 'employee', 'Сотрудник'

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.EMPLOYEE,
    )

    def __str__(self):
        return f"{self.username} ({self.role})"
