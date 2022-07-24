from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView

from apps.interviews.forms import CreateInterviewForm
from apps.interviews.models import Interview


class UserInterviewView(LoginRequiredMixin, DetailView):
    template_name = "interviews/detail.html"
    queryset = Interview.objects.filter(approve=True)


class CreateInterviewView(LoginRequiredMixin, CreateView):
    template_name = "interviews/index.html"
    model = Interview
    form_class = CreateInterviewForm
    success_url = reverse_lazy("users:index")

    def form_valid(self, form):
        instance = form.save(commit=False)
        setattr(instance, "user", self.request.user)
        return super().form_valid(form)
