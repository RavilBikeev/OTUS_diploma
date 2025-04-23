from django.db import models
from django.conf import settings
from datetime import date


class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="employee_profile",
    )
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None,
        related_name="employees",
    )
    hire_date = models.DateField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to="employee_photos/", blank=True, null=True)

    @property
    def days_in_company(self):
        if self.hire_date is None:
            return None
        return (date.today() - self.hire_date).days

    def __str__(self):
        return self.full_name
