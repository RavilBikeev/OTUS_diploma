from django.shortcuts import render
from .models import FAQ, FAQ_CATEGORIES


def faq_list(request):
    faqs = FAQ.objects.all()
    category = request.GET.get("category")
    query = request.GET.get("q")

    if category:
        faqs = faqs.filter(category=category)
    if query:
        faqs = faqs.filter(question__icontains=query)

    return render(
        request,
        "faq/faq_list.html",
        {
            "faqs": faqs,
            "categories": FAQ_CATEGORIES,
            "selected_category": category,
            "search_query": query,
        },
    )
