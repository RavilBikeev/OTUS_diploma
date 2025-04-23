from django.contrib import admin
from .models import Employee, Department


admin.site.register(Department)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("full_name", "position", "department")
    search_fields = ("full_name", "position", "department")
