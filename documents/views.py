from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Q
from .models import Document, DOCUMENT_CATEGORIES


@login_required
def document_list(request):
    selected_category = request.GET.get("category")
    documents = Document.objects.all()
    query = request.GET.get("q")

    if selected_category:
        documents = documents.filter(category=selected_category)
    if query:
        documents = documents.filter(Q(title__icontains=query))

    categories = DOCUMENT_CATEGORIES

    return render(
        request,
        "documents/document_list.html",
        {
            "documents": documents,
            "categories": categories,
            "query": query,
            "selected_category": selected_category,
        },
    )
