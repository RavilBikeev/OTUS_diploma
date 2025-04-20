from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Document


@login_required
def document_list(request):
    documents = Document.objects.all()
    return render(request, "documents/document_list.html", {"documents": documents})
