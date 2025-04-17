from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from core.models import Employee


@login_required
def profile_view(request):
    employee = Employee.objects.filter(user=request.user).first()
    return render(
        request, "users/profile.html", {"user": request.user, "employee": employee}
    )
