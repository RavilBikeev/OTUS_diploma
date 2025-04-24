from django.views.generic import ListView
from django.db.models import ExpressionWrapper, F, DurationField
from django.db.models.functions import Now
from .models import Employee, Department


class EmployeeListView(ListView):
    model = Employee
    template_name = "core/employees.html"
    context_object_name = "employees"

    def get_queryset(self):
        queryset = (
            super()
            .get_queryset()
            .annotate(
                days_in_company_value=ExpressionWrapper(
                    Now() - F("hire_date"), output_field=DurationField()
                )
            )
        )
        department = self.request.GET.get("department")
        if department:
            queryset = queryset.filter(department=department)
        search_query = self.request.GET.get("q")
        if search_query:
            queryset = queryset.filter(full_name__icontains=search_query)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["departments"] = Department.objects.all()
        department_id = self.request.GET.get("department")
        if department_id:
            context["selected_department"] = Department.objects.filter(
                id=department_id
            ).first()
        else:
            context["selected_department"] = None
        context["search_query"] = self.request.GET.get("q", "")
        return context
