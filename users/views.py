from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from core.models import Employee
from .forms import UserUpdateForm


@login_required
def profile_view(request):
    employee = Employee.objects.filter(user=request.user).first()
    return render(
        request, "users/profile.html", {"user": request.user, "employee": employee}
    )


@login_required
def edit_profile(request):
    user = request.user
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect("users:profile")
    else:
        form = UserUpdateForm(instance=user)
    return render(request, "users/edit_profile.html", {"form": form})
