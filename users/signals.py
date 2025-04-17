from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from core.models import Employee
from users.models import User


@receiver(post_save, sender=User)
def create_employee_profile(sender, instance, created, **kwargs):
    if created and instance.role == User.Role.EMPLOYEE:
        Employee.objects.create(user=instance, full_name=instance.get_full_name())
