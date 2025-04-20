from django.urls import path
from .views import document_list

app_name = "documents"

urlpatterns = [
    path("", document_list, name="list"),
]
