from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.interviews.forms import CreateInterviewForm
from apps.interviews.models import Interview


class CreateInterviewView(LoginRequiredMixin, CreateView):
    template_name = "interviews/index.html"
    model = Interview
    form_class = CreateInterviewForm
    success_url = reverse_lazy("users:index")

    def form_valid(self, form):
        instance = form.save(commit=False)
        setattr(instance, "user", self.request.user)
        return super().form_valid(form)
