from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import SignUpForm, SignInForm


class SignUpView(CreateView):
    template_name = "authnz/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("authnz:signup")


def signin_view(request):
    if request.method == "POST":
        form = SignInForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            if (user := authenticate(request, username=data["username"],
                                     passowrd=data["password"])) is not None:
                login(request, user)
                return redirect(reverse_lazy("authnz:signin"))

        return redirect(reverse_lazy("authnz:signin"))

    form = SignInForm()
    return render(request, "authnz/signin.html", context={"form": form})


@login_required
def signout_view(request):
    logout(request)
    return redirect(reverse_lazy("authnz:signin"))
