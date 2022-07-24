from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from .forms import SignUpForm, SignInForm
from .models import User


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User()
            user.username = data["username"]
            user.set_password(data["password"])
            user.email = data.get("email")
            user.save()

            login(request, user)

            return redirect(reverse_lazy("users:index"))

    form = SignUpForm()

    return render(request, "authnz/signup.html", context={"form": form})


def signin_view(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if (user := authenticate(request, **data)) is not None:
                login(request, user)
                return redirect(reverse_lazy("users:index"))

        return redirect(reverse_lazy("authnz:signin"))

    form = SignInForm()

    return render(request, "authnz/signin.html", context={"form": form})


@login_required
def signout_view(request):
    logout(request)
    return redirect(reverse_lazy("authnz:signin"))
