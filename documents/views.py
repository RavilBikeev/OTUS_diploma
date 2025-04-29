from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Document


@login_required
def document_list(request):
    selected_category = request.GET.get("category")
    documents = Document.objects.all()

    if selected_category:
        documents = documents.filter(category=selected_category)

    context = {
        "documents": documents,
        "selected_category": selected_category,
    }
    return render(request, "documents/document_list.html", context)
