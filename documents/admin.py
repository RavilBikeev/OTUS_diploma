from django.contrib import admin
from .models import Document


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "uploaded_at", "uploaded_by")
    search_fields = ("title", "description")
    list_filter = ("category",)
