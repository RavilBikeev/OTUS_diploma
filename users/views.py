from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from core.models import Employee
from .forms import UserUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login


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


def custom_login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("/news")
    else:
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form": form})
