from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import SignUpForm, SignInForm
from .models import User


class SignUpView(CreateView):
    template_name = "authnz/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("authnz:signup")


def signin_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST["username"],
            passowrd=request.POST["password"]
        )

        if user is None:
            return redirect(reverse_lazy("authnz:signin"))

        login(user)
        return redirect(reverse_lazy("authnz:signout"))

    form = SignInForm()
    return render(request, "authnz/signin.html", context={"form": form})
