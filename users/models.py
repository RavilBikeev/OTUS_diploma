from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "admin", "Администратор"
        HR = "hr", "HR"
        MANAGER = "manager", "Менеджер"
        EMPLOYEE = "employee", "Сотрудник"

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.EMPLOYEE,
    )

    def save(self, *args, **kwargs):
        if self.role in [self.Role.HR, self.Role.MANAGER]:
            self.is_staff = True
        else:
            self.is_staff = False
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} ({self.role})"
