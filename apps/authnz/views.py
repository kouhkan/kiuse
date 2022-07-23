from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import SignUpForm


class SignUpView(CreateView):
    template_name = "authnz/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("authnz:signup")
