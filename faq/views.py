from django.shortcuts import render
from .models import FAQ, FAQ_CATEGORIES
from django.db.models import Q


def faq_list(request):
    faqs = FAQ.objects.all()
    category = request.GET.get("category")
    query = request.GET.get("q")

    if category:
        faqs = faqs.filter(category=category)
    if query:
        faqs = faqs.filter(Q(question__icontains=query) | Q(answer__icontains=query))

    categories = FAQ_CATEGORIES

    return render(
        request,
        "faq/faq_list.html",
        {
            "faqs": faqs,
            "query": query,
            "categories": categories,
            "selected_category": category,
        },
    )
